"""Кто кому платит: лента сделок с кошельками (tape_fetch.py) + запись сборщика (flow_map.py), по дням.

    python flow_wallets.py prep  DATA_DIR/2026-10-27 --tapes ~/tapes --store ~/flow     # по дню
    python flow_wallets.py agg   --store ~/flow --out OUT                                 # по всем дням

prep (день):
  ev_<день>.csv.gz  заявки тейкеров внутри окна (мс, flow_map.events) + кошелёк тейкера (сопоставление с лентой:
                    окно, токен, сторона, размер ±1%, время ленты - время сервера в [-1,5; 10] с, ближайшая цена)
  tk_<день>.csv.gz  все тейкеры ленты (с T-600): rel = время ленты - начало окна (лента отстаёт от сервера ~2 с)
  mk_<день>.csv.gz  все мейкеры ленты: кошелёк мейкера и тейкера той же транзакции, глубина уровня
  wd_<день>.csv.gz  кошелёк x день: объёмы, результаты, скорость
Всё в терминах Up: dir = +1 купил Up / продал Down; p - цена Up; edge = 100*dir*(won - p) ц/шейр по исходу окна
(без комиссии; мейкерский ребейт не учтён).
agg: кошельки за все дни -> ярусы активности -> таблицы «кто кому платит» и поток по ярусам.
"""
from __future__ import annotations

import argparse
import glob
import os

import numpy as np
import pandas as pd

import flow_map as fm
from jump_study import save_parts

KEY = ["w", "ts", "wallet", "side", "outcome", "price", "size", "tx"]


def updir(outcome, side):
    up = outcome.astype(str).str.upper().str.startswith("U")
    buy = side.astype(str).str.upper().str.startswith("B")
    return np.where(up == buy, 1, -1), up


