"""Что было бы с ЖИВЫМИ ордерами, если бы переплата была больше: исполнения и доходность по книге сервера при фактической задержке каждого ордера.

    python live_slip_whatif.py bot_data_c1 --pm-roots data/2026-10-12 data/2026-10-13

Момент матчинга ордера = t_sent + http_ms - c; смещение c подбираем по согласию прогноза с фактом при фактической переплате (k=0),
затем для k = 0..10 ц к фактическому лимиту считаем: исполняется ли ордер (лучший ask сервера <= новый лимит, объём >= 5), по какой цене,
и доход при удержании до экспирации (победитель из live_windows) с комиссией 0.07*p*(1-p). Неисполненные = 0.
Ограничение: влияние нашего ордера на книгу и реакция конкурентов на нашу большую переплату не моделируются.
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--pm-roots", nargs="+", required=True)
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    d = orders_table(a.roots)
    days = {datetime.fromtimestamp(int(w), tz=timezone.utc).strftime("%Y-%m-%d") for w in d.w}
    roots = [r for r in a.pm_roots if os.path.basename(os.path.normpath(r)) in days]
    pm = PM(pd.concat([read(r, "pm_top") for r in roots], ignore_index=True))
    d = d[d.w.isin(pm.by_w)].copy()
    w = load(a.roots, "live_windows").groupby("slug", as_index=False).last()
    win = {s: str(x) for s, x in zip(w.slug, w.winner)}
    d["win"] = d.slug.map(win)
    print(f"ордеров {len(d)}, победитель известен у {d.win.notna().sum()}; значения winner: {sorted(set(d.win.dropna()))[:5]}")
    d["won"] = [np.nan if not isinstance(x, str) or x in ("nan", "None", "") else float(x.upper().startswith(("U", "1")) == (s > 0)) for x, s in zip(d.win, d.sgn)]
    d["ts"] = d.t_sent.astype(float) * 1000.0
    d["h"] = d.http_ms.astype(float)
    d["lim"] = d.limit.astype(float)
    d["size"] = d["size"].astype(float)

    def fill(r, c, k):
        t = r.ts + r.h - c
        px, av = side_px(pm.state(r.w, t, "srv"), r.sgn)
        lim = min(r.lim + k / 100.0, 0.99)
        ok = np.isfinite(px) and np.isfinite(av) and px <= lim + 1e-9 and min(r.size, av) >= 5 - 1e-9
        return ok, px

    print("\n=== подбор смещения c (мс): согласие прогноза с фактом при фактической переплате ===")
    best = (None, -1)
    for c in (0, 50, 100, 150, 200, 250, 300):
        ag = np.mean([fill(r, c, 0)[0] == r.filled_f for r in d.itertuples()])
        pr = np.mean([fill(r, c, 0)[0] for r in d.itertuples()])
        print(f"c={c:4d}: согласие {ag:.3f}, прогноз исполнено {pr:.3f} (факт {d.filled_f.mean():.3f})")
        if ag > best[1]:
            best = (c, ag)
    for c in sorted({best[0], max(best[0] - 50, 0), best[0] + 50}):
        print(f"\n=== что если переплата больше на k ц (c={c}) ===")
        rows = []
        for k in (0, 3, 5, 7, 10, 13, 17):
            f = [fill(r, c, k) for r in d.itertuples()]
            ok = np.array([x[0] for x in f])
            px = np.array([x[1] for x in f])
            fee = 0.07 * px * (1 - px)
            pay = np.where(d.won.values == 1, 1.0, 0.0) - px - fee
            m = ok & d.won.notna().values
            n = int(d.won.notna().sum())
            per_sig = float(np.where(m, pay, 0).sum() / n * 100)
            rows.append(dict(доплата_ц=k, исполнено=round(ok.mean(), 3), ср_цена=round(float(px[ok].mean()), 3) if ok.any() else np.nan,
                             ц_на_исполнение=round(float(pay[m].mean() * 100), 2) if m.any() else np.nan, ц_на_ордер=round(per_sig, 2),
                             долл_всего=round(float((pay[m] * d["size"].values[m]).sum()), 2), исполнений=int(ok.sum())))
        print(pd.DataFrame(rows).to_string(index=False))


if __name__ == "__main__":
    main()
