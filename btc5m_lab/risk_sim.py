"""Кластеры сигналов, пауза после первого сигнала и симуляция реальных лимитов бота (окно, сутки, стоп по убытку).

    python risk_sim.py data/2026-10-10 data/2026-10-11 --source bybit --thr 0.03 --sigma-mult 1 --slip 3 \
        --cooldowns 1,3,5,10,30,300 --latencies 200,300

Что считается:
  1. кластеры: сколько сигналов подряд бывает в одном окне в одну сторону и чем кончаются покупки по порядку
     (1-й, 2-й, 3-й ... сигнал кластера): прибыль на сигнал, доля выигравших;
  2. пауза: cooldown после сигнала для (окно, сторона): 1 с, 3 с ... 300 с (= один сигнал на окно и сторону);
  3. портфель с лимитами бота (как live.py): ордеров и $ на окно, $ на сутки, остановка при дневном убытке,
     минимальный интервал между ордерами; итог - $ в сутки, худший день, максимальная просадка.
Всё считается по состоянию книги Polymarket на сервере в момент матча, покупка и удержание до конца окна.
"""
from __future__ import annotations

import argparse
import heapq

import numpy as np
import pandas as pd

from lead_lag import FEE, PM, read
from replay import Params, collect_signals, execute, load_source, parse_slips


def cluster_stats(df: pd.DataFrame) -> pd.DataFrame:
    """По исполненным и неисполненным сигналам: размер кластера (окно, сторона) и результат по номеру сигнала."""
    d = df.sort_values("t").copy()
    d["k"] = d.groupby(["w", "sgn"]).cumcount() + 1
    d["n"] = d.groupby(["w", "sgn"]).k.transform("max")
    d["pnl_sh"] = np.where(d.fill & d.settle.notna(), d.settle * d.qty / 5.0, 0.0)       # ц на «шейр попытки»
    return d


