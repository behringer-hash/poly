#!/usr/bin/env bash
# timeout_min: 60
# v2 (osize). Различают ли признаки момента сигнала (книга, сделки, скачок Bybit/Binance, сила) прибыльные и убыточные живые покупки.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
A=/home/lab/incoming/bot_data_c1; B=/home/lab/incoming/bot_data_c1_s7
[ -d "$A" ] && [ -d "$B" ] || { echo "нет папок бота"; exit 0; }
days=$(ls -d "$DATA_DIR"/2026-10-12 "$DATA_DIR"/2026-10-13 "$DATA_DIR"/2026-10-16 "$DATA_DIR"/2026-10-17 "$DATA_DIR"/2026-10-18 2>/dev/null)
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/live_features_pnl.py --run r1 "$A" --run r2 "$B" --pm-roots $days > "$OUT_DIR/features.txt" 2>&1
echo "код $?"
head -c 8000 "$OUT_DIR/features.txt" | cut -c1-260
