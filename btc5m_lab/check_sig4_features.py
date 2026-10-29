"""Сверка признаков стратегии 4: пакетный расчёт обучения (sig_model.window_features, pandas) против потокового
расчёта бота (btc5m_jump/sig4_model.features_at, numpy) на выгрузке окон (window_export.py) + сверка прогноза деревьев.

    python check_sig4_features.py EXPORT_DIR [--windows 20] [--model ../btc5m_jump/models/sig3s_v2.npz]
"""
from __future__ import annotations

import argparse
import glob
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "btc5m_jump"))
import sig_model as sm          # noqa: E402
import sig4_model as live       # noqa: E402


def load(d, nm):
    fs = sorted(glob.glob(f"{d}/{nm}*.csv.gz"))
    return pd.concat([pd.read_csv(f) for f in fs], ignore_index=True) if fs else pd.DataFrame()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export_dir")
    ap.add_argument("--windows", type=int, default=20)
    ap.add_argument("--model", default=os.path.join(HERE, "..", "btc5m_jump", "models", "sig3s_v2.npz"))
    ap.add_argument("--trigger", action="store_true", help="сквозная проверка триггера бота (sig4.Sig4Trigger)")
    a = ap.parse_args()
    if a.trigger:
        check_trigger(a.export_dir, a.windows, a.model)
        return
    win = pd.read_csv(f"{a.export_dir}/ex_win.csv")
    top, ev, bt = load(a.export_dir, "ex_top"), load(a.export_dir, "ex_ev"), load(a.export_dir, "ex_btc")
    trees_b, trees_l = sm.Trees(a.model), live.Trees(a.model)
    ws = sorted(win.w)[: a.windows]
    worst = {n: 0.0 for n in sm.FEATS}
    nrow = nbad = 0
    pdiff = []
    for w in ws:
        K = float(win.set_index("w").loc[w, "ptb_twap"])
        tp = top[top.w == w].sort_values("srv", kind="stable")
        e = ev[ev.w == w].sort_values("server_ts", kind="stable")
        b = bt[bt.w == w].sort_values("t")
        book = (tp.srv.values, tp.bid.values, tp.ask.values, tp.bid_sz.values, tp.ask_sz.values)
        trades = (e.server_ts.values, (e.dir * e["size"]).values) if len(e) else None
        btc = {c: (b.t.values, b[c].values) for c in ("bnf", "by", "cb", "cl") if c in b}
        D = sm.window_features(w, K, book, trades, btc)
        if D is None:
            continue
        # потоково
        wd = live.WinData(w)
        for r in tp.itertuples():
            wd.add_top(r.srv, r.bid, r.ask, r.bid_sz, r.ask_sz)
        for r in e.itertuples():
            wd.add_trade(r.server_ts, r.dir * r.size)
        G = {c: live.GridSeries() for c in ("bnf", "by", "cb", "cl")}
        for c, g in G.items():
            if c in b:
                for T, p in zip(b.t.values, b[c].values):
                    if p == p:
                        g.add(float(T), float(p))
            g.start_window(w)
        Xb = D[sm.FEATS].values
        pb = trees_b.predict(Xb)
        for i, t in enumerate(D.t.values):
            t = float(t)
            tm = (w + t) * 1000.0
            for g in G.values():
                g.close_upto(tm)
            row, up, dn = live.features_at(t, wd, K, {c: G[c] for c in ("bnf", "by", "cb")}, G["cl"])
            if t < 12:              # до 12 с у обучения std «за всё окно» - не сравниваем fair
                continue
            nrow += 1
            bad = False
            for j, n in enumerate(sm.FEATS):
                x, y = row[j], Xb[i, j]
                if (x != x) != (y != y):
                    worst[n] = float("inf"); bad = True
                elif x == x:
                    dd = abs(x - y) / max(1.0, abs(y))
                    worst[n] = max(worst[n], dd)
                    bad = bad or dd > 1e-6
            nbad += bad
            pdiff.append(abs(trees_l.predict_row(row) - pb[i]))
    print(f"окон {len(ws)}, точек сетки (t >= 12 с) {nrow}, с расхождением > 1e-6: {nbad}")
    print("макс. относительное расхождение по признакам:")
    for n, v in worst.items():
        print(f"  {n:7s} {v:.2e}")
    pdiff = np.array(pdiff)
    print(f"прогноз: макс. |разница| {pdiff.max():.2e} ц, 99,9% {np.quantile(pdiff, 0.999):.2e} ц")



