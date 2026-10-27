"""Природа скачков BTC и реакция токенов Polymarket. Только выгрузка по записи сборщика.

    python jump_study.py data/2026-10-12 ... --out OUT

За день пишет:
  * js_dist_<день>: распределение |изменения цены| за горизонт H (50 мс ... 10 с) по каждому источнику, по сетке 100 мс
    (время биржи), в корзинах по долларам;
  * js_cnt_<день>: число скачков |dS за W мс| >= X (пауза 2 с на направление) по источнику, часу UTC, W и X;
  * js_ev_<день>_<fut|spot>: события - скачок источника за 100 мс >= $5 (пауза 1 с на направление):
      - путь цены всех источников (время биржи) от -2 с до +60 с относительно момента скачка t0, приход в Стокгольм;
      - момент, когда каждый источник прошёл половину хода (время биржи и приход);
      - форма: максимум хода за 2 с и время до него, объём и число сделок за 100 мс до t0;
      - книга растущего токена на сервере Polymarket (mid, bid, ask, объёмы) от -2 с до +30 с, первые реакции;
      - сделки рынка Polymarket по токенам и сторонам в интервалах после t0;
      - sigma, время до конца окна, исход.
"""
from __future__ import annotations

import argparse
import os

import numpy as np
import pandas as pd

from edge_source import per_sec_sigma, winners_ptb
from lead_lag import PM, read
from mm_sim import side_arrays

WINDOW = 300
SRC = {"fut": ("bnf_agg", "T", "price", "qty"), "spot": ("bn_agg", "T", "price", "qty"), "bybit": ("by_trade", "T", "price", "size"),
       "okx": ("ok_trade", "T", "price", "size"), "cb": ("cb_ticker", "t_ms", "price", "size")}
H_DIST = [50, 100, 200, 500, 1000, 2000, 5000, 10000]
BINS = [0, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30, 50, 75, 100, 1e9]
CNT_W = [100, 300, 1000]
CNT_X = [5, 10, 20, 40]
OFF_BTC = [-2000, -1000, -500, -300, -200, -100, -50, 0, 50, 100, 200, 300, 500, 1000, 2000, 5000, 10000, 30000, 60000]
OFF_TOK = [-2000, -1000, -500, -300, -200, -100, 0, 50, 100, 150, 200, 250, 300, 400, 500, 750, 1000, 1500, 2000, 3000, 5000,
           10000, 30000]
OFF_BA = [-100, 0, 100, 200, 300, 500, 1000, 2000, 5000]
OFF_SZ = [-100, 0, 200, 500]
TR_BINS = [-500, 0, 150, 300, 1000, 5000]


def load(root, name):
    stream, tcol, pcol, qcol = SRC[name]
    d = read(root, stream, ["recv_ms", tcol, pcol, qcol])
    if d.empty:
        return None
    d = d.dropna().rename(columns={tcol: "T", pcol: "p", qcol: "q"}).sort_values("T", kind="stable")
    return d["T"].values.astype(float), d.recv_ms.values.astype(float), d.p.values.astype(float), d.q.values.astype(float)


def px_at(T, p, t):
    i = np.searchsorted(T, t, side="right") - 1
    return np.where(i >= 0, p[np.maximum(i, 0)], np.nan)


def events(T, p, q, W=100.0, X=5.0, refr=1000.0):
    """Скачки: |p - p(T-W)| >= X. Событие - начало серии: перед ним в ту же сторону не было условия хотя бы refr мс
    (каждая сделка, где условие выполнено, продлевает серию). Возвращает (индекс, направление, dS)."""
    j = np.searchsorted(T, T - W, side="right") - 1
    dS = np.where(j >= 0, p - p[np.maximum(j, 0)], 0.0)
    idx = np.flatnonzero(np.abs(dS) >= X)
    last = {1: -1e18, -1: -1e18}
    out = []
    for i in idx:
        d = 1 if dS[i] > 0 else -1
        start = T[i] - last[d] >= refr
        last[d] = T[i]
        if start:
            out.append((i, d, dS[i]))
    return out


