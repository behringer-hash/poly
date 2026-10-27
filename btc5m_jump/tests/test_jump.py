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


def test_trigger_to_trader_end_to_end_dry():
    """Ход Binance -> JumpTrigger -> MakerTrader (dry): заявка ask + 1 по сильному сигналу, итог по книге через shadow_match_sec."""
    t, win = trader("dry", maker_price="ab", ab_modes=["ask", "ask1"], one_order_per_side=False, max_open_orders=100,
                    maker_life_sec=0.1, shadow_match_sec=0.05, variant="jump")
    win.end, win.book_lag_ms = win.start + 300, 10.0
    win.ready = lambda: True
    win.books["Up"].asks = {0.50: 3.0, 0.51: 20.0}
    win.books["Down"].asks = {0.52: 20.0}
    jump.clock = FakeClock(win.start + 150.0)
    jt = JumpTrigger(dict(variant="jump", jump_sigma_min_sec=0), t.pm, t.w, t)
    for s in jt.src.values():
        s.sig.sigma = lambda: 2.0

    async def go():
        jt.on_trade("fut", 0, 0, 100000.0)
        jt.on_trade("fut", 100, 0, 100008.0)
        await asyncio.sleep(0.6)
    run(go())
    orders = t.w.stream("maker_orders")
    assert len(orders) == 1 and orders[0][7] == 0.51 and orders[0][-1] == "ask1"
    sig = t.w.stream("jump_signals")
    assert len(sig) == 1 and sig[0][9] == "strong"
    fin = t.w.stream("maker_final")
    assert len(fin) == 1 and abs(fin[0][-1] - (3 * 0.50 + 2 * 0.51) / 5) < 1e-6


def test_weak_paused_after_strong_but_strong_not_after_weak():
    jt, win, rec = make()
    jt.on_trade("fut", 0, 0, 100000.0)
    jt.on_trade("fut", 100, 0, 100002.0)                  # слабый вверх
    jt.on_trade("fut", 200, 0, 100008.0)                  # сильный вверх через 0 с - не блокируется слабым
    assert [s["tier"] for s in rec.sigs] == ["weak", "strong"]
    jump.clock.t += 0.5
    jt.on_trade("fut", 700, 0, 100008.0)
    jt.on_trade("fut", 800, 0, 100010.0)                  # слабый через 0,5 с после сильного - пауза
    assert len(rec.sigs) == 2
    jump.clock.t += 0.6
    jt.on_trade("fut", 1400, 0, 100010.0)
    jt.on_trade("fut", 1500, 0, 100012.0)                 # через 1,1 с после сильного - можно
    assert [s["tier"] for s in rec.sigs] == ["weak", "strong", "weak"]
    jt.on_trade("fut", 1600, 0, 99990.0)                  # другая сторона (Down) - своя пауза
    assert rec.sigs[-1]["outcome"] == "Down"


def _panel_env(tmp_path=None):
    t, win = trader("dry", maker_price="ab", ab_modes=["ask", "ask1"], one_order_per_side=False, max_open_orders=100,
                    maker_life_sec=0.1, shadow_match_sec=0.05, variant="jump")
    win.end, win.book_lag_ms, win.ptb = win.start + 300, 120.0, 100000.0
    win.ready = lambda: True
    win.books["Up"].asks = {0.50: 30.0}
    win.books["Down"].asks = {0.52: 30.0}
    jump.clock = FakeClock(win.start + 150.0)
    t.pm.tw = {int(win.start + 148): 100012.4}
    t.pm.cl = {int(win.start + 149): 100013.0}
    jt = JumpTrigger(dict(variant="jump", jump_sigma_min_sec=0), t.pm, t.w, t)
    for s in jt.src.values():
        s.sig.sigma = lambda: 2.0
    return t, win, jt


def test_pulse_and_panel_render():
    import panel
    t, win, jt = _panel_env()
    panel.clock = jump.clock

    async def go():
        jt.on_trade("fut", 0, 0, 100000.0)
        jt.on_trade("fut", 100, 0, 100008.0)
        jt.on_trade("spot", 0, 0, 100003.0)
        jt.on_trade("spot", 50, 0, 100004.0)
        await asyncio.sleep(0.6)
    run(go())
    p = panel.MarketPanel(jt, t.pm, t, "dry", None, 1)
    x = p.snapshot(jump.clock.now())
    line = p.pulse_line(x)
    assert "Up 0.48/0.50" in line and "Down 0.50/0.52" in line and "TWAP60−PTB +12.4$" in line and "спот 100004.0" in line
    txt = p.panel_text(x)
    assert "ТРИГГЕР" in txt and "сильный от $" in txt and "ИСПОЛНЕНА" in txt and "ПОСЛЕДНИЕ СИГНАЛЫ" in txt
    print("\n" + line + "\n" + txt)


def test_panel_positions_pnl_and_chart():
    import random
    import panel
    t, win, jt = _panel_env()
    panel.clock = jump.clock

    async def go():
        jt.on_trade("fut", 0, 0, 100000.0)
        jt.on_trade("fut", 100, 0, 100008.0)          # сильный вверх -> Up 5 шт @0.50 тейкером
        jt.on_trade("spot", 0, 0, 100000.0)
        jt.on_trade("spot", 100, 0, 99992.0)          # сильный вниз -> Down 5 шт @0.52
        await asyncio.sleep(0.6)
    run(go())
    p = panel.MarketPanel(jt, t.pm, t, "dry", None, 1)
    pos = p.positions(jump.clock.now())
    assert len(pos) == 1 and pos[0]["qty"] == {"Up": 5.0, "Down": 5.0}
    assert abs(pos[0]["avg"]["Up"] - 0.50) < 1e-9 and abs(pos[0]["avg"]["Down"] - 0.52) < 1e-9
    txt = p.panel_text(p.snapshot(jump.clock.now()))
    assert "сумма средних 1.020" in txt and "ВРЕМЯ РАБОТЫ" in txt and "ИТОГО" in txt
    t.on_settle(win, "Up", "provisional", {})
    assert t.win_hist[-1]["pnl"] < 0 and not t.win_stats      # сумма средних > 1 + комиссии -> убыток при любом исходе
    random.seed(3)
    for i in range(25):
        t.win_hist.append(dict(slug=f"s{i}", start=win.start + 300 * (i + 1), winner="Up", pnl=random.uniform(-3, 4), pnl_api=None,
                               orders=5, filled=2, up=5, dn=0))
    t.win_hist[-1]["pnl_api"] = 9.0                         # сверка с Polymarket важнее оценки
    chart = p.pnl_chart(list(t.win_hist)[-20:])
    assert "последние 20" in chart[0] and "+9.00" in chart[1] and len(chart) == 1 + 4 + 1 + 4 + 1
    print("\n" + p.panel_text(p.snapshot(jump.clock.now())))
