"""Отбор сигналов по книге: помогает ли он в итоговой прибыли при реальных правилах бота и живой задержке.

    python filter_portfolio.py data/2026-10-10 ... data/2026-10-16 --live-data bot_data_c1 --source bybit

Что делаем:
  1. сигналы C1 (Bybit, порог 0.03, переплата 3 ц) за все дни; исполнение при каждой из набора задержек L (книга сервера);
  2. задержка до матча берётся у живых ордеров, ИСПОЛНИМЫХ при приходе на биржу (книга сервера через 25 мс ещё не выше лимита);
     неисполнимые при приходе не исполняются. Два режима:
       «независимая»  - задержка из общего распределения этих ордеров;
       «условная»     - вероятность МЕДЛЕННОГО ответа (> 400 мс) зависит от состояния книги на момент сигнала
                        (логистическая модель на живых ордерах: в тихой книге ответы медленнее), дальше задержка из быстрой
                        или из медленной части распределения. 30 розыгрышей на вариант;
  3. портфель с правилами бота: пауза 1 с после любого ордера и 5 с после покупки, пустые ордера лимит окна не занимают,
     не больше 10 ордеров и $30 на окно, без дневных лимитов;
  4. стратегии: все сигналы / верхние q% по прогнозу дожития (модель на ранних окнах) / простое правило
     «возраст верха книги >= A мс и обновлений за 500 мс <= K» (параметры подбираются на ранних окнах);
  5. оценка - только на поздних окнах.
"""
from __future__ import annotations

import argparse
import gc
import itertools
import os
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from fill_predict import FEATS, features
from lead_lag import PM, read
from live_vs_replay import orders_table, would_fill
from momentum_features import fit_logit
from replay import Params, collect_signals, execute, load_source, parse_slips
from risk_sim import portfolio

LS = [225, 275, 300, 325, 375, 450, 575, 775, 1200]
ARRIVE_MS = 25.0
BACK_MS = 22.0
SLOW_MS = 400.0
CAPS = dict(max_orders_window=10, max_spend_window=30.0, max_spend_day=1e9, max_loss_day=1e9, min_interval=1.0,
            after_fill_interval=5.0, release_unfilled=True)


def to_grid(eff: np.ndarray) -> np.ndarray:
    ls = np.array(LS, float)
    return np.array([int(np.argmin(np.abs(ls - e))) for e in eff], dtype=int)


def day_root(roots: list[str], w: int) -> str | None:
    name = datetime.fromtimestamp(w, tz=timezone.utc).strftime("%Y-%m-%d")
    for r in roots:
        if os.path.basename(os.path.normpath(r)) == name:
            return r
    return None


def live_latency_model(live_roots: list[str], roots: list[str], source: str) -> dict:
    """Распределение задержки живых ордеров, исполнимых при приходе, и модель вероятности медленного ответа по книге."""
    default = dict(all_idx=to_grid(np.array([250.0, 275.0, 300.0, 325.0, 375.0])), fast_idx=to_grid(np.array([275.0])),
                   slow_idx=to_grid(np.array([775.0])), model=None, n=0)
    d = orders_table(live_roots) if live_roots else pd.DataFrame()
    if d.empty:
        return default
    d["root"] = [day_root(roots, int(w)) for w in d.w]
    d = d[d.root.notna()]
    parts = []
    for root, g in d.groupby("root"):
        pm = PM(read(root, "pm_top"))
        g = g[g.w.isin(pm.by_w)].copy()
        g["arrive"] = [would_fill(pm, r.w, r.sgn, r.t_ms + ARRIVE_MS, float(r.limit), 1.0) for r in g.itertuples()]
        g = g[g.arrive]
        sigs = [dict(w=int(x.w), sgn=int(x.sgn), t=float(x.t_ms), view=float(x.ask_signal) if np.isfinite(x.ask_signal) else float(x.limit) - 0.03,
                     edge=float(x.edge_c) / 100.0 if np.isfinite(x.edge_c) else 0.03) for x in g.itertuples()]
        f = features(root, source, g, sigs)
        if len(f):
            parts.append(f.merge(g[["w", "t_ms", "sgn", "http_ms", "total_ms"]].rename(columns={"t_ms": "t"}), on=["w", "t", "sgn"], how="inner"))
        del pm
        gc.collect()
    if not parts:
        return default
    f = pd.concat(parts, ignore_index=True)
    eff = np.clip(f.total_ms.values.astype(float) - BACK_MS, LS[0], LS[-1])
    slow = (f.http_ms.values > SLOW_MS)
    X = f[FEATS].astype(float).fillna(0.0)
    mu, sd = X.mean(), X.std().replace(0, 1.0)
    b0, beta = fit_logit(((X - mu) / sd).values, slow.astype(float), np.zeros(len(f)), l2=10.0)
    idx = to_grid(eff)
    return dict(all_idx=idx, fast_idx=idx[~slow] if (~slow).any() else idx, slow_idx=idx[slow] if slow.any() else idx,
                model=(mu, sd, b0, beta), n=len(f), slow_share=float(slow.mean()))