def prep(root, tapes, store):
    day = os.path.basename(os.path.normpath(root))
    fn = os.path.join(tapes, f"tape_{day}.csv.gz")
    if not os.path.exists(fn):
        print(f"{day}: нет ленты"); return
    top, tr, bnf, win = fm.load_root(root)
    tape = pd.read_csv(fn, usecols=["mode"] + KEY, dtype={"wallet": str, "tx": str, "side": str, "outcome": str,
                                                          "mode": str})
    tape["mode"] = tape["mode"].str.lower()
    T = tape[tape["mode"] == "true"].drop(columns="mode").drop_duplicates(KEY)
    A = tape[tape["mode"] == "false"].drop(columns="mode").drop_duplicates(KEY)
    del tape
    # в транзакции ровно одна запись тейкера (лента takerOnly=true); остальные записи транзакции - мейкеры
    tx1 = T.drop_duplicates("tx").set_index("tx")
    is_tk = ((A.wallet.values == A.tx.map(tx1.wallet).values) & (A.side.values == A.tx.map(tx1.side).values)
             & (A.outcome.values == A.tx.map(tx1.outcome).values))
    M = A[~is_tk].copy()
    del A, tx1
    wins = pd.Series(win, dtype=float)
    for d in (T, M):
        d["txi"] = d.tx.str[2:15].map(lambda h: int(h, 16) if isinstance(h, str) and len(h) == 13 else -1)  # 52 бита - точно в float
        d["dir"], up = updir(d.outcome, d.side)
        d["p"] = np.where(up, d.price, 1 - d.price)
        d["won"] = d.w.map(wins)
        d["edge"] = 100 * d["dir"] * (d.won - d.p)
        d["rel"] = d.ts - d.w
        d["usd"] = d.price * d["size"]
    T["fee"] = 100 * 0.07 * T.p * (1 - T.p)
    usd = T.price * T["size"]
    T["round_usd"] = ((usd >= 1) & (np.abs(usd - np.round(usd)) < 0.006)).astype(int)
    # мейкеры: кошелёк тейкера той же транзакции и глубина уровня (ц хуже лучшего уровня этой транзакции для тейкера)
    tw = T.drop_duplicates("tx").set_index("tx")
    M["taker"] = M.tx.map(tw.wallet)
    M["tdir"] = M.tx.map(tw["dir"])
    best = M.assign(q=M.p * M.tdir).groupby("tx").q.transform("min")
    M["depth"] = np.round(100 * (M.p * M.tdir - best), 1)
    # заявки сборщика (мс) + кошелёк
    ev = fm.events(top, tr, bnf, win) if not (tr.empty or top.empty) else pd.DataFrame()
    del top, tr
    if len(ev):
        ev["sd"] = ev.side.astype(str).str[0].str.upper()
        ev["ts_s"] = ev.server_ts / 1000
        Tc = T[(T.rel >= -20) & (T.rel <= 320)].reset_index(drop=True)
        Tc = Tc.assign(o=Tc.outcome.str[0].str.upper(), sd=Tc.side.str[0].str.upper(), ti=np.arange(len(Tc)))
        ev = ev.reset_index(drop=True)
        ev["ei"] = np.arange(len(ev))
        pairs = []
        for w, e in ev.groupby("w"):
            t = Tc[Tc.w == w]
            if t.empty:
                continue
            c = e[["ei", "o", "sd", "size", "price_tok", "ts_s"]].merge(
                t[["ti", "o", "sd", "size", "price", "ts"]].rename(columns={"size": "size_t"}), on=["o", "sd"])
            c["dt"] = c.ts - c.ts_s
            c = c[(c.dt >= -1.5) & (c.dt <= 10) & (np.abs(c.size_t / c["size"] - 1) < 0.01)]
            c = c.assign(pd_=np.abs(c.price - c.price_tok)).sort_values(["pd_", "dt"])
            ue, ut = set(), set()
            for r in c.itertuples(index=False):
                if r.ei in ue or r.ti in ut:
                    continue
                ue.add(r.ei); ut.add(r.ti); pairs.append((r.ei, r.ti, r.dt))
        P = pd.DataFrame(pairs, columns=["ei", "ti", "dt"])
        ev["wallet"] = ev.ei.map(P.set_index("ei").ti.map(Tc.wallet))
        ev["tape_dt"] = ev.ei.map(P.set_index("ei").dt)
        ev["txi"] = ev.ei.map(P.set_index("ei").ti.map(Tc.txi)).fillna(-1).astype("int64")
        print(f"{day}: заявок сборщика {len(ev)}, с кошельком {ev.wallet.notna().mean():.1%}; тейкеров ленты в окне "
              f"{len(Tc)}, сопоставлено {len(P) / max(len(Tc), 1):.1%}", flush=True)
        keep = ["w", "t", "dir", "o", "side", "p", "p_tok", "size", "usd", "levels", "spr0", "dS1", "dS5", "dSf1", "won",
                "spread", "m1", "m5", "m30", "m60", "edge", "fee", "wallet", "tape_dt", "txi", "mid0", "mid1", "mid5", "mid60"]
        ev = ev[keep]
        ev.round(4).to_csv(os.path.join(store, f"ev_{day}.csv.gz"), index=False)
    T[["w", "rel", "wallet", "dir", "p", "size", "usd", "won", "edge", "fee", "round_usd"]].round(4).to_csv(
        os.path.join(store, f"tk_{day}.csv.gz"), index=False)
    M[["w", "rel", "wallet", "dir", "p", "size", "usd", "won", "edge", "taker", "depth", "txi"]].round(4).to_csv(
        os.path.join(store, f"mk_{day}.csv.gz"), index=False)
    # кошелёк x день (без «пыли»: цена Up >= 0,985 или <= 0,015 - добор почти решённого исхода, раздувает оборот)
    dT, dM = (T.p >= 0.985) | (T.p <= 0.015), (M.p >= 0.985) | (M.p <= 0.015)
    print(f"{day}: пыль - тейкеры ${T.usd[dT].sum() / 1e3:.0f} тыс из ${T.usd.sum() / 1e3:.0f} тыс", flush=True)
    T, M = T[~dT].copy(), M[~dM].copy()
    T["xe"] = T["size"] * T.edge
    T["xf"] = T["size"] * T.fee
    M["xe"] = M["size"] * M.edge
    g = T.groupby("wallet").agg(n_tk=("size", "size"), sh_tk=("size", "sum"), usd_tk=("usd", "sum"), xe_tk=("xe", "sum"),
                                xf_tk=("xf", "sum"), n_round=("round_usd", "sum"), win_tk=("w", "nunique"),
                                usd_tk_pre=("usd", lambda v: v[T.loc[v.index, "rel"] < 0].sum()))
    h = M.groupby("wallet").agg(n_mk=("size", "size"), sh_mk=("size", "sum"), usd_mk=("usd", "sum"), xe_mk=("xe", "sum"),
                                win_mk=("w", "nunique"),
                                usd_mk_pre=("usd", lambda v: v[M.loc[v.index, "rel"] < 0].sum()))
    wd = g.join(h, how="outer").fillna(0)
    allw = pd.concat([T[["wallet", "w"]], M[["wallet", "w"]]]).drop_duplicates()
    wd["win"] = allw.groupby("wallet").size()
    if len(ev):
        e = ev.dropna(subset=["wallet"]).copy()
        e["fast"] = (e.dS1 >= 3).astype(int)
        e["slow_against"] = (e.dS1 <= -3).astype(int)
        for c in ("m1", "m5", "m60"):
            e["x" + c] = e["size"] * e[c]
            e["s" + c] = e["size"] * e[c].notna()
        k = e.groupby("wallet").agg(n_ev=("size", "size"), n_fast=("fast", "sum"), n_against=("slow_against", "sum"),
                                    xm1=("xm1", "sum"), sm1=("sm1", "sum"), xm5=("xm5", "sum"), sm5=("sm5", "sum"),
                                    xm60=("xm60", "sum"), sm60=("sm60", "sum"))
        wd = wd.join(k, how="left").fillna(0)
    wd["day"] = day
    wd.reset_index().rename(columns={"index": "wallet"}).round(3).to_csv(os.path.join(store, f"wd_{day}.csv.gz"), index=False)
    print(f"{day}: тейкеров {len(T)}, мейкерских записей {len(M)}, кошельков {len(wd)}, окон с исходом "
          f"{T.dropna(subset=['won']).w.nunique()} из {T.w.nunique()}", flush=True)


