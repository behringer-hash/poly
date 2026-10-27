"""Мейкерское исполнение (live_maker.py): цена заявки, лимиты, полный цикл постановка -> снятие -> учёт, теневое исполнение."""
import asyncio
import time

import live
from common import clock
from live_maker import MakerTrader


class Book:
    def __init__(self, bb, ba, bids=None):
        self.bb, self.ba, self.bids = bb, ba, dict(bids or {})


class Win:
    def __init__(self, up=(0.48, 0.50), dn=(0.50, 0.52)):
        self.start, self.slug = 3000, "btc-updown-5m-3000"
        self.m = dict(up_token="UT", down_token="DT", condition_id="C")
        self.books = {"Up": Book(*up, bids={up[0]: 100.0}), "Down": Book(*dn, bids={dn[0]: 100.0})}


class PM:
    def __init__(self, win):
        self.windows, self.offset_ms = {win.start: win}, 0.0
        self.w = win

    def current_window(self, now):
        return self.w


class W:
    def __init__(self):
        self.rows = []

    def write(self, stream, row):
        self.rows.append((stream, row))

    def stream(self, name):
        return [r for s, r in self.rows if s == name]


class Client:
    def __init__(self, matched="5", post_exc=None, post_delay=0.0):
        self.posted, self.canceled, self.market_cancels = [], [], []
        self.matched, self.post_exc, self.post_delay = matched, post_exc, post_delay

    def create_order(self, args, opts):
        return dict(args)

    def post_order(self, order, typ, post_only=False):
        time.sleep(self.post_delay)
        if self.post_exc:
            raise self.post_exc
        self.posted.append((order, typ, post_only))
        return dict(success=True, status="live", orderID=f"O{len(self.posted)}")

    def cancel_order(self, payload):
        self.canceled.append(payload["orderID"])
        return dict(canceled=[payload["orderID"]], not_canceled={})

    def get_order(self, oid):
        return dict(size_matched=self.matched, status="MATCHED" if self.matched not in ("0", 0) else "CANCELED")

    def cancel_market_orders(self, p):
        self.market_cancels.append(p)

    def cancel_all(self):
        pass


def trader(mode="live", client=None, **kw):
    c = dict(live.DEFAULTS, stop_file="/nonexistent/STOP", price_min=0.05, price_max=0.95, variant="c1", size=5,
             maker_life_sec=0.1, max_orders_per_window=40, max_shares_per_window=30, max_spend_per_window=15.0,
             max_spend_per_day=300.0, max_loss_per_day=60.0, min_seconds_left=10, min_interval_sec=0)
    c.update(kw)
    win = Win()
    t = MakerTrader(c, mode, PM(win), W())
    if client is not None:
        t.client = client
        t._OrderArgs = lambda **k: k
        t._Opts = lambda **k: k
        t._BUY = "BUY"
        t._OrderType = type("OT", (), {"GTD": "GTD", "GTC": "GTC"})
        t._OrderPayload = lambda orderID: dict(orderID=orderID)
        t._MarketCancel = lambda **k: k
    return t, win


def sig(outcome="Up", sid=1, T=100.0):
    return dict(sid=sid, variant="c1", slug="btc-updown-5m-3000", start=3000, outcome=outcome, t=clock.now(), T=T, edge=0.04)


def run(coro):
    return asyncio.run(coro)


def test_quote_join_improve_and_no_cross():
    t, _ = trader("dry", maker_price="improve")
    assert t.quote(Book(0.48, 0.50)) == 0.49            # спред 2 ц - встаём на 1 ц выше bid
    assert t.quote(Book(0.49, 0.50)) == 0.49            # спред 1 ц - лучший bid
    assert t.quote(Book(None, 0.50)) is None
    t2, _ = trader("dry", maker_price="join")
    assert t2.quote(Book(0.48, 0.50)) == 0.48


def test_live_cycle_post_only_cancel_and_accounting():
    cl = Client(matched="5")
    t, win = trader("live", cl)

    async def go():
        t.on_signal(sig())
        await asyncio.sleep(0.5)
    run(go())
    order, typ, post_only = cl.posted[0]
    assert post_only and typ == "GTD" and order["price"] == 0.49 and order["expiration"] > time.time() + 180
    assert cl.canceled == ["O1"]
    st = t.win_stats[win.slug]
    assert st["shares"]["Up"] == 5 and abs(st["usdc"]["Up"] - 5 * 0.49) < 1e-9 and st["pending"]["Up"] == 0
    assert abs(t.day_spend - 5 * 0.49) < 1e-9 and not t.open
    fin = t.w.stream("maker_final")[0]
    assert fin[3] == "O1" and fin[8] == "canceled" and fin[9] == 5.0


