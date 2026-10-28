"""Лента сделок Polymarket с кошельками (data-api /trades) по окнам записи сборщика.

    python tape_fetch.py DATA_DIR/2026-10-28 --out DIR [--wfrom W --wto W] [--first N] [--modes false] [--probe]

Окна и condition_id берутся из потока windows сборщика. По каждому окну - все сделки рынка постранично.
Выход: DIR/tape_<день>.csv.gz (w, mode, ts, wallet, side, outcome, oi, price, size, tx, name) и
DIR/tape_<день>_windows.csv (окно, исход, число сделок, сколько страниц, ошибки).
--probe: дополнительно печатает все поля первой записи, проверяет limit 1000 и большие offset, выгружает pm_trades
с хэшем транзакции для этих окон (сверка семантики).
"""
from __future__ import annotations

import argparse
import json
import os
import time

import pandas as pd
import requests

from lead_lag import read

API = "https://data-api.polymarket.com/trades"
KEEP = ["timestamp", "proxyWallet", "side", "outcome", "outcomeIndex", "price", "size", "transactionHash", "name",
        "pseudonym", "asset"]
S = requests.Session()
S.headers["User-Agent"] = "Mozilla/5.0"


def get(params, tries=6):
    back = 1.0
    for _ in range(tries):
        try:
            r = S.get(API, params=params, timeout=20)
        except Exception as ex:          # сеть
            err = repr(ex)
            time.sleep(back); back *= 2
            continue
        if r.status_code == 429 or r.status_code >= 500:
            err = f"http {r.status_code}"
            time.sleep(back); back *= 2
            continue
        if r.status_code != 200:
            return None, f"http {r.status_code}: {r.text[:200]}"
        return r.json(), ""
    return None, err


def fetch_market(cond: str, taker_only: str, limit=500, max_pages=60, pause=0.12):
    rows, err, pages = [], "", 0
    for p in range(max_pages):
        js, err = get({"market": cond, "limit": limit, "offset": p * limit, "takerOnly": taker_only})
        pages += 1
        if js is None:
            break
        rows.extend(js)
        if len(js) < limit:
            break
        time.sleep(pause)
    return rows, pages, err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--out", required=True)
    ap.add_argument("--wfrom", type=int, default=0)
    ap.add_argument("--wto", type=int, default=10 ** 12)
    ap.add_argument("--first", type=int, default=0, help="только первые N окон")
    ap.add_argument("--modes", default="false", help="takerOnly: false, true или false,true")
    ap.add_argument("--probe", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    day = os.path.basename(os.path.normpath(a.root))
    ws = read(a.root, "windows")
    ws = ws.drop_duplicates("slug", keep="last")
    ws = ws[(ws.start >= a.wfrom) & (ws.start < a.wto) & ws.condition_id.notna()].sort_values("start")
    if a.first:
        ws = ws.head(a.first)
    print(f"{day}: окон {len(ws)}", flush=True)
    out_rows, meta = [], []
    t0 = time.time()
    for i, r in enumerate(ws.itertuples()):
        for mode in a.modes.split(","):
            rows, pages, err = fetch_market(r.condition_id, mode)
            if a.probe and rows and i == 0:
                print(f"\nполя записи (takerOnly={mode}):", json.dumps({k: (v if len(str(v)) < 90 else str(v)[:90])
                                                                        for k, v in rows[0].items()}, ensure_ascii=False))
            for x in rows:
                out_rows.append([int(r.start), mode] + [x.get(k) for k in KEEP])
            meta.append(dict(w=int(r.start), slug=r.slug, cond=r.condition_id, winner=r.official_winner, mode=mode,
                             n=len(rows), pages=pages, err=err,
                             ts_min=min((x.get("timestamp", 0) for x in rows), default=None),
                             ts_max=max((x.get("timestamp", 0) for x in rows), default=None)))
        if (i + 1) % 50 == 0:
            print(f"  {i + 1} окон, {len(out_rows)} записей, {time.time() - t0:.0f} с", flush=True)
    tape = pd.DataFrame(out_rows, columns=["w", "mode", "ts", "wallet", "side", "outcome", "oi", "price", "size", "tx",
                                           "name", "pseudonym", "asset"])
    if not a.probe:
        tape = tape.drop(columns=["pseudonym", "asset"])
    tape.to_csv(os.path.join(a.out, f"tape_{day}.csv.gz"), index=False)
    pd.DataFrame(meta).to_csv(os.path.join(a.out, f"tape_{day}_windows.csv"), index=False)
    print(f"{day}: записей {len(tape)}, окон {len(ws)}, {time.time() - t0:.0f} с; ошибок "
          f"{sum(1 for m in meta if m['err'])}", flush=True)
    if a.probe and len(ws):
        c = ws.iloc[0].condition_id
        for lim, off in ((1000, 0), (500, 3000), (500, 10000), (500, 20000)):
            js, err = get({"market": c, "limit": lim, "offset": off, "takerOnly": "false"})
            print(f"проверка limit={lim} offset={off}: {'ошибка ' + err if js is None else f'{len(js)} записей'}")
        tr = read(a.root, "pm_trades")
        tr = tr[tr.w.isin(ws.start.astype(int))]
        tr.to_csv(os.path.join(a.out, f"pmtr_{day}.csv.gz"), index=False)
        print(f"pm_trades этих окон: {len(tr)} строк")
        ws.to_csv(os.path.join(a.out, f"win_{day}.csv"), index=False)


if __name__ == "__main__":
    main()
