"""Краткосрочный прогноз mid Up (через 3 с) по книге Polymarket и BTC + проверка правила «тейкер при сильном прогнозе»
на днях, не участвовавших в обучении (скользящее окно: обучение на N предыдущих днях, проверка на следующем).

    python grid_model.py DATA_DIR --days 2026-10-15,2026-10-16,... --out OUT [--train 3]

Сетка 100 мс по каждому окну (3–297 с). Признаки — только прошлое на момент t (книга — время сервера, BTC — время
биржи): mid, спред, объёмы и перекос верха книги, «справедливая» P(Up) и BTC − K (фьючерс Binance со сдвигом на базис
к Chainlink), ходы mid за 0,3/1/3/10/30 с, ходы фьючерса Binance, Bybit, Coinbase за 0,3/1/3 с, изменение объёмов за
0,5 с, поток тейкеров (+ покупка Up / продажа Down) за 1 и 5 с, время в окне. Цель — mid Up через 3 с − mid сейчас (ц).
Правило: прогноз >= порога → покупка Up (<= −порога → Down) лимитом по ask момента t; сведение через L мс по книге
сервера: исполнено, если ask(t+L) <= лимита, по цене ask(t+L); не чаще раза в 2 с на сторону в окне; цены 0,05–0,95.
Результат — по исходу окна, после комиссии тейкера 0,07·p·(1−p). Выход: gm_res.csv (день × порог × задержка),
gm_fills.csv.gz (исполнения), gm_r2.csv.
"""
from __future__ import annotations

import argparse
import os
import time

import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.ensemble import HistGradientBoostingRegressor

from edge_source import winners_ptb
from lead_lag import read

FEATS = ["mid", "spr", "bz", "az", "imb", "fair", "dk", "dm03", "dm1", "dm3", "dm10", "dm30",
         "dbnf03", "dbnf1", "dbnf3", "dby03", "dby1", "dby3", "dcb03", "dcb1", "dcb3", "dbz5", "daz5", "fl1", "fl5", "t"]
THRS = (4.0, 6.0, 8.0, 10.0)
LAGS = (5, 7, 10)            # шагов по 100 мс


def at(ts, vs, t):
    i = np.searchsorted(ts, t, side="right") - 1
    return np.where(i >= 0, vs[np.maximum(i, 0)], np.nan)


def fair_series(t_ms, s, cl, K, w):
    """Как wv.fair_series: P(Up) по фьючерсу со сдвигом на базис к Chainlink (медиана за 60 с), σ по 1-с изменениям."""
    basis = pd.Series(cl - s).rolling(600, min_periods=50).median().ffill().values
    S = s + np.nan_to_num(basis)
    d1 = pd.Series(s).diff(10)
    sig = d1.rolling(3000, min_periods=300).std().values
    fallback = d1.std()
    sig = np.where(np.isfinite(sig), sig, fallback)
    T = np.maximum(300 - (t_ms / 1000 - w), 0.5)
    sd = np.where(T >= 60, sig * np.sqrt(np.maximum(T - 40, 1e-6)), sig * np.sqrt(T ** 3 / 10800))
    return norm.cdf((S - K) / np.maximum(sd, 1e-6)), S - K


