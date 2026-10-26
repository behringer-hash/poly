#!/usr/bin/env bash
# timeout_min: 25
# Проверка мейкерского исполнения (live_maker.py) на живых данных в режиме dry: 15 минут, без ключей и без заявок.
# Сводка: сигналы, пропуски, теневые исполнения, ошибки.
set -u
cd btc5m_lab || exit 0
D="$OUT_DIR/bot"
timeout -s INT 900 nice -n 5 "$PYTHON" -u bot.py --live live_config_maker.example.json --mode dry --no-chart --clip 5 \
    --single-clob --variants c1:0.035:bybit:1 --latencies 200,300 --show c1@200 --data-dir "$D" > "$OUT_DIR/bot_console.txt" 2>&1
echo "код выхода бота: $?"
echo "=== строки MAKER (последние 60) ==="; grep -a "MAKER" "$OUT_DIR/bot_console.txt" | tail -60 | cut -c1-220
echo "=== ошибки ==="; grep -a -i -E "traceback|error|ошибк|exception" "$OUT_DIR/bot_console.txt" | head -30 | cut -c1-220
"$PYTHON" - "$D" <<'PY'
import sys, glob, pandas as pd
D = sys.argv[1]
def rd(s):
    fs = glob.glob(f"{D}/**/{s}_*.csv*", recursive=True)
    return pd.concat([pd.read_csv(f) for f in fs], ignore_index=True) if fs else pd.DataFrame()
o, f, w = rd("maker_orders"), rd("maker_final"), rd("live_windows")
print(f"\nзаявок {len(o)}; статусы: {o.status.value_counts().to_dict() if len(o) else {}}")
if len(f):
    print(f"снято {len(f)}; теневых исполнений {(f.shadow_qty > 0).sum()} ({(f.shadow_qty > 0).mean():.1%}), шейров {f.shadow_qty.sum():.0f}")
    print("время теневого исполнения, мс:", f.shadow_ms.dropna().round().tolist()[:30])
if len(o):
    print("цена - bid:", (o.price - o.bid).round(2).value_counts().to_dict(), "| спред:", (o.ask - o.bid).round(2).value_counts().to_dict())
print(w.to_string(index=False) if len(w) else "итогов окон нет")
PY
tail -c 150000 "$OUT_DIR/bot_console.txt" > "$OUT_DIR/bot_console_tail.txt"; rm -f "$OUT_DIR/bot_console.txt"
find "$D" -name "pm_trades*" -delete 2>/dev/null
