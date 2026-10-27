"""Выгрузка куска записи сборщика за интервал времени: верх книги Polymarket (Up, время сервера и получения) и сделки
фьючерса и спота Binance - для сверки с живыми запусками ботов локально.

    python export_slice.py data/2026-10-27 --t0 1793116500 --t1 1793124900 --out OUT
Выход: xs_top (w, srv, recv_ms, bid, ask, bid_sz, ask_sz), xs_bnf / xs_bn (T, recv_ms, price), xs_trades (pm_trades);
файлы больше 1,8 МБ делятся на части _p0, _p1, ...
"""
from __future__ import annotations

import argparse
import os

import pandas as pd

from jump_study import save_parts
from lead_lag import read


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--t0", type=float, required=True)
    ap.add_argument("--t1", type=float, required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    t0, t1 = a.t0 * 1000, a.t1 * 1000
    top = read(a.root, "pm_top")
    top = top[(top.o == "U") & (top.recv_ms >= t0) & (top.recv_ms <= t1)].copy()
    top["srv"] = top.recv_ms - top.d
    top = top[["w", "srv", "recv_ms", "bid", "ask", "bid_sz", "ask_sz"]]
    save_parts(top, os.path.join(a.out, "xs_top"))
    print(f"pm_top: {len(top)} строк", flush=True)
    for name, stream in (("bnf", "bnf_agg"), ("bn", "bn_agg")):
        d = read(a.root, stream, ["recv_ms", "T", "price"]).dropna()
        d = d[(d["T"] >= t0 - 5000) & (d["T"] <= t1)]
        save_parts(d, os.path.join(a.out, f"xs_{name}"))
        print(f"{stream}: {len(d)} строк", flush=True)
    tr = read(a.root, "pm_trades")
    if not tr.empty:
        tcol = "server_ts" if "server_ts" in tr else "recv_ms"
        tr = tr[(tr[tcol] >= t0) & (tr[tcol] <= t1)]
        keep = [c for c in ("server_ts", "recv_ms", "w", "o", "side", "price", "size") if c in tr]
        save_parts(tr[keep], os.path.join(a.out, "xs_trades"))
        print(f"pm_trades: {len(tr)} строк", flush=True)
    for f in sorted(os.listdir(a.out)):
        print(f, os.path.getsize(os.path.join(a.out, f)))


if __name__ == "__main__":
    main()