# ---------------------------------------------------------------- agg
TIERS = [0, 3, 20, 100, 500, 10 ** 9]
REL = [-700, -300, -120, -63, -30, -15, 0, 30, 60, 120, 180, 240, 270, 300, 400]
SZ = [0, 10, 50, 200, 1000, 1e9]


def lab(edges, fmt=lambda x: f"{x:g}"):
    """подписи корзин с номером, чтобы сортировка совпадала с порядком"""
    return [f"{i:02d}) {fmt(a)}..{fmt(b)}" for i, (a, b) in enumerate(zip(edges[:-1], edges[1:]))]
TNAMES = ["a) 1-3 окна", "b) 4-20", "c) 21-100", "d) 101-500", "e) >500 окон"]


def frames(store, kind):
    for f in sorted(glob.glob(os.path.join(store, f"{kind}_*.csv.gz"))):
        yield pd.read_csv(f, dtype={"wallet": str, "taker": str})


def acc(store, kind, by_fn, metrics, extra_cols=()):
    """Суммы по (срез, окно) для взвешенных средних и кластерной погрешности; читает файлы по дням."""
    return acc_df(frames(store, kind) if isinstance(kind, str) else kind, by_fn, metrics)


def acc_df(it, by_fn, metrics):
    parts = []
    for d in it:
        d = d[(d.p < 0.985) & (d.p > 0.015)]                      # без «пыли»
        d["key"] = by_fn(d)
        d = d.dropna(subset=["key"])
        cols = {"S": d["size"], "U": d["usd"]}
        for m in metrics:
            ok = d[m].notna()
            cols["s_" + m] = d["size"] * ok
            cols["x_" + m] = d["size"] * d[m].fillna(0)
        x = pd.DataFrame(cols)
        x["key"], x["w"] = d["key"].astype(str), d.w
        x["n"] = 1
        parts.append(x.groupby(["key", "w"]).sum())
    if not parts:
        return pd.DataFrame()
    return pd.concat(parts).groupby(level=[0, 1]).sum()


def report(a, metrics, title, se_for=("edge",)):
    rows = []
    for k, g in a.groupby(level=0):
        r = {"срез": k, "записей": int(g.n.sum()), "окон": len(g), "шейров_тыс": round(g.S.sum() / 1e3, 1),
             "$тыс": round(g.U.sum() / 1e3, 1)}
        for m in metrics:
            s = g["s_" + m].sum()
            mu = g["x_" + m].sum() / s if s > 0 else np.nan
            r[m] = round(mu, 2)
            if m in se_for and s > 0:
                r[m + "_se"] = round(np.sqrt(((g["x_" + m] - mu * g["s_" + m]) ** 2).sum()) / s, 2)
                r[m + "_$тыс"] = round(g["x_" + m].sum() / 100 / 1e3, 1)
        rows.append(r)
    t = pd.DataFrame(rows)
    print(f"\n=== {title} ===\n{t.to_string(index=False)}", flush=True)
    return t


