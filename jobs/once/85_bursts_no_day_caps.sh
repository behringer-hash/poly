#!/usr/bin/env bash
# timeout_min: 150
# 1) risk_sim БЕЗ дневных лимитов трат и убытка (лимиты окна 10 ордеров и $30 остаются), C1 и C2;
# 2) burst_sim: пачки сигналов, их результат и способы ограничить вред, C1 по всем дням и только после 11:30 UTC 10 октября.
set -u
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -5)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
# shellcheck disable=SC2086
run() { name="$1"; script="$2"; shift 2
  "$PYTHON" btc5m_lab/$script.py $days --source bybit --latencies 200,300 "$@" > "$OUT_DIR/$name.txt" 2>&1
  echo "=== $name"; tail -n 25 "$OUT_DIR/$name.txt"; }
NODAY="--max-spend-day 1000000 --max-loss-day 1000000 --max-orders-window 10 --max-spend-window 30"
run nodaycap_C1_all risk_sim --thr 0.03 --sigma-mult 1 --slip 3 --cooldowns 1,10,30,300 $NODAY
run nodaycap_C1_forward risk_sim --thr 0.03 --sigma-mult 1 --slip 3 --cooldowns 1,10,30,300 $NODAY --since 1791631800
run nodaycap_C2_all risk_sim --thr 0.03 --sigma-mult 1.5 --slip 3 --cooldowns 1,10,30,300 $NODAY
run bursts_C1_all burst_sim --thr 0.03 --sigma-mult 1 --slip 3
run bursts_C1_forward burst_sim --thr 0.03 --sigma-mult 1 --slip 3 --since 1791631800