def build_day(root, max_windows=0):
    winners, ptb = winners_ptb(root)
    top = read(root, "pm_top", ["recv_ms", "d", "w", "o", "bid", "bid_sz", "ask", "ask_sz"])
    top = top[top.o == "U"].copy()
    top["srv"] = top.recv_ms - top.d
    top = top.sort_values(["w", "srv"], kind="stable")
    tr = read(root, "pm_trades", ["server_ts", "w", "o", "side", "size"]).dropna()
    up = tr.o.astype(str).str.upper().str.startswith("U")
    buy = tr.side.astype(str).str.upper().str.startswith("B")
    tr["sg"] = np.where(up == buy, 1.0, -1.0) * tr["size"]
    tr = tr.sort_values(["w", "server_ts"], kind="stable")
    src = {}
    for nm, st, tc in (("bnf", "bnf_agg", "T"), ("by", "by_trade", "T"), ("cb", "cb_ticker", "t_ms")):
        try:
            x = read(root, st, [tc, "price"]).dropna().sort_values(tc, kind="stable")
            src[nm] = (x[tc].values.astype(float), x.price.values.astype(float))
        except Exception as ex:
            print(f"  {st}: {ex!r}", flush=True)
    r = read(root, "rtds", ["feed", "ts_ms", "value"])
    r = r[r.feed == "cl"].dropna().sort_values("ts_ms", kind="stable")
    src["cl"] = (r.ts_ms.values.astype(float), r.value.values.astype(float))
    if "bnf" not in src:
        return pd.DataFrame()
    out = []
    tops = {w: g for w, g in top.groupby("w")}
    trs = {w: g for w, g in tr.groupby("w")}
    ws = sorted(winners)
    if max_windows:
        ws = ws[:max_windows]
    for w in ws:
        if w not in tops or w not in ptb:
            continue
        g = tops[w]
        if len(g) < 50:
            continue
        K = ptb[w]
        won = 1.0 if winners[w] == "Up" else 0.0
        ts = g.srv.values.astype(float)
        gt = np.round(np.arange(3, 297, 0.1), 1)
        tm = (w + gt) * 1000.0
        b, a = at(ts, g.bid.values, tm), at(ts, g.ask.values, tm)
        bz, az = at(ts, g.bid_sz.values, tm), at(ts, g.ask_sz.values, tm)
        mid = np.where(np.isnan(a), b, np.where(np.isnan(b), a, (a + b) / 2))
        # BTC на сетке 100 мс от T−20 с (для базиса и σ)
        gb = np.arange((w - 20) * 1000.0, (w + 300) * 1000.0, 100.0)
        X = {nm: at(src[nm][0], src[nm][1], gb) for nm in ("bnf", "by", "cb", "cl") if nm in src}
        if np.isnan(X["bnf"]).all():
            continue
        fr, dk = fair_series(gb, X["bnf"], X.get("cl", np.full(len(gb), np.nan)), K, w)
        fair = at(gb, fr, tm)
        dkk = at(gb, dk, tm)
        n = len(gt)

        def lag(x, k):
            o = np.full(n, np.nan)
            o[k:] = x[:-k]
            return o

        def lead(x, k):
            o = np.full(n, np.nan)
            o[:-k] = x[k:]
            return o
        F = dict(w=np.full(n, w), t=gt, mid=mid, spr=100 * (a - b), bz=bz, az=az, imb=bz / (bz + az), fair=fair, dk=dkk,
                 won=np.full(n, won), a=a, b=b)
        for k, nm in ((3, "03"), (10, "1"), (30, "3"), (100, "10"), (300, "30")):
            F["dm" + nm] = 100 * (mid - lag(mid, k))
        for c in ("bnf", "by", "cb"):
            if c in X:
                xc = at(gb, X[c], tm)
                for k, nm in ((3, "03"), (10, "1"), (30, "3")):
                    F[f"d{c}{nm}"] = xc - lag(xc, k)
            else:
                for nm in ("03", "1", "3"):
                    F[f"d{c}{nm}"] = np.full(n, np.nan)
        F["dbz5"], F["daz5"] = bz - lag(bz, 5), az - lag(az, 5)
        if w in trs:
            e = trs[w]
            et, cs = e.server_ts.values.astype(float), np.r_[0.0, np.cumsum(e.sg.values)]
            ix = lambda t: np.searchsorted(et, t, side="right")
            F["fl1"] = cs[ix(tm)] - cs[ix(tm - 1000)]
            F["fl5"] = cs[ix(tm)] - cs[ix(tm - 5000)]
        else:
            F["fl1"] = F["fl5"] = np.zeros(n)
        F["y3"] = 100 * (lead(mid, 30) - mid)
        for L in LAGS:
            F[f"a{L}"], F[f"b{L}"] = lead(a, L), lead(b, L)
            F[f"az{L}"], F[f"bz{L}"] = lead(az, L), lead(bz, L)
        out.append(pd.DataFrame(F))
    if not out:
        return pd.DataFrame()
    D = pd.concat(out, ignore_index=True)
    D = D[D.mid.between(0.05, 0.95)]
    keep = ["w", "won", "a", "b", "y3"] + FEATS + [f"{c}{L}" for L in LAGS for c in ("a", "b", "az", "bz")]
    D = D[[c for c in dict.fromkeys(keep)]]
    num = D.select_dtypes("float64").columns
    D[num] = D[num].astype("float32")
    return D.reset_index(drop=True)


