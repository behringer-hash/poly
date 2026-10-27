"""Триггер «ход BTC на Binance»: сделки фьючерса и спота Binance (aggTrade, время биржи) -> сигнал на покупку растущего токена.

Правило (как в симуляции P9-P11, btc5m_lab/mm_trig3.py):
  * событие - сделка источника (фьючерс или спот), цена которой отличается от цены последней сделки того же источника
    не позже W мс назад (по времени биржи) на dS; сигнал даёт тот источник, который сообщил о ходе первым;
  * сдвиг справедливой цены Up: dF = phi(z) * w * dS / sd, где z = Phi^-1(mid книги Up), T - секунд до конца окна,
    sd = sigma * sqrt(T - 40) при T >= 60, иначе sigma * sqrt(T^3 / 10800); w = 1 при T >= 60, иначе T / 60;
    sigma - секундная волатильность этого источника за 15 минут ($/sqrt(с));
  * ступени: |dF| >= thr_strong (6 ц) - заявка по ask + 1 ц; thr_weak (3 ц) <= |dF| < thr_strong - по ask (слой объёма);
  * растущая сторона: dS > 0 - Up, dS < 0 - Down; её bid - в границах ступени (сильные 0,01-0,99, слабые 0,10-0,99,
    подбор по записи P18), до конца окна 12-295 с;
  * пауза (на окно и сторону): сильный - не чаще раза в refractory_sec (1 с) между сильными; слабый - не раньше
    refractory_sec после любого сигнала этой стороны.
Сигнал уходит в MakerTrader.on_signal (live_maker.py): обычный лимит на покупку, живёт maker_life_sec (0,5 с), позиция до исхода.
"""
from __future__ import annotations

import asyncio
import math
from collections import deque
from statistics import NormalDist

import websockets

from common import Quantiles, RollingSigma, clock, emit, iter_ws, loads, log

JUMP_SCHEMAS = {
    "jump_signals": ["sid", "t", "src", "T_exch", "lat_ms", "dS", "sigma", "mid_up", "dF", "tier", "price_mode", "slug",
                     "outcome", "T_left", "bid", "ask", "bid_sz", "ask_sz", "book_lag_ms", "action"],
    "jump_feeds": ["t", "src", "event", "info"],
}

JUMP_DEFAULTS = {
    "jump_window_ms": 100,           # ход за W мс по времени биржи
    "jump_thr_weak": 0.03,           # нижняя ступень: сдвиг справедливой цены от 3 ц - заявка по ask
    "jump_thr_strong": 0.06,         # верхняя ступень: от 6 ц - заявка по ask + 1 ц
    "jump_price_weak": "ask",
    "jump_price_strong": "ask1",
    "jump_refractory_sec": 1.0,      # пауза на (окно, сторону, ступень)
    "jump_sources": ["fut", "spot"],
    "jump_min_move_usd": 0.5,        # ходы меньше не рассматриваем вовсе (экономия)
    "jump_sigma_min_sec": 300,       # не торговать, пока волатильность источника набрана меньше чем за N секунд
    "jump_t_min": 12.0,              # секунд до конца окна: от
    "jump_t_max": 295.0,             # до
    # bid растущей стороны (подбор по записи, P18): сильные - без ограничения, слабые - от 0,10 (0,05-0,10 стабильно в минус)
    "jump_bid_min_strong": 0.01,
    "jump_bid_max_strong": 0.99,
    "jump_bid_min_weak": 0.10,
    "jump_bid_max_weak": 0.99,
    "jump_bid_min": 0.01,            # общие внешние границы (для обеих ступеней)
    "jump_bid_max": 0.99,
    "jump_max_book_lag_ms": 1000.0,  # наша книга отстаёт от сервера больше - не торгуем (обрыв/перегрузка)
    "jump_pulse_sec": 1,             # строка ПУЛЬС в консоли раз в N секунд (0 - не выводить)
    "jump_panel": True,              # панель panel.txt в папке данных, обновляется раз в секунду
    # первыми - адреса, проверенные на сервере в Токио (latency_probe 26.10); остальные - запасные
    "jump_urls_fut": ["wss://fstream.binance.com/market/stream?streams=btcusdt@aggTrade",
                      "wss://fstream.binance.com/stream?streams=btcusdt@aggTrade",
                      "wss://fstream.binance.com/ws/btcusdt@aggTrade"],
    "jump_urls_spot": ["wss://stream.binance.com:9443/stream?streams=btcusdt@aggTrade",
                       "wss://stream.binance.com:9443/ws/btcusdt@aggTrade",
                       "wss://data-stream.binance.vision/ws/btcusdt@aggTrade"],
}

_ND = NormalDist()
_SQ2PI = math.sqrt(2 * math.pi)


