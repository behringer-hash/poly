"""Дополнительные биржи для записи: фьючерсы Binance, Bybit, OKX (бессрочные контракты BTC-USDT).

Цель - проверить, не опережает ли какая-то из них спот Binance и Coinbase и не
следуют ли за её тиками "тихие" входы кошелька. Пишем только сделки: это лёгкие
потоки, и в каждой сделке есть время биржи в мс - по нему и идёт анализ,
задержка доставки до вас на выводы не влияет.

Адреса бирж иногда меняются, поэтому у каждой несколько вариантов: при ошибке
или отсутствии данных программа переходит к следующему.
"""
from __future__ import annotations

import asyncio
import json

import websockets

from common import Quantiles, clock, iter_ws, loads, log, ms


def _bnf_parse(d):
    x = d.get("data") or d
    if x.get("e") != "aggTrade":
        return []
    return [((x["T"], x.get("E"), x["p"], x["q"].rstrip("0"), int(x["m"])), x["T"])]


def _bybit_parse(d):
    if not str(d.get("topic", "")).startswith("publicTrade"):
        return []
    out = []
    for it in d.get("data") or []:
        out.append(((it["T"], it["p"], it["v"], (it.get("S") or "?")[0]), it["T"]))
    return out


def _okx_parse(d):
    if "data" not in d or (d.get("arg") or {}).get("channel") != "trades":
        return []
    out = []
    for it in d["data"]:
        ts = int(it["ts"])
        out.append(((ts, it["px"], it["sz"], (it.get("side") or "?")[0]), ts))
    return out


def _bnf_book_parse(d):
    x = d.get("data") or d
    if x.get("e") != "bookTicker":
        return []
    t = x.get("T") or x.get("E")
    return [((t, x.get("E"), x.get("u"), x["b"], x["B"], x["a"], x["A"]), t)]


def _lv(levels, n=5):
    """Уровни книги компактной строкой 'цена:объём|цена:объём' (первые n)."""
    return "|".join(f"{p}:{q}" for p, q in (levels or [])[:n])


def _bnf_depth_parse(d):
    x = d.get("data") or d
    if x.get("e") != "depthUpdate":
        return []
    t = x.get("T") or x.get("E")
    return [((t, x.get("E"), _lv(x.get("b")), _lv(x.get("a"))), t)]


def _bnf_liq_parse(d):
    x = d.get("data") or d
    if x.get("e") != "forceOrder":
        return []
    o = x.get("o") or {}
    t = o.get("T") or x.get("E")
    return [((t, o.get("S"), o.get("p"), o.get("ap"), o.get("q"), o.get("z"), o.get("X")), t)]


def _bybit_book_parse(d):
    if not str(d.get("topic", "")).startswith("orderbook."):
        return []
    x = d.get("data") or {}
    t = d.get("ts") or x.get("cts")
    return [((t, d.get("cts") or x.get("cts"), d.get("type", "")[:1], x.get("u"), _lv(x.get("b")), _lv(x.get("a"))), t)]


def _bybit_liq_parse(d):
    topic = str(d.get("topic", ""))
    if not (topic.startswith("allLiquidation") or topic.startswith("liquidation")):
        return []
    data = d.get("data")
    items = data if isinstance(data, list) else [data] if data else []
    out = []
    for it in items:
        t = it.get("T") or it.get("updatedTime") or d.get("ts")
        out.append(((t, it.get("S") or it.get("side"), it.get("p") or it.get("price"),
                     it.get("v") or it.get("size")), t))
    return out


def _kraken_parse(d):
    if d.get("channel") != "trade" or d.get("type") not in ("update", "snapshot"):
        return []
    from datetime import datetime
    out = []
    for it in d.get("data") or []:
        t = int(datetime.fromisoformat(it["timestamp"].replace("Z", "+00:00")).timestamp() * 1000)
        out.append(((t, it["price"], it["qty"], (it.get("side") or "?")[0]), t))
    return out


def _bitstamp_parse(d):
    if d.get("event") != "trade":
        return []
    x = d.get("data") or {}
    t = int(x.get("microtimestamp", 0)) // 1000 or int(x.get("timestamp", 0)) * 1000
    return [((t, x.get("price"), x.get("amount"), "b" if x.get("type") == 0 else "s"), t)]


_BNF_HOSTS = ["wss://fstream.binance.com/public/stream?streams=", "wss://fstream.binance.com/stream?streams=",
              "wss://fstream.binance.com/market/stream?streams="]

