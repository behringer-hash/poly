"""Живой тест: реальные ордера минимального размера по сигналам одного бумажного варианта.

Запускается из bot.py:
    python bot.py --live live_config.json --mode dry    # без ключей: только показывает, что отправил бы
    python bot.py --live live_config.json --mode sign   # с ключами: подписывает ордера, но НЕ отправляет
    python bot.py --live live_config.json --mode live   # реальные ордера (попросит подтверждение)

Как устроено:
  * сигнал берётся от бумажного движка (тот же вариант, тот же момент);
  * ордер - FAK (fill-and-kill): купить до N шейров не дороже увиденного ask,
    неисполненный остаток сразу отменяется, в книге ничего не остаётся;
  * жёсткие лимиты на окно и на день, аварийная остановка файлом STOP;
  * каждый ордер пишется в live_orders рядом с номером бумажного сигнала (sid),
    чтобы сравнить: исполнился ли живой ордер там, где бумажный исполнился;
  * после окна фактические траты (с комиссией) сверяются с data-api Polymarket.

Приватный ключ читается из переменной окружения или файла, указанных в конфиге;
в консоль и файлы он не попадает.
"""
from __future__ import annotations

import asyncio
import json
import logging
import math
import os
import random
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

from common import clock, emit, log, taker_fee

# библиотека Polymarket сама печатает каждый отказ сервера - у нас он и так выводится понятнее
logging.getLogger("py_clob_client_v2").setLevel(logging.CRITICAL)
MIN_NOTIONAL = 1.0  # сервер не принимает исполняемые BUY-ордера дешевле $1


def order_size(base: float, price: float) -> float:
    """Не меньше base шейров и не меньше $1 (+5% запаса): при цене 0.14 это 8 шейров, а не 5."""
    return float(max(base, math.ceil(MIN_NOTIONAL * 1.05 / price - 1e-9)))

LIVE_SCHEMAS = {
    "live_orders": ["sid", "variant", "slug", "outcome", "t_signal", "t_sent", "t_resp", "sign_ms", "http_ms",
                    "total_ms", "limit", "size", "mode", "status", "filled", "usdc", "avg_px", "order_id",
                    "tx_hashes", "error", "raw"],
    # параметры каждого отправленного ордера (для подбора переплаты): и исполненных, и нет
    "live_order_meta": ["sid", "t_signal", "slug", "outcome", "variant", "ask_signal", "slip_c", "limit",
                        "edge_c", "fair", "T"],
    # маркауты живых исполнений: mid купленной стороны через 5 и 30 с минус цена и комиссия, ц/шейр
    "live_markouts": ["sid", "t_signal", "slug", "outcome", "slip_c", "edge_c", "avg_px", "fee_ps",
                      "horizon_s", "mid", "markout_c"],
    "live_windows": ["slug", "winner", "used", "orders", "filled_orders", "up_shares", "down_shares",
                     "usdc_est", "usdc_api", "fees_api", "pnl_est", "pnl_api", "day_pnl"],
}

