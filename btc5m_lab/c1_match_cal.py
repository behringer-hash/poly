"""Живые ордера C1 (FAK, лимит = ask сигнала + 7 ц) против книги сервера: когда на самом деле сводится тейкерский ордер.

    python c1_match_cal.py /home/lab/incoming/bot_data_c1_w --pm-roots data/2026-10-19 ... --out OUT

Для каждого живого ордера берём лучший ask его токена в книге СЕРВЕРА (pm_top, время сервера) в моменты t_sent + L,
перед ответом (t_resp - 11 / - 30 мс), минимум и максимум ask на отрезке [t_sent + 172, t_resp - 11] (возможное время
сведения), ask в нашей локальной книге в момент сигнала и время, когда ask сервера впервые стал выше лимита.
Выход: c1cal.csv.gz (строка на ордер; статистика считается отдельно).
"""
from __future__ import annotations

import argparse
import os

import numpy as np
import pandas as pd

from lead_lag import PM, read
from live_vs_replay import orders_table

LAGS = [0, 50, 100, 150, 175, 200, 250, 300, 350, 400, 500, 700, 1000, 1500, 2000]


def side(s, X, i):
    """(ask, объём на ask) токена X по индексу состояния книги Up."""
    if X == "U":
        return float(np.round(s["ask"][i], 2)), float(s["asz"][i])
    b = s["bid"][i]
    return (float(np.round(1 - b, 2)) if np.isfinite(b) else np.nan), float(s["bsz"][i])


def ask_path(s, X, i0, i1):
    if X == "U":
        return np.round(s["ask"][i0:i1 + 1].astype(float), 2)
    return np.round(1 - s["bid"][i0:i1 + 1].astype(float), 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("bot_root")
    ap.add_argument("--pm-roots", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    o = orders_table([a.bot_root])
    o = o.drop_duplicates(["slug", "outcome", "t_signal"]).reset_index(drop=True)
    o["day"] = pd.to_datetime(o.w, unit="s").dt.strftime("%Y-%m-%d")
    print(f"ордеров {len(o)}; по дням {o.day.value_counts().sort_index().to_dict()}", flush=True)
    rows = []
    for root in a.pm_roots:
        day = os.path.basename(os.path.normpath(root))
        od = o[o.day == day]
        if od.empty:
            continue
        top = read(root, "pm_top")
        if top.empty:
            print(f"{day}: нет pm_top", flush=True)
            continue
        pm = PM(top)
        del top
        n_ok = 0
        for r in od.itertuples():
            X = "U" if r.outcome == "Up" else "D"
            b = pm.by_w.get(int(r.w))
            if b is None:
                continue
            s, rc = b["srv"], b["rcv"]
            ts = float(r.t_sent) * 1000.0
            tresp = float(r.t_resp) * 1000.0 if np.isfinite(r.t_resp) else np.nan
            rec = dict(sid=r.sid, w=int(r.w), outcome=r.outcome, t_signal=r.t_signal, t_sent=r.t_sent, t_resp=r.t_resp,
                       http_ms=r.http_ms, limit=r.limit, ask_signal=r.ask_signal, status=r.status, filled=r.filled, avg_px=r.avg_px,
                       edge_c=getattr(r, "edge_c", np.nan), T=getattr(r, "T", np.nan), day=day)
            for L in LAGS:
                i = int(np.searchsorted(s["t"], ts + L, side="right") - 1)
                rec[f"a{L}"], rec[f"z{L}"] = side(s, X, i) if i >= 0 else (np.nan, np.nan)
            i = int(np.searchsorted(rc["t"], float(r.t_signal) * 1000.0, side="right") - 1)
            rec["a_rcv0"] = side(rc, X, i)[0] if i >= 0 else np.nan
            if np.isfinite(tresp):
                for k in (11, 30):
                    i = int(np.searchsorted(s["t"], tresp - k, side="right") - 1)
                    rec[f"a_resp{k}"] = side(s, X, i)[0] if i >= 0 else np.nan
                i0 = int(np.searchsorted(s["t"], ts + 172.0, side="right") - 1)
                i1 = int(np.searchsorted(s["t"], tresp - 11.0, side="right") - 1)
                if i0 >= 0 and i1 >= i0:
                    p = ask_path(s, X, i0, i1)
                    rec["a_min"], rec["a_max"] = (np.nanmin(p), np.nanmax(p)) if np.isfinite(p).any() else (np.nan, np.nan)
                    rec["n_chg"] = i1 - i0
            i0 = int(np.searchsorted(s["t"], ts, side="right") - 1)
            if i0 >= 0:
                i1 = int(np.searchsorted(s["t"], ts + 3000.0, side="right") - 1)
                p = ask_path(s, X, i0, i1)
                hi = np.flatnonzero(p > float(r.limit) + 1e-9)
                rec["run_ms"] = (s["t"][i0 + hi[0]] - ts) if len(hi) else np.nan
                if len(hi) and hi[0] == 0:
                    rec["run_ms"] = 0.0
            rows.append(rec)
            n_ok += 1
        print(f"{day}: ордеров {len(od)}, с книгой {n_ok}", flush=True)
        del pm
    d = pd.DataFrame(rows)
    d.to_csv(os.path.join(a.out, "c1cal.csv.gz"), index=False)
    if len(d):
        m = d.status == "matched"
        print(f"итого {len(d)}; исполнено {m.mean():.1%}", flush=True)
        for L in LAGS:
            pred = d[f"a{L}"] <= d.limit + 1e-9
            print(f"  L={L:5d}: прогноз исполнения {pred.mean():.1%}, совпадение с фактом {(pred == m).mean():.1%}, "
                  f"ask = цене сделки у исполненных {(np.abs(d[f'a{L}'] - d.avg_px) < 0.005)[m].mean():.1%}", flush=True)


if __name__ == "__main__":
    main()
