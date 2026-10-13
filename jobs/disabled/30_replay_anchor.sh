#!/usr/bin/env bash
# interval_min: 720
# timeout_min: 90
# Реплей стратегии «anchor» на записанных данных за последние 2 дня: источники Bybit, Coinbase, Binance futures.
# Результат: таблицы replay_<источник>.txt (доля исполнений, ц/шейр по расчёту и маркауту, ИИ по окнам, разбивка по дням).
set -u
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -2)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
for src in bybit coinbase binance_fut; do
  echo "=== $src"
  # shellcheck disable=SC2086
  "$PYTHON" btc5m_lab/replay.py $days --source "$src" --latencies 150,300,450,600 \
      --thr 0.01,0.02,0.03,0.05 --sigma-mult 0.75,1,1.5 --slip-c 0,3 > "$OUT_DIR/replay_$src.txt" 2>&1
  tail -n 3 "$OUT_DIR/replay_$src.txt"
done
