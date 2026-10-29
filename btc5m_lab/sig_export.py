"""Выгрузка признаков сигнала (sig_model.window_features) + цели (ход mid Up через 3 с) по дням для обучения модели
вне сервера (на сервере нет scikit-learn).

    python sig_export.py DATA_DIR/2026-10-16 [...] --out OUT [--step 10]

Шаг прореживания step (по 100 мс): 10 -> одна точка в секунду. Строки с mid вне 0,05–0,95 отброшены.
Выход: sigx_<день>_pNN.csv.gz (части <= 2 МБ): w, t, признаки FEATS, y3, won, fresh_up, fresh_dn.
"""
from __future__ import annotations

import argparse
import os
import time

import numpy as np
import pandas as pd

import sig_model as sm
from edge_maker import Trades
from edge_source import winners_ptb
from jump_study import save_parts
from lead_lag import PM, read
from mm_sim import Win


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--step", type=int, default=10)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for root in a.roots:
        t0 = time.time()
        day = os.path.basename(os.path.normpath(root))
        pm_top = read(root, "pm_top")
        if pm_top.empty:
            print(f"{day}: нет pm_top", flush=True)
            continue
        winners, ptb = winners_ptb(root)
        pm = PM(pm_top)
        del pm_top
        btc = {}
        for nm, st, tc in (("bnf", "bnf_agg", "T"), ("by", "by_trade", "T"), ("cb", "cb_ticker", "t_ms")):
            x = read(root, st, [tc, "price"]).dropna().sort_values(tc, kind="stable")
            if len(x):
                btc[nm] = (x[tc].values.astype(float), x.price.values.astype(float))
        r = read(root, "rtds", ["feed", "ts_ms", "value"])
        r = r[r.feed == "cl"].dropna().sort_values("ts_ms", kind="stable") if not r.empty else r
        if len(r):
            btc["cl"] = (r.ts_ms.values.astype(float), r.value.values.astype(float))
        tr = Trades(root)
        out = []
        for w in sorted(winners):
            if w not in pm.by_w or w not in ptb:
                continue
            try:
                win = Win(w, pm, tr, {})
                if len(win.st) < 20:
                    continue
                bu, au, bzu = win.s["U"]
                trades = None
                if win.tr is not None:
                    t_ = win.tr
                    trades = (t_[0], np.where((t_[1] == "U") == (t_[2] == "B"), 1.0, -1.0) * t_[4])
                D = sm.window_features(w, ptb[w], (win.st, bu, au, bzu, win.s["D"][2]), trades, btc)
                if D is None:
                    continue
                m = D.mid_raw.values
                y = np.full(len(m), np.nan)
                y[:-30] = 100 * (m[30:] - m[:-30])
                D["y3"] = y
                D["fresh_up"] = np.nanmax(np.vstack([D.dbnf03.values, D.dby03.values, D.dcb03.values]), axis=0)
                D["fresh_dn"] = -np.nanmin(np.vstack([D.dbnf03.values, D.dby03.values, D.dcb03.values]), axis=0)
                D = D.iloc[::a.step]
                D = D[D.mid.between(0.05, 0.95) & D.y3.notna()]
                D.insert(0, "w", w)
                D["won"] = 1 if winners[w] == "Up" else 0
                out.append(D[["w"] + sm.FEATS + ["y3", "won", "fresh_up", "fresh_dn"]])
            except Exception as ex:
                print(f"{day} {w}: {ex!r}"[:200], flush=True)
        if not out:
            continue
        X = pd.concat(out, ignore_index=True)
        X = X.astype({c: "float32" for c in X.columns if c not in ("w", "won")})
        save_parts(X.round(4), os.path.join(a.out, f"sigx_{day}"))
        print(f"{day}: строк {len(X)}, окон {X.w.nunique()}, {time.time() - t0:.0f} с", flush=True)


if __name__ == "__main__":
    main()
