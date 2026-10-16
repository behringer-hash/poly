"""Можно ли предсказать исполнение ордера по книге и задержке: три проверки.

    python fill_predict.py data/2026-10-13 data/2026-10-14 --live-data bot_data_c1 --source bybit

A. Каждый живой ордер против книги сервера в момент его матча, где момент = t_сигнала + (время ответа - обратная дорога).
   Если исполнение живых ордеров объясняется «книга сервера + реальная задержка», то расхождение с реплеем целиком в задержке.
B. Реплей C1 с задержкой не фиксированной (250/300/400), а взятой из ЖИВОГО распределения (с тяжёлым хвостом биржи):
   ожидаемая доля исполнений и прибыль на сигнал при реальной задержке.
C. Предсказание дожития ордера до матча (L=300 и 500 мс) по признакам книги и рынка, известным в момент сигнала:
   возраст верха книги, число обновлений за 500 мс, спред, объём на уровне, движение цены за 300/1000 мс до сигнала,
   сделки рынка за 1 с, размер скачка BTC, сила сигнала, время до конца окна. Обучение на ранних окнах, тест на поздних.
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from lead_lag import PM, read
from live_vs_replay import orders_table, would_fill
from momentum_features import fit_logit, last_at
from replay import Params, collect_signals, execute, load_source, parse_slips
from reprice_timing import side_series

BACK_MS = 22.0                      # обратная дорога ответа (половина RTT до CLOB)
BINS = [150, 200, 250, 300, 350, 400, 500, 650, 900, 1500]


def auc(y: np.ndarray, s: np.ndarray) -> float:
    y = np.asarray(y, bool)
    n1, n0 = y.sum(), (~y).sum()
    if n1 == 0 or n0 == 0:
        return np.nan
    r = pd.Series(s).rank().values
    return float((r[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def part_a(live_roots, pm_roots):
    d = orders_table(live_roots)
    if d.empty:
        print("A: нет живых ордеров")
        return None
    pm = PM(pd.concat([read(r, "pm_top") for r in pm_roots], ignore_index=True))
    d = d[d.w.isin(pm.by_w)].copy()
    print(f"=== A. Живые ордера против книги сервера (ордеров {len(d)}, исполнено {d.filled_f.mean():.1%}) ===")
    rows = []
    for back in (0.0, BACK_MS, 60.0, 120.0):
        pred = np.array([would_fill(pm, r.w, r.sgn, r.t_ms + r.total_ms - back, float(r.limit), 1.0) for r in d.itertuples()])
        y = d.filled_f.values
        tp, fp, fn, tn = int((pred & y).sum()), int((pred & ~y).sum()), int((~pred & y).sum()), int((~pred & ~y).sum())
        rows.append(dict(обратная_дорога_мс=back, прогноз_исп=round(pred.mean(), 3), точность=round((pred == y).mean(), 3),
                         TP=tp, FP=fp, FN=fn, TN=tn, полнота=round(tp / max(tp + fn, 1), 3), точность_плюс=round(tp / max(tp + fp, 1), 3)))
    print(pd.DataFrame(rows).to_string(index=False))
    print("(для сравнения: ответ «никогда не исполнится» даёт точность "
          f"{1 - d.filled_f.mean():.3f}; FP - прогноз «исполнится», факт нет; FN - наоборот)")
    return d


def lat_weights(d: pd.DataFrame | None):
    if d is None or d.empty:
        return [200, 250, 300, 400], np.array([0.25, 0.25, 0.25, 0.25])
    eff = np.clip(d.total_ms.values.astype(float) - BACK_MS, BINS[0], BINS[-1] - 1)
    cnt, _ = np.histogram(eff, bins=BINS)
    mid = [(BINS[i] + BINS[i + 1]) / 2 for i in range(len(BINS) - 1)]
    return [int(m) for m in mid], cnt / cnt.sum()


def part_b(roots, source, live_orders):
    Ls, w = lat_weights(live_orders)
    print("\n=== B. Реплей C1 с задержкой из живого распределения ===")
    print("корзины L, мс:", Ls, " веса:", np.round(w, 3))
    frames = []
    for root in roots:
        pt = read(root, "pm_top")
        wn = read(root, "windows").drop_duplicates("slug", keep="last")
        winners = dict(zip(wn.start.astype(int), wn.official_winner))
        t, px = load_source(root, source)
        sigs = collect_signals(pt, t, px, [Params(0.03, 1.0)])
        frames.append(execute(sigs, PM(pt), winners, Ls, slips=parse_slips("3")))
    df = pd.concat(frames, ignore_index=True)
    df = df[df.won.notna() | ~df.fill]
    df["pnl"] = np.where(df.fill & df.settle.notna(), df.settle * df.qty / 5.0, 0.0)
    wmap = dict(zip(Ls, w))
    df["wt"] = df.L.map(wmap)
    df["wpnl"] = df.pnl * df.wt
    df["wfill"] = df.fill.astype(float) * df.wt
    per = df.groupby(["w", "t", "sgn"]).agg(pnl=("wpnl", "sum"), fill=("wfill", "sum")).reset_index()
    g = per.groupby("w").agg(s=("pnl", "sum"), n=("pnl", "size"))
    rng = np.random.default_rng(0)
    idx = rng.integers(0, len(g), (800, len(g)))
    bs = g.s.values[idx].sum(1) / g.n.values[idx].sum(1)
    print(f"сигналов {len(per)}, окон {per.w.nunique()}: ожидаемая доля исполнений {per.fill.mean():.1%}, прибыль {per.pnl.mean():.2f} ц на сигнал "
          f"[{np.percentile(bs, 2.5):.2f}; {np.percentile(bs, 97.5):.2f}]")
    by = df.groupby("L").agg(доля_исп=("fill", "mean"), цсигнал=("pnl", "mean")).round(3)
    by["вес"] = [round(wmap[k], 3) for k in by.index]
    print("по корзинам задержки (при фиксированной L):")
    print(by.to_string())
    return df


def features(root, source, df_rows, sigs):
    """Признаки сигналов на момент t (только то, что известно к этому моменту)."""
    pt = read(root, "pm_top")
    u = pt[pt.o == "U"].sort_values("recv_ms")
    by_w = {int(w): g for w, g in u.groupby("w")}
    pm = PM(pt)
    tr = read(root, "pm_trades", ["server_ts", "w", "o", "side", "price", "size"])
    if len(tr):
        tr = tr[tr.side.astype(str).str.upper().str.startswith("B")]
    tr_by = {k: g.sort_values("server_ts") for k, g in tr.groupby(["w", "o"])} if len(tr) else {}
    t_src, px = load_source(root, source)
    rows = []
    for s in sigs:
        w, sgn, t = s["w"], s["sgn"], s["t"]
        g = by_w.get(w)
        arr = pm.by_w.get(w, {}).get("rcv")
        if g is None or arr is None:
            continue
        rec = g.recv_ms.values
        i = np.searchsorted(rec, t, side="right") - 1
        if i < 0:
            continue
        ts, ps = side_series(arr, sgn)
        p0 = ps[np.searchsorted(ts, t, side="right") - 1]

        def prev(x):
            j = np.searchsorted(ts, t - x, side="right") - 1
            return 100 * (p0 - ps[j]) if j >= 0 else np.nan

        sz = g.ask_sz.values[i] if sgn > 0 else g.bid_sz.values[i]
        tg = tr_by.get((w, "U" if sgn > 0 else "D"))
        n_tr = sz_tr = 0.0
        if tg is not None:
            m = (tg.server_ts.values > t - 1000) & (tg.server_ts.values <= t)
            n_tr, sz_tr = float(m.sum()), float(tg["size"].values[m].sum())
        rows.append(dict(w=w, t=t, sgn=sgn, age=t - rec[i], n500=float(((rec > t - 500) & (rec <= t)).sum()),
                         d=float(g.d.values[i]), spread=100 * float(g.ask.values[i] - g.bid.values[i]), size=float(sz) if np.isfinite(sz) else 0.0,
                         lvl=s["view"], mv300=prev(300), mv1000=prev(1000), n_tr=n_tr, sz_tr=sz_tr,
                         btc=abs(float(last_at(t_src, px, t) - last_at(t_src, px, t - 500))), edge=100 * s["edge"],
                         T=w + 300 - t / 1000))
    f = pd.DataFrame(rows)
    return f


FEATS = ["age", "n500", "d", "spread", "size", "lvl", "mv300", "mv1000", "n_tr", "sz_tr", "btc", "edge", "T"]


def part_c(roots, source):
    print("\n=== C. Предсказание дожития ордера до матча по признакам книги ===")
    parts = []
    for root in roots:
        pt = read(root, "pm_top")
        wn = read(root, "windows").drop_duplicates("slug", keep="last")
        winners = dict(zip(wn.start.astype(int), wn.official_winner))
        t, px = load_source(root, source)
        sigs = collect_signals(pt, t, px, [Params(0.03, 1.0)])
        ex = execute(sigs, PM(pt), winners, [300, 500], slips=parse_slips("3"))
        f = features(root, source, ex, sigs)
        if f.empty:
            continue
        for L in (300, 500):
            e = ex[ex.L == L][["w", "t", "sgn", "fill", "settle", "qty"]].rename(columns={"fill": f"y{L}", "settle": f"st{L}", "qty": f"q{L}"})
            f = f.merge(e, on=["w", "t", "sgn"], how="left")
        parts.append(f)
    d = pd.concat(parts, ignore_index=True)
    d = d.dropna(subset=["y300"]).reset_index(drop=True)
    d["pnl300"] = np.where(d.y300.astype(bool) & d.st300.notna(), d.st300 * d.q300 / 5.0, 0.0)
    cut = d.w.quantile(0.6)
    tr, te = d[d.w <= cut], d[d.w > cut]
    print(f"сигналов {len(d)}; обучение {len(tr)} (окна до {cut:.0f}), тест {len(te)}; доля исполнений: L=300 {d.y300.mean():.1%}, L=500 {d.y500.mean():.1%}")
    X = d[FEATS].astype(float).fillna(0.0)
    mu, sd = X[d.w <= cut].mean(), X[d.w <= cut].std().replace(0, 1.0)
    Z = ((X - mu) / sd).values
    ztr, zte = Z[(d.w <= cut).values], Z[(d.w > cut).values]
    for L in (300, 500):
        ytr, yte = tr[f"y{L}"].astype(float).values, te[f"y{L}"].astype(float).values
        b0, beta = fit_logit(ztr, ytr, np.zeros(len(ytr)), l2=5.0)
        p_te = 1 / (1 + np.exp(-(b0 + zte @ beta)))
        print(f"\n--- L={L} мс: AUC на тесте {auc(yte, p_te):.3f} (0.5 - ничего не предсказывает); база исполнения {yte.mean():.3f}")
        print("коэффициенты (на сигму признака): " + ", ".join(f"{c} {b:+.2f}" for c, b in zip(FEATS, beta)))
        dec = pd.qcut(pd.Series(p_te).rank(method="first"), 5, labels=False)
        rows = [dict(квинтиль_прогноза=int(k), n=int((dec == k).sum()), прогноз=round(float(p_te[dec == k].mean()), 3),
                     факт=round(float(yte[(dec == k).values].mean()), 3)) for k in sorted(dec.unique())]
        print(pd.DataFrame(rows).to_string(index=False))
        if L == 300:
            te2 = te.assign(p=p_te)
            hi, lo = te2[te2.p >= te2.p.median()], te2[te2.p < te2.p.median()]
            print(f"прибыль на сигнал (L=300): верхняя половина по прогнозу исполнения {hi.pnl300.mean():+.2f} ц "
                  f"(исполн. {hi.y300.mean():.1%}), нижняя {lo.pnl300.mean():+.2f} ц (исполн. {lo.y300.mean():.1%})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--live-data", nargs="*", default=[])
    ap.add_argument("--parts", default="abc")
    a = ap.parse_args()
    pd.set_option("display.width", 220)
    live = part_a(a.live_data, a.roots) if "a" in a.parts and a.live_data else None
    if "b" in a.parts:
        if live is None and a.live_data:
            live = orders_table(a.live_data)
        part_b(a.roots, a.source, live)
    if "c" in a.parts:
        part_c(a.roots, a.source)


if __name__ == "__main__":
    main()
