#!/usr/bin/env bash
# interval_min: 60
# Сводка недельного живого теста: путь pnl по суткам и общая статистика ордеров. Данные: /home/lab/incoming/bot_data_c1_w (копия папки бота).
cd btc5m_lab || exit 0
for D in /home/lab/incoming/bot_data_c1_w /home/lab/incoming/bot_data_c2; do
[ -d "$D" ] || { echo "нет $D (бот не запущен или данные не скопированы)"; continue; }
echo; echo "######## $D"
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
    try:
        from live_subgroups import table
        t = table(sys.argv[1], "w")
        t["slip"] = pd.to_numeric(t.slip_c, errors="coerce")
        rows = []
        for k, x in t.groupby("slip"):
            f = x[x.filled_f]
            rows.append(dict(доплата_ц=k, ордеров=len(x), исполнено=round(x.filled_f.mean(), 3), ц_шейр=round(f.pnl.sum() / max(f.fsh.sum(), 1) * 100, 2),
                             долл=round(x.pnl.sum(), 2), ц_на_ордер=round(x.pnl.sum() / x["size"].astype(float).sum() * 100, 2)))
        print("\nпо доплате (ордера с известным победителем):")
        print(pd.DataFrame(rows).to_string(index=False))
    except Exception as e:
        print("по доплате: нет данных", repr(e)[:100])
PY
done
