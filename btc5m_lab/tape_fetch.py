"""Лента сделок Polymarket с кошельками (data-api /trades) по окнам записи сборщика.

    python tape_fetch.py DATA_DIR/2026-10-28 --out DIR [--wfrom W --wto W] [--first N] [--modes false,true]
                         [--limit 1000] [--threads 3] [--probe]

Окна и condition_id - из потока windows сборщика; окна, которые закончились меньше 3 минут назад, пропускаются.
Каждое окно - все сделки рынка постранично (offset не больше 10 000 - ограничение API).
takerOnly=false - все записи (тейкер + мейкеры, по одной на кошелёк и уровень), takerOnly=true - только тейкеры.
Выход (пишется по мере загрузки, память не растёт):
  DIR/tape_<день>.csv.gz        w, mode, ts, wallet, side, outcome, oi, price, size, tx
  DIR/tape_<день>_windows.csv   окно, исход, число записей, страниц, ошибки
--probe: печатает поля первой записи, проверяет limit/offset, выгружает pm_trades этих окон.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor

import pandas as pd
import requests

from lead_lag import read

API = "https://data-api.polymarket.com/trades"
KEEP = ["timestamp", "proxyWallet", "side", "outcome", "outcomeIndex", "price", "size", "transactionHash"]
COLS = ["w", "mode", "ts", "wallet", "side", "outcome", "oi", "price", "size", "tx"]
_tl = threading.local()


def sess():
    if not hasattr(_tl, "s"):
        _tl.s = requests.Session()
        _tl.s.headers["User-Agent"] = "Mozilla/5.0"
    return _tl.s


def get(params, tries=7):
    back, err = 1.0, ""
    for _ in range(tries):
        try:
            r = sess().get(API, params=params, timeout=25)
        except Exception as ex:          # сеть
            err = repr(ex)[:120]
            time.sleep(back); back = min(back * 2, 30)
            continue
        if r.status_code == 429 or r.status_code >= 500:
            err = f"http {r.status_code}"
            time.sleep(back); back = min(back * 2, 30)
            continue
        if r.status_code != 200:
            return None, f"http {r.status_code}: {r.text[:160]}"
        return r.json(), ""
    return None, err


def fetch_market(cond: str, taker_only: str, limit=1000, pause=0.05):
    rows, err, pages, trunc = [], "", 0, False
    off = 0
    while True:
        js, err = get({"market": cond, "limit": limit, "offset": off, "takerOnly": taker_only})
        pages += 1
        if js is None:
            break
        rows.extend(js)
        if len(js) < limit:
            break
        off += limit
        if off > 10000:
            trunc = True
            break
        time.sleep(pause)
    return rows, pages, err, trunc


def one_window(r, modes, limit):
    recs, meta = [], []
    for mode in modes:
        rows, pages, err, trunc = fetch_market(r.condition_id, mode, limit)
        for x in rows:
            recs.append([int(r.start), mode] + [x.get(k) for k in KEEP])
        meta.append(dict(w=int(r.start), slug=r.slug, cond=r.condition_id, winner=r.official_winner, mode=mode,
                         n=len(rows), pages=pages, err=err, truncated=trunc,
                         ts_min=min((x.get("timestamp", 0) for x in rows), default=None),
                         ts_max=max((x.get("timestamp", 0) for x in rows), default=None)))
    return recs, meta, (rows[0] if rows else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--out", required=True)
    ap.add_argument("--wfrom", type=int, default=0)
    ap.add_argument("--wto", type=int, default=10 ** 12)
    ap.add_argument("--first", type=int, default=0, help="только первые N окон")
    ap.add_argument("--modes", default="false,true", help="takerOnly: false, true или false,true")
    ap.add_argument("--limit", type=int, default=1000)
    ap.add_argument("--threads", type=int, default=3)
    ap.add_argument("--probe", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    day = os.path.basename(os.path.normpath(a.root))
    ws = read(a.root, "windows")
    if ws.empty:
        print(f"{day}: нет потока windows"); return
    ws = ws.drop_duplicates("slug", keep="last")
    ws = ws[(ws.start >= a.wfrom) & (ws.start < min(a.wto, time.time() - 480)) & ws.condition_id.notna()]
    ws = ws.sort_values("start")
    if a.first:
        ws = ws.head(a.first)
    print(f"{day}: окон {len(ws)}", flush=True)
    modes = a.modes.split(",")
    fn = os.path.join(a.out, f"tape_{day}.csv.gz")
    metas, n_rec, t0 = [], 0, time.time()
    with gzip.open(fn, "wt", encoding="utf-8") as fh:
        fh.write(",".join(COLS) + "\n")
        with ThreadPoolExecutor(a.threads) as ex:
            futs = [ex.submit(one_window, r, modes, a.limit) for r in ws.itertuples()]
            for i, f in enumerate(futs):
                recs, meta, first = f.result()
                if a.probe and i == 0 and first:
                    print("поля записи:", json.dumps({k: (v if len(str(v)) < 90 else str(v)[:90])
                                                      for k, v in first.items()}, ensure_ascii=False))
                if recs:
                    pd.DataFrame(recs, columns=COLS).to_csv(fh, header=False, index=False)
                n_rec += len(recs)
                metas.extend(meta)
                if (i + 1) % 50 == 0:
                    print(f"  {i + 1} окон, {n_rec} записей, {time.time() - t0:.0f} с", flush=True)
    m = pd.DataFrame(metas)
    m.to_csv(os.path.join(a.out, f"tape_{day}_windows.csv"), index=False)
    print(f"{day}: записей {n_rec}, окон {len(ws)}, {time.time() - t0:.0f} с; ошибок {int((m.err.astype(str) != '').sum())}, "
          f"обрезано по offset {int(m.truncated.sum())}, файл {os.path.getsize(fn) / 1e6:.1f} МБ", flush=True)
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
