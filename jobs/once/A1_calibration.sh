#!/usr/bin/env bash
# timeout_min: 60
# Калибровка рынка по всем состояниям окна: средний результат покупки по ask (через 300 мс) по корзинам цены, z и времени.
set -u
ulimit -v 1500000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -4)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/calibration.py $days --source bybit --L 300 --step 5 > "$OUT_DIR/calibration.txt" 2>&1
echo "код $?"
head -c 14000 "$OUT_DIR/calibration.txt"