DEFAULTS = {
    "private_key_env": "PM_PRIVATE_KEY",   # имя переменной окружения с приватным ключом
    "private_key_file": "",                 # или путь к файлу с ключом (одна строка)
    "funder": "",                           # адрес кошелька Polymarket (proxy), куда зачислены деньги
    # 3 - "депозитный кошелёк" (аккаунты, созданные в 2026, в т.ч. по email), 1 - старые аккаунты по email (Magic),
    # 2 - браузерный кошелёк (Safe), 0 - прямой EOA. Режим sign сам проверит все и подскажет правильный.
    "signature_type": 3,
    "variant": "anc_3c_by",
    "size": 5,                              # шейров на ордер (минимум Polymarket - 5)
    "max_orders_per_window": 6,
    "max_shares_per_window": 30,
    "max_spend_per_window": 15.0,           # $ за окно
    "max_spend_per_day": 40.0,              # $ за сутки (UTC)
    "max_loss_per_day": 20.0,               # после такого убытка за сутки - стоп
    "min_seconds_left": 10,
    "min_interval_sec": 1.0,
    # на сколько центов выше увиденного ask ставить лимит FAK-ордера (переплата ради исполнения);
    # ордер забирает все уровни книги до этой цены, платим фактическую цену уровней, а не лимит
    "slippage_cents": 0,
    # эксперимент: для каждого ордера случайно выбирать переплату из списка (центов); пусто - всегда slippage_cents
    "slippage_choices": [],
    # как выбирать переплату: "fixed" - slippage_cents, "random" - случайно из slippage_choices,
    # "edge" - от силы сигнала: floor(запас сигнала - edge_margin_cents), от 0 до edge_slip_max_cents
    "slippage_mode": "",
    "edge_margin_cents": 1,
    "edge_slip_max_cents": 7,
    # реальная ценность сигнала больше, чем считает модель (по живым данным в 1,5-2 раза):
    # переплата = floor(edge_scale * запас - edge_margin_cents)
    "edge_scale": 1.0,
    # в последнюю минуту окна сигналы ценнее и исполняются чаще - свой потолок переплаты
    "last_minute_sec": 60,
    "edge_slip_max_last_min_cents": 7,
    # отдельный коэффициент для последней минуты (по умолчанию - как edge_scale)
    "price_min": 0.10,
    "price_max": 0.90,
    "stop_file": "STOP",
    # размер ордера по объёму на лучшем ask в момент сигнала: [[от_шейров, размер], ...];
    # пусто - всегда size. Размер не больше объёма, стоявшего по цене сигнала.
    "size_by_depth": [],
    "presign": True,          # заранее подписывать ордера на текущий ask и цены с переплатой
    "presign_max_age_sec": 8, # подписанный заранее ордер старше этого переподписывается (в ордере есть метка времени)                    # появился такой файл в папке программы - новые ордера не отправляются
}


def load_config(path: str) -> dict:
    cfg = dict(DEFAULTS)
    with open(path, encoding="utf-8") as f:
        user = json.load(f)
    cfg.update({k: v for k, v in user.items() if not k.startswith("_")})
    return cfg


