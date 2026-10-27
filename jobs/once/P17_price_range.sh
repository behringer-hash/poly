#!/usr/bin/env bash
# timeout_min: 180
# Ограничение цены покупки 0,20-0,90 (bid растущей стороны и цена заявки), профиль Токио, вся запись:
#  1) рабочее правило бота (3 ц - ask, 6 ц - ask+1) без ограничения (t9u) и с ограничением (t9r), сведение resp / 0,5 с / 1 с;
#  2) сетка P16 (пороги 3 и 6 ц, ask+0..5, resp / 0,5 / 1 / 1,5 с) с ограничением (t10r) - сравнение с P16 (t8).
set -u
ulimit -v 3000000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
start=$(date +%s)
days=$(ls -d "$DATA_DIR"/2026-1* 2>/dev/null | sort)
for d in $days; do
  for tag in t9u t9r; do
    pr=""; [ "$tag" = t9r ] && pr="--price-range 0.2 0.9"
    nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig3.py "$d" --out "$OUT_DIR" --tag $tag --profiles tokyo --tiers 0.03 0.06 \
        --dms resp f500 f1000 $pr 2>&1 | cut -c1-200 | tail -2
  done
  nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig3.py "$d" --out "$OUT_DIR" --tag t10r --profiles tokyo --fair 0.03 0.06 \
      --modes ask0 ask1p ask2p ask3p ask4p ask5p --dms resp f500 f1000 f1500 --price-range 0.2 0.9 2>&1 | cut -c1-200 | tail -2
  echo "  прошло $(( $(date +%s) - start )) с"
done