def agg(store, out):
    wd = pd.concat([pd.read_csv(f, dtype={"wallet": str}) for f in sorted(glob.glob(os.path.join(store, "wd_*.csv.gz")))])
    days = wd.day.nunique()
    W = wd.drop(columns="day").groupby("wallet").sum()
    W["days"] = wd.groupby("wallet").day.nunique()
    W["usd"] = W.usd_tk + W.usd_mk
    W["maker_share"] = W.usd_mk / W.usd.where(W.usd > 0)
    W["tk_edge"] = W.xe_tk / W.sh_tk.where(W.sh_tk > 0)
    W["tk_net"] = (W.xe_tk - W.xf_tk) / W.sh_tk.where(W.sh_tk > 0)
    W["mk_edge"] = W.xe_mk / W.sh_mk.where(W.sh_mk > 0)
    W["pnl_tk"] = (W.xe_tk - W.xf_tk) / 100
    W["pnl_mk"] = W.xe_mk / 100
    W["pnl"] = W.pnl_tk + W.pnl_mk
    W["round_share"] = W.n_round / W.n_tk.where(W.n_tk > 0)
    if "n_ev" in W:
        W["fast_share"] = W.n_fast / W.n_ev.where(W.n_ev > 0)
        W["m1"] = W.xm1 / W.sm1.where(W.sm1 > 0)
        W["m5"] = W.xm5 / W.sm5.where(W.sm5 > 0)
        W["m60"] = W.xm60 / W.sm60.where(W.sm60 > 0)
    W["tier"] = pd.cut(W.win, TIERS, labels=TNAMES)
    W["role"] = pd.cut(W.maker_share.fillna(0), [-0.01, 0.2, 0.8, 1.0], labels=["тейкер", "смешанный", "мейкер"])
    W.to_csv(os.path.join(store, "wallets_all.csv.gz"))
    print(f"дней {days}, кошельков {len(W)}, оборот ${W.usd.sum() / 1e6:.1f} млн (тейкеры ${W.usd_tk.sum() / 1e6:.1f} млн)")
    # ярусы активности
    rows = []
    for (t, r), g in W.groupby(["tier", "role"], observed=True):
        rows.append(dict(ярус=t, роль=r, кошельков=len(g), оборот_тейкер_тыс=round(g.usd_tk.sum() / 1e3, 1),
                         оборот_мейкер_тыс=round(g.usd_mk.sum() / 1e3, 1),
                         тейкер_ц_до_комиссии=round(g.xe_tk.sum() / max(g.sh_tk.sum(), 1), 2),
                         тейкер_ц_после=round((g.xe_tk.sum() - g.xf_tk.sum()) / max(g.sh_tk.sum(), 1), 2),
                         мейкер_ц=round(g.xe_mk.sum() / max(g.sh_mk.sum(), 1), 2),
                         pnl_тыс=round(g.pnl.sum() / 1e3, 1), в_плюсе=f"{(g.pnl > 0).mean():.0%}",
                         доля_круглых_usd=round(g.n_round.sum() / max(g.n_tk.sum(), 1), 2),
                         быстрых=round(g.n_fast.sum() / max(g.n_ev.sum(), 1), 3) if "n_ev" in g else np.nan,
                         m1=round(g.xm1.sum() / max(g.sm1.sum(), 1), 2) if "xm1" in g else np.nan))
    print("\n=== кошельки по ярусу активности (окон за период) и роли (доля мейкерского оборота) ===")
    print(pd.DataFrame(rows).to_string(index=False))
    # крупнейшие кошельки
    cols = ["win", "days", "usd_tk", "usd_mk", "maker_share", "tk_edge", "tk_net", "mk_edge", "pnl", "round_share",
            "fast_share", "m1", "m5", "m60", "n_ev"]
    cols = [c for c in cols if c in W]
    top = W.sort_values("usd", ascending=False).head(60)[cols].round(3)
    top.index = [x[:10] for x in top.index]
    print("\n=== 60 крупнейших кошельков по обороту ===\n" + top.to_string())
    for nm, s in (("в плюсе", W.sort_values("pnl", ascending=False).head(30)),
                  ("в минусе", W.sort_values("pnl").head(30))):
        x = s[cols].round(3); x.index = [i[:10] for i in x.index]
        print(f"\n=== 30 кошельков с наибольшим результатом ({nm}) ===\n" + x.to_string())
    W[(W.win >= 20) | (W.usd >= 2000)].reset_index()[["wallet"] + cols + ["pnl_tk", "pnl_mk", "tier", "role", "n_tk",
        "n_mk", "usd_tk_pre", "usd_mk_pre"]].round(4).pipe(lambda x: save_parts(x, os.path.join(out, "wallets")))
    # кто кому платит: мейкерские записи (ярус, роль мейкера) x (ярус, роль тейкера)
    cls = (W.tier.astype(str) + " / " + W.role.astype(str)).to_dict()
    tier = W.tier.astype(str).to_dict()
    a = acc(store, "mk", lambda d: d.wallet.map(tier) + "  <-  " + d.taker.map(tier), ["edge"])
    t1 = report(a, ["edge"], "мейкер (ярус) <- тейкер (ярус): результат мейкера по исходу, ц/шейр и $")
    role = W.role.astype(str).to_dict()
    a = acc(store, "mk", lambda d: d.wallet.map(role) + "  <-  " + d.taker.map(cls), ["edge"])
    report(a, ["edge"], "мейкер (роль) <- тейкер (ярус / роль)")
    # мейкеры: время и глубина
    a = acc(store, "mk", lambda d: pd.cut(d.rel, REL, labels=lab(REL)),
            ["edge"])
    report(a, ["edge"], "все мейкерские исполнения по времени ленты (rel = время ленты - старт; лента позже на ~2 с)")
    a = acc(store, "mk", lambda d: pd.cut(d.depth, [-0.1, 0.5, 1.5, 3.5, 6.5, 100], labels=["0) лучший", "1) 1 ц", "2) 2-3 ц", "3) 4-6 ц", "4) 7+ ц"]), ["edge"])
    report(a, ["edge"], "мейкеры по глубине уровня в транзакции (ц от лучшего)")
    # тейкеры (вся лента, с T-600): ярус и время
    a = acc(store, "tk", lambda d: d.wallet.map(cls), ["edge", "fee"])
    report(a, ["edge", "fee"], "тейкеры по ярусу / роли кошелька: результат по исходу до комиссии, комиссия")
    a = acc(store, "tk", lambda d: pd.cut(d.rel, REL, labels=lab(REL)),
            ["edge", "fee"])
    report(a, ["edge", "fee"], "тейкеры по времени ленты")
    a = acc(store, "tk", lambda d: pd.cut(d["size"], SZ, labels=lab(SZ)).astype(str) + " | " +
            d.round_usd.map({0: "не круглые $", 1: "круглые $"}), ["edge", "fee"])
    report(a, ["edge", "fee"], "тейкеры по размеру и «круглой сумме» (заявка на $N через интерфейс)")
    # заявки сборщика (мс): ярус тейкера x ход BTC до сделки, маркауты
    mt = ["spread", "m1", "m5", "m30", "m60", "edge", "fee"]
    a = acc(store, "ev", lambda d: d.wallet.map(cls), mt)
    report(a, mt, "внутри окна (мс): ярус / роль тейкера")
    btc = lambda d: pd.cut(d.dS1, [-1e9, -10, -3, -0.5, 0.5, 3, 10, 1e9],
                           labels=["0) < -10", "1) -10..-3", "2) -3..-0,5", "3) ≈0", "4) 0,5..3", "5) 3..10", "6) > 10"]).astype(str)
    a = acc(store, "ev", btc, mt)
    report(a, mt, "внутри окна: ход фьючерса BTC за 1 с до сделки в сторону тейкера, $")
    a = acc(store, "ev", lambda d: d.wallet.map(tier).astype(str) + " | BTC " + btc(d), mt)
    report(a, mt, "внутри окна: ярус тейкера x ход BTC")
    a = acc(store, "ev", lambda d: pd.cut(d.t, [-20, 0, 30, 60, 120, 180, 240, 270, 290, 310], labels=lab([-20, 0, 30, 60, 120, 180, 240, 270, 290, 310])).astype(str), mt)
    report(a, mt, "внутри окна: время")
    a = acc(store, "ev", lambda d: pd.cut(d.p_tok, [0, 0.1, 0.25, 0.4, 0.6, 0.75, 0.9, 1], labels=lab([0, 0.1, 0.25, 0.4, 0.6, 0.75, 0.9, 1])).astype(str) + " | " +
            np.where(d.side.astype(str).str.upper().str.startswith("B"), "купил", "продал"), mt)
    report(a, mt, "внутри окна: цена токена и сторона тейкера")
    a = acc(store, "ev", lambda d: pd.cut(d["size"], SZ, labels=lab(SZ)).astype(str), mt)
    report(a, mt, "внутри окна: размер заявки, шейров")
    a = acc(store, "ev", lambda d: d.w.map(lambda w: pd.Timestamp(w, unit="s").strftime("%m-%d")), mt)
    report(a, mt, "внутри окна: по дням")


