"""Симуляция простого маркет-мейкера на 5-минутных рынках BTC по записанным данным. Только выгрузка, ничего не торгует.

    python mm_sim.py data/2026-10-12 data/2026-10-13 ... --out OUT

Стратегия (на каждое окно, с 5-й секунды и до STOP_S секунд до конца):
  * держим две заявки на покупку по SIZE шейров: Up по лучшему bid Up и Down по лучшему bid Down (= 1 - лучший ask Up),
    то есть стоим в лучших ценах обеих сторон. Пара Up + Down стоит 1 - спред, к концу окна она всегда стоит ровно $1;
  * решение принимается по книге, ДОШЕДШЕЙ до нас (время получения), заявка действует на сервере через PLACE_MS;
  * лучшая цена стороны сменилась (видим по своей копии книги) - снимаем и переставляем на новую лучшую цену
    (снятие и новая заявка действуют через PLACE_MS; с новой заявкой мы в конце очереди);
  * сигнал (вариант): Bybit за последнюю секунду сдвинулся так, что справедливая цена Up сдвинулась на theta и больше
    (сдвиг = phi(z)*w*dS/sd, z по mid Up, sd как в модели C1) - снимаем заявку стороны, которая дешевеет (вниз - Up,
    вверх - Down), через PLACE_MS после прихода тика; эту сторону не котируем COOLDOWN_MS;
  * лимит остатка: заявку стороны ставим, только если после её полного исполнения |Up - Down| <= LIMIT шейров;
  * за STOP_S секунд до конца снимаем всё, позиция держится до конца окна (победивший токен платит $1).
Исполнение - только по сделкам рынка (pm_trades, время сервера): продажа нашего токена по нашей цене или покупка
другого по 1 - наша цена съедают очередь впереди, затем нас; сделка «сквозь» нашу цену (по худшей для продавца цене)
исполняет нас полностью. Очередь впереди: «back» - объём на нашей цене в снимке pm_depth (мы в конце очереди), «front» -
0 (мы первые, верхняя граница). Варианты: очередь x сигнал (нет / 3 ц / 1,5 ц).
Выход: mmfill_<день>.csv.gz (каждое исполнение: маркауты mid через 1/5/30 с, исход) и mmwin_<день>.csv.gz (итог окна).
"""
from __future__ import annotations

import argparse
import math
import os

import numpy as np
import pandas as pd

from common import norm_inv
from edge_maker import Depth, Trades
from edge_source import per_sec_sigma, winners_ptb
from lead_lag import PM, read
from replay import load_source

WINDOW = 300
PLACE_MS = 25.0
SIZE = 5.0
LIMIT = 10.0
START_S = 5.0
STOP_S = 20.0
COOLDOWN_MS = 1000.0
FILL_REACT_MS = 50.0
PX_LO, PX_HI = 0.05, 0.95
VARIANTS = [("back", None), ("back", 0.03), ("back", 0.015), ("front", None), ("front", 0.03), ("front", 0.015)]
INF = float("inf")
_nv = np.vectorize(lambda p: norm_inv(min(max(float(p), 1e-4), 1 - 1e-4)))


def side_arrays(s: dict):
    """bid/ask обеих сторон из книги Up (цены в центах, округлены); размер на лучшем bid стороны."""
    bid, ask = np.round(s["bid"].astype(float), 2), np.round(s["ask"].astype(float), 2)
    return {"U": (bid, ask, s["bsz"].astype(float)), "D": (np.round(1 - ask, 2), np.round(1 - bid, 2), s["asz"].astype(float))}


def next_change(v: np.ndarray) -> np.ndarray:
    """Для каждого индекса i - первый индекс j > i, где v[j] != v[i] (len(v), если такого нет)."""
    v = np.where(np.isfinite(v), v, -1.0)
    ch = np.flatnonzero(v[1:] != v[:-1]) + 1
    if len(ch) == 0:
        return np.full(len(v), len(v))
    k = np.searchsorted(ch, np.arange(len(v)), side="right")
    return np.where(k < len(ch), ch[np.minimum(k, len(ch) - 1)], len(v))


