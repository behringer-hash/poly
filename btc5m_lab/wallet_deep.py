"""Все исполнения одного кошелька за дни записи сборщика с миллисекундным контекстом + контрольная выборка чужих тейкеров.

    python wallet_deep.py 0x3048... --flow ~/flow --raw DATA_DIR ~/archive_data --out OUT [--ctrl 0.03]

Источник исполнений - хранилище flow_wallets.py (~/flow): ev_ (заявки тейкеров сборщика с кошельком, мс),
mk_ (мейкерские записи ленты, связаны с заявкой тейкера по txi), tk_ (все тейкеры ленты, с T-600, секунды).
Роли: T - его тейкерская заявка (время сервера); M - его мейкерское исполнение (время сервера заявки тейкера, который
его исполнил); P - его тейкерская запись ленты без мс-заявки (до T-15 или не сопоставлена; время ленты - 2,2 с).
Всё в терминах Up: dir +1 - купил Up / продал Down; p - цена Up.
Контекст (по сырым данным дня; если сырых нет - пусто):
  книга Up на сервере: mid в моменты -1000..+60000 мс, bid/ask/объёмы в -250, -1, +250 мс;
  глубина его токена (последний снимок pm_depth): объём bid/ask в пределах 2 и 5 ц от лучших;
  BTC: фьючерс Binance (bnf), спот Binance (bn), Bybit (by), Coinbase (cb), Chainlink (cl) - изменение цены, $,
       от момента сделки к сдвигам -5000..+5000 мс (знак: в сторону его dir); задержка от последнего хода >= 1 / 3 $
       за 300 мс в его сторону (bnf, by, cb), мс;
  поток: чистый объём других тейкеров в сторону Up за 1 и 5 с до сделки (шейров);
  позиция до исполнения: шейров Up / Down, затраты.
Выход: wfill_<день>.csv.gz, wctrl_<день>.csv.gz (контроль - доля --ctrl чужих заявок сборщика с тем же контекстом).
"""
from __future__ import annotations

import argparse
import glob
import os

import numpy as np
import pandas as pd

from jump_study import save_parts
from lead_lag import read

MIDS = [-5000, -2000, -1000, -500, -250, -100, -1, 100, 250, 500, 1000, 2000, 5000, 10000, 30000, 60000]
BOFF = [-5000, -2000, -1000, -500, -300, -200, -100, 100, 200, 500, 1000, 2000, 5000]


def raw_root(day, raws):
    for r in raws:
        p = os.path.join(r, day)
        if os.path.isdir(p) and glob.glob(os.path.join(p, "pm_top_*")):
            return p
    return None


def series(d, tcol, pcol="price"):
    d = d.dropna(subset=[tcol, pcol]).sort_values(tcol, kind="stable")
    return d[tcol].values.astype(float), d[pcol].values.astype(float)


def at(tt, vv, t):
    i = np.searchsorted(tt, t, side="right") - 1
    out = np.full(len(t), np.nan)
    ok = i >= 0
    out[ok] = vv[i[ok]]
    return out


def last_move_lag(tt, pp, t, sgn, thr, back=3000, W=300):
    """мс от последней сделки источника (за back мс до t), где цена сдвинулась >= thr $ за W мс в сторону sgn."""
    out = np.full(len(t), np.nan)
    if len(tt) < 10:
        return out
    j = np.searchsorted(tt, tt - W, side="right") - 1
    mv = pp - pp[np.maximum(j, 0)]
    up = np.flatnonzero(mv >= thr)
    dn = np.flatnonzero(mv <= -thr)
    for k in range(len(t)):
        idx = up if sgn[k] > 0 else dn
        i = np.searchsorted(tt[idx], t[k], side="right") - 1
        if i >= 0 and t[k] - tt[idx[i]] <= back:
            out[k] = t[k] - tt[idx[i]]
    return out


