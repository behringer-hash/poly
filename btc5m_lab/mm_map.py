"""Мейкер по карте потока (claude/flow_map.md): лесенка от лучшего bid на обе стороны + снятие «ударяемой» стороны по
ходу фьючерса Binance. Только повторный прогон по записанным данным, ничего не торгует.

    python mm_map.py DATA_DIR/2026-10-27 [...] --out OUT [--variants A0,A1,...]

Сторона X: покупка Up (U) или покупка Down (D); bid Down = 1 - ask Up. Решения - по книге, дошедшей до сборщика
(Стокгольм), раз в GRID_MS; заявка/отмена начинает действовать на сервере через PLACE_MS.
  * цели: уровни bid_X - k ц для k из OFFS (не дороже ask_X - 1 ц: post-only), цена в [PX_LO, PX_HI];
  * заявка «липкая»: стоит, пока bid_X - q <= max(OFFS) + 2 ц и q <= bid_X (рынок не ушёл ниже нас - иначе мы одни
    наверху, это обычно перед продажами - снимаем);
  * защита: сделка фьючерса Binance (время биржи T), ход за SIG_W мс >= SIG_USD $. BTC вверх - дорожает Up, тейкеры
    покупают Up у ask Up = у наших заявок на покупку Down: снимаем сторону D (вниз - сторону U). «sym» - обе стороны.
    Отмена действует на сервере через CANCEL_MS после T; новые заявки этой стороны не ставим COOLDOWN_MS;
  * лимиты: |Up - Down| (с заявками) <= LIMIT шейров, на сторону за окно <= MAXW шейров;
  * окно котирования [START_S, WINDOW - STOP_S] с начала окна; позиция держится до исхода.
Очередь (как в mm_ladder): впереди - объём на нашей цене при постановке (лучший bid сервера; глубже - снимок pm_depth;
глубже 5 уровней - «бесконечно»); сделки по нашей цене съедают очередь, потом нас; сделка по худшей цене исполняет нас
целиком; «prop» - отмены впереди (уменьшение уровня между снимками сверх сделок) сокращают очередь пропорционально,
«trades» - только сделки (пессимистично).
Выход: mmwin_<день>.csv.gz (окно x вариант), mmagg_<день>.csv.gz (исполнения по корзинам: время, уровень k, ход BTC
для тейкера, цена; исход, маркауты mid через 5 и 60 с, ребейт 20% комиссии).
"""
from __future__ import annotations

import argparse
import os
import time

import numpy as np
import pandas as pd

from edge_maker import Trades
from edge_source import winners_ptb
from lead_lag import PM, read
from mm_ladder import DepthDay, level_size
from mm_sim import Win

WINDOW = 300
GRID_MS = 100.0
PLACE_MS = 40.0
PX_LO, PX_HI = 0.05, 0.95
REBATE = 0.2 * 0.07
BASE = dict(OFFS=(0, 1, 2, 3), SIZE=10.0, LIMIT=60.0, MAXW=5000.0, START_S=5.0, STOP_S=15.0, prot="asym", SIG_USD=4.0,
            SIG_W=300.0, CANCEL_MS=175.0, COOLDOWN_MS=1000.0, queue="prop", alone=True, qf=1.0,
            MOM_MS=0.0, MOM_C=0.0, MOM_CANCEL=False, prot_src="bnf")
