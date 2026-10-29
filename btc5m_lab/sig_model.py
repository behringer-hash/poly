"""Краткосрочный сигнал «токен сейчас подорожает» (ход mid Up через 3 с, ц) — только numpy.

Признаки на сетке 100 мс внутри окна (3–297 с), только прошлое на момент t (книга — время сервера, BTC — время
биржи): mid, спред, объёмы и перекос верха книги, справедливая P(Up) и BTC − K (фьючерс Binance со сдвигом на базис к
Chainlink), ходы mid за 0,3/1/3/10/30 с, ходы фьючерса Binance, Bybit, Coinbase за 0,3/1/3 с, изменение объёмов за
0,5 с, поток тейкеров (+ покупка Up / продажа Down) за 1 и 5 с, время в окне.
Модель — градиентный бустинг (обучается локально в scikit-learn), деревья выгружаются в .npz и считаются здесь без
scikit-learn и scipy (на сервере записи их нет).
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd

FEATS = ["mid", "spr", "bz", "az", "imb", "fair", "dk", "dm03", "dm1", "dm3", "dm10", "dm30",
         "dbnf03", "dbnf1", "dbnf3", "dby03", "dby1", "dby3", "dcb03", "dcb1", "dcb3", "dbz5", "daz5", "fl1", "fl5", "t"]
GRID_T = np.round(np.arange(3, 297, 0.1), 1)          # с от начала окна


def phi(x):
    """Функция нормального распределения (erf через math, векторно)."""
    x = np.asarray(x, dtype=float)
    out = np.full(x.shape, np.nan)
    ok = np.isfinite(x)
    out[ok] = 0.5 * (1.0 + np.vectorize(math.erf)(x[ok] / math.sqrt(2.0)))
    return out


def at(ts, vs, t):
    """Последнее значение vs на моменты t (ts по возрастанию); nan до первого."""
    ts = np.asarray(ts, dtype=float)
    i = np.searchsorted(ts, t, side="right") - 1
    return np.where(i >= 0, np.asarray(vs, dtype=float)[np.maximum(i, 0)], np.nan)


def fair_series(t_ms, s, cl, K, w):
    """P(Up) по фьючерсу со сдвигом на базис к Chainlink (медиана за 60 с), σ по 1-с изменениям (как wv.fair_series)."""
    basis = pd.Series(cl - s).rolling(600, min_periods=50).median().ffill().values
    S = s + np.nan_to_num(basis)
    d1 = pd.Series(s).diff(10)
    sig = d1.rolling(3000, min_periods=300).std().values
    sig = np.where(np.isfinite(sig), sig, d1.std())
    T = np.maximum(300 - (t_ms / 1000 - w), 0.5)
    sd = np.where(T >= 60, sig * np.sqrt(np.maximum(T - 40, 1e-6)), sig * np.sqrt(T ** 3 / 10800))
    return phi((S - K) / np.maximum(sd, 1e-6)), S - K


def window_features(w, K, book, trades, btc):
    """book: (t_ms сервера, bid Up, ask Up, объём bid, объём ask); trades: (server_ts, знак·объём) или None;
    btc: {"bnf"|"by"|"cb"|"cl": (T_ms, цена)} — сырые сделки/тики или уже сетка. -> DataFrame на GRID_T."""
    ts, bid, ask, bsz, asz = (np.asarray(x, dtype=float) for x in book)
    tm = (w + GRID_T) * 1000.0
    n = len(GRID_T)
    b, a, bz, az = at(ts, bid, tm), at(ts, ask, tm), at(ts, bsz, tm), at(ts, asz, tm)
    mid = np.where(np.isnan(a), b, np.where(np.isnan(b), a, (a + b) / 2))
    gb = np.arange((w - 20) * 1000.0, (w + 300) * 1000.0, 100.0)
    X = {k: at(v[0], v[1], gb) for k, v in btc.items() if v is not None and len(v[0])}
    if "bnf" not in X or np.isnan(X["bnf"]).all():
        return None
    fr, dk = fair_series(gb, X["bnf"], X.get("cl", np.full(len(gb), np.nan)), K, w)

    def lag(x, k):
        o = np.full(n, np.nan)
        o[k:] = x[:-k]
        return o
    F = dict(t=GRID_T.astype(float), mid=mid, spr=100 * (a - b), bz=bz, az=az, imb=bz / (bz + az),
             fair=at(gb, fr, tm), dk=at(gb, dk, tm))
    for k, nm in ((3, "03"), (10, "1"), (30, "3"), (100, "10"), (300, "30")):
        F["dm" + nm] = 100 * (mid - lag(mid, k))
    for c in ("bnf", "by", "cb"):
        xc = at(gb, X[c], tm) if c in X else np.full(n, np.nan)
        for k, nm in ((3, "03"), (10, "1"), (30, "3")):
            F[f"d{c}{nm}"] = xc - lag(xc, k)
    F["dbz5"], F["daz5"] = bz - lag(bz, 5), az - lag(az, 5)
    if trades is not None and len(trades[0]):
        et = np.asarray(trades[0], dtype=float)
        cs = np.r_[0.0, np.cumsum(np.asarray(trades[1], dtype=float))]
        F["fl1"] = cs[np.searchsorted(et, tm, side="right")] - cs[np.searchsorted(et, tm - 1000, side="right")]
        F["fl5"] = cs[np.searchsorted(et, tm, side="right")] - cs[np.searchsorted(et, tm - 5000, side="right")]
    else:
        F["fl1"] = F["fl5"] = np.zeros(n)
    D = pd.DataFrame(F)
    D["mid_raw"], D["a"], D["b"] = mid, a, b
    return D


class Trees:
    """Сумма деревьев HistGradientBoosting, выгруженных export_trees()."""

    def __init__(self, path):
        z = np.load(path, allow_pickle=False)
        self.base = float(z["base"])
        self.feats = [str(x) for x in z["feats"]]
        self.feat, self.thr, self.left, self.right = z["feat"], z["thr"], z["left"], z["right"]
        self.leaf, self.val, self.mleft, self.root = z["leaf"], z["val"], z["mleft"], z["root"]

    def predict(self, X):
        X = np.asarray(X, dtype=float)
        n = X.shape[0]
        out = np.full(n, self.base)
        rows = np.arange(n)
        for r in self.root:
            node = np.full(n, r, dtype=np.int64)
            while True:
                lf = self.leaf[node]
                if lf.all():
                    break
                act = ~lf
                nd = node[act]
                x = X[rows[act], self.feat[nd]]
                go_left = np.where(np.isnan(x), self.mleft[nd], x <= self.thr[nd])
                node[act] = np.where(go_left, self.left[nd], self.right[nd])
            out += self.val[node]
        return out


def export_trees(model, feats, path):
    """Выгрузка sklearn HistGradientBoostingRegressor в .npz (узлы всех деревьев подряд)."""
    F, T, L, R, LF, V, ML, roots = [], [], [], [], [], [], [], []
    off = 0
    for it in model._predictors:
        nodes = it[0].nodes
        roots.append(off)
        F.append(nodes["feature_idx"].astype(np.int64))
        T.append(nodes["num_threshold"].astype(float))
        L.append(nodes["left"].astype(np.int64) + off)
        R.append(nodes["right"].astype(np.int64) + off)
        LF.append(nodes["is_leaf"].astype(bool))
        V.append(nodes["value"].astype(float))
        ML.append(nodes["missing_go_to_left"].astype(bool))
        off += len(nodes)
    np.savez_compressed(path, base=np.array(float(np.ravel(model._baseline_prediction)[0])), feats=np.array(feats),
                        feat=np.concatenate(F), thr=np.concatenate(T), left=np.concatenate(L), right=np.concatenate(R),
                        leaf=np.concatenate(LF), val=np.concatenate(V), mleft=np.concatenate(ML), root=np.array(roots))
