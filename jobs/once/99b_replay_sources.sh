#!/usr/bin/env bash
# timeout_min: 90
# v2: чтение записей игнорирует повторные заголовки (перезапуск сборщика дописывает их в файлы)
# Прибыль по источникам в модели C1 (порог 0.03, sigma x1, переплата 3 ц, L=250/300/400) на записи сервера.
set -u
ulimit -v 1500000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -4)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
for s in bybit bybit_trade binance_fut binance coinbase bitstamp; do
  echo "--- $s"
  # shellcheck disable=SC2086
  nice -n 19 "$PYTHON" -u btc5m_lab/replay.py $days --source $s --latencies 250,300,400 --thr 0.03 --sigma-mult 1 --slips 3 --exit-s 5 \
      > "$OUT_DIR/replay_$s.txt" 2>&1
  echo "код $?"; tail -n 8 "$OUT_DIR/replay_$s.txt" | cut -c1-200
done
