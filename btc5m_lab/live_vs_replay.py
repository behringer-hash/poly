"""Каждый живой ордер против записанной книги Polymarket: мог ли он исполниться и почему не исполнился.

    python live_vs_replay.py bot_data_c1 --pm-roots data/2026-10-12 data/2026-10-13 [--out per_order.csv]

Для каждого живого ордера (mode=live) берём состояние верха книги СЕРВЕРА Polymarket (запись pm_top, время recv-d)
в моменты t_signal + L и проверяем: лучший ask не выше лимита ордера и объёма хватает. Дальше:
  1. доля ордеров, которые «должны были» исполниться при каждом L, против фактической доли;
  2. согласие по ордерам: при каком L прогноз чаще всего совпадает с фактом;
  3. «время убегания»: через сколько мс после сигнала лучший ask впервые стал выше лимита (для исполненных и нет);
  4. состояние сервера в момент сигнала: сколько ордеров уже были мертвы на старте (сервер ушёл раньше, чем мы увидели).
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from analyze import load
from lead_lag import PM, read

LAGS = [100, 150, 200, 250, 300, 350, 400, 500, 700]


def orders_table(roots: list[str]) -> pd.DataFrame:
    lo, meta = load(roots, "live_orders"), load(roots, "live_order_meta")
    if lo.empty:
        return lo
    lo = lo[lo["mode"] == "live"].copy()
    k = ["sid", "slug", "outcome"]
    lo = lo.merge(meta[k + ["ask_signal", "slip_c", "edge_c", "T"]], on=k, how="left") if len(meta) else lo
    lo["w"] = lo.slug.astype(str).str.rsplit("-", n=1).str[-1].astype(float).astype(int)
    lo["sgn"] = np.where(lo.outcome == "Up", 1, -1)
    lo["filled_f"] = lo.status == "matched"
    lo["t_ms"] = lo.t_signal.astype(float) * 1000.0
    return lo.reset_index(drop=True)


def side_px(m, sgn):
    """(цена, объём) стороны ордера по верху книги Up: Down = зеркало."""
    if m is None:
        return np.nan, np.nan
    if sgn > 0:
        return m[1], m[3]
    return ((1 - m[0]) if np.isfinite(m[0]) else np.nan), m[2]


def would_fill(pm: PM, w: int, sgn: int, t_ms: float, limit: float, size: float, min_fill: float = 1.0) -> bool:
    px, avail = side_px(pm.state(w, t_ms, "srv"), sgn)
    return bool(np.isfinite(px) and np.isfinite(avail) and px <= limit + 1e-9 and min(size, avail) >= min_fill - 1e-9)


def run_away_ms(pm: PM, w: int, sgn: int, t_ms: float, limit: float, horizon_ms: float = 2000.0):
    """Сколько мс после t_ms лучший ask стороны впервые выше лимита (None - не убежал за горизонт, 0 - уже выше)."""
    s = pm.by_w.get(w, {}).get("srv")
    if s is None:
        return np.nan
    i0 = np.searchsorted(s["t"], t_ms, side="right") - 1
    idx = range(max(i0, 0), len(s["t"]))
    for i in idx:
        t = s["t"][i]
        if t > t_ms + horizon_ms:
            break
        px, _ = side_px((s["bid"][i], s["ask"][i], s["bsz"][i], s["asz"][i]), sgn)
        if np.isfinite(px) and px > limit + 1e-9:
            return max(t - t_ms, 0.0)
    return np.inf


def analyze(d: pd.DataFrame, pm: PM, lags=LAGS) -> dict:
    d = d.copy()
    for L in lags:
        d[f"wf{L}"] = [would_fill(pm, r.w, r.sgn, r.t_ms + L, float(r.limit), float(r["size"]) if "size" in d else 5.0)
                       for _, r in d.iterrows()]
    d["dead0"] = [not would_fill(pm, r.w, r.sgn, r.t_ms, float(r.limit), 1.0) for r in d.itertuples()]
    d["run_ms"] = [run_away_ms(pm, r.w, r.sgn, r.t_ms, float(r.limit)) for r in d.itertuples()]
    rows = []
    for L in lags:
        pred = d[f"wf{L}"]
        rows.append(dict(L=L, должны_исполниться=round(pred.mean(), 3), фактически=round(d.filled_f.mean(), 3),
                         согласие=round((pred == d.filled_f).mean(), 3),
                         из_исполненных_прогноз_да=round(pred[d.filled_f].mean(), 3) if d.filled_f.any() else np.nan,
                         из_неисполненных_прогноз_да=round(pred[~d.filled_f].mean(), 3)))
    return dict(table=pd.DataFrame(rows), data=d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+", help="папки данных бота (bot_data_c1)")
    ap.add_argument("--pm-roots", nargs="+", required=True, help="папки записи сервера (data/ГГГГ-ММ-ДД) с pm_top")
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    d = orders_table(a.roots)
    if d.empty:
        print("нет живых ордеров")
        return
    pt = pd.concat([read(r, "pm_top") for r in a.pm_roots], ignore_index=True)
    pm = PM(pt)
    d = d[d.w.isin(pm.by_w)].copy()
    print(f"живых ордеров с записью книги: {len(d)}, исполнено {d.filled_f.mean():.1%}; "
          f"http_ms медиана {d.http_ms.median():.0f}, p90 {d.http_ms.quantile(.9):.0f}")
    res = analyze(d, pm)
    print("\n=== 1-2. Прогноз по книге сервера (любой объём ≥ 1 шт) против факта ===")
    print(res["table"].to_string(index=False))
    d = res["data"]
    dead = d.dead0.mean()
    print(f"\n=== 4. Ордеров, уже мёртвых на старте (сервер в момент сигнала дороже лимита): {dead:.1%}; "
          f"из них исполнено {d[d.dead0].filled_f.mean():.1%}, из остальных {d[~d.dead0].filled_f.mean():.1%}")
    fin = d[np.isfinite(d.run_ms)]
    bins = [-1, 0, 50, 100, 150, 200, 300, 500, 1000, 1e9]
    lab = ["0 (уже выше)", "≤50", "50-100", "100-150", "150-200", "200-300", "300-500", "500-1000", ">1000"]
    cut = pd.cut(d.run_ms.replace(np.inf, 5e8), bins, labels=lab)
    g = d.groupby(cut, observed=True).agg(ордеров=("filled_f", "size"), исполнено=("filled_f", "mean"))
    g["доля_%"] = (100 * g["ордеров"] / len(d)).round(1)
    print("\n=== 3. Время убегания цены за лимит (мс после сигнала) ===")
    print(g.round(3).to_string())
    if len(fin):
        print(f"медиана времени убегания: {fin.run_ms.median():.0f} мс; "
              f"не убежала за 2 с: {(~np.isfinite(d.run_ms) | (d.run_ms == np.inf)).mean():.1%}")
    if a.out:
        keep = ["sid", "slug", "outcome", "t_signal", "limit", "size", "status", "filled", "avg_px", "http_ms", "total_ms",
                "dead0", "run_ms"] + [f"wf{L}" for L in LAGS]
        d[[c for c in keep if c in d.columns]].to_csv(a.out, index=False)


if __name__ == "__main__":
    main()
