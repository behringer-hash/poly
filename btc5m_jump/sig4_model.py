"""Стратегия 4: признаки модели сигнала в реальном времени и расчёт её деревьев (только numpy, без pandas/sklearn).

Признаки - те же, что при обучении (btc5m_lab/sig_model.window_features): сетка 100 мс внутри окна (3,0-296,9 с),
книга Polymarket - по времени сервера, BTC - по времени биржи, всё только из прошлого на момент сетки t:
  mid, спред, объёмы и перекос верха книги Up, справедливая P(Up) и BTC - K (фьючерс Binance + базис к Chainlink),
  ходы mid за 0,3/1/3/10/30 с, ходы фьючерса Binance, Bybit, Coinbase за 0,3/1/3 с, изменение объёмов за 0,5 с,
  поток тейкеров (+ покупка Up / продажа Down) за 1 и 5 с, время в окне.
Цель модели - ход mid Up через 3 с, центов. Модель - деревья градиентного бустинга, выгруженные в .npz
(btc5m_lab/sig_model.export_trees); здесь они считаются на чистом Python по одной строке.
Равенство с обучением проверено на записи сборщика (tools/check_sig4_features.py, README_RU.md «Стратегия 4»).
"""
from __future__ import annotations

import bisect
import math

import numpy as np

FEATS = ["mid", "spr", "bz", "az", "imb", "fair", "dk", "dm03", "dm1", "dm3", "dm10", "dm30",
         "dbnf03", "dbnf1", "dbnf3", "dby03", "dby1", "dby3", "dcb03", "dcb1", "dcb3", "dbz5", "daz5", "fl1", "fl5", "t"]
NAN = float("nan")
T0 = 3.0                 # первая точка сетки окна, с
T1 = 296.9               # последняя
N_GB = 3200              # ячеек BTC-сетки: от T-20 с до T+300 с по 100 мс
KEEP_BEFORE_MS = 5000.0  # сколько истории источника держать до начала BTC-сетки окна


def gb_times(w: int) -> np.ndarray:
    """BTC-сетка окна (мс) - ровно как при обучении."""
    return np.arange((w - 20) * 1000.0, (w + 300) * 1000.0, 100.0)


def grid_t(x: float) -> float:
    """Точка сетки окна (с) - то же число double, что при обучении (np.round(..., 1))."""
    return float(np.round(x, 1))


def phi(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0))) if math.isfinite(x) else NAN


class Trees:
    """Сумма деревьев HistGradientBoosting из .npz (поля как в btc5m_lab/sig_model.export_trees)."""

    def __init__(self, path: str):
        z = np.load(path, allow_pickle=False)
        self.path = path
        self.base = float(z["base"])
        self.feats = [str(x) for x in z["feats"]]
        if self.feats != FEATS:
            raise ValueError(f"признаки модели {path} не совпадают с FEATS")
        self.feat = z["feat"].astype(int).tolist()
        self.thr = z["thr"].astype(float).tolist()
        self.left = z["left"].astype(int).tolist()
        self.right = z["right"].astype(int).tolist()
        self.leaf = z["leaf"].astype(bool).tolist()
        self.val = z["val"].astype(float).tolist()
        self.mleft = z["mleft"].astype(bool).tolist()
        self.root = z["root"].astype(int).tolist()
        self.n_trees = len(self.root)

    def predict_row(self, x) -> float:
        feat, thr, left, right, leaf, val, mleft = self.feat, self.thr, self.left, self.right, self.leaf, self.val, self.mleft
        out = self.base
        for n in self.root:
            while not leaf[n]:
                v = x[feat[n]]
                if v != v:                                 # nan: сторона «пропуска», выученная деревом
                    n = left[n] if mleft[n] else right[n]
                else:
                    n = left[n] if v <= thr[n] else right[n]
            out += val[n]
        return out


