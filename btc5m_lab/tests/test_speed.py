import numpy as np
import pandas as pd

from lead_lag import PM
from replay import execute, parse_slips
from speed_compare import cluster_table, clusters, fires
from trade_jump import jump_signals

W0 = 3000
T0 = W0 * 1000


def test_fires_up_down_and_refractory():
    t = np.arange(0, 6000, 100.0)
    px = np.full(len(t), 100.0)
    px[20:] += 12.0                      # скачок вверх на 12 в момент 2000 мс
    px[45:] -= 15.0                      # вниз на 15 в 4500 мс
    f = fires(t, px, N=10, W=500)
    assert [(round(x), d) for x, d in f] == [(2000, 1), (4500, -1)]
    assert fires(t, px, N=20, W=500) == []          # такого скачка нет
    # медленный дрейф по 1 за 100 мс: за окно 500 мс набирается 5 < 10
    assert fires(t, 100 + np.arange(len(t)) * 1.0, N=10, W=500) == []


def test_clusters_first_source_and_delays():
    ev = [(1000.0, 1, "a"), (1040.0, 1, "b"), (1150.0, 1, "c"), (9000.0, -1, "a"), (9100.0, -1, "b")]
    cl = clusters(ev, span=2000)
    assert len(cl) == 2 and cl[0] == {"a": 1000.0, "b": 1040.0, "c": 1150.0}
    tab = cluster_table(cl, ["a", "b"]).set_index("источник")
    assert tab.loc["a", "первый_доля"] == 1.0 and tab.loc["b", "мед_отставание_мс"] == 70.0
    tab = cluster_table(cl, ["a", "b", "c"]).set_index("источник")
    assert tab.loc["c", "общих_событий"] == 1 and tab.loc["c", "покрытие_событий"] == 0.5


def _pm():
    rows = [dict(recv_ms=T0 + 5000 + i * 1000, d=40, w=W0, o="U", bid=0.49, bid_sz=50, ask=0.50, ask_sz=50, c=0)
            for i in range(60)]
    rows[20].update(bid=0.60, ask=0.61)                 # цена Up уехала через 15 с (на 20-й секунде)
    return PM(pd.DataFrame(rows))


def test_jump_signals_and_execute():
    pm = _pm()
    t = T0 + 5000 + np.arange(0, 30000, 100.0)
    px = np.full(len(t), 100.0)
    px[100:] += 20.0                                    # скачок вверх на 10 с
    sigs = jump_signals(pm, t, px, N=10, W_ms=500, cooldown_s=2.0)
    assert len(sigs) == 1 and sigs[0]["sgn"] == 1 and abs(sigs[0]["view"] - 0.50) < 1e-9
    df = execute(sigs, pm, {W0: "Up"}, [300], slips=parse_slips("3"))
    assert df.iloc[0].fill and abs(df.iloc[0].px - 0.50) < 1e-9


def test_read_drops_repeated_headers(tmp_path):
    from lead_lag import read
    (tmp_path / "windows_a.csv").write_text("start,official_winner\n3000,Up\nstart,official_winner\n3300,Down\n")
    (tmp_path / "by_trade_a.csv").write_text("recv_ms,T,price\n1,1,100.5\nrecv_ms,T,price\n2,2,101.5\n")
    d = read(str(tmp_path), "windows")
    assert d.start.astype(int).tolist() == [3000, 3300] and d.official_winner.tolist() == ["Up", "Down"]
    t = read(str(tmp_path), "by_trade", ["recv_ms", "price"])
    assert t.recv_ms.tolist() == [1, 2] and t.price.tolist() == [100.5, 101.5] and t.recv_ms.dtype != object


def test_calibration_states(tmp_path):
    import calibration
    w = 3000
    t0 = w * 1000
    pm_rows = [dict(recv_ms=t0 + i * 1000, d=40, w=w, o="U", bid=0.69, bid_sz=50, ask=0.70, ask_sz=50, c=0) for i in range(0, 300)]
    pd.DataFrame(pm_rows).to_csv(tmp_path / "pm_top_a.csv", index=False)
    pd.DataFrame([dict(slug=f"btc-updown-5m-{w}", start=w, official_winner="Up", ptb_twap=100.0)]).to_csv(tmp_path / "windows_a.csv", index=False)
    ticks = [dict(recv_ms=t0 + i * 500, price=100.0 + 5 + (i % 2)) for i in range(0, 600)]      # цена выше ptb на ~5
    pd.DataFrame(ticks).to_csv(tmp_path / "by_trade_a.csv", index=False)
    d = calibration.build_states(str(tmp_path), "bybit_trade", L=300, step=10)
    up = d[d.sgn == 1]
    assert len(up) > 10 and (up.won == 1).all() and (up.zs > 0).all()
    assert abs(up.pnl.iloc[0] - 100 * (1 - 0.70 - 0.07 * 0.7 * 0.3)) < 1e-6
    down = d[d.sgn == -1]
    assert (down.won == 0).all() and (down.zs < 0).all()
    m, lo, hi = calibration.boot_ci(up)
    assert m > 0


