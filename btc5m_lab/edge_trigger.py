"""Слабее порог сигнала и цена заявки «по ask»: выгрузка для анализа. Ничего не торгует.

    python edge_trigger.py data/2026-10-12 ... --out OUT

Сигналы C1 (модель anchor, Bybit, sigma x1, якорь в момент изменения книги, пауза 1 с на сторону) при порогах
edge = справедливая - ask - комиссия тейкера от -1 до 3,5 ц - у каждого порога свой поток сигналов (своя пауза).
По каждому сигналу три заявки на покупку стороны сигнала, решение в момент сигнала по книге, дошедшей до нас:
  join    - лучший bid; заявка действует на сервере через 25 мс;
  improve - bid + 1 ц, если спред не меньше 2 ц, иначе лучший bid;
  ask     - цена = ask, увиденный в момент сигнала. Если к приходу на сервер (25 мс) ask стороны всё ещё не выше этой
            цены, заявка исполнима сразу: биржа держит её 150 мс, исполнение тейкером по ask сервера в момент матча
            (через 210 мс - минимум по замерам, и 335 мс - медиана живых ордеров) с комиссией, если объёма на ask хватает.
            Если не исполнилась или к приходу цена уже ушла - заявка остаётся в книге bid'ом по этой цене (мейкер).
Мейкерское исполнение - только по сделкам рынка с очередью (как M2): all - продажи нашего токена и покупки другого
по зеркальной цене, same - только продажи нашего токена. Заявка живёт до 5 с; время исполнения - мс от постановки.
Результат: trig_<день>_<порог>.csv.gz.
"""
from __future__ import annotations

import argparse
import gc
import os

import numpy as np
import pandas as pd

from edge_maker import Depth, Trades, side_book, simulate
from edge_source import winners_ptb
from lead_lag import FEE, PM, read
from replay import Params, collect_signals, load_source

WINDOW = 300
THRS = (-0.010, -0.005, 0.0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035)
PLACE_MS = 25.0
LIFE_MS = 5000.0
SIZE = 5.0
TK = (210.0, 335.0)


def side_ask_size(state, sgn):
    if state is None:
        return np.nan, np.nan
    return (float(state[1]), float(state[3])) if sgn > 0 else (1 - float(state[0]), float(state[2]))


def maker_leg(r, pm, dep, tr, w, tok, sgn, q, t_act, t_end, prefix):
    ah = dep.bid_size_at(w, tok, t_act + 43.0, q)
    r[f"{prefix}ahead"] = ah
    r[f"{prefix}t_act"] = t_act
    for conv in ("all", "same"):
        r[f"{prefix}f_{conv}"] = simulate(tr, w, tok, q, t_act, t_end, ah, conv)


def orders(s, pm, dep, tr, win):
    w, sgn, t = s["w"], s["sgn"], s["t"]
    tok = "U" if sgn > 0 else "D"
    bid, ask = side_book(pm.state(w, t, "rcv"), sgn)
    if not (np.isfinite(bid) and np.isfinite(ask)):
        return []
    t_end = min(t + PLACE_MS + LIFE_MS, (w + WINDOW - 10) * 1000.0)
    won = 1.0 if (win[w] == "Up") == (sgn > 0) else 0.0
    base = dict(thr=s["p"].thr, w=w, t=t, sgn=sgn, T=round(w + WINDOW - t / 1000, 1), edge=round(s["edge"], 4),
                bid=bid, ask=ask, won=won)
    rows = []
    for mode in ("join", "improve", "ask"):
        if mode == "ask":
            q = round(ask, 2)
        else:
            q = round(bid + (0.01 if mode == "improve" and ask - bid >= 0.02 - 1e-9 else 0.0), 2)
        if not (0.01 <= q <= 0.99):
            continue
        r = dict(base, mode=mode, q=q)
        t_arr = t + PLACE_MS
        sb, sa = side_book(pm.state(w, t_arr, "srv"), sgn)
        marketable = np.isfinite(sa) and sa <= q + 1e-9
        r["mkt"] = int(marketable)
        if mode != "ask":
            if marketable:              # post-only отклонит: цена ушла вниз раньше, чем заявка дошла
                r["placed"] = 0
                rows.append(r)
                continue
            r["placed"] = 1
            maker_leg(r, pm, dep, tr, w, tok, sgn, q, t_arr, t_end, "")
            rows.append(r)
            continue
        r["placed"] = 1
        if not marketable:
            maker_leg(r, pm, dep, tr, w, tok, sgn, q, t_arr, t_end, "")
            rows.append(r)
            continue
        for L in TK:                     # исполнима при приходе: удержание биржей, затем матч по ask сервера
            px, sz = side_ask_size(pm.state(w, t + L, "srv"), sgn)
            ok = np.isfinite(px) and px <= q + 1e-9 and np.isfinite(sz) and sz >= SIZE - 1e-9
            r[f"tk{int(L)}"] = round(px, 4) if ok else np.nan
        # не исполнилась тейкером (по медиане 335 мс) - остаётся bid'ом по q с момента матча
        if not np.isfinite(r.get("tk335", np.nan)):
            maker_leg(r, pm, dep, tr, w, tok, sgn, q, t + TK[1], t_end, "")
        rows.append(r)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    params = [Params(thr) for thr in THRS]
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
            sigs = [s for s in collect_signals(pm_top, t_src, px, params) if s["w"] in win and s["w"] in pm.by_w]
            dep, tr = Depth(root), Trades(root)
            counts = {}
            by_thr: dict[float, list] = {}
            for s in sigs:
                by_thr.setdefault(s["p"].thr, []).extend(orders(s, pm, dep, tr, win))
                counts[s["p"].thr] = counts.get(s["p"].thr, 0) + 1
            for thr, rows in by_thr.items():
                d = pd.DataFrame(rows)
                for c in d.columns:
                    if d[c].dtype == float:
                        d[c] = d[c].round(4)
                d.to_csv(os.path.join(a.out, f"trig_{day}_{int(round(thr * 1000)):+d}.csv.gz"), index=False, compression="gzip")
            print(f"{day}: сигналов по порогам (ц): " + ", ".join(f"{100 * k:g}: {v}" for k, v in sorted(counts.items())), flush=True)
            del pm_top, pm, t_src, px, sigs, dep, tr, by_thr
            gc.collect()
        except Exception as ex:
            print(f"{day}: ошибка {ex!r}", flush=True)


if __name__ == "__main__":
    main()