class GridSeries:
    """Цена источника на BTC-сетке текущего окна: ячейка k = цена последней сделки со временем биржи <= gb[k]
    (как at(T, цена, gb) при обучении). Сырые сделки хранятся с запасом, ячейки закрываются по мере хода времени."""

    def __init__(self):
        self.hist: list[tuple[float, float]] = []    # (время биржи, цена), по возрастанию времени
        self.w = None
        self.gb = None
        self.vals = None
        self.k = 0
        self.ptr = 0
        self.last = NAN

    def add(self, T: float, px: float) -> None:
        h = self.hist
        if h and T < h[-1][0]:
            i = bisect.bisect_right(h, (T, float("inf")))
            if i < self.ptr:                  # сделка в уже закрытые ячейки - опоздала; только последняя цена
                return
            h.insert(i, (T, px))
        else:
            h.append((T, px))
        if len(h) > 400000:                   # страховка от разрастания без смены окна
            cut = len(h) - 300000
            del h[:cut]
            self.ptr = max(0, self.ptr - cut)

    def start_window(self, w: int) -> None:
        if self.w == w:
            return
        self.w, self.gb, self.vals, self.k, self.last = w, gb_times(w), np.full(N_GB, NAN), 0, NAN
        lim = self.gb[0] - KEEP_BEFORE_MS
        i = bisect.bisect_left(self.hist, (lim, -float("inf")))
        del self.hist[:i]
        self.ptr = 0

    def close_upto(self, t_ms: float) -> None:
        """Закрыть все ячейки с gb[k] <= t_ms."""
        if self.w is None:
            return
        gb, vals, h = self.gb, self.vals, self.hist
        k, ptr, last = self.k, self.ptr, self.last
        n = len(h)
        while k < N_GB and gb[k] <= t_ms:
            g = gb[k]
            while ptr < n and h[ptr][0] <= g:
                last = h[ptr][1]
                ptr += 1
            vals[k] = last
            k += 1
        self.k, self.ptr, self.last = k, ptr, last


class WinData:
    """Книга Up (время сервера) и сделки рынка одного окна - для признаков."""

    def __init__(self, w: int):
        self.w = w
        self.bt: list[float] = []          # время сервера, мс (по возрастанию)
        self.bk: list[tuple] = []          # (bid, ask, объём bid, объём ask)
        self.et: list[float] = []          # время сделок сервера, мс (по возрастанию)
        self.es: list[float] = []          # знак * объём: + покупка Up / продажа Down
        self.cs: list[float] = [0.0]       # накопленная сумма es

    def add_top(self, srv: float, bid, ask, bsz, asz) -> None:
        f = lambda v: NAN if v is None or v == "" else float(v)
        i = bisect.bisect_right(self.bt, srv)
        self.bt.insert(i, srv)
        self.bk.insert(i, (f(bid), f(ask), f(bsz), f(asz)))

    def add_trade(self, sts: float, signed: float) -> None:
        i = bisect.bisect_right(self.et, sts)
        self.et.insert(i, sts)
        self.es.insert(i, signed)
        if i == len(self.et) - 1:
            self.cs.append(self.cs[-1] + signed)
        else:                              # не по порядку - пересчитать суммы с места вставки
            del self.cs[i + 1:]
            for v in self.es[i:]:
                self.cs.append(self.cs[-1] + v)

    def book_at(self, tm: float):
        i = bisect.bisect_right(self.bt, tm) - 1
        return self.bk[i] if i >= 0 else (NAN, NAN, NAN, NAN)

    def flow(self, tm: float, back_ms: float) -> float:
        return self.cs[bisect.bisect_right(self.et, tm)] - self.cs[bisect.bisect_right(self.et, tm - back_ms)]


def _mid(b, a):
    if a != a:
        return b
    if b != b:
        return a
    return (a + b) / 2


def _cell(gb: np.ndarray, tm: float) -> int:
    return int(np.searchsorted(gb, tm, side="right")) - 1


def _basis_at(cl: np.ndarray, s: np.ndarray, k: int) -> float:
    """Медиана (Chainlink - фьючерс) за 600 ячеек до k включительно, если годных >= 50 (rolling(600, 50).median())."""
    lo = max(0, k - 599)
    x = cl[lo:k + 1] - s[lo:k + 1]
    x = x[np.isfinite(x)]
    return float(np.median(x)) if len(x) >= 50 else NAN


def _d1(s: np.ndarray, lo: int, k: int) -> np.ndarray:
    """Годные s[j] - s[j-10] для j в [lo, k] (Series.diff(10))."""
    j0 = max(lo, 10)
    if j0 > k:
        return np.array([])
    d = s[j0:k + 1] - s[j0 - 10:k + 1 - 10]
    return d[np.isfinite(d)]


