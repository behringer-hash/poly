"""Сводка по файлу activity кошелька (wallet_history.py): типы событий по дням, размеры сделок, время сделок в окне.

    python wallet_hist_stats.py ~/wallets/act_0x3048d653.csv.gz --out OUT
"""
import argparse
import os

import numpy as np
import pandas as pd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    A = pd.read_csv(a.file, usecols=["timestamp", "type", "slug", "outcome", "side", "price", "size", "usdcSize"])
    A["day"] = pd.to_datetime(A.timestamp, unit="s").dt.strftime("%Y-%m-%d")
    A["usdc"] = pd.to_numeric(A.usdcSize, errors="coerce").fillna(0)
    T = A.pivot_table(index="day", columns="type", values="usdc", aggfunc="sum").fillna(0).round(2)
    T.to_csv(os.path.join(a.out, "types_by_day.csv"))
    print(T.tail(50).to_string())
    t = A[(A.type == "TRADE") & A.slug.astype(str).str.startswith("btc-updown-5m")].copy()
    t["w"] = pd.to_numeric(t.slug.str.extract(r"-(\d{9,})$")[0], errors="coerce")
    t["rel"] = t.timestamp - t.w
    t["sz"] = pd.to_numeric(t["size"], errors="coerce")
    t["wk"] = pd.to_datetime(t.timestamp, unit="s").dt.to_period("W-SUN").astype(str)
    print("\nпродажи по неделям:", t.groupby("wk").side.apply(lambda v: (v == "SELL").mean()).round(4).to_dict())
    q = t.groupby("wk").agg(n=("sz", "size"), med=("sz", "median"), p90=("sz", lambda v: v.quantile(0.9)),
                            rel_p10=("rel", lambda v: v.quantile(0.1)), rel_med=("rel", "median"),
                            rel_p90=("rel", lambda v: v.quantile(0.9)), pre=("rel", lambda v: (v < 0).mean()),
                            px_med=("price", "median"))
    print("\n" + q.round(2).to_string())
    q.to_csv(os.path.join(a.out, "trades_by_week.csv"))
    h = t.assign(r=pd.cut(t.rel, [-700, -300, -120, -63, -30, 0, 30, 60, 120, 180, 240, 270, 300, 400])) \
        .pivot_table(index="r", columns="wk", values="sz", aggfunc="sum", observed=True).fillna(0)
    (h / h.sum()).round(3).to_csv(os.path.join(a.out, "rel_profile_by_week.csv"))
    print("\n" + (h / h.sum()).round(3).iloc[:, -8:].to_string())


if __name__ == "__main__":
    main()
