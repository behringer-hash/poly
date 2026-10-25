"""Вход лимитной заявкой (мейкером) после сигнала C1 и в случайные моменты для сравнения. Только выгрузка данных.

    python edge_maker.py data/2026-10-12 ... --out OUT

Для каждого сигнала C1 (как в боте: порог 3,5 ц, sigma x1, Bybit, якорь в момент изменения книги) и для контрольных
моментов без сигнала (40/100/160/220 с от начала окна, обе стороны) ставим заявку BUY 5 шейров своей стороны:
  * решение через D = 0 / 1000 / 3000 мс после сигнала по книге, дошедшей до нас; цена - лучший bid стороны (join)
    или bid + 1 ц, если спред не меньше 2 ц (improve); заявка начинает действовать на сервере через 25 мс;
  * если к этому моменту на сервере лучший ask стороны не выше нашей цены, заявка была бы исполнена как тейкер - не ставим;
  * очередь впереди: объём на нашей цене в последнем снимке pm_depth (cons) или 0 (front, верхняя граница);
  * исполнение только по сделкам рынка (pm_trades, время сервера): продажа нашего токена по нашей цене или покупка
    другого токена по 1 - наша цена съедают очередь (all), или только первое (same); сделка «сквозь» наш уровень
    значит, что уровень съеден целиком;
  * заявка живёт до 30 с (и не дольше, чем до 10 с до конца окна); время полного исполнения пишется в мс от постановки.
Результат: maker_<день>.csv.gz. Ничего не торгует.
"""
from __future__ import annotations

import argparse
import gc
import os

import numpy as np
import pandas as pd

from edge_source import collect, winners_ptb
from lead_lag import PM, read
from replay import load_source

WINDOW = 300
DS = (0, 1000, 3000)
LIFE_MS = 30000
PLACE_MS = 25.0
SIZE = 5.0
CTRL_OFFSETS = (40, 100, 160, 220)


class Depth:
    """Снимки топ-5 уровней книги каждой стороны (время - наше, локальное)."""

    def __init__(self, root: str):
        d = read(root, "pm_depth")
        self.by = {}
        if d.empty:
            return
        for (w, o), g in d.groupby(["w", "o"]):
            g = g.sort_values("ts_ms")
            self.by[(int(w), str(o))] = (g.ts_ms.values.astype(float),
                                          g[[f"b{i}" for i in range(1, 6)]].values.astype(float),
                                          g[[f"bs{i}" for i in range(1, 6)]].values.astype(float))

    def bid_size_at(self, w: int, o: str, t_local: float, q: float) -> float:
        x = self.by.get((w, o))
        if x is None:
            return np.nan
        i = np.searchsorted(x[0], t_local, side="right") - 1
        if i < 0:
            return np.nan
        px, sz = x[1][i], x[2][i]
        if not np.isfinite(px[0]) or q > px[0] + 1e-9:
            return 0.0                       # наша цена лучше лучшего bid - впереди никого
        hit = np.flatnonzero(np.abs(px - q) < 1e-9)
        if len(hit):
            return float(sz[hit[0]])
        return 1e9                           # уровень глубже пяти известных или пуст - считаем недостижимым


class Trades:
    def __init__(self, root: str):
        tr = read(root, "pm_trades", ["server_ts", "w", "o", "side", "price", "size", "tx"])
        self.by = {}
        self.diag = ""
        if tr.empty:
            return
        tr = tr.dropna(subset=["server_ts", "price", "size"])
        tr["side"] = tr.side.astype(str).str.upper().str[0]
        tr["o"] = tr.o.astype(str).str[0]
        both = tr.groupby("tx").o.nunique() if "tx" in tr else pd.Series(dtype=float)
        self.diag = f"сделок {len(tr)}, хэшей с обеими сторонами {(both > 1).mean():.1%}" if len(both) else f"сделок {len(tr)}"
        for w, g in tr.groupby("w"):
            g = g.sort_values("server_ts", kind="stable")
            self.by[int(w)] = (g.server_ts.values.astype(float), g.o.values, g.side.values,
                               g.price.values.astype(float), g["size"].values.astype(float))