def portfolio(df: pd.DataFrame, *, max_orders_window=10, max_spend_window=30.0, max_spend_day=100.0, max_loss_day=20.0,
              min_interval=1.0, min_seconds_left=10.0, max_shares_window=200.0) -> dict:
    """Прогон сигналов по времени через лимиты бота. df - строки одного варианта и одной задержки."""
    d = df.sort_values("t").reset_index(drop=True)
    day_of = lambda ts: int(ts // 86400)
    win_orders, win_spend, win_sh, win_pnl = {}, {}, {}, {}
    day_spend, day_pnl, stopped = {}, {}, set()
    pending: list[tuple[float, int]] = []            # (время расчёта окна, w)
    last_t = -1e18
    skipped = dict(стоп_убыток=0, лимит_суток=0, ордеров_окно=0, трат_окно=0, шейров_окно=0, интервал=0, мало_времени=0)
    sent = fills = 0
    cum, peak, dd = 0.0, 0.0, 0.0
    daily: dict[int, float] = {}
    for r in d.itertuples():
        t = r.t / 1000.0
        # рассчитываем окна, закончившиеся к этому моменту
        while pending and pending[0][0] <= t:
            _, w0 = heapq.heappop(pending)
            p = win_pnl.pop(w0, 0.0)
            dk = day_of(w0)
            day_pnl[dk] = day_pnl.get(dk, 0.0) + p
            daily[dk] = daily.get(dk, 0.0) + p
            cum += p
            peak = max(peak, cum)
            dd = max(dd, peak - cum)
            if -day_pnl[dk] >= max_loss_day:
                stopped.add(dk)
        dk = day_of(t)
        w = r.w
        T = w + 300 - t
        size = r.tgt
        est = r.limit * size + FEE * r.limit * (1 - r.limit) * size
        if dk in stopped:
            skipped["стоп_убыток"] += 1
        elif day_spend.get(dk, 0.0) + est > max_spend_day:
            skipped["лимит_суток"] += 1
        elif win_orders.get(w, 0) >= max_orders_window:
            skipped["ордеров_окно"] += 1
        elif win_spend.get(w, 0.0) + est > max_spend_window:
            skipped["трат_окно"] += 1
        elif win_sh.get((w, r.sgn), 0.0) + size > max_shares_window:
            skipped["шейров_окно"] += 1
        elif t - last_t < min_interval:
            skipped["интервал"] += 1
        elif T < min_seconds_left:
            skipped["мало_времени"] += 1
        else:
            sent += 1
            last_t = t
            if w not in win_orders:
                heapq.heappush(pending, (w + 300 + 5.0, w))
            win_orders[w] = win_orders.get(w, 0) + 1
            if r.fill:
                fills += 1
                cost = r.qty * r.px + FEE * r.px * (1 - r.px) * r.qty
                win_spend[w] = win_spend.get(w, 0.0) + cost
                day_spend[dk] = day_spend.get(dk, 0.0) + cost
                win_sh[(w, r.sgn)] = win_sh.get((w, r.sgn), 0.0) + r.qty
                if np.isfinite(r.settle):
                    win_pnl[w] = win_pnl.get(w, 0.0) + r.qty * r.settle / 100.0
    for _, w0 in sorted(pending):                    # хвост: окна, не закрытые до конца данных
        p = win_pnl.pop(w0, 0.0)
        dk = day_of(w0)
        daily[dk] = daily.get(dk, 0.0) + p
        cum += p
        peak = max(peak, cum)
        dd = max(dd, peak - cum)
    days = len(daily) or 1
    vals = np.array(list(daily.values())) if daily else np.array([0.0])
    return dict(ордеров=sent, исполнений=fills, пропущено=sum(skipped.values()), pnl_всего=round(cum, 2),
                pnl_в_сутки=round(cum / days, 2), худший_день=round(float(vals.min()), 2),
                просадка=round(dd, 2), дней_со_стопом=len(stopped), **{f"пр_{k}": v for k, v in skipped.items() if v})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--thr", type=float, default=0.03)
    ap.add_argument("--sigma-mult", type=float, default=1.0)
    ap.add_argument("--slip", default="3", help="переплата в центах (число) или e:масштаб:запас:потолок")
    ap.add_argument("--latencies", default="200,300")
    ap.add_argument("--cooldowns", default="1,3,5,10,30,300")
    ap.add_argument("--since", type=float, default=0)
    ap.add_argument("--max-orders-window", type=int, default=10)
    ap.add_argument("--max-spend-window", type=float, default=30.0)
    ap.add_argument("--max-spend-day", type=float, default=100.0)
    ap.add_argument("--max-loss-day", type=float, default=20.0)
    ap.add_argument("--min-interval", type=float, default=1.0)
    a = ap.parse_args()
    pd.set_option("display.width", 250)
    lat = [int(x) for x in a.latencies.split(",")]
    cds = [float(x) for x in a.cooldowns.split(",")]
    slips = parse_slips(a.slip)
    frames = []
    for root in a.roots:
        pt = read(root, "pm_top")
        wn = read(root, "windows").drop_duplicates("slug", keep="last")
        winners = dict(zip(wn.start.astype(int), wn.official_winner))
        t, px = load_source(root, a.source)
        params = [Params(a.thr, a.sigma_mult, 0.0, cd) for cd in cds]
        sigs = collect_signals(pt, t, px, params)
        frames.append(execute(sigs, PM(pt), winners, lat, slips=slips))
        print(f"{root}: сигналов {len(sigs)}")
    df = pd.concat(frames, ignore_index=True)
    if a.since:
        df = df[df.w >= a.since]
    df = df[df.won.notna() | ~df.fill]                  # окна без известного исхода исключаем из исполненных
    caps = dict(max_orders_window=a.max_orders_window, max_spend_window=a.max_spend_window,
                max_spend_day=a.max_spend_day, max_loss_day=a.max_loss_day, min_interval=a.min_interval)

    # --- 1. кластеры при cooldown = 1 с
    base1 = df[(df.base == Params(a.thr, a.sigma_mult).base)]
    for L in lat:
        c = cluster_stats(base1[base1.L == L])
        grp = c.groupby(["w", "sgn"]).agg(n=("k", "max"), fills=("fill", "sum"),
                                          pnl=("pnl_sh", "sum")).reset_index()
        bins = pd.cut(grp.n, [0, 1, 3, 5, 10, 20, 1000], labels=["1", "2-3", "4-5", "6-10", "11-20", "21+"])
        g = grp.groupby(bins, observed=True).agg(групп=("n", "size"), сигналов=("n", "sum"), исполнений=("fills", "sum"),
                                                  цсигнал=("pnl", "sum"))
        g["цсигнал"] = (g["цсигнал"] / g["сигналов"]).round(2)
        g["доля_сигналов_%"] = (100 * g["сигналов"] / g["сигналов"].sum()).round(1)
        print(f"\n=== кластеры (окно × сторона), cooldown 1 с, L={L} мс ===")
        print(g.to_string())
        c["ordb"] = pd.cut(c.k, [0, 1, 2, 3, 5, 10, 1000], labels=["1-й", "2-й", "3-й", "4-5-й", "6-10-й", "11-й+"])
        o = c.groupby("ordb", observed=True).agg(сигналов=("k", "size"), исполн=("fill", "mean"),
                                                  цсигнал=("pnl_sh", "mean"), доля_побед=("won", "mean"))
        print(f"--- результат по порядковому номеру сигнала в кластере, L={L} мс ---")
        print(o.round(3).to_string())
        fl = grp[grp.fills > 0]
        if len(fl):
            print(f"групп с исполнениями: {len(fl)}; убыточных: {(fl.pnl < 0).mean():.0%}; "
                  f"макс. исполнений в группе: {int(fl.fills.max())}; худшая группа {fl.pnl.min() * 5 / 100:.2f}$, "
                  f"лучшая {fl.pnl.max() * 5 / 100:.2f}$")

    # --- 2/3. пауза и лимиты бота
    rows = []
    for L in lat:
        for cd in cds:
            b = Params(a.thr, a.sigma_mult, 0.0, cd).base
            sub = df[(df.base == b) & (df.L == L)]
            unc = sub[sub.fill & sub.settle.notna()]
            res = portfolio(sub, **caps)
            rows.append(dict(L=L, пауза_с=cd, сигналов=len(sub), исполн_без_лимитов=int(sub.fill.sum()),
                             цсигнал_без_лимитов=round((unc.settle * unc.qty / 5.0).sum() / max(len(sub), 1), 2), **res))
    print("\n=== пауза после сигнала и лимиты бота "
          f"({a.max_orders_window} ордеров и ${a.max_spend_window:g} на окно, ${a.max_spend_day:g} в сутки, стоп −${a.max_loss_day:g}) ===")
    print(pd.DataFrame(rows).fillna(0).to_string(index=False))


if __name__ == "__main__":
    main()
