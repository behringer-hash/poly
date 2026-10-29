"""Вся история кошелька Polymarket (data-api /activity) с адаптивной нарезкой по времени.

    python wallet_history.py 0x3048... --out DIR [--store ~/wallets] [--since 2025-01-01]

API отдаёт не больше 500 записей за запрос и не даёт листать глубоко, поэтому интервал делится пополам, пока в нём
меньше 500 записей. Все типы событий (TRADE, REDEEM, MERGE, SPLIT, REWARD, CONVERSION, ...).
Выход:
  STORE/act_<кошелёк>.csv.gz      все записи (на сервере, в git не идут)
  DIR/hist_windows.csv.gz          по рынкам (окнам): покупки/продажи по исходам, выплаты, слияния, денежный итог
  DIR/hist_days.csv                по дням: оборот, окон, сделок, денежный итог, награды; типы событий
"""
from __future__ import annotations

import argparse
import os
import time

import pandas as pd
import requests

API = "https://data-api.polymarket.com/activity"
S = requests.Session()
S.headers["User-Agent"] = "Mozilla/5.0"
KEEP = ["timestamp", "type", "conditionId", "slug", "outcome", "outcomeIndex", "side", "price", "size", "usdcSize",
        "transactionHash", "asset"]


def get(params, tries=7):
    back = 1.0
    for _ in range(tries):
        try:
            r = S.get(API, params=params, timeout=30)
        except Exception:
            time.sleep(back); back = min(back * 2, 30); continue
        if r.status_code == 429 or r.status_code >= 500:
            time.sleep(back); back = min(back * 2, 30); continue
        if r.status_code != 200:
            raise RuntimeError(f"http {r.status_code}: {r.text[:200]}")
        return r.json()
    raise RuntimeError("нет ответа")