def check_trigger(export_dir, n_windows=5, model=None):
    """Сквозная проверка триггера бота: строки движка (pm_top / pm_trades / rtds) и сделки бирж в форматах бота ->
    Sig4Trigger.tick() на каждой точке сетки -> прогноз против пакетного расчёта обучения."""
    import types
    import sig4
    model = model or os.path.join(HERE, "..", "btc5m_jump", "models", "sig3s_v2.npz")
    win = pd.read_csv(f"{export_dir}/ex_win.csv")
    top, ev, bt = load(export_dir, "ex_top"), load(export_dir, "ex_ev"), load(export_dir, "ex_btc")
    tb = sm.Trees(model)
    diffs = []
    for w in sorted(win.w)[1:n_windows + 1]:
        K = float(win.set_index("w").loc[w, "ptb_twap"])
        clk = types.SimpleNamespace(t=0.0, now=lambda: clk.t)
        sig4.clock = clk
        fw = types.SimpleNamespace(start=w, end=w + 300, slug=str(w), book_lag_ms=10.0, ptb=K, ready=lambda: True,
                                   books={s: types.SimpleNamespace(bb=0.5, ba=0.51, bids={}, asks={}) for s in ("Up", "Down")})
        pm_ = types.SimpleNamespace(windows={w: fw}, offset_ms=0.0, current_window=lambda now: fw)
        tr = types.SimpleNamespace(open={}, on_signal=lambda s: None, cancel_early=lambda *a: False,
                                   mstats=dict(filled=0, shares=0.0), total_pnl=0.0)
        wr = types.SimpleNamespace(write=lambda s, r: None)
        st = sig4.Sig4Trigger(dict(variant="sig4"), pm_, wr, tr, trees=live.Trees(model))
        # история: прошлое окно и это (BTC-сетка от T-20 с)
        b = bt[bt.w == w].sort_values("t")
        for c, col in (("bnf", "bnf"), ("by", "by"), ("cb", "cb")):
            prev = None
            for T, p in zip(b.t.values, b[col].values):
                if p == p and p != prev:
                    st.on_btc(c, float(T), float(p), float(T) / 1000)
                    prev = p
        prev = None
        for T, p in zip(b.t.values, b.cl.values):
            if p == p and p != prev:
                st.on_row("rtds", (int(T) + 900, "cl", int(T), float(p)))
                prev = p
        for r in top[top.w == w].sort_values("srv", kind="stable").itertuples():
            st.on_row("pm_top", (int(r.srv) + 40, 40, w, "U", r.bid, r.bid_sz, r.ask, r.ask_sz, 0))
        for r in ev[ev.w == w].itertuples():
            st.on_row("pm_trades", (int(r.server_ts) + 40, int(r.server_ts), w, r.o, r.side, r.p, r.size, 0, ""))
        # пакетный прогноз
        tp = top[top.w == w].sort_values("srv", kind="stable"); e = ev[ev.w == w].sort_values("server_ts", kind="stable")
        D = sm.window_features(w, K, (tp.srv.values, tp.bid.values, tp.ask.values, tp.bid_sz.values, tp.ask_sz.values),
                               (e.server_ts.values, (e.dir * e["size"]).values) if len(e) else None,
                               {c: (b.t.values, b[c].values) for c in ("bnf", "by", "cb", "cl")})
        pb = dict(zip(np.round(D.t.values, 1), tb.predict(D[sm.FEATS].values)))
        st.t_start = w - 100
        for t in np.round(np.arange(12.0, 285.0, 0.1), 1):
            clk.t = w + t + 0.15
            p = st.tick()
            if p is not None:
                diffs.append(abs(p - pb[t]))
    d = np.array(diffs)
    print(f"триггер бота: окон {n_windows}, шагов {len(d)}, совпало точно {np.mean(d < 1e-9):.4f}, макс. разница {d.max():.2e} ц")


if __name__ == "__main__":
    main()
