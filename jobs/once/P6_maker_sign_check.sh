#!/usr/bin/env bash
# timeout_min: 40
# Тест мейкера в режиме sign (/home/lab/incoming/maker_data_sign): выгрузка заявок, итогов и исходов окон в OUT_DIR и
# проверка теневого исполнения по книге СЕРВЕРА Polymarket из записи сборщика (pm_top, время сервера = recv - d):
# для каждой заявки - ask и bid её стороны на сервере в момент сигнала и через 100/150/200/250/335/500 мс и объём на ask.
set -u
ulimit -v 2300000 2>/dev/null || true
D=/home/lab/incoming/maker_data_sign
[ -d "$D" ] || { echo "нет $D"; exit 0; }
du -sh "$D"; ls "$D"
cd btc5m_lab || exit 1
nice -n 19 "$PYTHON" -u - "$D" "$DATA_DIR" "$OUT_DIR" <<'PY' 2>&1 | cut -c1-260 | head -c 6000
import os, sys
import numpy as np
import pandas as pd
from analyze import load
from lead_lag import read
D, DATA, OUT = sys.argv[1:4]
o = load([D], "maker_orders").drop_duplicates(["sid", "slug", "outcome", "t_signal"])
f = load([D], "maker_final").drop_duplicates(["sid", "slug", "outcome"])
wn = load([D], "windows")
lw = load([D], "live_windows")
print(f"заявок {len(o)}, итогов {len(f)}, окон windows {len(wn)}, live_windows {len(lw)}")
o.to_csv(os.path.join(OUT, "mk_orders.csv.gz"), index=False)
f.to_csv(os.path.join(OUT, "mk_final.csv.gz"), index=False)
if len(wn):
    wn.drop_duplicates("slug", keep="last")[["slug", "start", "official_winner", "provisional_winner"]].to_csv(os.path.join(OUT, "mk_windows.csv.gz"), index=False)
days = sorted({pd.to_datetime(t, unit="s").strftime("%Y-%m-%d") for t in o.t_signal.astype(float)})
print("дни теста:", days)
tops = []
for d in days:
    p = os.path.join(DATA, d)
    if os.path.isdir(p):
        t = read(p, "pm_top", ["recv_ms", "d", "w", "o", "bid", "bid_sz", "ask", "ask_sz"])
        if len(t):
            tops.append(t[t.o == "U"])
if not tops:
    print("нет записи книги сервера за дни теста")
    sys.exit(0)
top = pd.concat(tops, ignore_index=True)
top["srv"] = top.recv_ms - top.d
print(f"строк книги сервера {len(top)}, с {pd.to_datetime(top.srv.min(), unit='ms')} по {pd.to_datetime(top.srv.max(), unit='ms')}")
by = {int(w): g.sort_values("srv") for w, g in top.groupby("w")}
LAGS = [0, 100, 150, 200, 250, 335, 500]
rows = []
for r in o.itertuples():
    w = int(str(r.slug).rsplit("-", 1)[-1])
    g = by.get(w)
    if g is None:
        continue
    t0 = float(r.t_signal) * 1000.0
    st = g.srv.values
    row = dict(sid=r.sid, slug=r.slug, outcome=r.outcome, t_signal=r.t_signal, price=r.price, mode=r.price_mode)
    for L in LAGS:
        i = np.searchsorted(st, t0 + L, side="right") - 1
        if i < 0:
            continue
        b, a, bs, az = g.bid.values[i], g.ask.values[i], g.bid_sz.values[i], g.ask_sz.values[i]
        if r.outcome == "Up":
            sa, ssz, sb = a, az, b
        else:
            sa, ssz, sb = round(1 - b, 2), bs, round(1 - a, 2)
        row[f"ask{L}"], row[f"asz{L}"], row[f"bid{L}"] = sa, ssz, sb
    rows.append(row)
x = pd.DataFrame(rows)
x.to_csv(os.path.join(OUT, "mk_srvbook.csv.gz"), index=False)
print(f"заявок с книгой сервера {len(x)}")
PY
ls -la "$OUT_DIR"