def save_parts(df: pd.DataFrame, stem: str, limit: int = 1_800_000):
    """Пишет csv.gz; если файл больше limit байт (раннер отбрасывает файлы > 2 МБ), делит на части _p0, _p1, ..."""
    f = stem + ".csv.gz"
    df.to_csv(f, index=False)
    n = int(np.ceil(os.path.getsize(f) / limit))
    if n <= 1:
        return
    os.remove(f)
    for k, part in enumerate(np.array_split(np.arange(len(df)), n + 1)):
        df.iloc[part].to_csv(f"{stem}_p{k}.csv.gz", index=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for root in a.roots:
        day = os.path.basename(os.path.normpath(root))
        S = {k: load(root, k) for k in SRC}
        S = {k: v for k, v in S.items() if v is not None and len(v[0]) > 1000}
        bk = read(root, "bnf_book", ["recv_ms", "T", "bid", "ask"])
        if len(bk) > 1000:
            bk = bk.dropna().sort_values("T", kind="stable")
            S["fut_book"] = (bk["T"].values.astype(float), bk.recv_ms.values.astype(float),
                             ((bk.bid + bk.ask) / 2).values.astype(float), np.zeros(len(bk)))
        print(f"{day}: источники " + ", ".join(f"{k} {len(v[0])}" for k, v in S.items()), flush=True)
        if "fut" not in S:
            continue
        t_lo = max(v[0][0] for v in S.values()) + 60000
        t_hi = min(v[0][-1] for v in S.values()) - 60000
        # 1. распределения изменений по сетке 100 мс
        grid = np.arange(t_lo, t_hi, 100.0)
        rows = []
        for k, (T, _, p, _) in S.items():
            p0 = px_at(T, p, grid)
            for H in H_DIST:
                d = np.abs(p0 - px_at(T, p, grid - H))
                d = d[np.isfinite(d)]
                h, _ = np.histogram(d, BINS)
                for b, c in enumerate(h):
                    rows.append(dict(day=day, src=k, H=H, bin=b, lo=BINS[b], n=int(c)))
        pd.DataFrame(rows).to_csv(os.path.join(a.out, f"js_dist_{day}.csv.gz"), index=False)
        # 2. частота скачков по часам
        rows = []
        for k, (T, _, p, q) in S.items():
            for W in CNT_W:
                for X in CNT_X:
                    ev = events(T, p, q, W, X, refr=2000.0)
                    hr = ((np.array([T[i] for i, _, _ in ev]) // 3600000) % 24).astype(int) if ev else np.array([], int)
                    for h_ in range(24):
                        rows.append(dict(day=day, src=k, W=W, X=X, hr=h_, n=int((hr == h_).sum())))
        # секундная волатильность фьючерса по часам
        T, _, p, _ = S["fut"]
        sec = np.arange(t_lo, t_hi, 1000.0)
        dp = np.diff(px_at(T, p, sec))
        hrs = ((sec[1:] // 3600000) % 24).astype(int)
        for h_ in range(24):
            x = dp[hrs == h_]
            if len(x) > 60:
                rows.append(dict(day=day, src="fut_sigma", W=1000, X=0, hr=h_, n=float(np.std(x))))
        pd.DataFrame(rows).to_csv(os.path.join(a.out, f"js_cnt_{day}.csv.gz"), index=False)
        # 3. события и реакция токенов
        top = read(root, "pm_top", ["recv_ms", "d", "w", "o", "bid", "bid_sz", "ask", "ask_sz"])
        pm = PM(top) if len(top) else None
        del top
        winners, ptb = winners_ptb(root)
        tr = read(root, "pm_trades", ["server_ts", "w", "o", "side", "price", "size"])
        trd = {}
        if len(tr):
            tr = tr.dropna(subset=["server_ts", "size"])
            tr["o"] = tr.o.astype(str).str[0]
            tr["side"] = tr.side.astype(str).str.upper().str[0]
            for w, g in tr.groupby("w"):
                g = g.sort_values("server_ts", kind="stable")
                trd[int(w)] = (g.server_ts.values.astype(float), g.o.values, g.side.values, g.price.values.astype(float),
                               g["size"].values.astype(float))
        sig_t, sig_v = per_sec_sigma(S["fut"][0], S["fut"][2])
        books = {}
        if pm is not None:
            for w, x in pm.by_w.items():
                books[w] = (x["srv"]["t"], side_arrays(x["srv"]))
        for evsrc in ("fut", "spot"):
            if evsrc not in S:
                continue
            T, R, p, q = S[evsrc]
            ev = events(T, p, q, 100.0, 5.0, refr=1000.0)
            out = []
            for i, d, dS in ev:
                t0 = T[i]
                if not (t_lo < t0 < t_hi):
                    continue
                r = dict(t0=t0, dir=d, dS100=round(d * dS, 2), rcv_lag=round(R[i] - t0, 1))
                j0 = np.searchsorted(T, t0 - 100, side="left")
                r["n_tr100"] = int(i - j0 + 1)
                r["q_tr100"] = round(float(q[j0:i + 1].sum()), 4)
                r["qmax100"] = round(float(q[j0:i + 1].max()), 4)
                # путь каждого источника относительно своей цены в t0-1000
                for k, (Tk, Rk, pk, _) in S.items():
                    base = px_at(Tk, pk, np.array([t0 - 1000.0]))[0]
                    path = d * (px_at(Tk, pk, t0 + np.array(OFF_BTC, float)) - base)
                    for o_, v in zip(OFF_BTC, path):
                        r[f"{k}_{o_}"] = round(float(v), 2) if np.isfinite(v) else np.nan
                    # когда источник прошёл половину хода фьючерса/спота (от base): время биржи и приход
                    a_, b_ = np.searchsorted(Tk, t0 - 1000, "left"), np.searchsorted(Tk, t0 + 3000, "right")
                    hit = np.flatnonzero(d * (pk[a_:b_] - base) >= 0.5 * abs(dS))
                    r[f"{k}_half_T"] = round(Tk[a_ + hit[0]] - t0, 1) if len(hit) else np.nan
                    r[f"{k}_half_R"] = round(Rk[a_ + hit[0]] - t0, 1) if len(hit) else np.nan
                # форма скачка по источнику события
                a_, b_ = np.searchsorted(T, t0, "left"), np.searchsorted(T, t0 + 2000, "right")
                base = px_at(T, p, np.array([t0 - 100.0]))[0]
                ex = d * (p[a_:b_] - base)
                if len(ex):
                    k_ = int(np.argmax(ex))
                    r["peak2s"], r["t_peak2s"] = round(float(ex[k_]), 2), round(T[a_ + k_] - t0, 1)
                # токен
                w = int(t0 // 1000 // WINDOW * WINDOW)
                r["w"] = w
                r["T_left"] = round((w + WINDOW) - t0 / 1000.0, 2)
                r["sigma"] = round(float(sig_v[min(max(np.searchsorted(sig_t, t0, side="right") - 1, 0), len(sig_v) - 1)]), 3)
                r["won"] = (1.0 if (winners[w] == "Up") == (d > 0) else 0.0) if w in winners else np.nan
                b = books.get(w)
                if b is not None:
                    tt, arr = b
                    X = "U" if d > 0 else "D"
                    bb, aa, bsz = arr[X]
                    asz = (arr["U"][2] if X == "D" else arr["D"][2])   # объём на ask стороны = объём на bid другой
                    def at(off):
                        k = np.searchsorted(tt, t0 + np.asarray(off, float), side="right") - 1
                        return np.maximum(k, 0), k >= 0
                    k, ok = at(OFF_TOK)
                    mid = np.where(ok, (bb[k] + aa[k]) / 2, np.nan)
                    for o_, v in zip(OFF_TOK, mid):
                        r[f"m_{o_}"] = round(float(v), 4) if np.isfinite(v) else np.nan
                    k, ok = at(OFF_BA)
                    for o_, vb, va in zip(OFF_BA, np.where(ok, bb[k], np.nan), np.where(ok, aa[k], np.nan)):
                        r[f"b_{o_}"], r[f"a_{o_}"] = vb, va
                    k, ok = at(OFF_SZ)
                    for o_, vb, va in zip(OFF_SZ, np.where(ok, bsz[k], np.nan), np.where(ok, asz[k], np.nan)):
                        r[f"bs_{o_}"], r[f"as_{o_}"] = vb, va
                    k0 = int(np.searchsorted(tt, t0, side="right") - 1)
                    if k0 >= 0:
                        a0, b0, m0 = aa[k0], bb[k0], (aa[k0] + bb[k0]) / 2
                        e_ = int(np.searchsorted(tt, t0 + 5000, side="right"))
                        seg = slice(k0 + 1, e_)
                        ts_ = tt[seg]
                        def first(mask):
                            h = np.flatnonzero(mask)
                            return round(ts_[h[0]] - t0, 1) if len(h) else np.nan
                        r["t_ask_up"] = first(aa[seg] > a0 + 1e-9)
                        r["t_bid_up"] = first(bb[seg] > b0 + 1e-9)
                        r["t_bid_dn"] = first(bb[seg] < b0 - 1e-9)
                        r["t_mid_up1"] = first((aa[seg] + bb[seg]) / 2 >= m0 + 0.01 - 1e-9)
                    x = trd.get(w)
                    if x is not None:
                        ts, o, side, pr, sz = x
                        a_, b_ = np.searchsorted(ts, t0 + TR_BINS[0], "left"), np.searchsorted(ts, t0 + TR_BINS[-1], "left")
                        rel = ts[a_:b_] - t0
                        bi = np.searchsorted(TR_BINS, rel, side="right") - 1
                        rising = o[a_:b_] == X
                        for lab, msk in (("rB", rising & (side[a_:b_] == "B")), ("rS", rising & (side[a_:b_] == "S")),
                                         ("fB", ~rising & (side[a_:b_] == "B")), ("fS", ~rising & (side[a_:b_] == "S"))):
                            for bn in range(len(TR_BINS) - 1):
                                r[f"{lab}{bn}"] = round(float(sz[a_:b_][msk & (bi == bn)].sum()), 1)
                out.append(r)
            E = pd.DataFrame(out)
            E.insert(0, "day", day)
            save_parts(E, os.path.join(a.out, f"js_ev_{day}_{evsrc}"))
            print(f"  события {evsrc}: {len(E)}, в окнах с книгой {E.m_0.notna().sum() if 'm_0' in E else 0}", flush=True)


if __name__ == "__main__":
    main()
