"""Вскрытие живых ордеров: на каком этапе ордер «умер» и чем отличаются исполненные от неисполненных.

    python live_autopsy.py bot_data_c1 --pm-roots data/2026-10-12 data/2026-10-13

Для каждого живого ордера смотрим книгу СЕРВЕРА Polymarket в моменты: сигнал, отправка (t_sent), ответ (t_resp), и время убегания цены за лимит
относительно отправки. Категории: мёртв на сигнале / убежала до ответа биржи / жива к ответу, но не исполнен / исполнен.
Также: статусы и тексты ошибок, доля исполнений по http_ms и по категориям, живой pnl по закрытым окнам (последняя запись каждого окна).
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from analyze import load
from lead_lag import PM, read
from live_vs_replay import orders_table, run_away_ms, would_fill


def live_pnl(roots: list[str]) -> None:
    w = load(roots, "live_windows")
    if w.empty:
        print("нет live_windows")
        return
    for c in ("filled_orders", "usdc_api", "fees_api", "pnl_est", "pnl_api"):
        w[c] = pd.to_numeric(w[c], errors="coerce")
    w = w.groupby("slug", as_index=False).last()
    f = w[w.filled_orders > 0]
    print(f"окон с исполнениями {len(f)} из {len(w)}; pnl_api {f.pnl_api.sum():+.2f}$ (по {f.pnl_api.notna().sum()} окнам с api), "
          f"pnl_est {f.pnl_est.sum():+.2f}$, потрачено api {f.usdc_api.sum():.2f}$, комиссии {f.fees_api.sum():.2f}$")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--pm-roots", nargs="+", required=True)
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    d = orders_table(a.roots)
    if d.empty:
        print("нет живых ордеров")
        return
    print("=== живой pnl ===")
    live_pnl(a.roots)
    print(f"\nордеров {len(d)}, исполнено {d.filled_f.mean():.1%}")
    print("\n=== статусы ===")
    print(d.status.value_counts().to_string())
    if "error" in d:
        e = d.error.fillna("").astype(str).str.slice(0, 90)
        print("\n=== тексты ошибок/ответов (топ) ===")
        print(e[e != ""].value_counts().head(8).to_string())
    pm = PM(pd.concat([read(r, "pm_top") for r in a.pm_roots], ignore_index=True))
    d = d[d.w.isin(pm.by_w)].copy()
    print(f"\nс записью книги: {len(d)}")
    d["ts"] = d.t_sent.astype(float) * 1000.0
    d["tr"] = d.t_resp.astype(float) * 1000.0
    d["wf_sig"] = [would_fill(pm, r.w, r.sgn, r.t_ms, float(r.limit), 1.0) for r in d.itertuples()]
    d["wf_sent"] = [would_fill(pm, r.w, r.sgn, r.ts, float(r.limit), 1.0) for r in d.itertuples()]
    d["wf_resp"] = [would_fill(pm, r.w, r.sgn, r.tr, float(r.limit), 1.0) for r in d.itertuples()]
    d["wf_mid"] = [would_fill(pm, r.w, r.sgn, (r.ts + r.tr) / 2, float(r.limit), 1.0) for r in d.itertuples()]
    d["run_after_send"] = [run_away_ms(pm, r.w, r.sgn, r.ts, float(r.limit), 3000.0) for r in d.itertuples()]
    d["h"] = d.http_ms.astype(float)
    d["send_lag"] = d.ts - d.t_ms
    cat = np.select([~d.wf_sig, ~d.wf_sent, ~d.wf_mid, ~d.wf_resp], ["1 мёртв на сигнале", "2 умер до отправки", "3 умер в первой половине пути", "4 умер во второй половине пути"],
                    "5 жив к ответу биржи")
    d["cat"] = cat
    g = d.groupby("cat").agg(ордеров=("filled_f", "size"), исполнено=("filled_f", "mean"), мед_http=("h", "median"), мед_отправка_мс=("send_lag", "median"))
    g["доля"] = (g["ордеров"] / len(d)).round(3)
    print("\n=== на каком этапе умер ордер (по книге сервера) ===")
    print(g.round(3).to_string())
    print("\n=== в категории 5 (книга жива к ответу): исполнено по http_ms ===")
    s = d[d.cat.str.startswith("5")]
    if len(s):
        print(s.groupby(pd.cut(s.h, [0, 260, 300, 350, 450, 700, 1e6]), observed=True).filled_f.agg(["size", "mean"]).round(3).to_string())
    print("\n=== исполнено по категориям: ИСПОЛНЕНО при том, что книга по записи уже была выше лимита (ошибка записи/задержка ленты?) ===")
    x = d[d.filled_f]
    print(f"исполненных {len(x)}; из них книга выше лимита к ответу: {(~x.wf_resp).mean():.1%}; на отправке: {(~x.wf_sent).mean():.1%}")
    print("\n=== задержка от сигнала до отправки (мс) ===")
    print(d.send_lag.describe().round(1).to_string())
    print("\n=== время убегания после отправки, мс: исполненные vs нет ===")
    for k, gg in d.groupby("filled_f"):
        r = gg.run_after_send.replace(np.inf, np.nan).dropna()
        print(f"исполнен={k}: n {len(gg)}, убежала за 3 с у {len(r)}, медиана {r.median():.0f}, p25 {r.quantile(.25):.0f}, p75 {r.quantile(.75):.0f}; http_ms медиана {gg.h.median():.0f}")
    d["day"] = (d.w // 86400).astype(int)
    print("\n=== по часам (UTC): ордеров, исполнено, мёртвых на сигнале ===")
    d["hr"] = ((d.w % 86400) // 3600).astype(int) // 3 * 3
    print(d.groupby(["day", "hr"]).agg(ордеров=("filled_f", "size"), исполнено=("filled_f", "mean"), мёртв=("wf_sig", lambda v: 1 - v.mean())).round(3).to_string())


if __name__ == "__main__":
    main()
