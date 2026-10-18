#!/usr/bin/env bash
# timeout_min: 90
# v2: + срезы по силе сигнала и пороги edge. Переплата 0-10 ц по дням с задержкой из живых ордеров.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
[ -d /home/lab/incoming/bot_data_c1 ] || { echo "нет /home/lab/incoming/bot_data_c1"; exit 0; }
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -6)
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/slip_by_day.py $days --live-data /home/lab/incoming/bot_data_c1 --source bybit > "$OUT_DIR/slip_by_day_edge.txt" 2>&1
echo "код $?"
head -c 8000 "$OUT_DIR/slip_by_day_edge.txt" | cut -c1-220
