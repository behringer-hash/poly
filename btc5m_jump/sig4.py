"""Стратегия 4 (claude/strategy_4_signal_maker.md): мейкер по сигналу модели.

Каждые 100 мс считаем прогноз модели (sig4_model, деревья из models/*.npz) - ход mid Up за ближайшие 3 с, центов -
по признакам на точке сетки t = (сейчас по часам сервера - sig4_lat_ms), как в симуляции (mm_map, варианты F*):
  * вход на сторону X (Up при прогнозе > 0, Down - при < 0): прогноз хода X >= sig4_thr_c (5 ц) И свежий ход BTC
    за 0,3 с в пользу X хотя бы на одной бирже >= sig4_fresh_usd ($2); время окна sig4_t_min..sig4_t_max с;
    на стороне нет своей заявки; нет паузы после хода BTC против;
  * заявка - через MakerTrader (live_maker.py): только на постановку (post-only), лучший bid + 1 ц при спреде >= 2 ц,
    иначе лучший bid; живёт maker_life_sec (1,5 с);
  * досрочное снятие: прогноз хода стороны < sig4_keep_c (1 ц); лучший bid ушёл выше цены заявки на sig4_far_ticks;
    ход BTC >= sig4_adverse_usd ($3) за sig4_adverse_ms (300 мс) против стороны на любой бирже - сразу по сделке,
    плюс пауза sig4_cooldown_sec (1 с) на новые заявки этой стороны;
  * позиция держится до исхода окна.
Источники: книга и сделки Polymarket и Chainlink - из движка pm.py (перехват записи pm_top / pm_trades / rtds),
фьючерс Binance (aggTrade), Bybit (publicTrade), Coinbase (ticker) - свои потоки, время биржи каждой сделки.
"""
from __future__ import annotations

import asyncio
import json
import math
import os
from collections import deque
from datetime import datetime

import websockets

from common import Quantiles, clock, emit, iter_ws, loads, log, window_start
from sig4_model import T0, T1, GridSeries, Trees, WinData, features_at, grid_t

SIG4_SCHEMAS = {
    "sig4_signals": ["sid", "t", "w", "t_grid", "side", "score", "fresh", "src", "bid", "ask", "bid_sz", "ask_sz",
                     "T_left", "book_lag_ms", "calc_ms", "action"],
    "sig4_cancels": ["t", "w", "side", "sid", "reason", "score", "detail"],
    "sig4_scores": ["t", "w", "t_grid", "score", "fresh_up", "fresh_dn", "mid", "fair", "dk", "calc_ms"],
    "sig4_feeds": ["t", "src", "event", "info"],
}

SIG4_DEFAULTS = {
    "sig4_model": "models/sig3s_v2.npz",   # деревья модели (относительно папки бота)
    "sig4_thr_c": 5.0,                     # вход: прогноз хода стороны, ц
    "sig4_keep_c": 1.0,                    # снять заявку, если прогноз стороны стал ниже, ц
    "sig4_fresh_usd": 2.0,                 # вход: ход BTC за 0,3 с в пользу стороны хотя бы на одной бирже, $ (0 - не требовать)
    "sig4_adverse_usd": 3.0,               # снять заявки стороны: ход BTC против за sig4_adverse_ms, $
    "sig4_adverse_ms": 300.0,
    "sig4_cooldown_sec": 1.0,              # пауза новых заявок стороны после хода против
    "sig4_lat_ms": 150.0,                  # признаки - на момент «сейчас по серверу - lat» (данные до него уже пришли)
    "sig4_tick_ms": 100.0,
    "sig4_t_min": 12.0,                    # секунды от начала окна: от
    "sig4_t_max": 285.0,                   # до
    "sig4_far_ticks": 2,                   # снять, если лучший bid стороны выше цены заявки на столько центов
    "sig4_max_book_lag_ms": 1000.0,        # книга отстаёт от сервера больше - новых заявок нет
    "sig4_max_feed_age_sec": 5.0,          # фьючерс Binance молчит дольше - новых заявок нет
    "sig4_log_abs_c": 3.0,                 # в sig4_scores - все точки с |прогнозом| от N ц (и раз в секунду - любая)
    "sig4_pulse_sec": 5,                   # строка ПУЛЬС раз в N секунд (0 - нет)
    "sig4_urls_bnf": ["wss://fstream.binance.com/market/stream?streams=btcusdt@aggTrade",
                      "wss://fstream.binance.com/stream?streams=btcusdt@aggTrade",
                      "wss://fstream.binance.com/ws/btcusdt@aggTrade"],
    "sig4_url_bybit": "wss://stream.bybit.com/v5/public/linear",
    "sig4_url_coinbase": "wss://ws-feed.exchange.coinbase.com",
}
SRC_NAME = {"bnf": "фьючерс Binance", "by": "Bybit", "cb": "Coinbase"}
CY, X = "\033[96m", "\033[0m"


