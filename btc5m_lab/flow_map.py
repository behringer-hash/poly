"""Карта потока тейкеров внутри окна: кто когда торгует и насколько он информирован (запись сборщика, мс).

    python flow_map.py DATA_DIR/2026-10-27 [DATA_DIR/...] --out OUT [--tag fm]
    python flow_map.py --slice RESULTS_DIR:r3a,r3b --out OUT          # локально по выгрузке export_slice

Каждая сделка pm_trades - со стороны тейкера (токен и сторона заявки). Всё переводится в термины Up:
dir = +1 (купил Up / продал Down), -1 (купил Down / продал Up); p = цена в Up.
Тейкерская заявка = сделки одного окна с одним временем сервера и одним направлением (одна заявка сводится
со многими мейкерами за раз).
Для каждой заявки: mid Up до сделки (1 мс раньше) и через 1/5/30/60 с, исход окна; ход фьючерса Binance за 1 и 5 с
до сделки. Величины на шейр, в центах, со стороны тейкера:
  spread = dir*(mid0 - p)          - сколько он переплатил к mid в момент сделки (обычно < 0)
  mN     = dir*(midN - p)          - маркаут через N с (то, что он «заработал» по цене N с спустя)
  edge   = dir*(won - p)           - результат по исходу окна (без комиссии)
Мейкер получает минус то же самое (плюс ребейт). Средние взвешены по шейрам; погрешность - по окнам.
Выход: OUT/<tag>_events.csv.gz (заявки, для дальнейших разрезов) и печать таблиц.
"""
from __future__ import annotations

import argparse
import glob
import os

import numpy as np
import pandas as pd

from lead_lag import read

HZ = (1, 5, 30, 60)


def load_root(root):
    top = read(root, "pm_top", ["recv_ms", "d", "w", "o", "bid", "ask", "bid_sz", "ask_sz"])
    top = top[top.o == "U"].copy()
    top["srv"] = top.recv_ms - top.d
    tr = read(root, "pm_trades", ["server_ts", "w", "o", "side", "price", "size"])
    bnf = read(root, "bnf_agg", ["T", "price"]).dropna()
    ws = read(root, "windows")
    win = {}
    if not ws.empty:
        ws = ws.drop_duplicates("slug", keep="last")
        for r in ws.itertuples():
            ow = str(r.official_winner).lower()
            if ow.startswith("up"):
                win[int(r.start)] = 1
            elif ow.startswith("down"):
                win[int(r.start)] = 0
    return top[["w", "srv", "bid", "ask", "bid_sz", "ask_sz"]], tr, bnf, win


def load_slice(spec):
    R, pfx = spec.split(":")
    rd = lambda p: pd.concat([pd.read_csv(f) for x in pfx.split(",") for f in sorted(glob.glob(f"{R}/{x}_{p}*.csv.gz"))],
                             ignore_index=True)
    top, tr, bnf = rd("top"), rd("trades"), rd("bnf")
    return top[["w", "srv", "bid", "ask", "bid_sz", "ask_sz"]], tr, bnf, {}


def events(top, tr, bnf, win):
    tr = tr.dropna(subset=["server_ts", "price", "size"]).copy()
    tr = tr[tr["size"] > 0]
    up = tr.o.astype(str).str.upper().str.startswith("U")
    buy = tr.side.astype(str).str.upper().str.startswith("B")
    tr["dir"] = np.where(up == buy, 1, -1)
    tr["p"] = np.where(up, tr.price, 1 - tr.price)
    tr["notional"] = tr.price * tr["size"]
    tr["pv"] = tr.p * tr["size"]
    g = tr.groupby(["w", "server_ts", "dir"], sort=False)
    ev = g.agg(size=("size", "sum"), pv=("pv", "sum"), usd=("notional", "sum"), fills=("size", "size"),
               levels=("p", "nunique"), p_first=("p", "first"), p_last=("p", "last")).reset_index()
    tok = g.agg(o=("o", "first"), side=("side", "first"), price_tok=("price", "mean")).reset_index(drop=True)
    ev = pd.concat([ev, tok], axis=1)
    ev["p"] = ev.pv / ev["size"]
    ev["t"] = ev.server_ts / 1000 - ev.w
    out = []
    top = top.sort_values(["w", "srv"], kind="stable")
    for w, e in ev.groupby("w"):
        b = top[top.w == w]
        if len(b) < 5:
            continue
        ts = b.srv.values.astype(float)
        bid, ask = b.bid.values.astype(float), b.ask.values.astype(float)
        # книга с одной стороной (в конце окна: 0,99 без ask / 0,01 без bid) - цена по оставшейся стороне
        mid = np.where(np.isnan(ask), bid, np.where(np.isnan(bid), ask, (bid + ask) / 2))
        spr = ask - bid
        e = e.copy()
        t = e.server_ts.values.astype(float)
        i0 = np.searchsorted(ts, t - 1, side="right") - 1
        e["mid0"] = np.where(i0 >= 0, mid[np.clip(i0, 0, None)], np.nan)
        e["spr0"] = np.where(i0 >= 0, spr[np.clip(i0, 0, None)], np.nan)
        for h in HZ:
            j = np.searchsorted(ts, t + 1000 * h, side="right") - 1
            ok = (j >= 0) & (t + 1000 * h <= ts[-1] + 1)
            e[f"mid{h}"] = np.where(ok, mid[np.clip(j, 0, None)], np.nan)
        e["won"] = win.get(int(w), np.nan)
        if np.isnan(e.won.iloc[0]):       # нет официального исхода - по последнему mid (> 0,9 / < 0,1)
            last = mid[-1] if ts[-1] / 1000 - w > 295 else np.nan
            e["won"] = 1.0 if last > 0.9 else (0.0 if last < 0.1 else np.nan)
        out.append(e)
    ev = pd.concat(out, ignore_index=True)
    bT, bP = bnf["T"].values.astype(float), bnf.price.values.astype(float)
    o = np.argsort(bT, kind="stable"); bT, bP = bT[o], bP[o]
    def px(t):
        i = np.searchsorted(bT, t, side="right") - 1
        return np.where(i >= 0, bP[np.clip(i, 0, None)], np.nan)
    t = ev.server_ts.values.astype(float)
    p0 = px(t)
    ev["dS1"] = ev["dir"] * (p0 - px(t - 1000))
    ev["dS5"] = ev["dir"] * (p0 - px(t - 5000))
    ev["dSf1"] = ev["dir"] * (px(t + 1000) - p0)
    d = ev["dir"]
    ev["spread"] = 100 * d * (ev.mid0 - ev.p)
    for h in HZ:
        ev[f"m{h}"] = 100 * d * (ev[f"mid{h}"] - ev.p)
    ev["edge"] = 100 * d * (ev.won - ev.p)
    ev["fee"] = 100 * 0.07 * ev.p * (1 - ev.p)
    ev["p_tok"] = np.where(ev.o.astype(str).str.upper().str.startswith("U"), ev.p, 1 - ev.p)  # цена купленного/проданного токена
    return ev


