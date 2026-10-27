#!/usr/bin/env bash
# timeout_min: 150
# Живой запуск 27.10 показал: заявка сводится через 0,5-1,5 с после отправки, и позже всего - когда цена уходит.
# Проверка на всей записи: выгодна ли покупка с переплатой ask + 0..5 ц при сведении ровно через 0,5 / 1 / 1,5 с после
# решения (dm f500 / f1000 / f1500) и в модели resp; пороги 3 ц и 6 ц; профиль Токио.
set -u
ulimit -v 3000000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
start=$(date +%s)
days=$(ls -d "$DATA_DIR"/2026-1* 2>/dev/null | sort)
for d in $days; do
  nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig3.py "$d" --out "$OUT_DIR" --tag t8 --profiles tokyo --fair 0.03 0.06 \
      --modes ask0 ask1p ask2p ask3p ask4p ask5p --dms resp f500 f1000 f1500 2>&1 | cut -c1-200 | tail -3
  echo "  прошло $(( $(date +%s) - start )) с"
done
