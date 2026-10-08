"""Замер задержек для выбора сервера (VPS) под бота. Один файл, запускается где угодно.

    pip install websockets requests numpy
    python latency_probe.py                 # 10 минут
    python latency_probe.py --minutes 5

Что меряет:
  * разрешена ли торговля с этого IP (официальная проверка Polymarket /api/geoblock);
  * время запросов к серверу ордеров Polymarket (постоянное соединение, как у бота);
  * задержку книги и сделок Polymarket (время сервера -> этот компьютер);
  * задержку BTC с бирж: спот и фьючерс Binance, Bybit, Coinbase, OKX (время биржи -> этот компьютер);
  * кто из бирж ведёт цену и когда сигнал с каждой биржи реально доходит сюда
    относительно момента тика на фьючерсе Binance.

В конце печатает сводку и сохраняет её в probe_<имя>_<время>.json - пришлите этот файл.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import platform
import socket
import ssl
import time
from datetime import datetime, timezone

import requests
import websockets

try:
    import numpy as np
except ImportError:  # pragma: no cover
    np = None

H = {"User-Agent": "Mozilla/5.0"}


def now_ms() -> float:
    return time.time_ns() / 1e6


def q(xs, p):
    if not xs:
        return None
    s = sorted(xs)
    return round(s[min(len(s) - 1, int(p * len(s)))], 1)


# ---------------------------------------------------------------- часы
def clock_offset():
    """(серверное время - локальное) в мс, лучший из 7 замеров по Binance, запасной - Coinbase."""
    for url, parse in (("https://api.binance.com/api/v3/time", lambda j: float(j["serverTime"])),
                       ("https://api.exchange.coinbase.com/time", lambda j: float(j["epoch"]) * 1000)):
        best = None
        try:
            for _ in range(7):
                t0 = now_ms()
                j = requests.get(url, headers=H, timeout=5).json()
                t1 = now_ms()
                off, rtt = parse(j) - (t0 + t1) / 2, t1 - t0
                if best is None or rtt < best[1]:
                    best = (off, rtt)
            return url.split("/")[2], round(best[0], 1), round(best[1], 1)
        except Exception:
            continue
    return None, 0.0, None


# ---------------------------------------------------------------- REST и TCP
def geoblock():
    try:
        return requests.get("https://polymarket.com/api/geoblock", headers=H, timeout=10).json()
    except Exception as ex:
        return {"error": repr(ex)}


def tcp_tls(host, port=443):
    try:
        ip = socket.getaddrinfo(host, port, socket.AF_INET)[0][4][0]
        best_t = best_s = None
        for _ in range(3):
            t0 = time.perf_counter()
            s = socket.create_connection((ip, port), timeout=10)
            t1 = time.perf_counter()
            ss = ssl.create_default_context().wrap_socket(s, server_hostname=host)
            t2 = time.perf_counter()
            ss.close()
            best_t = min(best_t or 1e9, (t1 - t0) * 1000)
            best_s = min(best_s or 1e9, (t2 - t1) * 1000)
        return {"ip": ip, "tcp_ms": round(best_t, 1), "tls_ms": round(best_s, 1)}
    except Exception as ex:
        return {"error": repr(ex)[:100]}


def clob_rest(n=40):
    """Время запросов к CLOB по постоянному соединению. POST /order без ключей сервер отклоняет
    (401), но запрос проходит тот же путь, что и настоящий ордер; 403 - регион закрыт."""
    s = requests.Session()
    s.headers.update(H)
    res = {"GET /time": [], "POST /order": []}
    status = {}
    s.get("https://clob.polymarket.com/time", timeout=5)  # прогрев соединения
    for i in range(n):
        t0 = time.perf_counter()
        s.get("https://clob.polymarket.com/time", timeout=5)
        res["GET /time"].append((time.perf_counter() - t0) * 1000)
        if i % 2 == 0:
            t0 = time.perf_counter()
            r = s.post("https://clob.polymarket.com/order", json={}, timeout=5)
            res["POST /order"].append((time.perf_counter() - t0) * 1000)
            status[r.status_code] = status.get(r.status_code, 0) + 1
        time.sleep(0.25)
    return {k: {"p50": q(v, .5), "p90": q(v, .9), "min": round(min(v), 1)} for k, v in res.items()} | \
        {"order_status": status}


# ---------------------------------------------------------------- потоки
class Feed:
    def __init__(self, name):
        self.name = name
        self.lat = []          # задержка сообщения, мс
        self.ticks = []        # (время биржи мс, цена) - для анализа, кто ведёт
        self.errors = 0
        self.url = None


async def run_feed(feed: Feed, urls, sub, parse, stop_at, off, ping=None):
    i = 0
    while time.time() < stop_at:
        url = urls[i % len(urls)]
        got = 0
        try:
            async with websockets.connect(url, open_timeout=10, ping_interval=None, max_queue=None,
                                          compression=None) as ws:
                if sub:
                    await ws.send(sub)
                feed.url = url
                last_ping = time.time()
                while time.time() < stop_at:
                    try:
                        raw = await asyncio.wait_for(ws.recv(), timeout=5)
                    except asyncio.TimeoutError:
                        raw = None
                    if ping and time.time() - last_ping > 15:
                        await ws.send(ping)
                        last_ping = time.time()
                    if not raw or raw in ("pong", "PONG"):
                        continue
                    recv = now_ms()
                    try:
                        d = json.loads(raw)
                    except Exception:
                        continue
                    for ets, px in parse(d):
                        got += 1
                        feed.lat.append(recv + off - ets)
                        if px is not None:
                            feed.ticks.append((ets, px))
        except Exception:
            feed.errors += 1
        if got == 0:
            i += 1
        await asyncio.sleep(1)


def p_bn(d):
    x = d.get("data") or d
    return [(x["T"], float(x["p"]))] if x.get("e") == "aggTrade" else []


def p_by(d):
    if not str(d.get("topic", "")).startswith("publicTrade"):
        return []
    return [(it["T"], float(it["p"])) for it in d.get("data") or []]


def p_cb(d):
    if d.get("type") != "ticker":
        return []
    t = datetime.fromisoformat(d["time"].replace("Z", "+00:00")).timestamp() * 1000
    return [(t, float(d["price"]))]


def p_ok(d):
    if (d.get("arg") or {}).get("channel") != "trades":
        return []
    return [(int(it["ts"]), float(it["px"])) for it in d.get("data") or []]


async def clob_feed(feed_book: Feed, feed_trades: Feed, stop_at, off):
    while time.time() < stop_at:
        try:
            st = int(time.time() // 300 * 300)
            m = requests.get("https://gamma-api.polymarket.com/events", params={"slug": f"btc-updown-5m-{st}"},
                             headers=H, timeout=10).json()[0]["markets"][0]
            toks = json.loads(m["clobTokenIds"])
            end = min(stop_at, st + 300)
            async with websockets.connect("wss://ws-subscriptions-clob.polymarket.com/ws/market", ping_interval=10,
                                          max_queue=None, compression=None, max_size=2**23) as ws:
                await ws.send(json.dumps({"type": "market", "assets_ids": toks}))
                feed_book.url = "clob market ws"
                while time.time() < end:
                    try:
                        raw = await asyncio.wait_for(ws.recv(), timeout=5)
                    except asyncio.TimeoutError:
                        continue
                    recv = now_ms()
                    try:
                        d = json.loads(raw)
                    except Exception:
                        continue
                    for e in (d if isinstance(d, list) else [d]):
                        ts = e.get("timestamp")
                        if not ts:
                            continue
                        lag = recv + off - int(ts)
                        (feed_trades if e.get("event_type") == "last_trade_price" else feed_book).lat.append(lag)
        except Exception:
            feed_book.errors += 1
            await asyncio.sleep(2)


# ---------------------------------------------------------------- кто ведёт
def lead_vs(ref: Feed, other: Feed, step=50):
    """Сдвиг (мс), при котором доходности other сильнее всего коррелируют с доходностями ref.
    >0 - other отстаёт от ref. Считается по времени бирж."""
    if np is None or len(ref.ticks) < 200 or len(other.ticks) < 200:
        return None
    def grid(ticks, g):
        t = np.array([a for a, _ in ticks], dtype=np.int64)
        p = np.array([b for _, b in ticks])
        o = np.argsort(t, kind="stable")
        t, p = t[o], p[o]
        i = np.searchsorted(t, g, side="right") - 1
        return np.where(i >= 0, p[np.clip(i, 0, None)], np.nan)
    t0 = max(ref.ticks[0][0], other.ticks[0][0]) + 2000
    t1 = min(max(a for a, _ in ref.ticks), max(a for a, _ in other.ticks)) - 2000
    if t1 - t0 < 60000:
        return None
    g = np.arange(t0, t1, step)
    a = np.diff(grid(ref.ticks, g), 2)
    b = np.diff(grid(other.ticks, g), 2)
    best = None
    for lag in range(-300, 301, step):
        s = lag // step
        x, y = (a[:len(a) - s], b[s:]) if s >= 0 else (a[-s:], b[:len(b) + s])
        m = ~(np.isnan(x) | np.isnan(y))
        if m.sum() < 100 or x[m].std() == 0 or y[m].std() == 0:
            continue
        c = float(np.corrcoef(x[m], y[m])[0, 1])
        if best is None or c > best[1]:
            best = (lag, c)
    return best


# ---------------------------------------------------------------- main
async def main_async(minutes):
    host = platform.node()
    print(f"Замер на {host}, {minutes} мин. Не закрывайте окно.\n", flush=True)
    geo = geoblock()
    print("Проверка Polymarket geoblock:", geo, flush=True)
    src, off, rtt = clock_offset()
    print(f"Смещение часов: {off} мс (по {src}, RTT {rtt} мс)", flush=True)
    hosts = ["clob.polymarket.com", "ws-subscriptions-clob.polymarket.com", "stream.binance.com",
             "fstream.binance.com", "data-stream.binance.vision", "stream.bybit.com", "ws-feed.exchange.coinbase.com",
             "ws.okx.com"]
    tcp = {h: tcp_tls(h, 8443 if h == "ws.okx.com" else 443) for h in hosts}
    print("TCP/TLS:", {h: v.get("tcp_ms") for h, v in tcp.items()}, flush=True)
    rest = await asyncio.to_thread(clob_rest)
    print("CLOB REST:", rest, flush=True)

    stop_at = time.time() + minutes * 60
    F = {n: Feed(n) for n in ("binance_futures", "binance_spot", "bybit", "coinbase", "okx")}
    book, trades = Feed("polymarket_book"), Feed("polymarket_trades")
    tasks = [
        run_feed(F["binance_futures"], ["wss://fstream.binance.com/market/stream?streams=btcusdt@aggTrade",
                                        "wss://fstream.binance.com/stream?streams=btcusdt@aggTrade"],
                 None, p_bn, stop_at, off),
        run_feed(F["binance_spot"], ["wss://stream.binance.com:9443/stream?streams=btcusdt@aggTrade",
                                     "wss://data-stream.binance.vision/stream?streams=btcusdt@aggTrade"],
                 None, p_bn, stop_at, off),
        run_feed(F["bybit"], ["wss://stream.bybit.com/v5/public/linear"],
                 json.dumps({"op": "subscribe", "args": ["publicTrade.BTCUSDT"]}), p_by, stop_at, off,
                 ping=json.dumps({"op": "ping"})),
        run_feed(F["coinbase"], ["wss://ws-feed.exchange.coinbase.com"],
                 json.dumps({"type": "subscribe", "product_ids": ["BTC-USD"], "channels": ["ticker"]}), p_cb,
                 stop_at, off),
        run_feed(F["okx"], ["wss://ws.okx.com:8443/ws/v5/public"],
                 json.dumps({"op": "subscribe", "args": [{"channel": "trades", "instId": "BTC-USDT-SWAP"}]}), p_ok,
                 stop_at, off, ping="ping"),
        clob_feed(book, trades, stop_at, off),
    ]

    loop_lag = []
    cpu0, wall0 = time.process_time(), time.time()

    async def lag_monitor():
        """Насколько программа опаздывает сама: если процессор сервера не справляется,
        сообщения копятся в очереди и "задержка" растёт не из-за сети."""
        while time.time() < stop_at:
            t0 = time.perf_counter()
            await asyncio.sleep(0.05)
            loop_lag.append((time.perf_counter() - t0 - 0.05) * 1000)

    async def progress():
        while time.time() < stop_at - 30:
            await asyncio.sleep(60)
            left = (stop_at - time.time()) / 60
            print(f"  ... осталось {left:.0f} мин; сообщений: " +
                  ", ".join(f"{f.name} {len(f.lat)}" for f in list(F.values()) + [book, trades]), flush=True)
    await asyncio.gather(*tasks, progress(), lag_monitor())
    cpu_share = (time.process_time() - cpu0) / max(1e-9, time.time() - wall0)
    try:
        import os
        load = os.getloadavg()[0]
        ncpu = os.cpu_count()
    except Exception:
        load, ncpu = None, None

    out = {"host": host, "time_utc": datetime.now(timezone.utc).isoformat(), "minutes": minutes, "geoblock": geo,
           "clock": {"source": src, "offset_ms": off, "rtt_ms": rtt}, "tcp_tls": tcp, "clob_rest": rest, "feeds": {},
           "machine": {"cpu_share_of_one_core": round(cpu_share, 3), "loadavg_1m": load, "cpus": ncpu,
                       "loop_lag_p50_ms": q(loop_lag, .5), "loop_lag_p99_ms": q(loop_lag, .99),
                       "loop_lag_max_ms": round(max(loop_lag), 1) if loop_lag else None}}
    print("\n=========== ИТОГ ===========")
    mch = out["machine"]
    print(f"Нагрузка: программа заняла {100 * mch['cpu_share_of_one_core']:.0f}% одного ядра, load {mch['loadavg_1m']} "
          f"на {mch['cpus']} ядер; задержка самой программы p99 {mch['loop_lag_p99_ms']} мс, макс {mch['loop_lag_max_ms']} мс"
          + (" - ПРОЦЕССОР НЕ СПРАВЛЯЕТСЯ, задержки ниже завышены" if (mch['loop_lag_p99_ms'] or 0) > 50 else ""))
    st = rest.get("order_status", {})
    if geo.get("blocked") is True or 403 in st:
        verdict = "ЗАКРЫТА - этот регион не подходит"
    elif geo.get("blocked") is False and 401 in st:
        verdict = "разрешена"
    else:
        verdict = "не удалось проверить однозначно"
    out["trading_allowed"] = verdict
    print(f"Торговля с этого IP: {verdict} (geoblock: страна {geo.get('country')}, регион {geo.get('region')}; "
          f"ответы сервера ордеров {st})")
    print(f"Ордер до Polymarket (POST /order туда-обратно): p50 {rest['POST /order']['p50']} мс, "
          f"статусы {rest['order_status']}")
    print(f"{'поток':20s} {'сообщ.':>7s} {'p50 мс':>8s} {'p90':>8s} {'p99':>8s}  отстаёт от фьючерса Binance")
    ref = F["binance_futures"]
    for f in list(F.values()) + [book, trades]:
        lv = lead_vs(ref, f) if f in F.values() and f is not ref else None
        out["feeds"][f.name] = {"n": len(f.lat), "p50": q(f.lat, .5), "p90": q(f.lat, .9), "p99": q(f.lat, .99),
                                "url": f.url, "errors": f.errors,
                                "lag_vs_binance_futures_ms": lv[0] if lv else None}
        lead_txt = "" if lv is None else f"{lv[0]:+d} мс (corr {lv[1]:.2f})"
        print(f"{f.name:20s} {len(f.lat):7d} {str(q(f.lat, .5)):>8s} {str(q(f.lat, .9)):>8s} "
              f"{str(q(f.lat, .99)):>8s}  {lead_txt}")
    # когда информация о тике реально доступна здесь
    arr = {}
    for name, f in F.items():
        d = out["feeds"][name]
        if d["p50"] is None:
            continue
        lead = 0 if name == "binance_futures" else (d["lag_vs_binance_futures_ms"] or 0)
        arr[name] = round(d["p50"] + lead, 1)
    out["arrival_after_binance_futures_tick_ms"] = arr
    print("\nСигнал о тике BTC доходит сюда через (мс после тика на фьючерсе Binance):")
    for name, v in sorted(arr.items(), key=lambda kv: kv[1]):
        print(f"  {name:18s} {v}")
    fn = f"probe_{host}_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    with open(fn, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print(f"\nСохранено в {fn} - пришлите этот файл.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes", type=float, default=10)
    a = ap.parse_args()
    try:
        asyncio.run(main_async(a.minutes))
    except KeyboardInterrupt:
        pass