class Win:
    """Данные одного окна: книга в двух видах, сделки, сигналы."""

    def __init__(self, w, pm: PM, tr: Trades, sig: dict):
        self.w = w
        rcv, srv = pm.by_w[w]["rcv"], pm.by_w[w]["srv"]
        self.rt, self.st = rcv["t"], srv["t"]
        self.r, self.s = side_arrays(rcv), side_arrays(srv)
        self.nc = {X: next_change(self.r[X][0]) for X in "UD"}
        self.tr = tr.by.get(w)
        self.sig = sig

    def rcv_idx(self, t):
        return int(np.searchsorted(self.rt, t, side="right") - 1)

    def srv_state(self, X, t):
        i = int(np.searchsorted(self.st, t, side="right") - 1)
        if i < 0:
            return np.nan, np.nan, np.nan
        b, a, z = self.s[X]
        return b[i], a[i], z[i]

    def mid(self, X, t):
        b, a, _ = self.srv_state(X, t)
        return (a + b) / 2 if np.isfinite(a) and np.isfinite(b) else np.nan


def signals(win: Win, bt, bp, sig_t, sig_v, thetas):
    """Тики Bybit в окне, где сдвиг справедливой цены Up за последнюю секунду >= theta: {theta: {+1: times, -1: times}}."""
    w = win.w
    a, b = np.searchsorted(bt, w * 1000.0, "left"), np.searchsorted(bt, (w + WINDOW) * 1000.0, "right")
    out = {th: {1: np.array([]), -1: np.array([])} for th in thetas}
    if b - a < 10:
        return out
    t, p = bt[a:b], bp[a:b]
    j = np.searchsorted(bt, t - 1000.0, side="right") - 1
    mv = p - bp[np.maximum(j, 0)]
    keep = np.abs(mv) >= 2.0
    if not keep.any():
        return out
    t, mv = t[keep], mv[keep]
    i = np.searchsorted(win.rt, t, side="right") - 1
    ok = i >= 0
    t, mv, i = t[ok], mv[ok], i[ok]
    bu, au, _ = win.r["U"]
    mid = (bu[i] + au[i]) / 2
    ok = np.isfinite(mid) & (mid > 0.01) & (mid < 0.99)
    t, mv, mid = t[ok], mv[ok], mid[ok]
    if not len(t):
        return out
    T = np.maximum((w + WINDOW) - t / 1000.0, 0.5)
    sg = sig_v[np.clip(np.searchsorted(sig_t, t, side="right") - 1, 0, len(sig_v) - 1)]
    sd = np.where(T >= 60, sg * np.sqrt(np.maximum(T - 40.0, 1e-9)), sg * np.sqrt(T ** 3 / 10800.0))
    wg = np.where(T >= 60, 1.0, T / 60.0)
    z = _nv(mid)
    dF = np.exp(-z * z / 2) / math.sqrt(2 * math.pi) * wg * mv / sd
    for th in thetas:
        for d in (1, -1):
            out[th][d] = t[d * dF >= th]
    return out


def fills_for(win: Win, X: str, q: float, ahead: float, ta: float, te: float):
    """Исполнения нашей заявки BUY X по q за [ta, te): список (время сервера, шейров) до SIZE."""
    x = win.tr
    if x is None or te <= ta:
        return []
    ts, o, side, px, sz = x
    i0, i1 = np.searchsorted(ts, ta, "left"), np.searchsorted(ts, te, "left")
    mirror = round(1 - q, 2)
    rem, out = SIZE, []
    for i in range(i0, i1):
        if o[i] == X and side[i] == "S":
            at, thr = abs(px[i] - q) < 1e-9, px[i] < q - 1e-9
        elif o[i] != X and side[i] == "B":
            at, thr = abs(px[i] - mirror) < 1e-9, px[i] > mirror + 1e-9
        else:
            continue
        if thr:
            out.append((ts[i], rem))
            return out
        if not at:
            continue
        ahead -= sz[i]
        if ahead < 0:
            f = min(-ahead, rem)
            ahead = 0.0
            rem -= f
            out.append((ts[i], f))
            if rem <= 1e-9:
                return out
    return out