def trade(te, p, thr, L):
    rows = []
    for side in ("U", "D"):
        if side == "U":
            m = p >= thr
            px0, px, won, sz = te.a.values, te[f"a{L}"].values, te.won.values, te[f"az{L}"].values
        else:
            m = p <= -thr
            px0, px, won, sz = 1 - te.b.values, 1 - te[f"b{L}"].values, 1 - te.won.values, te[f"bz{L}"].values
        idx = np.flatnonzero(m)
        if not len(idx):
            continue
        x = pd.DataFrame(dict(w=te.w.values[idx], t=te.t.values[idx], px0=px0[idx], px=px[idx], won=won[idx], sz=sz[idx],
                              p=p[idx]))
        x = x[(x.px > 0.05) & (x.px < 0.95)]
        x = x[x.groupby("w").t.diff().fillna(99) >= 2.0]
        x = x[x.px <= x.px0 + 1e-4].copy()
        x["side"] = side
        x["r"] = 100 * (x.won - x.px) - 100 * 0.07 * x.px * (1 - x.px)
        rows.append(x)
    return pd.concat(rows) if rows else pd.DataFrame()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data_dir")
    ap.add_argument("--days", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--train", type=int, default=3)
    ap.add_argument("--max-windows", type=int, default=0)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    days = [d for d in a.days.split(",") if os.path.isdir(os.path.join(a.data_dir, d))]
    t0 = time.time()
    res, fills, r2s, buf = [], [], [], []
    rng = np.random.default_rng(0)
    for te_day in days:
        te = build_day(os.path.join(a.data_dir, te_day), a.max_windows)
        print(f"{te_day}: сетка {len(te)} строк, {te.w.nunique() if len(te) else 0} окон, {time.time() - t0:.0f} с", flush=True)
        if not len(te):
            continue
        if len(buf) >= a.train:                       # обучение только на предыдущих днях
            tr = pd.concat([g for _, g in buf[-a.train:]], ignore_index=True)
            tr = tr[tr.y3.notna()]
            idx = rng.choice(len(tr), min(len(tr), 600000), replace=False)
            m = HistGradientBoostingRegressor(max_iter=300, learning_rate=0.05, max_leaf_nodes=31, l2_regularization=1.0)
            m.fit(tr[FEATS].values[idx], tr.y3.values[idx])
            del tr
            p = m.predict(te[FEATS].values)
            ok = te.y3.notna().values
            yv = te.y3.values[ok]
            r2 = 1 - ((yv - p[ok]) ** 2).sum() / ((yv - yv.mean()) ** 2).sum()
            r2s.append(dict(day=te_day, r2=r2, n=len(te), train=",".join(d for d, _ in buf[-a.train:])))
            for thr in THRS:
                for L in LAGS:
                    x = trade(te, p, thr, L)
                    if not len(x):
                        continue
                    x["day"], x["thr"], x["lag"] = te_day, thr, L
                    fills.append(x)
                    gw = x.groupby("w").r.agg(["sum", "size"])
                    mu = x.r.mean()
                    se = np.sqrt(((gw["sum"] - mu * gw["size"]) ** 2).sum()) / len(x)
                    res.append(dict(day=te_day, thr=thr, lag_ms=L * 100, n=len(x), r=mu, t=mu / se if se > 0 else np.nan,
                                    sum_c=x.r.sum(), px=x.px.mean(), sz_med=x.sz.median()))
            print(f"  проверка {te_day}: R² {r2:.3f}; {time.time() - t0:.0f} с", flush=True)
        buf.append((te_day, te))
        buf = buf[-a.train:]
    R = pd.DataFrame(res)
    R.to_csv(os.path.join(a.out, "gm_res.csv"), index=False)
    pd.DataFrame(r2s).to_csv(os.path.join(a.out, "gm_r2.csv"), index=False)
    if fills:
        pd.concat(fills).to_csv(os.path.join(a.out, "gm_fills.csv.gz"), index=False)
    if len(R):
        S = R.groupby(["thr", "lag_ms"]).apply(lambda g: pd.Series({"дней": len(g), "в_плюсе": int((g.r > 0).sum()),
                                                                    "n": g.n.sum(), "ц_шейр": g.sum_c.sum() / g.n.sum()}))
        print(S.round(2).to_string(), flush=True)


if __name__ == "__main__":
    main()
