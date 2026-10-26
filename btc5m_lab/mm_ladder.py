"""Маркет-мейкер «лесенкой» с полосой вокруг справедливой цены. Только выгрузка по записанным данным, ничего не торгует.

    python mm_ladder.py data/2026-10-12 ... --out OUT

Справедливая цена Up (как в C1): mid книги Up в момент последнего изменения mid (якорь) плюс ход Bybit с этого момента:
fair = Phi(z(mid) + w*dS/sd). Down = 1 - fair. Пересчёт каждые GRID_MS и на каждом тике Bybit, который за секунду сдвинул
справедливую цену на 1 ц и больше. Решения - по книге, дошедшей до нас; действуют на сервере через PLACE_MS.
На каждой стороне (покупка Up и покупка Down):
  * цели - K уровней: верхний = округление вниз (fair - m_in - сдвиг на остаток), дальше по 1 ц ниже, но ниже ask стороны
    (иначе заявка стала бы тейкерской - post-only отклонит);
  * заявка стоит, пока её цена в полосе [fair - m_out, fair - m_c]; вышла выше (опасно, обычно скачок BTC) или ниже
    (бесполезна) - снимаем; на свободные целевые уровни ставим новые. При смене лучшей цены книги ничего не делаем;
  * лимит остатка: заявки стороны в сумме не больше LIMIT - (своя сторона - другая), то есть |Up - Down| <= LIMIT;
  * за STOP_S до конца окна снимаем всё; позиция держится до конца окна.
Очередь: при постановке впереди весь объём на нашей цене (верх книги сервера, глубже - снимок pm_depth); если цена лучше
лучшего bid - впереди никого. Дальше очередь уменьшают сделки по нашей цене и («prop») отмены: уменьшение объёма уровня
между снимками глубины сверх сделок распределяется пропорционально между стоящими впереди и позади; уровень пропал - мы
первые. «trades» - только сделки. Сделка по худшей для продавца цене исполняет нас полностью.
Выход: ldwin_<день>.csv.gz (итог окна по вариантам) и ldagg_<день>.csv.gz (исполнения, сведённые по корзинам).
"""
from __future__ import annotations

import argparse
import math
import os

import numpy as np
import pandas as pd

from common import norm_cdf
from edge_maker import Trades
from edge_source import per_sec_sigma, winners_ptb
from lead_lag import PM, read
from mm_sim import Win, _nv, signals
from replay import load_source

WINDOW = 300
PLACE_MS = 25.0
SIZE = 5.0
LIMIT = 15.0
START_S, STOP_S = 5.0, 20.0
GRID_MS = 100.0
PX_LO, PX_HI = 0.03, 0.97
REBATE = 0.2 * 0.07
VARIANTS = {
    "L3": dict(K=3, m_in=0.01, m_c=0.005, m_out=0.05, queue="prop", skew=0.0),
    "L3_trades": dict(K=3, m_in=0.01, m_c=0.005, m_out=0.05, queue="trades", skew=0.0),
    "L3_wide": dict(K=3, m_in=0.02, m_c=0.01, m_out=0.06, queue="prop", skew=0.0),
    "L1": dict(K=1, m_in=0.01, m_c=0.005, m_out=0.03, queue="prop", skew=0.0),
    "L3_skew": dict(K=3, m_in=0.01, m_c=0.005, m_out=0.05, queue="prop", skew=0.01),
}
INF = float("inf")
_cdf = np.vectorize(norm_cdf)


class DepthDay:
    """Снимки топ-5 bid каждой стороны: время (сервер ~ локальное - 20 мс), цены и объёмы."""

    def __init__(self, root: str):
        d = read(root, "pm_depth", ["ts_ms", "w", "o"] + [f"b{i}" for i in range(1, 6)] + [f"bs{i}" for i in range(1, 6)])
        self.by = {}
        if d.empty:
            return
        for (w, o), g in d.groupby(["w", "o"]):
            g = g.sort_values("ts_ms", kind="stable")
            self.by[(int(w), str(o)[0])] = (g.ts_ms.values.astype(float) - 20.0,
                                            np.round(g[[f"b{i}" for i in range(1, 6)]].values.astype(float), 2),
                                            g[[f"bs{i}" for i in range(1, 6)]].values.astype(float))


