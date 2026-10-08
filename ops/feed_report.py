"""Задержки лент и качество записи за последние часы: по health_* потокам. Пишет feed_report.md в $OUT_DIR.

    DATA_DIR=... OUT_DIR=... python feed_report.py [часов, по умолчанию 6]

Задержка = локальное время приёма минус время события на бирже (включает смещение часов сервера, см. clock_*).
"""
from __future__ import annotations

import glob
import os
import sys

import numpy as np
import pandas as pd

DATA = os.environ.get("DATA_DIR", "data")
OUT = os.environ.get("OUT_DIR", ".")
HOURS = float(sys.argv[1]) if len(sys.argv) > 1 else 6.0


def read(stream: str) -> pd.DataFrame:
    fs = sorted(glob.glob(os.path.join(DATA, "*", f"{stream}_*.csv*")))
    dfs = []
    for f in fs:
        try:
            dfs.append(pd.read_csv(f, low_memory=False))
        except Exception:
            pass
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()


def tail(df: pd.DataFrame, col: str, hours: float) -> pd.DataFrame:
    if df.empty:
        return df
    df = df[pd.to_numeric(df[col], errors="coerce").notna()].copy()
    df[col] = pd.to_numeric(df[col])
    scale = 1000.0 if df[col].max() > 1e11 else 1.0
    return df[df[col] >= df[col].max() - hours * 3600 * scale]


def main():
    L = [f"# Задержки лент за последние {HOURS:g} ч\n"]
    hf = tail(read("health_feeds"), "ts", HOURS)
    if not hf.empty:
        for c in ("msgs", "lat_p50", "lat_p90"):
            hf[c] = pd.to_numeric(hf[c], errors="coerce")
        g = hf.groupby("feed").agg(
            интервалов=("msgs", "size"), сообщ_в_с=("msgs", lambda x: x.mean() / 10),
            пустых_интервалов_доля=("msgs", lambda x: (x == 0).mean()),
            лаг_p50_мс=("lat_p50", "median"), лаг_p90_мс=("lat_p90", lambda x: np.nanpercentile(x, 90) if x.notna().any() else np.nan))
        L += ["## Дополнительные биржи (health_feeds, интервалы по 10 с)", "```\n" + g.round(2).to_string() + "\n```", ""]
    hc = tail(read("health_cex"), "ts", HOURS)
    if not hc.empty:
        for c in hc.columns:
            hc[c] = pd.to_numeric(hc[c], errors="coerce")
        L += ["## Binance спот и Coinbase (health_cex)",
              f"- Binance: лаг p50 {hc.bn_lat_p50.median():.0f} мс, p90 по интервалам {np.nanpercentile(hc.bn_lat_p50, 90):.0f} мс, "
              f"сообщ/10с {hc.bn_msgs.mean():.0f}",
              f"- Coinbase: лаг p50 {hc.cb_lat_p50.median():.0f} мс, сообщ/10с {hc.cb_msgs.mean():.0f}",
              f"- задержка event loop процесса cex: p50 {hc.lag_p50.median():.2f} мс, p99 макс {hc.lag_p99.max():.1f} мс, "
              f"макс {hc.lag_max.max():.0f} мс", ""]
    hp = tail(read("health_pm"), "ts", HOURS)
    if not hp.empty:
        for c in hp.columns:
            hp[c] = pd.to_numeric(hp[c], errors="coerce")
        L += ["## Polymarket (health_pm)",
              f"- лаг ленты книги от сервера: p50 {hp.clob_lat_p50.median():.0f} мс, "
              f"p90 по интервалам {np.nanpercentile(hp.clob_lat_p90, 90):.0f} мс, макс {hp.clob_lat_p90.max():.0f} мс",
              f"- сообщений книги в 10 с: {hp.clob_msgs.mean():.0f}; сделок: {hp.trades.sum():.0f}",
              f"- задержка event loop процесса pm: p50 {hp.lag_p50.median():.2f} мс, макс {hp.lag_max.max():.0f} мс", ""]
    rt = tail(read("pm_rtt"), "ts_ms", HOURS)
    if not rt.empty:
        rt["rtt_ms"] = pd.to_numeric(rt.rtt_ms, errors="coerce")
        g = rt.groupby("endpoint").rtt_ms.describe(percentiles=[.5, .9, .99])[["count", "50%", "90%", "99%", "max"]]
        L += ["## RTT до Polymarket REST (pm_rtt, мс)", "```\n" + g.round(1).to_string() + "\n```", ""]
    ck = tail(read("clock"), "recv", HOURS)
    if not ck.empty:
        ck["offset_ms"] = pd.to_numeric(ck.offset_ms, errors="coerce")
        ck["rtt_ms"] = pd.to_numeric(ck.rtt_ms, errors="coerce")
        L += ["## Часы сервера относительно Binance",
              f"- смещение: медиана {ck.offset_ms.median():.1f} мс, размах {ck.offset_ms.min():.1f}…{ck.offset_ms.max():.1f} мс; "
              f"RTT до Binance REST p50 {ck.rtt_ms.median():.0f} мс", ""]
    if len(L) == 1:
        L.append("Нет данных за этот период.")
    text = "\n".join(L) + "\n"
    with open(os.path.join(OUT, "feed_report.md"), "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
