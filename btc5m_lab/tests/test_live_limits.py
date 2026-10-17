import live
from live import DEFAULTS, LiveTrader


class Clk:
    def __init__(self):
        self.t = 1000.0

    def now(self):
        return self.t


def trader(**kw):
    c = dict(DEFAULTS, stop_file="/nonexistent/STOP", price_min=0.05, price_max=0.95, **kw)
    return LiveTrader(c, "dry", None, None)


def sig(T=100.0, ask=0.30, outcome="Up"):
    return dict(limit=ask + 0.03, ask_signal=ask, T=T, outcome=outcome)


def st():
    return dict(orders=0, filled=0, spend=0.0, shares={"Up": 0.0, "Down": 0.0}, usdc={"Up": 0.0, "Down": 0.0}, cond=None)


def test_old_behaviour_after_any_order(monkeypatch):
    clk = Clk()
    monkeypatch.setattr(live, "clock", clk)
    t = trader(min_interval_sec=10)
    t.last_order_t = clk.t - 5
    assert t._check_limits(sig(), st()) == "слишком часто"
    t.last_order_t = clk.t - 11
    assert t._check_limits(sig(), st()) is None


def test_pause_after_fill_only(monkeypatch):
    clk = Clk()
    monkeypatch.setattr(live, "clock", clk)
    t = trader(min_interval_sec=1, min_interval_after_fill_sec=10)
    t.last_order_t = clk.t - 2                       # был пустой ордер 2 с назад - можно
    assert t._check_limits(sig(), st()) is None
    t.last_order_t = clk.t - 0.5                     # ордер ещё «летит»
    assert t._check_limits(sig(), st()) == "слишком часто"
    t.last_order_t, t.last_fill_t = clk.t - 2, clk.t - 5   # недавно купили
    assert t._check_limits(sig(), st()) == "слишком часто после исполнения"
    t.last_fill_t = clk.t - 11
    assert t._check_limits(sig(), st()) is None


class FakeW:
    def __init__(self):
        self.rows = []

    def write(self, stream, row):
        self.rows.append((stream, row))


class NoMatch(Exception):
    error_msg = "no orders found to match with FAK order"


def send_one(monkeypatch, resp_or_exc, **kw):
    clk = Clk()
    monkeypatch.setattr(live, "clock", clk)
    t = trader(**kw)
    t.mode, t.w = "live", FakeW()

    class Client:
        def create_order(self, *a, **k):
            return "ORD"

        def post_order(self, order, typ):
            if isinstance(resp_or_exc, Exception):
                raise resp_or_exc
            return resp_or_exc

    t.client = Client()
    t._OrderArgs = lambda **k: k
    t._Opts = lambda **k: k
    t._BUY, t._OrderType = "BUY", type("OT", (), {"FAK": "FAK"})
    s = dict(sid=1, variant="c1", slug="x", outcome="Up", t=clk.t, start=0, limit=0.33, ask_signal=0.30, slip_c=3, base_size=5)
    t.slip_stats[3] = dict(sent=1, fills=0, mk_sum=0.0, mk_n=0, mk5_sum=0.0, mk5_n=0)
    stt = st()
    stt["orders"] = 1
    t._send(s, "tok", stt, 1.7)
    return t, stt


def test_unfilled_slot_released_only_when_configured(monkeypatch):
    _, s1 = send_one(monkeypatch, NoMatch(), count_unfilled_orders=False)
    assert s1["orders"] == 0
    _, s2 = send_one(monkeypatch, NoMatch(), count_unfilled_orders=True)
    assert s2["orders"] == 1
    _, s3 = send_one(monkeypatch, RuntimeError("timeout"), count_unfilled_orders=False)
    assert s3["orders"] == 1                                       # неизвестный исход - место не освобождаем


def test_fill_sets_last_fill_t(monkeypatch):
    t, s = send_one(monkeypatch, dict(success=True, status="matched", makingAmount="1.1", takingAmount="5"),
                    min_interval_after_fill_sec=10)
    assert t.last_fill_t == 1000.0 and s["filled"] == 1 and s["orders"] == 1


def test_total_loss_survives_midnight(monkeypatch):
    clk = Clk()
    monkeypatch.setattr(live, "clock", clk)
    t = trader(max_loss_per_day=1e9, max_loss_total=25.0)
    t.day_pnl, t.total_pnl = -10.0, 5.0              # день плохой, но с запуска мы в плюсе
    assert t._check_limits(sig(), st()) is None
    t.total_pnl = -25.0
    assert "общий убыток" in t._check_limits(sig(), st())
    t.day = None                                      # наступили новые сутки: общий стоп не снимается
    assert "общий убыток" in t._check_limits(sig(), st())


def test_total_loss_off_by_default(monkeypatch):
    clk = Clk()
    monkeypatch.setattr(live, "clock", clk)
    t = trader(max_loss_per_day=1e9)
    t.total_pnl = -1000.0
    assert t._check_limits(sig(), st()) is None