# ---------------------------------------------------------------- agg2: где именно зарабатывают мейкеры
TB = [-700, -63, -15, 0, 60, 240, 300, 400]
TBL = ["0) до T-63", "1) T-63..-15", "2) T-15..0", "3) 0..60", "4) 60..240", "5) 240..300", "6) после"]
DB = [-0.1, 0.5, 1.5, 3.5, 6.5, 100]
DBL = ["0) лучший", "1) 1 ц", "2) 2-3 ц", "3) 4-6 ц", "4) 7+ ц"]


def mk_ev(store):
    """мейкерские записи + мс-заявка тейкера той же транзакции (ход BTC, mid через 1/5/60 с)"""
    for f in sorted(glob.glob(os.path.join(store, "mk_*.csv.gz"))):
        day = os.path.basename(f)[3:-7]
        m = pd.read_csv(f, dtype={"wallet": str, "taker": str})
        fe = os.path.join(store, f"ev_{day}.csv.gz")
        if os.path.exists(fe):
            e = pd.read_csv(fe, usecols=["txi", "t", "dS1", "dS5", "mid0", "mid1", "mid5", "mid60", "levels", "size"])
            e = e[e.txi >= 0].drop_duplicates("txi").rename(columns={"size": "tsize"})
            m = m.merge(e, on="txi", how="left")
            for h in (0, 1, 5, 60):
                m[f"k{h}"] = 100 * m["dir"] * (m[f"mid{h}"] - m.p)     # маркаут мейкера к mid через h с
        yield m


