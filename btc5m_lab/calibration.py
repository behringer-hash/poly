"""Калибровка рынка Polymarket по ВСЕМ состояниям окна (не только по скачкам): есть ли систематическое смещение цены.

    python calibration.py data/2026-10-10 data/2026-10-11 --source bybit --L 300 [--step 5]

Для каждого окна с известным исходом и каждой секунды (шаг --step) строим состояние:
  d = (цена BTC источника - ptb_twap) / (sigma * sqrt(T)) - z-оценка расстояния до цены-порога,
  T - секунд до конца, цена стороны (Up или Down) по ask через L мс (книга сервера), как для настоящей покупки.
Результат покупки: исход (1/0) - ask - комиссия. Смотрим средний результат по корзинам (z, T, цена) с 95% ИИ,
ресэмплинг по ОКНАМ (секунды одного окна зависимы). Положительная корзина = покупать по ask выгодно вне зависимости от скорости
(но надо помнить о числе проверенных корзин: часть «находок» случайна).
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from common import RollingSigma
from lead_lag import FEE, PM, read
from replay import load_source


def build_states(root: str, source: str, L: int, step: float, min_T: float = 10.0) -> pd.DataFrame:
    pt = read(root, "pm_top")
    wn = read(root, "windows").drop_duplicates("slug", keep="last")
    wn = wn[wn.official_winner.isin(["Up", "Down"]) & wn.ptb_twap.notna()]
    if wn.empty or pt.empty:
        return pd.DataFrame()
    pm = PM(pt)
    t_src, px = load_source(root, source)
    if len(t_src) < 100:
        return pd.DataFrame()
    # sigma по ходу времени (как в движке: скользящее по ~15 мин), считаем по секундной сетке
    rs = RollingSigma(900, 5.0)
    sec = np.floor(t_src / 1000.0)
    last_idx = np.r_[np.flatnonzero(np.diff(sec)) , len(sec) - 1]
    sig_t, sig_v = [], []
    for i in last_idx:
        rs.update(float(sec[i]), float(px[i]))
        sig_t.append(sec[i] * 1000.0)
        sig_v.append(rs.sigma())
    sig_t, sig_v = np.array(sig_t), np.array(sig_v)
    rows = []
    for w, ptb, win in zip(wn.start.astype(int), wn.ptb_twap.astype(float), wn.official_winner):
        if w not in pm.by_w:
            continue
        for t in np.arange(w + 5, w + 300 - min_T, step):
            tm = t * 1000.0
            i = np.searchsorted(t_src, tm, side="right") - 1
            if i < 0 or tm - t_src[i] > 1500:
                continue
            j = np.searchsorted(sig_t, tm, side="right") - 1
            if j < 0:
                continue
            T = w + 300 - t
            z = (px[i] - ptb) / (sig_v[j] * np.sqrt(T) + 1e-9)
            m = pm.state(w, tm + L, "srv")
            if m is None:
                continue
            bid, ask, bsz, asz = m
            for sgn in (1, -1):
                a = ask if sgn > 0 else (1 - bid if np.isfinite(bid) else np.nan)
                size = asz if sgn > 0 else bsz
                if not (np.isfinite(a) and np.isfinite(size) and size >= 5 and 0.02 <= a <= 0.98):
                    continue
                won = float((win == "Up") == (sgn > 0))
                rows.append(dict(w=w, t=t, T=T, sgn=sgn, zs=sgn * z, ask=a, won=won, pnl=100 * (won - a - FEE * a * (1 - a))))
    return pd.DataFrame(rows)


def boot_ci(d: pd.DataFrame, col: str = "pnl", n: int = 600, seed: int = 0) -> tuple[float, float, float]:
    g = d.groupby("w")[col].agg(["sum", "size"])
    if len(g) < 5:
        return float(d[col].mean()), np.nan, np.nan
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(g), (n, len(g)))
    bs = g["sum"].values[idx].sum(1) / g["size"].values[idx].sum(1)
    return float(d[col].mean()), float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))


def table(d: pd.DataFrame, by: str, bins, labels=None) -> pd.DataFrame:
    rows = []
    cut = pd.cut(d[by], bins, labels=labels)
    for k, g in d.groupby(cut, observed=True):
        m, lo, hi = boot_ci(g)
        rows.append({by: k, "строк": len(g), "окон": g.w.nunique(), "ask_ср": round(g.ask.mean(), 3), "побед": round(g.won.mean(), 3),
                     "разрыв_ц": round(100 * (g.won.mean() - g.ask.mean()), 2), "pnl_ц": round(m, 2), "ИИ_низ": round(lo, 2), "ИИ_верх": round(hi, 2)})
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--L", type=int, default=300)
    ap.add_argument("--step", type=float, default=5.0)
    a = ap.parse_args()
    pd.set_option("display.width", 230)
    d = pd.concat([build_states(r, a.source, a.L, a.step) for r in a.roots], ignore_index=True)
    if d.empty:
        print("нет данных")
        return
    print(f"состояний {len(d)}, окон {d.w.nunique()}, источник {a.source}, L={a.L} мс, шаг {a.step} с")
    m, lo, hi = boot_ci(d)
    print(f"в среднем: pnl {m:.2f} ц на шейр [{lo:.2f}; {hi:.2f}], побед {d.won.mean():.3f}, ask {d.ask.mean():.3f}")
    print("\n=== по цене покупки (ask) ===")
    print(table(d, "ask", [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, .95, 1]).to_string(index=False))
    print("\n=== по z = направленное расстояние до ptb в сигмах (z>0: сторона уже выигрывает) ===")
    print(table(d, "zs", [-99, -3, -2, -1, -0.5, 0, 0.5, 1, 2, 3, 99]).to_string(index=False))
    print("\n=== по оставшемуся времени T, с ===")
    print(table(d, "T", [0, 30, 60, 120, 200, 300]).to_string(index=False))
    for lo_t, hi_t in ((10, 60), (60, 150), (150, 290)):
        s = d[(d["T"] >= lo_t) & (d["T"] < hi_t)]
        print(f"\n=== T {lo_t}-{hi_t} с: по z ===")
        print(table(s, "zs", [-99, -2, -1, 0, 1, 2, 99]).to_string(index=False))
    # отложенная проверка: те же корзины по дням
    d["day"] = (d.w // 86400).astype(int)
    print("\n=== по дням: pnl на шейр (все состояния) ===")
    print(d.groupby("day").apply(lambda g: pd.Series(dict(строк=len(g), pnl_ц=round(g.pnl.mean(), 2)))).to_string())


if __name__ == "__main__":
    main()