FEEDS = {
    # имя: (поток в файлах, колонки, адреса, сообщение подписки, разбор, текстовый пинг, период пинга)
    "binance_futures": (
        "bnf_agg", ["recv_ms", "T", "E", "price", "qty", "m"],
        ["wss://fstream.binance.com/stream?streams=btcusdt@aggTrade",
         "wss://fstream.binance.com/market/stream?streams=btcusdt@aggTrade",
         "wss://fstream.binance.com/ws/btcusdt@aggTrade"],
        None, _bnf_parse, None, 0),
    "bybit": (
        "by_trade", ["recv_ms", "T", "price", "size", "side"],
        ["wss://stream.bybit.com/v5/public/linear"],
        json.dumps({"op": "subscribe", "args": ["publicTrade.BTCUSDT"]}), _bybit_parse,
        json.dumps({"op": "ping"}), 20),
    "okx": (
        "ok_trade", ["recv_ms", "T", "price", "size", "side"],
        ["wss://ws.okx.com:8443/ws/v5/public", "wss://wsaws.okx.com:8443/ws/v5/public"],
        json.dumps({"op": "subscribe", "args": [{"channel": "trades", "instId": "BTC-USDT-SWAP"}]}), _okx_parse,
        "ping", 20),
    # --- для поиска опережающих индикаторов (книга с объёмами, ликвидации, европейские биржи) ---
    "binance_futures_book": (
        "bnf_book", ["recv_ms", "T", "E", "u", "bid", "bid_qty", "ask", "ask_qty"],
        [h + "btcusdt@bookTicker" for h in _BNF_HOSTS] + ["wss://fstream.binance.com/ws/btcusdt@bookTicker"],
        None, _bnf_book_parse, None, 0),
    "binance_futures_depth": (
        "bnf_depth5", ["recv_ms", "T", "E", "bids", "asks"],
        [h + "btcusdt@depth5@100ms" for h in _BNF_HOSTS] + ["wss://fstream.binance.com/ws/btcusdt@depth5@100ms"],
        None, _bnf_depth_parse, None, 0),
    "binance_liq": (
        "bnf_liq", ["recv_ms", "T", "side", "price", "avg_price", "qty", "filled", "status"],
        [h + "btcusdt@forceOrder" for h in reversed(_BNF_HOSTS)] + ["wss://fstream.binance.com/ws/btcusdt@forceOrder"],
        None, _bnf_liq_parse, None, 0),
    "bybit_book": (
        "by_book1", ["recv_ms", "T", "cts", "type", "u", "bids", "asks"],
        ["wss://stream.bybit.com/v5/public/linear"],
        json.dumps({"op": "subscribe", "args": ["orderbook.1.BTCUSDT"]}), _bybit_book_parse,
        json.dumps({"op": "ping"}), 20),
    "bybit_liq": (
        "by_liq", ["recv_ms", "T", "side", "price", "size"],
        ["wss://stream.bybit.com/v5/public/linear"],
        json.dumps({"op": "subscribe", "args": ["allLiquidation.BTCUSDT"]}), _bybit_liq_parse,
        json.dumps({"op": "ping"}), 20),
    "kraken": (
        "kr_trade", ["recv_ms", "T", "price", "size", "side"],
        ["wss://ws.kraken.com/v2"],
        json.dumps({"method": "subscribe", "params": {"channel": "trade", "symbol": ["BTC/USD"]}}), _kraken_parse,
        json.dumps({"method": "ping"}), 20),
    "bitstamp": (
        "bs_trade", ["recv_ms", "T", "price", "size", "side"],
        ["wss://ws.bitstamp.net"],
        json.dumps({"event": "bts:subscribe", "data": {"channel": "live_trades_btcusd"}}), _bitstamp_parse,
        json.dumps({"event": "bts:heartbeat"}), 20),
}
# ликвидации и редкие сделки могут молчать дольше 30 с - для них не переключаем адрес по тишине
QUIET_OK = {"binance_liq", "bybit_liq", "bitstamp", "kraken"}

SCHEMAS = {v[0]: v[1] for v in FEEDS.values()}


class ExtraFeed:
    def __init__(self, name: str, writer, owner):
        self.name = name
        self.stream, _, self.urls, self.sub, self.parse, self.ping, self.ping_every = FEEDS[name]
        self.w = writer
        self.owner = owner  # для поправки часов (offset_ms)
        self.n = 0
        self.lat = Quantiles()

    async def _pinger(self, ws):
        try:
            while True:
                await asyncio.sleep(self.ping_every)
                await ws.send(self.ping)
        except Exception:
            pass

    async def run(self):
        i = 0
        while True:
            url = self.urls[i % len(self.urls)]
            got = 0
            try:
                # запись, а не торговля: терпим задержку, свой keepalive-пинг не шлём (см. cex.binance)
                async with websockets.connect(url, open_timeout=15, ping_interval=None,
                                              max_queue=4096, compression=None) as ws:
                    if self.sub:
                        await ws.send(self.sub)
                    log("cex", f"{self.name} подключён: {url}")
                    self.w.write("events", (clock.now(), "cex", self.name, "connected", url))
                    pinger = asyncio.create_task(self._pinger(ws)) if self.ping else None
                    try:
                        async for raw in iter_ws(ws, 600.0 if self.name in QUIET_OK else 30.0):
                            recv = clock.now()
                            if raw in ("pong", "PONG") or not raw:
                                continue
                            try:
                                d = loads(raw)
                            except Exception:
                                continue
                            for row, ets in self.parse(d):
                                got += 1
                                self.n += 1
                                self.lat.add(recv * 1000 - ets + self.owner.offset_ms)
                                self.w.write(self.stream, (ms(recv), *row))
                    finally:
                        if pinger:
                            pinger.cancel()
            except Exception as ex:
                self.w.write("events", (clock.now(), "cex", self.name, "disconnected", f"{url} {ex!r}"[:300]))
                log("cex", f"{self.name}: {ex!r} ({url})")
            if got == 0:  # с этим адресом данных нет - пробуем следующий
                i += 1
            await asyncio.sleep(3)

    def status_and_reset(self):
        r = (self.n, self.lat.q(0.5), self.lat.q(0.9))
        self.n = 0
        self.lat.clear()
        return r
