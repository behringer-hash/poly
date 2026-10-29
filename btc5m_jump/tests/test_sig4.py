"""Стратегия 4: деревья модели, сетка BTC, данные окна, признаки, решения триггера и досрочное снятие заявок."""
import math
import os

import numpy as np

import sig4
import sig4_model as M
from sig4 import Sig4Trigger
import asyncio

from test_live_maker import Client, W, sig as msig, trader

NAN = float("nan")


# ----------------------------------------------------------------------------- деревья
def _npz(tmp_path):
    """Два дерева: 1) mid <= 0.5 -> +1, иначе (и nan) -> +2; 2) dbnf03 <= 0 -> -0.5, nan -> влево."""
    f = M.FEATS
    feat = [f.index("mid"), 0, 0, f.index("dbnf03"), 0, 0]
    thr = [0.5, 0, 0, 0.0, 0, 0]
    left = [1, 0, 0, 4, 0, 0]
    right = [2, 0, 0, 5, 0, 0]
    leaf = [False, True, True, False, True, True]
    val = [0, 1.0, 2.0, 0, -0.5, 0.25]
    mleft = [False, False, False, True, False, False]
    p = os.path.join(tmp_path, "t.npz")
    np.savez_compressed(p, base=np.array(0.1), feats=np.array(f), feat=np.array(feat), thr=np.array(thr, float),
                        left=np.array(left), right=np.array(right), leaf=np.array(leaf), val=np.array(val, float),
                        mleft=np.array(mleft), root=np.array([0, 3]))
    return p


def test_trees_predict_row(tmp_path):
    t = M.Trees(_npz(str(tmp_path)))
    x = [NAN] * len(M.FEATS)
    x[M.FEATS.index("mid")] = 0.4
    x[M.FEATS.index("dbnf03")] = 3.0
    assert abs(t.predict_row(x) - (0.1 + 1.0 + 0.25)) < 1e-12
    x[M.FEATS.index("mid")] = NAN                       # nan в первом дереве -> вправо, во втором - влево
    x[M.FEATS.index("dbnf03")] = NAN
    assert abs(t.predict_row(x) - (0.1 + 2.0 - 0.5)) < 1e-12


def test_real_model_loads():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    t = M.Trees(os.path.join(here, "models", "sig3s_v2.npz"))
    assert t.n_trees > 50
    assert math.isfinite(t.predict_row([0.5] * len(M.FEATS)))


# ----------------------------------------------------------------------------- сетка BTC
def test_grid_series_cells():
    w = 999_900
    g = M.GridSeries()
    gb0 = (w - 20) * 1000.0
    g.add(gb0 - 50, 100.0)            # до сетки - даёт значение первой ячейке
    g.add(gb0 + 150, 101.0)           # между ячейками 1 и 2
    g.add(gb0 + 200, 102.0)           # ровно в ячейке 2
    g.start_window(w)
    g.close_upto(gb0 + 250)
    assert list(g.vals[:3]) == [100.0, 100.0, 102.0]
    assert g.k == 3 and math.isnan(g.vals[3])
    g.add(gb0 + 120, 999.0)           # опоздавшая сделка в закрытые ячейки - игнорируется
    g.add(gb0 + 310, 103.0)
    g.close_upto(gb0 + 400)
    assert list(g.vals[3:5]) == [102.0, 103.0]


def test_grid_series_new_window_rebuilds_from_history():
    w = 999_900
    g = M.GridSeries()
    g.start_window(w - 300)
    for i in range(0, 3300):          # сделка каждые 100 мс с T-320 с
        g.add((w - 320) * 1000.0 + 100 * i, 50000.0 + i)
    g.close_upto((w - 30) * 1000.0)   # прошлое окно уже прочитало эти сделки
    g.start_window(w)                 # новое окно: ячейки с T-20 с восстанавливаются из истории
    g.close_upto((w - 19) * 1000.0)
    assert g.vals[0] == 53000.0 and g.vals[10] == 53010.0


