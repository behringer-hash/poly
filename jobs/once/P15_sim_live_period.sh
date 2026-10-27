#!/usr/bin/env bash
# timeout_min: 60
# Симуляция (mm_trig3, модель resp) на 27.10 - сверка с живым запуском из Токио 16-18 UTC: лимит ask + 0..5 ц,
# пороги 3 ц и 6 ц; почасовой PnL (t7h) позволяет вырезать часы живого запуска.
set -u
ulimit -v 3000000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
d=$(ls -d "$DATA_DIR"/2026-10-27 2>/dev/null)
[ -z "$d" ] && { echo "нет данных"; exit 0; }
nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig3.py "$d" --out "$OUT_DIR" --tag t7 --fair 0.03 0.06 --modes ask0 ask1p ask2p ask3p ask5p --dms resp 2>&1 | cut -c1-200 | tail -25
