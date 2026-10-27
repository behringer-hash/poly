"""Триггер хода Binance (jump.py) и заявки по ask / ask + 1 ц (live_maker.py)."""
import asyncio
import math
from statistics import NormalDist

import jump
from jump import JumpTrigger, Source, fair_shift
from test_live_maker import Book, Client, W, run, trader


class FakeClock:
    def __init__(self, t=0.0):
        self.t = t

    def now(self):
        return self.t


class FBook:
    def __init__(self, bb, ba, bsz=100.0, asz=100.0):
        self.bb, self.ba = bb, ba
        self.bids, self.asks = {bb: bsz}, {ba: asz}


class FWin:
    def __init__(self, start, up=(0.49, 0.51)):
        self.start, self.end, self.slug = start, start + 300, f"btc-updown-5m-{start}"
        self.book_lag_ms = 20.0
        self.books = {"Up": FBook(*up), "Down": FBook(round(1 - up[1], 2), round(1 - up[0], 2))}

    def ready(self):
        return True


class FPM:
    def __init__(self, win):
        self.win, self.offset_ms = win, 0.0

    def current_window(self, now):
        return self.win


class Rec:
    def __init__(self):
        self.sigs = []

    def on_signal(self, s):
        self.sigs.append(s)


def make(t_now=1000.0 + 150, up=(0.49, 0.51), sigma=2.0, **kw):
    """Окно 1000..1300, сейчас t_now; волатильность источника fut выставлена вручную."""
    jump.clock = FakeClock(t_now)
    win = FWin(1000, up)
    rec = Rec()
    cfg = dict(variant="jump", jump_sources=["fut", "spot"], jump_sigma_min_sec=0)
    cfg.update(kw)
    jt = JumpTrigger(cfg, FPM(win), W(), rec)
    for s in jt.src.values():
        s.sig.sigma = lambda sigma=sigma: sigma
    return jt, win, rec


def test_fair_shift_formula():
    T, sigma, dS, mid = 150.0, 2.0, 10.0, 0.5
    z = NormalDist().inv_cdf(mid)
    exp = math.exp(-z * z / 2) / math.sqrt(2 * math.pi) * dS / (sigma * math.sqrt(T - 40))
    assert abs(fair_shift(mid, T, sigma, dS) - exp) < 1e-12
    T = 30.0                                             # последняя минута: sd = sigma*sqrt(T^3/10800), w = T/60
    exp = math.exp(-z * z / 2) / math.sqrt(2 * math.pi) * (T / 60) * dS / (sigma * math.sqrt(T ** 3 / 10800))
    assert abs(fair_shift(mid, T, sigma, dS) - exp) < 1e-12
    assert fair_shift(0.5, 150, 2.0, -10.0) < 0


def test_source_price_before_uses_exchange_time():
    s = Source("fut", 2000)
    for t, p in ((1000, 100.0), (1050, 101.0), (1120, 103.0)):
        s.add(t, p)
    assert s.price_before(1100) == 101.0
    assert s.price_before(1000) == 100.0
    assert s.price_before(999) is None


def test_tiers_and_side():
    # T = 150 с, sigma 2, mid 0.5: dF = 0.3989 * dS / (2 * sqrt(110)) = 0.019 * dS
    jt, win, rec = make()
    jt.on_trade("fut", 0, 0, 100000.0)
    jt.on_trade("fut", 100, 0, 100002.0)                  # $2 за 100 мс -> 3,8 ц: слабая, по ask
    assert len(rec.sigs) == 1 and rec.sigs[0]["tier"] == "weak" and rec.sigs[0]["price_mode"] == "ask"
    assert rec.sigs[0]["outcome"] == "Up" and abs(rec.sigs[0]["edge"] - 0.019 * 2) < 0.001
    jt.on_trade("fut", 200, 0, 100008.0)                  # +$6 к цене 100 мс назад -> 11 ц: сильная, ask + 1
    assert len(rec.sigs) == 2 and rec.sigs[1]["tier"] == "strong" and rec.sigs[1]["price_mode"] == "ask1"
    jt.on_trade("spot", 0, 0, 100000.0)
    jt.on_trade("spot", 100, 0, 99990.0)                  # вниз -> Down
    assert rec.sigs[-1]["outcome"] == "Down" and rec.sigs[-1]["src"] == "spot" and rec.sigs[-1]["tier"] == "strong"


