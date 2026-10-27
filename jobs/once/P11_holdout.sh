#!/usr/bin/env bash
# timeout_min: 60
# Отложенная проверка на данных коллектора с 26.10 (не использовались в подборе): конфигурации зафиксированы заранее -
# основная fair 6 ц + лимит ask+1; для сравнения fair 5 ц ask+1 и fair 3 ц ask (слой объёма). Модель сведения resp.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
start=$(date +%s)
days=$(ls -d "$DATA_DIR"/2026-10-2[6-9] "$DATA_DIR"/2026-10-3* "$DATA_DIR"/2026-11-* 2>/dev/null | sort)
for d in $days; do
  echo "== $(basename $d): файлов pm_top $(ls $d | grep -c pm_top), bnf_agg $(ls $d | grep -c bnf_agg), bn_agg $(ls $d | grep -c bn_agg)"
  nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig3.py "$d" --out "$OUT_DIR" --tag t5 --fair 0.03 0.05 0.06 \
      --modes ask0 ask1p --dms resp 2>&1 | cut -c1-200 | tail -20
  echo "  прошло $(( $(date +%s) - start )) с"
done
