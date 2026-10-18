"""Различают ли признаки момента сигнала прибыльные и убыточные ЖИВЫЕ покупки (а не номинальную силу сигнала).

    python live_features_pnl.py bot_data_c1 --pm-roots data/2026-10-12 data/2026-10-13 [--run r1] ...
    python live_features_pnl.py --run r1 bot_data_c1 --run r2 bot_data_c1_s7 --pm-roots data/...

Для каждого живого ордера берём признаки на момент сигнала (книга Polymarket: возраст верха, обновления за 500 мс, спред, объём, движение цены;
сделки рынка за 1 с; скачок Bybit за 500 мс; скачок Binance-фьючерса за 500 мс в ту же сторону; сила сигнала; время до конца) и считаем по квартилям:
доля исполнений, ц/шейр на исполненных, $ на ордер. Смотрим только признаки, у которых порядок квартилей (знак наклона) совпадает в обоих запусках.
"""
from __future__ import annotations

import argparse
import os
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from analyze import load
from fill_predict import FEATS, features
from live_vs_replay import orders_table
from momentum_features import last_at
from replay import load_source

FEE = 0.07


def run_table(root: str, run: str, pm_roots: list[str]) -> pd.DataFrame:
    d = orders_table([root])
    w = load([root], "live_windows").groupby("slug", as_index=False).last()
    d["win"] = d.slug.map(dict(zip(w.slug, w.winner.astype(str))))
    d = d[d.win.isin(["Up", "Down"])].copy()
    d["won"] = ((d.win == "Up") == (d.sgn > 0)).astype(float)
    d["avg"] = d.avg_px.astype(float)
    d["fsh"] = d.filled.astype(float).where(d.filled_f, 0.0)
    d["pnl"] = np.where(d.filled_f, (d.won - d.avg - FEE * d.avg * (1 - d.avg)) * d.fsh, 0.0)
    d["day"] = [datetime.fromtimestamp(int(x), tz=timezone.utc).strftime("%Y-%m-%d") for x in d.w]
    parts = []
    for r in pm_roots:
        name = os.path.basename(os.path.normpath(r))
        g = d[d.day == name]
        if g.empty:
            continue
        sigs = [dict(w=int(x.w), sgn=int(x.sgn), t=float(x.t_ms), view=float(x.ask_signal) if np.isfinite(float(x.ask_signal)) else float(x.limit) - 0.03,
                     edge=float(x.edge_c) / 100.0 if np.isfinite(float(x.edge_c)) else 0.03) for x in g.itertuples()]
        f = features(r, "bybit", g, sigs)
        if f.empty:
            continue
        tb, pb = load_source(r, "binance_fut")
        f["bn"] = [(last_at(tb, pb, t) - last_at(tb, pb, t - 500)) * s for t, s in zip(f.t, f.sgn)]     # скачок Binance-фьючерса в сторону ордера, $
        f["bybit_dir"] = f.btc                                                                          # |скачок Bybit| за 500 мс
        f["x_agree"] = (f.bn > 0).astype(float)
        parts.append(f.merge(g[["w", "t_ms", "sgn", "filled_f", "pnl", "fsh", "size"]].rename(columns={"t_ms": "t", "size": "osize"}), on=["w", "t", "sgn"], how="inner"))
    out = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()
    out["run"] = run
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="append", nargs=2, metavar=("NAME", "DIR"), required=True)
    ap.add_argument("--pm-roots", nargs="+", required=True)
    a = ap.parse_args()
    pd.set_option("display.width", 240)
    f = pd.concat([run_table(dr, nm, a.pm_roots) for nm, dr in a.run], ignore_index=True)
    f["osize"] = f["osize"].astype(float)
    print(f"ордеров с признаками {len(f)}, исполнено {int(f.filled_f.sum())}; " + ", ".join(f"{r}: {len(x)} ордеров, {x.pnl.sum():+.2f}$" for r, x in f.groupby("run")))
    feats = FEATS + ["bn", "x_agree"]
    rows = []
    for c in feats:
        x = f[c].astype(float)
        if x.nunique() < 4:
            continue
        q = pd.qcut(x.rank(method="first"), 4, labels=False)
        per = {}
        for run, g in f.groupby("run"):
            qq = q[g.index]
            per[run] = [g.pnl[qq == k].sum() / max(g["osize"][qq == k].sum(), 1) * 100 for k in range(4)]     # ц на отправленный шейр
        tot = [f.pnl[q == k].sum() for k in range(4)]
        fr = [f.filled_f[q == k].mean() for k in range(4)]
        sl = {r: np.polyfit(range(4), v, 1)[0] for r, v in per.items()}
        same = len({np.sign(v) for v in sl.values()}) == 1
        rows.append(dict(признак=c, q1_ср=round(x[q == 0].mean(), 1), q4_ср=round(x[q == 3].mean(), 1),
                         долл_по_кв=" ".join(f"{v:+.1f}" for v in tot), доля_исп=" ".join(f"{v:.2f}" for v in fr),
                         **{f"{r}_ц/шейр_по_кв": " ".join(f"{v:+.1f}" for v in vs) for r, vs in per.items()}, знак_наклона_совпал=same))
    print("\n=== признак -> квартили (q1 - низкие значения признака): $ всего, доля исполнений, ц на отправленный шейр по запускам ===")
    print(pd.DataFrame(rows).to_string(index=False))
    # подтверждение скачка другой биржей
    for col, name in (("x_agree", "Binance-фьючерс сдвинулся в ту же сторону за 500 мс"),):
        print(f"\n=== {name} ===")
        for k, g in f.groupby(col):
            for run, y in g.groupby("run"):
                fl = y[y.filled_f]
                print(f"{col}={k:.0f} {run}: ордеров {len(y)}, исполнено {y.filled_f.mean():.2f}, $ {y.pnl.sum():+.2f}, ц/шейр на исполненных {fl.pnl.sum() / max(fl.fsh.sum(), 1) * 100:+.2f}")
    print("\nОграничение: ~1200 ордеров, 400 исполнений; признаков 15 - часть наклонов случайна; нужны одинаковые знаки в обоих запусках.")


if __name__ == "__main__":
    main()