class Sig4Trigger:
    def __init__(self, lcfg: dict, pm, writer, trader, trees: Trees | None = None):
        self.c = {**SIG4_DEFAULTS, **{k: v for k, v in lcfg.items() if k.startswith("sig4_")}}
        self.variant = lcfg["variant"]
        self.pm, self.w, self.trader = pm, writer, trader
        if trees is None:
            path = self.c["sig4_model"]
            if not os.path.isabs(path):
                path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
            trees = Trees(path)
        self.trees = trees
        self.g = {c: GridSeries() for c in ("bnf", "by", "cb", "cl")}
        self.recent = {c: deque() for c in ("bnf", "by", "cb")}          # (время биржи, цена) за ~1 с - ход против
        self.lat = {c: Quantiles() for c in ("bnf", "by", "cb")}
        self.alive = {c: 0.0 for c in ("bnf", "by", "cb")}
        self.n = {c: 0 for c in ("bnf", "by", "cb")}
        self.wins: dict[int, WinData] = {}
        self.block: dict[tuple, float] = {}                            # (окно, сторона) -> до какого времени пауза
        self.sid = 0
        self.last_g = None
        self.last_log_sec = None
        self.last = dict(w=None, t=None, score=None, up=None, dn=None, mid=None, calc_ms=None)
        self.why = "запуск"              # почему сейчас нет прогноза (для пульса)
        self.calc = Quantiles()
        self.stats = dict(ticks=0, signals=0, skip_fresh=0, skip_block=0, skip_open=0, skip_feed=0, skip_book=0,
                          skip_history=0, cancel_keep=0, cancel_far=0, cancel_adverse=0, adverse=0)
        self.t_start = clock.now()          # окно торгуем, только если история BTC есть с T-20 с (как при обучении)

    def m(self, k):
        return self.c[k]

    # ------------------------------------------------------------------ данные движка (перехват записи pm.py)
    def on_row(self, stream: str, r: tuple) -> None:
        try:
            if stream == "pm_top":                    # recv_ms, d, w, o, bid, bid_sz, ask, ask_sz, cid
                if r[3] == "U" and r[1] is not None:
                    self._wd(int(r[2])).add_top(float(r[0]) - float(r[1]), r[4], r[6], r[5], r[7])
            elif stream == "pm_trades":               # recv_ms, server_ts, w, o, side, price, size, fee, tx
                sts, o, side, price, size = r[1], r[3], r[4], r[5], r[6]
                if sts is None or price is None or size is None:
                    return
                size = float(size)
                if size <= 0:
                    return
                self._wd(int(r[2])).add_trade(float(sts), size if (o == "U") == (side == "B") else -size)
            elif stream == "rtds":                    # recv_ms, feed, ts_ms, value
                if r[1] == "cl":
                    self.g["cl"].add(float(r[2]), float(r[3]))
        except (TypeError, ValueError):
            pass

    def _wd(self, w: int) -> WinData:
        wd = self.wins.get(w)
        if wd is None:
            wd = self.wins[w] = WinData(w)
            for k in [k for k in self.wins if k < w - 900]:
                self.wins.pop(k, None)
        return wd

    # ------------------------------------------------------------------ сделки бирж
    def on_btc(self, c: str, T: float, px: float, recv: float) -> None:
        self.g[c].add(T, px)
        self.n[c] += 1
        self.alive[c] = recv
        self.lat[c].add(recv * 1000 - T + self.pm.offset_ms)
        h = self.recent[c]
        h.append((T, px))
        while h and h[0][0] < T - 1500:
            h.popleft()
        p0 = None
        lim = T - float(self.m("sig4_adverse_ms"))
        for t_, p_ in reversed(h):
            if t_ <= lim:
                p0 = p_
                break
        if p0 is None:
            return
        dS = px - p0
        if abs(dS) >= float(self.m("sig4_adverse_usd")):
            self.on_adverse("Down" if dS > 0 else "Up", c, dS)

    def on_adverse(self, hurt: str, src: str, dS: float) -> None:
        """Ход BTC против стороны hurt: снять её заявки в текущем окне и не ставить новые sig4_cooldown_sec."""
        now = clock.now()
        w = window_start(now + self.pm.offset_ms / 1000.0)
        self.block[(w, hurt)] = now + float(self.m("sig4_cooldown_sec"))
        self.stats["adverse"] += 1
        for e in self._open(w, hurt):
            if self.trader.cancel_early(e["sid"], f"ход BTC {dS:+.1f}$ ({SRC_NAME[src]})"):
                self.stats["cancel_adverse"] += 1
                self.w.write("sig4_cancels", (round(now, 4), w, hurt, e["sid"], "adverse", None, f"{src} {dS:+.2f}"))

    def _open(self, w: int, side: str):
        return [e for e in list(self.trader.open.values())
                if e.get("start") == w and e.get("outcome") == side and not e.get("expired")]

    async def _feed(self, c: str, urls: list[str], sub: str | None, parse, ping: str | None):
        i = 0
        while True:
            url = urls[i % len(urls)]
            got = 0
            pinger = None
            try:
                async with websockets.connect(url, ping_interval=10 if ping is None else None, ping_timeout=10,
                                              max_queue=8192, compression=None) as ws:
                    if sub:
                        await ws.send(sub)
                    log("sig4", f"{SRC_NAME[c]} подключён: {url}")
                    self.w.write("sig4_feeds", (clock.now(), c, "connected", url))
                    if ping:
                        pinger = asyncio.create_task(self._pinger(ws, ping))
                    async for raw in iter_ws(ws, 15.0):
                        recv = clock.now()
                        if raw in ("pong", "PONG") or not raw:
                            continue
                        try:
                            d = loads(raw)
                        except Exception:
                            continue
                        for T, px in parse(d):
                            got += 1
                            self.on_btc(c, T, px, recv)
            except Exception as ex:
                log("sig4", f"{SRC_NAME[c]} разорван ({ex!r})"[:200])
                self.w.write("sig4_feeds", (clock.now(), c, "disconnected", repr(ex)[:300]))
            finally:
                if pinger:
                    pinger.cancel()
            if got == 0:
                i += 1
            await asyncio.sleep(1)

    @staticmethod
    async def _pinger(ws, msg):
        try:
            while True:
                await asyncio.sleep(10)
                await ws.send(msg)
        except Exception:
            pass

    @staticmethod
    def parse_bnf(d):
        x = d.get("data") or d
        if x.get("e") != "aggTrade":
            return []
        return [(float(x["T"]), float(x["p"]))]

    @staticmethod
    def parse_bybit(d):
        if not str(d.get("topic", "")).startswith("publicTrade"):
            return []
        return [(float(it["T"]), float(it["p"])) for it in d.get("data") or []]

    @staticmethod
    def parse_coinbase(d):
        if d.get("type") != "ticker" or not d.get("time") or d.get("price") is None:
            return []
        tms = int(datetime.fromisoformat(d["time"].replace("Z", "+00:00")).timestamp() * 1000)
        return [(float(tms), float(d["price"]))]

    # ------------------------------------------------------------------ решение раз в 100 мс
    def tick(self, now: float | None = None):
        """Один шаг: признаки на точке сетки, прогноз, снятия и новые заявки. Возвращает прогноз (или None)."""
        now = clock.now() if now is None else now
        c = self.c
        srv = now * 1000 + self.pm.offset_ms
        g_ms = math.floor((srv - float(c["sig4_lat_ms"])) / 100.0) * 100.0
        if g_ms == self.last_g:
            return None
        self.last_g = g_ms
        w = window_start(g_ms / 1000.0)
        t = grid_t((g_ms - w * 1000.0) / 1000.0)
        for gs in self.g.values():
            gs.start_window(w)
            gs.close_upto(g_ms)
        if t < T0 - 1e-9 or t > T1 + 1e-9:
            self.why = "начало окна"
            return None
        win = self.pm.windows.get(w)
        wd = self.wins.get(w)
        if win is None or wd is None or not win.ready():
            self.why = "нет книги окна"
            return None
        if win.ptb is None:
            self.why = "нет price to beat окна (бот запущен посреди окна - прогноз со следующего)"
            return None
        self.why = ""
        self.stats["ticks"] += 1
        t_calc = clock.now()
        row, up, dn = features_at(t, wd, float(win.ptb), {k: self.g[k] for k in ("bnf", "by", "cb")}, self.g["cl"])
        p = self.trees.predict_row(row)
        calc_ms = (clock.now() - t_calc) * 1000
        self.calc.add(calc_ms)
        self.last = dict(w=w, t=t, score=p, up=up, dn=dn, mid=row[0], calc_ms=calc_ms)
        sec = int(g_ms // 1000)
        if abs(p) >= float(c["sig4_log_abs_c"]) or sec != self.last_log_sec:
            self.last_log_sec = sec
            self.w.write("sig4_scores", (round(now, 4), w, t, round(p, 3), _r(up), _r(dn), _r(row[0], 4), _r(row[5], 4),
                                         _r(row[6]), round(calc_ms, 2)))
        for side in ("Up", "Down"):
            self._side(now, win, w, t, side, p if side == "Up" else -p, up if side == "Up" else dn, calc_ms)
        return p

    def _side(self, now, win, w, t, side, sx, fresh, calc_ms):
        c = self.c
        b = win.books[side]
        opn = self._open(w, side)
        for e in opn:                                      # досрочное снятие
            why = None
            if sx < float(c["sig4_keep_c"]):
                why, key = f"прогноз {sx:+.1f} ц", "cancel_keep"
            elif b.bb is not None and b.bb - e["q"] >= 0.01 * float(c["sig4_far_ticks"]) - 1e-9:
                why, key = f"bid ушёл вверх до {b.bb:.2f}", "cancel_far"
            if why and self.trader.cancel_early(e["sid"], why):
                self.stats[key] += 1
                self.w.write("sig4_cancels", (round(now, 4), w, side, e["sid"], key, round(sx, 3), why))
        if sx < float(c["sig4_thr_c"]):
            return
        if not (float(c["sig4_t_min"]) <= t <= float(c["sig4_t_max"])):
            return
        if float(c["sig4_fresh_usd"]) > 0 and not (fresh == fresh and fresh >= float(c["sig4_fresh_usd"])):
            self.stats["skip_fresh"] += 1
            return
        if opn:
            self.stats["skip_open"] += 1
            return
        if self.t_start + self.pm.offset_ms / 1000.0 > w - 20:
            self.stats["skip_history"] += 1
            return
        if now < self.block.get((w, side), 0.0):
            self.stats["skip_block"] += 1
            return
        if now - self.alive["bnf"] > float(c["sig4_max_feed_age_sec"]):
            self.stats["skip_feed"] += 1
            return
        if win.book_lag_ms is not None and win.book_lag_ms > float(c["sig4_max_book_lag_ms"]):
            self.stats["skip_book"] += 1
            return
        if b.bb is None or b.ba is None:
            self.stats["skip_book"] += 1
            return
        self.sid += 1
        self.stats["signals"] += 1
        src = max(("bnf", "by", "cb"), key=lambda k: self._fresh_src(k, side))
        sig = dict(sid=self.sid, t=now, slug=win.slug, start=w, T=win.end - now, outcome=side, variant=self.variant,
                   edge=sx / 100.0, move=fresh, anchor_age=None, price_mode="improve", tier="sig4", src=SRC_NAME[src],
                   win_ms=int(c["sig4_adverse_ms"]))
        self.w.write("sig4_signals", (self.sid, round(now, 4), w, t, side, round(sx, 3), _r(fresh), src, b.bb, b.ba,
                                      b.bids.get(b.bb), b.asks.get(b.ba), round(win.end - now, 2),
                                      round(win.book_lag_ms, 1) if win.book_lag_ms is not None else None,
                                      round(calc_ms, 2), "signal"))
        if self.trader is not None:
            self.trader.on_signal(sig)

    def _fresh_src(self, k, side):
        g = self.g[k]
        if g.vals is None or g.k < 4:
            return -1e9
        d = g.vals[g.k - 1] - g.vals[g.k - 4]
        d = d if side == "Up" else -d
        return d if d == d else -1e9

    async def tick_loop(self):
        step = float(self.m("sig4_tick_ms")) / 1000.0
        while True:
            await asyncio.sleep(step - (clock.now() % step) + 0.002)
            try:
                self.tick()
            except Exception as ex:                    # шаг не должен ронять бота
                log("sig4", f"ошибка шага: {ex!r}"[:200])

    async def pulse_loop(self):
        every = float(self.m("sig4_pulse_sec") or 0)
        if every <= 0:
            return
        while True:
            await asyncio.sleep(every)
            L, tr = self.last, self.trader
            win = self.pm.current_window(clock.now())
            book = ""
            if win is not None and win.ready():
                u = win.books["Up"]
                book = f"Up {u.bb}/{u.ba} | "
            ages = " ".join(f"{k} " + (f"{clock.now() - self.alive[k]:.1f}с назад" if self.alive[k] else "нет")
                            for k in ("bnf", "by", "cb"))
            if self.why or L["score"] is None:
                head = f"прогноза нет: {self.why or 'ждём данные'}"
            else:
                head = (f"t={L['t']:.1f}с | прогноз Up {L['score']:+.1f} ц (BTC за 0,3 с: вверх {_f(L['up'])}$, "
                        f"вниз {_f(L['dn'])}$) | расчёт {L['calc_ms'] or 0:.1f} мс")
            emit(f"\033[90m{datetime.now().strftime('%H:%M:%S')} ПУЛЬС {book}{head} | "
                 f"последние сделки: {ages} | сигналов {self.stats['signals']}, исполнено {tr.mstats['filled']} "
                 f"({tr.mstats['shares']:.0f} шт), PnL {tr.total_pnl:+.2f}$\033[0m")

    async def status_loop(self, every: float = 300.0):
        while True:
            await asyncio.sleep(every)
            st = self.stats
            parts = [f"{SRC_NAME[k]}: сделок {self.n[k]}, задержка p50/p90 {self.lat[k].q(0.5) or 0:.0f}/"
                     f"{self.lat[k].q(0.9) or 0:.0f} мс" for k in ("bnf", "by", "cb")]
            for q in self.lat.values():
                q.clear()
            emit(f"{CY}[SIG4] шагов {st['ticks']}, сигналов {st['signals']}; пропуски: нет свежего хода BTC {st['skip_fresh']}, "
                 f"заявка уже стоит {st['skip_open']}, неполная история окна {st['skip_history']}, пауза {st['skip_block']}, нет фьючерса {st['skip_feed']}, книга "
                 f"{st['skip_book']}; снятия: прогноз {st['cancel_keep']}, рынок ушёл {st['cancel_far']}, BTC против "
                 f"{st['cancel_adverse']} (ходов против {st['adverse']}); расчёт p50/p90 {self.calc.q(0.5) or 0:.1f}/"
                 f"{self.calc.q(0.9) or 0:.1f} мс | " + " | ".join(parts) + X)

    def tasks(self):
        c = self.c
        return [
            self._feed("bnf", list(c["sig4_urls_bnf"]), None, self.parse_bnf, None),
            self._feed("by", [c["sig4_url_bybit"]], json.dumps({"op": "subscribe", "args": ["publicTrade.BTCUSDT"]}),
                       self.parse_bybit, json.dumps({"op": "ping"})),
            self._feed("cb", [c["sig4_url_coinbase"]],
                       json.dumps({"type": "subscribe", "product_ids": ["BTC-USD"], "channels": ["ticker"]}),
                       self.parse_coinbase, None),
            self.tick_loop(), self.pulse_loop(), self.status_loop(),
        ]


def _r(x, nd=2):
    return None if x is None or x != x else round(x, nd)


def _f(x):
    return "—" if x is None or x != x else f"{x:+.1f}"
