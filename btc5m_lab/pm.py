"""Процесс 2: Polymarket (книга ордеров, сделки, RTDS/Chainlink) + бумажная торговля.

Бумажный движок живёт в этом же процессе, потому что ему нужна книга Polymarket
"здесь и сейчас". Для него открывается собственное лёгкое соединение с Binance
(запись сырого Binance идёт в процессе cex).
"""
from __future__ import annotations

import asyncio
from collections import deque
import json
import time

import requests
import websockets

from common import (WINDOW_SEC, DataWriter, ms, binance_bbo, binance_url, flush_console, LoopLag, Quantiles, RollingSigma, big_rcvbuf_socket, clock, fnum,
                    iter_ws, loads, log, probe_clock, slug_for, utc_str, window_start)
from paper import PAPER_SCHEMAS, Paper, settle_sd
from common import norm_inv

SCHEMAS = {
    # Все времена - целые мс. w - начало окна (unix, с), o - U/D.
    # Изменения ЛУЧШИХ ЦЕН (изменения только объёма не пишем - это 94% трафика);
    # d = recv_ms - время сервера Polymarket; c - номер соединения (0/1)
    "pm_top": ["recv_ms", "d", "w", "o", "bid", "bid_sz", "ask", "ask_sz", "c"],
    # топ-5 уровней с частотой depth_hz (только если что-то изменилось)
    "pm_depth": ["ts_ms", "w", "o"] + [f"b{i}" for i in range(1, 6)] + [f"bs{i}" for i in range(1, 6)]
                + [f"a{i}" for i in range(1, 6)] + [f"as{i}" for i in range(1, 6)],
    # все сделки рынка; tx - первые 16 символов хэша транзакции (для поиска сделок кошелька)
    "pm_trades": ["recv_ms", "server_ts", "w", "o", "side", "price", "size", "fee_bps", "tx"],
    # feed: tw (TWAP60), cl (Chainlink), rb (Binance через Polymarket)
    "rtds": ["recv_ms", "feed", "ts_ms", "value"],
    # время HTTPS-запросов к CLOB (нижняя граница задержки ордера)
    "pm_rtt": ["ts_ms", "endpoint", "status", "rtt_ms"],
    "windows": ["logged_at", "slug", "start", "end", "question", "condition_id", "up_token", "down_token",
                "fee_type", "taker_base_fee", "ptb_twap", "ptb_chainlink", "end_twap", "end_chainlink",
                "provisional_winner", "official_winner", "official_prices", "settled_with"],
    "events_pm": ["ts", "process", "feed", "event", "detail"],
    "clock_pm": ["recv", "source", "offset_ms", "rtt_ms"],
    "health_pm": ["ts", "clob_msgs", "clob_lat_p50", "clob_lat_p90", "top_changes", "trades", "rtds_msgs",
                  "bn_msgs", "bn_lat_p50", "lag_p50", "lag_p99", "lag_max"],
    **PAPER_SCHEMAS,
}

RTDS_SHORT = {"twap60": "tw", "chainlink": "cl", "rtds_binance": "rb"}
RTDS_FEEDS = {  # feed -> (topic, symbol)
    "twap60": ("crypto_prices_twap_sixty", "btc/usd"),
    "chainlink": ("crypto_prices_chainlink", "btc/usd"),
    "rtds_binance": ("crypto_prices", "btcusdt"),
}


def _sz(v):
    return None if v is None else round(v, 1)


def _px(v):
    """Цена из сообщения сервера; всё вне (0, 1) - отсутствие уровня."""
    try:
        x = float(v)
    except (TypeError, ValueError):
        return None
    return x if 0.0 < x < 1.0 else None


# ============================================================================ книга
class Book:
    __slots__ = ("bids", "asks", "ready", "bb", "ba", "last_top", "last_mid", "anchor_btc", "anchor_px", "anchor_px_res", "anchor_ts",
                 "last_update", "last_depth", "last_w", "pend", "z0_mid", "z0")

    def __init__(self):
        self.bids: dict[float, float] = {}
        self.asks: dict[float, float] = {}
        self.ready = False
        self.bb = None
        self.ba = None
        self.last_top = None
        self.last_mid = None
        self.anchor_btc = None   # цена BTC в момент последнего изменения mid (для модели "anchor")
        self.anchor_px: dict[str, float] = {}  # цены всех источников BTC в момент последнего изменения mid
        self.anchor_px_res: dict[str, float] = {}  # "остаточный" якорь: учитывает, какую часть хода книга отыграла
        self.anchor_ts = None
        self.last_update = 0.0
        self.last_depth = None
        self.last_w = 0.0     # когда последний раз писали строку pm_top для этой книги
        self.pend = None      # отложенная (из-за прореживания) строка с изменением объёма
        self.z0_mid = None    # кэш norm_inv(mid) для бумажного движка
        self.z0 = 0.0

    def snapshot(self, bids, asks):
        self.bids = {float(l["price"]): float(l["size"]) for l in bids}
        self.asks = {float(l["price"]): float(l["size"]) for l in asks}
        self.bb = max(self.bids) if self.bids else None
        self.ba = min(self.asks) if self.asks else None
        self.ready = True

    def set_level(self, side: str, price: float, size: float):
        book = self.bids if side == "BUY" else self.asks
        if size == 0:
            book.pop(price, None)
        else:
            book[price] = size

    def refresh_best(self, bb=None, ba=None):
        # Polymarket присылает best_bid/best_ask в каждом изменении - используем их,
        # при отсутствии пересчитываем по книге
        self.bb = bb if bb is not None else (max(self.bids) if self.bids else None)
        self.ba = ba if ba is not None else (min(self.asks) if self.asks else None)
        if self.bb is not None and not 0.0 < self.bb < 1.0:
            self.bb = None
        if self.ba is not None and not 0.0 < self.ba < 1.0:
            self.ba = None

    def top(self):
        return (self.bb, self.bids.get(self.bb) if self.bb is not None else None,
                self.ba, self.asks.get(self.ba) if self.ba is not None else None)

    def mid(self):
        if self.bb is not None and self.ba is not None:
            return (self.bb + self.ba) / 2
        return None

    def levels(self, n: int):
        b = sorted(self.bids.items(), key=lambda kv: -kv[0])[:n]
        a = sorted(self.asks.items(), key=lambda kv: kv[0])[:n]
        return b, a


