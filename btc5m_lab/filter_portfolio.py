"""Отбор сигналов по книге: помогает ли он в итоговой прибыли при реальных правилах бота и живой задержке.

    python filter_portfolio.py data/2026-10-10 ... data/2026-10-16 --live-data bot_data_c1 --source bybit

Что делаем:
  1. сигналы C1 (Bybit, порог 0.03, переплата 3 ц) за все дни; исполнение при каждой из набора задержек L (книга сервера);
  2. «живая» задержка: ордер, который в момент прихода на биржу (t+25 мс) уже не исполним, не исполнится; у исполнимого задержка
     берётся из ЭМПИРИЧЕСКОГО распределения ваших живых ордеров, которые были исполнимы при приходе (у них хвост тяжелее,
     чем у остальных). 30 розыгрышей на каждый вариант;
  3. портфель с правилами бота: пауза 1 с после любого ордера и 5 с после покупки, пустые ордера лимит окна не занимают,
     не больше 10 ордеров и $30 на окно, без дневных лимитов (чтобы видеть полную картину);
  4. стратегии отбора: все сигналы / верхние q% по прогнозу дожития (логистическая модель на ранних окнах) / простое правило
     «возраст верха книги >= A мс и обновлений за 500 мс <= K» (параметры подбираются на ранних окнах);
  5. оценка - только на поздних окнах (которых модель и правило не видели).
"""
from __future__ import annotations

import argparse
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
CAPS = dict(max_orders_window=10, max_spend_window=30.0, max_spend_day=1e9, max_loss_day=1e9, min_interval=1.0,
            after_fill_interval=5.0, release_unfilled=True)


def empirical_pool(live_roots: list[str], pm: PM) -> np.ndarray:
    """Эффективная задержка до матча (мс) у живых ордеров, исполнимых в момент прихода на биржу."""
    d = orders_table(live_roots)
    if d.empty:
        return np.array([250.0, 275.0, 300.0, 325.0, 375.0])
    d = d[d.w.isin(pm.by_w)]
    ok = [would_fill(pm, r.w, r.sgn, r.t_ms + ARRIVE_MS, float(r.limit), 1.0) for r in d.itertuples()]
    eff = np.clip(d.total_ms.values.astype(float)[np.array(ok, bool)] - BACK_MS, LS[0], LS[-1])
    return eff


def to_grid(eff: np.ndarray) -> np.ndarray:
    ls = np.array(LS, float)
    return np.array([int(np.argmin(np.abs(ls - e))) for e in eff])


def day_root(roots: list[str], w: int) -> str | None:
    name = datetime.fromtimestamp(w, tz=timezone.utc).strftime("%Y-%m-%d")
    for r in roots:
        if os.path.basename(os.path.normpath(r)) == name:
            return r
    return None


def build(roots: list[str], source: str, live_roots: list[str]):
    sig_frames, grid_arrays, pools = [], [], []
    pm_all = None
    for root in roots:
        pt = read(root, "pm_top")
        wn = read(root, "windows").drop_duplicates("slug", keep="last")
        winners = dict(zip(wn.start.astype(int), wn.official_winner))
        t, px = load_source(root, source)
        sigs = [s for s in collect_signals(pt, t, px, [Params(0.03, 1.0)]) if s["w"] in winners]
        pm = PM(pt)
        if pm_all is None:
            pm_all = pm
        else:
            pm_all.by_w.update(pm.by_w)
        ex = execute(sigs, pm, winners, LS, slips=parse_slips("3"))
        f = features(root, source, ex, sigs)
        if f.empty:
            continue
        # исполнимость при приходе на биржу
        arr = []
        for s in sigs:
            st = pm.state(s["w"], s["t"] + ARRIVE_MS, "srv")
            lim = round(s["view"] + 0.03, 4)
            if st is None:
                arr.append(False)
                continue
            px_s = st[1] if s["sgn"] > 0 else (1 - st[0] if np.isfinite(st[0]) else np.nan)
            arr.append(bool(np.isfinite(px_s) and px_s <= lim + 1e-9))
        key = pd.DataFrame([dict(w=s["w"], t=s["t"], sgn=s["sgn"], arrive=a) for s, a in zip(sigs, arr)]).drop_duplicates(["w", "t", "sgn"])
        f = f.merge(key, on=["w", "t", "sgn"], how="left")
        ex = ex.drop_duplicates(["w", "t", "sgn", "L"])
        sig_frames.append(f.drop_duplicates(["w", "t", "sgn"]).reset_index(drop=True))
        grid_arrays.append(ex)
    if not sig_frames:
        raise SystemExit("нет сигналов")
    sig = pd.concat(sig_frames, ignore_index=True)
    ex = pd.concat(grid_arrays, ignore_index=True)
    pool = empirical_pool(live_roots, pm_all) if live_roots else np.array([250.0, 275.0, 300.0, 325.0, 375.0])
    return sig, ex, pool


