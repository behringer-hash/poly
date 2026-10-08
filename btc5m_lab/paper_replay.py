"""Настоящий движок paper.py на виртуальном времени: те же классы Paper / Book / WindowState, что в живом боте.

    python paper_replay.py data/2026-10-08 --sources bybit,coinbase --primary bybit \
        --variants anc_3c_by:0.03:bybit,anc_2c_by:0.02:bybit [--latencies 50,150,300,600]

Вместо сети подаём в движок записанные события в порядке получения (recv_ms): изменения верха книги Up
(Down - зеркало) и тики источников цены BTC. Часы и call_later движка заменены виртуальными, поэтому
отложенные проверки исполнения и маркауты срабатывают в нужный момент записи, а не в реальное время.
Результат - те же таблицы paper_signals / paper_fills / paper_markouts / paper_windows, что пишет бот.

Отличия от живого запуска (честно):
  * книга состоит из одного лучшего уровня на сторону (глубина не записана) - исполнение по верхнему уровню;
  * "остаточный" якорь (anchor="residual") упрощён: якорь просто равен текущей цене источника;
  * book_lag_ms берётся из столбца d записи pm_top (лаг ленты Polymarket в момент сообщения).
"""
from __future__ import annotations

import argparse
import heapq
import itertools
import types

import numpy as np
import pandas as pd

import common
import paper as paper_mod
from config import Config, Variant
from lead_lag import read
from pm import WindowState
from replay import load_source


class VClock:
    def __init__(self):
        self.t = 0.0

    def now(self) -> float:
        return self.t


class VLoop:
    """Минимальная замена asyncio-цикла: только call_later, события выполняются по виртуальному времени."""

    def __init__(self, clk: VClock):
        self.clk, self.h, self.n = clk, [], itertools.count()

    def call_later(self, delay, fn, *args):
        heapq.heappush(self.h, (self.clk.t + delay, next(self.n), fn, args))

    def run_until(self, t: float):
        while self.h and self.h[0][0] <= t:
            ts, _, fn, args = heapq.heappop(self.h)
            self.clk.t = max(self.clk.t, ts)
            fn(*args)


class ListWriter:
    def __init__(self):
        self.rows: dict[str, list] = {}

    def write(self, stream, row):
        self.rows.setdefault(stream, []).append(tuple(row))


class FakePM:
    """Состояние, которое движок читает у процесса pm (см. paper.Paper.evaluate)."""

    def __init__(self, cfg):
        self.cfg = cfg
        self.windows: dict[int, WindowState] = {}
        self.src: dict[str, dict] = {}
        self.sigma = common.RollingSigma(900, cfg.sigma_fallback)
        self.bn_mid = None
        self.bn_recv = 0.0
        self.basis = None
        self.cl: dict = {}
        self.offset_ms = 0.0
        self.fut_qi = self.fut_qi_prev = None

    def current_window(self, ts):
        return self.windows.get(common.window_start(ts))

    def momentum_move(self, *a, **k):
        return None

    def momentum_sigma(self, *a, **k):
        return None


def parse_variants(spec: str) -> list[Variant]:
    out = []
    for item in spec.split(","):
        p = item.split(":")
        name, thr, src = p[0], float(p[1]), p[2]
        mult = float(p[3]) if len(p) > 3 else 1.0
        out.append(Variant(name, "anchor", thr, source=src, sigma_mult=mult))
    return out


def run(root_or_frames, sources: dict[str, tuple[np.ndarray, np.ndarray]], primary: str, variants: list[Variant],
        latencies: list[int], winners: dict[int, str], pm_top: pd.DataFrame | None = None) -> dict[str, pd.DataFrame]:
    saved = {k: getattr(paper_mod, k) for k in ("clock", "asyncio", "log", "emit")}
    clk, w_out = VClock(), ListWriter()
    loop = VLoop(clk)
    # подмена часов и цикла в модуле движка (на время прогона)
    paper_mod.clock = clk
    paper_mod.asyncio = types.SimpleNamespace(get_running_loop=lambda: loop)
    paper_mod.log = lambda *a, **k: None
    paper_mod.emit = lambda *a, **k: None
    try:
        return _run(root_or_frames, sources, primary, variants, latencies, winners, pm_top, clk, loop, w_out)
    finally:
        for k, v in saved.items():
            setattr(paper_mod, k, v)


