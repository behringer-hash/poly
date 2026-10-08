"""Тест задержек реальных ордеров Polymarket: где именно тратится время.

    python order_latency_test.py --config live_config_mm.json            # все тесты
    python order_latency_test.py --config live_config_mm.json --no-fill  # без реальных покупок (A, B, C)

Запускать на том же сервере, что и бот, при ОСТАНОВЛЕННОМ боте (иначе они мешают друг другу).

Тесты:
  A  сеть: GET /time по постоянному соединению (как у библиотеки)
  B  сеть + авторизация: запрос баланса с ключом API
  C  ордер, который НЕ исполняется: заявка BUY 5 шт по 0.01 + её отмена
  D  исполняемый ордер: покупка ~$1 по ask + 2ц (FAK); серверное время исполнения берём
     из потока сделок рынка по хэшу транзакции. Половина ордеров с defer_exec=True.
  E  то же, но обычным лимитным ордером (GTC), для сравнения типов
Во всех тестах отдельно меряется "чистый" HTTP-запрос и работа библиотеки после ответа.
Параллельно слушается приватный канал событий по своим ордерам (серверные метки времени).

Итог печатается таблицей и сохраняется в order_latency_<время>.json.
Стоимость: A-C бесплатно; D и E - около 20 покупок по ~$1 (потеря порядка $2-4 на спреде и
комиссии; купленные токены остаются позициями до резолва окна).
"""
from __future__ import annotations

import argparse
import asyncio
import json
import math
import os
import sys
import time
from datetime import datetime

import requests
import websockets

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import probe_clock  # noqa: E402
from live import load_config  # noqa: E402

H = {"User-Agent": "Mozilla/5.0"}


def q(xs, p):
    xs = sorted(x for x in xs if x is not None)
    return round(xs[min(len(xs) - 1, int(p * len(xs)))], 1) if xs else None


def now_ms():
    return time.time_ns() / 1e6


