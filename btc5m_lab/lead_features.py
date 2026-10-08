"""Информационная ценность признаков фьючерса Binance (и Bitstamp) для цены Up-токена Polymarket.

    python lead_features.py data/2026-10-07 [--match-ms 205] [--hold-s 5] [--grid-ms 200]

Выборка - моменты через каждые --grid-ms внутри окон (T от 10 до 290 с), без привязки к порогам. Для каждого
признака берём долю q самых сильных значений |f|, направление = знак f и смотрим:
  * info_ц - дрейф mid Up в нашу сторону за hold_s от момента решения (чистая информация, без спреда и комиссии);
  * net0_ц - прибыль после спреда и комиссии, если бы ордер исполнился мгновенно (match=0);
  * net_ц  - то же с реальной задержкой матча --match-ms (цена исполнения = ask сервера на момент матча).
Все признаки считаются по данным, доступным к моменту решения (по recv_ms), без заглядывания вперёд.
"""
from __future__ import annotations

import argparse
import math

import numpy as np
import pandas as pd

from lead_lag import FEE, PM, futures, read, rolling_sigma
from common import norm_cdf


def last_idx(t_sorted: np.ndarray, t: np.ndarray) -> np.ndarray:
    """Индекс последней записи с временем <= t (или -1)."""
    return np.searchsorted(t_sorted, t, side="right") - 1


