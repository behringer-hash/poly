#!/usr/bin/env bash
# timeout_min: 60
# v2: лимит памяти 2.3 ГБ (1.5 мало для pandas + данных дня), по одному дню освобождаем память
# Проверка вперёд (данные после 12:00 UTC 13 октября) с переплатами 0-10 ц шагом 1-2 и от силы сигнала; для сравнения тот же набор на всех данных.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
for mode in forward all; do
  n=6; [ "$mode" = forward ] && n=4
  days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -$n)
  [ -z "$days" ] && { echo "нет данных"; exit 0; }
  since=0; [ "$mode" = forward ] && since=1791892800
  echo "=== C1 (Bybit, 0.03, sigma x1), переплаты 0-10 ц: $mode"
  # shellcheck disable=SC2086
  nice -n 19 "$PYTHON" -u btc5m_lab/replay.py $days --source bybit --latencies 250,300,400 --thr 0.03 --sigma-mult 1 \
      --slips 0,1,2,3,4,5,6,8,10,e:1:1:10,e:1.5:2:10 --exit-s 5 --since $since > "$OUT_DIR/slips_$mode.txt" 2>&1
  echo "код $?"
  head -c 7000 "$OUT_DIR/slips_$mode.txt" | cut -c1-200
done