def run_window(win: Win, dep: Depth, queue: str, theta, won: dict, day: str, var: str):
    w = win.w
    t_begin, t_stop = (w + START_S) * 1000.0, (w + WINDOW - STOP_S) * 1000.0
    sig = win.sig.get(theta) if theta is not None else None
    qty, cost = {"U": 0.0, "D": 0.0}, {"U": 0.0, "D": 0.0}
    orders = {"U": None, "D": None}
    wake = {"U": t_begin, "D": t_begin}
    blocked = {"U": False, "D": False}
    fills, cnt = [], {"orders": 0, "touch": 0, "signal": 0, "stop": 0, "filled": 0, "cross": 0}
    nmax = 0.0

    def try_place(X, td):
        if td >= t_stop:
            wake[X] = INF
            return
        n = qty["U"] - qty["D"]
        n_after = n + (SIZE if X == "U" else -SIZE)
        if abs(n_after) > LIMIT + 1e-9 and abs(n_after) > abs(n):
            blocked[X], wake[X] = True, INF
            return
        blocked[X] = False
        i = win.rcv_idx(td)
        if i < 0:
            wake[X] = td + 500
            return
        b, a, _ = win.r[X]
        q = b[i]
        nxt = win.nc[X][i]
        t_next = win.rt[nxt] if nxt < len(win.rt) else INF
        if not (np.isfinite(q) and np.isfinite(a[i]) and PX_LO <= q <= PX_HI and a[i] > q):
            wake[X] = t_next if t_next < INF else td + 1000
            return
        ta = td + PLACE_MS
        sb, sa, ssz = win.srv_state(X, ta)
        if np.isfinite(sa) and sa <= q + 1e-9:          # на сервере уже пересекла бы спред: post-only отклонит
            cnt["cross"] += 1
            wake[X] = t_next if t_next < INF else td + 1000
            return
        if queue == "front":
            ahead = 0.0
        else:
            ahead = dep.bid_size_at(w, X, ta + 43.0, q)
            if not np.isfinite(ahead):
                ahead = ssz if np.isfinite(sb) and abs(sb - q) < 1e-9 else 1e9
        # естественный конец заявки
        end, reason, nxt_dec = t_stop + PLACE_MS, "stop", INF
        if t_next + PLACE_MS < end:
            end, reason, nxt_dec = t_next + PLACE_MS, "touch", t_next
        if sig is not None:
            st = sig[-1 if X == "U" else 1]
            k = np.searchsorted(st, td, side="right")
            if k < len(st) and st[k] + PLACE_MS < end:
                end, reason, nxt_dec = st[k] + PLACE_MS, "signal", st[k] + COOLDOWN_MS
        fl = fills_for(win, X, q, ahead, ta, end)
        if fl and sum(f for _, f in fl) >= SIZE - 1e-9:
            end, reason, nxt_dec = fl[-1][0], "filled", fl[-1][0] + FILL_REACT_MS
        orders[X] = dict(q=q, ta=ta, ahead=ahead, fl=fl, k=0, end=end, reason=reason, nxt=nxt_dec)
        cnt["orders"] += 1
        wake[X] = INF

    while True:
        # ближайшее событие: исполнение, конец заявки или попытка поставить
        best_t, best = INF, None
        for X in "UD":
            o = orders[X]
            if o is not None:
                t_ev = o["fl"][o["k"]][0] if o["k"] < len(o["fl"]) else o["end"]
                kind = "fill" if o["k"] < len(o["fl"]) else "end"
            else:
                t_ev, kind = wake[X], "wake"
            if t_ev < best_t:
                best_t, best = t_ev, (X, kind)
        if best is None or best_t == INF:
            break
        X, kind = best
        if kind == "fill":
            o = orders[X]
            t, f = o["fl"][o["k"]]
            o["k"] += 1
            qty[X] += f
            cost[X] += f * o["q"]
            nmax = max(nmax, abs(qty["U"] - qty["D"]))
            T = (w + WINDOW) - t / 1000.0
            m0 = win.mid(X, t)
            fills.append(dict(day=day, var=var, w=w, t=t, X=X, q=o["q"], qty=f, T=round(T, 1), ahead=o["ahead"],
                              age=round(t - o["ta"]), m0=m0, m1=win.mid(X, t + 1000), m5=win.mid(X, t + 5000),
                              m30=win.mid(X, t + 30000), won=won[X], n_after=qty["U"] - qty["D"]))
            Y = "D" if X == "U" else "U"
            if blocked[Y]:
                try_place(Y, t)
        elif kind == "end":
            o = orders[X]
            cnt[o["reason"]] += 1
            orders[X] = None
            wake[X] = o["nxt"]
        else:
            try_place(X, best_t)
    pnl = qty["U"] * won["U"] + qty["D"] * won["D"] - cost["U"] - cost["D"]
    pairs = min(qty["U"], qty["D"])
    pair_px = (cost["U"] / qty["U"] if qty["U"] else 0) + (cost["D"] / qty["D"] if qty["D"] else 0)
    row = dict(day=day, var=var, w=w, qU=qty["U"], cU=round(cost["U"], 4), qD=qty["D"], cD=round(cost["D"], 4),
               win="Up" if won["U"] else "Down", pnl=round(pnl, 4), pairs=pairs,
               pair_pnl=round(pairs * (1 - pair_px), 4) if qty["U"] and qty["D"] else 0.0, nmax=nmax, **cnt)
    return row, fills


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--source", default="bybit")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    thetas = sorted({th for _, th in VARIANTS if th is not None})
    for root in a.roots:
        day = os.path.basename(os.path.normpath(root))
        try:
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
            dep, tr = Depth(root), Trades(root)
            wrows, frows, bad = [], [], []
            for w in sorted(winners):
                if w not in pm.by_w:
                    continue
                try:
                    win = Win(w, pm, tr, {})
                    if len(win.rt) < 10:
                        continue
                    win.sig = signals(win, bt, bp, sig_t, sig_v, thetas)
                    won = {"U": 1.0 if winners[w] == "Up" else 0.0, "D": 1.0 if winners[w] == "Down" else 0.0}
                    for queue, th in VARIANTS:
                        var = f"{queue}_{'nosig' if th is None else f'sig{round(th * 1000)}'}"
                        r, f = run_window(win, dep, queue, th, won, day, var)
                        wrows.append(r)
                        frows += f
                except Exception as ex:          # одно окно не должно ронять весь день
                    bad.append(f"{w}: {ex!r}"[:120])
            if bad:
                print(f"{day}: пропущено окон из-за ошибок {len(bad)}, первая: {bad[0]}", flush=True)
            W, F = pd.DataFrame(wrows), pd.DataFrame(frows)
            W.to_csv(os.path.join(a.out, f"mmwin_{day}.csv.gz"), index=False)
            F.to_csv(os.path.join(a.out, f"mmfill_{day}.csv.gz"), index=False)
            g = W.groupby("var").agg(окон=("w", "size"), pnl=("pnl", "sum"), пары=("pair_pnl", "sum"), шейров=("qU", "sum"))
            print(f"{day}: окон {W.w.nunique()}, исполнений {len(F)}; {tr.diag}\n{g.round(2).to_string()}", flush=True)
        except MemoryError:
            print(f"{day}: не хватило памяти", flush=True)


if __name__ == "__main__":
    main()
