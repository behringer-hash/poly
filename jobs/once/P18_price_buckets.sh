#!/usr/bin/env bash
# timeout_min: 150
# Подбор ценовых границ по данным: рабочее правило бота (3 ц - ask, 6 ц - ask+1) без ценового фильтра (bid растущей
# стороны 0,01-0,99), результат по корзинам цены с шагом 0,05 (pb: 0 = bid < 0,05, 1 = 0,05-0,10, ..., 19 = >= 0,95),
# сведение resp / 0,5 с / 1 с, профиль Токио, вся запись.
set -u
ulimit -v 3000000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
start=$(date +%s)
E=$(python3 -c "print(' '.join(f'{x/100:.2f}' for x in range(5, 100, 5)))")
echo "границы корзин: $E"
for d in $(ls -d "$DATA_DIR"/2026-1* 2>/dev/null | sort); do
  nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig3.py "$d" --out "$OUT_DIR" --tag t11 --profiles tokyo --tiers 0.03 0.06 \
      --dms resp f500 f1000 --price-range 0.01 0.99 --p-edges $E 2>&1 | cut -c1-200 | tail -2
  echo "  прошло $(( $(date +%s) - start )) с"
done
