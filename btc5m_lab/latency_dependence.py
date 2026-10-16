"""Зависит ли время ответа биржи на ордер от состояния рынка и от того, мог ли ордер исполниться при приходе.

    python latency_dependence.py data/2026-10-12 data/2026-10-13 --live-data bot_data_c1 --source bybit

Живые ордера делим на «исполнимые при приходе на биржу» (книга сервера через 25 мс после сигнала ещё не выше лимита)
и «неисполнимые» (цена уже ушла) и сравниваем время ответа. Затем у исполнимых смотрим, связано ли «медленно» (> 400 мс)
с признаками активности рынка на момент сигнала (число обновлений книги за 500 мс, возраст верха, размер скачка BTC, сила сигнала,
время до конца окна, сделки рынка за 1 с, лаг ленты Polymarket) и с долей исполнений по времени ответа.
"""
from __future__ import annotations

import argparse
import os
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from fill_predict import FEATS, auc, features
from lead_lag import PM, read
from live_vs_replay import orders_table, would_fill
from momentum_features import fit_logit

QS = [0.05, 0.1, 0.25, 0.5, 0.75, 0.9]


def find_root(roots: list[str], w: int) -> str | None:
    name = datetime.fromtimestamp(w, tz=timezone.utc).strftime("%Y-%m-%d")
    for r in roots:
        if os.path.basename(os.path.normpath(r)) == name:
            return r
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--live-data", nargs="+", required=True)
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--slow-ms", type=float, default=400.0)
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    d = orders_table(a.live_data)
    if d.empty:
        print("нет живых ордеров")
        return
    pms = {}
    for r in a.roots:
        pm = PM(read(r, "pm_top"))
        pms[r] = pm
    d["root"] = [find_root(a.roots, int(w)) for w in d.w]
    d = d[d.root.notna()].copy()
    d["arrive"] = [would_fill(pms[r.root], r.w, r.sgn, r.t_ms + 25.0, float(r.limit), 1.0) for r in d.itertuples()]
    d["slow"] = d.http_ms > a.slow_ms
    d["filled"] = d.filled_f
    print(f"живых ордеров {len(d)}, исполнено {d.filled.mean():.1%}; исполнимых при приходе {d.arrive.mean():.1%}")
    rows = []
    for name, m in (("исполнимы при приходе (цена ещё не ушла)", d.arrive), ("неисполнимы при приходе (цена уже ушла)", ~d.arrive)):
        s = d[m]
        rows.append(dict(группа=name, ордеров=len(s), исполнено=round(s.filled.mean(), 3), **{f"p{int(q * 100)}": round(s.http_ms.quantile(q)) for q in QS},
                         медленных=round(s.slow.mean(), 3), свыше_1с=round((s.http_ms > 1000).mean(), 3)))
    print("\n=== время ответа биржи http_ms по группам ===")
    print(pd.DataFrame(rows).to_string(index=False))
    s = d[d.arrive].copy()
    s["hb"] = pd.cut(s.http_ms, [0, 260, 300, 350, 450, 700, 1e6])
    print("\n=== у исполнимых при приходе: доля исполнений по времени ответа ===")
    print(s.groupby("hb", observed=True).filled.agg(["size", "mean"]).round(3).to_string())
    # признаки на момент сигнала
    parts = []
    for r, g in s.groupby("root"):
        sigs = [dict(w=int(x.w), sgn=int(x.sgn), t=float(x.t_ms), view=float(x.ask_signal) if np.isfinite(x.ask_signal) else float(x.limit) - 0.03,
                     edge=float(x.edge_c) / 100.0 if np.isfinite(x.edge_c) else 0.03) for x in g.itertuples()]
        f = features(r, a.source, g, sigs)
        if len(f):
            parts.append(f.merge(g[["w", "t_ms", "sgn", "slow", "http_ms", "filled"]].rename(columns={"t_ms": "t"}), on=["w", "t", "sgn"], how="inner"))
    if not parts:
        print("нет признаков")
        return
    f = pd.concat(parts, ignore_index=True)
    print(f"\n=== у исполнимых при приходе ({len(f)} ордеров): доля медленных (> {a.slow_ms:g} мс) по квинтилям признаков ===")
    for c in FEATS:
        x = f[c].astype(float)
        if x.nunique() < 5:
            continue
        q = pd.qcut(x.rank(method="first"), 4, labels=False)
        print(f"{c:8s} " + "  ".join(f"[{x[q == k].mean():8.1f}] {f.slow[q == k].mean():.2f}" for k in range(4)))
    X = f[FEATS].astype(float).fillna(0.0)
    Z = ((X - X.mean()) / X.std().replace(0, 1.0)).values
    y = f.slow.astype(float).values
    b0, beta = fit_logit(Z, y, np.zeros(len(y)), l2=10.0)
    p = 1 / (1 + np.exp(-(b0 + Z @ beta)))
    print(f"\nлогистическая модель «медленный ответ» по признакам (на тех же данных, переобучение возможно): AUC {auc(y, p):.3f}")
    print("коэффициенты: " + ", ".join(f"{c} {b:+.2f}" for c, b in zip(FEATS, beta)))
    # перестановочный контроль, чтобы отличить закономерность от шума при ~260 ордерах
    rng = np.random.default_rng(0)
    null = []
    for _ in range(100):
        yp = rng.permutation(y)
        b0p, bp = fit_logit(Z, yp, np.zeros(len(y)), l2=10.0)
        null.append(auc(yp, 1 / (1 + np.exp(-(b0p + Z @ bp)))))
    print(f"контроль: AUC при случайной перестановке меток в среднем {np.mean(null):.3f}, 95-й процентиль {np.percentile(null, 95):.3f}")


if __name__ == "__main__":
    main()
