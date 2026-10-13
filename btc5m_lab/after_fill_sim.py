"""Пауза только после ИСПОЛНЕННОГО ордера против паузы после любого отправленного (реплей по состоянию книги сервера).

    python after_fill_sim.py data/2026-10-12 data/2026-10-13 --source bybit --thr 0.03 --sigma-mult 1 --slip 3 [--since T]

Реальные лимиты бота: 10 ордеров и $30 на окно, $100 в сутки, стоп -$20 (и вариант без дневных лимитов для сравнения).
"""
from __future__ import annotations

import argparse

import pandas as pd

from burst_sim import NO_DAY, build
from risk_sim import portfolio

SCEN = [
    ("как сейчас: 10 с после любого ордера", dict(min_interval=10.0)),
    ("1 с после любого + 10 с после покупки", dict(min_interval=1.0, after_fill_interval=10.0)),
    ("то же + пустые ордера не занимают лимит окна", dict(min_interval=1.0, after_fill_interval=10.0, release_unfilled=True)),
    ("1 с + 5 с после покупки + освобождать", dict(min_interval=1.0, after_fill_interval=5.0, release_unfilled=True)),
    ("1 с + 3 с после покупки + освобождать", dict(min_interval=1.0, after_fill_interval=3.0, release_unfilled=True)),
    ("только 1 с между ордерами + освобождать", dict(min_interval=1.0, release_unfilled=True)),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--thr", type=float, default=0.03)
    ap.add_argument("--sigma-mult", type=float, default=1.0)
    ap.add_argument("--slip", default="3")
    ap.add_argument("--latencies", default="250,300,400")
    ap.add_argument("--since", type=float, default=0)
    a = ap.parse_args()
    pd.set_option("display.width", 250)
    lat = [int(x) for x in a.latencies.split(",")]
    df = build(a.roots, a.source, a.thr, a.sigma_mult, a.slip, lat, a.since)
    span_days = (df.t.max() - df.t.min()) / 86_400_000.0
    print(f"\nсигналов {len(df[df.L == lat[0]])}, окон {df.w.nunique()}, период {span_days:.2f} сут (в_сутки считается по числу календарных дней)")
    for title, extra in (("реальные лимиты: $100 в сутки, стоп -$20", {}), ("без дневных лимитов", NO_DAY)):
        rows = []
        for L in lat:
            sub = df[df.L == L]
            for name, kw in SCEN:
                r = portfolio(sub, **{**extra, **kw})
                rows.append(dict(L=L, сценарий=name, ордеров=r["ордеров"], исполн=r["исполнений"], pnl=r["pnl_всего"],
                                 в_сутки=r["pnl_в_сутки"], просадка=r["просадка"], худшее_окно=r["худшее_окно"],
                                 на_исполнение=round(r["pnl_всего"] / max(r["исполнений"], 1), 2),
                                 пр_интервал=r.get("пр_интервал", 0), пр_после_покупки=r.get("пр_пауза_после_исполнения", 0),
                                 пр_лимит_окна=r.get("пр_ордеров_окно", 0), пр_лимит_суток=r.get("пр_лимит_суток", 0)))
        print(f"\n=== {title} ===")
        print(pd.DataFrame(rows).to_string(index=False))


if __name__ == "__main__":
    main()