def _run(root_or_frames, sources, primary, variants, latencies, winners, pm_top, clk, loop, w_out):
    cfg = Config()
    cfg.variants, cfg.latencies_ms, cfg.paper_btc_source, cfg.paper = variants, latencies, primary, True
    pm = FakePM(cfg)
    engine = paper_mod.Paper(cfg, pm, w_out)

    u = (read(root_or_frames, "pm_top") if pm_top is None else pm_top)
    u = u[u.o == "U"].sort_values("recv_ms", kind="stable")
    pt = u.recv_ms.values.astype(float)
    t_all = [pt]
    kind = [np.zeros(len(pt), np.int8)]
    for k, (name, (st, _)) in enumerate(sources.items()):
        t_all.append(st)
        kind.append(np.full(len(st), k + 1, np.int8))
    times, kinds = np.concatenate(t_all), np.concatenate(kind)
    order = np.argsort(times, kind="stable")
    offs = np.cumsum([0] + [len(x) for x in t_all])
    names = list(sources)
    pw, pd_, pbid, pbs, pask, pas = (u.w.values.astype(np.int64), u.d.values.astype(float), u.bid.values.astype(float),
                                     u.bid_sz.values.astype(float), u.ask.values.astype(float), u.ask_sz.values.astype(float))

    def on_book(j: int, t: float):
        w = int(pw[j])
        win = pm.windows.get(w)
        if win is None:
            win = pm.windows[w] = WindowState(w, {"up_token": "u", "down_token": "d"})
        up, dn = win.books["Up"], win.books["Down"]
        b, bs, a, as_ = pbid[j], pbs[j], pask[j], pas[j]
        up.bids = {b: bs} if np.isfinite(b) else {}
        up.asks = {a: as_} if np.isfinite(a) else {}
        dn.bids = {round(1 - a, 4): as_} if np.isfinite(a) else {}
        dn.asks = {round(1 - b, 4): bs} if np.isfinite(b) else {}
        for book in (up, dn):
            book.refresh_best()
            book.ready = True
            book.last_update = t
        win.book_lag_ms = pd_[j]
        price_moved = False
        for book in (up, dn):
            top = book.top()
            if top != book.last_top:
                price_moved = price_moved or book.last_top is None or top[0] != book.last_top[0] or top[2] != book.last_top[2]
                book.last_top = top
                mid = book.mid()
                if mid != book.last_mid:
                    book.last_mid = mid
                    book.anchor_btc = pm.bn_mid
                    book.anchor_px = {k: v["px"] for k, v in pm.src.items()}
                    book.anchor_px_res = dict(book.anchor_px)
                    book.anchor_ts = t
        if price_moved and win.ready():
            engine.evaluate(t, "book")

    def on_src(name: str, px: float, t: float):
        s = pm.src.setdefault(name, {"px": None, "recv": 0.0, "alive": 0.0})
        s["px"], s["recv"], s["alive"] = px, t, t
        if name == primary:
            pm.bn_mid, pm.bn_recv = px, t
            pm.sigma.update(t, px)
            engine.evaluate(t, "btc")
        else:
            engine.evaluate(t, name)

    for i in order:
        t = times[i] / 1000.0
        loop.run_until(t)
        clk.t = max(clk.t, t)
        k = int(kinds[i])
        if k == 0:
            on_book(i, t)
        else:
            name = names[k - 1]
            on_src(name, sources[name][1][i - offs[k]], t)
    loop.run_until(float("inf"))
    for w in sorted(pm.windows):
        if w in winners:
            engine.settle(pm.windows[w], winners[w], "official")
    return {s: pd.DataFrame(w_out.rows.get(s, []), columns=cols) for s, cols in paper_mod.PAPER_SCHEMAS.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--sources", default="binance_fut")
    ap.add_argument("--primary", default=None)
    ap.add_argument("--variants", required=True, help="имя:порог:источник[:sigma_mult],…")
    ap.add_argument("--latencies", default="50,150,300,600")
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    srcs = {n: load_source(a.root, n) for n in a.sources.split(",")}
    wn = read(a.root, "windows").drop_duplicates("slug", keep="last")
    winners = dict(zip(wn.start.astype(int), wn.official_winner))
    res = run(a.root, srcs, a.primary or a.sources.split(",")[0], parse_variants(a.variants),
              [int(x) for x in a.latencies.split(",")], winners)
    sg, fl, pw = res["paper_signals"], res["paper_fills"], res["paper_windows"]
    print(f"сигналов {len(sg)} в {sg.slug.nunique()} окнах; исполнений {int((fl.status == 'fill').sum())} из {len(fl)}")
    g = fl.groupby(["variant", "latency_ms"]).status.agg(сигн="size", исполн=lambda s: (s == "fill").mean())
    g["PnL_$"] = pw.groupby(["variant", "latency_ms"]).pnl.sum()
    print(g.round(3).to_string())


if __name__ == "__main__":
    main()
