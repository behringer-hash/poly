"""Выгрузка окон целиком для поштучного разбора торговли кошелька (книга, поток заявок с кошельками, BTC, Chainlink).

    python window_export.py DATA_DIR/2026-10-29 [...] --wallet 0x... --wfrom W --wto W --out OUT

Для каждого окна [wfrom, wto): лента data-api (takerOnly true/false) -> кошельки тейкеров и мейкеров; заявки тейкеров
сборщика (flow_map.events, мс) сопоставлены с лентой. Выход (все с колонкой w):
  ex_win.csv      окно: цена к старту (TWAP60 и Chainlink), победитель
  ex_top          верх книги Up на сервере: srv, bid, ask, bid_sz, ask_sz (Down: bid = 1 - ask Up)
  ex_dep          снимки 5 уровней обеих сторон (pm_depth)
  ex_ev           заявки тейкеров: server_ts, dir (+1 Up), o, side, p (цена Up), size, levels, кошелёк (10 знаков)
  ex_his          исполнения кошелька: роль T (тейкер, мс) / M (мейкер, время заявки тейкера) / P (только лента),
                  токен, сторона, цена токена, шейров, кошелёк контрагента
  ex_btc          сетка 100 мс от T-20 до T+305 с: фьючерс Binance (bnf; bfb - середина bookTicker), спот Binance (bn),
                  Bybit, OKX (ok), Coinbase, Chainlink (последняя цена)
"""
from __future__ import annotations

import argparse
import os
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import pandas as pd

import flow_map as fm
from jump_study import save_parts
from lead_lag import read
from tape_fetch import fetch_market

KEY = ["ts", "wallet", "side", "outcome", "price", "size", "tx"]