def level_size(B, S, q):
    """Объём на цене q в снимке: 0 - уровня нет (цена лучше лучшего bid или пустой уровень внутри известных), nan - глубже."""
    if not np.isfinite(B[0]) or q > B[0] + 1e-9:
        return 0.0
    hit = np.flatnonzero(np.abs(B - q) < 1e-9)
    if len(hit):
        return float(S[hit[0]]) if np.isfinite(S[hit[0]]) else 0.0
    lo = np.nanmin(B)
    return 0.0 if q >= lo - 1e-9 else np.nan


def bucket(x, edges):
    return int(np.searchsorted(edges, x, side="right"))


class Prep:
    """Общие для всех вариантов данные окна: события и справедливая цена в моменты пересчёта."""

    def __init__(self, win: Win, dep: DepthDay, bt, bp, sig_t, sig_v):
        w = self.w = win.w
        self.win = win
        self.t_begin, self.t_stop = (w + START_S) * 1000.0, (w + WINDOW - STOP_S) * 1000.0
        # моменты пересчёта: сетка + тики Bybit со сдвигом справедливой цены >= 1 ц за секунду
        grid = np.arange(self.t_begin, self.t_stop, GRID_MS)
        sg = signals(win, bt, bp, sig_t, sig_v, [0.01])[0.01]
        te = np.unique(np.concatenate([grid, sg[1], sg[-1]]))
        te = te[(te >= self.t_begin) & (te <= self.t_stop + GRID_MS)]
        bu, au, _ = win.r["U"]
        mid = np.where(np.isfinite(bu) & np.isfinite(au), (bu + au) / 2, np.nan)
        chg = np.r_[True, ~((mid[1:] == mid[:-1]) | (np.isnan(mid[1:]) & np.isnan(mid[:-1])))]
        last = np.maximum.accumulate(np.where(chg, np.arange(len(mid)), 0))
        i = np.searchsorted(win.rt, te, side="right") - 1
        ok = i >= 0
        te, i = te[ok], i[ok]
        m = mid[i]
        ta_anchor = win.rt[last[i]]
        s_now = bp[np.clip(np.searchsorted(bt, te, side="right") - 1, 0, len(bp) - 1)]
        s_anc = bp[np.clip(np.searchsorted(bt, ta_anchor, side="right") - 1, 0, len(bp) - 1)]
        T = np.maximum((w + WINDOW) - te / 1000.0, 0.5)
        sgm = sig_v[np.clip(np.searchsorted(sig_t, te, side="right") - 1, 0, len(sig_v) - 1)]
        sd = np.where(T >= 60, sgm * np.sqrt(np.maximum(T - 40.0, 1e-9)), sgm * np.sqrt(T ** 3 / 10800.0))
        wg = np.where(T >= 60, 1.0, T / 60.0)
        good = np.isfinite(m) & (m > 0.01) & (m < 0.99)
        fair = np.full(len(te), np.nan)
        if good.any():
            fair[good] = _cdf(_nv(m[good]) + wg[good] * (s_now[good] - s_anc[good]) / sd[good])
        self.te, self.fair = te, np.clip(fair, 0.01, 0.99)
        self.askU, self.bidU = au[i], bu[i]
        # события: 0 - сделка, 1 - снимок глубины Up, 2 - снимок глубины Down, 3 - пересчёт
        tr = win.tr
        parts = [(te, np.full(len(te), 3), np.arange(len(te)))]
        if tr is not None:
            parts.append((tr[0], np.zeros(len(tr[0]), int), np.arange(len(tr[0]))))
        self.dep = {}
        for k, X in ((1, "U"), (2, "D")):
            x = dep.by.get((w, X))
            if x is not None:
                self.dep[X] = x
                parts.append((x[0], np.full(len(x[0]), k), np.arange(len(x[0]))))
        t = np.concatenate([p[0] for p in parts])
        kd = np.concatenate([p[1] for p in parts])
        ix = np.concatenate([p[2] for p in parts])
        o = np.lexsort((kd, t))
        self.ev_t, self.ev_k, self.ev_i = t[o], kd[o], ix[o]


