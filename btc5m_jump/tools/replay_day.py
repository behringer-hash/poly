"""Прогон триггера бота (jump.py) по записи сборщика btc5m_lab: какие сигналы дал бы бот в Стокгольме.

    python3 tools/replay_day.py /home/lab/data/2026-10-20 ... --out OUT

Решение - в момент получения сделки Binance (recv_ms), книга Polymarket - такая, какой она до нас доходила (pm_top, recv_ms),
время биржи сделки - T. Три настройки ступеней: только 3 ц, только 6 ц (для сверки с n_ev симуляции mm_trig3, профиль
stockholm) и рабочая 3 ц / 6 ц. Выход: jr_counts.csv (сигналов по дню и настройке) и jr_<день>.csv.gz (сигналы рабочей настройки).
"""
from __future__ import annotations

import argparse
import glob
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

import jump  # noqa: E402


def read(root, stream, cols=None):
    fs = sorted(glob.glob(os.path.join(root, f"{stream}_*.csv*")))
    out = []
    for f in fs:
        try:
            d = pd.read_csv(f, usecols=cols, low_memory=False)
        except pd.errors.EmptyDataError:
            continue
        if cols:
            for c in cols:
                d = d[d[c].astype(str) != c]          # повторные заголовки после перезапуска сборщика
        out.append(d)
    return pd.concat(out, ignore_index=True) if out else pd.DataFrame()


class Clock:
    t = 0.0

    def now(self):
        return self.t


class FB:
    __slots__ = ("bb", "ba", "bids", "asks")

    def __init__(self):
        self.bb = self.ba = None
        self.bids, self.asks = {}, {}


class FW:
    def __init__(self, start):
        self.start, self.end, self.slug = start, start + 300, f"btc-updown-5m-{start}"
        self.book_lag_ms = None
        self.books = {"Up": FB(), "Down": FB()}

    def ready(self):
        return True


class FPM:
    """Окно и книга на момент clock.t по записи pm_top (время получения)."""

    def __init__(self, top: pd.DataFrame, clock: Clock):
        self.clock, self.offset_ms = clock, 0.0
        t = top[top.o == "U"]
        self.by = {}
        for w, g in t.groupby("w"):
            g = g.sort_values("recv_ms", kind="stable")
            self.by[int(w)] = (g.recv_ms.values.astype(float), np.round(g.bid.values.astype(float), 2),
                               np.round(g.ask.values.astype(float), 2), g.bid_sz.values.astype(float), g.ask_sz.values.astype(float))
        self.wins = {}

    def current_window(self, now):
        st = int(now // 300 * 300)
        x = self.by.get(st)
        if x is None:
            return None
        i = int(np.searchsorted(x[0], now * 1000.0, side="right") - 1)
        if i < 0:
            return None
        win = self.wins.get(st) or self.wins.setdefault(st, FW(st))
        bid, ask, bsz, asz = x[1][i], x[2][i], x[3][i], x[4][i]
        u, d = win.books["Up"], win.books["Down"]
        ok = np.isfinite(bid) and np.isfinite(ask)
        u.bb, u.ba = (bid, ask) if ok else (None, None)
        d.bb, d.ba = (round(1 - ask, 2), round(1 - bid, 2)) if ok else (None, None)
        u.bids, u.asks, d.bids, d.asks = {u.bb: bsz}, {u.ba: asz}, {d.bb: asz}, {d.ba: bsz}
        return win


class Wr:
    def __init__(self):
        self.rows = []

    def write(self, s, r):
        if s == "jump_signals":
            self.rows.append(r)


CONFIGS = {"only3": dict(jump_thr_weak=0.03, jump_thr_strong=9.0), "only6": dict(jump_thr_weak=0.06, jump_thr_strong=9.0),
           "prod": dict(jump_thr_weak=0.03, jump_thr_strong=0.06)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    counts = []
    for root in a.roots:
        day = os.path.basename(os.path.normpath(root))
        top = read(root, "pm_top", ["recv_ms", "w", "o", "bid", "bid_sz", "ask", "ask_sz"])
        if top.empty:
            print(f"{day}: нет pm_top", flush=True)
            continue
        for c in ("recv_ms", "w", "bid", "bid_sz", "ask", "ask_sz"):
            top[c] = pd.to_numeric(top[c], errors="coerce")
        tr = []
        for name, stream in (("fut", "bnf_agg"), ("spot", "bn_agg")):
            d = read(root, stream, ["recv_ms", "T", "price"])
            for c in d.columns:
                d[c] = pd.to_numeric(d[c], errors="coerce")
            d = d.dropna()
            d["src"] = name
            tr.append(d)
        tr = pd.concat(tr, ignore_index=True).sort_values(["recv_ms", "T"], kind="stable")
        clock = Clock()
        jump.clock = clock
        pm = FPM(top, clock)
        del top
        trig = {k: JT(k, v, pm) for k, v in CONFIGS.items()}
        rcv, T, px, src = tr.recv_ms.values, tr["T"].values, tr.price.values, tr.src.values
        print(f"{day}: сделок {len(tr)} (фьючерс {(src == 'fut').sum()}, спот {(src == 'spot').sum()})", flush=True)
        for i in range(len(tr)):
            clock.t = rcv[i] / 1000.0
            for jt in trig.values():
                jt.on_trade(src[i], float(T[i]), clock.t, float(px[i]))
        for k, jt in trig.items():
            st = jt.stats
            counts.append(dict(day=day, cfg=k, strong=st["strong"], weak=st["weak"], moves=st["moves"], skip_book=st["skip_book"],
                               skip_time=st["skip_time"], skip_price=st["skip_price"], skip_sigma=st["skip_sigma"]))
            print(f"  {k}: сильных {st['strong']}, слабых {st['weak']} | {st}", flush=True)
        d = pd.DataFrame(trig["prod"].w.rows, columns=jump.JUMP_SCHEMAS["jump_signals"])
        d.to_csv(os.path.join(a.out, f"jr_{day}.csv.gz"), index=False)
    pd.DataFrame(counts).to_csv(os.path.join(a.out, "jr_counts.csv"), index=False)


def JT(name, over, pm):
    cfg = dict(variant="jump", jump_sigma_min_sec=0, **over)
    return jump.JumpTrigger(cfg, pm, Wr(), None)


if __name__ == "__main__":
    main()
