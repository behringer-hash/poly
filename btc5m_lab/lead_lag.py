"""Есть ли в данных фьючерса Binance опережающий признак, на котором можно заработать с реальной задержкой ордера?

    python lead_lag.py data/2026-10-07 [--match-ms 205] [--slip-c 3] [--hold-s 5]

Событийная симуляция по сырым записям (`bnf_book`, `bnf_agg`, `bnf_liq`, `pm_top`, `windows`):
  * сигнал наблюдается в момент ПРИХОДА сообщения (recv_ms) - то есть с реальной задержкой ленты;
  * ордер доходит до движка Polymarket через --match-ms (отправка -> матч, по order_latency_test ~205 мс);
  * цена исполнения - лучший ask на сервере Polymarket в момент матча (время сервера = recv - d),
    а не тот ask, который мы видели при решении; если он выше увиденного + slip - промах;
  * результат: маркаут по mid через --hold-s секунд и расчёт по official_winner, комиссия 0.07*p*(1-p).
"""
from __future__ import annotations

import argparse
import glob
import os

import numpy as np
import pandas as pd

FEE = 0.07
CLOCK_OFFSET_MS = 18.0  # local - binance, из clock_*.csv; нужен только для оценок опережения по времени биржи


def read(root: str, stream: str, cols=None) -> pd.DataFrame:
    fs = sorted(glob.glob(os.path.join(root, f"{stream}_*.csv*")))
    if not fs:
        return pd.DataFrame()
    return pd.concat([pd.read_csv(f, usecols=cols, low_memory=False) for f in fs], ignore_index=True)


class PM:
    """Верх книги Up: bid/ask во времени сервера (recv-d) и во времени получения (recv)."""

    def __init__(self, root: str | pd.DataFrame):
        """root - папка с pm_top или уже загруженная таблица pm_top (recv_ms, d, w, o, bid, bid_sz, ask, ask_sz)."""
        t = read(root, "pm_top") if isinstance(root, str) else root
        t = t[t.o == "U"].copy()
        t["srv"] = t.recv_ms - t.d
        self.by_w = {}
        for w, g in t.groupby("w"):
            self.by_w[int(w)] = dict(
                srv=self._pack(g.sort_values("srv")), rcv=self._pack(g.sort_values("recv_ms"), key="recv_ms"))

    @staticmethod
    def _pack(g, key="srv"):
        return dict(t=g[key].values.astype(float), bid=g.bid.values, ask=g.ask.values,
                    bsz=g.bid_sz.values, asz=g.ask_sz.values)

    def state(self, w: int, t_ms: float, kind: str):
        """Последнее известное состояние верха книги Up к моменту t_ms: (bid, ask, bid_sz, ask_sz)."""
        s = self.by_w.get(w, {}).get(kind)
        if s is None:
            return None
        i = np.searchsorted(s["t"], t_ms, side="right") - 1
        if i < 0:
            return None
        return s["bid"][i], s["ask"][i], s["bsz"][i], s["asz"][i]


def futures(root: str):
    bk = read(root, "bnf_book").sort_values("E").reset_index(drop=True)
    bk["mid"] = (bk.bid + bk.ask) / 2
    bk["qi"] = (bk.bid_qty - bk.ask_qty) / (bk.bid_qty + bk.ask_qty)
    return bk


