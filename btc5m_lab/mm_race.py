"""Хронометраж для маркет-мейкинга: успеваем ли мы снять устаревшую котировку раньше, чем её съест информированный тейкер.

    python mm_race.py data/2026-10-13 data/2026-10-14 ... --out OUT

Событие - скачок BTC на фьючерсе Binance (сделки bnf_agg, время биржи T): |цена - цена W мс назад| >= N $.
Для каждого скачка в текущем окне Polymarket:
  * книга сервера (pm_top, время сервера = recv - d) перед скачком: ask растущего токена r_ask0 и объём на нём. Котировки
    мейкеров по этой цене (ask растущего = bid падающего по зеркальной цене) после скачка устарели;
  * «съедания» - сделки рынка по устаревшей цене: покупка растущего токена по цене <= r_ask0 или продажа падающего по цене
    >= 1 - r_ask0 (время сервера server_ts, по одному на хэш транзакции);
  * переоценка - первый момент, когда ask растущего на сервере выше r_ask0 (все котировки по старой цене исчезли);
  * наша осведомлённость - для каждого источника первый ПРИХОД (recv_ms) сообщения, где цена источника сдвинулась хотя бы
    на половину скачка в ту же сторону от своего уровня до начала скачка;
  * устаревание по модели: справедливая цена растущего токена (якорь = mid книги до скачка, ход BTC, sigma) минус r_ask0.
Часы: время биржи Binance, сервера Polymarket и нашего сервера считаются синхронными (наш сервер на chrony); для оценки
ошибки печатаются минимальные задержки recv - время источника. Выход: race_<день>.csv.gz (строка на скачок) и сводка.
"""
from __future__ import annotations

import argparse
import math
import os

import numpy as np
import pandas as pd

from common import norm_cdf, norm_inv
from lead_lag import read
from paper import settle_sd
from replay import load_source

SOURCES = ["binance_fut", "binance_fut_book", "binance", "binance_book", "bybit", "bybit_trade", "coinbase", "okx"]
GRID = [-200, 0, 50, 100, 150, 200, 250, 300, 400, 500, 750, 1000, 2000, 3000]