def p_slow(sig: pd.DataFrame, lat: dict) -> np.ndarray:
    if lat["model"] is None:
        return np.full(len(sig), 0.25)
    mu, sd, b0, beta = lat["model"]
    Z = ((sig[FEATS].astype(float).fillna(0.0) - mu) / sd).values
    return 1 / (1 + np.exp(-(b0 + Z @ beta)))


def build(roots: list[str], source: str):
    sig_frames, ex_frames = [], []
    for root in roots:
        pt = read(root, "pm_top")
        wn = read(root, "windows").drop_duplicates("slug", keep="last")
        winners = dict(zip(wn.start.astype(int), wn.official_winner))
        t, px = load_source(root, source)
        sigs = [s for s in collect_signals(pt, t, px, [Params(0.03, 1.0)]) if s["w"] in winners]
        pm = PM(pt)
        ex = execute(sigs, pm, winners, LS, slips=parse_slips("3"))
        f = features(root, source, ex, sigs, series=(t, px))
        arr = []
        for s in sigs:
            st = pm.state(s["w"], s["t"] + ARRIVE_MS, "srv")
            lim = round(s["view"] + 0.03, 4)
            if st is None:
                arr.append(False)
                continue
            px_s = st[1] if s["sgn"] > 0 else (1 - st[0] if np.isfinite(st[0]) else np.nan)
            arr.append(bool(np.isfinite(px_s) and px_s <= lim + 1e-9))
        if f.empty:
            continue
        key = pd.DataFrame([dict(w=s["w"], t=s["t"], sgn=s["sgn"], arrive=a) for s, a in zip(sigs, arr)]).drop_duplicates(["w", "t", "sgn"])
        f = f.merge(key, on=["w", "t", "sgn"], how="left").drop_duplicates(["w", "t", "sgn"]).reset_index(drop=True)
        sig_frames.append(f)
        ex_frames.append(ex.drop_duplicates(["w", "t", "sgn", "L"]))
        del pt, wn, t, px, sigs, pm, ex
        gc.collect()
    if not sig_frames:
        raise SystemExit("нет сигналов")
    return pd.concat(sig_frames, ignore_index=True), pd.concat(ex_frames, ignore_index=True)


def make_table(sig: pd.DataFrame, ex: pd.DataFrame) -> dict:
    """По каждому сигналу и каждой задержке: исполнение и результат (массивы для быстрых розыгрышей)."""
    sig = sig.reset_index(drop=True)
    key = sig[["w", "t", "sgn"]].copy()
    key["i"] = np.arange(len(sig))
    e = ex.merge(key, on=["w", "t", "sgn"], how="inner")
    out = {"L": {}}
    for j, L in enumerate(LS):
        g = e[e.L == L].set_index("i").reindex(np.arange(len(sig)))
        out["L"][j] = dict(fill=g.fill.fillna(False).values.astype(bool), px=g.px.values, qty=g.qty.fillna(0).values, settle=g.settle.values,
                           limit=g.limit.values, tgt=g.tgt.values, edge=g.edge.values)
    return out


def draw(sig: pd.DataFrame, tab: dict, keep: np.ndarray, lat: dict, mode: str, ps: np.ndarray, rng) -> pd.DataFrame:
    n = len(sig)
    if mode == "indep":
        pick = rng.choice(lat["all_idx"], size=n)
    else:
        slow = rng.random(n) < ps
        pick = np.where(slow, rng.choice(lat["slow_idx"], size=n), rng.choice(lat["fast_idx"], size=n))
    fill = np.zeros(n, bool)
    px, qty, settle, limit, tgt, edge = (np.full(n, np.nan), np.zeros(n), np.full(n, np.nan), np.full(n, np.nan), np.full(n, np.nan), np.full(n, np.nan))
    for j in range(len(LS)):
        m = pick == j
        a = tab["L"][j]
        fill[m] = a["fill"][m]
        px[m], qty[m], settle[m], limit[m], tgt[m], edge[m] = a["px"][m], a["qty"][m], a["settle"][m], a["limit"][m], a["tgt"][m], a["edge"][m]
    fill &= sig.arrive.fillna(False).values.astype(bool)
    d = pd.DataFrame(dict(w=sig.w.values, t=sig.t.values, sgn=sig.sgn.values, fill=fill, px=px, qty=qty, settle=settle, limit=limit, tgt=tgt, edge=edge))
    return d[keep].reset_index(drop=True)