class WindowState:
    def __init__(self, start: int, market: dict):
        self.start = start
        self.end = start + WINDOW_SEC
        self.slug = slug_for(start)
        self.m = market
        self.asset_to_outcome = {market["up_token"]: "Up", market["down_token"]: "Down"}
        # два независимых соединения с собственными копиями книги; пишем и торгуем
        # по активному, при его обрыве мгновенно переключаемся на резервное
        self.conn_books = [{"Up": Book(), "Down": Book()}, {"Up": Book(), "Down": Book()}]
        self.active = 0
        self.book_lag_ms = None   # отставание нашей книги от сервера Polymarket по последнему сообщению, мс
        self.ptb = None
        self.ptb_chainlink = None
        self.resolved = False

    @property
    def books(self):
        return self.conn_books[self.active]

    def conn_ready(self, cid: int) -> bool:
        b = self.conn_books[cid]
        return b["Up"].ready and b["Down"].ready

    def ready(self):
        return self.conn_ready(self.active)


# ============================================================================ процесс
class PM:
    def __init__(self, cfg):
        self.cfg = cfg
        self.w = DataWriter(cfg.data_dir, SCHEMAS, "pm")
        self.lag = LoopLag()
        self.windows: dict[int, WindowState] = {}
        self._window_tasks: dict[int, asyncio.Task] = {}
        # BTC
        self.cl: dict[int, float] = {}      # chainlink по секундам
        self.tw: dict[int, float] = {}      # twap60 по секундам
        self.bn_mid: float | None = None
        self.bn_recv: float = 0.0     # время последнего изменения цены BTC
        self.bn_alive: float = 0.0    # время последнего любого сообщения фида BTC (фид жив)
        # все источники цены BTC: имя -> {"px": цена, "recv": когда изменилась, "alive": последнее сообщение}
        self.src: dict[str, dict] = {}
        self.src_lat = {"bybit": Quantiles(), "coinbase": Quantiles()}
        self.by_msgs = {"book": 0, "trade": 0, "other": 0}  # сообщений Bybit за интервал статуса
        # история цен источников для моментум-триггера: имя -> deque[(время приёма, цена)]
        self.mom_hist: dict[str, deque] = {}
        self.mom_sigma: dict[str, RollingSigma] = {}   # волатильность каждого источника за 5 мин, $/sqrt(с)
        self.fut_qi = None                             # дисбаланс верха книги фьючерса Binance, -1..1
        self.fut_qi_prev = None                        # предыдущее значение (сигнал - только при пересечении порога)
        self.src_lat.setdefault("binance_fut_book", Quantiles())
        self.qi_thresholds = sorted({v.qi_min for v in self.cfg.variants if v.model == "imbalance" and v.qi_min > 0})
        self.qi_eval_min = self.qi_thresholds[0] if self.qi_thresholds else 2.0
        self.src_lat.setdefault("binance_fut", Quantiles())
        self.bn_sec: dict[int, float] = {}  # цена Binance по секундам (для базиса к Chainlink)
        self.basis: float | None = None     # chainlink - binance, EMA
        self.sigma = RollingSigma(900, cfg.sigma_fallback)
        # статистика
        self.n_clob = self.n_top = self.n_trades = self.n_rtds = self.n_bn = 0
        self.clob_lat = Quantiles()
        self.rtt_q = Quantiles(200)
        self.bn_lat = Quantiles()
        self.offset_ms = 0.0
        self.paper = Paper(cfg, self, self.w) if cfg.paper else None
        self.maker = None
        if getattr(cfg, "maker", False):
            from maker import MAKER_SCHEMAS, MakerPaper
            self.w.schemas.update(MAKER_SCHEMAS)
            self.maker = MakerPaper(cfg, self, self.w, getattr(cfg, "maker_show", None))

    # ---------------------------------------------------------------- helpers
    def current_window(self, ts: float) -> WindowState | None:
        return self.windows.get(window_start(ts))

    def _fetch_market(self, slug: str) -> dict:
        r = requests.get(f"{self.cfg.gamma_api}/events", params={"slug": slug}, timeout=10)
        r.raise_for_status()
        ev = r.json()
        if not ev:
            raise RuntimeError("рынок ещё не создан")
        m = ev[0]["markets"][0]
        outcomes = json.loads(m["outcomes"])
        toks = json.loads(m["clobTokenIds"])
        return {
            "question": m.get("question"), "condition_id": m.get("conditionId"),
            "up_token": toks[outcomes.index("Up")], "down_token": toks[outcomes.index("Down")],
            "fee_type": m.get("feeType"), "taker_base_fee": m.get("takerBaseFee"),
            "closed": m.get("closed"), "outcome_prices": m.get("outcomePrices"), "outcomes": outcomes,
        }

    # ---------------------------------------------------------------- окна
    async def windows_loop(self):
        while True:
            now = clock.now()
            cur = window_start(now)
            for st in (cur, cur + WINDOW_SEC):
                if st not in self._window_tasks and now >= st - self.cfg.pre_open_sec and now < st + WINDOW_SEC:
                    self._window_tasks[st] = asyncio.create_task(self.run_window(st))
            # чистка старых окон (после резолюции + запас)
            for st in list(self.windows):
                w = self.windows[st]
                if now > w.end + 1500 or (w.resolved and now > w.end + 60):
                    self.windows.pop(st, None)
                    self._window_tasks.pop(st, None)
            await asyncio.sleep(0.5)

    async def run_window(self, st: int):
        slug = slug_for(st)
        market = None
        while market is None and clock.now() < st + WINDOW_SEC:
            try:
                market = await asyncio.to_thread(self._fetch_market, slug)
            except Exception as ex:
                log("pm", f"{slug}: рынок недоступен ({ex}); повтор через 2 с")
                await asyncio.sleep(2)
        if market is None:
            return
        win = WindowState(st, market)
        self.windows[st] = win
        log("pm", f"окно {slug} ({utc_str(st)} UTC): {market['question']}")
        asyncio.create_task(self.resolve_window(win))
        stop_at = win.end + self.cfg.post_close_sec
        conns = [self._conn_loop(win, 0, stop_at)]
        if self.cfg.backup_clob:
            conns.append(self._conn_loop(win, 1, stop_at))
        await asyncio.gather(*conns)

    async def _conn_loop(self, win: WindowState, cid: int, stop_at: float):
        if cid == 1:
            await asyncio.sleep(1.0)  # разнести подключения во времени
        while clock.now() < stop_at:
            try:
                await asyncio.wait_for(self.clob_listen(win, cid), timeout=max(1.0, stop_at - clock.now()))
            except asyncio.TimeoutError:
                break
            except Exception as ex:
                for b in win.conn_books[cid].values():
                    b.ready = False
                self.w.write("events_pm", (clock.now(), "pm", f"clob{cid}", "disconnected",
                                           f"{win.slug} {ex!r}"[:300]))
                if cid == win.active and win.conn_ready(1 - cid):
                    win.active = 1 - cid
                    self.w.write("events_pm", (clock.now(), "pm", f"clob{1 - cid}", "promoted", win.slug))
                else:
                    log("pm", f"{win.slug}: CLOB#{cid} разорван ({ex!r}), переподключение")
                await asyncio.sleep(0.3)

    async def clob_listen(self, win: WindowState, cid: int):
        sock, host = await asyncio.to_thread(big_rcvbuf_socket, self.cfg.clob_ws)
        async with websockets.connect(self.cfg.clob_ws, ping_interval=None, max_queue=4096, compression=None,
                                      max_size=2**23, sock=sock, server_hostname=host) as ws:
            await ws.send(json.dumps({"type": "market", "assets_ids": [win.m["up_token"], win.m["down_token"]]}))
            pinger = asyncio.create_task(self._text_ping(ws, 10))
            try:
                async for raw in iter_ws(ws, 15.0):
                    recv = clock.now()
                    if raw == "PONG" or not raw:
                        continue
                    try:
                        d = loads(raw)
                    except Exception:
                        continue
                    if cid == win.active:
                        self.n_clob += 1
                    for e in (d if isinstance(d, list) else [d]):
                        self._on_clob(win, e, recv, cid)
            finally:
                pinger.cancel()

    @staticmethod
    async def _text_ping(ws, every):
        try:
            while True:
                await asyncio.sleep(every)
                await ws.send("PING")
        except Exception:
            pass

    def _on_clob(self, win: WindowState, e: dict, recv: float, cid: int):
        et = e.get("event_type")
        sts = e.get("timestamp")
        sts = int(sts) if sts else None
        books = win.conn_books[cid]
        if cid != win.active and not win.ready() and win.conn_ready(cid):
            win.active = cid  # активное соединение без книги, это - с книгой: переключаемся
            self.w.write("events_pm", (recv, "pm", f"clob{cid}", "promoted", win.slug))
        primary = cid == win.active
        if sts and primary:
            lag = recv * 1000 - sts + self.offset_ms
            self.clob_lat.add(lag)
            win.book_lag_ms = lag
        touched = set()
        if et == "price_change":
            items = e.get("price_changes")
            if items is None:  # старый формат
                items = [dict(c, asset_id=e.get("asset_id")) for c in e.get("changes", [])]
            for it in items:
                oc = win.asset_to_outcome.get(it.get("asset_id"))
                if oc is None:
                    continue
                b = books[oc]
                b.set_level(it.get("side", "").upper(), float(it["price"]), float(it["size"]))
                b.refresh_best(_px(it.get("best_bid")), _px(it.get("best_ask")))
                touched.add(oc)
        elif et == "book":
            oc = win.asset_to_outcome.get(e.get("asset_id"))
            if oc is None:
                return
            books[oc].snapshot(e.get("bids") or e.get("buys") or [], e.get("asks") or e.get("sells") or [])
            touched.add(oc)
        elif et == "last_trade_price":
            if not primary:
                return
            oc = win.asset_to_outcome.get(e.get("asset_id"))
            self.n_trades += 1
            tx = (e.get("transaction_hash") or "")[2:18]
            self.w.write("pm_trades", (ms(recv), sts, win.start, (oc or "?")[0], (e.get("side") or "?")[0],
                                       e.get("price"), e.get("size"), e.get("fee_rate_bps"), tx))
            if self.maker is not None and oc and sts:
                self.maker.on_trade(win, oc, (e.get("side") or "?")[0], e.get("price"), e.get("size"), sts)
            return
        else:
            return
        price_moved = False
        for oc in touched:
            b = books[oc]
            b.last_update = recv
            top = b.top()
            if top != b.last_top:
                price_changed = b.last_top is None or top[0] != b.last_top[0] or top[2] != b.last_top[2]
                price_moved = price_moved or price_changed
                b.last_top = top
                # цены - всегда; изменения только объёма - по настройке top_sizes
                # (по умолчанию только Up: книга Down - зеркало, её лучшие уровни те же)
                size_ok = self.cfg.top_sizes == "both" or (self.cfg.top_sizes == "up" and oc == "Up")
                row = (ms(recv), ms(recv) - sts if sts else None, win.start, oc[0],
                       top[0], _sz(top[1]), top[2], _sz(top[3]), cid)
                if primary and price_changed:
                    self._write_top(b, row, recv)
                elif primary and size_ok:
                    # изменения только объёма идут пачками по десятку за миллисекунды:
                    # пишем не чаще раза в top_size_throttle_ms, последнее состояние пачки - с задержкой
                    if recv - b.last_w >= self.cfg.top_size_throttle_ms / 1000:
                        self._write_top(b, row, recv)
                    else:
                        b.pend = (row, recv)
                mid = b.mid()
                if mid != b.last_mid:
                    self._update_residual_anchor(b, oc, b.last_mid, mid, win, recv)
                    b.last_mid = mid
                    b.anchor_btc = self.bn_mid
                    b.anchor_px = {k: v["px"] for k, v in self.src.items()}
                    b.anchor_ts = recv
        # оценку сигналов по событиям книги запускаем только при изменении лучших цен: изменения
        # одних объёмов (сотни в секунду) на модель не влияют, а процессор съедают
        if price_moved and primary and self.paper is not None and win.ready():
            self.paper.evaluate(recv, "book")
        if price_moved and primary and self.maker is not None and win.ready():
            self.maker.requote(recv)

    def _update_residual_anchor(self, b, oc, old_mid, new_mid, win, recv):
        """Книга сдвинулась с old_mid на new_mid. Переводим этот сдвиг в доллары хода BTC, которые рынок
        "отыграл", и сдвигаем якорь только на них: неотыгранная часть хода остаётся в памяти."""
        if not self.src:
            return
        if old_mid is None or new_mid is None or not (0.01 < old_mid < 0.99) or not (0.01 < new_mid < 0.99):
            b.anchor_px_res = {k: v["px"] for k, v in self.src.items()}
            return
        T = max(win.end - recv, 0.5)
        sd, wgt = settle_sd(T, self.sigma.sigma())
        sgn = 1.0 if oc == "Up" else -1.0
        priced = sgn * (norm_inv(new_mid) - norm_inv(old_mid)) * sd / max(wgt, 1e-3)
        res = {}
        for k, v in self.src.items():
            S = v["px"]
            if S is None:
                continue
            A = b.anchor_px_res.get(k, S)
            unpriced = S - A
            left = unpriced - priced
            if unpriced == 0 or left * unpriced <= 0:
                left = 0.0            # рынок отыграл всё (или сдвинулся против) - начинаем с нуля
            elif abs(left) > abs(unpriced):
                left = unpriced       # книга ушла против хода BTC - неотыгранное не растёт
            res[k] = S - left
        b.anchor_px_res = res

    def _write_top(self, b, row, recv):
        self.n_top += 1
        self.w.write("pm_top", row)
        b.last_w = recv
        b.pend = None

    async def top_flush_loop(self):
        thr = self.cfg.top_size_throttle_ms / 1000
        while True:
            await asyncio.sleep(0.02)
            now = clock.now()
            for win in list(self.windows.values()):
                for b in win.books.values():
                    if b.pend is not None and now - b.last_w >= thr:
                        row, recv = b.pend
                        self._write_top(b, row, recv)

    async def depth_loop(self):
        period = 1.0 / self.cfg.depth_hz
        n = self.cfg.depth_levels
        while True:
            await asyncio.sleep(period)
            ts = clock.now()
            for win in list(self.windows.values()):
                if ts > win.end + self.cfg.post_close_sec:
                    continue
                for oc, b in win.books.items():
                    if not b.ready:
                        continue
                    bl, al = b.levels(n)
                    key = (tuple(bl), tuple(al))
                    if key == b.last_depth:
                        continue
                    b.last_depth = key
                    pad = lambda lv, k: [(lv[i][k] if k == 0 else _sz(lv[i][k])) if i < len(lv) else None
                                         for i in range(5)]
                    self.w.write("pm_depth", (ms(ts), win.start, oc[0], *pad(bl, 0), *pad(bl, 1),
                                              *pad(al, 0), *pad(al, 1)))

    # ---------------------------------------------------------------- резолюция
    def _tw_near(self, sec: int, exact_only: bool):
        """TWAP60 из потока Polymarket на секунду sec; соседние секунды - только если
        точная так и не пришла (поток изредка пропускает секунду)."""
        v = self.tw.get(sec)
        if v is not None or exact_only:
            return v
        for d in (-1, 1, -2, 2):
            v = self.tw.get(sec + d)
            if v is not None:
                return v
        return None

    def _twap_calc(self, sec: int):
        """Запасной вариант: TWAP60, посчитанный самим по посекундным ценам Chainlink."""
        vals = [self.cl[s] for s in range(sec - 59, sec + 1) if s in self.cl]
        return sum(vals) / len(vals) if len(vals) >= 40 else None

    async def _twap_at(self, sec: int, wait: int):
        """TWAP60 на секунду sec. Ждём значение из потока до sec+wait; соседние секунды и
        собственный расчёт по Chainlink - только когда эта секунда уже точно прошла."""
        while True:
            now = clock.now() + self.offset_ms / 1000
            passed = now >= sec + 3
            v = self._tw_near(sec, exact_only=not passed)
            if v is not None:
                return v, "twap"
            if now >= sec + 8:
                v = self._twap_calc(sec)
                if v is not None:
                    return v, "chainlink_calc"
            if now >= sec + wait:
                return None, "none"
            await asyncio.sleep(1)

    async def resolve_window(self, win: WindowState):
        try:
            await self._resolve_window(win)
        except Exception as ex:  # задача не должна умирать молча: иначе окно никогда не закроется
            log("pm", f"{win.slug}: ошибка при подведении итогов окна: {ex!r}")
            self.w.write("events_pm", (clock.now(), "pm", "resolve", "error", f"{win.slug} {ex!r}"[:300]))

    async def _resolve_window(self, win: WindowState):
        # price to beat = TWAP60 Chainlink на секунду начала окна
        win.ptb, src_start = await self._twap_at(win.start, 60)
        if src_start != "twap":
            log("pm", f"{win.slug}: нет TWAP60 из потока на начало окна, price to beat: {src_start}")
        win.ptb_chainlink = self.cl.get(win.start)

        await asyncio.sleep(max(0.0, win.end - clock.now()) + 3)
        end_tw, src_end = await self._twap_at(win.end, 30)
        prov, used_prov = None, "provisional"
        if end_tw is not None and win.ptb is not None:
            prov = "Up" if end_tw >= win.ptb else "Down"
            if "chainlink_calc" in (src_start, src_end):
                used_prov = "provisional_calc"
        else:  # последний запасной вариант: по последней цене книги перед концом окна
            bu = win.books["Up"]
            m = bu.last_mid if bu.last_mid is not None else (bu.bb if bu.bb is not None else bu.ba)
            if m is not None:
                prov, used_prov = ("Up" if m >= 0.5 else "Down"), "provisional_book"
            log("pm", f"{win.slug}: нет TWAP60 на конец окна, исход по книге: {prov}")
        # бумажные счета закрываем сразу по предварительному исходу;
        # официальный исход из gamma пишем в windows.csv, анализ опирается на него
        if self.paper is not None and prov:
            self.paper.settle(win, prov, used_prov)
        if self.maker is not None and prov:
            self.maker.settle(win, prov)

        official, prices = None, None
        deadline = clock.now() + 1200
        while clock.now() < deadline:
            try:
                m = await asyncio.to_thread(self._fetch_market, win.slug)
                pr = json.loads(m["outcome_prices"]) if m.get("outcome_prices") else None
                if pr and m.get("closed"):
                    prices = pr
                    fp = [float(x) for x in pr]
                    if max(fp) > 0.99:
                        official = m["outcomes"][fp.index(max(fp))]
                        break
            except Exception:
                pass
            await asyncio.sleep(30)
        used = "official" if official else ("provisional" if prov else "none")
        self.w.write("windows", (clock.now(), win.slug, win.start, win.end, win.m["question"], win.m["condition_id"],
                                 win.m["up_token"], win.m["down_token"], win.m["fee_type"], win.m["taker_base_fee"],
                                 win.ptb, win.ptb_chainlink, end_tw, self.cl.get(win.end), prov, official,
                                 json.dumps(prices) if prices else None, used))
        if prov and official and prov != official:
            log("pm", f"{win.slug}: предварительный исход {prov} != официальный {official}")
        win.resolved = True
        if self.paper is not None and not prov and official:
            self.paper.settle(win, official, "official")
        if self.maker is not None and not prov and official:
            self.maker.settle(win, official)

    # ---------------------------------------------------------------- RTDS (Chainlink и др.)
    async def rtds(self, feed: str):
        topic, sym = RTDS_FEEDS[feed]
        sub = json.dumps({"action": "subscribe", "subscriptions": [{
            "topic": topic, "type": "update", "filters": json.dumps({"symbol": sym}, separators=(",", ":"))}]})
        target = {"twap60": self.tw, "chainlink": self.cl}.get(feed)
        while True:
            try:
                async with websockets.connect(self.cfg.rtds_ws, ping_interval=None, max_queue=4096) as ws:
                    await ws.send(sub)
                    log("pm", f"RTDS[{feed}] подключён")
                    pinger = asyncio.create_task(self._text_ping(ws, 5))
                    try:
                        async for raw in iter_ws(ws, 20.0):  # тишина 20 с = поток завис, переподключаемся
                            recv = clock.now()
                            if not raw:
                                continue
                            try:
                                d = loads(raw)
                            except Exception:
                                continue
                            p = d.get("payload")
                            if not isinstance(p, dict):
                                continue
                            items = p["data"] if "data" in p else [p]
                            for it in items:
                                try:
                                    v = float(it["value"])
                                    tms = int(it["timestamp"])
                                except (KeyError, TypeError, ValueError):
                                    continue
                                self.n_rtds += 1
                                self.w.write("rtds", (ms(recv), RTDS_SHORT[feed], tms, v))
                                sec = tms // 1000
                                if target is not None:
                                    target[sec] = v
                                    if sec % 600 == 0 and len(target) > 4000:  # храним только последний час
                                        for k in [k for k in target if k < sec - 3600]:
                                            target.pop(k, None)
                                if feed == "chainlink":
                                    self._update_basis(sec, v)
                                elif feed == "rtds_binance" and self.cfg.paper_btc_source == "rtds":
                                    self._on_src("rtds", recv, v)
                    finally:
                        pinger.cancel()
            except Exception as ex:
                log("pm", f"RTDS[{feed}] разорван ({ex!r}), переподключение через 2 с")
                self.w.write("events_pm", (clock.now(), "pm", f"rtds_{feed}", "disconnected", repr(ex)[:300]))
                await asyncio.sleep(2)

    def _update_basis(self, sec: int, cl_value: float):
        bn = self.bn_sec.get(sec)
        if bn is None:
            return
        x = cl_value - bn
        self.basis = x if self.basis is None else self.basis + 0.05 * (x - self.basis)

    # ---------------------------------------------------------------- Binance для бумажной торговли
    def _alive(self, name: str, recv: float):
        s = self.src.setdefault(name, {"px": None, "recv": 0.0, "alive": 0.0})
        s["alive"] = recv
        if name == self.cfg.paper_btc_source:
            self.bn_alive = recv

    def _on_src(self, name: str, recv: float, px: float):
        """Новая цена от источника name. Основной источник идёт в _on_btc (волатильность,
        базис, оценка сигналов), остальные только обновляют свою цену и тоже запускают оценку."""
        s = self.src.setdefault(name, {"px": None, "recv": 0.0, "alive": 0.0})
        s["px"], s["recv"], s["alive"] = px, recv, recv
        h = self.mom_hist.get(name)
        if h is None:
            h = self.mom_hist[name] = deque(maxlen=5000)
        h.append((recv, px))
        while h and recv - h[0][0] > 5.0:
            h.popleft()
        sg = self.mom_sigma.get(name)
        if sg is None:
            sg = self.mom_sigma[name] = RollingSigma(300, 0.0)
        sg.update(recv, px)
        if name == self.cfg.paper_btc_source:
            self._on_btc(recv, px)
        elif self.paper is not None:
            self.paper.evaluate(recv, name)
        if self.maker is not None:
            self.maker.requote(recv)

    async def bybit_lite(self):
        """Bybit BTCUSDT (бессрочный). Цена - середина лучших bid/ask из orderbook.1 (верх книги
        меняется раньше сделок), а если верх книги неизвестен или "перекрещен" - последняя сделка.
        Книга глубины 1: в каждом сообщении на стороне максимум один живой уровень, его и берём;
        запись с объёмом 0 означает, что уровень снят."""
        url = "wss://stream.bybit.com/v5/public/linear"
        sub = json.dumps({"op": "subscribe", "args": ["orderbook.1.BTCUSDT", "publicTrade.BTCUSDT"]})
        while True:
            last = None
            bid = ask = trade_px = None
            try:
                async with websockets.connect(url, ping_interval=None, max_queue=4096, compression=None) as ws:
                    await ws.send(sub)
                    log("pm", "Bybit (для бумажной торговли) подключён")
                    self.w.write("events_pm", (clock.now(), "pm", "bybit", "connected", ""))
                    pinger = asyncio.create_task(self._json_ping(ws, 10))
                    try:
                        async for raw in iter_ws(ws, 15.0):
                            recv = clock.now()
                            self._alive("bybit", recv)
                            d = loads(raw)
                            topic = str(d.get("topic", ""))
                            if topic.startswith("orderbook.1"):
                                self.by_msgs["book"] += 1
                                x = d.get("data") or {}
                                snap = d.get("type") == "snapshot"
                                for side in ("b", "a"):
                                    lv = x.get(side) or []
                                    live = [float(p_) for p_, q_ in lv if float(q_) > 0]
                                    gone = {float(p_) for p_, q_ in lv if float(q_) == 0}
                                    cur = bid if side == "b" else ask
                                    if live:
                                        cur = max(live) if side == "b" else min(live)
                                    elif snap or (cur is not None and cur in gone):
                                        cur = None
                                    if side == "b":
                                        bid = cur
                                    else:
                                        ask = cur
                                ets = d.get("cts") or d.get("ts")
                                if ets:
                                    lat = recv * 1000 - float(ets) + self.offset_ms
                                    self.src_lat["bybit"].add(lat)
                                    if self.cfg.paper_btc_source == "bybit":
                                        self.bn_lat.add(lat)
                            elif topic.startswith("publicTrade"):
                                self.by_msgs["trade"] += 1
                                data = d.get("data") or []
                                if data:
                                    trade_px = float(max(data, key=lambda z: z["T"])["p"])
                            else:
                                self.by_msgs["other"] += 1
                                continue
                            if bid is not None and ask is not None and ask > bid:
                                px = (bid + ask) / 2
                            else:
                                px = trade_px
                            if px is None or px == last:
                                continue
                            last = px
                            self._on_src("bybit", recv, px)
                    finally:
                        pinger.cancel()
            except Exception as ex:
                log("pm", f"Bybit разорван ({ex!r}), переподключение через 2 с")
                self.w.write("events_pm", (clock.now(), "pm", "bybit", "disconnected", repr(ex)[:300]))
                await asyncio.sleep(2)

    @staticmethod
    async def _json_ping(ws, every):
        try:
            while True:
                await asyncio.sleep(every)
                await ws.send(json.dumps({"op": "ping"}))
        except Exception:
            pass

    def _on_btc(self, recv: float, mid: float):
        self.bn_mid = mid
        self.bn_recv = recv
        self.bn_alive = recv
        self.n_bn += 1
        sec = int(recv + self.offset_ms / 1000)  # секунда по часам сервера
        self.bn_sec[sec] = mid
        if len(self.bn_sec) > 900:
            for k in [k for k in self.bn_sec if k < sec - 600]:
                self.bn_sec.pop(k, None)
        self.sigma.update(recv, mid)
        if self.paper is not None:
            self.paper.evaluate(recv, "btc")

    async def coinbase_lite(self):
        """Coinbase BTC-USD как быстрый источник цены для бумажной торговли.
        ticker - на каждую сделку (с лучшими bid/ask), heartbeat - раз в секунду (признак живого канала)."""
        from datetime import datetime
        sub = json.dumps({"type": "subscribe", "product_ids": ["BTC-USD"], "channels": ["ticker", "heartbeat"]})
        last = None
        while True:
            try:
                async with websockets.connect(self.cfg.coinbase_ws, ping_interval=10, ping_timeout=10,
                                              max_queue=4096, compression=None) as ws:
                    await ws.send(sub)
                    log("pm", "Coinbase (для бумажной торговли) подключён")
                    self.w.write("events_pm", (clock.now(), "pm", "coinbase", "connected", ""))
                    async for raw in iter_ws(ws, 5.0):
                        recv = clock.now()
                        self._alive("coinbase", recv)
                        x = loads(raw)
                        if x.get("type") != "ticker":
                            continue
                        try:
                            tms = datetime.fromisoformat(x["time"].replace("Z", "+00:00")).timestamp() * 1000
                            self.src_lat["coinbase"].add(recv * 1000 - tms + self.offset_ms)
                            if self.cfg.paper_btc_source == "coinbase":
                                self.bn_lat.add(recv * 1000 - tms + self.offset_ms)
                        except Exception:
                            pass
                        bb, ba = x.get("best_bid"), x.get("best_ask")
                        mid = (float(bb) + float(ba)) / 2 if bb and ba else float(x["price"])
                        if mid == last:
                            continue
                        last = mid
                        self._on_src("coinbase", recv, mid)
            except Exception as ex:
                log("pm", f"Coinbase разорван ({ex!r}), переподключение через 2 с")
                self.w.write("events_pm", (clock.now(), "pm", "coinbase", "disconnected", repr(ex)[:300]))
                await asyncio.sleep(2)

    def momentum_sigma(self, name: str):
        """Волатильность источника ($/sqrt(с)) за последние 5 минут; None - ещё не набралась."""
        if name == "binance_any":
            name = "binance_fut"
        sg = self.mom_sigma.get(name)
        return sg.sigma() if sg is not None and sg.warm else None

    def momentum_move(self, name: str, window_ms: int):
        """Изменение цены источника за последние window_ms мс (по времени приёма); None - нет данных."""
        if name == "binance_any":
            ms = [m for m in (self.momentum_move("binance", window_ms), self.momentum_move("binance_fut", window_ms))
                  if m is not None]
            return max(ms, key=abs) if ms else None
        h = self.mom_hist.get(name)
        if not h or len(h) < 2:
            return None
        t_now, p_now = h[-1]
        t0 = t_now - window_ms / 1000
        if h[0][0] > t0:            # истории на всё окно ещё нет
            return None
        p0 = None
        for t, px in reversed(h):   # последняя цена не позже t0
            if t <= t0:
                p0 = px
                break
        return None if p0 is None else p_now - p0

    async def binance_fut_book_lite(self):
        """Верх книги фьючерса Binance с объёмами -> дисбаланс (bid_qty-ask_qty)/(bid_qty+ask_qty).
        Сотни сообщений в секунду: оценку сигналов запускаем только при сильном дисбалансе."""
        urls = self.cfg.paper_binance_fut_book_urls
        i = 0
        while True:
            url = urls[i % len(urls)]
            got = 0
            try:
                async with websockets.connect(url, ping_interval=10, ping_timeout=10, max_queue=8192,
                                              compression=None) as ws:
                    log("pm", f"книга фьючерса Binance (дисбаланс) подключена: {url}")
                    self.w.write("events_pm", (clock.now(), "pm", "binance_fut_book", "connected", url))
                    async for raw in iter_ws(ws, 30.0):
                        recv = clock.now()
                        x = loads(raw)
                        x = x.get("data") or x
                        if x.get("e") != "bookTicker" or "B" not in x:
                            continue
                        got += 1
                        bq, aq = float(x["B"]), float(x["A"])
                        if bq + aq <= 0:
                            continue
                        if "T" in x:
                            self.src_lat["binance_fut_book"].add(recv * 1000 - x["T"] + self.offset_ms)
                        prev = self.fut_qi
                        self.fut_qi = qi = (bq - aq) / (bq + aq)
                        self.fut_qi_prev = prev
                        s = self.src.setdefault("binance_fut_book", {"px": None, "recv": 0.0, "alive": 0.0})
                        s["px"] = (float(x["b"]) + float(x["a"])) / 2
                        s["recv"] = s["alive"] = recv
                        # оценка только в момент, когда дисбаланс ПЕРЕСЁК какой-то из порогов (или сменил сторону),
                        # а не на каждом сообщении, пока он остаётся высоким
                        if self.paper is not None and abs(qi) >= self.qi_eval_min and (
                                prev is None or (prev > 0) != (qi > 0) or
                                any(abs(prev) < th <= abs(qi) for th in self.qi_thresholds)):
                            self.paper.evaluate(recv, "binance_fut_book")
            except Exception as ex:
                log("pm", f"книга фьючерса Binance разорвана ({ex!r})")
                self.w.write("events_pm", (clock.now(), "pm", "binance_fut_book", "disconnected", repr(ex)[:300]))
            if got == 0:
                i += 1
            await asyncio.sleep(2)

    async def binance_fut_lite(self):
        """Фьючерс Binance BTCUSDT: цена последней сделки (aggTrade) и её задержка до нас."""
        url = self.cfg.paper_binance_fut_url
        while True:
            last = None
            try:
                async with websockets.connect(url, ping_interval=10, ping_timeout=10, max_queue=4096,
                                              compression=None) as ws:
                    log("pm", "фьючерс Binance (моментум) подключён")
                    self.w.write("events_pm", (clock.now(), "pm", "binance_fut", "connected", ""))
                    async for raw in iter_ws(ws, 15.0):
                        recv = clock.now()
                        self._alive("binance_fut", recv)
                        x = loads(raw)
                        x = x.get("data") or x
                        if x.get("e") == "aggTrade":
                            self.src_lat["binance_fut"].add(recv * 1000 - x["T"] + self.offset_ms)
                            px = float(x["p"])
                            if px == last:
                                continue
                            last = px
                            self._on_src("binance_fut", recv, px)
            except Exception as ex:
                log("pm", f"фьючерс Binance разорван ({ex!r}), переподключение через 2 с")
                self.w.write("events_pm", (clock.now(), "pm", "binance_fut", "disconnected", repr(ex)[:300]))
                await asyncio.sleep(2)

    async def binance_lite(self):
        url, names = binance_url(self.cfg)
        if self.cfg.paper_binance:
            url, names = self.cfg.paper_binance_url, ["aggTrade", "bookTicker"]
        use_trades = "bookTicker" not in names and "depth5" not in names  # цена только по сделкам
        last = None
        while True:
            try:
                async with websockets.connect(url, ping_interval=10, ping_timeout=10, max_queue=4096,
                                              compression=None) as ws:
                    log("pm", "Binance (для бумажной торговли) подключён")
                    self.w.write("events_pm", (clock.now(), "pm", "binance", "connected", ""))
                    async for raw in iter_ws(ws, 5.0):
                        recv = clock.now()
                        self._alive("binance", recv)
                        x = loads(raw)
                        x = x.get("data") or x
                        if x.get("e") == "aggTrade":
                            self.bn_lat.add(recv * 1000 - x["E"] + self.offset_ms)
                            if use_trades:
                                self._on_src("binance", recv, float(x["p"]))
                            continue
                        q = binance_bbo(x)
                        if q is not None:
                            bbo = (q[1], q[3])
                            if bbo == last:
                                continue
                            last = bbo
                            self._on_src("binance", recv, (float(q[1]) + float(q[3])) / 2)
            except Exception as ex:
                log("pm", f"Binance разорван ({ex!r}), переподключение через 2 с")
                self.w.write("events_pm", (clock.now(), "pm", "binance", "disconnected", repr(ex)[:300]))
                await asyncio.sleep(2)

    # ---------------------------------------------------------------- задержка до CLOB (без ключей)
    def _rtt_once(self, endpoint: str, token: str | None):
        s = self._http
        t0 = time.perf_counter()
        if endpoint == "time":
            r = s.get("https://clob.polymarket.com/time", timeout=5)
        elif endpoint == "book":
            r = s.get("https://clob.polymarket.com/book", params={"token_id": token}, timeout=5)
        else:  # пустой POST без ключей: сервер отклонит, но путь запроса тот же, что у ордера
            r = s.post("https://clob.polymarket.com/order", json={}, timeout=5)
        return r.status_code, (time.perf_counter() - t0) * 1000, r.text[:200]

    async def rtt_loop(self):
        import requests
        self._http = requests.Session()
        self._http.headers["User-Agent"] = "Mozilla/5.0"
        i = 0
        warned = False
        while True:
            await asyncio.sleep(5)
            i += 1
            win = self.current_window(clock.now())
            eps = ["time"] + (["book"] if win else []) + (["order"] if i % 6 == 0 else [])
            for ep in eps:
                try:
                    st, rtt, txt = await asyncio.to_thread(self._rtt_once, ep, win.m["up_token"] if win else None)
                except Exception as ex:
                    st, rtt, txt = -1, None, repr(ex)
                self.w.write("pm_rtt", (ms(clock.now()), ep, st, round(rtt, 1) if rtt else None))
                if ep == "book" and st == 200:
                    self.rtt_q.add(rtt)
                if ep == "order" and st == 403 and not warned:
                    warned = True
                    log("pm", f"ВНИМАНИЕ: сервер ордеров Polymarket ответил 403: {txt[:120]}")

    # ---------------------------------------------------------------- часы и статус
    async def clock_loop(self):
        while True:
            try:
                src, off, rtt = await asyncio.to_thread(probe_clock, self.cfg.binance_rest)
                self.offset_ms = off
                self.w.write("clock_pm", (clock.now(), src, round(off, 2), round(rtt, 2)))
            except Exception as ex:
                log("pm", f"замер часов не удался: {ex!r}")
            await asyncio.sleep(60)

    @staticmethod
    def rss_mb():
        try:
            with open("/proc/self/status") as f:
                for line in f:
                    if line.startswith("VmRSS:"):
                        return int(line.split()[1]) / 1024
        except Exception:
            return None

    async def status(self):
        while True:
            await asyncio.sleep(self.cfg.status_every_sec)
            lag = self.lag.snapshot_reset()
            row = (clock.now(), self.n_clob, self.clob_lat.q(0.5), self.clob_lat.q(0.9), self.n_top, self.n_trades,
                   self.n_rtds, self.n_bn, self.bn_lat.q(0.5), lag[0], lag[1], lag[2])
            self.w.write("health_pm", row)
            win = self.current_window(clock.now())
            wtxt = "нет окна"
            if win is not None:
                u, d = win.books["Up"], win.books["Down"]
                wtxt = (f"T-{win.end - clock.now():5.1f}s Up {fnum(u.bb, '.2f')}/{fnum(u.ba, '.2f')} "
                        f"Down {fnum(d.bb, '.2f')}/{fnum(d.ba, '.2f')} ptb={fnum(win.ptb, '.1f')}")
            log("pm", f"{wtxt} | CLOB {self.n_clob} сообщ., задержка p50/p90={fnum(row[2])}/{fnum(row[3])} мс | "
                      f"BTC[{self.cfg.paper_btc_source}]={fnum(self.bn_mid, '.1f')} ({self.n_bn} обн., задержка p50 {fnum(row[8])} мс, "
                      f"тишина {1000 * (clock.now() - self.bn_alive):.0f} мс; Bybit сообщ.: книга {self.by_msgs['book']}, "
                      f"сделки {self.by_msgs['trade']}) "
                      + " ".join(f"{k}={fnum((self.src.get(k) or {}).get('px'), '.1f')} p50={fnum(q.q(0.5))}мс"
                                 for k, q in self.src_lat.items() if k != self.cfg.paper_btc_source) + " "
                      f"σ={self.sigma.sigma():.2f}{'' if self.sigma.warm else ' (разогрев)'} "
                      f"базис={fnum(self.basis, '+.1f')} | "
                      f"HTTPS до CLOB p50={fnum(self.rtt_q.q(0.5))} мс | lag loop p99/max={fnum(lag[1])}/{fnum(lag[2])} мс")
            self.n_clob = self.n_top = self.n_trades = self.n_rtds = self.n_bn = 0
            self.clob_lat.clear()
            self.bn_lat.clear()
            for q in self.src_lat.values():
                q.clear()
            self.by_msgs = {"book": 0, "trade": 0, "other": 0}

    async def main(self):
        tasks = [self.windows_loop(), self.depth_loop(), self.top_flush_loop(), self.clock_loop(), self.status(), self.lag.run(),
                 self.rtt_loop()]
        tasks += [self.rtds(f) for f in RTDS_FEEDS]
        if self.cfg.paper:
            tasks += [self.bybit_lite(), self.coinbase_lite()]
            if self.cfg.paper_btc_source == "binance" or self.cfg.paper_binance:
                tasks.append(self.binance_lite())
            if self.cfg.paper_binance_fut:
                tasks.append(self.binance_fut_lite())
            if self.cfg.paper_binance_fut_book:
                tasks.append(self.binance_fut_book_lite())
        await asyncio.gather(*tasks)


def run(cfg):
    p = PM(cfg)
    try:
        asyncio.run(p.main())
    except KeyboardInterrupt:
        pass
    finally:
        if p.paper is not None:
            p.paper.print_summary()
        p.w.close()
        flush_console()