def run_window(P: Prep, prm: dict, won: dict, day: str, var: str, agg: dict):
    win, w = P.win, P.w
    K, m_in, m_c, m_out, qmode, skew = prm["K"], prm["m_in"], prm["m_c"], prm["m_out"], prm["queue"], prm["skew"]
    orders = {"U": [], "D": []}
    qty, cost = {"U": 0.0, "D": 0.0}, {"U": 0.0, "D": 0.0}
    cnt = dict(placed=0, cancel_danger=0, cancel_far=0, cancel_stop=0, fills=0, cross=0)
    nmax, reb = 0.0, 0.0
    tr = win.tr
    T_ED, P_ED, A_ED, AH_ED = [60, 120, 200], [0.2, 0.35, 0.5, 0.65, 0.8], [500, 5000, 30000], [0.5, 50, 500]

    def fill(o, X, t, f):
        nonlocal nmax, reb
        o["rem"] -= f
        qty[X] += f
        cost[X] += f * o["q"]
        nmax = max(nmax, abs(qty["U"] - qty["D"]))
        reb += REBATE * o["q"] * (1 - o["q"]) * f
        cnt["fills"] += 1
        m5 = win.mid(X, t + 5000)
        key = (var, bucket((w + WINDOW) - t / 1000.0, T_ED), bucket(o["q"], P_ED), bucket(t - o["ta"], A_ED), bucket(o["A0"], AH_ED))
        a = agg.setdefault(key, [0, 0.0, 0.0, 0.0, 0.0])
        a[0] += 1
        a[1] += f
        a[2] += (m5 - o["q"]) * f if np.isfinite(m5) else 0.0
        a[3] += (won[X] - o["q"]) * f
        a[4] += REBATE * o["q"] * (1 - o["q"]) * f

    for t, kd, ix in zip(P.ev_t, P.ev_k, P.ev_i):
        if kd == 0:                                   # сделка рынка
            o_tok, side, px, sz = tr[1][ix], tr[2][ix], tr[3][ix], tr[4][ix]
            for X in "UD":
                if o_tok == X and side == "S":
                    eff = px
                elif o_tok != X and side == "B":
                    eff = round(1 - px, 2)
                else:
                    continue
                for o in orders[X]:
                    if o["rem"] <= 1e-9 or o["ta"] > t or o["dead"] <= t:
                        continue
                    if o["q"] > eff + 1e-9:
                        fill(o, X, t, o["rem"])
                    elif abs(o["q"] - eff) < 1e-9:
                        o["traded"] += sz
                        o["A"] -= sz
                        if o["A"] < 0:
                            f = min(-o["A"], o["rem"])
                            o["A"] = 0.0
                            fill(o, X, t, f)
        elif kd in (1, 2):                            # снимок глубины: отмены впереди нас
            X = "U" if kd == 1 else "D"
            _, B, S = P.dep[X]
            for o in orders[X]:
                if o["rem"] <= 1e-9 or o["ta"] > t or o["dead"] <= t:
                    continue
                s_new = level_size(B[ix], S[ix], o["q"])
                if not np.isfinite(s_new):
                    continue
                base = o["S_prev"] - o["traded"]
                if qmode == "prop" and np.isfinite(base) and base > 1e-9 and s_new < base and o["A"] > 0:
                    o["A"] = max(0.0, o["A"] - (base - s_new) * o["A"] / base)
                if s_new <= 1e-9:
                    o["A"] = 0.0
                o["S_prev"], o["traded"] = s_new, 0.0
        else:                                         # пересчёт справедливой цены и заявок
            fU = P.fair[ix]
            for X in "UD":
                orders[X] = [o for o in orders[X] if o["dead"] > t and o["rem"] > 1e-9]
            if t >= P.t_stop:
                for X in "UD":
                    for o in orders[X]:
                        if o["dead"] == INF:
                            o["dead"] = t + PLACE_MS
                            cnt["cancel_stop"] += 1
                continue
            if not np.isfinite(fU):
                continue
            for X in "UD":
                Y = "D" if X == "U" else "U"
                fX = fU if X == "U" else 1 - fU
                askX = P.askU[ix] if X == "U" else round(1 - P.bidU[ix], 2)
                live = []
                for o in orders[X]:
                    if o["dead"] != INF:
                        continue
                    if o["q"] > fX - m_c + 1e-9:
                        o["dead"] = t + PLACE_MS
                        cnt["cancel_danger"] += 1
                    elif o["q"] < fX - m_out - 1e-9:
                        o["dead"] = t + PLACE_MS
                        cnt["cancel_far"] += 1
                    else:
                        live.append(o)
                n_x = qty[X] - qty[Y]
                allow = LIMIT - n_x - sum(o["rem"] for o in live)
                shift = skew * n_x / SIZE
                top = math.floor((min(fX - m_in - shift, fX - m_c - 0.001)) * 100 + 1e-9) / 100
                if np.isfinite(askX):
                    top = min(top, round(askX - 0.01, 2))
                have = {round(o["q"], 2) for o in live}
                for k in range(K):
                    q = round(top - 0.01 * k, 2)
                    if allow < SIZE - 1e-9:
                        break
                    if q in have or not (PX_LO <= q <= PX_HI) or q < fX - m_out - 1e-9:
                        continue
                    ta = t + PLACE_MS
                    sb, sa, ssz = win.srv_state(X, ta)
                    if np.isfinite(sa) and sa <= q + 1e-9:
                        cnt["cross"] += 1
                        continue
                    if np.isfinite(sb) and abs(sb - q) < 1e-9:
                        A = ssz if np.isfinite(ssz) else 1e9
                    elif not np.isfinite(sb) or q > sb + 1e-9:
                        A = 0.0
                    else:
                        A = np.nan
                        x = P.dep.get(X)
                        if x is not None:
                            j = int(np.searchsorted(x[0], ta, side="right") - 1)
                            if j >= 0:
                                A = level_size(x[1][j], x[2][j], q)
                        A = 1e9 if not np.isfinite(A) else A
                    orders[X].append(dict(q=q, ta=ta, A=A, A0=A, rem=SIZE, dead=INF, S_prev=A if A < 1e8 else np.nan, traded=0.0))
                    allow -= SIZE
                    cnt["placed"] += 1
    pnl = qty["U"] * won["U"] + qty["D"] * won["D"] - cost["U"] - cost["D"]
    pairs = min(qty["U"], qty["D"])
    pair_px = (cost["U"] / qty["U"] if qty["U"] else 0) + (cost["D"] / qty["D"] if qty["D"] else 0)
    return dict(day=day, var=var, w=w, qU=qty["U"], cU=round(cost["U"], 4), qD=qty["D"], cD=round(cost["D"], 4),
                win="Up" if won["U"] else "Down", pnl=round(pnl, 4), rebate=round(reb, 4), pairs=pairs,
                pair_pnl=round(pairs * (1 - pair_px), 4) if qty["U"] and qty["D"] else 0.0, nmax=nmax, **cnt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--variants", default=",".join(VARIANTS))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    vars_ = [v for v in a.variants.split(",") if v in VARIANTS]
    for root in a.roots:
        day = os.path.basename(os.path.normpath(root))
        pm_top = read(root, "pm_top")
        if pm_top.empty:
            print(f"{day}: нет pm_top", flush=True)
            continue
        winners, _ = winners_ptb(root)
        pm = PM(pm_top)
        del pm_top
        bt, bp = load_source(root, a.source)
        if len(bt) < 1000:
            print(f"{day}: мало тиков {a.source}", flush=True)
            continue
        sig_t, sig_v = per_sec_sigma(bt, bp)
        dep, tr = DepthDay(root), Trades(root)
        wrows, agg, bad = [], {}, []
        for w in sorted(winners):
            if w not in pm.by_w:
                continue
            try:
                win = Win(w, pm, tr, {})
                if len(win.rt) < 10:
                    continue
                P = Prep(win, dep, bt, bp, sig_t, sig_v)
                won = {"U": 1.0 if winners[w] == "Up" else 0.0, "D": 1.0 if winners[w] == "Down" else 0.0}
                for v in vars_:
                    wrows.append(run_window(P, VARIANTS[v], won, day, v, agg))
            except Exception as ex:          # одно окно не должно ронять весь день
                bad.append(f"{w}: {ex!r}"[:160])
        if bad:
            print(f"{day}: пропущено окон из-за ошибок {len(bad)}, первая: {bad[0]}", flush=True)
        W = pd.DataFrame(wrows)
        A = pd.DataFrame([dict(day=day, var=k[0], Tb=k[1], pb=k[2], ageb=k[3], ahb=k[4], n=v[0], qty=v[1], mk5=v[2], out=v[3], reb=v[4])
                          for k, v in agg.items()])
        W.to_csv(os.path.join(a.out, f"ldwin_{day}.csv.gz"), index=False)
        A.to_csv(os.path.join(a.out, f"ldagg_{day}.csv.gz"), index=False)
        if len(W):
            g = W.groupby("var").agg(окон=("w", "size"), pnl=("pnl", "sum"), доля=("rebate", "sum"), пары=("pair_pnl", "sum"),
                                     шейров=("qU", "sum"), заявок=("placed", "sum"))
            print(f"{day}: окон {W.w.nunique()}\n{g.round(1).to_string()}", flush=True)


if __name__ == "__main__":
    main()
