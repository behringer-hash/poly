#!/usr/bin/env bash
# timeout_min: 90
# Стратегия «скачок на N$ по сырым сделкам» (без модели справедливой цены) против C1.
set -u
ulimit -v 1500000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -4)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/trade_jump.py $days --sources bybit_trade,binance_fut,binance --N 8,15,25 --W 250,500,1000 \
    --latencies 250,300,400 --slips 0,3,5 --baseline > "$OUT_DIR/trade_jump.txt" 2>&1
echo "код $?"
head -c 14000 "$OUT_DIR/trade_jump.txt"
