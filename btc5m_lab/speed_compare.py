"""Какой источник цены BTC сообщает о скачке РАНЬШЕ всех (по времени прихода на ваш сервер и по времени самой биржи).

    python speed_compare.py data/2026-10-10 data/2026-10-11 --sources bybit,bybit_trade,binance_fut,binance \
        --N 10,20,30 --W 500,1000

Для каждого источника отдельно ищем «скачок»: цена изменилась не меньше чем на N долларов за последние W мс (по тикам этого же
источника). Скачок засчитывается один раз на направление с паузой 2 с. Скачки разных источников в пределах окна кластера (2 с,
то же направление) считаем одним событием рынка, а дальше смотрим, насколько позже самого первого источника сработал каждый:
  ось recv - время прихода на ваш сервер (то, что важно для торговли: чей сигнал вы увидите первым);
  ось exch - время самой биржи (кто опережает на самом деле, без задержек доставки; часы бирж не синхронны, точность ±10-30 мс).
Книжные источники (bybit, binance_fut_book...) - середина лучших bid/ask, остальные - цена последней сделки.
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from lead_lag import read
from replay import load_source

# источник -> (поток с временем биржи, колонка времени биржи, колонка цены); только для оси exch
EXCH = {
    "binance": ("bn_agg", "T", "price"),
    "binance_fut": ("bnf_agg", "T", "price"),
    "bybit_trade": ("by_trade", "T", "price"),
    "bybit_spot_trade": ("bys_trade", "T", "price"),
    "okx": ("ok_trade", "T", "price"),
    "kraken": ("kr_trade", "T", "price"),
    "bitstamp": ("bs_trade", "T", "price"),
}


def fires(t: np.ndarray, px: np.ndarray, N: float, W: float, refractory: float = 2000.0) -> list[tuple[float, int]]:
    """Моменты скачков: |цена - цена W мс назад| >= N; одно срабатывание на направление, пауза refractory."""
    if len(t) < 2:
        return []
    j = np.searchsorted(t, t - W, side="right") - 1
    move = np.where(j >= 0, px - px[np.maximum(j, 0)], 0.0)
    last = {1: -1e18, -1: -1e18}
    out = []
    for i in np.flatnonzero(np.abs(move) >= N):
        d = 1 if move[i] > 0 else -1
        if t[i] - last[d] < refractory:
            continue
        last[d] = t[i]
        out.append((float(t[i]), d))
    return out


def clusters(events: list[tuple[float, int, str]], span: float = 2000.0) -> list[dict[str, float]]:
    """events: (время, направление, источник). Кластер: от первого неиспользованного события и далее span мс, то же направление;
    у каждого источника берётся его первое срабатывание."""
    ev = sorted(events)
    used = [False] * len(ev)
    out = []
    for i, (t0, d, s0) in enumerate(ev):
        if used[i]:
            continue
        c: dict[str, float] = {}
        for k in range(i, len(ev)):
            t, dk, s = ev[k]
            if t - t0 > span:
                break
            if used[k] or dk != d:
                continue
            used[k] = True
            c.setdefault(s, t)
        out.append(c)
    return out


def cluster_table(cl: list[dict[str, float]], sources: list[str]) -> pd.DataFrame:
    full = [c for c in cl if all(s in c for s in sources)]
    rows = []
    for s in sources:
        cover = np.mean([s in c for c in cl]) if cl else np.nan
        delay = np.array([c[s] - min(c.values()) for c in full]) if full else np.array([])
        first = np.mean([c[s] == min(c.values()) for c in full]) if full else np.nan
        rows.append(dict(источник=s, покрытие_событий=round(cover, 3), общих_событий=len(full), первый_доля=round(first, 3),
                         мед_отставание_мс=round(float(np.median(delay)), 1) if len(delay) else np.nan,
                         p25=round(float(np.percentile(delay, 25)), 1) if len(delay) else np.nan,
                         p75=round(float(np.percentile(delay, 75)), 1) if len(delay) else np.nan,
                         p90=round(float(np.percentile(delay, 90)), 1) if len(delay) else np.nan))
    return pd.DataFrame(rows).sort_values("мед_отставание_мс")


def load_recv(roots: list[str], name: str) -> tuple[np.ndarray, np.ndarray]:
    ts, ps = [], []
    for r in roots:
        try:
            t, p = load_source(r, name)
        except Exception:
            continue
        if len(t):
            ts.append(t)
            ps.append(p)
    if not ts:
        return np.array([]), np.array([])
    t, p = np.concatenate(ts), np.concatenate(ps)
    o = np.argsort(t, kind="stable")
    return t[o], p[o]


def load_exch(roots: list[str], name: str):
    stream, tcol, pcol = EXCH[name]
    d = pd.concat([read(r, stream, [tcol, pcol, "recv_ms"]) for r in roots], ignore_index=True)
    d = d.dropna().sort_values(tcol, kind="stable")
    return d[tcol].values.astype(float), d[pcol].values.astype(float), (d.recv_ms - d[tcol]).values.astype(float)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--sources", default="bybit,bybit_trade,binance_fut,binance")
    ap.add_argument("--N", default="10,20,30", help="размер скачка, долларов (через запятую)")
    ap.add_argument("--W", default="500,1000", help="окно скачка, мс (через запятую)")
    ap.add_argument("--span", type=float, default=2000.0)
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    src = [s.strip() for s in a.sources.split(",") if s.strip()]
    data = {s: load_recv(a.roots, s) for s in src}
    src = [s for s in src if len(data[s][0]) > 100]
    print("источники с данными:", ", ".join(f"{s} ({len(data[s][0])} тиков)" for s in src))
    ex = {s: load_exch(a.roots, s) for s in src if s in EXCH}
    if ex:
        print("\n=== средняя задержка доставки (приход минус время биржи), мс: p10 / p50 / p90 (часы бирж и ваши не синхронизированы - важна разница между биржами) ===")
        print(pd.DataFrame({s: dict(p10=np.percentile(v[2], 10), p50=np.percentile(v[2], 50), p90=np.percentile(v[2], 90))
                            for s, v in ex.items()}).T.round(0).to_string())
    for N in [float(x) for x in a.N.split(",")]:
        for W in [float(x) for x in a.W.split(",")]:
            print(f"\n################ скачок >= ${N:g} за {W:g} мс ################")
            ev = [(t, d, s) for s in src for t, d in fires(*data[s], N, W)]
            cl = clusters(ev, a.span)
            print(f"событий рынка (кластеров) {len(cl)}; срабатываний: " + ", ".join(f"{s} {sum(1 for e in ev if e[2] == s)}" for s in src))
            print("--- ось recv: во сколько ваш сервер увидел скачок (отставание от самого раннего источника) ---")
            print(cluster_table(cl, src).to_string(index=False))
            es = [s for s in src if s in ex]
            if len(es) >= 2:
                evx = [(t, d, s) for s in es for t, d in fires(ex[s][0], ex[s][1], N, W)]
                print("--- ось exch: кто опережает по времени самой биржи ---")
                print(cluster_table(clusters(evx, a.span), es).to_string(index=False))


if __name__ == "__main__":
    main()
