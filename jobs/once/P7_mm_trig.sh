#!/usr/bin/env bash
# timeout_min: 175
# Ход BTC на Binance за 50/100/200 мс -> заявка в лучший bid растущего токена (btc5m_lab/mm_trig.py), профили Токио и
# Стокгольм, 11 дней записи. Выход: trg_/trgh_<день>.csv.gz в OUT_DIR.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/2026-1* 2>/dev/null | sort | grep -v 2026-10-2[2-9])
[ -z "$days" ] && { echo "нет данных"; exit 0; }
start=$(date +%s)
for d in $days; do
  nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig.py "$d" --out "$OUT_DIR" 2>&1 | cut -c1-200 | tail -18
  echo "  прошло $(( $(date +%s) - start )) с"
done
ls -la "$OUT_DIR" | tail -5