def cat(roots, stream, cols=None):
    ds = [read(r, stream, cols) for r in roots]
    ds = [d for d in ds if not d.empty]
    return pd.concat(ds, ignore_index=True) if ds else pd.DataFrame()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--wallet", required=True)
    ap.add_argument("--wfrom", type=int, required=True)
    ap.add_argument("--wto", type=int, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    W = a.wallet.lower()
    t0 = time.time()
    ws = cat(a.roots, "windows").drop_duplicates("slug", keep="last")
    ws = ws[(ws.start >= a.wfrom) & (ws.start < min(a.wto, time.time() - 480)) & ws.condition_id.notna()].sort_values("start")
    print(f"окон {len(ws)}", flush=True)

    def tape(r):
        out = []
        for mode in ("true", "false"):
            rows, _, err, _ = fetch_market(r.condition_id, mode)
            for x in rows:
                out.append(dict(w=int(r.start), mode=mode, ts=x.get("timestamp"), wallet=str(x.get("proxyWallet", "")).lower(),
                                side=x.get("side"), outcome=x.get("outcome"), price=x.get("price"), size=x.get("size"),
                                tx=x.get("transactionHash")))
        return out
    with ThreadPoolExecutor(3) as ex:
        tp = pd.DataFrame([x for rows in ex.map(tape, list(ws.itertuples())) for x in rows])
    print(f"лента: {len(tp)} записей, {time.time() - t0:.0f} с", flush=True)
    Tt = tp[tp["mode"] == "true"].drop(columns="mode").drop_duplicates(["w"] + KEY)
    A = tp[tp["mode"] == "false"].drop(columns="mode").drop_duplicates(["w"] + KEY)
    tx1 = Tt.drop_duplicates("tx").set_index("tx")
    is_tk = ((A.wallet.values == A.tx.map(tx1.wallet).values) & (A.side.values == A.tx.map(tx1.side).values)
             & (A.outcome.values == A.tx.map(tx1.outcome).values))
    Mk = A[~is_tk].copy()
    Mk["taker"] = Mk.tx.map(tx1.wallet)
    # сборщик
    top = cat(a.roots, "pm_top", ["recv_ms", "d", "w", "o", "bid", "ask", "bid_sz", "ask_sz"])
    top = top[(top.o == "U") & top.w.isin(ws.start)]
    top["srv"] = top.recv_ms - top.d
    tr = cat(a.roots, "pm_trades", ["server_ts", "w", "o", "side", "price", "size"])
    tr = tr[tr.w.isin(ws.start)]
    bnf = cat(a.roots, "bnf_agg", ["T", "price"]).dropna()
    win = {int(r.start): (1 if str(r.official_winner).startswith("Up") else 0 if str(r.official_winner).startswith("Down") else np.nan)
           for r in ws.itertuples()}
    ev = fm.events(top[["w", "srv", "bid", "ask", "bid_sz", "ask_sz"]], tr, bnf, win)
    ev["sd"] = ev.side.astype(str).str[0].str.upper()
    ev["ts_s"] = ev.server_ts / 1000
    Tt = Tt.reset_index(drop=True)
    Tt["o"] = Tt.outcome.str[0].str.upper()
    Tt["sd"] = Tt.side.str[0].str.upper()
    Tt["ti"] = np.arange(len(Tt))
    ev = ev.reset_index(drop=True)
    ev["ei"] = np.arange(len(ev))
    pairs = []
    for w, e in ev.groupby("w"):
        t = Tt[Tt.w == w]
        c = e[["ei", "o", "sd", "size", "price_tok", "ts_s"]].merge(
            t[["ti", "o", "sd", "size", "price", "ts"]].rename(columns={"size": "size_t"}), on=["o", "sd"])
        c["dt"] = c.ts - c.ts_s
        c = c[(c.dt >= -1.5) & (c.dt <= 10) & (np.abs(c.size_t / c["size"] - 1) < 0.01)]
        c = c.assign(pd_=np.abs(c.price - c.price_tok)).sort_values(["pd_", "dt"])
        ue, ut = set(), set()
        for r in c.itertuples(index=False):
            if r.ei in ue or r.ti in ut:
                continue
            ue.add(r.ei); ut.add(r.ti); pairs.append((r.ei, r.ti))
    P = pd.DataFrame(pairs, columns=["ei", "ti"])
    ev["ti"] = ev.ei.map(P.set_index("ei").ti)
    ev["wallet"] = ev.ti.map(Tt.wallet)
    ev["tx"] = ev.ti.map(Tt.tx)
    print(f"заявок сборщика {len(ev)}, с кошельком {ev.wallet.notna().mean():.1%}", flush=True)
    # его исполнения
    rows = []
    for r in ev[ev.wallet == W].itertuples():
        rows.append(dict(w=r.w, ts=r.server_ts, role="T", tok=r.o, side=r.side, price=r.price_tok, size=r.size, levels=r.levels,
                         cp=""))
    tx_ts = ev.dropna(subset=["tx"]).set_index("tx").server_ts
    for r in Mk[Mk.wallet == W].itertuples():
        rows.append(dict(w=r.w, ts=tx_ts.get(r.tx, (r.ts - 2.2) * 1000), role="M" if r.tx in tx_ts.index else "Ml",
                         tok=str(r.outcome)[0].upper(), side=str(r.side)[0].upper(), price=r.price, size=r.size, levels=np.nan,
                         cp=str(r.taker)[:10]))
    got = set(ev[ev.wallet == W].ti.dropna().astype(int))
    for r in Tt[(Tt.wallet == W) & ~Tt.ti.isin(got)].itertuples():
        rows.append(dict(w=r.w, ts=(r.ts - 2.2) * 1000, role="P", tok=r.o, side=r.sd, price=r.price, size=r.size, levels=np.nan,
                         cp=""))
    H = pd.DataFrame(rows).sort_values(["w", "ts"])
    # выгрузка
    wsx = ws[["start", "slug", "ptb_twap", "ptb_chainlink", "end_twap", "official_winner"]].rename(columns={"start": "w"})
    wsx["n_his"] = wsx.w.map(H.groupby("w").size()).fillna(0).astype(int)
    wsx.to_csv(os.path.join(a.out, "ex_win.csv"), index=False)
    save_parts(top[["w", "srv", "bid", "ask", "bid_sz", "ask_sz"]].round(3), os.path.join(a.out, "ex_top"))
    dep = cat(a.roots, "pm_depth")
    if not dep.empty:
        dep = dep[dep.w.isin(ws.start)]
        dep["o"] = dep.o.astype(str).str[0]
        save_parts(dep.round(3), os.path.join(a.out, "ex_dep"))
    ev["w10"] = ev.wallet.astype(str).str[:10]
    save_parts(ev[["w", "server_ts", "dir", "o", "side", "p", "size", "levels", "w10"]].round(4), os.path.join(a.out, "ex_ev"))
    save_parts(H.round(4), os.path.join(a.out, "ex_his"))
    # BTC на сетке 100 мс
    srcs = {"bnf": bnf.sort_values("T")}
    for nm, st, tc, pc in (("by", "by_trade", "T", "price"), ("cb", "cb_ticker", "t_ms", "price"),
                           ("bn", "bn_agg", "T", "price"), ("ok", "ok_trade", "T", "price")):
        try:
            d = cat(a.roots, st, [tc, pc]).dropna()
        except Exception as ex:                                 # потока нет в этот день
            print(f"{st}: {ex!r}", flush=True); continue
        if not d.empty:
            srcs[nm] = d.rename(columns={tc: "T", pc: "price"}).sort_values("T")
    try:                                                        # середина лучших цен фьючерса (bookTicker, время биржи)
        d = cat(a.roots, "bnf_book", ["T", "bid", "ask"]).dropna()
        if not d.empty:
            srcs["bfb"] = d.assign(price=(d.bid + d.ask) / 2)[["T", "price"]].sort_values("T")
    except Exception as ex:
        print(f"bnf_book: {ex!r}", flush=True)
    d = cat(a.roots, "rtds", ["feed", "ts_ms", "value"])
    if not d.empty:
        srcs["cl"] = d[d.feed == "cl"].rename(columns={"ts_ms": "T", "value": "price"}).sort_values("T")
    grid = []
    for w in ws.start.astype(int):
        g = np.arange((w - 20) * 1000, (w + 305) * 1000, 100.0)
        row = {"w": np.full(len(g), w), "t": g}
        for nm, d in srcs.items():
            tt, pp = d["T"].values.astype(float), d.price.values.astype(float)
            i = np.searchsorted(tt, g, side="right") - 1
            row[nm] = np.where(i >= 0, pp[np.maximum(i, 0)], np.nan)
        grid.append(pd.DataFrame(row))
    save_parts(pd.concat(grid).round(2), os.path.join(a.out, "ex_btc"))
    print(f"готово: его исполнений {len(H)} в {H.w.nunique()} окнах, {time.time() - t0:.0f} с", flush=True)
    print(H.role.value_counts().to_dict())


if __name__ == "__main__":
    main()
