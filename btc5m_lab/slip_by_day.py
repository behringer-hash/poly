"""Доходность C1 при разной переплате по дням, с задержкой, взятой из ЖИВЫХ ордеров (а не придуманной).

    python slip_by_day.py data/2026-10-1* --live-data bot_data_c1 --source bybit

Матчинг = сигнал + http_ms живого ордера (проверено: совпадение с фактом 98%). Распределение http_ms - 25 квантилей по всем живым ордерам, равные веса.
Выводим по дням: доля исполнений и центы на сигнал (до экспирации, неисполненные = 0) для переплат 0..10 ц. Дни 12-13 октября - период живого запуска (контроль).
"""
from __future__ import annotations

import argparse
import gc
import os

import numpy as np
import pandas as pd

from lead_lag import PM, read
from live_vs_replay import orders_table
from replay import Params, collect_signals, execute, load_source, parse_slips

SLIPS = "0,1,2,3,4,5,6,8,10"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--live-data", nargs="+", required=True)
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--thr", type=float, default=0.03)
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    h = orders_table(a.live_data).http_ms.astype(float).dropna().values
    lat = sorted({int(round(x)) for x in np.quantile(h, (np.arange(25) + 0.5) / 25)})
    print(f"живых ордеров {len(h)}, http_ms квантили: {lat}")
    slips = parse_slips(SLIPS)
    res = []
    for root in a.roots:
        pm_top = read(root, "pm_top")
        if pm_top.empty:
            continue
        wn = read(root, "windows").drop_duplicates("slug", keep="last")
        winners = dict(zip(wn.start.astype(int), wn.official_winner))
        t, px = load_source(root, a.source)
        sigs = collect_signals(pm_top, t, px, [Params(a.thr, 1.0)])
        r = execute(sigs, PM(pm_top), winners, lat, hold_s=5, view="srv", slips=slips)
        r["day"] = os.path.basename(os.path.normpath(root))
        r["nsig"] = len(sigs)
        res.append(r)
        print(f"{root}: сигналов {len(sigs)}")
        del pm_top, wn, t, px, sigs
        gc.collect()
    d = pd.concat(res, ignore_index=True)
    d["c"] = np.where(d.fill & d.settle.notna(), d.settle, 0.0)
    d["slip_c"] = d.slip.str.replace("slip", "").astype(float)
    sig_per_day = d.groupby("day").apply(lambda g: g[["w", "t", "sgn"]].drop_duplicates().shape[0])
    print("\n=== доля исполнений по дням и переплате (задержка из живых ордеров) ===")
    print(d.pivot_table(index="day", columns="slip_c", values="fill", aggfunc="mean").round(3).to_string())
    print("\n=== ц на сигнал (до экспирации, неисполненные = 0) ===")
    print(d.pivot_table(index="day", columns="slip_c", values="c", aggfunc="mean").round(2).to_string())
    print("\n=== ц на исполнение ===")
    f = d[d.fill & d.settle.notna()]
    print(f.pivot_table(index="day", columns="slip_c", values="settle", aggfunc="mean").round(2).to_string())
    print("\n=== все дни вместе: исполнений, ц на сигнал, ц на исполнение, $ на сигнал-день (5 шейров) ===")
    rows = []
    for s, g in d.groupby("slip_c"):
        ff = g[g.fill & g.settle.notna()]
        rows.append(dict(доплата_ц=s, исполнено=round(g.fill.mean(), 3), ц_на_сигнал=round(g.c.mean(), 2), ц_на_исполнение=round(ff.settle.mean(), 2),
                         сигналов_в_день=round(len(g.drop_duplicates(["w", "t", "sgn"])) / g.day.nunique())))
    print(pd.DataFrame(rows).to_string(index=False))
    # доверительный интервал по окнам для лучших и 3 ц
    rng = np.random.default_rng(0)
    print("\n=== 95% ИИ (бутстреп по окнам) ц на сигнал ===")
    for s in (0, 3, 5, 10):
        g = d[d.slip_c == s]
        per = g.groupby("w").c.agg(["sum", "size"])
        idx = np.arange(len(per))
        bs = [per["sum"].values[b].sum() / per["size"].values[b].sum() for b in (rng.choice(idx, len(idx)) for _ in range(500))]
        print(f"доплата {s:>2} ц: {g.c.mean():.2f} [{np.percentile(bs, 2.5):.2f}; {np.percentile(bs, 97.5):.2f}]")


if __name__ == "__main__":
    main()