def simulate(tr: Trades, w: int, tok: str, q: float, t_act: float, t_end: float, ahead: float, conv: str):
    """Время полного исполнения (мс от t_act) или nan."""
    x = tr.by.get(w)
    if x is None or not np.isfinite(ahead):
        return np.nan
    ts, o, side, px, sz = x
    i0, i1 = np.searchsorted(ts, t_act, side="left"), np.searchsorted(ts, t_end, side="left")
    mirror = round(1 - q, 2)
    filled = 0.0
    for i in range(i0, i1):
        at = through = False
        if o[i] == tok and side[i] == "S":
            at, through = abs(px[i] - q) < 1e-9, px[i] < q - 1e-9
        elif o[i] != tok and side[i] == "B":
            through = px[i] > mirror + 1e-9
            at = conv == "all" and abs(px[i] - mirror) < 1e-9
        if through:
            return ts[i] - t_act
        if not at:
            continue
        ahead -= sz[i]
        if ahead < 0:
            filled += -ahead
            ahead = 0.0
            if filled >= SIZE - 1e-9:
                return ts[i] - t_act
    return np.nan


def side_book(state, sgn):
    if state is None:
        return np.nan, np.nan
    bid, ask = float(state[0]), float(state[1])
    return (bid, ask) if sgn > 0 else (1 - ask, 1 - bid)


def side_mid(pm: PM, w: int, t: float, sgn: int) -> float:
    b, a = side_book(pm.state(w, t, "srv"), sgn)
    return (a + b) / 2 if np.isfinite(a) and np.isfinite(b) else np.nan


def orders_for(kind, w, t0, sgn, pm, dep, tr, win, Ds):
    rows = []
    tok = "U" if sgn > 0 else "D"
    won = (1.0 if (win[w] == "Up") == (sgn > 0) else 0.0)
    for D in Ds:
        t_dec = t0 + D
        bid, ask = side_book(pm.state(w, t_dec, "rcv"), sgn)
        if not (np.isfinite(bid) and np.isfinite(ask)):
            continue
        t_end = min(t_dec + PLACE_MS + LIFE_MS, (w + WINDOW - 10) * 1000.0)
        t_act = t_dec + PLACE_MS
        if t_end <= t_act:
            continue
        for mode in ("join", "improve"):
            q = round(bid + (0.01 if mode == "improve" and ask - bid >= 0.02 - 1e-9 else 0.0), 2)
            if not (0.01 <= q <= 0.98):
                continue
            sb, sa = side_book(pm.state(w, t_act, "srv"), sgn)
            r = dict(kind=kind, w=w, t=t0, sgn=sgn, D=D, mode=mode, T=round(w + WINDOW - t_act / 1000, 1), q=q,
                     spread=round(ask - bid, 2), life=round(t_end - t_act), won=won)
            if np.isfinite(sa) and sa <= q + 1e-9:
                r["placed"] = 0              # заявка пересекла бы спред: post-only отклонит
                rows.append(r)
                continue
            r["placed"] = 1
            ah = dep.bid_size_at(w, tok, t_act + 43.0, q)
            r["ahead"] = ah
            for conv in ("all", "same"):
                for qm, a0 in (("cons", ah), ("front", 0.0)):
                    r[f"f_{conv}_{qm}"] = simulate(tr, w, tok, q, t_act, t_end, a0, conv)
            f = r["f_all_cons"]
            if np.isfinite(f):
                r["mf0"] = round(side_mid(pm, w, t_act + f, sgn), 4)
                r["mf10"] = round(side_mid(pm, w, t_act + f + 10000, sgn), 4)
            r["m_dec"] = round(side_mid(pm, w, t_dec, sgn), 4)
            rows.append(r)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for root in a.roots:
        day = os.path.basename(os.path.normpath(root))
        try:
            pm_top = read(root, "pm_top")
            if pm_top.empty:
                print(f"{day}: нет pm_top")
                continue
            win, _ = winners_ptb(root)
            pm = PM(pm_top)
            t_src, px = load_source(root, a.source)
            if len(t_src) < 1000:
                print(f"{day}: мало тиков")
                continue
            sigs = [s for s in collect(pm_top, t_src, px, delays=(0,)) if s["w"] in win]
            dep, tr = Depth(root), Trades(root)
            rows = []
            for s in sigs:
                rows += orders_for("sig", s["w"], s["t"], s["sgn"], pm, dep, tr, win, DS)
            for w in sorted(win):
                if w not in pm.by_w:
                    continue
                for off in CTRL_OFFSETS:
                    for sgn in (1, -1):
                        rows += orders_for("ctl", w, (w + off) * 1000.0, sgn, pm, dep, tr, win, (0,))
            d = pd.DataFrame(rows)
            if len(d):
                d.to_csv(os.path.join(a.out, f"maker_{day}.csv.gz"), index=False, compression="gzip")
            print(f"{day}: сигналов {len(sigs)}, заявок {len(d)}; {tr.diag}", flush=True)
            del pm_top, pm, t_src, px, sigs, dep, tr, rows, d
            gc.collect()
        except Exception as ex:
            print(f"{day}: ошибка {ex!r}", flush=True)


if __name__ == "__main__":
    main()
