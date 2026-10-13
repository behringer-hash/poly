import numpy as np
import pandas as pd

from lead_lag import PM
from live_vs_replay import analyze, orders_table, run_away_ms, would_fill


def pm_top():
    # окно w=1000: ask Up 0.30 до 1000.5 с (сервер), затем 0.36; в момент сигнала Down: bid 0.64 -> цена Down 0.36
    rows = [dict(recv_ms=1000_000 + t + 40, d=40, w=1000, o="U", bid=b, bid_sz=50, ask=a, ask_sz=40)
            for t, b, a in [(0, 0.29, 0.30), (300, 0.35, 0.36)]]
    return pd.DataFrame(rows)


def test_would_fill_and_run_away():
    pm = PM(pm_top())
    t0 = 1000_000 + 100
    assert would_fill(pm, 1000, 1, t0 + 100, 0.33, 5)          # ask 0.30 ещё на месте (сервер до t=300)
    assert not would_fill(pm, 1000, 1, t0 + 250, 0.33, 5)      # на 350 мс уже 0.36 > лимита
    assert abs(run_away_ms(pm, 1000, 1, t0, 0.33) - 200) < 1  # цена убежала через ~200 мс
    assert run_away_ms(pm, 1000, 1, t0, 0.40) == np.inf         # лимит выше всех цен


def test_analyze_agreement(tmp_path):
    d = pd.DataFrame(dict(w=[1000, 1000], sgn=[1, 1], t_ms=[1000_100.0, 1000_100.0], limit=[0.33, 0.33],
                          size=[5, 5], filled_f=[True, False]))
    res = analyze(d, PM(pm_top()), lags=[100, 300])
    t = res["table"].set_index("L")
    assert t.loc[100, "должны_исполниться"] == 1.0 and t.loc[300, "должны_исполниться"] == 0.0
    assert t.loc[100, "согласие"] == 0.5


def test_orders_table(tmp_path):
    pd.DataFrame(dict(sid=[1], variant=["c1"], slug=["btc-updown-5m-1000"], outcome=["Up"], t_signal=[1000.1],
                      mode=["live"], status=["matched"], limit=[0.33], size=[5])
                 ).to_csv(tmp_path / "live_orders_x.csv", index=False)
    pd.DataFrame(dict(sid=[1], slug=["btc-updown-5m-1000"], outcome=["Up"], ask_signal=[0.30], slip_c=[3], edge_c=[3.5],
                      T=[100])).to_csv(tmp_path / "live_order_meta_x.csv", index=False)
    d = orders_table([str(tmp_path)])
    assert d.w.iloc[0] == 1000 and d.sgn.iloc[0] == 1 and d.filled_f.iloc[0] and abs(d.t_ms.iloc[0] - 1000100) < 1e-6
