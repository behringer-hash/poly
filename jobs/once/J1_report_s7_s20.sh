#!/usr/bin/env bash
# timeout_min: 60
# Отчёт по двум живым ботам: c1 (доплата 7 ц, порог 3.5, bot_data_c1_w) и c2 (доплата 20 ц, порог 3.5, bot_data_c2):
# путь pnl, статистика ордеров, по этапам (автопсия), разложение «бумага против жизни».
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
for run in bot_data_c1_w bot_data_c2; do
  D=/home/lab/incoming/$run
  echo; echo "################ $run"
  [ -d "$D" ] || { echo "нет $D"; continue; }
  nice -n 19 "$PYTHON" -u btc5m_lab/daypnl_path.py "$D" 2>&1 | cut -c1-200 | head -c 3000
  days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -3)
  # shellcheck disable=SC2086
  nice -n 19 "$PYTHON" -u btc5m_lab/live_autopsy.py "$D" --pm-roots $days 2>&1 | cut -c1-200 | sed -n '/ордеров /,/по часам/p' | head -c 3500
  # shellcheck disable=SC2086
  nice -n 19 "$PYTHON" -u btc5m_lab/live_decompose.py "$D" --pm-roots $days 2>&1 | cut -c1-200 | head -c 2500
done
