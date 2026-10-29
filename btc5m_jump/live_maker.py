"""Мейкерское исполнение сигналов: по сигналу варианта ставим пассивную заявку на покупку и снимаем её через пару секунд.

Включается в файле настроек живого теста ключом "execution": "maker" (см. live_config_maker.example.json):
    python bot.py --live live_config_maker.json --mode dry   # без ключей: заявки не ставятся, исполнение - теневое
    python bot.py --live live_config_maker.json --mode sign  # подписывает, но не отправляет
    python bot.py --live live_config_maker.json --mode live  # настоящие заявки

Идея (разбор M2/M4): сразу после скачка BTC запоздавшие продажи (тейкерские ордера биржа держит 150 мс) бьют в лучшие
bid по старой цене. Пассивная заявка задержки не проходит и встаёт в книгу за ~25 мс, поэтому успевает их поймать.
Исполнения в первые 0,5 с после постановки дают основную прибыль, поздние - убыток, поэтому заявка живёт недолго.

Как устроено:
  * цена - лучший bid стороны сигнала, или bid + 1 ц, если спред не меньше 2 ц ("maker_price": "improve");
    заявка post-only: если она пересекла бы спред, сервер её отклонит, тейкером мы не покупаем;
  * "maker_price": "ask" - цена = ask в момент сигнала, без post-only: если ask ещё на месте, заявка исполняется сразу
    тейкером (биржа держит её 150 мс, комиссия тейкера), иначе стоит bid'ом по этой цене до снятия;
  * "maker_price": "ab" - на каждый сигнал случайно один из режимов ab_modes (по умолчанию improve и ask): A/B-тест
    в одинаковых условиях; режим пишется в maker_orders/maker_final (price_mode), итоги - по режимам;
  * тип GTD со сроком gtd_expire_sec (страховка: если снять не удалось, биржа снимет сама), иначе GTC;
  * через maker_life_sec заявка снимается, затем по get_order узнаём, сколько исполнилось; позиция держится до конца окна;
  * одна открытая заявка на сторону, лимиты на окно и сутки, файл STOP, стоп после серии ошибок;
  * «теневое» исполнение по сделкам рынка (очередь - объём уровня на момент постановки, как в симуляции M2) считается
    во всех режимах; в dry и sign оно же идёт в учёт PnL, в live пишется рядом с фактом для сравнения с симуляцией;
  * в live слушаем приватный канал заявок (события с временем) - для разбора, когда именно исполнялись заявки.
Все изменения состояния - в потоке event loop; сеть - в отдельных пулах потоков (отправка и снятие не ждут друг друга).
"""
from __future__ import annotations

import asyncio
import json
import os
import random
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

from common import clock, emit, log, taker_fee
from live import LiveTrader, order_size

FEE_RATE = 0.07
TAKER_CHECK_SEC = 0.335   # теневая проверка заявки по ask: исполнилась ли сразу (удержание биржей 150 мс + дорога)
MODE_NAME = {"join": "по bid", "improve": "bid+1", "ask": "по ask", "ask1": "ask+1"}
TAKER_MODES = ("ask", "ask1")      # обычный лимит, может исполниться сразу тейкером
GTD_MIN_SEC = 240                  # нижняя граница срока GTD: сервер отклоняет срок меньше 180 с (+ запас на предподпись)

MAKER_LIVE_SCHEMAS = {
    "maker_orders": ["sid", "slug", "outcome", "t_signal", "t_sent", "t_resp", "http_ms", "price", "size", "mode", "status",
                     "order_id", "error", "bid", "ask", "ahead", "edge_c", "T", "presigned", "sign_ms", "price_mode"],
    "maker_final": ["sid", "slug", "outcome", "order_id", "price", "size", "t_cancel", "cancel_ms", "cancel_status",
                    "size_matched", "order_status", "shadow_qty", "shadow_ms", "error", "shadow_first_ms", "price_mode",
                    "shadow_taker", "shadow_px"],
    "maker_user_events": ["recv_ms", "event_type", "type", "order_id", "status", "size_matched", "price", "outcome", "raw"],
}

MAKER_DEFAULTS = {
    "maker_price": "improve",      # join - лучший bid; improve - bid + 1 ц, если спред >= 2 ц; ask - по ask сигнала
                                   # (может исполниться сразу тейкером, с комиссией); ab - случайно из ab_modes на каждый сигнал
    "ab_modes": ["improve", "ask"],
    "maker_life_sec": 2.0,         # сколько секунд заявка стоит в книге
    "order_type": "GTD",           # GTD (со страховочным сроком) или GTC
    "gtd_expire_sec": 300,         # срок GTD-заявки от момента подписи; сервер требует не меньше 180 с (ответ
                                   # 'expiration is less than 180 seconds in the future'), меньше GTD_MIN_SEC не ставим
    "max_open_orders": 2,
    "one_order_per_side": True,    # False - по каждому сигналу своя заявка, даже если прошлая на этой стороне ещё стоит
    "max_consecutive_errors": 5,
    "shadow_match_sec": TAKER_CHECK_SEC,  # dry/sign: через сколько секунд после сигнала заявка по ask сводится с книгой
}

USER_WS = "wss://ws-subscriptions-clob.polymarket.com/ws/user"
CY, GR, RD, X = "\033[96m", "\033[92m", "\033[91m", "\033[0m"


