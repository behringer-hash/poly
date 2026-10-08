"""Что можно получить из истории задним числом? Проверка источников с сервера (в песочнице Claude они закрыты).

Пишет history_probe.md в $OUT_DIR. Только GET/HEAD к публичным адресам, ничего не скачивает целиком.
"""
from __future__ import annotations

import json
import os
import time
from datetime import datetime, timedelta, timezone

import requests

OUT = os.environ.get("OUT_DIR", ".")
S = requests.Session()
S.headers["User-Agent"] = "btc5m-lab-probe/1.0"
L: list[str] = ["# Проверка доступной истории\n", f"UTC: {datetime.now(timezone.utc):%Y-%m-%d %H:%M:%S}\n"]


def get(url, **kw):
    try:
        return S.get(url, timeout=20, **kw)
    except Exception as e:  # noqa: BLE001
        L.append(f"- ОШИБКА {url}: {e}")
        return None


def head(url):
    try:
        r = S.head(url, timeout=20, allow_redirects=True)
        return r.status_code, r.headers.get("Content-Length")
    except Exception as e:  # noqa: BLE001
        return f"ошибка {e}", None


def snippet(x, n=500):
    s = x if isinstance(x, str) else json.dumps(x, ensure_ascii=False)
    return s[:n] + ("…" if len(s) > n else "")


# ---------- 1. Дампы бирж (скачать можно за любой день)
L.append("## Дампы бирж по дням (HEAD: код ответа и размер файла)")
days = [(datetime.now(timezone.utc) - timedelta(days=d)).strftime("%Y-%m-%d") for d in (2, 7, 30, 90)]
L.append("| источник | " + " | ".join(days) + " |\n|---|" + "---|" * len(days))
BV = "https://data.binance.vision/data"
paths = {
    "Binance futures aggTrades": lambda d: f"{BV}/futures/um/daily/aggTrades/BTCUSDT/BTCUSDT-aggTrades-{d}.zip",
    "Binance futures bookTicker": lambda d: f"{BV}/futures/um/daily/bookTicker/BTCUSDT/BTCUSDT-bookTicker-{d}.zip",
    "Binance futures bookDepth": lambda d: f"{BV}/futures/um/daily/bookDepth/BTCUSDT/BTCUSDT-bookDepth-{d}.zip",
    "Binance spot aggTrades": lambda d: f"{BV}/spot/daily/aggTrades/BTCUSDT/BTCUSDT-aggTrades-{d}.zip",
    "Binance spot trades": lambda d: f"{BV}/spot/daily/trades/BTCUSDT/BTCUSDT-trades-{d}.zip",
    "Bybit trades": lambda d: f"https://public.bybit.com/trading/BTCUSDT/BTCUSDT{d}.csv.gz",
}
for name, f in paths.items():
    cells = []
    for d in days:
        code, size = head(f(d))
        cells.append(f"{code}, {int(size) / 1e6:.0f} МБ" if size and str(size).isdigit() else str(code))
    L.append(f"| {name} | " + " | ".join(cells) + " |")

# ---------- 2. Polymarket: старые рынки BTC 5m
L.append("\n## Polymarket: исторические данные по рынкам BTC 5m")
now = int(time.time())
for label, back in (("1 час назад", 3600), ("1 сутки назад", 86400), ("7 суток назад", 7 * 86400), ("30 суток назад", 30 * 86400)):
    start = (now - back) // 300 * 300
    slug = f"btc-updown-5m-{start}"
    L.append(f"\n### {label}: {slug}")
    r = get("https://gamma-api.polymarket.com/events", params={"slug": slug})   # так же ищет рынки lab-collector
    if r is None or r.status_code != 200:
        L.append(f"- gamma: {None if r is None else r.status_code}")
        continue
    ev = r.json()
    if not ev or not ev[0].get("markets"):
        L.append("- gamma: событие не найдено")
        continue
    m = ev[0]["markets"][0]
    cond = m.get("conditionId")
    tokens = m.get("clobTokenIds")
    tokens = json.loads(tokens) if isinstance(tokens, str) else tokens
    L.append(f"- gamma: найден, closed={m.get('closed')}, volume={m.get('volume')}, conditionId={str(cond)[:14]}…")
    r = get("https://data-api.polymarket.com/trades", params={"market": cond, "limit": 500, "takerOnly": "false"})
    if r is not None and r.status_code == 200:
        tr = r.json()
        ts = [t.get("timestamp") for t in tr if isinstance(t, dict)]
        L.append(f"- data-api trades: {len(tr)} сделок за один запрос; поля: {sorted(tr[0].keys()) if tr else '—'}; "
                 f"timestamp {min(ts) if ts else '—'}…{max(ts) if ts else '—'} (разрешение — секунды)")
    else:
        L.append(f"- data-api trades: {None if r is None else r.status_code} {snippet(r.text, 200) if r is not None else ''}")
    if tokens:
        r = get("https://clob.polymarket.com/prices-history",
                params={"market": tokens[0], "startTs": start, "endTs": start + 300, "fidelity": 1})
        if r is not None and r.status_code == 200:
            h = r.json().get("history", [])
            L.append(f"- prices-history (fidelity=1): {len(h)} точек за 5 минут; пример: {snippet(h[:3], 200)}")
        else:
            L.append(f"- prices-history: {None if r is None else r.status_code}")
        r = get("https://clob.polymarket.com/book", params={"token_id": tokens[0]})
        L.append(f"- clob /book (стакан сейчас): {None if r is None else r.status_code} "
                 f"{'' if r is None else snippet(r.text, 160)}")

L.append("\n## Вывод для чтения человеком\n- Если дампы Binance/Bybit доступны, историю цен BTC можно получить за любой день.\n"
         "- Если у Polymarket доступны только сделки (секунды) и prices-history (минимум 1 минута), то стакан с точностью "
         "до миллисекунд задним числом получить нельзя — его надо записывать (это делает lab-collector).")
txt = "\n".join(L) + "\n"
with open(os.path.join(OUT, "history_probe.md"), "w", encoding="utf-8") as fh:
    fh.write(txt)
print(txt)
