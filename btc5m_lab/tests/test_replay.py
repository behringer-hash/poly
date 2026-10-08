"""Реплей на синтетических данных: проверяем направление сигнала, задержку исполнения, якорь и кулдаун."""
import numpy as np
import pandas as pd
import pytest

from lead_lag import PM
from replay import Params, collect_signals, execute, summarize

W = 3000                       # начало окна (кратно 300), секунды
T0 = W * 1000                  # то же в мс


def top(rows):
    """rows: (recv_ms, d, bid, ask, bsz, asz) для токена Up."""
    return pd.DataFrame([dict(recv_ms=r, d=d, w=W, o="U", bid=b, bid_sz=bs, ask=a, ask_sz=az, c=0)
                         for r, d, b, a, bs, az in rows])


def ticks(jump_at=None, jump=0.0, n=120):
    t = T0 + 5000 + np.arange(n) * 1000.0
    px = 100.0 + np.where(np.arange(n) % 2 == 0, 0.5, -0.5)      # шум ±0.5 -> sigma около 1
    if jump_at is not None:
        px = px + np.where(t >= jump_at, jump, 0.0)
    return t, px


def test_up_signal_and_latency_fill_vs_miss():
    t_jump = T0 + 100_000
    # книга стоит 0.49/0.51; через 200 мс после скачка ask уходит на 0.60
    pm_rows = [(T0 + 10_000, 20, .49, .51, 100, 100), (t_jump + 200, 20, .58, .60, 100, 100)]
    pt = top(pm_rows)
    t, px = ticks(t_jump, jump=15.0)
    sigs = collect_signals(pt, t, px, [Params(0.03)])
    ups = [s for s in sigs if s["sgn"] == 1]
    assert ups and not [s for s in sigs if s["sgn"] == -1]
    s = ups[0]
    assert s["t"] == t_jump and s["view"] == pytest.approx(0.51)
    df = execute(sigs, PM(pt), {W: "Up"}, [50, 400])
    fast = df[df.L == 50].iloc[0]
    slow = df[df.L == 400].iloc[0]
    assert fast.fill and fast.px == pytest.approx(0.51) and fast.settle > 40      # выигрыш Up: (1 - .51 - fee)
    assert not slow.fill                                                         # ask уже ушёл на 0.60 > лимита
    # с переплатой 10 ц медленный ордер исполняется по 0.60
    df2 = execute(collect_signals(pt, t, px, [Params(0.03, slip_c=10)]), PM(pt), {W: "Up"}, [400])
    assert df2.iloc[0].fill and df2.iloc[0].px == pytest.approx(0.60)


def test_down_signal_on_drop():
    t_jump = T0 + 100_000
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100)])
    t, px = ticks(t_jump, jump=-15.0)
    sigs = collect_signals(pt, t, px, [Params(0.03)])
    assert sigs and all(s["sgn"] == -1 for s in sigs)
    assert sigs[0]["view"] == pytest.approx(1 - 0.49)        # ask Down = 1 - bid Up


def test_anchor_resets_when_book_reprices():
    t_jump = T0 + 100_000
    # книга отыграла скачок через 100 мс: mid изменился -> якорь сдвинулся, повторных сигналов нет
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100), (t_jump + 100, 20, .72, .74, 100, 100)])
    t, px = ticks(t_jump, jump=15.0)
    sigs = collect_signals(pt, t, px, [Params(0.03)])
    assert [s["t"] for s in sigs] == [t_jump]                # только первый тик скачка, до репрайсинга


def test_cooldown_limits_repeated_signals():
    t_jump = T0 + 100_000
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100)])
    t, px = ticks(t_jump, jump=15.0)
    s1 = collect_signals(pt, t, px, [Params(0.03, cooldown_s=1.0)])
    s60 = collect_signals(pt, t, px, [Params(0.03, cooldown_s=60.0)])
    assert len(s60) < len(s1) and len(s60) >= 1


def test_no_signal_on_noise_and_thin_size_is_miss():
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 2)])         # на ask всего 2 шейра
    t, px = ticks()
    assert collect_signals(pt, t, px, [Params(0.03)]) == []
    t2, px2 = ticks(T0 + 100_000, 15.0)
    sigs = collect_signals(pt, t2, px2, [Params(0.03)])
    df = execute(sigs, PM(pt), {W: "Up"}, [50])
    assert sigs and not df.fill.any()                        # min_fill = 5, а объёма 2


def test_summarize_shapes():
    t_jump = T0 + 100_000
    pt = top([(T0 + 10_000, 20, .49, .51, 100, 100)])
    t, px = ticks(t_jump, 15.0)
    df = execute(collect_signals(pt, t, px, [Params(0.03)]), PM(pt), {W: "Up"}, [50, 300])
    out = summarize(df, n_boot=50)
    assert set(out.L) == {50, 300} and (out.исполн >= 0).all()
