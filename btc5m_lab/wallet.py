"""Процесс 3: действия отслеживаемого кошелька через data-api Polymarket.

Пишем ВСЕ типы событий (TRADE, REDEEM, MERGE, SPLIT, CONVERSION), а не только
TRADE/REDEEM: если кошелёк сливает пары Up+Down через MERGE, без этого его PnL
считается неверно. Точное время исполнения каждой сделки потом берём из
pm_trades по transaction_hash (серверное время Polymarket в мс).
"""
from __future__ import annotations

import time

import requests

from common import DataWriter, clock, flush_console, log

SCHEMAS = {
    "wallet": ["detected", "seeded", "ts", "type", "slug", "outcome", "side", "price", "size", "usdc_size",
               "tx_hash", "asset", "condition_id"],
}
TYPES = "TRADE,REDEEM,MERGE,SPLIT,CONVERSION"


def key(t: dict):
    return (t.get("transactionHash"), t.get("asset"), t.get("type"), t.get("side"),
            t.get("price"), t.get("size"), t.get("timestamp"))


def fetch(cfg, limit=200):
    r = requests.get(f"{cfg.data_api}/activity",
                     params={"user": cfg.wallet, "limit": limit, "offset": 0, "type": TYPES,
                             "sortBy": "TIMESTAMP", "sortDirection": "DESC"},
                     headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    if r.status_code == 429:
        raise RuntimeError("429")
    r.raise_for_status()
    return r.json()


def run(cfg):
    w = DataWriter(cfg.data_dir, SCHEMAS, "wallet")
    known: set = set()
    seeded = False
    backoff = cfg.wallet_poll_sec
    n_new = 0
    last_status = time.time()
    log("wallet", f"слежу за {cfg.wallet}")
    try:
        while True:
            try:
                batch = fetch(cfg)
                backoff = cfg.wallet_poll_sec
            except Exception as ex:
                backoff = min(30.0, backoff * 2)
                log("wallet", f"ошибка запроса ({ex}); пауза {backoff:.0f} с")
                time.sleep(backoff)
                continue
            det = clock.now()
            new = [t for t in batch if key(t) not in known]
            new.sort(key=lambda t: t.get("timestamp", 0))
            for t in new:
                known.add(key(t))
                w.write("wallet", (det, int(not seeded), t.get("timestamp"), t.get("type"), t.get("slug"),
                                   t.get("outcome"), t.get("side"), t.get("price"), t.get("size"),
                                   t.get("usdcSize"), t.get("transactionHash"), t.get("asset"),
                                   t.get("conditionId")))
            if seeded and len(new) >= 190:
                log("wallet", "за один опрос пришло почти 200 событий - часть могла потеряться")
            if seeded:
                n_new += len(new)
            seeded = True
            if time.time() - last_status > 60:
                log("wallet", f"новых событий за минуту: {n_new}")
                n_new = 0
                last_status = time.time()
            time.sleep(backoff)
    except KeyboardInterrupt:
        pass
    finally:
        w.close()
        flush_console()
