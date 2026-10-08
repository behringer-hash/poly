"""Сверка: настоящий движок paper.py (виртуальное время) против упрощённого реплея на одних и тех же данных.

    python fidelity_check.py data/2026-10-08 --sources bybit,coinbase --primary bybit --thr 0.03

Печатает: совпадение сигналов (по миллисекундам) и доли исполнений для трёх способов проверки -
движок paper.py, реплей с view="rcv" (должен совпасть с движком) и реплей с view="srv" (реальное состояние
книги на сервере Polymarket в момент матча; ближе к живым ордерам).
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

import paper_replay as pr
import replay as rp
from lead_lag import PM, read


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--sources", default="bybit,coinbase")
    ap.add_argument("--primary", default="bybit")
    ap.add_argument("--thr", type=float, default=0.03)
    ap.add_argument("--latencies", default="150,300,450,600")
    a = ap.parse_args()
    lat = [int(x) for x in a.latencies.split(",")]
    srcs = {n: rp.load_source(a.root, n) for n in a.sources.split(",")}
    wn = read(a.root, "windows").drop_duplicates("slug", keep="last")
    winners = dict(zip(wn.start.astype(int), wn.official_winner))
    pt = read(a.root, "pm_top")
    res = pr.run(a.root, srcs, a.primary, pr.parse_variants(f"v:{a.thr}:{a.primary}"), lat, winners, pm_top=pt)
    sg, fl = res["paper_signals"], res["paper_fills"]
    eng = set(zip((sg.recv * 1000).round(), np.where(sg.outcome == "Up", 1, -1)))
    t, px = srcs[a.primary]
    sigs = rp.collect_signals(pt, t, px, [rp.Params(a.thr)])
    mine = set(zip([round(s["t"]) for s in sigs], [s["sgn"] for s in sigs]))
    print(f"сигналы: движок {len(eng)}, реплей {len(mine)}, общих {len(eng & mine)}, "
          f"только движок {len(eng - mine)}, только реплей {len(mine - eng)}")
    pm = PM(pt)
    rows = {"движок paper.py": fl.groupby("latency_ms").status.apply(lambda s: (s == "fill").mean())}
    for v in ("rcv", "srv"):
        rows[f"реплей view={v}"] = rp.execute(sigs, pm, winners, lat, view=v).groupby("L").fill.mean()
    print("\nдоля исполнений по задержке, мс:")
    print(pd.DataFrame(rows).round(3).to_string())


if __name__ == "__main__":
    main()