def test_unfilled_order_releases_reservation():
    cl = Client(matched="0")
    t, win = trader("live", cl)

    async def go():
        t.on_signal(sig())
        await asyncio.sleep(0.5)
    run(go())
    st = t.win_stats[win.slug]
    assert st["shares"]["Up"] == 0 and abs(st["spend"]) < 1e-9 and abs(t.day_spend) < 1e-9 and st["orders"] == 1


def test_one_open_order_per_side_and_limits():
    cl = Client(post_delay=0.2)
    t, win = trader("live", cl, maker_life_sec=0.5)

    async def go():
        t.on_signal(sig(sid=1))
        t.on_signal(sig(sid=2))                       # та же сторона, первая заявка ещё стоит
        t.on_signal(sig("Down", sid=3))               # другая сторона - можно
        t.on_signal(sig("Up", sid=4, T=5.0))          # мало времени (и сторона занята)
        await asyncio.sleep(1.2)
    run(go())
    assert [o["token_id"] for o, _, _ in cl.posted] == ["UT", "DT"]
    assert t.check_maker_limits(sig(T=5.0), t._new_st(), 0.49, 5) == "мало времени до конца окна"
    assert t.check_maker_limits(sig(), t._new_st(), 0.97, 5) == "цена вне диапазона"


def test_slow_post_is_cancelled_right_after_response():
    cl = Client(post_delay=0.3)
    t, _ = trader("live", cl, maker_life_sec=0.05)

    async def go():
        t.on_signal(sig())
        await asyncio.sleep(0.8)
    run(go())
    assert cl.canceled == ["O1"] and not t.open


def test_exception_on_post_cancels_token_and_stops_after_errors():
    cl = Client(post_exc=RuntimeError("timeout"))
    t, win = trader("live", cl, max_consecutive_errors=2)

    async def go():
        t.on_signal(sig(sid=1))
        await asyncio.sleep(0.3)
        t.on_signal(sig(sid=2))
        await asyncio.sleep(0.3)
    run(go())
    assert [p["asset_id"] for p in cl.market_cancels] == ["UT", "UT"]
    assert "ошибок подряд" in (t.stopped_reason or "")
    assert t.win_stats[win.slug]["pending"]["Up"] == 0


def test_dry_shadow_fill_queue_and_through():
    t, win = trader("dry")

    async def go():
        t.on_signal(sig("Up", sid=1))                 # bid Up 0.48, ask 0.50 -> заявка 0.49, впереди 0 (уровень пуст)
        t.on_signal(sig("Down", sid=2))               # bid Down 0.50, ask 0.52 -> 0.51
        await asyncio.sleep(0.02)
        e_up = next(o for o in t.open.values() if o["outcome"] == "Up")
        now_srv = clock.now() * 1000
        t.on_market_trade(win, "Up", "S", "0.49", "3", now_srv - 1000)    # до постановки - не считается
        t.on_market_trade(win, "Up", "S", "0.49", "3", now_srv + 10)      # у нашего уровня: 3 из 5
        assert abs(e_up["shadow_qty"] - 3) < 1e-9 and not e_up["shadow_done"]
        t.on_market_trade(win, "Down", "B", "0.51", "4", now_srv + 11)     # покупка Down по 1 - 0.49 - тоже наш уровень
        assert e_up["shadow_done"] and e_up["shadow_qty"] == 5
        t.on_market_trade(win, "Down", "S", "0.50", "1", now_srv + 12)     # продажа Down ниже 0.51 - сквозь уровень
        await asyncio.sleep(0.6)
    run(go())
    st = t.win_stats[win.slug]
    assert st["shares"]["Up"] == 5 and st["shares"]["Down"] == 5 and not t.open


def test_settle_has_no_fee_for_maker():
    t, win = trader("dry")
    st = t.win_stats.setdefault(win.slug, t._new_st())
    st.update(orders=2, filled=1)
    st["shares"]["Up"], st["usdc"]["Up"] = 5.0, 2.45

    async def go():
        t.on_settle(win, "Up", "provisional", {})
    run(go())
    assert abs(t.total_pnl - (5.0 - 2.45)) < 1e-9


def test_watchdog_halts_on_stuck_order():
    t, win = trader("live", Client(), maker_life_sec=0.0)
    t.watchdog_every = 0.02
    t.mode = "live"

    async def go():
        st = t.win_stats.setdefault(win.slug, t._new_st())
        st["pending"]["Up"] = 5
        t.open[9] = dict(sid=9, slug=win.slug, outcome="Up", t_signal=clock.now() - 100, q=0.49, size=5,
                                        oid="O9", shadow_qty=0.0, shadow_ms=None)
        task = asyncio.create_task(t.watchdog_loop())
        await asyncio.sleep(0.1)
        task.cancel()
    run(go())
    assert not t.open and "без итога" in (t.stopped_reason or "") and t.win_stats[win.slug]["pending"]["Up"] == 0


