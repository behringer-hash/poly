"""Разложение разрыва «бумага против жизни» на одних и тех же живых ордерах.

    python live_decompose.py bot_data_c1_s7 --pm-roots data/2026-10-16 data/2026-10-17 data/2026-10-18

Берём ордера, которые бот реально отправил (лимит и размер как в жизни), и считаем результат (ц на ордер, неисполненные = 0; $ всего) в сценариях:
  A  бумага: матч через 200 мс, книга, дошедшая до нас (rcv)          - как считает бумажный бот
  B  то же, но книга сервера (srv)
  C  300 мс, srv        D  335 мс (медиана живых), srv
  E  фактическая задержка каждого ордера (t_sent + http_ms - c), srv
  F  факт: что реально исполнилось и сколько заработало (цена исполнения, комиссия, победитель из live_windows)
Разница между соседними сценариями показывает вклад каждого фактора: задержка 200 -> 335 (A->B->D), разброс и зависимость задержки от сигнала (D->E), остальное (E->F).
"""
from __future__ import annotations

import argparse
import os
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from analyze import load
from lead_lag import PM, read
from live_vs_replay import orders_table, side_px

FEE = 0.07


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--pm-roots", nargs="+", required=True)
    ap.add_argument("--c", type=float, default=25.0, help="смещение матчинга от ответа биржи, мс (подбирается в live_slip_whatif)")
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    d = orders_table(a.roots)
    days = {datetime.fromtimestamp(int(w), tz=timezone.utc).strftime("%Y-%m-%d") for w in d.w}
    roots = [r for r in a.pm_roots if os.path.basename(os.path.normpath(r)) in days]
    pm = PM(pd.concat([read(r, "pm_top") for r in roots], ignore_index=True))
    d = d[d.w.isin(pm.by_w)].copy()
    w = load(a.roots, "live_windows").groupby("slug", as_index=False).last()
    win = dict(zip(w.slug, w.winner.astype(str)))
    d["win"] = d.slug.map(win)
    d = d[d.win.isin(["Up", "Down"])].copy()
    d["won"] = ((d.win == "Up") == (d.sgn > 0)).astype(float)
    d["ts"] = d.t_sent.astype(float) * 1000.0
    d["h"] = d.http_ms.astype(float)
    d["lim"] = d.limit.astype(float)
    d["size"] = d["size"].astype(float)
    print(f"ордеров с известным победителем {len(d)}, из {d.slug.nunique()} окон; фактическая доля исполнений {d.filled_f.mean():.1%}; медиана http {d.h.median():.0f} мс")

    def sim(kind, t_fn):
        fills, pay = [], []
        for r in d.itertuples():
            px, av = side_px(pm.state(r.w, t_fn(r), kind), r.sgn)
            ok = np.isfinite(px) and np.isfinite(av) and px <= r.lim + 1e-9 and min(r.size, av) >= 5 - 1e-9
            fills.append(ok)
            pay.append((r.won - px - FEE * px * (1 - px)) * min(r.size, av) if ok else 0.0)
        return np.array(fills), np.array(pay)

    med = float(d.h.median())
    scen = [("A бумага: 200 мс, книга rcv", "rcv", lambda r: r.t_ms + 200.0),
            ("B 200 мс, книга сервера", "srv", lambda r: r.t_ms + 200.0),
            ("C 300 мс, сервер", "srv", lambda r: r.t_ms + 300.0),
            (f"D {med:.0f} мс (медиана живых), сервер", "srv", lambda r: r.t_ms + med),
            ("E фактическая задержка каждого ордера", "srv", lambda r: r.ts + r.h - a.c)]
    rows = []
    for name, kind, fn in scen:
        f, p = sim(kind, fn)
        rows.append(dict(сценарий=name, исполнено=round(f.mean(), 3), долл_всего=round(p.sum(), 2), ц_на_ордер=round(p.sum() / d["size"].sum() * 100, 2),
                         ц_на_исполненный_шейр=round(p.sum() / max(d["size"].values[f].sum(), 1) * 100, 2)))
    fee = FEE * d.avg_px.astype(float) * (1 - d.avg_px.astype(float))
    real = np.where(d.filled_f, (d.won - d.avg_px.astype(float) - fee) * d.filled.astype(float), 0.0)
    sz = d.filled.astype(float).where(d.filled_f, 0).sum()
    rows.append(dict(сценарий="F факт (живые исполнения)", исполнено=round(d.filled_f.mean(), 3), долл_всего=round(float(real.sum()), 2),
                     ц_на_ордер=round(real.sum() / d["size"].sum() * 100, 2), ц_на_исполненный_шейр=round(real.sum() / max(sz, 1) * 100, 2)))
    print("\n=== результат на одних и тех же ордерах (ц на ордер: на каждый отправленный шейр) ===")
    print(pd.DataFrame(rows).to_string(index=False))
    # какие ордера исполняются в E, но не в A, и наоборот: качество «потерянных» исполнений
    fA, pA = sim("rcv", lambda r: r.t_ms + 200.0)
    fE, pE = sim("srv", lambda r: r.ts + r.h - a.c)
    m = fA & ~fE
    print(f"\nисполнились бы в бумаге (A), но не в жизни (E): {int(m.sum())} ордеров ({m.mean():.1%}), их результат по бумаге {pA[m].sum():+.2f}$ "
          f"({pA[m].sum() / max(d['size'].values[m].sum(), 1) * 100:+.2f} ц/шейр)")
    both = fA & fE
    print(f"исполнились в обоих: {int(both.sum())}, результат по бумаге {pA[both].sum():+.2f}$ ({pA[both].sum() / max(d['size'].values[both].sum(), 1) * 100:+.2f} ц/шейр)")
    print("\n(если «исполнились бы в бумаге, но не в жизни» сильно прибыльнее «в обоих» - исполнения теряются именно на лучших сигналах)")
    rng = np.random.default_rng(0)
    idx = np.arange(len(d))
    bs = [pA[b].sum() - pE[b].sum() for b in (rng.choice(idx, len(idx)) for _ in range(500))]
    print(f"A минус E, $ (95% ИИ бутстреп по ордерам): {pA.sum() - pE.sum():+.2f} [{np.percentile(bs, 2.5):+.2f}; {np.percentile(bs, 97.5):+.2f}]")


if __name__ == "__main__":
    main()
