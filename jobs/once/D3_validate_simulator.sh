#!/usr/bin/env bash
# timeout_min: 90
# Проверка самого симулятора: правила первого живого запуска (пауза 10 с, лимиты) на сигналах того периода против фактических исполнений и pnl;
# заодно повтор отбора на всех днях. Данные бота: /home/lab/incoming/bot_data_c1 (копия).
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -6)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
[ -d /home/lab/incoming/bot_data_c1 ] || { echo "нет /home/lab/incoming/bot_data_c1"; exit 0; }
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/filter_portfolio.py $days --source bybit --live-data /home/lab/incoming/bot_data_c1 --draws 20 > "$OUT_DIR/validate.txt" 2>&1
echo "код $?"
head -c 7000 "$OUT_DIR/validate.txt" | cut -c1-230
