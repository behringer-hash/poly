"""Тесты математики, на которой держатся все выводы: ошибка здесь молча портит анализ."""
import math
from types import SimpleNamespace

import pytest

from common import RollingSigma, norm_cdf, norm_inv, slug_for, taker_fee, window_start
from config import Config
from paper import Paper, settle_sd


def test_norm_roundtrip():
    for p in (0.01, 0.2, 0.5, 0.73, 0.99):
        assert norm_cdf(norm_inv(p)) == pytest.approx(p, abs=1e-9)
    assert norm_cdf(0) == 0.5


def test_taker_fee_shape():
    assert taker_fee(0.5, 0.07) == pytest.approx(0.0175)
    assert taker_fee(0.3, 0.07) == pytest.approx(taker_fee(0.7, 0.07))
    assert taker_fee(0.0, 0.07) == 0 and taker_fee(1.0, 0.07) == 0


def test_window_helpers():
    assert window_start(1791192089.3) == 1791192000
    assert slug_for(1791192000) == "btc-updown-5m-1791192000"


def test_settle_sd_continuous_at_60s():
    sigma = 3.0
    sd_hi, w_hi = settle_sd(60.0, sigma)
    sd_lo, w_lo = settle_sd(59.999, sigma)
    assert sd_hi == pytest.approx(sigma * math.sqrt(20))
    assert sd_lo == pytest.approx(sd_hi, rel=1e-3)
    assert w_hi == 1.0 and w_lo == pytest.approx(1.0, abs=1e-3)


def test_settle_sd_last_minute_shrinks_and_weights():
    sigma = 2.0
    sd30, w30 = settle_sd(30.0, sigma)
    assert w30 == pytest.approx(0.5)
    assert sd30 == pytest.approx(sigma * math.sqrt(30 ** 3 / (3 * 3600)))
    assert settle_sd(10.0, sigma)[0] < sd30 < settle_sd(60.0, sigma)[0]


def test_settle_sd_long_horizon():
    # T>=60: var = σ²(T-60) + σ²·60/3 = σ²(T-40)
    assert settle_sd(300.0, 1.0)[0] == pytest.approx(math.sqrt(260))


def test_rolling_sigma_unit_steps():
    rs = RollingSigma(window_sec=900, fallback=5.0)
    assert rs.sigma() == 5.0 and not rs.warm
    px, t0 = 100.0, 1_000_000.0
    for i in range(200):
        px += 1.0 if i % 2 == 0 else -1.0
        rs.update(t0 + i + 0.5, px)
    assert rs.warm
    assert rs.sigma() == pytest.approx(1.0, rel=0.05)


def _paper():
    return Paper(Config(), SimpleNamespace(), None)


def _win(ptb, end=1000):
    return SimpleNamespace(ptb=ptb, end=end)


def test_prob_up_abs_at_the_money_and_deep_itm():
    p = _paper()
    p.pm = SimpleNamespace(bn_mid=100_000.0, basis=0.0, offset_ms=0, cl={})
    assert p.prob_up_abs(_win(100_000.0), now=700.0, T=300.0, sigma=3.0) == pytest.approx(0.5)
    assert p.prob_up_abs(_win(99_000.0), now=700.0, T=300.0, sigma=3.0) > 0.999
    assert p.prob_up_abs(_win(101_000.0), now=700.0, T=300.0, sigma=3.0) < 0.001


def test_prob_up_abs_last_minute_uses_known_twap():
    p = _paper()
    end = 1000
    # первые 30 секунд TWAP-окна уже известны и сильно выше ptb; цена сейчас = ptb
    cl = {s: 100_050.0 for s in range(end - 60, end - 30)}
    p.pm = SimpleNamespace(bn_mid=100_000.0, basis=0.0, offset_ms=0, cl=cl)
    pr = p.prob_up_abs(_win(100_000.0, end), now=float(end - 30), T=30.0, sigma=1.0)
    assert pr > 0.99


def test_prob_up_abs_needs_inputs():
    p = _paper()
    p.pm = SimpleNamespace(bn_mid=None, basis=0.0, offset_ms=0, cl={})
    assert p.prob_up_abs(_win(1.0), 0.0, 100.0, 1.0) is None
    p.pm = SimpleNamespace(bn_mid=1.0, basis=None, offset_ms=0, cl={})
    assert p.prob_up_abs(_win(1.0), 0.0, 100.0, 1.0) is None
