"""Реплей на синтетических данных: проверяем направление сигнала, задержку исполнения, якорь и кулдаун."""
import numpy as np
import pandas as pd
import pytest

from lead_lag import PM
from replay import Params, collect_signals, execute, summarize

W = 3000                       # начало окна (кратно 300), секунды
T0 = W * 1000                  # то же в мс


def top(rows):
    """rows: (recv_ms, d, bid, ask, bsz, asz) для токена Up."""
    return pd.DataFrame([dict(recv_ms=r, d=d, w=W, o="U", bid=b, bid_sz=bs, ask=a, ask_sz=az, c=0)
                         for r, d, b, a, bs, az in rows])


def ticks(jump_at=None, jump=0.0, n=120):
    t = T0 + 5000 + np.arange(n) * 1000.0
    px = 100.0 + np.where(np.arange(n) % 2 == 0, 0.5, -0.5)      # шум ±0.5 -> sigma около 1
    if jump_at is not None:
        px = px + np.where(t >= jump_at, jump, 0.0)
    return t, px


def test_up_signal_and_latency_fill_vs_miss():
    t_jump = T0 + 100_000
    # книга стоит 0.49/0.51; через 200 мс после скачка ask уходит на 0.60
    pm_rows = [(T0 + 10_000, 20, .49, .51, 100, 100), (t_jump + 200, 20, .58, .60, 100, 100)]
    pt = top(pm_rows)
    t, px = ticks(t_jump, jump=15.0)
    sigs = collect_signals(pt, t, px, [Params(0.03)])
    ups = [s for s in sigs if s["sgn"] == 1]
    assert ups and not [s for s in sigs if s["sgn"] == -1]
    s = ups[0]
    assert s["t"] == t_jump and s["view"] == pytest.approx(0.51)
    df = execute(sigs, PM(pt), {W: "Up"}, [50, 400])
    fast = df[df.L == 50].iloc[0]
    slow = df[df.L == 400].iloc[0]
    assert fast.fill and fast.px == pytest.approx(0.51) and fast.settle > 40      # выигрыш Up: (1 - .51 - fee)
    assert not slow.fill                                                         # ask уже ушёл на 0.60 > лимита
    # с переплатой 10 ц медленный ордер исполняется по 0.60
    df2 = execute(collect_signals(pt, t, px, [Params(0.03, slip_c=10)]), PM(pt), {W: "Up"}, [400])
    assert df2.iloc[0].fill and df2.iloc[0].px == pytest.approx(0.60)


def test_down_signal_on_drop():
    t_jump = T0 + 100_000
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100)])
    t, px = ticks(t_jump, jump=-15.0)
    sigs = collect_signals(pt, t, px, [Params(0.03)])
    assert sigs and all(s["sgn"] == -1 for s in sigs)
    assert sigs[0]["view"] == pytest.approx(1 - 0.49)        # ask Down = 1 - bid Up


def test_anchor_resets_when_book_reprices():
    t_jump = T0 + 100_000
    # книга отыграла скачок через 100 мс: mid изменился -> якорь сдвинулся, повторных сигналов нет
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100), (t_jump + 100, 20, .72, .74, 100, 100)])
    t, px = ticks(t_jump, jump=15.0)
    sigs = collect_signals(pt, t, px, [Params(0.03)])
    assert [s["t"] for s in sigs] == [t_jump]                # только первый тик скачка, до репрайсинга


def test_cooldown_limits_repeated_signals():
    t_jump = T0 + 100_000
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100)])
    t, px = ticks(t_jump, jump=15.0)
    s1 = collect_signals(pt, t, px, [Params(0.03, cooldown_s=1.0)])
    s60 = collect_signals(pt, t, px, [Params(0.03, cooldown_s=60.0)])
    assert len(s60) < len(s1) and len(s60) >= 1


def test_no_signal_on_noise_and_thin_size_is_miss():
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 2)])         # на ask всего 2 шейра
    t, px = ticks()
    assert collect_signals(pt, t, px, [Params(0.03)]) == []
    t2, px2 = ticks(T0 + 100_000, 15.0)
    sigs = collect_signals(pt, t2, px2, [Params(0.03)])
    df = execute(sigs, PM(pt), {W: "Up"}, [50])
    assert sigs and not df.fill.any()                        # min_fill = 5, а объёма 2


def test_summarize_shapes():
    t_jump = T0 + 100_000
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100)])
    t, px = ticks(t_jump, 15.0)
    df = execute(collect_signals(pt, t, px, [Params(0.03)]), PM(pt), {W: "Up"}, [50, 300])
    out = summarize(df, n_boot=50)
    assert set(out.L) == {50, 300} and (out.исполн >= 0).all()


