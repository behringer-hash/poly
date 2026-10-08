"""Диагностика канала до Binance: какие адрес/порт/набор потоков работают у вас без задержек.

    python bn_diag.py

Около 3 минут. По очереди подключается к разным адресам Binance и по 25 секунд
меряет: сколько сообщений приходит, задержку биржа -> вы (по времени сделок) и паузы.
В конце печатает таблицу. Пришлите её целиком.
"""
from __future__ import annotations

import asyncio
import sys
import time

import requests
import websockets

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from common import clock, loads, probe_clock  # noqa: E402

TESTS = [
    ("stream.binance.com:9443  aggTrade", "wss://stream.binance.com:9443", "btcusdt@aggTrade"),
    ("stream.binance.com:443   aggTrade", "wss://stream.binance.com:443", "btcusdt@aggTrade"),
    ("data-stream.vision       aggTrade", "wss://data-stream.binance.vision", "btcusdt@aggTrade"),
    ("stream.binance.com:9443  agg+bookTicker", "wss://stream.binance.com:9443", "btcusdt@aggTrade/btcusdt@bookTicker"),
    ("stream.binance.com:443   agg+bookTicker", "wss://stream.binance.com:443", "btcusdt@aggTrade/btcusdt@bookTicker"),
    ("data-stream.vision       agg+bookTicker", "wss://data-stream.binance.vision", "btcusdt@aggTrade/btcusdt@bookTicker"),
    ("stream.binance.com:443   agg+depth5@100ms", "wss://stream.binance.com:443", "btcusdt@aggTrade/btcusdt@depth5@100ms"),
    ("data-stream.vision       agg+depth5@100ms", "wss://data-stream.binance.vision", "btcusdt@aggTrade/btcusdt@depth5@100ms"),
]
DUR = 25.0


def pct(xs, p):
    if not xs:
        return None
    s = sorted(xs)
    return s[min(len(s) - 1, int(p * len(s)))]


async def one(name, base, streams, offset_ms):
    url = f"{base}/stream?streams={streams}"
    n_agg = n_other = 0
    lat, gaps = [], []
    t_conn = None
    err = ""
    try:
        t0 = time.perf_counter()
        async with websockets.connect(url, open_timeout=10, ping_interval=10, ping_timeout=10,
                                      max_queue=None, compression=None) as ws:
            t_conn = (time.perf_counter() - t0) * 1000
            end = time.perf_counter() + DUR
            last = time.perf_counter()
            while time.perf_counter() < end:
                try:
                    raw = await asyncio.wait_for(ws.recv(), timeout=max(0.1, end - time.perf_counter()))
                except asyncio.TimeoutError:
                    break
                now_p = time.perf_counter()
                gaps.append(now_p - last)
                last = now_p
                recv = clock.now()
                x = loads(raw)
                x = x.get("data") or x
                if x.get("e") == "aggTrade":
                    n_agg += 1
                    lat.append(recv * 1000 + offset_ms - x["E"])
                else:
                    n_other += 1
    except Exception as ex:
        err = repr(ex)[:80]
    return dict(name=name, conn_ms=t_conn, agg_s=n_agg / DUR, other_s=n_other / DUR,
                lat50=pct(lat, .5), lat90=pct(lat, .9), latmax=max(lat) if lat else None,
                maxgap=max(gaps) if gaps else None, err=err)


def f(x, fmt="7.0f"):
    return format(x, fmt) if x is not None else "    n/a"


async def main():
    print("Замер смещения часов...", flush=True)
    try:
        src, off, rtt = probe_clock("https://api.binance.com")
        print(f"  источник {src}: смещение {off:+.1f} мс, RTT {rtt:.0f} мс", flush=True)
    except Exception as ex:
        off = 0.0
        print(f"  не удалось ({ex}); задержки будут без поправки на часы", flush=True)
    for host in ("https://api.binance.com/api/v3/ping", "https://api.exchange.coinbase.com/time"):
        try:
            ts = []
            for _ in range(3):
                t0 = time.perf_counter()
                requests.get(host, timeout=5)
                ts.append((time.perf_counter() - t0) * 1000)
            print(f"  HTTPS {host.split('/')[2]}: {min(ts):.0f} мс (лучший из 3)", flush=True)
        except Exception as ex:
            print(f"  HTTPS {host.split('/')[2]}: ошибка {ex!r}"[:120], flush=True)

    rows = []
    for name, base, streams in TESTS:
        print(f"Тест: {name} ...", flush=True)
        rows.append(await one(name, base, streams, off))
    print("\nтест                                     подкл.мс  сделок/с  прочих/с  задержка p50   p90    max   макс.пауза,с  ошибка")
    for r in rows:
        print(f"{r['name']:40s} {f(r['conn_ms'])}  {f(r['agg_s'], '8.1f')}  {f(r['other_s'], '8.1f')}  "
              f"{f(r['lat50'])}  {f(r['lat90'])}  {f(r['latmax'])}  {f(r['maxgap'], '10.1f')}    {r['err']}")
    print("\nНорма: задержка p50 в пределах 30-150 мс, max без секундных выбросов, пауза < 1-2 с.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