def test_momentum_events_and_logit(tmp_path):
    import momentum_features as mf
    w = 3000
    t0 = w * 1000
    pm_rows = [dict(recv_ms=t0 + i * 500, d=40, w=w, o="U", bid=0.49, bid_sz=50, ask=0.50, ask_sz=50, c=0) for i in range(0, 600)]
    for r in pm_rows[100:]:
        r.update(bid=0.59, ask=0.60)                       # после скачка (t0+50 с) Up дороже
    pd.DataFrame(pm_rows).to_csv(tmp_path / "pm_top_a.csv", index=False)
    pd.DataFrame([dict(slug=f"btc-updown-5m-{w}", start=w, official_winner="Up", ptb_twap=100.0)]).to_csv(tmp_path / "windows_a.csv", index=False)
    px = np.full(600, 100.0) + (np.arange(600) % 2) * 0.1
    px[100:] += 20.0                                       # скачок вверх на 20 в момент +50 с
    pd.DataFrame(dict(recv_ms=t0 + np.arange(600) * 500, price=px)).to_csv(tmp_path / "by_trade_a.csv", index=False)
    ev = mf.build_events(str(tmp_path), "bybit_trade", N=10, W=500, L=300)
    assert len(ev) == 1 and ev.dir.iloc[0] == 1 and abs(ev.ask.iloc[0] - 0.60) < 1e-9 and ev.won.iloc[0] == 1.0
    assert ev.jump.iloc[0] >= 10 and ev.z0.iloc[0] > 0 and abs(ev.rep1.iloc[0] - 10.0) < 1e-6 or ev.rep1.iloc[0] > 0
    # логистическая модель находит признак, который сдвигает исход
    rng = np.random.default_rng(0)
    x = rng.normal(size=4000)
    ask = rng.uniform(0.3, 0.7, 4000)
    y = (rng.uniform(size=4000) < 1 / (1 + np.exp(-(mf.logit(ask) + 1.0 * x)))).astype(float)
    b0, beta = mf.fit_logit(x[:, None], y, mf.logit(ask), l2=1.0)
    assert 0.8 < beta[0] < 1.2 and abs(b0) < 0.15


def test_first_pass_and_auc_and_weights():
    import reprice_timing as rt
    import fill_predict as fp
    t = np.array([0.0, 100.0, 200.0, 300.0])
    p = np.array([0.50, 0.50, 0.60, 0.70])
    assert rt.first_pass(t, p, 50.0, 0.50) == 150.0           # цена выше 0.50 впервые в момент 200
    assert rt.first_pass(t, p, 250.0, 0.50) == 0.0            # к моменту 250 уже выше
    assert np.isinf(rt.first_pass(t, p, 0.0, 0.80))           # выше 0.80 не будет
    assert rt.at(t, p, 150.0) == 0.50 and np.isnan(rt.at(t, p, -1.0))
    assert fp.auc(np.array([0, 0, 1, 1]), np.array([0.1, 0.2, 0.8, 0.9])) == 1.0
    assert abs(fp.auc(np.array([0, 1, 0, 1]), np.array([0.5, 0.5, 0.5, 0.5])) - 0.5) < 1e-9
    Ls, w = fp.lat_weights(pd.DataFrame(dict(total_ms=[300.0, 310.0, 320.0, 900.0])))
    assert abs(w.sum() - 1.0) < 1e-9 and len(Ls) == len(w)


def test_filter_portfolio_helpers():
    import filter_portfolio as fpf
    assert list(fpf.to_grid(np.array([225.0, 1300.0, 290.0]))) == [0, len(fpf.LS) - 1, fpf.LS.index(300)]
    n = 6
    sig = pd.DataFrame(dict(w=[3000] * n, t=[3000_000.0 + 10_000 * i for i in range(n)], sgn=[1] * n, arrive=[True, True, True, True, True, False]))
    rows = []
    for i in range(n):
        for L in fpf.LS:
            rows.append(dict(w=3000, t=sig.t[i], sgn=1, L=L, fill=(L <= 300), px=0.5, qty=5.0, settle=100 * (1 - 0.5 - 0.02), limit=0.53, tgt=5.0, edge=0.04))
    ex = pd.DataFrame(rows)
    tab = fpf.make_table(sig, ex)
    pool_idx = fpf.to_grid(np.array([225.0, 275.0]))              # всегда L <= 300: исполняется
    rng = np.random.default_rng(0)
    d = fpf.draw(sig, tab, np.ones(n, bool), pool_idx, rng)
    assert d.fill.tolist() == [True] * 5 + [False]                  # шестой неисполним при приходе
    r = fpf.simulate(sig, tab, np.ones(n, bool), pool_idx, draws=3)
    assert r["исполн"] > 0 and r["pnl"] > 0
    pool_late = fpf.to_grid(np.array([1200.0]))                     # всегда поздно: не исполняется
    assert fpf.simulate(sig, tab, np.ones(n, bool), pool_late, draws=3)["исполн"] == 0