# M*: как торгует x-MoneyForWhiskas (claude/wallet_moneyforwhiskas_1029.md, раздел 8): заявка только по лучшему bid и
# только на токен, чей mid вырос >= MOM_C ц за MOM_MS (по книге сборщика); снятие по ходу BTC против на любой из бирж
# (фьючерс Binance, Bybit, Coinbase); позицию не выравниваем (LIMIT большой).
_M = dict(OFFS=(0,), MOM_MS=10000.0, MOM_C=3.0, MOM_CANCEL=True, prot_src="all", SIG_USD=3.0, LIMIT=300.0)
VARIANTS = {
    "A0": {},                                             # основное правило
    "A1_noprot": dict(prot="none"),
    "A2_sym": dict(prot="sym"),
    "A3_L123": dict(OFFS=(1, 2, 3)),
    "A4_L0": dict(OFFS=(0,)),
    "A5_L2_6": dict(OFFS=(2, 3, 4, 5, 6)),
    "A6_c300": dict(CANCEL_MS=300.0),
    "A7_qtrades": dict(queue="trades"),
    "A8_sig2": dict(SIG_USD=2.0),
    # место в очереди: qf - доля объёма уровня впереди нас при постановке (1 - в конце очереди, 0 - первые)
    "Q0_back": {},
    "Q1_half": dict(qf=0.5),
    "Q2_front": dict(qf=0.0),
    "Q2_front_noprot": dict(qf=0.0, prot="none"),
    "Q2_front_L123": dict(qf=0.0, OFFS=(1, 2, 3)),
    "M0_mom": dict(_M),
    "M1_nomom": dict(_M, MOM_MS=0.0, MOM_C=0.0, MOM_CANCEL=False),
    "M2_mom_front": dict(_M, qf=0.0),
    "M3_mom5s2c": dict(_M, MOM_MS=5000.0, MOM_C=2.0),
    "M4_mom_keep": dict(_M, MOM_CANCEL=False),
    "M5_mom_fut": dict(_M, prot_src="bnf"),
    "M6_mom_L01": dict(_M, OFFS=(0, 1)),
    "M7_antimom": dict(_M, MOM_C=-3.0),
    "M8_nomom_front": dict(_M, MOM_MS=0.0, MOM_C=0.0, MOM_CANCEL=False, qf=0.0),
}
A_ED = [0.5, 100, 1000, 1e8]
INF = float("inf")
T_ED = [0, 30, 60, 120, 180, 240, 270]
P_ED = [0.1, 0.25, 0.4, 0.6, 0.75, 0.9]
B_ED = [-10, -3, 3, 10]


def bucket(x, edges):
    return int(np.searchsorted(edges, x, side="right"))


def btc_signals(bT, bP, w, W, thr, start, stop):
    """Сделки фьючерса в окне с ходом за W мс >= thr: (время биржи, знак), не чаще одного на знак за 200 мс."""
    a, b = np.searchsorted(bT, start - 2000, "left"), np.searchsorted(bT, stop, "right")
    if b - a < 5:
        return np.array([]), np.array([])
    t, p = bT[a:b], bP[a:b]
    j = np.searchsorted(bT, t - W, side="right") - 1
    mv = p - bP[np.maximum(j, 0)]
    k = np.abs(mv) >= thr
    t, s = t[k], np.sign(mv[k])
    keep, last = [], {1.0: -INF, -1.0: -INF}
    for i in range(len(t)):
        if t[i] - last[s[i]] >= 200:
            keep.append(i)
            last[s[i]] = t[i]
    return t[keep], s[keep]


class Prep:
    def __init__(self, win: Win, dep: DepthDay, bT, bP, extra=None):
        self.win, self.w = win, win.w
        self.dep = {X: dep.by.get((win.w, X)) for X in "UD"}
        self.bT, self.bP = bT, bP
        self.extra = extra or []                     # [(T, P)] доп. биржи для защиты (Bybit, Coinbase)


