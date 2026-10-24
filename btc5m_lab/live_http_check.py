"""Проверка замера http_ms: не завышает ли ожидание хэша транзакции (py_clob_client_v2.post_order) время ответа у исполненных ордеров.

    python live_http_check.py bot_data_c1_w [bot_data_c2 ...]

Для каждой папки: квантили http_ms по статусам (matched / no_match), доля исполненных без хэша транзакции и их http_ms,
задержка от сигнала до отправки (очередь потоков) и число ордеров, отправленных одновременно с другими.
"""
from __future__ import annotations

import sys

import numpy as np
import pandas as pd

from live_vs_replay import orders_table


def q(x):
    x = pd.Series(x).dropna().astype(float)
    return " ".join(f"{np.percentile(x, p):7.0f}" for p in (10, 50, 90, 99)) + f" {x.max():8.0f}" if len(x) else "нет"


def main():
    pd.set_option("display.width", 200)
    for root in sys.argv[1:]:
        d = orders_table([root])
        if d.empty:
            print(root, ": нет ордеров")
            continue
        d["h"] = d.http_ms.astype(float)
        d["lag"] = (d.t_sent.astype(float) - d.t_signal.astype(float)) * 1000
        d["tx"] = d.tx_hashes.fillna("").astype(str).str.len() > 0
        print(f"\n=== {root}: ордеров {len(d)} ===")
        print("http_ms  p10      p50      p90      p99      max")
        for st, g in d.groupby("status"):
            print(f"{st:10s} n={len(g):5d}  {q(g.h)}")
        m = d[d.status == "matched"]
        print(f"\nисполненных {len(m)}, из них без хэша транзакции в ответе: {(~m.tx).sum()} ({(~m.tx).mean():.1%})")
        if (~m.tx).any():
            print("  http_ms исполненных БЕЗ хэша:", q(m[~m.tx].h))
            print("  http_ms исполненных С хэшем: ", q(m[m.tx].h))
        print("доля ответов дольше 1 с: исполненные %.1f%%, неисполненные %.1f%%" % (100 * (m.h > 1000).mean(), 100 * (d[d.status == 'no_match'].h > 1000).mean()))
        print("задержка сигнал→отправка, мс (p10/p50/p90/p99/max):", q(d.lag))
        d = d.sort_values("t_sent")
        gap = d.t_sent.astype(float).diff() * 1000
        print(f"ордеров, отправленных менее чем через 300 мс после предыдущего: {(gap < 300).sum()} ({(gap < 300).mean():.1%}); задержка сигнал→отправка у них p50 {d.lag[gap < 300].median():.1f} мс, p99 {np.percentile(d.lag[gap < 300].dropna(), 99):.1f} мс" if (gap < 300).any() else "нет близких ордеров")


if __name__ == "__main__":
    main()