def ts(t: float) -> str:
    return datetime.fromtimestamp(t).strftime("%H:%M:%S.%f")[:-3]


class ShadowHook:
    """Подключается к PM на место бумажного мейкера (pm.maker): PM отдаёт сюда сделки рынка."""

    def __init__(self, trader):
        self.t = trader

    def requote(self, now):
        pass

    def settle(self, win, winner):
        pass

    def on_trade(self, win, oc, side, price, size, sts):
        self.t.on_market_trade(win, oc, side, price, size, sts)


class MakerTrader(LiveTrader):
    def __init__(self, lcfg: dict, mode: str, pm, writer, ui=None):
        if mode == "live" and lcfg.get("test_only"):
            raise SystemExit("этот файл настроек помечен test_only (без лимитов) - он только для режимов dry и sign")
        super().__init__(lcfg, mode, pm, writer, ui)
        self.post_pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="mk-post")
        self.aux_pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="mk-aux")
        self.open: dict[int, dict] = {}          # номер сигнала -> состояние заявки
        self.errors = 0
        self.hook = ShadowHook(self)
        self.watchdog_every = 5.0
        self.mstats = dict(signals=0, placed=0, skipped=0, filled=0, shares=0.0, shadow_filled=0, shadow_shares=0.0, trades_seen=0)
        self.mode_stats: dict[str, dict] = {}    # режим цены -> заявок, исполнено, шейров, PnL (для A/B)
        self.recent: dict[int, dict] = {}        # номер сигнала -> постановка и итог (для панели jump)
        self.http_hist = deque(maxlen=100)       # время ответа сервера по последним заявкам, мс
        self.win_hist = deque(maxlen=60)         # итоги закрытых окон (для панели): slug, start, winner, pnl, pnl_api
        self.t_start = clock.now()
        self.last_error = None                   # (время, статус, текст) последней ошибки постановки - для панели

    def on_reconciled(self, slug, pnl):
        """Сверка окна с Polymarket (live, из потока сверки): точный PnL окна - в историю для панели."""
        for h in self.win_hist:
            if h["slug"] == slug:
                h["pnl_api"] = pnl

    def _note(self, sid, **kw):
        d = self.recent.setdefault(sid, {})
        d.update(kw)
        if len(self.recent) > 300:
            for k in list(self.recent)[:100]:
                self.recent.pop(k, None)

    def m(self, key):
        return self.c.get(key, MAKER_DEFAULTS[key])

    # ------------------------------------------------------------------ подключение
    def connect(self):
        super().connect()
        if self.mode == "dry":
            return
        from py_clob_client_v2 import OrderPayload
        self._OrderPayload = OrderPayload
        # post_order у библиотеки после исполнения опрашивает сделки до появления хэшей транзакций (лишние запросы,
        # в Токио ~240 мс каждый): ответ сервера нужен сразу - время ответа и снятие заявки не должны их ждать
        if self.client is not None and hasattr(self.client, "_resolve_transactions_hashes"):
            self.client._resolve_transactions_hashes = lambda resp: resp
        try:
            from py_clob_client_v2 import OrderMarketCancelParams
            self._MarketCancel = OrderMarketCancelParams
        except ImportError:  # pragma: no cover
            self._MarketCancel = None

    def _order_type(self):
        return getattr(self._OrderType, "GTD" if str(self.m("order_type")).upper() == "GTD" else "GTC")

    def _make_order(self, tok, px, sz):
        kw = dict(token_id=tok, price=px, size=sz, side=self._BUY)
        if str(self.m("order_type")).upper() == "GTD":
            kw["expiration"] = int(time.time()) + max(int(self.m("gtd_expire_sec")), GTD_MIN_SEC)
        return self.client.create_order(self._OrderArgs(**kw), self._Opts(tick_size="0.01"))

    # ------------------------------------------------------------------ цена и лимиты
    def modes(self) -> list[str]:
        m = str(self.m("maker_price")).lower()
        return [str(x).lower() for x in self.m("ab_modes")] if m == "ab" else [m]

    def pick_mode(self) -> str:
        ms = self.modes()
        return ms[random.randrange(len(ms))]

    def quote(self, b, mode=None):
        """Цена заявки по нашей копии книги стороны; None - поставить нельзя.
        join/improve - пассивная (ниже ask); ask - по ask, такая заявка может исполниться сразу."""
        mode = mode or self.modes()[0]
        bid, ask = b.bb, b.ba
        if bid is None or ask is None:
            return None
        if mode == "ask":
            return round(ask, 2)
        if mode == "ask1":
            return round(min(ask + 0.01, 0.99), 2)
        q = bid + (0.01 if mode == "improve" and ask - bid >= 0.02 - 1e-9 else 0.0)
        q = round(q, 2)
        return q if q < ask - 1e-9 else None

    def _new_st(self):
        return dict(orders=0, filled=0, spend=0.0, shares={"Up": 0.0, "Down": 0.0}, usdc={"Up": 0.0, "Down": 0.0},
                    pending={"Up": 0.0, "Down": 0.0}, cond=None)

    def check_maker_limits(self, s, st, q, size) -> str | None:
        c = self.c
        today = datetime.now(timezone.utc).date()
        if self.day != today:
            self.day, self.day_spend, self.day_pnl = today, 0.0, 0.0
            self.stopped_reason = None if (self.stopped_reason or "").startswith("дневн") else self.stopped_reason
        if os.path.exists(c["stop_file"]):
            return f"найден файл {c['stop_file']} - аварийная остановка"
        if self.stopped_reason:
            return self.stopped_reason
        lt = c.get("max_loss_total")
        if lt is not None and -self.total_pnl >= lt:
            self.stopped_reason = f"общий убыток с запуска {self.total_pnl:.2f}$ достиг лимита"
            return self.stopped_reason
        if -self.day_pnl >= c["max_loss_per_day"]:
            self.stopped_reason = f"дневной убыток {self.day_pnl:.2f}$ достиг лимита"
            return self.stopped_reason
        if self.m("one_order_per_side") and any(o["slug"] == s["slug"] and o["outcome"] == s["outcome"]
                                                for o in self.open.values()):
            return "заявка этой стороны ещё стоит"
        if len(self.open) >= int(self.m("max_open_orders")):
            return "много открытых заявок"
        if not (c["price_min"] <= q <= c["price_max"]):
            return "цена вне диапазона"
        if s["T"] < c["min_seconds_left"] + float(self.m("maker_life_sec")):
            return "мало времени до конца окна"
        cost = q * size
        if self.day_spend + cost > c["max_spend_per_day"]:
            return f"дневной лимит трат {c['max_spend_per_day']}$"
        if st["orders"] >= c["max_orders_per_window"]:
            return "лимит заявок на окно"
        if st["spend"] + cost > c["max_spend_per_window"]:
            return "лимит трат на окно"
        if st["shares"][s["outcome"]] + st["pending"][s["outcome"]] + size > c["max_shares_per_window"]:
            return "лимит шейров на окно"
        if clock.now() - self.last_order_t < float(c.get("min_interval_sec", 0) or 0):
            return "слишком часто"
        return None

    # ------------------------------------------------------------------ сигнал -> заявка
    def on_signal(self, s):
        if s["variant"] != self.c["variant"]:
            return
        self.loop = asyncio.get_running_loop()
        self.mstats["signals"] += 1
        win = self.pm.windows.get(s["start"])
        if win is None:
            return
        b = win.books[s["outcome"]]
        mode = s.get("price_mode") or self.pick_mode()
        q = self.quote(b, mode)
        st = self.win_stats.setdefault(s["slug"], self._new_st())
        if q is None:
            self.mstats["skipped"] += 1
            self._note(s["sid"], status="нет цены")
            emit(f"{ts(s['t'])} СИГНАЛ #{s['sid']} {s['outcome']} - заявка не ставится: нет цены ниже ask (bid {b.bb}, ask {b.ba})")
            return
        size = order_size(float(self.c["size"]), q)
        why = self.check_maker_limits(s, st, q, size)
        if why:
            self.mstats["skipped"] += 1
            self._note(s["sid"], status="пропуск: " + why)
            emit(f"{ts(s['t'])} СИГНАЛ #{s['sid']} {s['outcome']} - заявка не ставится: {why}")
            return
        life = float(self.m("maker_life_sec"))
        now = clock.now()
        e = dict(sid=s["sid"], slug=s["slug"], start=s["start"], outcome=s["outcome"],
                 token=win.m["up_token"] if s["outcome"] == "Up" else win.m["down_token"],
                 q=q, mirror=round(1 - q, 2), size=size, t_signal=s["t"], T=s["T"], edge=s.get("edge", 0.0),
                 bid=b.bb, ask=b.ba, ahead=float(b.bids.get(q, 0.0)), status="sending", oid="", expired=False,
                 t_act_srv=now * 1000 + self.pm.offset_ms + 15.0, t_end_srv=None,
                 shadow_qty=0.0, shadow_ms=None, shadow_first_ms=None, shadow_left=float(b.bids.get(q, 0.0)),
                 shadow_done=False, move=s.get("move"), anchor_age=s.get("anchor_age"),
                 mode=mode, taker_wait=(mode in TAKER_MODES), shadow_taker=False, shadow_px=None,
                 src=s.get("src"), tier=s.get("tier"), win_ms=s.get("win_ms"))
        self.open[e["sid"]] = e
        st["cond"] = win.m.get("condition_id")
        st["orders"] += 1
        st["spend"] += q * size
        st["pending"][e["outcome"]] += size
        self.day_spend += q * size
        self.last_order_t = now
        ms = self.mode_stats.setdefault(mode, dict(orders=0, filled=0, shares=0.0, pnl=0.0))
        ms["orders"] += 1
        self.loop.run_in_executor(self.post_pool, self._place, e)
        self.loop.call_later(life, self._expire, e)
        if mode in TAKER_MODES:
            self.loop.call_later(float(self.m("shadow_match_sec")), self._shadow_taker_check, e)

    def _place(self, e):
        """Поток отправки: подписанная заранее (или сейчас) post-only заявка."""
        t_sent = clock.now()
        r = dict(t_sent=t_sent, t_resp=t_sent, http_ms=None, status="dry", oid="", err="", presigned=False, sign_ms=None)
        if self.mode != "dry":
            try:
                t0 = time.perf_counter()
                pre = self.presigned.pop((e["token"], e["q"], e["size"]), None)
                if pre is not None and time.time() - pre[1] <= float(self.c.get("presign_max_age_sec", 8)):
                    order, r["presigned"] = pre[0], True
                else:
                    order = self._make_order(e["token"], e["q"], e["size"])
                r["sign_ms"] = (time.perf_counter() - t0) * 1000
                if self.mode == "sign":
                    r["status"] = "signed_not_sent"
                else:
                    t1 = time.perf_counter()
                    resp = self.client.post_order(order, self._order_type(), post_only=e["mode"] not in TAKER_MODES)
                    r["http_ms"] = (time.perf_counter() - t1) * 1000
                    r["oid"] = resp.get("orderID") or resp.get("orderId") or ""
                    r["err"] = resp.get("errorMsg") or ""
                    r["status"] = str(resp.get("status") or ("ok" if resp.get("success") else "error"))
            except Exception as ex:
                msg = str(getattr(ex, "error_msg", "") or ex)
                low = msg.lower()
                r["status"] = "rejected_cross" if ("post" in low and "only" in low) or "cross" in low else "exception"
                r["err"] = msg[:300]
            r["t_resp"] = clock.now()
        self.loop.call_soon_threadsafe(self._placed, e, r)

    def _placed(self, e, r):
        e.update(oid=r["oid"], t_sent=r["t_sent"], t_resp=r["t_resp"])
        self._note(e["sid"], status=r["status"], q=e["q"], mode=e["mode"], t_sent=r["t_sent"], http_ms=r["http_ms"],
                   sign_ms=r["sign_ms"], presigned=r["presigned"])
        if r["err"] and r["status"] in ("error", "exception", "rejected_cross"):
            self._note(e["sid"], err=r["err"])
            self.last_error = (clock.now(), r["status"], r["err"])
        if r["http_ms"]:
            self.http_hist.append(r["http_ms"])
        self.w.write("maker_orders", (e["sid"], e["slug"], e["outcome"], e["t_signal"], r["t_sent"], r["t_resp"],
                                      round(r["http_ms"], 1) if r["http_ms"] else None, e["q"], e["size"], self.mode,
                                      r["status"], r["oid"], r["err"], e["bid"], e["ask"], e["ahead"],
                                      round(100 * e["edge"], 3), round(e["T"], 2), int(r["presigned"]),
                                      round(r["sign_ms"], 2) if r["sign_ms"] is not None else None, e["mode"]))
        life = self.m("maker_life_sec")
        if self.mode in ("dry", "sign"):
            e["status"] = "shadow"
            how = ("не отправляется (dry)" if self.mode == "dry" else
                   "подписана, не отправлена (sign" + (", готовая подпись)" if r["presigned"] else f", подпись {r['sign_ms'] or 0:.0f} мс)"))
            shadow = (f"исполнение: сразу по ask, если он не выше цены заявки через {1000 * float(self.m('shadow_match_sec')):.0f} мс, "
                      "иначе по сделкам рынка" if e["mode"] in TAKER_MODES else "исполнение считается по сделкам рынка")
            self._print_order(e, f"{how}; {shadow}, снятие через {life} с")
        elif r["oid"] and r["status"] not in ("error", "exception", "rejected_cross"):
            e["status"] = "live"
            self.errors = 0
            self.mstats["placed"] += 1
            self._print_order(e, f"в книге, ответ биржи {r['http_ms'] or 0:.0f} мс; снятие через {life} с")
        else:
            e["status"] = "failed"
            if r["status"] != "rejected_cross":
                self.errors += 1
                if self.errors >= int(self.m("max_consecutive_errors")):
                    self.stopped_reason = f"{self.errors} ошибок подряд при постановке заявок"
            self._print_order(e, f"{RD}НЕ ПОСТАВЛЕНА{X}: {r['status']} {r['err'][:120]}")
            if r["status"] == "exception":
                # исход неизвестен: заявка могла встать - снимаем всё по этому токену (у нас там не больше одной)
                self.loop.run_in_executor(self.aux_pool, self._cancel_token, e)
            else:
                self._final(e, dict(t_cancel=clock.now(), cancel_ms=None, cancel_status="not_placed", size_matched=0.0,
                                    order_status="", err=r["err"]))
            return
        if e.get("cancel_asap") or clock.now() >= e["t_signal"] + float(self.m("maker_life_sec")):
            self._expire(e)        # просили снять раньше / ответ пришёл позже срока жизни - снимаем сразу

    def cancel_early(self, sid: int, why: str = "") -> bool:
        """Снять заявку раньше срока жизни (стратегия 4: прогноз упал, рынок ушёл, ход BTC против).
        Если ответа на постановку ещё нет - снимем сразу, как только он придёт. True - снятие запрошено."""
        e = self.open.get(sid)
        if e is None or e.get("expired") or e.get("status") == "failed":
            return False
        if e.get("early"):
            return False
        e["early"] = why or "досрочно"
        if e["status"] == "sending":
            e["cancel_asap"] = True
            return True
        self._expire(e)
        return True

    def _expire(self, e):
        if e["expired"] or e["status"] == "sending":
            return                  # ещё нет ответа на постановку - _placed вызовет снова
        if e["status"] == "failed":
            return
        e["expired"] = True
        e["t_end_srv"] = clock.now() * 1000 + self.pm.offset_ms + 15.0
        if e["status"] == "live":
            self.loop.run_in_executor(self.aux_pool, self._do_cancel, e)
        else:  # dry/sign: дождаться сделок, которые уже идут к нам по ленте (~40 мс), и закрыть по теневому исполнению
            self.loop.call_later(0.3, self._final, e, dict(t_cancel=clock.now(), cancel_ms=None, cancel_status="shadow",
                                                            size_matched=None, order_status="", err=""))

    def _do_cancel(self, e):
        t0 = clock.now()
        status, err = "", ""
        for attempt in range(2):
            try:
                resp = self.client.cancel_order(self._OrderPayload(orderID=e["oid"]))
                canceled = (resp or {}).get("canceled") or []
                status = "canceled" if e["oid"] in canceled else ("not_canceled " + json.dumps((resp or {}).get("not_canceled"))[:150])
                break
            except Exception as ex:
                err = repr(ex)[:200]
                time.sleep(0.2)
        cancel_ms = (clock.now() - t0) * 1000
        size_matched, ostatus = None, ""
        for attempt in range(3):
            try:
                o = self.client.get_order(e["oid"]) or {}
                size_matched = float(o.get("size_matched") or 0)
                ostatus = str(o.get("status") or "")
                break
            except Exception as ex:
                err = (err + " | get_order " + repr(ex))[:300]
                time.sleep(0.3)
        if not status and ostatus.upper() in ("LIVE", "ORDER_STATUS_LIVE"):
            try:            # снять не удалось, а заявка ещё стоит - снимаем все свои заявки и останавливаемся
                self.client.cancel_all()
            except Exception:
                pass
            self.loop.call_soon_threadsafe(self._halt, "не удалось снять заявку")
        self.loop.call_soon_threadsafe(self._final, e, dict(t_cancel=t0, cancel_ms=cancel_ms, cancel_status=status or "error",
                                                            size_matched=size_matched, order_status=ostatus, err=err))

    def _cancel_token(self, e):
        err = ""
        try:
            if self._MarketCancel is not None:
                self.client.cancel_market_orders(self._MarketCancel(market=self.win_stats.get(e["slug"], {}).get("cond") or "",
                                                                    asset_id=e["token"]))
            else:
                self.client.cancel_all()
        except Exception as ex:
            err = repr(ex)[:200]
        self.loop.call_soon_threadsafe(self._final, e, dict(t_cancel=clock.now(), cancel_ms=None, cancel_status="token_cancel",
                                                            size_matched=None, order_status="", err=err))

    def _halt(self, why):
        self.stopped_reason = why
        log("maker", f"ОСТАНОВКА: {why}")

    def _final(self, e, r):
        if self.open.get(e["sid"]) is e:
            self.open.pop(e["sid"])
        if self.mode in ("dry", "sign"):
            filled = min(e["shadow_qty"], e["size"])
            px, fee_ps = e["q"], 0.0
            if e.get("shadow_taker") and filled > 0:     # тейкерская часть по ask книги + остаток по цене заявки
                tk = min(e.get("shadow_tk", filled), filled)
                px = (tk * e["shadow_px"] + (filled - tk) * e["q"]) / filled
                fee_ps = tk * taker_fee(e["shadow_px"], FEE_RATE) / filled
        else:
            filled = r["size_matched"] or 0.0   # None - неизвестно: в учёт не идёт, PnL уточнит сверка с Polymarket
            px = e["q"]
            # заявка по ask могла исполниться тейкером: в оценке берём комиссию тейкера (верхняя оценка), точно - сверка
            fee_ps = taker_fee(px, FEE_RATE) if e.get("mode") in TAKER_MODES else 0.0
        filled = min(filled, e["size"])
        cost = (px + fee_ps) * filled
        st = self.win_stats.get(e["slug"])
        if st is not None:
            st["pending"][e["outcome"]] -= e["size"]
            delta = cost - e["q"] * e["size"]
            st["spend"] += delta
            self.day_spend += delta
            if filled > 0:
                st["filled"] += 1
                st["shares"][e["outcome"]] += filled
                st["usdc"][e["outcome"]] += cost
        if filled > 0:
            self.last_fill_t = clock.now()
            self.mstats["filled"] += 1
            self.mstats["shares"] += filled
            ms = self.mode_stats.setdefault(e.get("mode", ""), dict(orders=0, filled=0, shares=0.0, pnl=0.0))
            ms["filled"] += 1
            ms["shares"] += filled
        if e["shadow_qty"] > 0:
            self.mstats["shadow_filled"] += 1
            self.mstats["shadow_shares"] += e["shadow_qty"]
        self._note(e["sid"], filled=filled, px=px, taker=bool(e.get("shadow_taker")), done=True,
                   cancel=r["cancel_status"][:20] if r["cancel_status"] else "")
        self.w.write("maker_final", (e["sid"], e["slug"], e["outcome"], e["oid"], e["q"], e["size"], r["t_cancel"],
                                     round(r["cancel_ms"], 1) if r["cancel_ms"] else None, r["cancel_status"],
                                     r["size_matched"], r["order_status"], round(e["shadow_qty"], 3),
                                     round(e["shadow_ms"], 1) if e["shadow_ms"] is not None else None, r["err"],
                                     round(e["shadow_first_ms"], 1) if e["shadow_first_ms"] is not None else None,
                                     e.get("mode", ""), int(bool(e.get("shadow_taker"))), e.get("shadow_px")))
        if st is not None and filled > 0:
            st.setdefault("fills", []).append(dict(sid=e["sid"], outcome=e["outcome"], q=px, qty=filled, fee=fee_ps * filled,
                                                   mode=e.get("mode", "")))
        self._print_final(e, r, filled)

    def _print_order(self, e, result):
        mv = "" if e.get("move") is None else f"BTC {e['move']:+.1f}$"
        if e.get("src"):           # сигнал хода Binance (jump.py)
            what = f"{mv} за {e.get('win_ms') or 100} мс ({e['src']}) | сдвиг цены {100 * e['edge']:.1f} ц [{e.get('tier')}]"
        else:
            age = "" if e.get("anchor_age") is None else f" за {e['anchor_age']:.1f} с без переоценки книги"
            what = f"{mv}{age} | edge {100 * e['edge']:.1f} ц"
        emit(f"{CY}{ts(e['t_signal'])} СИГНАЛ #{e['sid']} {e['outcome']}{X} | {what} | "
             f"до конца окна {e['T']:.0f} с\n"
             f"             ЗАЯВКА #{e['sid']} [{MODE_NAME.get(e['mode'], e['mode'])}] BUY {e['outcome']} {e['size']:.0f} шт @ {e['q']:.2f} "
             f"(bid {e['bid']:.2f} / ask {e['ask']:.2f}, впереди в очереди {e['ahead']:.0f} шт) → {result}")

    def _print_final(self, e, r, filled):
        sh = e["shadow_qty"]
        first = "" if e["shadow_first_ms"] is None else f", первое через {e['shadow_first_ms']:.0f} мс"
        full = "" if e["shadow_ms"] is None else f", полностью через {e['shadow_ms']:.0f} мс"
        if self.mode in ("dry", "sign") and e.get("shadow_taker"):
            fee = taker_fee(e["shadow_px"], FEE_RATE) * sh
            what = f"{GR}ИСПОЛНЕНА СРАЗУ{X} тейкером {sh:.0f} шт по {e['shadow_px']:.2f} (комиссия {fee:.2f}$)"
        elif self.mode in ("dry", "sign"):
            what = (f"{GR}ИСПОЛНЕНА{X} {sh:.0f} шт по сделкам рынка{first}{full}" if sh >= e["size"] - 1e-9 else
                    f"{GR}ЧАСТИЧНО{X} {sh:.0f} из {e['size']:.0f} шт по сделкам рынка{first}" if sh > 0 else "не исполнена")
        else:
            if r["size_matched"] is None:
                what = f"{RD}исполнение неизвестно{X} ({r['cancel_status']} {r['err'][:80]})"
            else:
                what = (f"{GR}ИСПОЛНЕНА{X} {filled:.0f} шт" if filled >= e["size"] - 1e-9 else
                        f"{GR}ЧАСТИЧНО{X} {filled:.0f} из {e['size']:.0f} шт" if filled > 0 else "не исполнена")
                what += f" (снятие: {r['cancel_status'][:40]}"
                what += f", {r['cancel_ms']:.0f} мс)" if r["cancel_ms"] else ")"
            what += f" | по сделкам рынка: {sh:.0f} шт{first}"
        if e.get("early"):
            what += f" | снята досрочно: {e['early']}"
        emit(f"{ts(clock.now())} ИТОГ   #{e['sid']} [{MODE_NAME.get(e.get('mode'), e.get('mode'))}] {e['outcome']} @ {e['q']:.2f}: {what}")

    # ------------------------------------------------------------------ теневое исполнение по сделкам рынка
    def _shadow_taker_check(self, e):
        """Заявка по ask: если через ~335 мс ask стороны всё ещё не выше нашей цены и объёма хватает - считаем, что
        она исполнилась сразу тейкером по этому ask (с комиссией); иначе дальше она стоит bid'ом по своей цене."""
        if not e.get("taker_wait"):
            return
        e["taker_wait"] = False
        if self.open.get(e["sid"]) is not e:
            return
        win = self.pm.windows.get(e["start"])
        b = win.books[e["outcome"]] if win is not None else None
        now_srv = clock.now() * 1000 + self.pm.offset_ms
        got, cost = 0.0, 0.0
        if b is not None and b.ba is not None and b.ba <= e["q"] + 1e-9:
            for px in sorted(p for p in b.asks if p <= e["q"] + 1e-9):     # уровни не выше цены заявки
                f = min(b.asks[px], e["size"] - got)
                got, cost = got + f, cost + f * px
                if got >= e["size"] - 1e-9:
                    break
        if got > 1e-9:
            e.update(shadow_qty=got, shadow_tk=got, shadow_taker=True, shadow_px=round(cost / got, 4))
            e["shadow_first_ms"] = now_srv - e["t_act_srv"]
            if got >= e["size"] - 1e-9:
                e["shadow_done"] = True
                e["shadow_ms"] = e["shadow_first_ms"]
            else:                   # остаток стоит bid'ом по цене заявки
                e["t_act_srv"] = now_srv
                e["shadow_left"] = float(b.bids.get(e["q"], 0.0))
        else:
            e["t_act_srv"] = now_srv
            e["shadow_left"] = float(b.bids.get(e["q"], 0.0)) if b is not None else 0.0

    def on_market_trade(self, win, oc, side, price, size, sts):
        self.mstats["trades_seen"] += 1          # контроль: сделки рынка до нас доходят
        if not self.open:
            return
        try:
            price, size, sts = float(price), float(size), float(sts)
        except (TypeError, ValueError):
            return
        for e in list(self.open.values()):
            if e["slug"] != win.slug or e["shadow_done"] or e.get("taker_wait") or sts < e["t_act_srv"]:
                continue
            if e["t_end_srv"] is not None and sts >= e["t_end_srv"]:
                continue
            at = through = False
            if oc == e["outcome"] and side == "S":
                at, through = abs(price - e["q"]) < 1e-9, price < e["q"] - 1e-9
            elif oc != e["outcome"] and side == "B":
                at, through = abs(price - e["mirror"]) < 1e-9, price > e["mirror"] + 1e-9
            if through and e["shadow_first_ms"] is None:
                e["shadow_first_ms"] = sts - e["t_act_srv"]
            if through:
                e["shadow_qty"] = e["size"]
            elif at:
                e["shadow_left"] -= size
                if e["shadow_left"] < 0:
                    if e["shadow_first_ms"] is None:
                        e["shadow_first_ms"] = sts - e["t_act_srv"]
                    e["shadow_qty"] = min(e["size"], e["shadow_qty"] - e["shadow_left"])
                    e["shadow_left"] = 0.0
            else:
                continue
            if e["shadow_qty"] >= e["size"] - 1e-9:
                e["shadow_done"] = True
                e["shadow_ms"] = sts - e["t_act_srv"]

    # ------------------------------------------------------------------ предподпись
    def _presign_targets(self):
        win = self.pm.current_window(clock.now())
        if win is None or self.client is None:
            return []
        out = []
        for side, tok in (("Up", win.m["up_token"]), ("Down", win.m["down_token"])):
            b = win.books[side]
            for px in {self.quote(b, m) for m in self.modes()} | {b.bb}:
                if px is None or not (self.c["price_min"] <= px <= self.c["price_max"]):
                    continue
                px = round(px, 2)
                out.append((tok, px, order_size(float(self.c["size"]), px)))
        return out

    async def presign_loop(self):
        loop = asyncio.get_running_loop()
        while True:
            await asyncio.sleep(0.2)
            if self.client is None or not self.c.get("presign", True) or self.mode == "dry":
                continue
            now = time.time()
            maxage = float(self.c.get("presign_max_age_sec", 8))
            targets = self._presign_targets()
            keep = set(targets)
            for k in [k for k, (_, ts) in self.presigned.items() if k not in keep or now - ts > maxage]:
                self.presigned.pop(k, None)
            for k in targets:
                if k in self.presigned:
                    continue
                tok, px, sz = k
                try:
                    order = await loop.run_in_executor(self.presign_pool, self._make_order, tok, px, sz)
                    self.presigned[k] = (order, time.time())
                except Exception as ex:
                    log("maker", f"предподпись не удалась: {ex!r}"[:160])
                    break

    # ------------------------------------------------------------------ приватный канал заявок
    def extra_tasks(self):
        return [self.user_ws(), self.watchdog_loop()]

    async def watchdog_loop(self):
        """Заявка, по которой давно нет итога (сеть, сбой потока), не должна вечно занимать место и резерв:
        снимаем все свои заявки, закрываем её как неизвестную (PnL уточнит сверка) и останавливаемся."""
        self.loop = asyncio.get_running_loop()
        while True:
            await asyncio.sleep(self.watchdog_every)
            limit = float(self.m("maker_life_sec")) + 30.0
            for e in [e for e in list(self.open.values()) if clock.now() - e["t_signal"] > limit]:
                self._halt(f"заявка #{e['sid']} без итога дольше {limit:.0f} с")
                if self.mode == "live" and self.client is not None:
                    self.loop.run_in_executor(self.aux_pool, self._cancel_all_quiet)
                self._final(e, dict(t_cancel=clock.now(), cancel_ms=None, cancel_status="watchdog", size_matched=None,
                                    order_status="", err="нет итога"))

    def _cancel_all_quiet(self):
        try:
            self.client.cancel_all()
        except Exception as ex:
            log("maker", f"cancel_all не удался: {ex!r}"[:160])

    async def user_ws(self):
        if self.mode != "live" or self.client is None:
            return
        import websockets
        while True:
            conds = sorted({w.m.get("condition_id") for w in list(self.pm.windows.values()) if w.m.get("condition_id")})
            if not conds:
                await asyncio.sleep(2)
                continue
            try:
                async with websockets.connect(USER_WS, ping_interval=None, max_queue=4096) as ws:
                    auth = {"apiKey": self.creds.api_key, "secret": self.creds.api_secret, "passphrase": self.creds.api_passphrase}
                    await ws.send(json.dumps({"auth": auth, "type": "user", "markets": conds}))
                    last_ping = time.time()
                    while True:
                        try:
                            raw = await asyncio.wait_for(ws.recv(), timeout=2.0)
                        except asyncio.TimeoutError:
                            raw = None
                        if time.time() - last_ping > 10:
                            await ws.send("PING")
                            last_ping = time.time()
                        if raw and raw != "PONG":
                            self._user_event(raw)
                        now_conds = sorted({w.m.get("condition_id") for w in list(self.pm.windows.values())
                                            if w.m.get("condition_id")})
                        if now_conds != conds:
                            break           # новые окна - переподписываемся
            except Exception as ex:
                log("maker", f"приватный канал разорван ({ex!r})"[:160])
                await asyncio.sleep(2)

    def _user_event(self, raw):
        recv = int(clock.now() * 1000)
        try:
            d = json.loads(raw)
        except Exception:
            return
        for x in (d if isinstance(d, list) else [d]):
            if not isinstance(x, dict):
                continue
            oid = x.get("id") if x.get("event_type") == "order" else (x.get("taker_order_id") or x.get("id"))
            self.w.write("maker_user_events", (recv, x.get("event_type"), x.get("type"), oid, x.get("status"),
                                               x.get("size_matched"), x.get("price"), x.get("outcome"),
                                               json.dumps(x, separators=(",", ":"))[:4000]))

    async def stats_loop(self):
        while True:
            await asyncio.sleep(300)
            s = self.mstats
            emit(f"\033[96m[MAKER] с запуска: сигналов {s['signals']}, поставлено {s['placed']}, пропущено {s['skipped']}, "
                 f"исполнено {s['filled']} заявок ({s['shares']:.0f} шт), теневых исполнений {s['shadow_filled']} "
                 f"({s['shadow_shares']:.0f} шт), сделок рынка получено {s['trades_seen']} | PnL с запуска {self.total_pnl:+.2f}$\033[0m")

    # ------------------------------------------------------------------ итог окна (комиссии мейкера нет)
    def on_settle(self, win, winner, used, results):
        st = self.win_stats.pop(win.slug, None)
        if not st or st["orders"] == 0:
            self.win_hist.append(dict(slug=win.slug, start=win.start, winner=winner, pnl=0.0, pnl_api=None, orders=0,
                                      filled=0, up=0.0, dn=0.0))
            return
        payout = st["shares"][winner]
        cost = sum(st["usdc"].values())
        pnl_est = payout - cost
        self.win_hist.append(dict(slug=win.slug, start=win.start, winner=winner, pnl=pnl_est, pnl_api=None,
                                  orders=st["orders"], filled=st["filled"], up=st["shares"]["Up"], dn=st["shares"]["Down"]))
        self.day_pnl += pnl_est
        self.total_pnl += pnl_est
        self.mstats["windows"] = self.mstats.get("windows", 0) + 1
        how = " (по сделкам рынка)" if self.mode in ("dry", "sign") else ""
        lines = [f"{CY}══ ОКНО {datetime.fromtimestamp(win.start).strftime('%H:%M')}-"
                 f"{datetime.fromtimestamp(win.start + 300).strftime('%H:%M')} закрыто, победил {winner}{X} | "
                 f"заявок {st['orders']}, исполнено {st['filled']}{how}"]
        for f in st.get("fills", []):
            pnl = ((1.0 if f["outcome"] == winner else 0.0) - f["q"]) * f["qty"] - f.get("fee", 0.0)
            col = GR if pnl >= 0 else RD
            fee = f", комиссия {f['fee']:.2f}$" if f.get("fee") else ""
            lines.append(f"     #{f['sid']} [{MODE_NAME.get(f.get('mode'), f.get('mode'))}] {f['outcome']} {f['qty']:.0f} шт "
                         f"@ {f['q']:.2f}{fee} → {col}{pnl:+.2f}${X}")
            ms = self.mode_stats.setdefault(f.get("mode"), dict(orders=0, filled=0, shares=0.0, pnl=0.0))
            ms["pnl"] += pnl
        m = self.mstats
        orders = m["signals"] - m["skipped"]
        lines.append(f"     итог окна {pnl_est:+.2f}$ | с запуска: сигналов {m['signals']}, заявок {orders}, исполнено "
                     f"{m['filled']} ({m['filled'] / max(orders, 1):.1%}), {m['shares']:.0f} шт, PnL {self.total_pnl:+.2f}$ "
                     f"| сделок рынка получено {m['trades_seen']}")
        if len(self.mode_stats) > 1:
            lines.append("     по режимам: " + "; ".join(
                f"{MODE_NAME.get(k, k)}: заявок {v['orders']}, исполнено {v['filled']} ({v['filled'] / max(v['orders'], 1):.1%}), "
                f"PnL {v['pnl']:+.2f}$" for k, v in sorted(self.mode_stats.items())))
        emit("\n".join(lines))
        row = [win.slug, winner, used, st["orders"], st["filled"], st["shares"]["Up"], st["shares"]["Down"], round(cost, 4)]
        if self.mode == "live" and st["cond"] and st["filled"] > 0:
            asyncio.get_running_loop().run_in_executor(self.pool, self._reconcile, row, st, winner, pnl_est)
        else:
            self.w.write("live_windows", tuple(row + [None, None, round(pnl_est, 4), None, round(self.day_pnl, 4)]))

    def shutdown(self):
        super().shutdown()
        self.post_pool.shutdown(wait=False)
        self.aux_pool.shutdown(wait=False)