class LiveTrader:
    def __init__(self, lcfg: dict, mode: str, pm, writer, ui=None):
        assert mode in ("dry", "sign", "live")
        self.c, self.mode, self.pm, self.w, self.ui = lcfg, mode, pm, writer, ui
        self.client = None
        self.pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="live")
        self.win_stats: dict[str, dict] = {}   # slug -> счётчики и позиция окна
        self.day = None
        self.day_spend = 0.0
        self.day_pnl = 0.0
        self.last_order_t = 0.0
        self.stopped_reason = None
        self.paper_by_sid: dict[int, dict] = {}  # sid -> {L: "fill"/"miss"} для сравнения
        self.live_by_sid: dict[int, str] = {}
        self.cmp = {"live_fill": 0, "live_total": 0}
        self.warm_tokens: set[str] = set()
        self.loop = None
        self.presigned: dict[tuple, tuple] = {}   # (token, цена, размер) -> (подписанный ордер, когда подписан)
        self.presign_pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="presign")
        # статистика по переплате: slip -> отправлено, исполнено, сумма и число маркаутов 30 с
        self.slip_stats: dict[int, dict] = {}

    # ------------------------------------------------------------------ подключение
    def _key(self) -> str:
        if self.c.get("private_key_file"):
            with open(self.c["private_key_file"], encoding="utf-8") as f:
                return f.read().strip()
        k = os.environ.get(self.c["private_key_env"], "").strip()
        if not k:
            raise SystemExit(f"не найден приватный ключ: задайте переменную окружения {self.c['private_key_env']} "
                             f"или private_key_file в конфиге")
        return k

    def _client(self, sig_type: int, creds=None):
        from py_clob_client_v2 import ClobClient
        return ClobClient("https://clob.polymarket.com", 137, key=self._key(), creds=creds,
                          signature_type=sig_type, funder=self.c["funder"])

    def connect(self):
        if self.mode == "dry":
            log("live", "режим dry: ключи не используются, ордера не создаются и не отправляются")
            return
        try:
            from py_clob_client_v2 import (AssetType, BalanceAllowanceParams, OrderArgs, OrderType,
                                           PartialCreateOrderOptions, Side)
        except ImportError:
            raise SystemExit("нужна библиотека Polymarket CLOB v2: pip install py_clob_client_v2")
        # импорт заранее: в момент ордера не тратим на него время
        self._OrderArgs, self._OrderType, self._Opts, self._BUY = OrderArgs, OrderType, PartialCreateOrderOptions, Side.BUY
        if not self.c.get("funder"):
            raise SystemExit("в конфиге не указан funder - адрес кошелька Polymarket")
        l1 = self._client(int(self.c["signature_type"]))
        # сначала получаем уже существующий ключ API (у аккаунта, торговавшего через сайт или API, он
        # обычно есть); создаём новый, только если его нет. Иначе сервер отвечает "Could not create api key"
        try:
            self.creds = l1.derive_api_key()
        except Exception:
            self.creds = l1.create_api_key()
        log("live", f"сервер CLOB версии {l1.get_version()}")
        self.client = self._client(int(self.c["signature_type"]), self.creds)
        self.check_balance(AssetType, BalanceAllowanceParams)

    def check_balance(self, AssetType, BalanceAllowanceParams):
        """Баланс по каждому типу подписи. Сервер кэширует баланс, поэтому сначала просим его
        обновить. Если деньги видны при другом signature_type, чем в конфиге, - тип указан
        неверно, и ордера сервер тоже отклонит."""
        eoa = self.client.get_address()
        log("live", f"ключ принадлежит адресу {eoa}; кошелёк Polymarket (funder) {self.c['funder']}")
        conf = int(self.c["signature_type"])
        names = {0: "0 (прямой кошелёк)", 1: "1 (старый аккаунт по email)", 2: "2 (браузерный кошелёк)",
                 3: "3 (депозитный кошелёк - новые аккаунты)"}
        found = {}
        for st in [conf] + [x for x in (3, 1, 2, 0) if x != conf]:
            try:
                cl = self.client if st == conf else self._client(st, self.creds)
                p = BalanceAllowanceParams(asset_type=AssetType.COLLATERAL)
                cl.update_balance_allowance(p)
                bal = cl.get_balance_allowance(p)
                usdc = float(bal.get("balance", 0) or 0) / 1e6
                found[st] = usdc
                log("live", f"  signature_type={names[st]}: баланс {usdc:.2f} USDC")
            except Exception as ex:
                msg = str(ex)
                if "no deposit wallet" in msg:
                    msg = "депозитного кошелька для этого ключа нет"
                log("live", f"  signature_type={names[st]}: {msg[:160]}")
        if found.get(conf, 0) >= 5:
            log("live", f"баланс для работы: {found[conf]:.2f} USDC - всё в порядке")
            return
        other = [st for st, v in found.items() if st != conf and v > 0]
        if other:
            msg = (f"деньги видны при signature_type={other[0]}, а в конфиге {conf}. "
                   f"Поставьте в конфиге \"signature_type\": {other[0]} и перезапустите.")
            if self.mode == "live":  # с неверным типом сервер отклонит все ордера - не запускаемся
                raise SystemExit("ОСТАНОВКА: " + msg)
            log("live", "ВНИМАНИЕ: " + msg)
        else:
            log("live", "ВНИМАНИЕ: ни при одном типе подписи баланс не найден. Скорее всего, ключ относится к "
                        "другому аккаунту, чем funder, или деньги ещё не зачислены на торговый баланс.")

    async def keepalive(self):
        """Держим HTTP/2-соединение с CLOB тёплым, чтобы ордер не тратил время на установку связи."""
        while True:
            await asyncio.sleep(15)
            if self.client is not None:
                try:
                    await asyncio.get_running_loop().run_in_executor(self.pool, self.client.get_ok)
                except Exception:
                    pass

    def _warm(self, win):
        """Кэшируем шаг цены, neg_risk и ставку комиссии токенов окна - иначе библиотека
        делала бы эти запросы при первом ордере и теряла на них десятки мс."""
        for tok in (win.m["up_token"], win.m["down_token"]):
            if tok in self.warm_tokens or self.client is None:
                continue
            try:
                # создаём (но не отправляем) пробный ордер: библиотека закэширует версию сервера,
                # шаг цены, neg_risk и параметры комиссии этого токена
                self.client.create_order(self._OrderArgs(token_id=tok, price=0.5, size=5, side=self._BUY),
                                         self._Opts(tick_size="0.01"))
                self.warm_tokens.add(tok)
            except Exception as ex:
                log("live", f"прогрев токена не удался: {ex!r}")

    def _slip_mode(self) -> str:
        m = (self.c.get("slippage_mode") or "").lower()
        if m in ("fixed", "random", "edge"):
            return m
        return "random" if self.c.get("slippage_choices") else "fixed"  # как в прошлых версиях

    def _slip_for(self, s) -> int:
        mode = self._slip_mode()
        if mode == "edge":
            # платим сверху не больше, чем стоит сигнал, минус запас безопасности
            last_min = s.get("T", 999) <= float(self.c.get("last_minute_sec", 60))
            scale = float(self.c.get("edge_scale_last_min" if last_min and "edge_scale_last_min" in self.c
                                     else "edge_scale", 1.0))
            room = scale * 100 * s["edge"] - float(self.c.get("edge_margin_cents", 1))
            cap = int(self.c.get("edge_slip_max_last_min_cents" if last_min else "edge_slip_max_cents", 7))
            return int(max(0, min(math.floor(room), cap)))
        if mode == "random":
            return int(random.choice(self.c["slippage_choices"]))
        return int(round(float(self.c.get("slippage_cents", 0) or 0)))

    def _slip_candidates(self):
        mode = self._slip_mode()
        if mode == "edge":
            top = max(int(self.c.get("edge_slip_max_cents", 7)), int(self.c.get("edge_slip_max_last_min_cents", 7)))
            return list(range(0, top + 1))
        if mode == "random":
            return sorted(set(int(x) for x in self.c["slippage_choices"]))
        return [int(round(float(self.c.get("slippage_cents", 0) or 0)))]

    def _presign_targets(self):
        """Какие ордера держать подписанными: для обеих сторон текущего окна - ask и ask + каждая переплата."""
        win = self.pm.current_window(clock.now())
        if win is None or self.client is None:
            return []
        slips = self._slip_candidates()
        out = []
        for side, tok in (("Up", win.m["up_token"]), ("Down", win.m["down_token"])):
            ask = win.books[side].ba
            if ask is None or not (self.c["price_min"] <= ask <= self.c["price_max"]):
                continue
            for sl in slips:
                px = round(min(ask + sl / 100, 0.99), 2)
                out.append((tok, px, order_size(self.c["size"], px)))
        return out

    async def presign_loop(self):
        """Фоновая подпись: по сигналу остаётся только отправить готовый ордер (экономия ~8 мс и
        никаких редких выбросов подписи на 100+ мс). Подпись идёт по одному ордеру за раз,
        чтобы не отнимать процессор у приёма данных."""
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
                    order = await loop.run_in_executor(
                        self.presign_pool, lambda: self.client.create_order(
                            self._OrderArgs(token_id=tok, price=px, size=sz, side=self._BUY), self._Opts(tick_size="0.01")))
                    self.presigned[k] = (order, time.time())
                except Exception as ex:
                    log("live", f"предподпись не удалась: {ex!r}"[:160])
                    break

    async def warm_loop(self):
        loop = asyncio.get_running_loop()
        while True:
            await asyncio.sleep(1)
            for win in list(self.pm.windows.values()):
                if self.client is not None and win.m["up_token"] not in self.warm_tokens:
                    await loop.run_in_executor(self.pool, self._warm, win)

    # ------------------------------------------------------------------ лимиты
    def _size_for_depth(self, ask_sz) -> float:
        base = float(self.c["size"])
        table = sorted(self.c.get("size_by_depth") or [], key=lambda x: x[0])
        if not table or ask_sz is None:
            return base
        size = base
        for thr, sz in table:
            if ask_sz >= thr:
                size = float(sz)
        # не больше, чем стояло по цене сигнала (иначе ордер полезет на следующие, более дорогие уровни)
        return max(base, min(size, math.floor(ask_sz)))

    def _check_limits(self, s, st) -> str | None:
        c = self.c
        today = datetime.now(timezone.utc).date()
        if self.day != today:
            self.day, self.day_spend, self.day_pnl = today, 0.0, 0.0
            self.stopped_reason = None if (self.stopped_reason or "").startswith("дневн") else self.stopped_reason
        if os.path.exists(c["stop_file"]):
            return f"найден файл {c['stop_file']} - аварийная остановка"
        if self.stopped_reason:
            return self.stopped_reason
        if -self.day_pnl >= c["max_loss_per_day"]:
            self.stopped_reason = f"дневной убыток {self.day_pnl:.2f}$ достиг лимита"
            return self.stopped_reason
        size = order_size(s.get("base_size", c["size"]), s["limit"])
        cost = s["limit"] * size + taker_fee(s["limit"], 0.07) * size
        if self.day_spend + cost > c["max_spend_per_day"]:
            return f"дневной лимит трат {c['max_spend_per_day']}$"
        if st["orders"] >= c["max_orders_per_window"]:
            return "лимит ордеров на окно"
        if st["spend"] + cost > c["max_spend_per_window"]:
            return "лимит трат на окно"
        if st["shares"][s["outcome"]] + size > c["max_shares_per_window"]:
            return "лимит шейров на окно"
        if not (c["price_min"] <= s.get("ask_signal", s["limit"]) <= c["price_max"]):
            return "цена вне диапазона"
        if s["T"] < c["min_seconds_left"]:
            return "мало времени до конца окна"
        if clock.now() - self.last_order_t < c["min_interval_sec"]:
            return "слишком часто"
        return None

    # ------------------------------------------------------------------ события движка
    def on_signal(self, s):
        if s["variant"] != self.c["variant"]:
            return
        self.loop = asyncio.get_running_loop()
        slip_c = self._slip_for(s)
        s = dict(s, ask_signal=s["limit"], limit=round(min(s["limit"] + slip_c / 100, 0.99), 2), slip_c=slip_c,
                 base_size=self._size_for_depth(s.get("ask_sz")))
        st = self.win_stats.setdefault(s["slug"], dict(orders=0, filled=0, spend=0.0, shares={"Up": 0.0, "Down": 0.0},
                                                       usdc={"Up": 0.0, "Down": 0.0}, cond=None))
        why = self._check_limits(s, st)
        if why:
            emit(f"          [LIVE] #{s['sid']} пропуск: {why}")
            return
        st["orders"] += 1
        self.last_order_t = clock.now()
        ss = self.slip_stats.setdefault(slip_c, dict(sent=0, fills=0, mk_sum=0.0, mk_n=0, mk5_sum=0.0, mk5_n=0))
        ss["sent"] += 1
        self.w.write("live_order_meta", (s["sid"], s["t"], s["slug"], s["outcome"], s["variant"], s["ask_signal"],
                                         slip_c, s["limit"], round(100 * s["edge"], 3), round(s["fair"], 5),
                                         round(s["T"], 2)))
        win = self.pm.windows.get(s["start"])
        token = win.m["up_token"] if s["outcome"] == "Up" else win.m["down_token"]
        st["cond"] = win.m.get("condition_id")
        sz = order_size(s["base_size"], s["limit"])
        est = s["limit"] * sz + taker_fee(s["limit"], 0.07) * sz
        self.day_spend += est  # резервируем сразу; уточним по ответу
        st["spend"] += est
        asyncio.get_running_loop().run_in_executor(self.pool, self._send, s, token, st, est)

    def _send(self, s, token, st, est):
        t_sent = clock.now()
        limit = round(s["limit"], 2)
        size = order_size(s.get("base_size", self.c["size"]), limit)
        status, filled, usdc, avg, oid, txs, err, raw = "dry", 0.0, 0.0, None, "", "", "", ""
        sign_ms = http_ms = None
        t1 = None
        if self.mode == "dry":
            status = "dry"
        else:
            try:
                t0 = time.perf_counter()
                pre = self.presigned.pop((token, limit, size), None)
                if pre is not None and time.time() - pre[1] <= float(self.c.get("presign_max_age_sec", 8)):
                    order = pre[0]
                    s["presigned"] = True
                else:
                    order = self.client.create_order(self._OrderArgs(token_id=token, price=limit, size=size,
                                                                     side=self._BUY), self._Opts(tick_size="0.01"))
                sign_ms = (time.perf_counter() - t0) * 1000
                if self.mode == "sign":
                    status = "signed_not_sent"
                else:
                    t1 = time.perf_counter()
                    resp = self.client.post_order(order, self._OrderType.FAK)
                    http_ms = (time.perf_counter() - t1) * 1000
                    raw = json.dumps(resp, separators=(",", ":"))[:600]
                    status = str(resp.get("status") or ("ok" if resp.get("success") else "error"))
                    err = resp.get("errorMsg") or ""
                    oid = resp.get("orderID") or ""
                    txs = ";".join(resp.get("transactionsHashes") or resp.get("transactionHashes") or [])
                    # для покупки: making = отданные USDC, taking = полученные шейры
                    try:
                        usdc = float(resp.get("makingAmount") or 0)
                        filled = float(resp.get("takingAmount") or 0)
                    except (TypeError, ValueError):
                        usdc = filled = 0.0
                    avg = usdc / filled if filled > 0 else None
            except Exception as ex:
                if t1 is not None:
                    http_ms = (time.perf_counter() - t1) * 1000
                msg = str(getattr(ex, "error_msg", "") or ex)
                if "no orders found to match" in msg:
                    status, err = "no_match", "встречных заявок по этой цене уже нет"
                elif "min size" in msg or "invalid amount" in msg:
                    status, err = "rejected_size", msg[:200]
                else:
                    status, err = "exception", repr(ex)[:300]
        t_resp = clock.now()
        total_ms = (t_resp - s["t"]) * 1000
        # уточняем резерв лимитов по факту
        fact = usdc + (taker_fee(avg, 0.07) * filled if avg else 0.0)
        self.day_spend += fact - est
        st["spend"] += fact - est
        if filled > 0:
            st["filled"] += 1
            st["shares"][s["outcome"]] += filled
            st["usdc"][s["outcome"]] += usdc
        self.live_by_sid[s["sid"]] = "fill" if filled > 0 else "miss"
        if filled > 0 and avg and self.loop is not None:
            self.slip_stats[s["slip_c"]]["fills"] += 1
            self.loop.call_soon_threadsafe(self._schedule_markouts, s, avg)
        self.w.write("live_orders", (s["sid"], s["variant"], s["slug"], s["outcome"], s["t"], t_sent, t_resp,
                                     round(sign_ms, 1) if sign_ms else None, round(http_ms, 1) if http_ms else None,
                                     round(total_ms, 1), limit, size, self.mode, status, filled, usdc,
                                     round(avg, 4) if avg else None, oid, txs, err, raw))
        tag = f"[LIVE {self.mode}] #{s['sid']} BUY {s['outcome']} {size:.0f} @ {limit:.2f}"
        if abs(limit - s.get("ask_signal", limit)) > 1e-9:
            tag += f" (ask {s['ask_signal']:.2f} +{100 * (limit - s['ask_signal']):.0f}ц)"
        timing = ("готовый ордер" if s.get("presigned") else f"подпись {sign_ms:.0f} мс") if sign_ms is not None else ""
        if http_ms:
            timing += f", ответ сервера {http_ms:.0f} мс, от сигнала {total_ms:.0f} мс"
        if self.mode == "live":
            if filled > 0:
                emit(f"\033[95m{tag}\033[0m → ИСПОЛНЕНО {filled:.2f} шт по {avg:.3f} (${usdc:.2f}) | {timing}")
            elif status == "no_match":
                emit(f"\033[95m{tag}\033[0m → не исполнено: {err} | {timing}")
            elif err or status in ("exception", "error", "rejected_size"):
                emit(f"\033[95m{tag}\033[0m → ОШИБКА: {err or status} | {timing}")
            else:
                emit(f"\033[95m{tag}\033[0m → не исполнено ({status}) | {timing}")
        else:
            emit(f"\033[95m{tag}\033[0m → {status} {timing}")
        if self.ui is not None and getattr(self.ui, "chart", None) is not None and filled > 0:
            self.ui.chart.add_live(s["start"], t_resp - s["start"], avg, s["outcome"], filled)

    def _schedule_markouts(self, s, avg):
        for h in (5, 30):
            self.loop.call_later(h, self._markout, s, avg, h)

    def _markout(self, s, avg, h):
        win = self.pm.windows.get(s["start"])
        mid = None
        if win is not None:
            b = win.books[s["outcome"]]
            mid = b.mid()
            if mid is None and clock.now() > win.end:  # окно уже закончилось - маркаут посчитаем по итогу окна
                mid = None
        fee_ps = taker_fee(avg, 0.07)
        mk = None if mid is None else 100 * (mid - avg - fee_ps)
        self.w.write("live_markouts", (s["sid"], s["t"], s["slug"], s["outcome"], s["slip_c"], round(100 * s["edge"], 3),
                                       round(avg, 4), round(fee_ps, 5), h, mid, None if mk is None else round(mk, 3)))
        if mk is None:
            return
        ss = self.slip_stats[s["slip_c"]]
        if h == 30:
            ss["mk_sum"] += mk
            ss["mk_n"] += 1
        else:
            ss["mk5_sum"] += mk
            ss["mk5_n"] += 1
        col = "\033[92m" if mk > 0 else "\033[91m"
        emit(f"\033[95m[LIVE] #{s['sid']} (+{s['slip_c']}ц) через {h} с mid {mid:.3f} → \033[0m{col}{mk:+.1f}ц/шейр\033[0m")

    def slip_summary(self) -> str:
        parts = []
        for k in sorted(self.slip_stats):
            v = self.slip_stats[k]
            fr = v["fills"] / v["sent"] if v["sent"] else 0
            mk = f"{v['mk_sum'] / v['mk_n']:+.1f}ц" if v["mk_n"] else "n/a"
            parts.append(f"+{k}ц: {v['fills']}/{v['sent']} ({fr:.0%}), маркаут30с {mk}")
        return "; ".join(parts)

    def on_fill(self, f):
        if f["variant"] == self.c["variant"]:
            self.paper_by_sid.setdefault(f["sid"], {})[f["L"]] = f["status"]

    def on_markout(self, m):
        pass

    def on_settle(self, win, winner, used, results):
        st = self.win_stats.pop(win.slug, None)
        if not st or st["orders"] == 0:
            return
        payout = st["shares"][winner]
        usdc_est = sum(st["usdc"].values())
        fees_est = sum(taker_fee(st["usdc"][o] / st["shares"][o], 0.07) * st["shares"][o]
                       for o in ("Up", "Down") if st["shares"][o] > 0)
        pnl_est = payout - usdc_est - fees_est
        self.day_pnl += pnl_est
        # сравнение с бумагой по тем же сигналам
        sids = [sid for sid in self.live_by_sid if sid in self.paper_by_sid]
        lines = []
        for L in sorted({L for sid in sids for L in self.paper_by_sid[sid]}):
            both = [(self.live_by_sid[sid], self.paper_by_sid[sid].get(L)) for sid in sids
                    if self.paper_by_sid[sid].get(L)]
            if both:
                pf = sum(p == "fill" for _, p in both) / len(both)
                lines.append(f"бумага@{L}мс {pf:.0%}")
        lf = sum(v == "fill" for v in self.live_by_sid.values()) / max(1, len(self.live_by_sid))
        emit(f"\033[95m[LIVE] окно {datetime.fromtimestamp(win.start).strftime('%H:%M')}: ордеров {st['orders']}, "
             f"исполнено {st['filled']}; Up {st['shares']['Up']:.1f} / Down {st['shares']['Down']:.1f} шт; "
             f"победил {winner} → PnL ≈ {pnl_est:+.2f}$ (оценка) | за сутки {self.day_pnl:+.2f}$, "
             f"потрачено {self.day_spend:.2f}$\033[0m")
        emit(f"\033[95m[LIVE] доля исполнений с запуска: живые {lf:.0%} vs " + ", ".join(lines) + "\033[0m")
        if self.slip_stats:
            emit(f"\033[95m[LIVE] по переплате с запуска: {self.slip_summary()}\033[0m")
        row = [win.slug, winner, used, st["orders"], st["filled"], st["shares"]["Up"], st["shares"]["Down"],
               round(usdc_est + fees_est, 4)]
        if self.mode == "live" and st["cond"] and st["filled"] > 0:
            asyncio.get_running_loop().run_in_executor(self.pool, self._reconcile, row, st, winner, pnl_est)
        else:
            self.w.write("live_windows", tuple(row + [None, None, round(pnl_est, 4), None, round(self.day_pnl, 4)]))

    def _reconcile(self, row, st, winner, pnl_est):
        """Точные траты окна (с комиссиями) по данным Polymarket; сделки появляются там с задержкой."""
        import requests
        time.sleep(30)
        try:
            r = requests.get("https://data-api.polymarket.com/activity",
                             params={"user": self.c["funder"], "market": st["cond"], "type": "TRADE", "limit": 500},
                             headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
            acts = r.json()
            usdc = sum(float(a["usdcSize"]) for a in acts)
            fees = sum(float(a["usdcSize"]) - float(a["price"]) * float(a["size"]) for a in acts)
            shares_win = sum(float(a["size"]) for a in acts if a.get("outcome") == winner)
            pnl = shares_win - usdc
            self.day_pnl += pnl - pnl_est
            emit(f"\033[95m[LIVE] сверка с Polymarket: потрачено ${usdc:.2f} (комиссии ${fees:.2f}), "
                 f"PnL окна {pnl:+.2f}$ (оценка была {pnl_est:+.2f}$)\033[0m")
            self.w.write("live_windows", tuple(row + [round(usdc, 4), round(fees, 4), round(pnl_est, 4),
                                                      round(pnl, 4), round(self.day_pnl, 4)]))
        except Exception as ex:
            log("live", f"сверка не удалась: {ex!r}")
            self.w.write("live_windows", tuple(row + [None, None, round(pnl_est, 4), None, round(self.day_pnl, 4)]))

    def shutdown(self):
        if self.mode == "live" and self.client is not None:
            try:
                self.client.cancel_all()  # FAK не оставляет заявок, но на всякий случай
            except Exception:
                pass
        self.pool.shutdown(wait=False)
        self.presign_pool.shutdown(wait=False)


class Fanout:
    """Раздаёт события бумажного движка нескольким получателям (консоль бота + живой трейдер)."""

    def __init__(self, *targets):
        self.t = [x for x in targets if x is not None]

    def __getattr__(self, name):
        def call(*a, **k):
            for x in self.t:
                fn = getattr(x, name, None)
                if fn is not None:
                    try:
                        fn(*a, **k)
                    except Exception as ex:
                        log("bot", f"{type(x).__name__}.{name}: {ex!r}")
        return call
