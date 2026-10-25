"""На чём зарабатывает C1: устаревшая цена или моментум. Только выгрузка компактных данных, статистика считается отдельно.

    python edge_source.py data/2026-10-12 data/2026-10-13 ... --live-dirs /home/lab/incoming/bot_data_c1 ... --out OUT

По каждому дню пишет в OUT (gzip CSV, каждый файл < 2 МБ):
  sig_<день>.csv.gz   - сигналы C1 (порог 3,5 ц, sigma x1, Bybit) при якоре со сдвигом d = 0/50/100/200/400 мс
                        после изменения книги (d = 0 - как в боте). По каждому сигналу: цена, которую видел бот (view),
                        mid и ask стороны по книге СЕРВЕРА через h мс, исход окна.
  base_<день>.csv.gz  - состояния окна каждые 5 с без всякого сигнала: книга Up сервера в момент t и через 335 мс,
                        цена Bybit (как пришла к нам) сейчас и 2/10/30/60 с назад, sigma, ptb, исход.
                        По ним видно, предсказывает ли недавний ход BTC исход сверх цены токена (моментум) и есть ли
                        постоянная ошибка цены по корзинам цены и T.
  live_orders.csv.gz  - все живые ордера с mid/ask стороны по книге сервера через h мс после сигнала и исходом.
Ничего не торгует и не меняет.
"""
from __future__ import annotations

import argparse
import gc
import os

import numpy as np
import pandas as pd

from common import RollingSigma, norm_cdf, norm_inv
from lead_lag import FEE, PM, read
from paper import settle_sd
from replay import load_source

WINDOW = 300
DELAYS = (0, 50, 100, 200, 400)
H_FULL = (0, 100, 200, 335, 500, 1000, 2000, 5000, 15000, 30000, 60000)
H_ASK = (335, 1000, 2000, 5000)
H_LIVE = (0, 335, 1000, 2000, 5000, 30000)