def context(F, root):
    """F: w, ts (мс сервера), dir, o (U/D - его токен). Добавляет столбцы контекста."""
    t = F.ts.values.astype(float)
    top = read(root, "pm_top", ["recv_ms", "d", "w", "o", "bid", "ask", "bid_sz", "ask_sz"])
    top = top[top.o == "U"]
    top = top.assign(srv=top.recv_ms - top.d)
    cols = {}
    for k in (f"mid{x}" for x in MIDS):
        cols[k] = np.full(len(F), np.nan)
    for k in ("bid", "ask", "bsz", "asz"):
        for x in (-250, -1, 250):
            cols[f"{k}{x}"] = np.full(len(F), np.nan)
    for w, idx in F.groupby("w").indices.items():
        b = top[top.w == w].sort_values("srv", kind="stable")
        if len(b) < 5:
            continue
        ts = b.srv.values.astype(float)
        bid, ask = b.bid.values.astype(float), b.ask.values.astype(float)
        mid = np.where(np.isnan(ask), bid, np.where(np.isnan(bid), ask, (bid + ask) / 2))
        tw = t[idx]
        for x in MIDS:
            j = np.searchsorted(ts, tw + x, side="right") - 1
            ok = (j >= 0) & (tw + x <= ts[-1] + 1)
            cols[f"mid{x}"][idx] = np.where(ok, mid[np.maximum(j, 0)], np.nan)
        for x in (-250, -1, 250):
            j = np.searchsorted(ts, tw + x, side="right") - 1
            ok = j >= 0
            jj = np.maximum(j, 0)
            cols[f"bid{x}"][idx] = np.where(ok, bid[jj], np.nan)
            cols[f"ask{x}"][idx] = np.where(ok, ask[jj], np.nan)
            cols[f"bsz{x}"][idx] = np.where(ok, b.bid_sz.values[jj], np.nan)
            cols[f"asz{x}"][idx] = np.where(ok, b.ask_sz.values[jj], np.nan)
    del top
    # глубина его токена
    dep = read(root, "pm_depth")
    for k in ("bv2", "bv5", "av2", "av5"):
        cols[k] = np.full(len(F), np.nan)
    if not dep.empty:
        dep["o"] = dep.o.astype(str).str[0]
        for (w, o), idx in F.groupby(["w", "o"]).indices.items():
            g = dep[(dep.w == w) & (dep.o == o)].sort_values("ts_ms", kind="stable")
            if g.empty:
                continue
            j = np.searchsorted(g.ts_ms.values - 20.0, t[idx], side="right") - 1
            ok = j >= 0
            B = g[[f"b{i}" for i in range(1, 6)]].values.astype(float)
            BS = g[[f"bs{i}" for i in range(1, 6)]].values.astype(float)
            A = g[[f"a{i}" for i in range(1, 6)]].values.astype(float)
            AS = g[[f"as{i}" for i in range(1, 6)]].values.astype(float)
            jj = np.maximum(j, 0)
            for lim, nm in ((0.021, "2"), (0.051, "5")):
                bv = np.nansum(np.where(B[jj] >= B[jj][:, :1] - lim, BS[jj], 0), axis=1)
                av = np.nansum(np.where(A[jj] <= A[jj][:, :1] + lim, AS[jj], 0), axis=1)
                cols["bv" + nm][idx] = np.where(ok, bv, np.nan)
                cols["av" + nm][idx] = np.where(ok, av, np.nan)
    del dep
    # BTC
    sgn = F["dir"].values.astype(float)
    srcs = {}
    d = read(root, "bnf_agg", ["T", "price"]); srcs["bnf"] = series(d, "T") if not d.empty else None
    d = read(root, "bn_agg", ["T", "price"]); srcs["bn"] = series(d, "T") if not d.empty else None
    d = read(root, "by_trade", ["T", "price"]); srcs["by"] = series(d, "T") if not d.empty else None
    d = read(root, "cb_ticker", ["t_ms", "price"]); srcs["cb"] = series(d, "t_ms") if not d.empty else None
    d = read(root, "rtds", ["feed", "ts_ms", "value"])
    srcs["cl"] = series(d[d.feed == "cl"], "ts_ms", "value") if not d.empty else None
    del d
    for nm, s in srcs.items():
        for x in BOFF:
            cols[f"{nm}{x}"] = np.full(len(F), np.nan)
        if s is None or len(s[0]) < 10:
            continue
        tt, pp = s
        p0 = at(tt, pp, t)
        for x in BOFF:
            cols[f"{nm}{x}"] = np.round(sgn * (at(tt, pp, t + x) - p0), 2) * (1 if x > 0 else -1)
        if nm in ("bnf", "by", "cb"):
            for thr in (1, 3):
                cols[f"lag_{nm}{thr}"] = last_move_lag(tt, pp, t, sgn, thr)
    # поток других тейкеров (pm_trades: сторона тейкера)
    tr = read(root, "pm_trades", ["server_ts", "w", "o", "side", "price", "size"])
    tr = tr.dropna(subset=["server_ts", "size"])
    up = tr.o.astype(str).str.upper().str.startswith("U")
    buy = tr.side.astype(str).str.upper().str.startswith("B")
    tr["sv"] = np.where(up == buy, 1, -1) * tr["size"]
    tr = tr.sort_values("server_ts", kind="stable")
    tt, cs = tr.server_ts.values.astype(float), np.cumsum(tr.sv.values)
    def vol(a, b):
        i, j = np.searchsorted(tt, a, "left") - 1, np.searchsorted(tt, b, "left") - 1
        return np.where(j >= 0, cs[np.maximum(j, 0)], 0) - np.where(i >= 0, cs[np.maximum(i, 0)], 0)
    cols["flow1"] = sgn * vol(t - 1000, t - 1)
    cols["flow5"] = sgn * vol(t - 5000, t - 1)
    cols["flowp1"] = sgn * vol(t + 1, t + 1000)
    return pd.concat([F.reset_index(drop=True), pd.DataFrame(cols)], axis=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("wallet")
    ap.add_argument("--flow", default=os.path.expanduser("~/flow"))
    ap.add_argument("--raw", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ctrl", type=float, default=0.03)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    W = a.wallet.lower()
    tiers = pd.read_csv(os.path.join(a.flow, "wallets_all.csv.gz"), usecols=["wallet", "tier", "role", "win"])
    tier = dict(zip(tiers.wallet.str.lower(), tiers.tier.astype(str).str[:1]))
    rng = np.random.default_rng(1)
    for fe in sorted(glob.glob(os.path.join(a.flow, "ev_*.csv.gz"))):
        day = os.path.basename(fe)[3:-7]
        ev = pd.read_csv(fe, dtype={"wallet": str})
        ev["wallet"] = ev.wallet.str.lower()
        ev["ts"] = np.round((ev.w + ev.t) * 1000)
        mk = pd.read_csv(os.path.join(a.flow, f"mk_{day}.csv.gz"), dtype={"wallet": str, "taker": str})
        mk["wallet"] = mk.wallet.str.lower()
        tk = pd.read_csv(os.path.join(a.flow, f"tk_{day}.csv.gz"), dtype={"wallet": str})
        tk["wallet"] = tk.wallet.str.lower()
        # его тейкерские заявки (мс)
        T = ev[ev.wallet == W].copy()
        T["role"] = "T"
        T["o"] = T.o.astype(str).str[0]
        # его мейкерские исполнения: время и признаки заявки тейкера
        M = mk[mk.wallet == W].merge(ev[ev.txi >= 0][["txi", "ts", "t", "levels", "size", "wallet", "dS1"]]
                                     .rename(columns={"size": "tsize", "wallet": "twallet", "dS1": "tdS1"}),
                                     on="txi", how="left")
        M["role"] = "M"
        M["o"] = np.where(M["dir"] > 0, "U", "D")              # мейкер всегда покупает (проверим по доле)
        M["ttier"] = M.taker.str.lower().map(tier)
        # тейкерские записи ленты без мс-заявки (до T-15 и несопоставленные)
        P = tk[tk.wallet == W].copy()
        if len(T):
            key = set(zip(T.w, np.round(T["size"], 2), np.round(T.p, 3)))
            P = P[[k not in key for k in zip(P.w, np.round(P["size"], 2), np.round(P.p, 3))]]
        P["role"] = "P"
        P["ts"] = np.round((P.w + P.rel - 2.2) * 1000)
        P["o"] = np.where(P["dir"] > 0, "U", "D")
        F = pd.concat([T, M, P], ignore_index=True, sort=False)
        F["ms"] = (F.role != "P") & F.ts.notna()               # время сервера с мс (иначе - по ленте)
        F["ts"] = F.ts.where(F.ts.notna(), np.round((F.w + F.rel - 2.2) * 1000))
        F = F.sort_values(["w", "ts"], kind="stable").reset_index(drop=True)
        # позиция до исполнения (по всем ролям), шейры и затраты в терминах токена
        F["shU"] = np.where(F["dir"] > 0, F["size"], 0.0)
        F["shD"] = np.where(F["dir"] < 0, F["size"], 0.0)
        F["cU"] = F.shU * F.p
        F["cD"] = F.shD * (1 - F.p)
        for c in ("shU", "shD", "cU", "cD"):
            F["pos_" + c] = F.groupby("w")[c].cumsum() - F[c]
        root = raw_root(day, a.raw)
        C = ev[(ev.wallet != W) & (rng.random(len(ev)) < a.ctrl)].copy()
        C["o"] = C.o.astype(str).str[0]
        C["tier"] = C.wallet.map(tier)
        if root:
            F = context(F, root)
            C = context(C, root)
        keep_drop = [c for c in ("txi", "mid0", "mid1", "mid5", "mid60") if c in F]
        save_parts(F.drop(columns=keep_drop).round(4), os.path.join(a.out, f"wfill_{day}"))
        save_parts(C.drop(columns=[c for c in ("txi",) if c in C]).round(4), os.path.join(a.out, f"wctrl_{day}"))
        print(f"{day}: сырые {'есть' if root else 'НЕТ'}; его тейкерских заявок {len(T)}, мейкерских {len(M)} "
              f"(с мс {M.ts.notna().mean():.0%}), только лента {len(P)}; контроль {len(C)}", flush=True)


if __name__ == "__main__":
    main()
