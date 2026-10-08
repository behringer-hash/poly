"""Бумажные варианты `anc_*` по задержкам: доля исполнений, ц/шейр и ц/сигнал, ИИ bootstrap'ом по окнам.

    python trigger_vs_latency.py bot_data_3c bot_data_3c_v2

ц/сигнал = PnL всех сигналов варианта (неисполненные = 0) / число сигналов: показывает, что даёт сам триггер
с учётом того, что часть ордеров не исполняется. Исход берётся по official_winner.
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from analyze import FEE_RATE, load


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--prefix", default="anc")
    a = ap.parse_args()
    pd.set_option("display.width", 200)
    off = load(a.roots, "windows").drop_duplicates("slug", keep="last").set_index("slug").official_winner
    f = load(a.roots, "paper_fills")
    f = f[f.variant.str.startswith(a.prefix) & f.slug.map(off).notna()].copy()
    f["win"] = (f.slug.map(off) == f.outcome).astype(float)
    f["fill"] = f.status == "fill"
    px = f.avg_px.fillna(0.0)
    f["pnl"] = np.where(f.fill, f.qty * (f.win - px - FEE_RATE * px * (1 - px)), 0.0)
    f["sh"] = np.where(f.fill, f.qty, 0.0)
    rng = np.random.default_rng(0)
    rows = []
    for (v, L), d in f.groupby(["variant", "latency_ms"]):
        w = d.groupby("slug").agg(p=("pnl", "sum"), n=("pnl", "size"))
        idx = rng.integers(0, len(w), (1500, len(w)))
        bs = 100 * w.p.values[idx].sum(1) / w.n.values[idx].sum(1)
        rows.append((v, int(L), len(d), d.fill.mean(), 100 * d.pnl.sum() / max(d.sh.sum(), 1e-9),
                     100 * d.pnl.sum() / len(d), *np.percentile(bs, [2.5, 97.5]), len(w)))
    print(pd.DataFrame(rows, columns=["variant", "L", "сигн", "исполн", "ц/шейр", "ц/сигнал", "ИИ-", "ИИ+",
                                      "окон"]).round(2).to_string(index=False))


if __name__ == "__main__":
    main()
