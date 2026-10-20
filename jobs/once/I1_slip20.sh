#!/usr/bin/env bash
# timeout_min: 120
# Доплата до 20 ц: реплей по шести дням (задержка из живых ордеров) и пересчёт живых ордеров обоих запусков (k = добавка к фактическому лимиту: запуск 1 лимит +3 ц, запуск 2 +7 ц).
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
A=/home/lab/incoming/bot_data_c1; B=/home/lab/incoming/bot_data_c1_s7
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -6)
echo "=== реплей по шести дням, доплата 0-20 ц ==="
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/slip_by_day.py $days --live-data "$B" --source bybit > "$OUT_DIR/replay20.txt" 2>&1
echo "код $?"
sed -n '/доля исполнений по дням/,/ц на исполнение ===/p;/все дни вместе/,/по силе сигнала/p' "$OUT_DIR/replay20.txt" | cut -c1-200 | head -c 4500
for run in "$A" "$B"; do
  echo; echo "=== живые ордера: $run ==="
  d12=$(ls -d "$DATA_DIR"/2026-10-12 "$DATA_DIR"/2026-10-13 2>/dev/null); d7=$(ls -d "$DATA_DIR"/2026-10-16 "$DATA_DIR"/2026-10-17 "$DATA_DIR"/2026-10-18 2>/dev/null)
  pm=$d7; [ "$run" = "$A" ] && pm=$d12
  # shellcheck disable=SC2086
  nice -n 19 "$PYTHON" -u btc5m_lab/live_slip_whatif.py "$run" --pm-roots $pm 2>&1 | cut -c1-200 | head -c 2800
done