def events_for(P: Prep, prm):
    w, win = P.w, P.win
    t0, t1 = (w + prm["START_S"]) * 1000.0, (w + WINDOW - prm["STOP_S"]) * 1000.0
    parts = [(np.arange(t0, t1 + GRID_MS, GRID_MS), 3, None)]
    tr = win.tr
    if tr is not None:
        parts.append((tr[0], 0, None))
    for k, X in ((1, "U"), (2, "D")):
        x = P.dep[X]
        if x is not None:
            parts.append((x[0], k, None))
    if prm["prot"] != "none":
        srcs = [(P.bT, P.bP)] + (P.extra if prm["prot_src"] == "all" else [])
        for xT, xP in srcs:
            st, ss = btc_signals(xT, xP, w, prm["SIG_W"], prm["SIG_USD"], t0, t1)
            parts.append((st + prm["CANCEL_MS"], 4, ss))
    T, K, I, S = [], [], [], []
    for t, k, s in parts:
        T.append(t)
        K.append(np.full(len(t), k))
        I.append(np.arange(len(t)))
        S.append(s if s is not None else np.zeros(len(t)))
    t, k, i, s = (np.concatenate(x) for x in (T, K, I, S))
    o = np.lexsort((k, t))
    return t[o], k[o], i[o], s[o]


