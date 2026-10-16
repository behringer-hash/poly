#!/usr/bin/env bash
# timeout_min: 90
# A: живые ордера против книги сервера с реальной задержкой; B: реплей с живым распределением задержки; C: предсказание дожития по книге.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -6)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
live=""; [ -d /home/lab/incoming/bot_data_c1 ] && live="--live-data /home/lab/incoming/bot_data_c1"
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/fill_predict.py $days --source bybit $live > "$OUT_DIR/fill_predict.txt" 2>&1
echo "код $?"
head -c 12000 "$OUT_DIR/fill_predict.txt" | cut -c1-220