class Tester:
    def __init__(self, cfg, n_fill, max_spend):
        self.c = cfg
        self.n_fill = n_fill
        self.max_spend = max_spend
        self.spent = 0.0
        self.results = {}          # тест -> список словарей
        self.trades_by_tx = {}     # хэш транзакции -> (время сервера мс, время приёма мс)
        self.user_events = []      # события приватного канала
        self.offset = 0.0          # серверное время - локальное, мс
        self.loop = None
        self.resubscribe = False

    # ---------------------------------------------------------------- подключение
    def connect(self):
        from py_clob_client_v2 import ClobClient
        import py_clob_client_v2.client as CM
        self.CM = CM
        key = (open(self.c["private_key_file"]).read().strip() if self.c.get("private_key_file")
               else os.environ.get(self.c["private_key_env"], "").strip())
        if not key:
            raise SystemExit("нет приватного ключа (private_key_file или переменная окружения)")
        l1 = ClobClient("https://clob.polymarket.com", 137, key=key, signature_type=int(self.c["signature_type"]),
                        funder=self.c["funder"])
        try:
            self.creds = l1.derive_api_key()
        except Exception:
            self.creds = l1.create_api_key()
        self.cl = ClobClient("https://clob.polymarket.com", 137, key=key, creds=self.creds,
                             signature_type=int(self.c["signature_type"]), funder=self.c["funder"])
        try:
            src, off, rtt = probe_clock("https://api.binance.com")
            self.offset = off
            print(f"часы: смещение {off:+.1f} мс (по {src}, RTT {rtt:.0f} мс)")
        except Exception as ex:
            print(f"часы: замер не удался ({ex}); серверные времена без поправки")
        st = int(time.time() // 300 * 300)
        # если до конца окна меньше 2 минут - берём следующее
        if st + 300 - time.time() < 120:
            st += 300
            print("до конца текущего окна мало времени - жду следующее")
            while time.time() < st + 5:
                time.sleep(1)
        m = requests.get("https://gamma-api.polymarket.com/events", params={"slug": f"btc-updown-5m-{st}"},
                         headers=H, timeout=10).json()[0]["markets"][0]
        self.market = m
        self.condition = m["conditionId"]
        self.tokens = json.loads(m["clobTokenIds"])
        self.window_end = st + 300
        print(f"окно btc-updown-5m-{st}, до конца {self.window_end - time.time():.0f} с")
        from py_clob_client_v2 import AssetType, BalanceAllowanceParams
        p = BalanceAllowanceParams(asset_type=AssetType.COLLATERAL)
        self.cl.update_balance_allowance(p)
        bal = float(self.cl.get_balance_allowance(p).get("balance", 0) or 0) / 1e6
        print(f"баланс {bal:.2f} USDC")

    # ---------------------------------------------------------------- потоки событий
    async def market_ws(self):
        while True:
            try:
                async with websockets.connect("wss://ws-subscriptions-clob.polymarket.com/ws/market", ping_interval=10,
                                              max_queue=4096, max_size=2**23) as ws:
                    await ws.send(json.dumps({"type": "market", "assets_ids": self.tokens}))
                    subscribed = list(self.tokens)
                    async for raw in ws:
                        if self.tokens != subscribed:
                            break  # новое окно - переподключаемся с новыми токенами
                        recv = now_ms()
                        try:
                            d = json.loads(raw)
                        except Exception:
                            continue
                        for e in (d if isinstance(d, list) else [d]):
                            if e.get("event_type") == "last_trade_price" and e.get("transaction_hash"):
                                self.trades_by_tx[e["transaction_hash"].lower()] = (int(e["timestamp"]), recv)
            except Exception:
                await asyncio.sleep(1)

    async def user_ws(self):
        auth = {"apiKey": self.creds.api_key, "secret": self.creds.api_secret, "passphrase": self.creds.api_passphrase}
        while True:
            try:
                async with websockets.connect("wss://ws-subscriptions-clob.polymarket.com/ws/user", ping_interval=10,
                                              max_queue=4096) as ws:
                    await ws.send(json.dumps({"auth": auth, "type": "user", "markets": [self.condition]}))
                    cond = self.condition
                    async for raw in ws:
                        if self.condition != cond:
                            break
                        recv = now_ms()
                        try:
                            d = json.loads(raw)
                        except Exception:
                            continue
                        for e in (d if isinstance(d, list) else [d]):
                            if isinstance(e, dict):
                                self.user_events.append((recv, e))
            except Exception:
                await asyncio.sleep(1)

    # ---------------------------------------------------------------- низкоуровневая отправка
    def raw_post(self, order, order_type, defer_exec=False):
        """Отправка ордера с раздельным замером: чистый HTTP-запрос и работа библиотеки после ответа."""
        CM, cl = self.CM, self.cl
        owner = cl.creds.api_key
        payload = (CM.order_to_json_v2(order, owner, order_type, False, defer_exec) if CM._is_v2_order(order)
                   else CM.order_to_json_v1(order, owner, order_type, False, defer_exec))
        ser = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
        hdr = cl._l2_headers("POST", CM.POST_ORDER, body=payload, serialized_body=ser)
        t_send = now_ms()
        try:
            res = cl._post(f"{cl.host}{CM.POST_ORDER}", headers=hdr, data=ser)
            err = ""
        except Exception as ex:
            res, err = {}, str(getattr(ex, "error_msg", "") or ex)[:200]
        t_resp = now_ms()
        t_lib = t_resp
        if isinstance(res, dict) and not defer_exec and res.get("tradeIDs") and not res.get("transactionsHashes"):
            try:
                res = cl._resolve_transactions_hashes(res)   # то, что делает библиотека после ответа
            except Exception:
                pass
            t_lib = now_ms()
        return res, err, t_send, t_resp, t_lib

    def sign(self, token, price, size):
        from py_clob_client_v2 import OrderArgs, PartialCreateOrderOptions, Side
        return self.cl.create_order(OrderArgs(token_id=token, price=price, size=size, side=Side.BUY),
                                    PartialCreateOrderOptions(tick_size="0.01"))

    # ---------------------------------------------------------------- тесты
    def test_a(self, n=50):
        r = []
        self.cl.get_server_time()
        for _ in range(n):
            t0 = now_ms()
            self.cl.get_server_time()
            r.append({"rtt": now_ms() - t0})
            time.sleep(0.1)
        self.results["A сеть: GET /time"] = r

    def test_b(self, n=30):
        from py_clob_client_v2 import AssetType, BalanceAllowanceParams
        p = BalanceAllowanceParams(asset_type=AssetType.COLLATERAL)
        r = []
        for _ in range(n):
            t0 = now_ms()
            self.cl.get_balance_allowance(p)
            r.append({"rtt": now_ms() - t0})
            time.sleep(0.1)
        self.results["B сеть + авторизация: баланс"] = r

    def test_c(self, n=20):
        from py_clob_client_v2 import OrderPayload, OrderType
        r = []
        tok = self.tokens[0]
        for _ in range(n):
            order = self.sign(tok, 0.01, 5)
            res, err, ts, tr, tl = self.raw_post(order, OrderType.GTC)
            oid = (res or {}).get("orderID") or (res or {}).get("orderId")
            row = {"rtt": tr - ts, "status": (res or {}).get("status"), "err": err, "t_send": ts, "order_id": oid}
            if oid:
                t0 = now_ms()
                try:
                    self.cl.cancel_order(OrderPayload(orderID=oid))
                    row["cancel_rtt"] = now_ms() - t0
                except Exception as ex:
                    row["cancel_err"] = str(ex)[:120]
            r.append(row)
            time.sleep(0.3)
        self.results["C ордер без исполнения (0.01) + отмена"] = r

    def _next_window(self):
        """Окно заканчивается - переходим на следующее (токены, условие рынка)."""
        st = self.window_end
        print("  окно заканчивается - перехожу на следующее")
        while time.time() < st + 5:
            time.sleep(1)
        m = requests.get("https://gamma-api.polymarket.com/events", params={"slug": f"btc-updown-5m-{st}"},
                         headers=H, timeout=10).json()[0]["markets"][0]
        self.tokens = json.loads(m["clobTokenIds"])
        self.condition = m["conditionId"]
        self.window_end = st + 300
        self.resubscribe = True

    def best_ask(self, token):
        b = self.cl.get_order_book(token)
        asks = getattr(b, "asks", None) or (b.get("asks") if isinstance(b, dict) else [])
        prices = [float(getattr(a, "price", None) or a["price"]) for a in asks]
        return min(prices) if prices else None

    def test_fill(self, name, order_type, defer_flags):
        from py_clob_client_v2 import OrderType
        ot = getattr(OrderType, order_type)
        r = []
        i = 0
        tries = 0
        while i < self.n_fill and tries < self.n_fill * 6:
            tries += 1
            if time.time() > self.window_end - 20:
                self._next_window()
            # берём сторону, чей ask ближе к 0.5
            asks = [(self.best_ask(t), t) for t in self.tokens]
            asks = [(a, t) for a, t in asks if a and 0.05 <= a <= 0.93]
            if not asks:
                print("  подходящей цены нет (рынок у края) - жду")
                time.sleep(2)
                continue
            ask, tok = min(asks, key=lambda x: abs(x[0] - 0.5))
            limit = round(min(ask + 0.02, 0.97), 2)
            size = float(max(5, math.ceil(1.05 / limit)))
            if self.spent + limit * size > self.max_spend:
                print("  достигнут лимит трат теста")
                break
            order = self.sign(tok, limit, size)
            defer = defer_flags[i % len(defer_flags)]
            i += 1
            res, err, ts, tr, tl = self.raw_post(order, ot, defer_exec=defer)
            txs = [h.lower() for h in ((res or {}).get("transactionsHashes") or [])]
            filled = float((res or {}).get("takingAmount") or 0)
            self.spent += float((res or {}).get("makingAmount") or 0)
            r.append({"rtt": tr - ts, "lib_extra": tl - tr, "defer": defer, "status": (res or {}).get("status"),
                      "filled": filled, "txs": txs, "trade_ids": (res or {}).get("tradeIDs"), "err": err,
                      "t_send": ts, "t_resp": tr, "ask": ask, "limit": limit})
            oid = (res or {}).get("orderID") or (res or {}).get("orderId")
            if order_type == "GTC" and oid and (res or {}).get("status") not in ("matched",):
                try:  # остаток лимитного ордера не оставляем в книге
                    from py_clob_client_v2 import OrderPayload
                    self.cl.cancel_order(OrderPayload(orderID=oid))
                except Exception:
                    pass
            print(f"  {name}: {'defer ' if defer else ''}ответ {tr - ts:.0f} мс, после ответа библиотека ещё "
                  f"{tl - tr:.0f} мс, исполнено {filled:.2f} ({(res or {}).get('status') or err[:60]})")
            time.sleep(2)
        self.results[name] = r

    # ---------------------------------------------------------------- сведение
    def enrich(self):
        """Серверное время исполнения по хэшу транзакции (поток сделок рынка)."""
        for name, rows in self.results.items():
            for row in rows:
                for h in row.get("txs") or []:
                    if h in self.trades_by_tx:
                        srv, recv = self.trades_by_tx[h]
                        row["send_to_match"] = srv - (row["t_send"] + self.offset)
                        row["match_to_resp"] = (row["t_resp"] + self.offset) - srv
                        break

    def summary(self):
        print("\n==================== ИТОГ ====================")
        print(f"{'тест':45s} {'n':>3s} {'ответ p50':>10s} {'p90':>7s} {'мин':>7s}   дополнительно")
        out = {}
        for name, rows in self.results.items():
            rt = [x["rtt"] for x in rows if x.get("rtt") is not None]
            extra = []
            s2m = [x["send_to_match"] for x in rows if x.get("send_to_match") is not None]
            if s2m:
                extra.append(f"отправка->исполнение p50 {q(s2m, .5)} мс (мин {q(s2m, 0)})")
            m2r = [x["match_to_resp"] for x in rows if x.get("match_to_resp") is not None]
            if m2r:
                extra.append(f"исполнение->ответ p50 {q(m2r, .5)} мс")
            lib = [x["lib_extra"] for x in rows if x.get("lib_extra")]
            if lib:
                extra.append(f"библиотека после ответа p50 {q(lib, .5)} мс")
            cr = [x["cancel_rtt"] for x in rows if x.get("cancel_rtt")]
            if cr:
                extra.append(f"отмена p50 {q(cr, .5)} мс")
            for d in (False, True):
                sub = [x["rtt"] for x in rows if x.get("defer") is d and "defer" in x]
                if sub and any("defer" in x and x["defer"] for x in rows):
                    extra.append(f"{'defer' if d else 'обычный'}: ответ p50 {q(sub, .5)}")
            print(f"{name:45s} {len(rt):3d} {str(q(rt, .5)):>10s} {str(q(rt, .9)):>7s} {str(q(rt, 0)):>7s}   "
                  + "; ".join(extra))
            out[name] = rows
        ev = [(r, e.get("event_type"), e.get("type"), e.get("status"), e.get("timestamp"), e.get("matchtime"))
              for r, e in self.user_events]
        print(f"\nсобытий приватного канала: {len(ev)} (сохранены в файл для разбора)")
        fn = f"order_latency_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
        with open(fn, "w", encoding="utf-8") as f:
            json.dump({"offset_ms": self.offset, "results": out, "user_events": [
                {"recv": r, **e} for r, e in self.user_events]}, f, ensure_ascii=False, indent=1, default=str)
        print(f"сохранено в {fn} - пришлите этот файл")


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="live_config_mm.json")
    ap.add_argument("--no-fill", action="store_true", help="только бесплатные тесты A, B, C")
    ap.add_argument("--n-fill", type=int, default=10, help="исполняемых ордеров в каждом из тестов D и E")
    ap.add_argument("--max-spend", type=float, default=30.0, help="потолок трат на тесты D и E, $")
    a = ap.parse_args()
    cfg = load_config(a.config)
    t = Tester(cfg, a.n_fill, a.max_spend)
    t.connect()
    if not a.no_fill:
        print(f"\nТесты D и E купят до {2 * a.n_fill} раз по ~$1 (потолок ${a.max_spend:.0f}). "
              f"Убедитесь, что бот остановлен.")
        if input("Введите ДА, чтобы продолжить: ").strip().upper() != "ДА":
            a.no_fill = True
            print("исполняемые тесты пропущены")
    loop = asyncio.get_running_loop()
    feeds = [asyncio.create_task(t.market_ws()), asyncio.create_task(t.user_ws())]
    await asyncio.sleep(3)  # дать потокам подключиться

    def run_tests():
        print("\nA: сеть...")
        t.test_a()
        print("B: сеть + авторизация...")
        t.test_b()
        print("C: ордер без исполнения + отмена...")
        t.test_c()
        if not a.no_fill:
            print("D: исполняемый FAK (половина с defer_exec)...")
            t.test_fill("D исполняемый FAK", "FAK", [False, True])
            print("E: исполняемый обычный лимитный (GTC)...")
            t.test_fill("E исполняемый GTC", "GTC", [False])
    await loop.run_in_executor(None, run_tests)
    await asyncio.sleep(3)  # дождаться последних событий о сделках
    for f in feeds:
        f.cancel()
    t.enrich()
    t.summary()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
