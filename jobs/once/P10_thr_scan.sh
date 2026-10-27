#!/usr/bin/env bash
# timeout_min: 120
# Порог чувствительности при откалиброванном моменте сведения (resp - по живым ордерам C1, см. P9):
# ход Binance -> лимит по ask / ask+1 / ask+2, fair 3, 4, 5, 6, 8, 10 ц; Токио и Стокгольм. Дни до 21.10, как в P8/P9.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
start=$(date +%s)
days=$(ls -d "$DATA_DIR"/2026-1* 2>/dev/null | sort | grep -v 2026-10-2[2-9])
for d in $days; do
  nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig3.py "$d" --out "$OUT_DIR" --tag t4 --fair 0.03 0.04 0.05 0.06 0.08 0.10 \
      --modes ask0 ask1p ask2p --dms resp 2>&1 | cut -c1-200 | tail -40
  echo "  прошло $(( $(date +%s) - start )) с"
done
