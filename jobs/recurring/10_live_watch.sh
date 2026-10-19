#!/usr/bin/env bash
# interval_min: 60
# Сводка недельного живого теста: путь pnl по суткам и общая статистика ордеров. Данные: /home/lab/incoming/bot_data_c1_w (копия папки бота).
D=/home/lab/incoming/bot_data_c1_w
[ -d "$D" ] || { echo "нет $D (живой тест не запущен или данные не скопированы)"; exit 0; }
cd btc5m_lab || exit 0
"$PYTHON" daypnl_path.py "$D" 2>&1 | cut -c1-200 | head -c 3000
"$PYTHON" - "$D" <<'PY' 2>&1 | head -c 2000
import sys
import pandas as pd
from live_vs_replay import orders_table
d = orders_table([sys.argv[1]])
if d.empty:
    print("нет живых ордеров")
else:
    d["day"] = pd.to_datetime(d.t_signal.astype(float), unit="s").dt.strftime("%m-%d")
    print(f"\nордеров {len(d)}, исполнено {int(d.filled_f.sum())} ({d.filled_f.mean():.1%}), http_ms медиана {d.http_ms.astype(float).median():.0f}")
    g = d.groupby("day").agg(ордеров=("filled_f", "size"), исполнено=("filled_f", "sum"), доля=("filled_f", "mean"))
    print(g.round(3).to_string())
PY