# ----------------------------------------------------------------------------- данные окна
def test_windata_book_and_flow():
    wd = M.WinData(1000)
    wd.add_top(1000_100.0, 0.49, 0.51, 100, 50)
    wd.add_top(1000_050.0, 0.48, 0.50, 10, 20)        # не по порядку
    assert wd.book_at(1000_060.0) == (0.48, 0.50, 10.0, 20.0)
    assert wd.book_at(1000_100.0) == (0.49, 0.51, 100.0, 50.0)
    assert all(math.isnan(v) for v in wd.book_at(1000_000.0))
    wd.add_trade(1000_500.0, 5.0)
    wd.add_trade(1000_200.0, -2.0)                     # не по порядку
    wd.add_trade(1001_300.0, 7.0)
    assert wd.flow(1001_300.0, 1000.0) == 12.0         # (300, 1300] -> 5 + 7
    assert wd.flow(1001_300.0, 5000.0) == 10.0


def _setup(w=999_900, up_moves=None, book=(0.49, 0.51)):
    """Окно w: книга стоит, BTC (три биржи) - сделка каждые 100 мс с T-25 с, в конце ход up_moves[c] за 0,3 с."""
    wd = M.WinData(w)
    wd.add_top((w - 1) * 1000.0, book[0], book[1], 300, 200)
    G = {c: M.GridSeries() for c in ("bnf", "by", "cb", "cl")}
    t_end = (w + 60) * 1000.0
    for c, g in G.items():
        base = 60000.0 if c != "cl" else 60010.0
        T, i = (w - 25) * 1000.0, 0
        while T <= t_end:
            px = base + (0.5 * (i % 4) if T < t_end - 5000 else 0.0)   # колебания для σ; последние 5 с - ровно
            if up_moves and c in up_moves and T > t_end - 300:
                px = base + up_moves[c]
            g.add(T, px)
            T += 100.0
            i += 1
        g.start_window(w)
        g.close_upto(t_end)
    return wd, G


def test_features_fresh_and_lags():
    w = 999_900
    wd, G = _setup(w, up_moves={"by": 4.0, "cb": -1.0})
    row, up, dn = M.features_at(60.0, wd, 60000.0, {c: G[c] for c in ("bnf", "by", "cb")}, G["cl"])
    f = dict(zip(M.FEATS, row))
    assert f["mid"] == 0.5 and abs(f["spr"] - 2.0) < 1e-9 and f["t"] == 60.0
    assert f["dby03"] == 4.0 and f["dcb03"] == -1.0 and f["dbnf03"] == 0.0
    assert up == 4.0 and dn == 1.0
    assert f["dm1"] == 0.0 and f["fl1"] == 0.0
    assert 0.5 < f["fair"] < 1.0 and abs(f["dk"] - 10.0) < 1e-6      # базис Chainlink - фьючерс = +10 (медиана)
    # ранние точки сетки: лаги раньше t=3 с - nan, как при обучении
    row, _, _ = M.features_at(3.2, wd, 60000.0, {c: G[c] for c in ("bnf", "by", "cb")}, G["cl"])
    f = dict(zip(M.FEATS, row))
    assert f["dm03"] != f["dm03"] and f["dm1"] != f["dm1"] and f["dbnf03"] != f["dbnf03"]


# ----------------------------------------------------------------------------- триггер
class FakeClock:
    def __init__(self, t):
        self.t = t

    def now(self):
        return self.t


class FBook:
    def __init__(self, bb, ba):
        self.bb, self.ba = bb, ba
        self.bids, self.asks = {bb: 100.0}, {ba: 100.0}


class FWin:
    def __init__(self, start, up=(0.49, 0.51)):
        self.start, self.end, self.slug = start, start + 300, f"btc-updown-5m-{start}"
        self.book_lag_ms, self.ptb = 20.0, 60000.0
        self.books = {"Up": FBook(*up), "Down": FBook(round(1 - up[1], 2), round(1 - up[0], 2))}

    def ready(self):
        return True


class FPM:
    def __init__(self, win):
        self.windows, self.offset_ms, self.win = {win.start: win}, 0.0, win

    def current_window(self, now):
        return self.win


class ConstTrees:
    path, n_trees = "const.npz", 1

    def __init__(self, v):
        self.v = v

    def predict_row(self, x):
        return self.v


class FTrader:
    def __init__(self):
        self.open, self.sigs, self.cancels = {}, [], []

    def on_signal(self, s):
        self.sigs.append(s)
        self.open[s["sid"]] = dict(sid=s["sid"], start=s["start"], outcome=s["outcome"], q=0.50, expired=False)

    def cancel_early(self, sid, why=""):
        e = self.open.get(sid)
        if e is None or e["expired"]:
            return False
        e["expired"] = True
        self.cancels.append((sid, why))
        return True


