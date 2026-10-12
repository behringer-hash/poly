#!/usr/bin/env bash
# timeout_min: 150
# Кластеры сигналов, пауза после первого сигнала и симуляция лимитов бота: 10 ордеров и $30 на окно, $100 в сутки, стоп -$20.
# C1: порог 0.03, sigma x1, +3 ц (все накопленные дни), C1 только после 11:30 UTC 10 октября, C2: порог 0.03, sigma x1.5, +3 ц.
set -u
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -5)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
run() {  # run <имя> <аргументы risk_sim>
  name="$1"; shift
  # shellcheck disable=SC2086
  "$PYTHON" btc5m_lab/risk_sim.py $days --source bybit --latencies 200,300 --cooldowns 1,3,5,10,30,300 \
      --max-orders-window 10 --max-spend-window 30 --max-spend-day 100 --max-loss-day 20 "$@" > "$OUT_DIR/risk_$name.txt" 2>&1
  echo "=== $name"; sed -n '/кластеры/,$p' "$OUT_DIR/risk_$name.txt" | head -80
}
run C1_all --thr 0.03 --sigma-mult 1 --slip 3
run C1_forward --thr 0.03 --sigma-mult 1 --slip 3 --since 1791631800
run C2_all --thr 0.03 --sigma-mult 1.5 --slip 3