def fair_shift(mid_up: float, T: float, sigma: float, dS: float) -> float:
    """Сдвиг справедливой цены Up при ходе BTC на dS (знак - как у dS)."""
    z = _ND.inv_cdf(min(max(mid_up, 1e-4), 1 - 1e-4))
    if T >= 60:
        sd, w = sigma * math.sqrt(max(T - 40.0, 1e-9)), 1.0
    else:
        sd, w = sigma * math.sqrt(T ** 3 / 10800.0), T / 60.0
    if sd <= 0:
        return 0.0
    return math.exp(-z * z / 2) / _SQ2PI * w * dS / sd


class Source:
    """История сделок одного источника (время биржи, цена) и его секундная волатильность."""

    def __init__(self, name: str, keep_ms: float):
        self.name = name
        self.keep_ms = keep_ms
        self.h: deque = deque()
        self.sig = RollingSigma(900, 5.0)
        self.lat = Quantiles()
        self.lat_hist: deque = deque()      # (время приёма, задержка мс) за последнюю минуту - для панели
        self.n = 0
        self.alive = 0.0
        self.last_px = None                 # цена и ход за W мс последней сделки - для пульса и панели
        self.last_dS = 0.0
        self.last_T = None

    def add(self, T_ms: float, px: float) -> None:
        h = self.h
        h.append((T_ms, px))
        lim = T_ms - self.keep_ms
        while h and h[0][0] < lim:
            h.popleft()
        self.sig.update(T_ms / 1000.0, px)
        self.n += 1

    def price_before(self, T_ms: float):
        """Цена последней сделки не позже T_ms; None - истории не хватает."""
        for t, px in reversed(self.h):
            if t <= T_ms:
                return px
        return None

    def sigma_ready(self, min_sec: int) -> bool:
        return len(self.sig.diffs) >= min_sec