def _engine_vs_replay(pt, t, px, winners, thr=0.03):
    """Сигналы настоящего движка paper.py (виртуальное время) и упрощённого реплея должны совпасть."""
    import paper_replay as pr
    res = pr.run(None, {"src": (t, px)}, "src", pr.parse_variants(f"v:{thr}:src"), [50, 400], winners, pm_top=pt)
    eng = res["paper_signals"]
    mine = collect_signals(pt, t, px, [Params(thr)])
    a = sorted((round(r.recv * 1000), 1 if r.outcome == "Up" else -1) for r in eng.itertuples())
    b = sorted((round(s["t"]), s["sgn"]) for s in mine)
    return a, b, res


def test_real_engine_matches_replay_signals_and_fills():
    t_jump = T0 + 100_000
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100), (t_jump - 300, 20, .49, .51, 100, 90),   # свежая книга (движок: не старше 2 с)
              (t_jump + 200, 20, .58, .60, 100, 100)])
    t, px = ticks(t_jump, jump=15.0)
    a, b, res = _engine_vs_replay(pt, t, px, {W: "Up"})
    assert a == b and a                                   # те же сигналы в те же миллисекунды
    fl = res["paper_fills"].set_index("latency_ms")
    assert fl.loc[50, "status"] == "fill" and fl.loc[400, "status"] == "miss"
    # движок проверяет исполнение по локальной копии книги (view="rcv"), реплей с view="rcv" даёт то же
    df = execute(collect_signals(pt, t, px, [Params(0.03)]), PM(pt), {W: "Up"}, [50, 400], view="rcv")
    assert list(df.sort_values("L").fill) == [True, False]


def test_book_lag_filter_matches_engine():
    t_jump = T0 + 100_000
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100), (t_jump - 500, 900, .49, .51, 100, 100)])   # лаг ленты 900 мс
    t, px = ticks(t_jump, jump=15.0)
    a, b, _ = _engine_vs_replay(pt, t, px, {W: "Up"})
    assert a == b == []                                   # по отставшей книге не торгуем ни движок, ни реплей


def test_early_exit_sells_at_bid_with_fees():
    t_jump = T0 + 100_000
    # после скачка ask остаётся 0.51, а через 3 с книга переоценивается: bid 0.70 / ask 0.72
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100), (t_jump + 3_000, 20, .70, .72, 100, 100)])
    t, px = ticks(t_jump, jump=15.0)
    sigs = collect_signals(pt, t, px, [Params(0.03)])
    df = execute(sigs, PM(pt), {W: "Up"}, [50], exit_s=(1, 5), exit_ms=200)
    r = df.iloc[0]
    assert r.fill and r.px == pytest.approx(0.51)
    fee_in, fee_out = 0.07 * .51 * .49, 0.07 * .70 * .30
    assert r["x5"] == pytest.approx((0.70 - 0.51 - fee_in - fee_out) * 100)    # продали по bid 0.70
    assert r["x1"] < r["x5"]                                                    # через 1 с переоценки ещё нет
    from replay import summarize_exit
    assert not summarize_exit(df, (1, 5), n_boot=20).empty


def test_read_skips_empty_files(tmp_path):
    from lead_lag import read
    (tmp_path / "windows_00.csv").write_text("")                              # свежесозданный пустой файл
    (tmp_path / "windows_01.csv").write_text("slug,start\na,1\n")
    assert list(read(str(tmp_path), "windows").slug) == ["a"]
    assert read(str(tmp_path), "nothing").empty


def test_overpay_modes_buy_more_levels_of_price():
    from replay import parse_slips, slip_extra_c, slip_label
    t_jump = T0 + 100_000
    # ask 0.51 уходит на 0.55 через 200 мс: без переплаты - промах, с переплатой 5 ц - покупка по 0.55
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100), (t_jump + 200, 20, .53, .55, 100, 100)])
    t, px = ticks(t_jump, jump=15.0)
    sigs = collect_signals(pt, t, px, [Params(0.03)])
    sl = parse_slips("0,5,e:1:1:8")
    assert [slip_label(x) for x in sl] == ["slip0", "slip5", "edge1m1c8"]
    df = execute(sigs, PM(pt), {W: "Up"}, [400], slips=sl, exit_s=(5,))
    by = df.groupby("slip").fill.max()
    assert not by["slip0"] and by["slip5"]
    assert df[df.slip == "slip5"].iloc[0].px == pytest.approx(0.55)
    # переплата от силы сигнала: edge 0.097 -> floor(9.7*1 - 1) = 8 ц, но не больше потолка
    assert slip_extra_c(("edge", 1.0, 1.0, 8.0), 0.097) == 8
    assert slip_extra_c(("edge", 1.0, 1.0, 8.0), 0.015) == 0
    from replay import slip_report
    assert not slip_report(df, (5,)).empty
