"""Серии сигналов («пачки ордеров в один момент»): как часто, чем кончаются и как ограничить вред.

    python burst_sim.py data/2026-10-10 data/2026-10-11 --source bybit --thr 0.03 --sigma-mult 1 --slip 3

Разделы отчёта:
  A. структура пачек: сигналы одного окна и стороны с паузой между соседними не больше --burst-gap секунд;
  B. результат по номеру ордера в пачке, по паузе до предыдущего сигнала и по силе первого сигнала;
  C. итог пачек в долларах и насколько результаты внутри пачки зависимы (все выигрыши/все проигрыши);
  D. способы ограничить вред (потолок ордеров на пачку/сторону, пауза, требование усиления сигнала) через лимиты бота,
     БЕЗ дневных лимитов трат и убытка (чтобы видеть полную картину).
Исполнение по состоянию книги Polymarket на сервере в момент матча, покупка и удержание до конца окна.
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from lead_lag import PM, read
from replay import Params, collect_signals, execute, load_source, parse_slips
from risk_sim import portfolio

NO_DAY = dict(max_spend_day=1e9, max_loss_day=1e9)


def build(roots, source, thr, sigma, slip, lat, since):
    frames = []
    for root in roots:
        pt = read(root, "pm_top")
        wn = read(root, "windows").drop_duplicates("slug", keep="last")
        winners = dict(zip(wn.start.astype(int), wn.official_winner))
        t, px = load_source(root, source)
        sigs = collect_signals(pt, t, px, [Params(thr, sigma)])
        frames.append(execute(sigs, PM(pt), winners, lat, slips=parse_slips(slip)))
        print(f"{root}: сигналов {len(sigs)}")
    df = pd.concat(frames, ignore_index=True)
    if since:
        df = df[df.w >= since]
    df = df[df.won.notna() | ~df.fill].copy()
    df["pnl_sh"] = np.where(df.fill & df.settle.notna(), df.settle * df.qty / 5.0, 0.0)       # ц на «шейр попытки»
    df["usd"] = np.where(df.fill & df.settle.notna(), df.qty * df.settle / 100.0, 0.0)
    return df


def add_bursts(d: pd.DataFrame, gap: float) -> pd.DataFrame:
    d = d.sort_values(["w", "sgn", "t"]).copy()
    d["gap"] = d.groupby(["w", "sgn"]).t.diff() / 1000.0
    d["new"] = (d.gap.isna() | (d.gap > gap)).astype(int)
    d["burst"] = d.groupby(["w", "sgn"]).new.cumsum()
    d["pos"] = d.groupby(["w", "sgn", "burst"]).cumcount() + 1
    d["size"] = d.groupby(["w", "sgn", "burst"]).pos.transform("max")
    first_edge = d.groupby(["w", "sgn", "burst"]).edge.transform("first")
    d["edge0"] = first_edge * 100
    return d


def metrics(g: pd.DataFrame) -> pd.Series:
    f = g[g.fill]
    return pd.Series(dict(сигналов=len(g), исполн=round(g.fill.mean(), 3), цсигнал=round(g.pnl_sh.mean(), 2),
                          доля_побед=round(f.won.mean(), 3) if len(f) else np.nan))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--source", default="bybit")
    ap.add_argument("--thr", type=float, default=0.03)
    ap.add_argument("--sigma-mult", type=float, default=1.0)
    ap.add_argument("--slip", default="3")
    ap.add_argument("--latencies", default="200,300")
    ap.add_argument("--burst-gap", type=float, default=3.0, help="секунд между соседними сигналами одной пачки")
    ap.add_argument("--since", type=float, default=0)
    a = ap.parse_args()
    pd.set_option("display.width", 250)
    lat = [int(x) for x in a.latencies.split(",")]
    df = build(a.roots, a.source, a.thr, a.sigma_mult, a.slip, lat, a.since)
    days = max(df.w.nunique() * 300 / 86400.0, 1e-9)
    print(f"\nокон с сигналами: {df.w.nunique()}, период ≈ {df.w.nunique() * 300 / 3600:.1f} ч окон; сигналов {df[df.L == lat[0]].shape[0]}")

    for L in lat:
        d = add_bursts(df[df.L == L], a.burst_gap)
        print(f"\n################ задержка ордера {L} мс, пачка = сигналы с паузой ≤ {a.burst_gap:g} с ################")
        # --- A
        b = d[d.pos == 1]
        bins = pd.cut(b["size"], [0, 1, 2, 3, 5, 10, 20, 1000], labels=["1", "2", "3", "4-5", "6-10", "11-20", "21+"])
        A = b.groupby(bins, observed=True).agg(пачек=("size", "size"), сигналов=("size", "sum"))
        A["доля_сигналов_%"] = (100 * A["сигналов"] / A["сигналов"].sum()).round(1)
        span = d.groupby(["w", "sgn", "burst"]).t.agg(lambda x: (x.max() - x.min()) / 1000.0)
        print("\n=== A. размеры пачек ===")
        print(A.to_string())
        print(f"пачек всего {len(b)}, в среднем {len(d) / len(b):.2f} сигнала; длительность пачки из 3+ сигналов: "
              f"медиана {span[b['size'].values >= 3].median():.1f} с, макс {span.max():.0f} с")
        # --- B
        d["ordb"] = pd.cut(d.pos, [0, 1, 2, 3, 5, 10, 1000], labels=["1-й", "2-й", "3-й", "4-5-й", "6-10-й", "11-й+"])
        print("\n=== B1. результат по номеру ордера в пачке ===")
        print(d.groupby("ordb", observed=True).apply(metrics).to_string())
        gb = pd.cut(d.gap, [0, 1.5, 2.5, 5, 10, 30, 1e9], labels=["1-1.5 с", "1.5-2.5", "2.5-5", "5-10", "10-30", "30+"])
        print("\n=== B2. по паузе до предыдущего сигнала той же стороны в окне (первый сигнал окна не входит) ===")
        print(d[d.gap.notna()].groupby(gb[d.gap.notna()], observed=True).apply(metrics).to_string())
        print("\n=== B3. по силе первого сигнала пачки (edge, центов): размер пачки и результат 1-го / остальных ===")
        eb = pd.cut(d.edge0, [0, 4, 6, 10, 1000], labels=["3-4", "4-6", "6-10", "10+"])
        rows = []
        for k, g in d.groupby(eb, observed=True):
            first, rest = g[g.pos == 1], g[g.pos > 1]
            rows.append(dict(edge_первого_ц=k, пачек=len(first), ср_размер=round(g.groupby(["w", "sgn", "burst"]).size().mean(), 2),
                             цсигнал_1й=round(first.pnl_sh.mean(), 2), цсигнал_остальных=round(rest.pnl_sh.mean(), 2) if len(rest) else np.nan))
        print(pd.DataFrame(rows).to_string(index=False))
        # --- C
        fl = d[d.fill].copy()
        grp = fl.groupby(["w", "sgn", "burst"]).agg(n=("usd", "size"), usd=("usd", "sum"), win=("won", "mean")).reset_index()
        multi = grp[grp.n >= 2]
        p = fl.won.mean()
        same_exp = np.mean([p ** n + (1 - p) ** n for n in multi.n]) if len(multi) else np.nan
        print("\n=== C. итог пачек в $ (только исполненные ордера) ===")
        print(f"пачек с исполнениями {len(grp)}, из них убыточных {(grp.usd < 0).mean():.0%}; "
              f"средний итог {grp.usd.mean():.2f}$, худшая {grp.usd.min():.2f}$, лучшая {grp.usd.max():.2f}$")
        if len(multi):
            same = ((multi.win == 0) | (multi.win == 1)).mean()
            print(f"пачек с 2+ исполнениями: {len(multi)}; все ордера пачки дали один и тот же исход в {same:.0%} случаев "
                  f"(при независимости ожидалось бы {same_exp:.0%}) — чем выше разрыв, тем сильнее зависимость")

    # --- D. способы ограничить вред
    print("\n################ D. способы ограничить вред (лимиты окна 10 ордеров и $30 остаются, дневных лимитов нет) ################")
    scen = [
        ("как сейчас: интервал 1 с", dict(min_interval=1.0)),
        ("пауза между любыми ордерами 3 с", dict(min_interval=3.0)),
        ("пауза 10 с", dict(min_interval=10.0)),
        ("пауза 30 с", dict(min_interval=30.0)),
        ("пауза 10 с на сторону окна", dict(min_interval=1.0, side_interval=10.0)),
        ("не больше 1 ордера на сторону окна", dict(min_interval=1.0, max_orders_side=1)),
        ("не больше 2 на сторону окна", dict(min_interval=1.0, max_orders_side=2)),
        ("не больше 3 на сторону окна", dict(min_interval=1.0, max_orders_side=3)),
        ("не больше 5 на сторону окна", dict(min_interval=1.0, max_orders_side=5)),
        ("следующий ордер стороны только если edge выше на 1 ц", dict(min_interval=1.0, edge_step_c=1.0)),
        ("то же, +3 на сторону", dict(min_interval=1.0, edge_step_c=1.0, max_orders_side=3)),
        ("пауза 10 с + не больше 3 на сторону", dict(min_interval=10.0, max_orders_side=3)),
        ("без лимитов окна, интервал 1 с (для сравнения)", dict(min_interval=1.0, max_orders_window=10_000, max_spend_window=1e9)),
    ]
    rows = []
    for L in lat:
        sub = df[df.L == L]
        for name, kw in scen:
            res = portfolio(sub, **{**NO_DAY, **kw})
            rows.append(dict(L=L, сценарий=name, ордеров=res["ордеров"], исполн=res["исполнений"], pnl_всего=res["pnl_всего"],
                             в_сутки=res["pnl_в_сутки"], худший_день=res["худший_день"], просадка=res["просадка"],
                             худшее_окно=res["худшее_окно"], на_исполнение=round(res["pnl_всего"] / max(res["исполнений"], 1), 2)))
    print(pd.DataFrame(rows).to_string(index=False))


if __name__ == "__main__":
    main()