def build_features(root: str, grid_ms: int):
    bk = futures(root).sort_values("recv_ms").reset_index(drop=True)
    sig = rolling_sigma(bk.sort_values("E").reset_index(drop=True))  # σ по времени биржи; ниже берём как скаляр по секундам
    # σ по секундам для быстрого доступа
    sec = (bk.recv_ms // 1000).astype(np.int64)
    sg = pd.Series(sig, index=(bk.sort_values("E").E // 1000).astype(np.int64).values)
    sg = sg[~sg.index.duplicated(keep="last")]
    rv, mid, qi = bk.recv_ms.values.astype(float), bk.mid.values, bk.qi.values

    ag = read(root, "bnf_agg").sort_values("recv_ms")
    a_t, a_q = ag.recv_ms.values.astype(float), ag.qty.values * np.where(ag.m.values == 0, 1.0, -1.0)
    cs_signed = np.r_[0, np.cumsum(a_q)]
    cs_abs = np.r_[0, np.cumsum(np.abs(a_q))]

    bs = read(root, "bs_trade").sort_values("recv_ms")
    b_t, b_p = bs.recv_ms.values.astype(float), bs.price.values

    dp = read(root, "bnf_depth5").sort_values("recv_ms")
    qsum = lambda col: dp[col].str.findall(r":([0-9.]+)").map(lambda xs: sum(map(float, xs))).values
    d_t = dp.recv_ms.values.astype(float)
    d_imb = (qsum("bids") - qsum("asks")) / (qsum("bids") + qsum("asks"))

    cl = read(root, "rtds")
    cl = cl[cl.feed == "cl"].sort_values("recv_ms")
    c_t, c_v = cl.recv_ms.values.astype(float), cl.value.values
    c_fut = mid[last_idx(rv, c_t).clip(0)]
    basis_s = pd.Series(c_v - c_fut).rolling(60, min_periods=10).median().values

    pm = PM(root)
    wn = read(root, "windows").drop_duplicates("slug", keep="last")
    ptb = dict(zip(wn.start.astype(int), wn.ptb_twap))
    t0, t1 = rv.min() + 400_000, rv.max() - 5_000
    grid = np.arange(t0, t1, grid_ms, dtype=float)
    rows = []
    for t in grid:
        w = int(t // 1000 // 300 * 300)
        T = w + 300 - t / 1000
        if T < 10 or T > 290:
            continue
        i = last_idx(rv, np.array([t]))[0]
        if i < 0:
            continue
        s = sg.get(int(t // 1000), np.nan)
        if not np.isfinite(s):
            continue
        f = dict(t=t, w=w, T=T)
        for W in (100, 300, 1000, 3000):
            j = max(last_idx(rv, np.array([t - W]))[0], 0)
            f[f"ret{W}"] = (mid[i] - mid[j]) / (s * math.sqrt(W / 1000))
        j = max(last_idx(rv, np.array([t - 300]))[0], 0)
        f["qi"], f["dqi300"] = qi[i], qi[i] - qi[j]
        for W in (200, 1000):
            lo, hi = np.searchsorted(a_t, t - W, side="right"), np.searchsorted(a_t, t, side="right")
            tot = cs_abs[hi] - cs_abs[lo]
            f[f"flow{W}"] = (cs_signed[hi] - cs_signed[lo]) / tot if tot > 0 else 0.0
        kb = last_idx(b_t, np.array([t, t - 300]))
        f["bs_ret300"] = (b_p[kb[0]] - b_p[kb[1]]) / (s * math.sqrt(0.3)) if kb.min() >= 0 else np.nan
        kd = last_idx(d_t, np.array([t]))[0]
        f["dep5"] = d_imb[kd] if kd >= 0 else np.nan
        # разрыв «справедливая вероятность по фьючерсу + базис к Chainlink - mid рынка» (только T >= 60)
        v = pm.state(w, t, "rcv")
        kc = last_idx(c_t, np.array([t]))[0]
        p0 = ptb.get(w)
        if T >= 60 and v is not None and kc >= 0 and p0 is not None and np.isfinite(p0) and np.isfinite(basis_s[kc]) \
                and np.isfinite(v[0]) and np.isfinite(v[1]):
            fair = norm_cdf((mid[i] + basis_s[kc] - p0) / (s * math.sqrt(T - 40.0)))
            f["gap"] = (fair - (v[0] + v[1]) / 2) * 10   # масштаб: 0.1 вероятности = 1.0
        rows.append(f)
    return pd.DataFrame(rows), pm


def outcomes(df: pd.DataFrame, pm: PM, match_ms: float, hold_s: float):
    """Для каждого момента: mid Up при решении, bid/ask Up на матче, mid Up на выходе."""
    out = {k: np.full(len(df), np.nan) for k in ("mid0", "bid_m", "ask_m", "bid_0", "ask_0", "mid_e", "mid_e0")}
    for n, (t, w) in enumerate(zip(df.t.values, df.w.values.astype(int))):
        v = pm.state(w, t, "rcv")
        m = pm.state(w, t + match_ms, "srv")
        z = pm.state(w, t, "srv")
        e = pm.state(w, t + match_ms + hold_s * 1000, "srv")
        e0 = pm.state(w, t + hold_s * 1000, "srv")
        if v is not None:
            out["mid0"][n] = (v[0] + v[1]) / 2
        if m is not None:
            out["bid_m"][n], out["ask_m"][n] = m[0], m[1]
        if z is not None:
            out["bid_0"][n], out["ask_0"][n] = z[0], z[1]
        if e is not None:
            out["mid_e"][n] = (e[0] + e[1]) / 2
        if e0 is not None:
            out["mid_e0"][n] = (e0[0] + e0[1]) / 2
    return pd.DataFrame(out)


def fee(p):
    return FEE * p * (1 - p)


def evaluate(df: pd.DataFrame, o: pd.DataFrame, feat: str, qs=(0.05, 0.02, 0.01), n_boot=1500):
    d = pd.concat([df.reset_index(drop=True), o], axis=1).dropna(subset=[feat, "mid0", "mid_e", "mid_e0"])
    res = []
    for q in qs:
        thr = d[feat].abs().quantile(1 - q)
        s = d[d[feat].abs() >= thr].copy()
        sg = np.sign(s[feat].values)
        # Up: купить по ask; Down: купить Down по 1 - bid
        px_m = np.where(sg > 0, s.ask_m, 1 - s.bid_m)
        px_0 = np.where(sg > 0, s.ask_0, 1 - s.bid_0)
        ex_m = np.where(sg > 0, s.mid_e, 1 - s.mid_e)
        ex_0 = np.where(sg > 0, s.mid_e0, 1 - s.mid_e0)
        info = sg * (s.mid_e0.values - s.mid0.values)
        net_m = ex_m - px_m - fee(px_m)
        net_0 = ex_0 - px_0 - fee(px_0)
        ok = np.isfinite(net_m) & (px_m >= 0.10) & (px_m <= 0.90)
        wsum = pd.DataFrame({"w": s.w.values, "v": np.where(ok, net_m, 0.0)}).groupby("w").v.agg(["sum", "size"])
        idx = np.random.default_rng(0).integers(0, len(wsum), (n_boot, len(wsum)))
        bs = wsum["sum"].values[idx].sum(1) / wsum["size"].values[idx].sum(1) * 100
        res.append(dict(признак=feat, доля=q, n=len(s), info_ц=100 * np.nanmean(info),
                        net0_ц=100 * np.nanmean(net_0[(px_0 >= 0.10) & (px_0 <= 0.90)]),
                        net_ц=100 * np.nanmean(net_m[ok]) if ok.any() else np.nan,
                        **{"ИИ-": np.percentile(bs, 2.5), "ИИ+": np.percentile(bs, 97.5)}))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--match-ms", type=float, default=205)
    ap.add_argument("--hold-s", type=float, default=5)
    ap.add_argument("--grid-ms", type=int, default=200)
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    df, pm = build_features(a.root, a.grid_ms)
    o = outcomes(df, pm, a.match_ms, a.hold_s)
    print(f"моментов {len(df)}, окон {df.w.nunique()}, match={a.match_ms} мс, hold={a.hold_s} с")
    feats = [c for c in df.columns if c not in ("t", "w", "T")]
    rows = []
    for f in feats:
        rows += evaluate(df, o, f)
    print(pd.DataFrame(rows).round(2).to_string(index=False))


if __name__ == "__main__":
    main()