class JumpTrigger:
    def __init__(self, lcfg: dict, pm, writer, trader):
        self.c = {**JUMP_DEFAULTS, **{k: v for k, v in lcfg.items() if k.startswith("jump_")}}
        self.variant = lcfg["variant"]
        self.pm, self.w, self.trader = pm, writer, trader
        W = float(self.c["jump_window_ms"])
        self.W = W
        self.src = {name: Source(name, max(2000.0, 4 * W)) for name in self.c["jump_sources"]}
        self.last: dict[tuple, float] = {}
        self.sid = 0
        self.stats = dict(moves=0, weak=0, strong=0, sent=0, skip_book=0, skip_sigma=0, skip_time=0, skip_price=0)
        self.evals: deque = deque(maxlen=20000)      # (время, источник, dS, dF) каждой оценки - для панели
        self.recent_sigs: deque = deque(maxlen=12)   # последние сигналы с задержками - для панели
        self.sig_hist: deque = deque(maxlen=20000)   # (время, ступень) сигналов - счёт за 5 минут
        self.t_start = clock.now()

    def m(self, k):
        return self.c[k]

    # ------------------------------------------------------------------ событие
    def on_trade(self, name: str, T_ms: float, recv: float, px: float) -> None:
        s = self.src[name]
        p0 = s.price_before(T_ms - self.W)
        s.add(T_ms, px)
        s.last_px, s.last_T = px, T_ms
        if p0 is None:
            return
        dS = px - p0
        s.last_dS = dS
        if abs(dS) < float(self.m("jump_min_move_usd")):
            return
        self.evaluate(name, T_ms, recv, dS)

    def evaluate(self, name: str, T_ms: float, recv: float, dS: float):
        """Возвращает словарь сигнала (или None) - для тестов; сигнал уходит трейдеру."""
        pm, c = self.pm, self.c
        self.stats["moves"] += 1
        now = clock.now()
        win = pm.current_window(now)
        if win is None or not win.ready():
            self.stats["skip_book"] += 1
            return None
        T = win.end - now
        if not (float(c["jump_t_min"]) < T < float(c["jump_t_max"])):
            self.stats["skip_time"] += 1
            return None
        if win.book_lag_ms is not None and win.book_lag_ms > float(c["jump_max_book_lag_ms"]):
            self.stats["skip_book"] += 1
            return None
        s = self.src[name]
        if not s.sigma_ready(int(c["jump_sigma_min_sec"])):
            self.stats["skip_sigma"] += 1
            return None
        bu = win.books["Up"]
        if bu.bb is None or bu.ba is None:
            self.stats["skip_book"] += 1
            return None
        mid = (bu.bb + bu.ba) / 2
        if not 0.01 < mid < 0.99:
            self.stats["skip_price"] += 1
            return None
        sigma = s.sig.sigma()
        dF = fair_shift(mid, T, sigma, dS)
        self.evals.append((now, name, dS, dF))
        a = abs(dF)
        if a >= float(c["jump_thr_strong"]):
            tier, mode = "strong", str(c["jump_price_strong"])
        elif a >= float(c["jump_thr_weak"]):
            tier, mode = "weak", str(c["jump_price_weak"])
        else:
            return None
        side = "Up" if dS > 0 else "Down"
        b = win.books[side]
        lo = max(float(c["jump_bid_min"]), float(c[f"jump_bid_min_{tier}"]))
        hi = min(float(c["jump_bid_max"]), float(c[f"jump_bid_max_{tier}"]))
        if b.bb is None or b.ba is None or not (lo - 1e-9 <= b.bb <= hi + 1e-9):
            self.stats["skip_price"] += 1
            return None
        # пауза: сильные - не чаще раза в refractory_sec между сильными (слабые их не блокируют);
        # слабые - не раньше refractory_sec после любого сигнала этой стороны в окне (не докупаем продолжение хода)
        refr = float(c["jump_refractory_sec"])
        ks, kw = (win.start, side, "strong"), (win.start, side, "weak")
        if tier == "strong":
            if now - self.last.get(ks, -1e18) < refr:
                return None
            self.last[ks] = now
        else:
            if now - max(self.last.get(kw, -1e18), self.last.get(ks, -1e18)) < refr:
                return None
            self.last[kw] = now
        self.stats[tier] += 1
        self.sid += 1
        sig = dict(sid=self.sid, t=now, slug=win.slug, start=win.start, T=T, outcome=side, variant=self.variant,
                   edge=a, move=dS, anchor_age=None, price_mode=mode, tier=tier, src=name, win_ms=int(self.W))
        self.w.write("jump_signals", (self.sid, round(now, 4), name, int(T_ms), round(recv * 1000 - T_ms + pm.offset_ms, 1),
                                      round(dS, 2), round(sigma, 3), round(mid, 4), round(dF, 5), tier, mode, win.slug, side,
                                      round(T, 2), b.bb, b.ba, b.bids.get(b.bb), b.asks.get(b.ba),
                                      round(win.book_lag_ms, 1) if win.book_lag_ms is not None else None, "signal"))
        self.sig_hist.append((now, tier))
        self.recent_sigs.append(dict(sig, lat_ms=recv * 1000 - T_ms + pm.offset_ms, recv=recv, dF=dF, mid=mid, sigma=sigma,
                                     bid=b.bb, ask=b.ba))
        if self.trader is not None:
            self.stats["sent"] += 1
            self.trader.on_signal(sig)
        return sig

    # ------------------------------------------------------------------ потоки Binance
    async def feed(self, name: str):
        urls = list(self.c["jump_urls_fut"] if name == "fut" else self.c["jump_urls_spot"])
        s = self.src[name]
        i = 0
        while True:
            url = urls[i % len(urls)]
            got = 0
            try:
                async with websockets.connect(url, ping_interval=10, ping_timeout=10, max_queue=8192, compression=None) as ws:
                    log("jump", f"Binance {name} подключён: {url}")
                    self.w.write("jump_feeds", (clock.now(), name, "connected", url))
                    async for raw in iter_ws(ws, 15.0):
                        recv = clock.now()
                        x = loads(raw)
                        x = x.get("data") or x
                        if x.get("e") != "aggTrade":
                            continue
                        got += 1
                        T_ms = float(x["T"])
                        s.alive = recv
                        lat = recv * 1000 - T_ms + self.pm.offset_ms
                        s.lat.add(lat)
                        s.lat_hist.append((recv, lat))
                        while s.lat_hist and s.lat_hist[0][0] < recv - 60:
                            s.lat_hist.popleft()
                        self.on_trade(name, T_ms, recv, float(x["p"]))
            except Exception as ex:
                log("jump", f"Binance {name} разорван ({ex!r})"[:200])
                self.w.write("jump_feeds", (clock.now(), name, "disconnected", repr(ex)[:300]))
            if got == 0:
                i += 1                      # адрес не отдал ни одной сделки - пробуем следующий
            await asyncio.sleep(1)

    async def status_loop(self, every: float = 300.0):
        while True:
            await asyncio.sleep(every)
            st = self.stats
            parts = []
            for name, s in self.src.items():
                parts.append(f"{name}: сделок {s.n}, задержка p50/p90 {s.lat.q(0.5) or 0:.0f}/{s.lat.q(0.9) or 0:.0f} мс, "
                             f"σ {s.sig.sigma():.2f}$/√с{'' if s.sigma_ready(int(self.c['jump_sigma_min_sec'])) else ' (набирается)'}")
                s.lat.clear()
            emit(f"\033[96m[JUMP] ходов ≥${float(self.c['jump_min_move_usd']):g} за {self.W:.0f} мс: {st['moves']}, сигналов: "
                 f"сильных {st['strong']}, слабых {st['weak']}; пропуски: книга {st['skip_book']}, время {st['skip_time']}, "
                 f"цена {st['skip_price']}, σ {st['skip_sigma']} | " + " | ".join(parts) + "\033[0m")

    def tasks(self):
        return [self.feed(n) for n in self.src] + [self.status_loop()]
