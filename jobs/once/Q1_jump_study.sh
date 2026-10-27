#!/usr/bin/env bash
# timeout_min: 170
# Природа скачков BTC и реакция токенов (btc5m_lab/jump_study.py): распределения изменений цены, частота скачков,
# таблица событий с путём BTC на всех биржах и книги токена. Все дни записи. Выход: js_* в OUT_DIR.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/2026-1* 2>/dev/null | sort)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
start=$(date +%s)
for d in $days; do
  nice -n 19 "$PYTHON" -u btc5m_lab/jump_study.py "$d" --out "$OUT_DIR" 2>&1 | cut -c1-300 | tail -6
  echo "  прошло $(( $(date +%s) - start )) с"
done
ls -la "$OUT_DIR" | awk '{print $5, $9}' | tail -60