def make_table(sig: pd.DataFrame, ex: pd.DataFrame) -> dict:
    """По каждому сигналу и каждой задержке: исполнение и результат (в виде массивов для быстрых розыгрышей)."""
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


def draw(sig: pd.DataFrame, tab: dict, keep: np.ndarray, pool_idx: np.ndarray, rng) -> pd.DataFrame:
    n = len(sig)
    pick = rng.choice(pool_idx, size=n)
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


def simulate(sig, tab, keep, pool_idx, draws=30, seed=0) -> dict:
    rng = np.random.default_rng(seed)
    acc = []
    for _ in range(draws):
        d = draw(sig, tab, keep, pool_idx, rng)
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
    sig, ex, pool = build(a.roots, a.source, a.live_data)
    pool_idx = to_grid(pool)
    print(f"сигналов {len(sig)}, окон {sig.w.nunique()}; живых исполнимых ордеров для распределения задержки: {len(pool)}")
    print("доля задержек по корзинам L:", dict(zip(LS, np.round(np.bincount(pool_idx, minlength=len(LS)) / len(pool_idx), 3))))
    tab = make_table(sig, ex)
    cut = sig.w.quantile(0.6)
    tr_m, te_m = (sig.w <= cut).values, (sig.w > cut).values
    days_te = max((sig.t[te_m].max() - sig.t[te_m].min()) / 86_400_000.0, 1e-9)
    print(f"обучение/подбор: окна до {cut:.0f} ({tr_m.sum()} сигналов), тест: после ({te_m.sum()} сигналов, {days_te:.2f} сут)")
    # модель дожития (цель - исполнение при L=300)
    j300 = LS.index(300)
    y = tab["L"][j300]["fill"].astype(float)
    X = sig[FEATS].astype(float).fillna(0.0)
    mu, sd = X[tr_m].mean(), X[tr_m].std().replace(0, 1.0)
    Z = ((X - mu) / sd).values
    b0, beta = fit_logit(Z[tr_m], y[tr_m], np.zeros(tr_m.sum()), l2=5.0)
    p = 1 / (1 + np.exp(-(b0 + Z @ beta)))
    print("модель дожития: " + ", ".join(f"{c} {b:+.2f}" for c, b in zip(FEATS, beta)))
    # простое правило: подбор на обучающих окнах
    rules = []
    for A, K in itertools.product([0, 50, 100, 200, 400, 800], [1, 2, 3, 5, 99]):
        keep = ((sig.age >= A) & (sig.n500 <= K)).values
        if (keep & tr_m).sum() < 300:
            continue
        r = simulate(sig, tab, keep & tr_m, pool_idx, draws=8)
        rules.append((A, K, r["pnl"], r["ордеров"], keep))
    rules.sort(key=lambda x: -x[2])
    print("\nправило «возраст >= A мс и обновлений за 500 мс <= K»: топ-5 на обучающих окнах (pnl $ на всём обучающем периоде)")
    for A, K, pnl, n, _ in rules[:5]:
        print(f"  A={A:4d} K={K:2d}: pnl ${pnl:7.2f}, ордеров {n:6.0f}")
    best = rules[0] if rules else None
    rows = []

    def run(name, keep):
        r = simulate(sig, tab, keep & te_m, pool_idx, draws=a.draws, seed=1)
        n_sig = int((keep & te_m).sum())
        rows.append(dict(стратегия=name, сигналов=n_sig, ордеров=round(r["ордеров"]), исполнений=round(r["исполн"], 1), pnl_долл=round(r["pnl"], 2),
                         pnl_в_сутки=round(r["pnl"] / days_te, 2), разброс_розыгрышей=round(r["pnl_sd"], 2),
                         худшее_окно=round(r["худшее_окно"], 2), просадка=round(r["просадка"], 2)))

    run("все сигналы", np.ones(len(sig), bool))
    for q in (0.7, 0.5, 0.3):
        thr = np.quantile(p[te_m], 1 - q)
        run(f"верхние {int(q * 100)}% по прогнозу дожития", p >= thr)
    if best:
        run(f"правило A={best[0]} K={best[1]}", best[4])
    rng = np.random.default_rng(5)
    run("случайные 50% (контроль)", rng.random(len(sig)) < 0.5)
    print("\n=== ТЕСТ на поздних окнах: портфель с правилами бота и живой задержкой ===")
    print(pd.DataFrame(rows).to_string(index=False))
    print("(разброс_розыгрышей - стандартное отклонение pnl между 30 случайными розыгрышами задержки, не доверительный интервал)")


if __name__ == "__main__":
    main()