def agg2(store, out):
    W = pd.read_csv(os.path.join(store, "wallets_all.csv.gz"), index_col=0, dtype={"tier": str, "role": str})
    tier, role = W.tier.astype(str).to_dict(), W.role.astype(str).to_dict()
    tb = lambda d: pd.cut(d.rel, TB, labels=TBL).astype(str)
    db = lambda d: pd.cut(d.depth, DB, labels=DBL).astype(str)
    a = acc(store, "mk", lambda d: tb(d) + " | " + db(d), ["edge"])
    report(a, ["edge"], "мейкеры: время ленты x глубина уровня (ц от лучшего уровня транзакции)")
    a = acc(store, "mk", lambda d: db(d) + " | тейкер " + d.taker.map(tier).astype(str), ["edge"])
    report(a, ["edge"], "мейкеры: глубина x ярус тейкера")
    a = acc(store, "mk", lambda d: d.wallet.map(tier).astype(str) + " | " + db(d), ["edge"])
    report(a, ["edge"], "мейкеры: ярус мейкера x глубина")
    btc = lambda d: pd.cut(d.dS1, [-1e9, -10, -3, 3, 10, 1e9],                # dS1 уже со знаком тейкера
                           labels=["0) < -10", "1) -10..-3", "2) спокойно", "3) 3..10", "4) > 10"]).astype(str)
    calm = lambda d: np.where((d.dS1.abs() < 3) & (d.dS5.abs() < 10), "спокойно", "ход BTC")
    mt = ["edge", "k0", "k1", "k5", "k60"]
    a = acc(store, mk_ev(store), lambda d: ("BTC за 1 с в сторону тейкера " + btc(d)).where(d.dS1.notna()), mt)
    report(a, mt, "мейкеры внутри окна: ход BTC до сделки (в сторону тейкера); k = маркаут мейкера к mid через N с",
           se_for=("edge", "k60"))
    a = acc(store, mk_ev(store), lambda d: (pd.Series(calm(d), index=d.index) + " | " + db(d)).where(d.dS1.notna()), mt)
    report(a, mt, "мейкеры внутри окна: BTC спокоен (|за 1 с| < 3 и |за 5 с| < 10) или нет x глубина", se_for=("edge", "k60"))
    a = acc(store, mk_ev(store), lambda d: (pd.cut(d.tsize, [0, 10, 50, 200, 1000, 1e9], labels=lab(SZ)).astype(str) + " | "
                                           + pd.Series(calm(d), index=d.index)).where(d.dS1.notna()), mt)
    report(a, mt, "мейкеры внутри окна: размер заявки тейкера x BTC", se_for=("edge", "k60"))
    # кто когда торгует: доля оборота тейкеров по ярусам во времени
    rows = []
    for d in frames(store, "tk"):
        d = d[(d.p < 0.985) & (d.p > 0.015)]
        d = d.assign(tb=tb(d), tr=d.wallet.map(tier).astype(str), xe=d["size"] * d.edge)
        rows.append(d.groupby(["tb", "tr"]).agg(usd=("usd", "sum"), sh=("size", "sum"), xe=("xe", "sum")))
    g = pd.concat(rows).groupby(level=[0, 1]).sum()
    share = (g.usd / g.usd.groupby(level=0).transform("sum")).unstack().round(3)
    print("\n=== доля оборота тейкеров по ярусу кошелька во времени окна ===\n" + share.to_string())
    print("\n=== результат тейкеров по исходу (ц/шейр) по ярусу во времени ===\n" +
          (g.xe / g.sh).unstack().round(2).to_string())
    print("\n=== оборот тейкеров, $ тыс в сутки ===\n" + (g.usd.unstack() / 1e3 / 12).round(1).to_string())
    # профили мейкеров: 15 лучших по мейкерскому результату + 10 крупнейших по мейкерскому обороту
    sel = list(W.sort_values("pnl_mk", ascending=False).head(15).index) + \
        list(W.sort_values("usd_mk", ascending=False).head(10).index) + \
        list(W.sort_values("pnl_mk").head(5).index)
    sel = list(dict.fromkeys(sel))
    prof = []
    for d in mk_ev(store):
        d = d[d.wallet.isin(sel) & (d.p < 0.985) & (d.p > 0.015)]
        d = d.assign(db=db(d), tb=tb(d), xe=d["size"] * d.edge, x5=d["size"] * d.k5.fillna(0), s5=d["size"] * d.k5.notna(),
                     am=d.taker.map(tier).astype(str).str[:1].isin(["a", "b", "c"]) * d["size"],
                     calm=(pd.Series(calm(d), index=d.index) == "спокойно") * d["size"] * d.dS1.notna(),
                     sev=d["size"] * d.dS1.notna())
        prof.append(d.groupby(["wallet", "db"]).agg(sh=("size", "sum"), xe=("xe", "sum")).assign(kind="d"))
        prof.append(d.groupby(["wallet", "tb"]).agg(sh=("size", "sum"), xe=("xe", "sum")).rename_axis(["wallet", "db"])
                    .assign(kind="t"))
        prof.append(d.groupby("wallet").agg(sh=("size", "sum"), xe=("xe", "sum"), x5=("x5", "sum"), s5=("s5", "sum"),
                                            am=("am", "sum"), calm=("calm", "sum"), sev=("sev", "sum"), n=("size", "size"),
                                            w=("w", "nunique"))
                    .assign(db="все", kind="a").set_index("db", append=True))
    P = pd.concat(prof).groupby(level=[0, 1]).sum(numeric_only=True)
    rows = []
    for wl in sel:
        if wl not in P.index.get_level_values(0):
            continue
        p = P.loc[wl]
        tot = p.loc["все"]
        r = dict(кошелёк=wl[:10], окон=int(W.loc[wl, "win"]), мейкер_тыс=round(W.loc[wl, "usd_mk"] / 1e3),
                 доля_мейкер=round(W.loc[wl, "maker_share"], 2), pnl_мейкер=round(W.loc[wl, "pnl_mk"]),
                 pnl_тейкер=round(W.loc[wl, "pnl_tk"]), ц_шейр=round(tot.xe / tot.sh, 2),
                 маркаут5с=round(tot.x5 / tot.s5, 2) if tot.s5 > 0 else np.nan,
                 ср_размер=round(tot.sh / tot.n, 1), от_любителей=round(tot.am / tot.sh, 2),
                 при_спокойном_BTC=round(tot.calm / tot.sev, 2) if tot.sev > 0 else np.nan)
        for lb in DBL:
            r["гл" + lb[:1]] = round(p.sh.get(lb, 0) / tot.sh, 2)
        for lb in TBL[:6]:
            r["вр" + lb[:1]] = round(p.sh.get(lb, 0) / tot.sh, 2)
        r["ц_гл0"] = round(p.xe.get(DBL[0], np.nan) / p.sh.get(DBL[0], np.nan), 2) if p.sh.get(DBL[0], 0) else np.nan
        r["ц_гл2+"] = round(sum(p.xe.get(x, 0) for x in DBL[2:]) / max(sum(p.sh.get(x, 0) for x in DBL[2:]), 1), 2)
        rows.append(r)
    print("\n=== профили мейкеров (гл0..4 - доля шейров по глубине: лучший, 1 ц, 2-3, 4-6, 7+; вр0..5 - по времени: "
          "до T-63, T-63..-15, -15..0, 0..60, 60..240, 240..300; от_любителей - доля шейров против тейкеров с 1-100 окнами) ===")
    print(pd.DataFrame(rows).to_string(index=False))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["prep", "agg", "agg2", "daily"])
    ap.add_argument("root", nargs="?")
    ap.add_argument("--tapes", default=os.path.expanduser("~/tapes"))
    ap.add_argument("--store", default=os.path.expanduser("~/flow"))
    ap.add_argument("--out", default=".")
    a = ap.parse_args()
    os.makedirs(a.store, exist_ok=True)
    os.makedirs(a.out, exist_ok=True)
    if a.cmd == "prep":
        prep(a.root, a.tapes, a.store)
    elif a.cmd == "agg":
        agg(a.store, a.out)
    elif a.cmd == "agg2":
        agg2(a.store, a.out)
    else:
        daily(a.store, a.out)



