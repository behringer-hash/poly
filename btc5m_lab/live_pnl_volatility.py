"""Какие колебания pnl ожидать: по распределению результатов закрытых окон живого бота.

    python live_pnl_volatility.py bot_data_c2 [--stop 35] [--windows-per-day N]

Берём результаты окон (pnl_api, иначе pnl_est), считаем разброс на окно, затем моделируем сутки и неделю бутстрепом окон
в двух вариантах: как наблюдалось (среднее как есть) и без преимущества (среднее = 0). Выводим перцентили итога дня/недели,
вероятность закончить день в минусе и вероятность хоть раз упасть ниже -stop (общий убыток с начала).
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from analyze import load


def windows(root):
    w = load([root], "live_windows")
    for c in ("pnl_api", "pnl_est", "filled_orders", "orders"):
        w[c] = pd.to_numeric(w[c], errors="coerce")
    w = w.groupby("slug", as_index=False).last()
    w["t"] = w.slug.astype(str).str.rsplit("-", n=1).str[-1].astype(float).astype(int)
    w = w[w.filled_orders > 0].sort_values("t")
    w["pnl"] = w.pnl_api.fillna(w.pnl_est)
    return w


def simulate(x, n_per_day, days, stop, centered, rng, reps=4000):
    x = np.asarray(x, float)
    if centered:
        x = x - x.mean()
    day = np.empty(reps)
    hit_day = hit_all = 0
    week = np.empty(reps)
    for r in range(reps):
        path = rng.choice(x, n_per_day * days).cumsum()
        day[r] = path[n_per_day - 1]
        week[r] = path[-1]
        hit_day += path[:n_per_day].min() <= -stop
        hit_all += path.min() <= -stop
    return day, week, hit_day / reps, hit_all / reps


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--stop", type=float, default=35.0)
    ap.add_argument("--windows-per-day", type=int, default=0)
    a = ap.parse_args()
    w = windows(a.root)
    if w.empty:
        print("нет окон")
        return
    hrs = max((w.t.max() - w.t.min()) / 3600.0, 1.0)
    per_day = a.windows_per_day or int(round(len(w) / hrs * 24))
    x = w.pnl.values
    print(f"{a.root}: окон с исполнениями {len(w)} за {hrs:.1f} ч (≈{per_day} окон в сутки), ордеров в окне в среднем {w.orders.mean():.1f}")
    print(f"результат окна: среднее {x.mean():+.2f}$, стд {x.std():.2f}$, перцентили 5/25/50/75/95: " + " ".join(f"{np.percentile(x, q):+.1f}" for q in (5, 25, 50, 75, 95))
          + f", худшее {x.min():+.1f}$, лучшее {x.max():+.1f}$, итого {x.sum():+.2f}$")
    rng = np.random.default_rng(0)
    for centered, title in ((False, "как наблюдалось (среднее окна как есть)"), (True, "без преимущества (среднее окна = 0)")):
        day, week, hd, ha = simulate(x, per_day, 7, a.stop, centered, rng)
        print(f"\n=== {title} ===")
        print(f"итог за сутки, перцентили 5/25/50/75/95: " + " ".join(f"{np.percentile(day, q):+.0f}" for q in (5, 25, 50, 75, 95)) + f"; вероятность дня в минусе {np.mean(day < 0):.0%}")
        print(f"итог за неделю, перцентили 5/25/50/75/95: " + " ".join(f"{np.percentile(week, q):+.0f}" for q in (5, 25, 50, 75, 95)) + f"; вероятность недели в минусе {np.mean(week < 0):.0%}")
        print(f"вероятность хоть раз упасть ниже -{a.stop:g}$ (по закрытым окнам): в первые сутки {hd:.0%}, за неделю {ha:.0%}")


if __name__ == "__main__":
    main()
