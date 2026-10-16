"""Как быстро цена ask токена уезжает после нашего сигнала C1 и кто её съедает (сделки конкурентов или снятие заявок).

    python reprice_timing.py data/2026-10-13 data/2026-10-14 --source bybit --thr 0.03 --slip 3

Для каждого сигнала C1 (время t - момент, когда мы его увидели; вид книги СЕРВЕРА, как в реплее):
  * доживаемость: доля сигналов, у которых лучший ask стороны через x мс всё ещё не выше лимита (ask сигнала + переплата),
    и не выше самого ask сигнала; для x от -300 (до сигнала) до 2000 мс;
  * время до первого сдвига: через сколько мс после t ask впервые выше ask сигнала / на 1 ц выше / выше лимита;
    0 - к моменту t сервер уже дороже («мёртвый на старте»);
  * механизм: был ли до ухода цены за лимит хоть один купленный токен нашей стороны по цене до лимита в ленте сделок
    рынка (значит заявку забрал конкурент-тейкер) или цена ушла без сделок (маркет-мейкеры сняли и переставили заявки);
  * срезы по силе сигнала, цене, времени до конца окна.
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from lead_lag import PM, read
from replay import Params, collect_signals, load_source

GRID = [-300, -200, -100, 0, 50, 100, 150, 200, 250, 300, 400, 500, 750, 1000, 1500, 2000]
HORIZON = 3000.0


def side_series(arr: dict, sgn: int):
    return arr["t"], (arr["ask"] if sgn > 0 else 1.0 - arr["bid"])


def at(t_arr: np.ndarray, p_arr: np.ndarray, tq: float) -> float:
    i = np.searchsorted(t_arr, tq, side="right") - 1
    return float(p_arr[i]) if i >= 0 else np.nan


def first_pass(t_arr: np.ndarray, p_arr: np.ndarray, t0: float, thr: float, horizon: float = HORIZON) -> float:
    """Через сколько мс после t0 цена впервые строго выше thr (0 - уже выше в момент t0, inf - не за горизонт)."""
    i0 = np.searchsorted(t_arr, t0, side="right") - 1
    if i0 >= 0 and p_arr[i0] > thr + 1e-9:
        return 0.0
    j = np.searchsorted(t_arr, t0 + horizon, side="right")
    seg = p_arr[i0 + 1:j]
    k = np.flatnonzero(seg > thr + 1e-9)
    return float(t_arr[i0 + 1 + k[0]] - t0) if len(k) else np.inf


def build(root: str, source: str, thr: float, slip_c: float) -> pd.DataFrame:
    pt = read(root, "pm_top")
    if pt.empty:
        return pd.DataFrame()
    pm = PM(pt)
    t_src, px = load_source(root, source)
    sigs = collect_signals(pt, t_src, px, [Params(thr, 1.0)])
    tr = read(root, "pm_trades", ["server_ts", "w", "o", "side", "price", "size"])
    if len(tr):
        tr = tr[tr.side.astype(str).str.upper().str.startswith("B")]
    tr_by = {k: g.sort_values("server_ts") for k, g in tr.groupby(["w", "o"])} if len(tr) else {}
    rows = []
    for s in sigs:
        w, sgn, t, a0 = s["w"], s["sgn"], s["t"], s["view"]
        arr = pm.by_w.get(w, {}).get("srv")
        if arr is None:
            continue
        ts, ps = side_series(arr, sgn)
        limit = round(a0 + slip_c / 100, 4)
        r = dict(w=w, sgn=sgn, t=t, a0=a0, edge=100 * s["edge"], T=w + 300 - t / 1000)
        for x in GRID:
            p = at(ts, ps, t + x)
            r[f"p{x}"] = np.nan if not np.isfinite(p) else 100 * (p - a0)
        r["t_up"] = first_pass(ts, ps, t, a0)
        r["t_1c"] = first_pass(ts, ps, t, a0 + 0.01)
        r["t_lim"] = first_pass(ts, ps, t, limit)
        # сделки: покупки токена нашей стороны по цене до лимита между t и уходом цены за лимит
        g = tr_by.get((w, "U" if sgn > 0 else "D"))
        r["trade_dt"] = np.nan
        if g is not None:
            m = (g.server_ts.values >= t) & (g.server_ts.values <= t + HORIZON) & (g.price.values <= limit + 1e-9)
            if m.any():
                r["trade_dt"] = float(g.server_ts.values[m][0] - t)
        rows.append(r)
    return pd.DataFrame(rows)


def q(x: pd.Series, qs=(0.1, 0.25, 0.5, 0.75, 0.9)):
    x = x.replace(np.inf, np.nan).dropna()
    return " ".join(f"{np.quantile(x, k):6.0f}" for k in qs) if len(x) else "n/a"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--thr", type=float, default=0.03)
    ap.add_argument("--slip", type=float, default=3.0)
    ap.add_argument("--since", type=float, default=0)
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    d = pd.concat([build(r, a.source, a.thr, a.slip) for r in a.roots], ignore_index=True)
    if a.since:
        d = d[d.w >= a.since]
    if d.empty:
        print("нет сигналов")
        return
    lim_c = a.slip
    print(f"сигналов {len(d)}, окон {d.w.nunique()}, источник {a.source}, порог {a.thr}, лимит = ask сигнала + {a.slip:g} ц")
    print("\n=== доживаемость: доля сигналов, у которых к моменту t+x на сервере ask не выше (x от сигнала, мс) ===")
    rows = []
    for x in GRID:
        c = d[f"p{x}"]
        rows.append(dict(x_мс=x, не_выше_ask_сигнала=round((c <= 0.0001).mean(), 3), не_выше_лимита=round((c <= lim_c + 0.0001).mean(), 3),
                         мед_сдвиг_ц=round(c.median(), 2), p90_сдвиг_ц=round(c.quantile(0.9), 2)))
    print(pd.DataFrame(rows).to_string(index=False))
    print("\n=== время до первого сдвига вверх после сигнала, мс (квантили 10/25/50/75/90; inf - не ушла за 3 с) ===")
    for col, name in (("t_up", "выше ask сигнала"), ("t_1c", "на 1 ц выше"), ("t_lim", "выше лимита")):
        c = d[col]
        print(f"{name:20s} {q(c)}   мёртвых на старте (0 мс): {(c == 0).mean():.1%}; не ушла за 3 с: {np.isinf(c).mean():.1%}")
    dead = d.t_lim == 0
    print(f"\nдоля со сдвигом за 150 мс: {(d.t_lim <= 150).mean():.1%}, за 300 мс: {(d.t_lim <= 300).mean():.1%}, за 500 мс: {(d.t_lim <= 500).mean():.1%}, "
          f"за 1000 мс: {(d.t_lim <= 1000).mean():.1%}")
    print("\n=== механизм ухода цены за лимит (только сигналы, где она ушла за 3 с) ===")
    gone = d[np.isfinite(d.t_lim)]
    tr_first = gone.trade_dt.notna() & (gone.trade_dt <= gone.t_lim + 1)
    print(f"сделка конкурента по цене до лимита успела до ухода цены: {tr_first.mean():.1%}; цена ушла без такой сделки "
          f"(заявки сняты/переставлены): {(~tr_first).mean():.1%}")
    print("время первой такой сделки после t, мс (10/25/50/75/90):", q(gone.trade_dt))
    for name, col, bins in (("сила сигнала, ц", "edge", [0, 3.5, 4.5, 6, 10, 100]), ("ask сигнала", "a0", [0, .2, .5, .8, 1]),
                            ("осталось, с", "T", [0, 60, 120, 200, 300])):
        print(f"\n=== срез: {name} ===")
        rows = []
        for k, g in d.groupby(pd.cut(d[col], bins), observed=True):
            rows.append(dict(корзина=str(k), сигналов=len(g), мед_t_лимит_мс=round(float(g.t_lim.replace(np.inf, np.nan).median()), 0) if g.t_lim.replace(np.inf, np.nan).notna().any() else np.nan,
                             жив_300=round((g.p300 <= lim_c + 0.0001).mean(), 3), жив_500=round((g.p500 <= lim_c + 0.0001).mean(), 3),
                             мёртв_на_старте=round((g.t_lim == 0).mean(), 3)))
        print(pd.DataFrame(rows).to_string(index=False))
    d["day"] = (d.w // 86400).astype(int)
    print("\n=== по дням: жив на 300 мс, медиана t_лимит ===")
    print(d.groupby("day").apply(lambda g: pd.Series(dict(сигналов=len(g), жив_300=round((g.p300 <= lim_c + 0.0001).mean(), 3),
                                                          мед_t_лимит=g.t_lim.replace(np.inf, np.nan).median()))).to_string())


if __name__ == "__main__":
    main()