def test_several_orders_per_side_when_allowed():
    cl = Client(post_delay=0.05)
    t, win = trader("live", cl, maker_life_sec=0.3, one_order_per_side=False, max_open_orders=10)

    async def go():
        t.on_signal(sig(sid=1))
        t.on_signal(sig(sid=2))                        # та же сторона, первая заявка ещё стоит - всё равно ставим
        await asyncio.sleep(0.8)
    run(go())
    assert len(cl.posted) == 2 and sorted(cl.canceled) == ["O1", "O2"] and not t.open
    assert t.win_stats[win.slug]["shares"]["Up"] == 10


def test_test_only_config_refuses_live():
    import pytest
    with pytest.raises(SystemExit):
        trader("live", Client(), test_only=True)
    t, _ = trader("sign", None, test_only=True)          # sign и dry - можно
    assert t.mode == "sign"


def test_jump_bot_builds_config_without_c1_signals():
    import jump_bot
    cfg = jump_bot.build_cfg("d")
    assert cfg.variants == [] and cfg.latencies_ms == [] and cfg.paper and not cfg.backup_clob


def test_signal_engine_without_paper_fills_calls_listener():
    from types import SimpleNamespace
    import jump_bot
    from paper import Paper
    cfg = jump_bot.build_cfg("d")
    seen = []
    p = Paper(cfg, SimpleNamespace(), None)
    p.listener = SimpleNamespace(on_settle=lambda *a: seen.append(a))
    p.settle(SimpleNamespace(slug="x"), "Up", "provisional")
    assert p.acc == {} and len(seen) == 1


def test_ab_mode_ask_is_not_post_only_and_modes_alternate():
    import random
    random.seed(1)
    cl = Client(matched="0")
    t, win = trader("live", cl, maker_price="ab", one_order_per_side=False, max_open_orders=100, maker_life_sec=0.05,
                     max_spend_per_window=1e9, max_shares_per_window=1e9)

    async def go():
        for i in range(20):
            t.on_signal(sig(sid=i + 1))
        await asyncio.sleep(0.6)
    run(go())
    by_price = {o["price"]: po for o, _, po in cl.posted}
    assert by_price.get(0.50) is False and by_price.get(0.49) is True     # ask 0.50 - без post-only; bid+1 = 0.49 - post-only
    assert set(t.mode_stats) == {"improve", "ask"} and sum(v["orders"] for v in t.mode_stats.values()) == 20


def test_ask_mode_shadow_taker_fill_with_fee():
    t, win = trader("dry", maker_price="ask")
    win.books["Up"].asks = {0.50: 50.0}

    async def go():
        t.on_signal(sig("Up", sid=1))              # ask 0.50 на месте и объёма хватает -> исполнение сразу
        await asyncio.sleep(0.7)
    run(go())
    st = t.win_stats[win.slug]
    fee = 0.07 * 0.5 * 0.5 * 5
    assert st["shares"]["Up"] == 5 and abs(st["usdc"]["Up"] - (5 * 0.50 + fee)) < 1e-9
    fin = t.w.stream("maker_final")[0]
    assert fin[15] == "ask" and fin[16] == 1 and fin[17] == 0.50


def test_ask_mode_rests_as_bid_when_ask_moved():
    t, win = trader("dry", maker_price="ask", maker_life_sec=1.0)
    win.books["Up"].asks = {0.50: 50.0}

    async def go():
        t.on_signal(sig("Up", sid=1))
        e = next(iter(t.open.values()))
        now_srv = clock.now() * 1000
        t.on_market_trade(win, "Up", "S", "0.50", "5", now_srv + 20)    # пока биржа держит заявку - не считается
        win.books["Up"].ba, win.books["Up"].asks = 0.52, {0.52: 50.0}   # ask ушёл вверх
        await asyncio.sleep(0.4)
        assert not e["shadow_taker"] and not e["taker_wait"] and e["shadow_qty"] == 0
        t.on_market_trade(win, "Up", "S", "0.50", "5", clock.now() * 1000 + 10)   # продажа по нашей цене - исполнение мейкером
        await asyncio.sleep(1.2)
    run(go())
    st = t.win_stats[win.slug]
    assert st["shares"]["Up"] == 5 and abs(st["usdc"]["Up"] - 2.5) < 1e-9          # без комиссии
