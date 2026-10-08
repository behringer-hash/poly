"""Офлайн-анализ записанных данных бота (bot_data*/): честная оценка вариантов.

    python analyze.py bot_data_mom bot_data_mom2

Что делает:
  * пересчитывает исход по official_winner из windows (а не по provisional);
  * считает EV на шейр в момент сигнала (win - ask - fee), без допущений об исполнении;
  * доверительный интервал bootstrap'ом по ОКНАМ (сигналы внутри окна сильно коррелированы);
  * устойчивость по дням и разрезы по T, цене, edge для выбранного варианта.
"""
from __future__ import annotations

import argparse
import glob
import os

import numpy as np
import pandas as pd

FEE_RATE = 0.07


def load(roots: list[str], stream: str) -> pd.DataFrame:
    files = []
    for r in roots:
        files += glob.glob(os.path.join(r, "**", f"{stream}_*.csv*"), recursive=True)
    dfs = []
    for f in sorted(files):
        try:
            d = pd.read_csv(f, dtype=str)
        except Exception:
            continue
        if len(d):
            dfs.append(d)
    if not dfs:
        return pd.DataFrame()
    d = pd.concat(dfs, ignore_index=True)
    first = d.columns[0]
    d = d[d[first] != first].copy()  # повторные заголовки после перезапусков процесса
    for c in d.columns:
        x = pd.to_numeric(d[c], errors="coerce")
        if d[c].notna().sum() and x.notna().sum() >= 0.9 * d[c].notna().sum():
            d[c] = x
    return d.reset_index(drop=True)


def signals_with_outcome(roots: list[str]) -> pd.DataFrame:
    ws = load(roots, "windows").drop_duplicates("slug", keep="last")
    off = ws.set_index("slug").official_winner
    sg = load(roots, "paper_signals")
    sg = sg[sg.slug.map(off).notna()].copy()
    sg["win"] = (sg.slug.map(off) == sg.outcome).astype(float)
    sg["fee"] = FEE_RATE * sg.ask * (1 - sg.ask)
    sg["ev"] = sg.win - sg.ask - sg.fee
    sg["day"] = pd.to_datetime(sg.recv, unit="s").dt.strftime("%m-%d")
    return sg


def boot_ci(d: pd.DataFrame, n: int = 2000, seed: int = 0) -> tuple[float, float]:
    """95% ИИ среднего EV на шейр, ресэмплинг целых окон."""
    w = d.groupby("slug").ev.agg(["sum", "size"])
    idx = np.random.default_rng(seed).integers(0, len(w), (n, len(w)))
    s = w["sum"].values[idx].sum(1) / w["size"].values[idx].sum(1)
    return tuple(np.percentile(s, [2.5, 97.5]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--variant", default="anc_3c_by")
    a = ap.parse_args()
    pd.set_option("display.width", 200)
    sg = signals_with_outcome(a.roots)
    print(f"сигналов {len(sg)}, окон {sg.slug.nunique()}\n")
    rows = []
    for v, d in sg.groupby("variant"):
        lo, hi = boot_ci(d)
        rows.append((v, len(d), d.slug.nunique(), 100 * d.ev.mean(), 100 * lo, 100 * hi))
    print(pd.DataFrame(rows, columns=["variant", "сигн", "окон", "EV ц/шейр", "ИИ-", "ИИ+"]).round(2).to_string(index=False))
    print("\nEV ц/шейр по дням:")
    print((100 * sg.pivot_table(index="variant", columns="day", values="ev", aggfunc="mean")).round(2).to_string())
    d = sg[sg.variant == a.variant]
    if len(d):
        print(f"\nРазрезы для {a.variant}:")
        for col, bins in (("T", [0, 30, 60, 120, 180, 240, 300]), ("ask", [0, .2, .35, .5, .65, .8, .95]),
                          ("edge", [0, .03, .04, .06, .1, 1])):
            print(d.groupby(pd.cut(d[col], bins), observed=True).agg(n=("ev", "size"), ev=("ev", "mean"),
                                                                    win=("win", "mean")).round(3).to_string())


if __name__ == "__main__":
    main()
