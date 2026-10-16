#!/usr/bin/env bash
# timeout_min: 40
# Зависит ли время ответа биржи от того, мог ли ордер исполниться при приходе, и от состояния рынка (с перестановочным контролем).
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/2026-10-12 "$DATA_DIR"/2026-10-13 2>/dev/null)
[ -z "$days" ] && { echo "нет данных за 12-13 октября"; exit 0; }
[ -d /home/lab/incoming/bot_data_c1 ] || { echo "нет /home/lab/incoming/bot_data_c1"; exit 0; }
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/latency_dependence.py $days --live-data /home/lab/incoming/bot_data_c1 --source bybit > "$OUT_DIR/latency_dependence.txt" 2>&1
echo "код $?"
head -c 9000 "$OUT_DIR/latency_dependence.txt" | cut -c1-230
