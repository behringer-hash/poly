#!/usr/bin/env bash
# timeout_min: 40
# Пауза только после исполненного ордера (1 с после любого + 10/5/3 с после покупки) против 10 с после любого ордера.
# Два прогона: все накопленные дни и только период живого запуска C1 (с ~17:50 UTC 12 октября).
set -u
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -4)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
for mode in all live; do
  since=0; [ "$mode" = live ] && since=1791827400
  echo "=== $mode"
  # shellcheck disable=SC2086
  "$PYTHON" btc5m_lab/after_fill_sim.py $days --source bybit --thr 0.03 --sigma-mult 1 --slip 3 --latencies 250,300,400 \
      --since $since > "$OUT_DIR/after_fill_$mode.txt" 2>&1
  head -c 4500 "$OUT_DIR/after_fill_$mode.txt"
done
