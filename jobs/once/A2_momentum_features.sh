#!/usr/bin/env bash
# timeout_min: 90
# Моментум после скачка Bybit: признаки продолжения движения и логистическая модель поверх цены рынка (тест на поздних окнах).
set -u
ulimit -v 1500000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -4)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
for cfg in "8 500" "15 500" "25 1000"; do
  set -- $cfg
  echo "##### N=$1 W=$2"
  # shellcheck disable=SC2086
  nice -n 19 "$PYTHON" -u btc5m_lab/momentum_features.py $days --source bybit --N "$1" --W "$2" --L 300 > "$OUT_DIR/momentum_N$1_W$2.txt" 2>&1
  echo "код $?"
  head -c 9000 "$OUT_DIR/momentum_N$1_W$2.txt"
done
