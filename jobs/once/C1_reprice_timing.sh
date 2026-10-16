#!/usr/bin/env bash
# timeout_min: 60
# Как быстро цена ask уезжает после сигнала C1, доля мёртвых на старте, механизм (сделки конкурентов или снятие заявок), срезы.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -6)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/reprice_timing.py $days --source bybit --thr 0.03 --slip 3 > "$OUT_DIR/reprice_timing.txt" 2>&1
echo "код $?"
head -c 9000 "$OUT_DIR/reprice_timing.txt" | cut -c1-220