def fetch(user, t0, t1, out, stats):
    """Записи за [t0, t1] (секунды), рекурсивно делит интервал."""
    js = get({"user": user, "limit": 500, "offset": 0, "start": t0, "end": t1, "sortBy": "TIMESTAMP",
              "sortDirection": "ASC"})
    stats["req"] += 1
    if len(js) < 500:
        out.extend(js)
        return
    if t1 - t0 <= 1:                          # больше 500 событий в одну секунду: листаем offset
        off = 500
        out.extend(js)
        while True:
            more = get({"user": user, "limit": 500, "offset": off, "start": t0, "end": t1, "sortBy": "TIMESTAMP",
                        "sortDirection": "ASC"})
            stats["req"] += 1
            out.extend(more)
            if len(more) < 500:
                return
            off += 500
    mid = (t0 + t1) // 2
    fetch(user, t0, mid, out, stats)
    fetch(user, mid + 1, t1, out, stats)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("user")
    ap.add_argument("--out", required=True)
    ap.add_argument("--store", default=os.path.expanduser("~/wallets"))
    ap.add_argument("--since", default="2025-06-01")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    os.makedirs(a.store, exist_ok=True)
    user = a.user.lower()
    t_start = int(pd.Timestamp(a.since, tz="UTC").timestamp())
    first = get({"user": user, "limit": 1, "start": t_start, "sortBy": "TIMESTAMP", "sortDirection": "ASC"})
    if not first:
        print("нет записей"); return
    t0 = int(first[0]["timestamp"])
    t_end = int(time.time())
    print(f"первая запись {pd.Timestamp(t0, unit='s')}", flush=True)
    rows, stats, T = [], {"req": 0}, time.time()
    day = 86400
    fn = os.path.join(a.store, f"act_{user[:10]}.csv.gz")
    days = list(range(t0 - t0 % day, t_end + 1, day))

    def one(d):
        buf = []
        fetch(user, d, min(d + day - 1, t_end), buf, stats)
        return pd.DataFrame([{k: x.get(k) for k in KEEP} for x in buf]) if buf else None

    parts = []
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(3) as ex:
        for i, p in enumerate(ex.map(one, days)):
            if p is not None:
                parts.append(p)
            if (i + 1) % 10 == 0:
                print(f"  дней {i + 1}/{len(days)}: записей {sum(len(x) for x in parts)}, запросов {stats['req']}, "
                      f"{time.time() - T:.0f} с", flush=True)
    A = pd.concat(parts, ignore_index=True).drop_duplicates()
    A.to_csv(fn, index=False)
    print(f"всего записей {len(A)}, запросов {stats['req']}, {time.time() - T:.0f} с; типы: "
          f"{A.type.value_counts().to_dict()}", flush=True)
    A["day"] = pd.to_datetime(A.timestamp, unit="s").dt.strftime("%Y-%m-%d")
    A["usdc"] = pd.to_numeric(A.usdcSize, errors="coerce").fillna(0)
    A["size"] = pd.to_numeric(A["size"], errors="coerce").fillna(0)
    sgn = {"BUY": -1, "SELL": 1}
    A["cash"] = 0.0
    tr = A.type == "TRADE"
    A.loc[tr, "cash"] = A.loc[tr, "side"].map(sgn).fillna(0) * A.loc[tr, "usdc"]
    for t in ("REDEEM", "MERGE", "REWARD", "CONVERSION", "MAKER_REBATE"):
        A.loc[A.type == t, "cash"] = A.loc[A.type == t, "usdc"]
    A.loc[A.type == "SPLIT", "cash"] = -A.loc[A.type == "SPLIT", "usdc"]
    # по окнам
    t = A[A.slug.notna() & (A.slug.astype(str) != "")]
    g = t.groupby("slug")
    W = pd.DataFrame({
        "t_first": g.timestamp.min(), "t_last": g.timestamp.max(), "cash": g.cash.sum(),
        "n_trades": g.apply(lambda x: (x.type == "TRADE").sum()),
        "buy_usd": g.apply(lambda x: x.usdc[(x.type == "TRADE") & (x.side == "BUY")].sum()),
        "sell_usd": g.apply(lambda x: x.usdc[(x.type == "TRADE") & (x.side == "SELL")].sum()),
        "up_sh": g.apply(lambda x: x["size"][(x.type == "TRADE") & (x.side == "BUY") & (x.outcome == "Up")].sum()),
        "dn_sh": g.apply(lambda x: x["size"][(x.type == "TRADE") & (x.side == "BUY") & (x.outcome == "Down")].sum()),
        "up_usd": g.apply(lambda x: x.usdc[(x.type == "TRADE") & (x.side == "BUY") & (x.outcome == "Up")].sum()),
        "dn_usd": g.apply(lambda x: x.usdc[(x.type == "TRADE") & (x.side == "BUY") & (x.outcome == "Down")].sum()),
        "redeem": g.apply(lambda x: x.usdc[x.type == "REDEEM"].sum()),
        "merge": g.apply(lambda x: x.usdc[x.type == "MERGE"].sum()),
    }).reset_index()
    W.round(4).to_csv(os.path.join(a.out, "hist_windows.csv.gz"), index=False)
    D = A.groupby("day").agg(n=("type", "size"), cash=("cash", "sum"),
                             trades=("type", lambda v: (v == "TRADE").sum()),
                             buy_usd=("usdc", lambda v: v[(A.loc[v.index, "type"] == "TRADE") & (A.loc[v.index, "side"] == "BUY")].sum()),
                             reward=("usdc", lambda v: v[A.loc[v.index, "type"].isin(["REWARD", "MAKER_REBATE"])].sum()),
                             windows=("slug", "nunique"))
    D.round(2).to_csv(os.path.join(a.out, "hist_days.csv"))
    print(D.tail(40).round(1).to_string())
    print("рынки (первые слова slug):", t.slug.astype(str).str.extract(r"^([a-z]+-[a-z]+-[0-9a-z]+)")[0].value_counts().head(10).to_dict())


if __name__ == "__main__":
    main()
