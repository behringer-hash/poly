#!/usr/bin/env bash
# timeout_min: 30
# N2 = N1 на обновлённой копии (данные до 26.10) + исходы всех окон из потока windows. Живой запуск c1 (bot_data_c1_w): выгрузка всех ордеров с исходом окна, итогов окон, маркаутов и бумажных сделок
# на тех же сигналах в OUT_DIR (статистика считается отдельно). Плюс проверка, нет ли копии данных новее.
set -u
ulimit -v 2300000 2>/dev/null || true
D=/home/lab/incoming/bot_data_c1_w
echo "== копия папки бота: $D"
[ -d "$D" ] || { echo "нет $D"; exit 0; }
du -sh "$D" 2>/dev/null
echo "самые новые файлы:"
find "$D" -type f -printf '%TY-%Tm-%Td %TH:%TM  %s  %P\n' 2>/dev/null | sort | tail -8
echo "файлов по потокам:"
find "$D" -type f -printf '%f\n' | sed -E 's/_[0-9]{4}-[0-9]{2}-[0-9]{2}.*//' | sort | uniq -c
echo "== другие копии (bot_data_c1_w*) в /home/lab:"
find /home/lab -maxdepth 4 -type d -name 'bot_data_c1_w*' 2>/dev/null
ls -la /home/lab/incoming 2>/dev/null
cd btc5m_lab || exit 1
nice -n 19 "$PYTHON" -u - "$D" "$OUT_DIR" <<'PY' 2>&1 | cut -c1-220 | head -c 8000
import os, sys
import pandas as pd
from analyze import load
from live_subgroups import table
root, out = sys.argv[1], sys.argv[2]
from live_vs_replay import orders_table
t = orders_table([root])
lw = load([root], "live_windows").groupby("slug", as_index=False).last()
win = dict(zip(lw.slug, lw.winner.astype(str)))
wn = load([root], "windows")
if len(wn):
    wn = wn.groupby("slug", as_index=False).last()
    wn[["slug", "start", "official_winner", "provisional_winner", "settled_with"]].to_csv(os.path.join(out, "c1w_windows_all.csv.gz"), index=False)
    for sl, a, b in zip(wn.slug, wn.official_winner.astype(str), wn.provisional_winner.astype(str)):
        if win.get(sl) not in ("Up", "Down"):
            win[sl] = a if a in ("Up", "Down") else b
t["win"] = t.slug.map(win)
print(f"ордеров {len(t)}, с исходом {t.win.isin(['Up', 'Down']).sum()}")
meta = load([root], "live_order_meta")
if len(meta):
    m = meta[["sid", "slug", "outcome", "fair"]].drop_duplicates(["sid", "slug", "outcome"])
    t = t.merge(m, on=["sid", "slug", "outcome"], how="left")
keep = [c for c in ["sid", "slug", "w", "outcome", "sgn", "t_signal", "t_sent", "t_resp", "sign_ms", "http_ms", "total_ms",
                    "limit", "size", "status", "filled", "usdc", "avg_px", "error", "ask_signal", "slip_c", "edge_c",
                    "fair", "T", "win"] if c in t.columns]
t[keep].to_csv(os.path.join(out, "c1w_orders.csv.gz"), index=False)
print(f"исполнено {int(t.filled_f.sum())}")
allo = load([root], "live_orders")
print(f"всего строк live_orders {len(allo)}; по режимам {allo['mode'].value_counts().to_dict() if len(allo) else {}}")
for s in ["live_windows", "live_markouts", "paper_fills", "paper_windows", "paper_markouts"]:
    x = load([root], s)
    if len(x):
        x.to_csv(os.path.join(out, f"c1w_{s}.csv.gz"), index=False)
    print(f"{s}: {len(x)} строк")
ps = load([root], "paper_signals")
if len(ps):
    cols = [c for c in ["sig_id", "recv", "slug", "T", "outcome", "variant", "reason", "ask", "ask_sz", "bid", "mid",
                        "fair_anchor", "edge", "btc_move_since_anchor", "anchor_age", "sigma", "btc_age_ms", "book_age_ms"] if c in ps.columns]
    ps[cols].to_csv(os.path.join(out, "c1w_paper_signals.csv.gz"), index=False)
    print(f"paper_signals: {len(ps)} строк; варианты {ps.variant.value_counts().to_dict()}")
PY
ls -la "$OUT_DIR"
