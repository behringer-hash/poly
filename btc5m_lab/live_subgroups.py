"""Где в живых исполнениях прибыль и где убыток: подгруппы по силе сигнала, цене, времени до конца окна, стороне, часу, времени ответа.

    python live_subgroups.py bot_data_c1 bot_data_c1_s7

Каждая папка бота - отдельный запуск (run). Берём все живые ордера с известным победителем окна. Метрики по группе:
  исполнено (доля ордеров), ц/шейр на исполненных (цена исполнения, комиссия 0.07 p(1-p), выигрыш по победителю), $ всего, и $ на ордер (неисполненные = 0).
Дублируем для каждого запуска отдельно: группа интересна, только если знак один и тот же в обоих.
"""
from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from analyze import load
from live_vs_replay import orders_table

FEE = 0.07


def table(root: str, run: str) -> pd.DataFrame:
    d = orders_table([root])
    w = load([root], "live_windows").groupby("slug", as_index=False).last()
    d["win"] = d.slug.map(dict(zip(w.slug, w.winner.astype(str))))
    d = d[d.win.isin(["Up", "Down"])].copy()
    d["run"] = run
    d["won"] = ((d.win == "Up") == (d.sgn > 0)).astype(float)
    d["avg"] = d.avg_px.astype(float)
    d["fsh"] = d.filled.astype(float).where(d.filled_f, 0.0)
    fee = FEE * d.avg * (1 - d.avg)
    d["pnl"] = np.where(d.filled_f, (d.won - d.avg - fee) * d.fsh, 0.0)
    d["ask"] = d.ask_signal.astype(float)
    d["edge"] = d.edge_c.astype(float)
    d["Tl"] = d["T"].astype(float)
    d["hr"] = ((d.w % 86400) // 3600 // 6) * 6
    d["h"] = d.http_ms.astype(float)
    return d


def report(d: pd.DataFrame, col: str, bins, labels=None, title=""):
    g = pd.cut(d[col], bins, labels=labels) if bins is not None else d[col]
    rows = []
    for k, x in d.groupby(g, observed=True):
        f = x[x.filled_f]
        row = dict(группа=str(k), ордеров=len(x), исполнено=round(x.filled_f.mean(), 3), ц_шейр=round(f.pnl.sum() / max(f.fsh.sum(), 1) * 100, 2),
                   долл=round(x.pnl.sum(), 2), ц_на_ордер=round(x.pnl.sum() / x["size"].astype(float).sum() * 100, 2))
        for run, y in x.groupby("run"):
            ff = y[y.filled_f]
            row[f"{run}_ц_шейр"] = round(ff.pnl.sum() / max(ff.fsh.sum(), 1) * 100, 2) if len(ff) else np.nan
            row[f"{run}_долл"] = round(y.pnl.sum(), 2)
        rows.append(row)
    print(f"\n=== {title} ===")
    print(pd.DataFrame(rows).to_string(index=False))


def main():
    roots = sys.argv[1:]
    pd.set_option("display.width", 240)
    d = pd.concat([table(r, f"r{i + 1}") for i, r in enumerate(roots)], ignore_index=True)
    print(f"ордеров {len(d)}, исполнено {int(d.filled_f.sum())}; по запускам: " + ", ".join(f"{r}: {len(x)} ордеров, {x.pnl.sum():+.2f}$" for r, x in d.groupby("run")))
    report(d, "edge", [0, 3.5, 4.5, 6, 8, 12, 100], title="сила сигнала (edge, ц после комиссии)")
    report(d, "ask", [0, 0.15, 0.3, 0.45, 0.6, 0.75, 1], title="ask сигнала")
    report(d, "Tl", [0, 40, 80, 120, 180, 240, 300], title="осталось до конца окна, с")
    report(d, "sgn", None, title="сторона (+1 Up, -1 Down)")
    report(d, "hr", None, title="часы суток UTC (блоки по 6 ч)")
    report(d, "h", [0, 260, 300, 350, 450, 700, 1e6], title="время ответа биржи, мс (смотрим только как индикатор)")
    # самые «чистые» гипотезы: сочетание сильного сигнала и умеренной цены; для честности - разбиение по запускам
    s = d[(d.edge >= 6) & (d.ask.between(0.2, 0.8))]
    print(f"\nсильный сигнал (edge>=6 ц) и ask 0.2-0.8: ордеров {len(s)}, исполнено {s.filled_f.mean():.1%}, $ {s.pnl.sum():+.2f}; "
          + ", ".join(f"{r}: {x.pnl.sum():+.2f}$ на {len(x)}" for r, x in s.groupby("run")))
    rest = d.drop(s.index)
    print(f"остальные: ордеров {len(rest)}, $ {rest.pnl.sum():+.2f}; " + ", ".join(f"{r}: {x.pnl.sum():+.2f}$ на {len(x)}" for r, x in rest.groupby("run")))
    print("\nВНИМАНИЕ: групп много, часть различий случайна; смотрим только знаки, совпадающие в обоих запусках, и крупные группы.")


if __name__ == "__main__":
    main()
