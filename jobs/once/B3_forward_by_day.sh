#!/usr/bin/env bash
# timeout_min: 60
# C1 по дням: колонка «дни» (цсигнал по каждому календарному дню) для переплат 0/3/8 ц и задержек 250/300/400 мс; вперёд и на всех данных.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
for mode in forward all; do
  n=6; [ "$mode" = forward ] && n=4
  days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -$n)
  since=0; [ "$mode" = forward ] && since=1791892800
  echo "=== C1 по дням: $mode (дни идут по порядку календарных суток, последний может быть неполным)"
  # shellcheck disable=SC2086
  nice -n 19 "$PYTHON" -u btc5m_lab/replay.py $days --source bybit --latencies 250,300,400 --thr 0.03 --sigma-mult 1 --slip-c 0,3,8 \
      --since $since > "$OUT_DIR/by_day_$mode.txt" 2>&1
  echo "код $?"
  grep -v "^/home" "$OUT_DIR/by_day_$mode.txt" | head -c 4000 | cut -c1-220
done
