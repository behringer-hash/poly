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