def wmean(f, col):
    x, s = f[col], f["size"]
    ok = x.notna()
    x, s, w = x[ok], s[ok], f.w[ok]
    if s.sum() <= 0:
        return np.nan, np.nan
    m = (s * x).sum() / s.sum()
    e = (s * (x - m)).groupby(w).sum()
    return m, np.sqrt((e ** 2).sum()) / s.sum()


def table(ev, by, title):
    rows = []
    for k, f in ev.groupby(by, observed=True):
        r = {by if isinstance(by, str) else "срез": k, "заявок": len(f), "шейров_тыс": round(f["size"].sum() / 1e3, 1),
             "$тыс": round(f.usd.sum() / 1e3, 1), "окон": f.w.nunique()}
        for c in ("spread", "m1", "m5", "m30", "m60", "edge"):
            m, se = wmean(f, c)
            r[c] = round(m, 2)
            if c in ("m60", "edge"):
                r[c + "_se"] = round(se, 2)
        r["мейкер_исход"] = round(-r["edge"], 2)
        rows.append(r)
    print(f"\n=== {title} (ц/шейр со стороны тейкера; мейкер = минус) ===")
    print(pd.DataFrame(rows).to_string(index=False))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="*")
    ap.add_argument("--slice", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--tag", default="fm")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    parts = []
    srcs = [("slice", a.slice)] if a.slice else [("root", r) for r in a.roots]
    for kind, src in srcs:
        top, tr, bnf, win = load_slice(src) if kind == "slice" else load_root(src)
        if tr.empty or top.empty:
            print(f"{src}: нет данных"); continue
        ev = events(top, tr, bnf, win)
        ev["day"] = os.path.basename(os.path.normpath(src)) if kind == "root" else "slice"
        parts.append(ev)
        print(f"{src}: окон {ev.w.nunique()}, заявок {len(ev)}, с исходом {ev.won.notna().mean():.0%}", flush=True)
        del top, tr, bnf
    ev = pd.concat(parts, ignore_index=True)
    keep = ["day", "w", "server_ts", "t", "dir", "o", "side", "p", "p_tok", "size", "usd", "fills", "levels", "mid0",
            "spr0", "dS1", "dS5", "dSf1", "won", "spread"] + [f"m{h}" for h in HZ] + ["edge", "fee"]
    ev[keep].to_csv(os.path.join(a.out, f"{a.tag}_events.csv.gz"), index=False)
    ev["время"] = pd.cut(ev.t, [-20, 0, 30, 60, 120, 180, 240, 270, 290, 310])
    ev["размер"] = pd.cut(ev["size"], [0, 10, 50, 200, 1000, 1e9], labels=["<10", "10-50", "50-200", "200-1000", ">1000"])
    ev["цена_токена"] = pd.cut(ev.p_tok, [0, 0.1, 0.25, 0.4, 0.6, 0.75, 0.9, 1.0])
    ev["BTC_за_1с"] = pd.cut(ev.dS1, [-1e9, -10, -3, -0.5, 0.5, 3, 10, 1e9],
                             labels=["< -10 против", "-10..-3", "-3..-0,5", "≈0", "0,5..3", "3..10", "> 10 по ходу"])
    ev["сторона"] = ev.side.astype(str) + "_" + ev.o.astype(str)
    print(f"\nвсего: окон {ev.w.nunique()}, заявок {len(ev)}, шейров {ev['size'].sum() / 1e6:.2f} млн, "
          f"${ev.usd.sum() / 1e6:.2f} млн")
    for by in ("время", "размер", "цена_токена", "BTC_за_1с", "сторона"):
        table(ev, by, by)


if __name__ == "__main__":
    main()