def rolling_sigma(bk: pd.DataFrame) -> np.ndarray:
    """σ $/√с: std секундных приращений mid за последние 5 минут (со сдвигом, без заглядывания вперёд)."""
    sec = (bk.E // 1000).astype(np.int64)
    last = bk.groupby(sec).mid.last()
    last = last.reindex(range(int(last.index.min()), int(last.index.max()) + 1)).ffill()
    sg = last.diff().rolling(300, min_periods=60).std().shift(1)
    s = sg.reindex(sec.values).values
    return np.where(np.isfinite(s) & (s > 0.3), s, 5.0)


def detect(bk: pd.DataFrame, sigma: np.ndarray, kind: str, param: float, win_ms: int = 300):
    """Индексы строк bnf_book и направление (+1/-1) для сигналов типа mom / qi (по фронту пересечения)."""
    E, mid, qi = bk.E.values, bk.mid.values, bk.qi.values
    if kind == "mom":
        j = np.searchsorted(E, E - win_ms, side="right") - 1
        j = np.clip(j, 0, None)
        move = mid - mid[j]
        thr = param * sigma * np.sqrt(win_ms / 1000)
        up, dn = move >= thr, move <= -thr
    elif kind == "qi":
        up, dn = qi >= param, qi <= -param
    else:
        raise ValueError(kind)
    out = []
    for sgn, m in ((1, up), (-1, dn)):
        edge = m & ~np.r_[False, m[:-1]]
        out += [(i, sgn) for i in np.flatnonzero(edge)]
    return sorted(out)


def simulate(bk, pm, off, sigs, match_ms, slip_c, hold_s, min_T=10, lo=0.10, hi=0.90, cooldown_ms=1000,
             feed_lag_ms=None, pm_lag_ms=25.0):
    """feed_lag_ms=None - решение в момент реального прихода сообщения (recv_ms); число - гипотетическая
    задержка ленты от события на бирже (E + смещение часов + feed_lag_ms), например 0 при размещении у биржи."""
    recv = bk.recv_ms.values if feed_lag_ms is None else bk.E.values + CLOCK_OFFSET_MS + feed_lag_ms
    rows, last = [], {}
    for i, sgn in sigs:
        t_dec = float(recv[i])
        w = int(t_dec // 1000 // 300 * 300)
        T = w + 300 - t_dec / 1000
        if T < min_T or t_dec / 1000 - w < 3:
            continue
        if t_dec - last.get((w, sgn), -1e18) < cooldown_ms:
            continue
        v = pm.state(w, t_dec, "rcv") if feed_lag_ms is None else pm.state(w, t_dec - pm_lag_ms, "srv")
        if v is None:
            continue
        bid, ask, _, asz = v
        view = ask if sgn > 0 else (1 - bid if np.isfinite(bid) else np.nan)
        if not np.isfinite(view) or not (lo <= view <= hi):
            continue
        last[(w, sgn)] = t_dec
        m = pm.state(w, t_dec + match_ms, "srv")
        e = pm.state(w, t_dec + match_ms + hold_s * 1000, "srv")
        if m is None or e is None:
            continue
        px = m[1] if sgn > 0 else (1 - m[0] if np.isfinite(m[0]) else np.nan)
        fill = bool(np.isfinite(px) and px <= view + slip_c / 100 + 1e-9)
        ex_mid = (e[0] + e[1]) / 2 if np.isfinite(e[0]) and np.isfinite(e[1]) else np.nan
        ex = ex_mid if sgn > 0 else 1 - ex_mid
        win = off.get(w)
        rows.append(dict(w=w, t=t_dec, T=T, sgn=sgn, view=view, px=px if fill else np.nan, fill=fill,
                         fee=FEE * px * (1 - px) if fill else np.nan, mk=ex - px if fill else np.nan,
                         won=(None if win is None else float((win == "Up") == (sgn > 0))) if fill else np.nan))
    return pd.DataFrame(rows)


def summarize(df: pd.DataFrame, label: str, n_boot=2000, seed=0):
    if df.empty:
        return dict(сигнал=label, сигн=0)
    f = df[df.fill & df.mk.notna()]
    mk_net = (f.mk - f.fee) * 100
    st = (f.won - f.px - f.fee) * 100
    w = df.assign(mk_net=np.where(df.fill & df.mk.notna(), (df.mk - df.fee) * 100, 0.0)).groupby("w").mk_net.agg(["sum", "size"])
    idx = np.random.default_rng(seed).integers(0, len(w), (n_boot, len(w)))
    bs = w["sum"].values[idx].sum(1) / w["size"].values[idx].sum(1)
    return {"сигнал": label, "сигн": len(df), "исполн": round(df.fill.mean(), 3), "окон": df.w.nunique(),
            "маркаут_ц/шейр": round(mk_net.mean(), 2) if len(f) else np.nan,
            "расчёт_ц/шейр": round(st.mean(), 2) if st.notna().any() else np.nan,
            "ц/сигнал": round(w["sum"].sum() / w["size"].sum(), 2),
            "ИИ-": round(np.percentile(bs, 2.5), 2), "ИИ+": round(np.percentile(bs, 97.5), 2)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--match-ms", type=float, default=205)
    ap.add_argument("--slip-c", type=float, default=3)
    ap.add_argument("--hold-s", type=float, default=5)
    ap.add_argument("--feed-lag-ms", type=float, default=None, help="гипотетическая задержка ленты (по умолчанию - реальная)")
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    bk, pm = futures(a.root), PM(a.root)
    wn = read(a.root, "windows").drop_duplicates("slug", keep="last")
    off = dict(zip(wn.start.astype(int), wn.official_winner))
    sg = rolling_sigma(bk)
    specs = [("mom", k) for k in (1.5, 2.5, 3.5, 5.0)] + [("qi", q) for q in (0.8, 0.9, 0.95, 0.98)]
    res = []
    for kind, p in specs:
        sigs = detect(bk, sg, kind, p)
        df = simulate(bk, pm, off, sigs, a.match_ms, a.slip_c, a.hold_s, feed_lag_ms=a.feed_lag_ms)
        res.append(summarize(df, f"{kind}{p}"))
    print(pd.DataFrame(res).to_string(index=False))


if __name__ == "__main__":
    main()