def test_refractory_per_window_side_tier_and_first_source():
    jt, win, rec = make()
    jt.on_trade("fut", 0, 0, 100000.0)
    jt.on_trade("fut", 100, 0, 100008.0)                  # сильный вверх (фьючерс)
    jt.on_trade("spot", 0, 0, 100000.0)
    jt.on_trade("spot", 110, 0, 100009.0)                 # тот же ход на споте - пауза (кто первый)
    assert len(rec.sigs) == 1 and rec.sigs[0]["src"] == "fut"
    jump.clock.t += 1.01                                  # через секунду - снова можно
    jt.on_trade("fut", 1200, 0, 100020.0)
    assert len(rec.sigs) == 2


def test_filters_time_bid_and_small_moves():
    jt, win, rec = make(t_now=1000.0 + 290)               # до конца окна 10 с < 12
    jt.on_trade("fut", 0, 0, 100000.0)
    jt.on_trade("fut", 100, 0, 100020.0)
    assert rec.sigs == [] and jt.stats["skip_time"] == 1
    jt, win, rec = make(up=(0.96, 0.97))                  # bid растущей стороны 0.96 > 0.95
    jt.on_trade("fut", 0, 0, 100000.0)
    jt.on_trade("fut", 100, 0, 100500.0)
    assert rec.sigs == []
    jt, win, rec = make()
    jt.on_trade("fut", 0, 0, 100000.0)
    jt.on_trade("fut", 100, 0, 100000.4)                  # меньше $0,5 - даже не рассматривается
    assert jt.stats["moves"] == 0
    jt.on_trade("fut", 300, 0, 100001.0)                  # +0,6 за 100 мс: 1,1 ц < 3 ц - не сигнал
    assert jt.stats["moves"] == 1 and rec.sigs == []


def test_stale_book_and_sigma_warmup_block():
    jt, win, rec = make()
    win.book_lag_ms = 5000.0
    jt.on_trade("fut", 0, 0, 100000.0)
    jt.on_trade("fut", 100, 0, 100020.0)
    assert rec.sigs == [] and jt.stats["skip_book"] == 1
    jt, win, rec = make(jump_sigma_min_sec=300)
    jt.on_trade("fut", 0, 0, 100000.0)
    jt.on_trade("fut", 100, 0, 100020.0)
    assert rec.sigs == [] and jt.stats["skip_sigma"] == 1


def test_quote_ask_and_ask1_are_plain_limits():
    cl = Client(matched="0")
    t, win = trader("live", cl, maker_price="ab", ab_modes=["ask", "ask1"], one_order_per_side=False, max_open_orders=100,
                     maker_life_sec=0.05, max_spend_per_window=1e9, max_shares_per_window=1e9)
    assert t.quote(Book(0.48, 0.50), "ask") == 0.50 and t.quote(Book(0.48, 0.50), "ask1") == 0.51
    assert t.quote(Book(0.97, 0.99), "ask1") == 0.99
    win.books["Up"].asks, win.books["Down"].asks = {0.50: 50.0}, {0.52: 50.0}

    async def go():
        t.on_signal(dict(sid=1, variant="c1", slug=win.slug, start=win.start, outcome="Up", t=0.0, T=100.0, edge=0.07, price_mode="ask1", tier="strong", src="fut", move=8.0))
        t.on_signal(dict(sid=2, variant="c1", slug=win.slug, start=win.start, outcome="Down", t=0.0, T=100.0, edge=0.04,
                         price_mode="ask", tier="weak", src="spot", move=-3.0))
        await asyncio.sleep(0.4)
    run(go())
    posted = {o["price"]: po for o, _, po in cl.posted}
    assert posted == {0.51: False, 0.52: False}           # Up ask 0.50 + 1 ц; Down ask 0.52; оба без post-only
    assert {e[-1] for e in t.w.stream("maker_orders")} == {"ask1", "ask"}


def test_shadow_taker_sweeps_levels_up_to_limit():
    t, win = trader("dry", maker_price="ask1", shadow_match_sec=0.05)
    b = win.books["Up"]
    b.asks = {0.50: 2.0, 0.51: 10.0}                       # на 0.50 только 2 шейра, остальное на 0.51

    async def go():
        t.on_signal(dict(sid=1, variant="c1", slug=win.slug, start=win.start, outcome="Up", t=0.0, T=100.0, edge=0.07,
                         price_mode="ask1"))
        await asyncio.sleep(0.5)
    run(go())
    fin = t.w.stream("maker_final")
    assert len(fin) == 1
    st = t.mstats
    assert st["filled"] == 1 and abs(st["shares"] - 5) < 1e-9
    assert abs(fin[0][-1] - (2 * 0.50 + 3 * 0.51) / 5) < 1e-6    # средняя цена тейкерской части