def fair_at(s: np.ndarray, cl: np.ndarray, gb: np.ndarray, K: float, w: int, k: int):
    """Справедливая P(Up) и S - K в ячейке k BTC-сетки (как sig_model.fair_series в этой ячейке).
    Отличие: если 1-с ходов за 300 с меньше 300 (первые ~11 с окна), при обучении бралось std за всё окно
    (будущее), здесь - std по тому, что есть; поэтому торговать раньше 12 с окна не стоит."""
    b = _basis_at(cl, s, k)
    if b != b:                                        # ffill: последний годный базис раньше k
        for j in range(k - 1, -1, -1):
            b = _basis_at(cl, s, j)
            if b == b:
                break
    S = s[k] + (0.0 if b != b else b)
    d = _d1(s, max(0, k - 2999), k)
    sig = float(np.std(d, ddof=1)) if len(d) >= 300 else NAN
    if sig != sig:
        d = _d1(s, 0, k)
        sig = float(np.std(d, ddof=1)) if len(d) >= 2 else NAN
    T = max(300.0 - (gb[k] / 1000.0 - w), 0.5)
    sd = sig * math.sqrt(max(T - 40, 1e-6)) if T >= 60 else sig * math.sqrt(T ** 3 / 10800)
    fair = phi((S - K) / max(sd, 1e-6)) if sd == sd and S == S else NAN
    return fair, S - K


def features_at(t: float, wd: WinData, K: float, btc: dict, cl: GridSeries):
    """Строка признаков в точке сетки окна t (с). btc: {"bnf"|"by"|"cb": GridSeries}, cl: GridSeries Chainlink;
    ячейки сетки до t уже закрыты (close_upto). Возвращает (список в порядке FEATS, ход BTC за 0,3 с вверх
    (max по биржам), вниз (-min по биржам))."""
    w = wd.w
    bnf = btc["bnf"]
    gb = bnf.gb

    def tm_of(x):
        return (w + x) * 1000.0

    def lagt(k):                                      # точка сетки на k шагов раньше; None - раньше начала сетки
        x = grid_t(t - 0.1 * k)
        return x if x >= T0 - 1e-9 else None

    tm = tm_of(t)
    b, a, bz, az = wd.book_at(tm)
    mid = _mid(b, a)
    sz = bz + az
    f = dict(t=t, mid=mid, spr=100 * (a - b), bz=bz, az=az, imb=bz / sz if sz == sz and sz != 0 else NAN)
    k = _cell(gb, tm)
    if k >= 0 and K is not None and K == K:
        f["fair"], f["dk"] = fair_at(bnf.vals, cl.vals if cl.vals is not None else np.full(N_GB, NAN), gb, K, w, k)
    else:
        f["fair"], f["dk"] = NAN, NAN
    for kk, nm in ((3, "03"), (10, "1"), (30, "3"), (100, "10"), (300, "30")):
        x = lagt(kk)
        if x is None:
            f["dm" + nm] = NAN
        else:
            bb, aa, _, _ = wd.book_at(tm_of(x))
            f["dm" + nm] = 100 * (mid - _mid(bb, aa))
    fresh = []
    for c in ("bnf", "by", "cb"):
        g = btc.get(c)
        ok = g is not None and g.vals is not None and g.w == w and k >= 0
        cur = g.vals[k] if ok else NAN
        for kk, nm in ((3, "03"), (10, "1"), (30, "3")):
            x = lagt(kk)
            if x is None or not ok:
                f[f"d{c}{nm}"] = NAN
            else:
                kp = _cell(gb, tm_of(x))
                f[f"d{c}{nm}"] = float(cur - g.vals[kp]) if kp >= 0 else NAN
        v = f[f"d{c}03"]
        if v == v:
            fresh.append(v)
    x5 = lagt(5)
    if x5 is None:
        f["dbz5"] = f["daz5"] = NAN
    else:
        _, _, bz5, az5 = wd.book_at(tm_of(x5))
        f["dbz5"], f["daz5"] = bz - bz5, az - az5
    f["fl1"], f["fl5"] = (wd.flow(tm, 1000.0), wd.flow(tm, 5000.0)) if wd.et else (0.0, 0.0)
    up = max(fresh) if fresh else NAN
    dn = -min(fresh) if fresh else NAN
    return [float(f[n]) for n in FEATS], up, dn