# ---------------------------------------------------------------- daily: устойчивость главных выводов по дням
def daily(store, out):
    W = pd.read_csv(os.path.join(store, "wallets_all.csv.gz"), index_col=0, dtype={"tier": str, "role": str})
    tier = W.tier.astype(str).str[:1].to_dict()
    rows = []
    for m in mk_ev(store):
        m = m[(m.p < 0.985) & (m.p > 0.015)]
        day = pd.to_datetime(m.w.min(), unit="s").strftime("%m-%d")
        mt, tt = m.wallet.map(tier), m.taker.map(tier)
        calm = (m.dS1.abs() < 3) & (m.dS5.abs() < 10)
        sets = {
            "мейкеры глубина 2+ ц": m.depth >= 1.5,
            "мейкеры глубина 1 ц": (m.depth >= 0.5) & (m.depth < 1.5),
            "мейкеры лучший уровень": m.depth < 0.5,
            "мейкеры T-63..-15 глубина 1+": (m.rel > -63) & (m.rel <= -15) & (m.depth >= 0.5),
            "мейкеры лучший, BTC спокоен": (m.depth < 0.5) & calm & m.dS1.notna(),
            "мейкеры против хода BTC (тейкер против)": m.dS1 <= -3,
            "мейкеры по ходу BTC (тейкер по ходу)": m.dS1 >= 3,
            "крупные мейкеры (e) <- тейкеры a-d": (mt == "e") & tt.isin(["a", "b", "c", "d"]),
            "крупные мейкеры (e) <- тейкеры e": (mt == "e") & (tt == "e"),
            "все мейкеры <- тейкеры a-b": tt.isin(["a", "b"]),
        }
        for k, msk in sets.items():
            f = m[msk]
            if len(f):
                rows.append(dict(day=day, срез=k, sh=f["size"].sum(), xe=(f["size"] * f.edge).sum(),
                                 x60=(f["size"] * f.k60.fillna(0)).sum(), s60=(f["size"] * f.k60.notna()).sum()))
    d = pd.DataFrame(rows)
    d["ц"] = d.xe / d.sh
    piv = d.pivot(index="срез", columns="day", values="ц").round(2)
    tot = d.groupby("срез").agg(sh=("sh", "sum"), xe=("xe", "sum"), x60=("x60", "sum"), s60=("s60", "sum"))
    piv["всего_ц"] = (tot.xe / tot.sh).round(2)
    piv["маркаут60_ц"] = (tot.x60 / tot.s60).round(2)
    piv["дней_в_плюсе"] = (d.pivot(index="срез", columns="day", values="ц") > 0).sum(axis=1).astype(str) + "/" + \
        d.pivot(index="срез", columns="day", values="ц").notna().sum(axis=1).astype(str)
    piv["$тыс_в_сутки"] = (tot.xe / 100 / 1e3 / d.day.nunique()).round(1)
    pd.set_option("display.width", 300)
    print("=== результат мейкеров по исходу, ц/шейр, по дням ===\n" + piv.to_string())
    rows = []
    for t in frames(store, "tk"):
        t = t[(t.p < 0.985) & (t.p > 0.015)]
        day = pd.to_datetime(t.w.min(), unit="s").strftime("%m-%d")
        tr = t.wallet.map(tier)
        for k in "abcde":
            f = t[tr == k]
            rows.append(dict(day=day, ярус=k, ц=(f["size"] * f.edge).sum() / f["size"].sum()))
    print("\n=== тейкеры по ярусу (a 1-3 окна ... e >500), ц/шейр до комиссии, по дням ===\n" +
          pd.DataFrame(rows).pivot(index="ярус", columns="day", values="ц").round(2).to_string())


if __name__ == "__main__":
    main()