def make_trigger(score, up_moves=None, now_rel=60.15, **kw):
    w = 999_900
    sig4.clock = FakeClock(w + now_rel)
    win = FWin(w)
    tr = FTrader()
    cfg = dict(variant="sig4")
    cfg.update(kw)
    st = Sig4Trigger(cfg, FPM(win), W(), tr, trees=ConstTrees(score))
    st.t_start = w - 100
    wd, G = _setup(w, up_moves)
    st.wins[w], st.g = wd, G
    for c in ("bnf", "by", "cb"):
        st.alive[c] = w + now_rel
    return st, tr, w


def test_signal_needs_score_and_fresh_btc():
    st, tr, w = make_trigger(6.0, up_moves={"bnf": 2.5})
    assert st.tick() == 6.0
    assert len(tr.sigs) == 1
    s = tr.sigs[0]
    assert s["outcome"] == "Up" and s["price_mode"] == "improve" and s["start"] == w and abs(s["edge"] - 0.06) < 1e-12
    st, tr, _ = make_trigger(6.0, up_moves={"bnf": 1.5})          # ход BTC мал - нет сигнала
    st.tick()
    assert tr.sigs == [] and st.stats["skip_fresh"] == 1
    st, tr, _ = make_trigger(-6.0, up_moves={"cb": -2.0})         # прогноз вниз и ход вниз - Down
    st.tick()
    assert [s["outcome"] for s in tr.sigs] == ["Down"]
    st, tr, _ = make_trigger(4.0, up_moves={"bnf": 5.0})          # прогноз ниже порога
    st.tick()
    assert tr.sigs == []


def test_no_signal_outside_time_or_without_history():
    st, tr, _ = make_trigger(6.0, up_moves={"bnf": 3.0}, now_rel=10.15)   # раньше 12 с окна
    st.tick()
    assert tr.sigs == []
    st, tr, w = make_trigger(6.0, up_moves={"bnf": 3.0})
    st.t_start = w - 5                                                     # бот запущен позже T-20 с
    st.tick()
    assert tr.sigs == [] and st.stats["skip_history"] == 1


def test_early_cancel_on_score_drop_and_adverse_move():
    st, tr, w = make_trigger(6.0, up_moves={"bnf": 3.0})
    st.tick()
    assert len(tr.open) == 1
    st.trees = ConstTrees(0.5)                                             # прогноз упал ниже 1 ц - снять
    sig4.clock.t += 0.1
    st.tick()
    assert tr.cancels and "прогноз" in tr.cancels[0][1]
    # ход BTC против: заявка Up снимается сразу по сделке, новые Up - не раньше чем через 1 с
    st, tr, w = make_trigger(6.0, up_moves={"bnf": 3.0})
    st.tick()
    sid = tr.sigs[0]["sid"]
    T = (w + 60.2) * 1000.0
    st.on_btc("by", T - 400, 60000.0, w + 60.2)
    st.on_btc("by", T, 59996.0, w + 60.2)
    assert tr.cancels and tr.cancels[0][0] == sid and "BTC" in tr.cancels[0][1]
    assert st.block[(w, "Up")] > sig4.clock.t


def test_maker_cancel_early_live_and_while_sending():
    cl = Client(matched="0")
    t, win = trader("live", cl, maker_life_sec=5.0)

    async def go():
        t.on_signal(msig(sid=1))
        await asyncio.sleep(0.15)                      # заявка в книге, жить ей ещё ~5 с
        assert t.cancel_early(1, "тест") and not t.cancel_early(1, "повтор")
        await asyncio.sleep(0.3)
    asyncio.run(go())
    assert cl.canceled == ["O1"] and not t.open
    cl2 = Client(matched="0", post_delay=0.3)
    t2, _ = trader("live", cl2, maker_life_sec=5.0)

    async def go2():
        t2.on_signal(msig(sid=1))
        await asyncio.sleep(0.05)                      # ответа на постановку ещё нет
        assert t2.cancel_early(1, "тест")
        await asyncio.sleep(0.6)
    asyncio.run(go2())
    assert cl2.canceled == ["O1"] and not t2.open
