"""Процесс 1: запись сырых данных бирж (Binance aggTrade + bookTicker, Coinbase ticker)
и смещения локальных часов относительно сервера Binance.

Ничего не считает - только принимает, ставит локальную метку времени и отдаёт в writer.
Отдельный процесс, чтобы тяжёлый поток Polymarket не мог задержать приём BTC.
"""
from __future__ import annotations

import asyncio
import json
from datetime import datetime

import websockets

from feeds_extra import SCHEMAS as EXTRA_SCHEMAS
from feeds_extra import ExtraFeed

from common import DataWriter, ms, binance_bbo, binance_url, flush_console, LoopLag, Quantiles, clock, fnum, iter_ws, loads, log, probe_clock

SCHEMAS = {
    # все времена в мс. recv_ms - локальное время приёма, T - время сделки на Binance
    "bn_agg": ["recv_ms", "T", "price", "qty", "m"],
    # только при изменении лучших цен (не объёмов)
    "bn_book": ["recv_ms", "bid", "bid_qty", "ask", "ask_qty"],
    # t_ms - время сделки на Coinbase; side: b/s
    "cb_ticker": ["recv_ms", "t_ms", "price", "size", "side", "bid", "ask"],
    # offset = серверное время Binance - локальное (мс), rtt - время запроса
    "clock": ["recv", "source", "offset_ms", "rtt_ms"],
    "events": ["ts", "process", "feed", "event", "detail"],
    "health_cex": ["ts", "bn_msgs", "bn_lat_p50", "bn_lat_p90", "cb_msgs", "cb_lat_p50", "lag_p50", "lag_p99", "lag_max"],
    # доп. биржи: сделок за 10 с и задержка биржа -> вы
    "health_feeds": ["ts", "feed", "msgs", "lat_p50", "lat_p90"],
    **EXTRA_SCHEMAS,
}


class Cex:
    def __init__(self, cfg):
        self.cfg = cfg
        self.w = DataWriter(cfg.data_dir, SCHEMAS, "cex")
        self.lag = LoopLag()
        self.bn_n = 0
        self.cb_n = 0
        self.bn_lat = Quantiles()
        self.cb_lat = Quantiles()
        self.offset_ms: float = 0.0
        self.extra = [ExtraFeed(n, self.w, self) for n in cfg.extra_feeds]
        self._last_bbo = None

    # ------------------------------------------------------------------ Binance
    async def binance(self):
        url, _ = binance_url(self.cfg)
        while True:
            try:
                # Запись, а не торговля: до Азии данные идут с задержкой в секунды, и наш пинг
                # застревает в очереди за ними. Свой пинг не шлём (сервер Binance пингует сам,
                # ответ уходит автоматически), обрыв определяем по 30 с полной тишины.
                async with websockets.connect(url, ping_interval=None,
                                              max_queue=4096, compression=None) as ws:
                    log("cex", f"Binance подключён: {url}")
                    self.w.write("events", (clock.now(), "cex", "binance", "connected", ""))
                    async for raw in iter_ws(ws, 30.0):
                        recv = clock.now()
                        d = loads(raw)
                        x = d.get("data") or d
                        e = x.get("e")
                        if e == "aggTrade":
                            self.bn_n += 1
                            self.w.write("bn_agg", (ms(recv), x["T"], x["p"], x["q"].rstrip("0"), int(x["m"])))
                            self.bn_lat.add(recv * 1000 - x["E"] + self.offset_ms)
                        else:
                            q = binance_bbo(x)
                            if q is not None and (q[1], q[3]) != self._last_bbo:
                                self._last_bbo = (q[1], q[3])
                                self.w.write("bn_book", (ms(recv), *q[1:]))
            except Exception as ex:
                log("cex", f"Binance разорван: {ex!r}. Переподключение через 2 с")
                self.w.write("events", (clock.now(), "cex", "binance", "disconnected", repr(ex)[:300]))
                await asyncio.sleep(2)

    # ------------------------------------------------------------------ Coinbase
    async def coinbase(self):
        sub = json.dumps({"type": "subscribe", "product_ids": ["BTC-USD"], "channels": ["ticker"]})
        while True:
            try:
                async with websockets.connect(self.cfg.coinbase_ws, ping_interval=10, ping_timeout=10,
                                              max_queue=4096, compression=None) as ws:
                    await ws.send(sub)
                    log("cex", "Coinbase подключён")
                    async for raw in ws:
                        recv = clock.now()
                        x = loads(raw)
                        if x.get("type") != "ticker":
                            continue
                        try:
                            tms = datetime.fromisoformat(x["time"].replace("Z", "+00:00")).timestamp() * 1000
                        except Exception:
                            tms = None
                        self.cb_n += 1
                        if tms:
                            self.cb_lat.add(recv * 1000 - tms + self.offset_ms)
                        self.w.write("cb_ticker", (ms(recv), int(tms) if tms else None, x.get("price"), x.get("last_size"),
                                                   (x.get("side") or "?")[0], x.get("best_bid"), x.get("best_ask")))
            except Exception as ex:
                log("cex", f"Coinbase разорван: {ex!r}. Переподключение через 5 с")
                self.w.write("events", (clock.now(), "cex", "coinbase", "disconnected", repr(ex)[:300]))
                await asyncio.sleep(5)

    # ------------------------------------------------------------------ часы
    async def clock_loop(self):
        while True:
            try:
                src, off, rtt = await asyncio.to_thread(probe_clock, self.cfg.binance_rest)
                self.offset_ms = off
                self.w.write("clock", (clock.now(), src, round(off, 2), round(rtt, 2)))
            except Exception as ex:
                log("cex", f"замер часов не удался: {ex!r}")
            await asyncio.sleep(60)

    # ------------------------------------------------------------------ статус
    async def status(self):
        while True:
            await asyncio.sleep(self.cfg.status_every_sec)
            lag = self.lag.snapshot_reset()
            row = (clock.now(), self.bn_n, self.bn_lat.q(0.5), self.bn_lat.q(0.9), self.cb_n,
                   self.cb_lat.q(0.5), lag[0], lag[1], lag[2])
            self.w.write("health_cex", row)
            log("cex", f"Binance {self.bn_n} сд. задержка p50/p90={fnum(row[2])}/{fnum(row[3])} мс | "
                       f"Coinbase {self.cb_n} задержка p50={fnum(row[5])} мс | "
                       f"смещение часов {self.offset_ms:+.1f} мс | lag loop p99/max={fnum(lag[1])}/{fnum(lag[2])} мс")
            self.bn_n = self.cb_n = 0
            self.bn_lat.clear()
            self.cb_lat.clear()
            parts = []
            for f in self.extra:
                n, p50, p90 = f.status_and_reset()
                self.w.write("health_feeds", (clock.now(), f.name, n, p50, p90))
                parts.append(f"{f.name} {n} сд. p50={fnum(p50)} мс")
            if parts:
                log("cex", " | ".join(parts))

    async def main(self):
        tasks = [self.binance(), self.clock_loop(), self.status(), self.lag.run()] + [f.run() for f in self.extra]
        if self.cfg.coinbase:
            tasks.append(self.coinbase())
        await asyncio.gather(*tasks)


def run(cfg):
    c = Cex(cfg)
    try:
        asyncio.run(c.main())
    except KeyboardInterrupt:
        pass
    finally:
        c.w.close()
        flush_console()
