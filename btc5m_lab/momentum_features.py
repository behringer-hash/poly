"""Моментум после скачка: какие признаки предсказывают, что токен в сторону скачка выиграет чаще, чем говорит его цена.

    python momentum_features.py data/2026-10-10 data/2026-10-11 --source bybit --N 8 --W 500 --L 300

Событие: источник цены (по умолчанию середина книги Bybit) сдвинулся не меньше чем на N долларов за W мс (как speed_compare.fires).
Покупаем токен стороны скачка по ask книги СЕРВЕРА через L мс (то есть после переоценки, без расчёта на устаревшую цену),
держим до конца окна. Результат: исход(1/0) - ask - комиссия, в центах на шейр.

Признаки на момент события: размер и скорость скачка, предыдущий ход за 2/5/30 с, расстояние до ptb в сигмах (z) и время T,
уже случившаяся переоценка токена, подтверждение другими площадками (Binance фьючерсы, Coinbase, OKX), дисбаланс агрессивных
сделок (Bybit, Binance), объём сделок, ликвидации. Дальше: корзины по каждому признаку (с ИИ по окнам) и логистическая модель
исхода со смещением logit(ask) - то есть модель предсказывает ТОЛЬКО то, что рынок не учёл. Оценка модели - на последних по времени
окнах, которых она не видела.
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from calibration import boot_ci
from common import RollingSigma
from lead_lag import FEE, PM, read
from replay import load_source
from speed_compare import fires

FEATURES = ["jump", "speed", "m2", "m5", "m30", "z0", "T", "rep1", "rep5", "conf_bf", "conf_cb", "conf_ok",
            "imb_by", "imb_bf", "vol1", "liq5"]


def last_at(t: np.ndarray, p: np.ndarray, tq):
    i = np.searchsorted(t, tq, side="right") - 1
    return np.where(i >= 0, p[np.maximum(i, 0)], np.nan)


def flow_series(root: str, stream: str, kind: str):
    """(время, накопленный знаковый объём, накопленный объём): знак +1 - агрессор покупает."""
    try:
        return _flow_series(root, stream, kind)
    except ValueError:                 # потока или колонок нет в этих данных
        return None


def _flow_series(root: str, stream: str, kind: str):
    if kind == "bnf":
        d = read(root, stream, ["recv_ms", "qty", "price", "m"])
        if d.empty:
            return None
        v = d.qty.values.astype(float)
        s = np.where(d.m.values.astype(float) == 1, -1.0, 1.0)
    else:
        d = read(root, stream, ["recv_ms", "size", "price", "side"])
        if d.empty:
            return None
        v = d["size"].values.astype(float)
        s = np.where(d.side.astype(str).str.startswith("B").values, 1.0, -1.0)
    o = np.argsort(d.recv_ms.values, kind="stable")
    t = d.recv_ms.values.astype(float)[o]
    return t, np.cumsum((s * v)[o]), np.cumsum(v[o])


def liq_series(root: str):
    ts, vs = [], []
    for stream, qcol in (("by_liq", "size"), ("bnf_liq", "qty")):
        try:
            d = read(root, stream, ["recv_ms", "price", qcol])
        except ValueError:
            continue
        if len(d):
            ts.append(d.recv_ms.values.astype(float))
            vs.append((d.price.values.astype(float) * d[qcol].values.astype(float)))
    if not ts:
        return None
    t, v = np.concatenate(ts), np.concatenate(vs)
    o = np.argsort(t, kind="stable")
    return t[o], np.cumsum(v[o])


def window_sum(t: np.ndarray, cum: np.ndarray, te, ms: float):
    a = np.searchsorted(t, te, side="right") - 1
    b = np.searchsorted(t, te - ms, side="right") - 1
    ca = np.where(a >= 0, cum[np.maximum(a, 0)], 0.0)
    cb = np.where(b >= 0, cum[np.maximum(b, 0)], 0.0)
    return ca - cb


def build_events(root: str, source: str, N: float, W: float, L: int, cooldown_ms: float = 2000.0) -> pd.DataFrame:
    pt = read(root, "pm_top")
    wn = read(root, "windows").drop_duplicates("slug", keep="last")
    wn = wn[wn.official_winner.isin(["Up", "Down"]) & wn.ptb_twap.notna()]
    if pt.empty or wn.empty:
        return pd.DataFrame()
    pm = PM(pt)
    ptb = dict(zip(wn.start.astype(int), wn.ptb_twap.astype(float)))
    win = dict(zip(wn.start.astype(int), wn.official_winner))
    t, px = load_source(root, source)
    if len(t) < 100:
        return pd.DataFrame()
    ev = fires(t, px, N, W, refractory=cooldown_ms)
    if not ev:
        return pd.DataFrame()
    te = np.array([e[0] for e in ev])
    dr = np.array([e[1] for e in ev], dtype=float)
    # sigma ($/sqrt(c)) на момент события: скользящее по ~15 мин на секундной сетке
    sec = np.floor(t / 1000.0)
    idx = np.r_[np.flatnonzero(np.diff(sec)), len(sec) - 1]
    rs, sg_t, sg_v = RollingSigma(900, 5.0), [], []
    for i in idx:
        rs.update(float(sec[i]), float(px[i]))
        sg_t.append(sec[i] * 1000.0)
        sg_v.append(rs.sigma())
    sg_t, sg_v = np.array(sg_t), np.array(sg_v)
    sig = last_at(sg_t, sg_v, te)
    p_now = last_at(t, px, te)
    f = pd.DataFrame(dict(te=te, dir=dr, sig=sig))
    f["w"] = (te // 1000 // 300 * 300).astype(int)
    f["T"] = f.w + 300 - te / 1000
    f["el"] = te / 1000 - f.w
    f["jump"] = np.abs(p_now - last_at(t, px, te - W))
    f["speed"] = f.jump / (W / 1000.0)
    for s_ in (2, 5, 30):
        f[f"m{s_}"] = dr * (p_now - last_at(t, px, te - s_ * 1000.0)) / (sig * np.sqrt(s_) + 1e-9)
    f["ptb"] = f.w.map(ptb)
    f["z0"] = dr * (p_now - f.ptb) / (sig * np.sqrt(f["T"].clip(lower=1)) + 1e-9)
    # подтверждение другими площадками: изменение их цены за те же W мс в сторону скачка, в долях N
    for name, col in (("binance_fut", "conf_bf"), ("coinbase", "conf_cb"), ("okx", "conf_ok")):
        try:
            t2, p2 = load_source(root, name)
            f[col] = dr * (last_at(t2, p2, te) - last_at(t2, p2, te - W)) / N if len(t2) > 10 else np.nan
        except Exception:
            f[col] = np.nan
    for stream, kind, col in (("by_trade", "by", "imb_by"), ("bnf_agg", "bnf", "imb_bf")):
        fs = flow_series(root, stream, kind)
        if fs is None:
            f[col] = np.nan
            if col == "imb_by":
                f["vol1"] = np.nan
            continue
        tt, cs, cv = fs
        sv, vv = window_sum(tt, cs, te, 1000.0), window_sum(tt, cv, te, 1000.0)
        f[col] = dr * sv / (vv + 1e-9)
        if col == "imb_by":
            f["vol1"] = np.log1p(vv)
    ls = liq_series(root)
    f["liq5"] = np.log1p(window_sum(ls[0], ls[1], te, 5000.0)) if ls is not None else np.nan
    # книга Polymarket: вход по ask через L мс, цена токена стороны скачка и уже случившаяся переоценка
    rows = []
    for r in f.itertuples():
        if r.T < 15 or r.el < 3 or r.w not in win:
            continue
        sg = int(r.dir)
        m_e = pm.state(r.w, r.te + L, "srv")
        m_0 = pm.state(r.w, r.te, "srv")
        m_1 = pm.state(r.w, r.te - 1000, "srv")
        m_5 = pm.state(r.w, r.te - 5000, "srv")
        if m_e is None or m_0 is None:
            continue

        def mid(m):
            if m is None or not (np.isfinite(m[0]) and np.isfinite(m[1])):
                return np.nan
            u = (m[0] + m[1]) / 2
            return u if sg > 0 else 1 - u

        a = m_e[1] if sg > 0 else (1 - m_e[0] if np.isfinite(m_e[0]) else np.nan)
        size = m_e[3] if sg > 0 else m_e[2]
        if not (np.isfinite(a) and np.isfinite(size) and size >= 5 and 0.05 <= a <= 0.95):
            continue
        won = float((win[r.w] == "Up") == (sg > 0))
        rows.append(dict(idx=r.Index, ask=a, rep1=100 * (mid(m_0) - mid(m_1)), rep5=100 * (mid(m_0) - mid(m_5)), won=won,
                         pnl=100 * (won - a - FEE * a * (1 - a))))
    if not rows:
        return pd.DataFrame()
    g = pd.DataFrame(rows).set_index("idx")
    return f.join(g, how="inner").drop(columns=["ptb"])


def logit(p):
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return np.log(p / (1 - p))


def fit_logit(X: np.ndarray, y: np.ndarray, off: np.ndarray, l2: float = 5.0, it: int = 50):
    """Логистическая регрессия со смещением off и L2 на коэффициенты (кроме свободного члена). Возвращает (b0, beta)."""
    n, k = X.shape
    A = np.c_[np.ones(n), X]
    w = np.zeros(k + 1)
    R = np.diag([0.0] + [l2] * k)
    for _ in range(it):
        z = A @ w + off
        p = 1 / (1 + np.exp(-z))
        g = A.T @ (p - y) + R @ w
        H = (A * (p * (1 - p))[:, None]).T @ A + R + 1e-6 * np.eye(k + 1)
        step = np.linalg.solve(H, g)
        w -= step
        if np.abs(step).max() < 1e-7:
            break
    return w[0], w[1:]


def prep(df: pd.DataFrame, feats, mu=None, sd=None):
    X = df[feats].astype(float).copy()
    X = X.fillna(0.0)
    if mu is None:
        mu, sd = X.mean(), X.std().replace(0, 1.0)
    return ((X - mu) / sd).values, mu, sd


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--N", type=float, default=8.0)
    ap.add_argument("--W", type=float, default=500.0)
    ap.add_argument("--L", type=int, default=300)
    ap.add_argument("--train-frac", type=float, default=0.6)
    a = ap.parse_args()
    pd.set_option("display.width", 230)
    d = pd.concat([build_events(r, a.source, a.N, a.W, a.L) for r in a.roots], ignore_index=True)
    d = d.dropna(subset=["z0", "m2"]).reset_index(drop=True)
    if d.empty:
        print("нет событий")
        return
    print(f"событий {len(d)}, окон {d.w.nunique()}, источник {a.source}, скачок >= ${a.N:g} за {a.W:g} мс, вход по ask через {a.L} мс")
    m, lo, hi = boot_ci(d)
    print(f"в среднем: pnl {m:.2f} ц на шейр [{lo:.2f}; {hi:.2f}], побед {d.won.mean():.3f}, ask {d.ask.mean():.3f}")
    feats = [c for c in FEATURES if d[c].notna().mean() > 0.5]
    print("\n=== по признакам: квинтили (pnl в центах на шейр, ИИ по окнам) ===")
    for c in feats:
        q = pd.qcut(d[c].rank(method="first"), 5, labels=False) if d[c].nunique() > 10 else d[c]
        rows = []
        for k, g in d.groupby(q):
            mm, l, h = boot_ci(g, n=300)
            rows.append(f"{k}: {g[c].mean():+.2f} | n={len(g)} pnl {mm:+.2f} [{l:+.2f};{h:+.2f}]")
        print(f"-- {c}\n   " + "\n   ".join(rows))
    # модель: обучение на первых по времени окнах, оценка на остальных
    cut = d.w.quantile(a.train_frac)
    tr, te = d[d.w <= cut], d[d.w > cut]
    if len(tr) < 200 or len(te) < 100:
        print("\nмало данных для модели")
        return
    X_tr, mu, sd = prep(tr, feats)
    b0, beta = fit_logit(X_tr, tr.won.values, logit(tr.ask.values))
    X_te, _, _ = prep(te, feats, mu, sd)
    p_te = 1 / (1 + np.exp(-(b0 + X_te @ beta + logit(te.ask.values))))
    te = te.assign(edge=100 * (p_te - te.ask - FEE * te.ask * (1 - te.ask)))
    print(f"\n=== модель (logit исхода со смещением logit(ask)): обучение {len(tr)} событий, тест {len(te)} (окна позже) ===")
    print("коэффициенты (в сигмах признака): " + ", ".join(f"{c} {b:+.3f}" for c, b in zip(feats, beta)))
    print(f"тест: средний pnl всех событий {te.pnl.mean():+.2f}; корреляция предсказанного edge и фактического pnl {np.corrcoef(te.edge, te.pnl)[0, 1]:+.3f}")
    for q in (0.5, 0.3, 0.2, 0.1):
        s = te[te.edge >= te.edge.quantile(1 - q)]
        mm, l, h = boot_ci(s, n=500)
        print(f"  верхние {int(q * 100):>3}% по предсказанному edge: n={len(s):5d} окон={s.w.nunique():4d} pnl {mm:+.2f} [{l:+.2f};{h:+.2f}] ц/шейр")
    s = te[te.edge > 0]
    mm, l, h = boot_ci(s, n=500)
    print(f"  edge > 0: n={len(s)} pnl {mm:+.2f} [{l:+.2f};{h:+.2f}]")
    Xtr_p = 1 / (1 + np.exp(-(b0 + X_tr @ beta + logit(tr.ask.values))))
    tr_edge = 100 * (Xtr_p - tr.ask.values - FEE * tr.ask.values * (1 - tr.ask.values))
    s = tr[tr_edge >= np.quantile(tr_edge, 0.9)]
    print(f"  (на обучении верхние 10%: pnl {s.pnl.mean():+.2f} - разница с тестом показывает переобучение)")


if __name__ == "__main__":
    main()
