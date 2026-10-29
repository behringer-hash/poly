#!/usr/bin/env bash
# timeout_min: 30
# Покрытие потоков по часам (строк) за 16–21 и 26–29.10: проверка, не было ли пропусков бирж 17.10 (P35 — убыточный день).
set -u
cd btc5m_lab || exit 1
nice -n 19 "$PYTHON" -u -W ignore - "$DATA_DIR" <<'PY'
import sys, os, glob, pandas as pd
D = sys.argv[1]
rows = []
for day in ["2026-10-16","2026-10-17","2026-10-18","2026-10-19","2026-10-20","2026-10-21","2026-10-26","2026-10-27","2026-10-28","2026-10-29"]:
    for st, tc in (("bnf_agg","T"),("by_trade","T"),("cb_ticker","t_ms"),("rtds","ts_ms"),("pm_top","recv_ms"),("pm_trades","server_ts")):
        for f in sorted(glob.glob(os.path.join(D, day, f"{st}_*.csv*"))):
            try:
                x = pd.read_csv(f, usecols=[tc], low_memory=False)
            except Exception:
                continue
            t = pd.to_numeric(x[tc], errors="coerce").dropna()
            if not len(t): continue
            h = pd.to_datetime(t, unit="ms").dt.floor("4h")
            for k, v in h.value_counts().items():
                rows.append((day, st, k, v))
R = pd.DataFrame(rows, columns=["day","st","h","n"]).groupby(["h","st"]).n.sum().unstack().fillna(0).astype(int)
pd.set_option("display.width", 250); pd.set_option("display.max_rows", 200)
print(R.to_string())
PY