def simulate(sig, tab, keep, lat, mode, ps, draws=30, seed=0) -> dict:
    rng = np.random.default_rng(seed)
    acc = []
    for _ in range(draws):
        d = draw(sig, tab, keep, lat, mode, ps, rng)
        if d.empty:
            continue
        r = portfolio(d, **CAPS)
        acc.append([r["ордеров"], r["исполнений"], r["pnl_всего"], r["худшее_окно"], r["просадка"]])
    a = np.array(acc) if acc else np.zeros((1, 5))
    return dict(ордеров=a[:, 0].mean(), исполн=a[:, 1].mean(), pnl=a[:, 2].mean(), pnl_sd=a[:, 2].std(), худшее_окно=a[:, 3].mean(), просадка=a[:, 4].mean())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--live-data", nargs="*", default=[])
    ap.add_argument("--draws", type=int, default=30)
    a = ap.parse_args()
    pd.set_option("display.width", 230)
    lat = live_latency_model(a.live_data, a.roots, a.source)
    gc.collect()
    sig, ex = build(a.roots, a.source)
    tab = make_table(sig, ex)
    del ex
    gc.collect()
    ps = p_slow(sig, lat)
    print(f"сигналов {len(sig)}, окон {sig.w.nunique()}; живых исполнимых при приходе ордеров для задержки: {lat['n']}, медленных {lat.get('slow_share', float('nan')):.1%}")
    print("доля задержек по корзинам L (все исполнимые при приходе):", dict(zip(LS, np.round(np.bincount(lat["all_idx"], minlength=len(LS)) / len(lat["all_idx"]), 3))))
    print(f"прогнозная доля медленных ответов на сигналах: среднее {ps.mean():.3f}, по квартилям возраста верха книги: " +
          ", ".join(f"{ps[(pd.qcut(sig.age.rank(method='first'), 4, labels=False) == k).values].mean():.2f}" for k in range(4)))
    cut = sig.w.quantile(0.6)
    tr_m, te_m = (sig.w <= cut).values, (sig.w > cut).values
    days_te = max((sig.t[te_m].max() - sig.t[te_m].min()) / 86_400_000.0, 1e-9)
    print(f"обучение/подбор: окна до {cut:.0f} ({tr_m.sum()} сигналов), тест: после ({te_m.sum()} сигналов, {days_te:.2f} сут)")
    j300 = LS.index(300)
    y = tab["L"][j300]["fill"].astype(float)
    X = sig[FEATS].astype(float).fillna(0.0)
    mu, sd = X[tr_m].mean(), X[tr_m].std().replace(0, 1.0)
    Z = ((X - mu) / sd).values
    b0, beta = fit_logit(Z[tr_m], y[tr_m], np.zeros(tr_m.sum()), l2=5.0)
    p = 1 / (1 + np.exp(-(b0 + Z @ beta)))
    print("модель дожития: " + ", ".join(f"{c} {b:+.2f}" for c, b in zip(FEATS, beta)))
    rules = []
    for A, K in itertools.product([0, 50, 100, 200, 400, 800], [1, 2, 3, 5, 99]):
        keep = ((sig.age >= A) & (sig.n500 <= K)).values
        if (keep & tr_m).sum() < 300:
            continue
        r = simulate(sig, tab, keep & tr_m, lat, "cond", ps, draws=8)
        rules.append((A, K, r["pnl"], r["ордеров"], keep))
    rules.sort(key=lambda x: -x[2])
    print("\nправило «возраст >= A мс и обновлений за 500 мс <= K», условная задержка: топ-5 на обучающих окнах (pnl $ за обучающий период)")
    for A, K, pnl, n, _ in rules[:5]:
        print(f"  A={A:4d} K={K:2d}: pnl ${pnl:7.2f}, ордеров {n:6.0f}")
    best = rules[0] if rules else None
    strategies = [("все сигналы", np.ones(len(sig), bool))]
    for q in (0.7, 0.5, 0.3):
        strategies.append((f"верхние {int(q * 100)}% по прогнозу дожития", p >= np.quantile(p[te_m], 1 - q)))
    if best:
        strategies.append((f"правило A={best[0]} K={best[1]}", best[4]))
    strategies.append(("случайные 50% (контроль)", np.random.default_rng(5).random(len(sig)) < 0.5))
    for mode, title in (("indep", "независимая задержка (оптимистично)"), ("cond", "условная задержка: в тихой книге ответы медленнее")):
        rows = []
        for name, keep in strategies:
            r = simulate(sig, tab, keep & te_m, lat, mode, ps, draws=a.draws, seed=1)
            rows.append(dict(стратегия=name, сигналов=int((keep & te_m).sum()), ордеров=round(r["ордеров"]), исполнений=round(r["исполн"], 1),
                             pnl_долл=round(r["pnl"], 2), pnl_в_сутки=round(r["pnl"] / days_te, 2), разброс=round(r["pnl_sd"], 2),
                             худшее_окно=round(r["худшее_окно"], 2), просадка=round(r["просадка"], 2)))
        print(f"\n=== ТЕСТ на поздних окнах, {title} ===")
        print(pd.DataFrame(rows).to_string(index=False))
    print("(разброс - стандартное отклонение pnl между случайными розыгрышами задержки, не доверительный интервал)")


if __name__ == "__main__":
    main()
