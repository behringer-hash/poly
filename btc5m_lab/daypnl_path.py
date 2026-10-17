"""Путь дневного pnl бота по закрытым окнам: как менялся счётчик day_pnl и где сработал лимит убытка.

    python daypnl_path.py bot_data_c1_s7
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone

import pandas as pd

from analyze import load


def main():
    w = load(sys.argv[1:], "live_windows")
    w["t"] = w.slug.astype(str).str.rsplit("-", n=1).str[-1].astype(float).astype(int)
    for c in ("pnl_est", "pnl_api", "day_pnl", "usdc_api"):
        w[c] = pd.to_numeric(w[c], errors="coerce")
    w = w.sort_values("t").drop_duplicates("slug", keep="last")
    w["utc"] = [datetime.fromtimestamp(x, tz=timezone.utc) for x in w.t]
    w["день"] = w.utc.dt.strftime("%m-%d")
    print(f"окон {len(w)}, с {w.utc.min()} по {w.utc.max()}")
    print("\n=== по суткам UTC: окон, сумма pnl_est, сумма pnl_api, последний day_pnl, минимум day_pnl, максимум day_pnl, потрачено api ===")
    g = w.groupby("день").agg(окон=("slug", "size"), pnl_est=("pnl_est", "sum"), pnl_api=("pnl_api", "sum"), последний=("day_pnl", "last"),
                              минимум=("day_pnl", "min"), максимум=("day_pnl", "max"), потрачено=("usdc_api", "sum"))
    print(g.round(2).to_string())
    print(f"\nвсего: pnl_est {w.pnl_est.sum():+.2f}, pnl_api {w.pnl_api.sum():+.2f}")
    w["cum_api"] = w.pnl_api.fillna(w.pnl_est).cumsum()
    print(f"кумулятивный pnl (api, иначе est): минимум {w.cum_api.min():+.2f}, максимум {w.cum_api.max():+.2f}, конец {w.cum_api.iloc[-1]:+.2f}, просадка от максимума {(w.cum_api - w.cum_api.cummax()).min():+.2f}")
    print("\n=== последние 12 окон: время, pnl_est, pnl_api, day_pnl ===")
    print(w[["utc", "orders", "filled_orders", "pnl_est", "pnl_api", "day_pnl"]].tail(12).to_string(index=False))


if __name__ == "__main__":
    main()