def sigma_series(T: np.ndarray, px: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """sigma ($/sqrt(с)) по секундным приращениям за прошлые 15 минут (без заглядывания вперёд), по секундам."""
    s = pd.Series(px, index=pd.to_datetime(T, unit="ms")).resample("1s").last().ffill()
    sig = s.diff().rolling(900, min_periods=120).std().shift(1).bfill().clip(lower=0.5)
    return (s.index.asi8 // 1_000_000).astype(float), sig.values.astype(float)


def fires(t: np.ndarray, px: np.ndarray, N: float, W: float, refractory: float) -> list[tuple[int, int]]:
    j = np.searchsorted(t, t - W, side="right") - 1
    move = np.where(j >= 0, px - px[np.maximum(j, 0)], 0.0)
    last = {1: -1e18, -1: -1e18}
    out = []
    for i in np.flatnonzero(np.abs(move) >= N):
        d = 1 if move[i] > 0 else -1
        if t[i] - last[d] < refractory:
            continue
        last[d] = t[i]
        out.append((int(i), d))
    return out


def day(root: str, N: float, W: float, refr: float, min_gap: float) -> tuple[pd.DataFrame, dict]:
    diag = {}
    top = read(root, "pm_top", ["recv_ms", "d", "w", "o", "bid", "bid_sz", "ask", "ask_sz"])
    tr = read(root, "pm_trades", ["recv_ms", "server_ts", "w", "o", "side", "price", "size", "tx"])
    fa = read(root, "bnf_agg", ["recv_ms", "T", "price"])
    if top.empty or tr.empty or fa.empty:
        return pd.DataFrame(), {"нет данных": [x for x, d in (("pm_top", top), ("pm_trades", tr), ("bnf_agg", fa)) if d.empty]}
    top = top[top.o == "U"].dropna(subset=["bid", "ask"]).copy()
    top["srv"] = top.recv_ms - top.d
    diag["pm_top d (recv-сервер), мс: min/p1/p50"] = [round(float(np.percentile(top.d, q)), 1) for q in (0, 1, 50)]
    tr = tr.dropna(subset=["server_ts", "price", "size"]).copy()
    tr["lat"] = tr.recv_ms - tr.server_ts
    diag["pm_trades recv-server_ts, мс: min/p1/p50"] = [round(float(np.percentile(tr.lat, q)), 1) for q in (0, 1, 50)]
    tr["side"] = tr.side.astype(str).str.upper().str[0]
    tr["o"] = tr.o.astype(str).str[0]
    fa = fa.dropna().sort_values("T", kind="stable")
    fa["lat"] = fa.recv_ms - fa["T"]
    diag["bnf_agg recv-T, мс: min/p1/p50"] = [round(float(np.percentile(fa.lat, q)), 1) for q in (0, 1, 50)]
    T, px, rcv = fa["T"].values.astype(float), fa.price.values.astype(float), fa.recv_ms.values.astype(float)
    sig_t, sig_v = sigma_series(T, px)

    books = {}
    for w, g in top.groupby("w"):
        g = g.sort_values("srv", kind="stable")
        books[int(w)] = (g.srv.values.astype(float), g.bid.values.astype(float), g.ask.values.astype(float),
                         g.bid_sz.values.astype(float), g.ask_sz.values.astype(float))
    trades = {}
    for w, g in tr.groupby("w"):
        g = g.sort_values("server_ts", kind="stable")
        trades[int(w)] = (g.server_ts.values.astype(float), g.o.values, g.side.values, g.price.values.astype(float),
                          g["size"].values.astype(float), g.tx.astype(str).values)
    src = {}
    for name in SOURCES:
        try:
            st, sp = load_source(root, name)
            if len(st) > 1000:
                src[name] = (st, sp)
        except Exception:
            pass
    diag["источники"] = list(src)

    rows = []
    for i, s in fires(T, px, N, W, refr):
        t0 = T[i]
        w = int(t0 // 1000 // 300 * 300)
        Tl = (w + 300) - t0 / 1000.0
        if not (10.0 < Tl < 295.0) or w not in books:
            continue
        bt, bb, ba, bbs, bas = books[w]
        k = np.searchsorted(bt, t0, side="right") - 1
        if k < 0:
            continue
        bid0, ask0 = bb[k], ba[k]
        if not (0.03 < bid0 < ask0 < 0.97):
            continue
        r_ask0 = ask0 if s > 0 else round(1 - bid0, 4)
        r_sz0 = bas[k] if s > 0 else bbs[k]
        mid_r0 = (bid0 + ask0) / 2 if s > 0 else 1 - (bid0 + ask0) / 2
        j0 = np.searchsorted(T, t0 - W, side="right") - 1
        dS = abs(px[i] - px[max(j0, 0)])
        sg = float(sig_v[min(max(np.searchsorted(sig_t, t0, side="right") - 1, 0), len(sig_v) - 1)])
        sd, wgt = settle_sd(Tl, sg)
        fair_r = norm_cdf(norm_inv(min(max(mid_r0, 1e-4), 1 - 1e-4)) + wgt * dS / sd)
        gap = fair_r - r_ask0
        if gap < min_gap:
            continue
        j1 = np.searchsorted(T, t0 + 1000, side="right") - 1
        row = dict(day=os.path.basename(os.path.normpath(root)), w=w, t0=t0, s=s, T=round(Tl, 2), dS=round(dS, 2),
                   dS_1s=round(s * (px[j1] - px[max(j0, 0)]), 2), sigma=round(sg, 3), bid0=bid0, ask0=ask0, r_ask0=r_ask0,
                   r_sz0=r_sz0, fair_r=round(fair_r, 4), gap=round(gap, 4), rcv_bnf=round(rcv[i] - t0, 1))
        # переоценка: ask растущего на сервере выше r_ask0
        rep = np.nan
        for m in range(k + 1, len(bt)):
            if bt[m] > t0 + 5000:
                break
            r_ask = ba[m] if s > 0 else 1 - bb[m]
            if r_ask > r_ask0 + 1e-9:
                rep = bt[m] - t0
                break
        row["rep"] = rep
        # съедания по устаревшей цене (и любые покупки растущего - спрос)
        x = trades.get(w)
        picks = []
        any_buy = np.nan
        if x is not None:
            ts, o, side, p, sz, tx = x
            a, b = np.searchsorted(ts, t0 - 500, side="left"), np.searchsorted(ts, t0 + 3000, side="right")
            seen = set()
            r_tok, f_tok = ("U", "D") if s > 0 else ("D", "U")
            for m in range(a, b):
                buy_r = o[m] == r_tok and side[m] == "B"
                sell_f = o[m] == f_tok and side[m] == "S"
                if buy_r and np.isnan(any_buy) and ts[m] >= t0:
                    any_buy = ts[m] - t0
                stale = (buy_r and p[m] <= r_ask0 + 1e-9) or (sell_f and p[m] >= 1 - r_ask0 - 1e-9)
                if not stale or (tx[m] != "nan" and tx[m] in seen):
                    continue
                seen.add(tx[m])
                picks.append((ts[m] - t0, sz[m]))
        row["any_buy"] = any_buy
        pk = np.array(picks) if picks else np.zeros((0, 2))
        after = pk[pk[:, 0] >= -200] if len(pk) else pk
        row["first_pick"] = float(after[:, 0].min()) if len(after) else np.nan
        row["n_pick"] = len(after)
        for gx in GRID:
            row[f"v{gx}"] = round(float(after[after[:, 0] <= gx, 1].sum()) if len(after) else 0.0, 2)
        row["v_all"] = round(float(after[:, 1].sum()) if len(after) else 0.0, 2)
        # осведомлённость: первый приход сообщения источника со сдвигом >= половины скачка
        for name, (st, sp) in src.items():
            b0 = np.searchsorted(st, t0 - W, side="right") - 1
            if b0 < 0:
                row[f"aw_{name}"] = np.nan
                continue
            base = sp[b0]
            e = np.searchsorted(st, t0 + 3000, side="right")
            hit = np.flatnonzero(s * (sp[b0 + 1:e] - base) >= 0.5 * dS)
            row[f"aw_{name}"] = round(st[b0 + 1 + hit[0]] - t0, 1) if len(hit) else np.nan
        rows.append(row)
    return pd.DataFrame(rows), diag


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--N", type=float, default=10.0, help="скачок, $")
    ap.add_argument("--W", type=float, default=1000.0, help="за сколько мс")
    ap.add_argument("--refr", type=float, default=2000.0)
    ap.add_argument("--min-gap", type=float, default=0.0, help="минимальное устаревание r_ask0 по модели, $")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    allr = []
    for root in a.roots:
        dname = os.path.basename(os.path.normpath(root))
        try:
            d, diag = day(root, a.N, a.W, a.refr, a.min_gap)
        except MemoryError:
            print(f"{dname}: не хватило памяти")
            continue
        print(f"{dname}: скачков {len(d)}; {diag}", flush=True)
        if len(d):
            d.to_csv(os.path.join(a.out, f"race_{dname}.csv.gz"), index=False)
            allr.append(d)
    if not allr:
        return
    r = pd.concat(allr, ignore_index=True)
    r = r[r.gap >= 0.03]
    print(f"\nскачков с устареванием >= 3 ц: {len(r)}")
    q = lambda c: [round(float(np.nanpercentile(r[c], p)), 0) if r[c].notna().any() else None for p in (10, 25, 50, 75, 90)]
    print("доля со съеданием:", round(float(r.first_pick.notna().mean()), 3), "| первое съедание, мс p10/25/50/75/90:", q("first_pick"))
    print("переоценка (ask растущего выше старого), мс:", q("rep"))
    for c in [c for c in r.columns if c.startswith("aw_")]:
        print(f"осведомлённость {c[3:]:18s} мс:", q(c), "нет:", round(float(r[c].isna().mean()), 3))


if __name__ == "__main__":
    main()
