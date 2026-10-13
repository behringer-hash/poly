"""Стратегия «скачок цены BTC на N долларов по сырым сделкам -> покупка Up/Down» без модели справедливой цены и якоря.

    python trade_jump.py data/2026-10-10 data/2026-10-11 --sources bybit_trade,binance_fut,binance --N 8,15,25 --W 250,500,1000 \
        --latencies 250,300,400 --slips 0,3,5

Сигнал: цена источника (последняя сделка) сейчас минус цена W мс назад >= N долларов (вверх: покупаем Up, вниз: Down).
Никакой проверки «устарела ли цена на Polymarket» нет - только скорость; из фильтров только цена стороны 0.05-0.95,
не меньше 10 с до конца окна и пауза между сигналами одной стороны окна (--cooldown, с).
Исполнение - по состоянию книги сервера Polymarket через L мс (как в replay.py), удержание до конца окна.
Обозначения в колонке вариант: thr{N}_s{W в секундах}_slip{переплата ц}. Базой для сравнения служит C1 из replay.py.
"""
from __future__ import annotations

import argparse
import itertools

import numpy as np
import pandas as pd

from lead_lag import PM, read
from replay import Params, collect_signals, execute, load_source, parse_slips, summarize
from speed_compare import fires


def jump_signals(pm: PM, t: np.ndarray, px: np.ndarray, N: float, W_ms: float, cooldown_s: float, *,
                 lo: float = 0.05, hi: float = 0.95, min_T: float = 10.0, min_elapsed: float = 3.0) -> list[dict]:
    p = Params(N, W_ms / 1000.0, 0.0, cooldown_s)
    last: dict[tuple, float] = {}
    out = []
    for tt, d in fires(t, px, N, W_ms, refractory=0.0):
        w = int(tt // 1000 // 300 * 300)
        T = w + 300 - tt / 1000
        if T < min_T or tt / 1000 - w < min_elapsed:
            continue
        st = pm.state(w, tt, "rcv")
        if st is None or not (np.isfinite(st[0]) and np.isfinite(st[1])):
            continue
        a = st[1] if d > 0 else 1 - st[0]
        if not (lo <= a <= hi):
            continue
        if tt - last.get((w, d), -1e18) < cooldown_s * 1000:
            continue
        last[(w, d)] = tt
        out.append(dict(p=p, w=w, sgn=d, t=tt, view=a, edge=0.0))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--sources", default="bybit_trade,binance_fut,binance")
    ap.add_argument("--N", default="8,15,25")
    ap.add_argument("--W", default="250,500,1000")
    ap.add_argument("--latencies", default="250,300,400")
    ap.add_argument("--slips", default="0,3,5")
    ap.add_argument("--cooldown", type=float, default=2.0)
    ap.add_argument("--since", type=float, default=0)
    ap.add_argument("--baseline", action="store_true", help="добавить C1 (порог 0.03, sigma 1, Bybit, переплата 3 ц) для сравнения")
    a = ap.parse_args()
    pd.set_option("display.width", 250)
    srcs = [s.strip() for s in a.sources.split(",")]
    lat = [int(x) for x in a.latencies.split(",")]
    slips = parse_slips(a.slips)
    frames = []
    for root in a.roots:
        pt = read(root, "pm_top")
        wn = read(root, "windows").drop_duplicates("slug", keep="last")
        winners = dict(zip(wn.start.astype(int), wn.official_winner))
        pm = PM(pt)
        for s in srcs:
            t, px = load_source(root, s)
            if len(t) < 100:
                continue
            sigs = []
            for N, W in itertools.product([float(x) for x in a.N.split(",")], [float(x) for x in a.W.split(",")]):
                sigs += jump_signals(pm, t, px, N, W, a.cooldown)
            df = execute(sigs, pm, winners, lat, slips=slips)
            df["variant"] = s + ":" + df["variant"]
            frames.append(df)
            print(f"{root} {s}: тиков {len(t)}, сигналов {len(sigs)}")
        if a.baseline:
            t, px = load_source(root, "bybit")
            sg = collect_signals(pt, t, px, [Params(0.03, 1.0)])
            df = execute(sg, pm, winners, lat, slips=parse_slips("3"))
            df["variant"] = "C1(bybit,thr0.03)"
            frames.append(df)
    if not frames:
        print("нет данных")
        return
    allr = pd.concat(frames, ignore_index=True)
    if a.since:
        allr = allr[allr.w >= a.since]
    days = max((allr.t.max() - allr.t.min()) / 86_400_000.0, 1e-9)
    sm = summarize(allr, n_boot=800)
    sm["сигн_в_сутки"] = (sm["сигн"] / days).round(0)
    print(f"\nпериод {days:.2f} сут, окон {allr.w.nunique()}. цсигнал - центов на сигнал (неисполненный = 0), ИИ - 95% по окнам")
    for L in lat:
        x = sm[sm.L == L].sort_values("цсигнал", ascending=False)
        print(f"\n=== задержка {L} мс: 25 лучших по цсигнал и 5 худших ===")
        print(pd.concat([x.head(25), x.tail(5)]).drop(columns=["дни"]).to_string(index=False))
    # проверка на отложенной выборке: топ-10 по первой половине окон, результат на второй
    ws = sorted(allr.w.unique())
    if len(ws) >= 40:
        cut = ws[len(ws) // 2]
        L = lat[len(lat) // 2]
        tr = summarize(allr[(allr.w < cut) & (allr.L == L)], n_boot=300).set_index("вариант")
        te = summarize(allr[(allr.w >= cut) & (allr.L == L)], n_boot=300).set_index("вариант")
        j = tr[["сигн", "исполн", "цсигнал"]].join(te[["сигн", "исполн", "цсигнал", "ИИ_низ", "ИИ_верх"]], lsuffix="_обуч", rsuffix="_тест")
        top = j.sort_values("цсигнал_обуч", ascending=False).head(10)
        print(f"\n=== отложенная выборка (L={L} мс): топ-10 по первой половине окон, результат на второй ===")
        print(top.round(2).to_string())
        print(f"все {len(j)} вариантов: средний цсигнал обуч {j.цсигнал_обуч.mean():.2f}, тест {j.цсигнал_тест.mean():.2f}; "
              f"у топ-10: тест {top.цсигнал_тест.mean():.2f}")


if __name__ == "__main__":
    main()