def collect(pm_top: pd.DataFrame, src_t: np.ndarray, src_px: np.ndarray, thr: float = 0.035, sigma_mult: float = 1.0,
            delays=DELAYS, cooldown_ms: float = 1000, max_age_ms: float = 1000, max_book_lag_ms: float = 400,
            min_T: float = 5, min_elapsed: float = 3, lo: float = 0.05, hi: float = 0.95) -> list[dict]:
    """Как replay.collect_signals, но якорь берётся по цене источника через d мс после изменения mid книги
    (до этого момента сигналов нет). d = 0 совпадает с ботом."""
    u = pm_top[pm_top.o == "U"].sort_values("recv_ms", kind="stable")
    pt, pw = u.recv_ms.values.astype(float), u.w.values.astype(np.int64)
    pbid, pask, pdl = u.bid.values.astype(float), u.ask.values.astype(float), u.d.values.astype(float)
    times = np.concatenate([pt, src_t])
    kind = np.concatenate([np.zeros(len(pt), np.int8), np.ones(len(src_t), np.int8)])
    order = np.argsort(times, kind="stable")
    rs = RollingSigma(900, 5.0)
    out: list[dict] = []
    last_sig: dict = {}
    inv_cache: dict = {}
    st = dict(bid=np.nan, ask=np.nan, mid=np.nan, d=0.0, w=-1, tb=None, a0=None, px=None, ts=None)
    n_pm = len(pt)

    def evaluate(t: float):
        if st["tb"] is None or st["px"] is None or not (np.isfinite(st["bid"]) and np.isfinite(st["ask"])):
            return
        w = int(t // 1000 // WINDOW * WINDOW)
        if w != st["w"] or t - st["ts"] > max_age_ms or st["d"] > max_book_lag_ms:
            return
        T = w + WINDOW - t / 1000
        if T < min_T or t / 1000 - w < min_elapsed:
            return
        sd, wgt = settle_sd(T, rs.sigma())
        for d in delays:
            ta = st["tb"] + d
            if t < ta:
                continue
            if d == 0:
                anchor = st["a0"]
            else:
                i = np.searchsorted(src_t, ta, side="right") - 1
                if i < 0:
                    continue
                anchor = src_px[i]
            dS = st["px"] - anchor
            for sgn in (1, -1):
                a = st["ask"] if sgn > 0 else 1 - st["bid"]
                b = st["bid"] if sgn > 0 else 1 - st["ask"]
                if not (lo <= a <= hi):
                    continue
                m = round((a + b) / 2, 6)
                z0 = inv_cache.get(m)
                if z0 is None:
                    z0 = inv_cache[m] = norm_inv(m)
                edge = norm_cdf(z0 + sgn * wgt * dS / (sd * sigma_mult)) - a - FEE * a * (1 - a)
                if edge < thr:
                    continue
                key = (d, w, sgn)
                if t - last_sig.get(key, -1e18) < cooldown_ms:
                    continue
                last_sig[key] = t
                out.append(dict(d=d, w=w, sgn=sgn, t=t, T=round(T, 2), view=a, edge=round(edge, 4),
                                aage=round(t - st["tb"], 1), dS=round(dS, 2)))

    for i in order:
        t = times[i]
        if kind[i] == 1:
            px = src_px[i - n_pm]
            rs.update(t / 1000, px)
            st["px"], st["ts"] = px, t
            evaluate(t)
            continue
        w = int(pw[i])
        if w != st["w"]:
            st.update(w=w, mid=np.nan, bid=np.nan, ask=np.nan, tb=None, a0=None)
        nb, na = pbid[i], pask[i]
        moved = (nb != st["bid"] and not (np.isnan(nb) and np.isnan(st["bid"]))) or \
            (na != st["ask"] and not (np.isnan(na) and np.isnan(st["ask"])))
        st["bid"], st["ask"], st["d"] = nb, na, pdl[i]
        if np.isfinite(nb) and np.isfinite(na):
            new_mid = (nb + na) / 2
            if new_mid != st["mid"]:
                st["mid"] = new_mid
                if st["px"] is not None:
                    st["tb"], st["a0"] = t, st["px"]
        if moved:
            evaluate(t)
    return out


def side_at(pm: PM, w: int, t_ms: np.ndarray, sgn: np.ndarray):
    """mid и ask стороны по книге СЕРВЕРА в моменты t_ms (векторно по одному окну)."""
    s = pm.by_w.get(w, {}).get("srv")
    n = len(t_ms)
    if s is None:
        return np.full(n, np.nan), np.full(n, np.nan)
    i = np.searchsorted(s["t"], t_ms, side="right") - 1
    ok = i >= 0
    ii = np.where(ok, i, 0)
    bid = np.where(ok, s["bid"][ii].astype(float), np.nan)
    ask = np.where(ok, s["ask"][ii].astype(float), np.nan)
    mid_up = (bid + ask) / 2
    mid = np.where(sgn > 0, mid_up, 1 - mid_up)
    sask = np.where(sgn > 0, ask, 1 - bid)
    return mid, sask


def winners_ptb(root: str):
    wn = read(root, "windows")
    if wn.empty:
        return {}, {}
    wn = wn.drop_duplicates("slug", keep="last")
    win = {int(s): w for s, w in zip(wn.start, wn.official_winner) if w in ("Up", "Down")}
    ptb = {int(s): float(p) for s, p in zip(wn.start, pd.to_numeric(wn.ptb_twap, errors="coerce")) if np.isfinite(p)}
    return win, ptb


def per_sec_sigma(t_src: np.ndarray, px: np.ndarray):
    rs = RollingSigma(900, 5.0)
    sec = np.floor(t_src / 1000.0)
    last_idx = np.r_[np.flatnonzero(np.diff(sec)), len(sec) - 1]
    st, sv = [], []
    for i in last_idx:
        rs.update(float(sec[i]), float(px[i]))
        st.append(sec[i] * 1000.0)
        sv.append(rs.sigma())
    return np.array(st), np.array(sv)


def signals_table(sigs: list[dict], pm: PM, win: dict) -> pd.DataFrame:
    d = pd.DataFrame(sigs)
    if d.empty:
        return d
    d["won"] = [(1.0 if (win.get(w) == "Up") == (s > 0) else 0.0) if w in win else np.nan for w, s in zip(d.w, d.sgn)]
    for w, g in d.groupby("w"):
        tt, sg = g.t.values, g.sgn.values
        for h in H_FULL:
            m, a = side_at(pm, int(w), tt + h, sg)
            d.loc[g.index, f"m{h}"] = np.round(m, 4)
            if h in H_ASK:
                d.loc[g.index, f"a{h}"] = np.round(a, 4)
    full = d.d == 0
    keep = [f"m{h}" for h in H_FULL if h not in (0, 335, 1000, 2000, 5000)]
    d.loc[~full, keep] = np.nan          # для сдвинутых якорей дальние горизонты не нужны (размер файла)
    return d


def base_table(pm: PM, win: dict, ptb: dict, t_src, px, sig_t, sig_v, step_s: float = 5.0) -> pd.DataFrame:
    rows = []
    for w in sorted(pm.by_w):
        if w not in win:
            continue
        tt = np.arange(w + 5, w + WINDOW - 3, step_s) * 1000.0
        s = pm.by_w[w]["srv"]
        i = np.searchsorted(s["t"], tt, side="right") - 1
        j = np.searchsorted(s["t"], tt + 335, side="right") - 1
        ok = (i >= 0) & (j >= 0)
        if not ok.any():
            continue
        tt, i, j = tt[ok], i[ok], j[ok]
        k = np.searchsorted(t_src, tt, side="right") - 1
        lags = {}
        for back in (0, 2, 10, 30, 60):
            kb = np.searchsorted(t_src, tt - back * 1000, side="right") - 1
            lags[back] = np.where(kb >= 0, px[np.maximum(kb, 0)], np.nan)
        age = np.where(k >= 0, tt - t_src[np.maximum(k, 0)], np.nan)
        q = np.searchsorted(sig_t, tt, side="right") - 1
        sg = np.where(q >= 0, sig_v[np.maximum(q, 0)], np.nan)
        rows.append(pd.DataFrame(dict(
            w=w, T=np.round(w + WINDOW - tt / 1000, 1), bid=s["bid"][i], ask=s["ask"][i], bsz=s["bsz"][i], asz=s["asz"][i],
            bid_e=s["bid"][j], ask_e=s["ask"][j], s0=lags[0], s2=lags[2], s10=lags[10], s30=lags[30], s60=lags[60],
            src_age=np.round(age), sigma=np.round(sg, 3), ptb=ptb.get(w, np.nan), up_won=float(win[w] == "Up"))))
    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()


def live_rows(live: pd.DataFrame, pm: PM, win: dict) -> pd.DataFrame:
    d = live[live.w.isin(pm.by_w)].copy()
    if d.empty:
        return d
    d["won"] = [(1.0 if (win.get(w) == "Up") == (s > 0) else 0.0) if w in win else np.nan for w, s in zip(d.w, d.sgn)]
    for w, g in d.groupby("w"):
        tt, sg = g.t_ms.values.astype(float), g.sgn.values
        for h in H_LIVE:
            m, a = side_at(pm, int(w), tt + h, sg)
            d.loc[g.index, f"m{h}"] = np.round(m, 4)
            d.loc[g.index, f"a{h}"] = np.round(a, 4)
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--live-dirs", nargs="*", default=[])
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    live = pd.DataFrame()
    if a.live_dirs:
        from live_vs_replay import orders_table
        parts = []
        for ld in a.live_dirs:
            o = orders_table([ld])
            if len(o):
                o["bot"] = os.path.basename(os.path.normpath(ld))
                parts.append(o)
        if parts:
            live = pd.concat(parts, ignore_index=True)
            print(f"живых ордеров {len(live)}")
    live_out = []
    for root in a.roots:
        day = os.path.basename(os.path.normpath(root))
        try:
            pm_top = read(root, "pm_top")
            if pm_top.empty:
                print(f"{day}: нет pm_top")
                continue
            win, ptb = winners_ptb(root)
            pm = PM(pm_top)
            t_src, px = load_source(root, a.source)
            if len(t_src) < 1000:
                print(f"{day}: мало тиков {a.source}")
                continue
            sigs = collect(pm_top, t_src, px)
            st = signals_table(sigs, pm, win)
            if len(st):
                st.to_csv(os.path.join(a.out, f"sig_{day}.csv.gz"), index=False, compression="gzip")
            sig_t, sig_v = per_sec_sigma(t_src, px)
            bt = base_table(pm, win, ptb, t_src, px, sig_t, sig_v)
            if len(bt):
                bt.to_csv(os.path.join(a.out, f"base_{day}.csv.gz"), index=False, compression="gzip")
            if len(live):
                lr = live_rows(live, pm, win)
                if len(lr):
                    live_out.append(lr)
            n0 = int((st.d == 0).sum()) if len(st) else 0
            print(f"{day}: окон с исходом {len(win)}, тиков {len(t_src)}, сигналов d=0: {n0}, всего строк сигналов {len(st)}, "
                  f"состояний {len(bt)}", flush=True)
            del pm_top, pm, t_src, px, sigs, st, bt
            gc.collect()
        except Exception as ex:  # один плохой день не должен ронять остальные
            print(f"{day}: ошибка {ex!r}", flush=True)
    if live_out:
        lo = pd.concat(live_out, ignore_index=True)
        cols = [c for c in ["bot", "sid", "w", "t_ms", "sgn", "status", "filled_f", "filled", "usdc", "avg_px", "limit", "size",
                            "ask_signal", "slip_c", "edge_c", "T", "http_ms", "won"] if c in lo.columns]
        cols += [c for c in lo.columns if (c.startswith("m") or c.startswith("a")) and c[1:].isdigit()]
        lo[cols].to_csv(os.path.join(a.out, "live_orders.csv.gz"), index=False, compression="gzip")
        print(f"живых ордеров с книгой: {len(lo)}")


if __name__ == "__main__":
    main()