def run_window(P: Prep, prm: dict, won: dict, day: str, var: str, agg: dict):
    win, w = P.win, P.w
    OFFS, SIZE, LIMIT, MAXW = prm["OFFS"], prm["SIZE"], prm["LIMIT"], prm["MAXW"]
    maxoff = max(OFFS)
    orders = {"U": [], "D": []}
    qty, cost = {"U": 0.0, "D": 0.0}, {"U": 0.0, "D": 0.0}
    block = {"U": -INF, "D": -INF}
    cnt = dict(placed=0, c_sig=0, c_alone=0, c_far=0, c_stop=0, fills=0, cross=0)
    reb = 0.0
    tr = win.tr
    bT, bP = P.bT, P.bP
    t_stop = (w + WINDOW - prm["STOP_S"]) * 1000.0

    def btc_move(t, dirm):
        i = int(np.searchsorted(bT, t, side="right") - 1)
        j = int(np.searchsorted(bT, t - 1000, side="right") - 1)
        if i < 0 or j < 0:
            return np.nan
        return -dirm * (bP[i] - bP[j])                   # ход за 1 с в сторону тейкера (тейкер против мейкера)

    def fill(o, X, t, f, kind):
        nonlocal reb
        o["rem"] -= f
        qty[X] += f
        cost[X] += f * o["q"]
        r = REBATE * o["q"] * (1 - o["q"]) * f
        reb += r
        cnt["fills"] += 1
        m5, m60 = win.mid(X, t + 5000), win.mid(X, t + 60000)
        mv = btc_move(t, 1 if X == "U" else -1)
        key = (var, bucket(t / 1000.0 - w, T_ED), o["k"], bucket(mv, B_ED) if np.isfinite(mv) else -1,
               bucket(o["q"], P_ED), kind, bucket(o["A0"], A_ED))
        a = agg.setdefault(key, [0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        a[0] += 1
        a[1] += f
        a[2] += (won[X] - o["q"]) * f
        if np.isfinite(m5):
            a[3] += (m5 - o["q"]) * f
            a[4] += f
        if np.isfinite(m60):
            a[5] += (m60 - o["q"]) * f
            a[6] += f
        a[7] += r

    ev_t, ev_k, ev_i, ev_s = events_for(P, prm)
    for t, kd, ix, sg in zip(ev_t, ev_k, ev_i, ev_s):
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
                        fill(o, X, t, o["rem"], 1)
                    elif abs(o["q"] - eff) < 1e-9:
                        o["traded"] += sz
                        o["A"] -= sz
                        if o["A"] < 0:
                            f = min(-o["A"], o["rem"])
                            o["A"] = 0.0
                            fill(o, X, t, f, 0)
        elif kd in (1, 2):                            # снимок глубины: отмены впереди
            X = "U" if kd == 1 else "D"
            _, B, S = P.dep[X]
            for o in orders[X]:
                if o["rem"] <= 1e-9 or o["ta"] > t or o["dead"] <= t:
                    continue
                s_new = level_size(B[ix], S[ix], o["q"])
                if not np.isfinite(s_new):
                    continue
                base = o["S_prev"] - o["traded"]
                if prm["queue"] == "prop" and np.isfinite(base) and base > 1e-9 and s_new < base and o["A"] > 0:
                    o["A"] = max(0.0, o["A"] - (base - s_new) * o["A"] / base)
                if s_new <= 1e-9:
                    o["A"] = 0.0
                o["S_prev"], o["traded"] = s_new, 0.0
        elif kd == 4:                                 # ход BTC: отмена действует сейчас (время уже сдвинуто)
            hit = ["D"] if sg > 0 else ["U"]
            if prm["prot"] == "sym":
                hit = ["U", "D"]
            for X in hit:
                for o in orders[X]:
                    if o["dead"] == INF and o["rem"] > 1e-9:
                        o["dead"] = t
                        cnt["c_sig"] += 1
                block[X] = max(block[X], t - PLACE_MS + prm["COOLDOWN_MS"])
        else:                                         # пересчёт заявок по книге сборщика
            for X in "UD":
                orders[X] = [o for o in orders[X] if o["dead"] > t and o["rem"] > 1e-9]
            if t >= t_stop:
                for X in "UD":
                    for o in orders[X]:
                        if o["dead"] == INF:
                            o["dead"] = t + PLACE_MS
                            cnt["c_stop"] += 1
                continue
            i = win.rcv_idx(t)
            if i < 0:
                continue
            for X in "UD":
                Y = "D" if X == "U" else "U"
                bidX, askX = win.r[X][0][i], win.r[X][1][i]
                if not np.isfinite(bidX):
                    continue
                live = []
                for o in orders[X]:
                    if o["dead"] != INF:
                        continue
                    if prm["alone"] and o["q"] > bidX + 1e-9:
                        o["dead"] = t + PLACE_MS
                        cnt["c_alone"] += 1
                    elif o["q"] < bidX - (maxoff + 2) / 100 - 1e-9:
                        o["dead"] = t + PLACE_MS
                        cnt["c_far"] += 1
                    else:
                        live.append(o)
                if prm["MOM_MS"] > 0:
                    j = win.rcv_idx(t - prm["MOM_MS"])
                    b0, a0 = (win.r[X][0][j], win.r[X][1][j]) if j >= 0 else (np.nan, np.nan)
                    m_now = (bidX + askX) / 2 if np.isfinite(askX) else np.nan
                    m_then = (b0 + a0) / 2 if np.isfinite(b0) and np.isfinite(a0) else np.nan
                    d = 100 * (m_now - m_then) if np.isfinite(m_now) and np.isfinite(m_then) else np.nan
                    ok = np.isfinite(d) and (d >= prm["MOM_C"] if prm["MOM_C"] >= 0 else d <= prm["MOM_C"])
                    if not ok:
                        if prm["MOM_CANCEL"]:
                            for o in live:
                                o["dead"] = t + PLACE_MS
                                cnt["c_far"] += 1
                        continue
                if t < block[X]:
                    continue
                pend = sum(o["rem"] for o in live)
                allow = min(LIMIT - (qty[X] - qty[Y]) - pend, MAXW - qty[X] - pend)
                have = {round(o["q"], 2) for o in live}
                for k in OFFS:
                    if allow < SIZE - 1e-9:
                        break
                    q = round(bidX - k / 100, 2)
                    if q in have or not (PX_LO <= q <= PX_HI):
                        continue
                    if np.isfinite(askX) and q > askX - 0.01 + 1e-9:
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
                        x = P.dep[X]
                        if x is not None:
                            j = int(np.searchsorted(x[0], ta, side="right") - 1)
                            if j >= 0:
                                A = level_size(x[1][j], x[2][j], q)
                        A = 1e9 if not np.isfinite(A) else A
                    if prm["qf"] < 1:
                        A = 0.0 if prm["qf"] <= 0 else (A * prm["qf"] if A < 1e8 else A)
                    orders[X].append(dict(q=q, k=k, ta=ta, A=A, A0=A, rem=SIZE, dead=INF,
                                          S_prev=A if A < 1e8 else np.nan, traded=0.0))
                    allow -= SIZE
                    cnt["placed"] += 1
    pnl = qty["U"] * won["U"] + qty["D"] * won["D"] - cost["U"] - cost["D"]
    pairs = min(qty["U"], qty["D"])
    return dict(day=day, var=var, w=w, qU=qty["U"], cU=round(cost["U"], 4), qD=qty["D"], cD=round(cost["D"], 4),
                win="Up" if won["U"] else "Down", pnl=round(pnl, 4), rebate=round(reb, 4), pairs=pairs, **cnt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--variants", default=",".join(v for v in VARIANTS if v.startswith("A")))
    ap.add_argument("--max-windows", type=int, default=0)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    vars_ = [v for v in a.variants.split(",") if v in VARIANTS]
    prms = {v: {**BASE, **VARIANTS[v]} for v in vars_}
    for root in a.roots:
        t_day = time.time()
        day = os.path.basename(os.path.normpath(root))
        pm_top = read(root, "pm_top")
        if pm_top.empty:
            print(f"{day}: нет pm_top", flush=True)
            continue
        winners, _ = winners_ptb(root)
        pm = PM(pm_top)
        del pm_top
        b = read(root, "bnf_agg", ["T", "price"]).dropna()
        b = b.sort_values("T", kind="stable")
        bT, bP = b["T"].values.astype(float), b.price.values.astype(float)
        del b
        extra = []
        for st, tc in (("by_trade", "T"), ("cb_ticker", "t_ms")):
            try:
                x = read(root, st, [tc, "price"]).dropna().sort_values(tc, kind="stable")
                if len(x):
                    extra.append((x[tc].values.astype(float), x.price.values.astype(float)))
            except Exception as ex:
                print(f"{day}: {st} не прочитан: {ex!r}", flush=True)
        dep, tr = DepthDay(root), Trades(root)
        wrows, agg, bad = [], {}, []
        ws = [w for w in sorted(winners) if w in pm.by_w]
        if a.max_windows:
            ws = ws[:a.max_windows]
        for w in ws:
            try:
                win = Win(w, pm, tr, {})
                if len(win.rt) < 10:
                    continue
                P = Prep(win, dep, bT, bP, extra)
                won = {"U": 1.0 if winners[w] == "Up" else 0.0, "D": 1.0 if winners[w] == "Down" else 0.0}
                for v in vars_:
                    wrows.append(run_window(P, prms[v], won, day, v, agg))
            except Exception as ex:          # одно окно не должно ронять весь день
                bad.append(f"{w}: {ex!r}"[:160])
        if bad:
            print(f"{day}: пропущено окон из-за ошибок {len(bad)}, первая: {bad[0]}", flush=True)
        W = pd.DataFrame(wrows)
        A = pd.DataFrame([dict(day=day, var=k[0], tb=k[1], k=k[2], bb=k[3], pb=k[4], ft=k[5], ab=k[6], n=v[0], qty=v[1], out=v[2],
                               m5=v[3], s5=v[4], m60=v[5], s60=v[6], reb=v[7]) for k, v in agg.items()])
        W.to_csv(os.path.join(a.out, f"mmwin_{day}.csv.gz"), index=False)
        A.to_csv(os.path.join(a.out, f"mmagg_{day}.csv.gz"), index=False)
        if len(W):
            W["sh"] = W.qU + W.qD
            g = W.groupby("var").agg(окон=("w", "size"), pnl=("pnl", "sum"), ребейт=("rebate", "sum"), шейров=("sh", "sum"),
                                     заявок=("placed", "sum"), снято_сигнал=("c_sig", "sum"))
            g["ц_шейр"] = 100 * g.pnl / g.шейров
            print(f"{day}: окон {W.w.nunique()}, {time.time() - t_day:.0f} с\n{g.round(2).to_string()}", flush=True)


if __name__ == "__main__":
    main()
