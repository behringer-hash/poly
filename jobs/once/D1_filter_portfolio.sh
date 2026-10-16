#!/usr/bin/env bash
# timeout_min: 90
# v2: память (не держим все дни), условная задержка, возвращено в D1 только 6 дней
# Отбор сигналов по прогнозу дожития и простое правило (возраст верха книги, число обновлений) в портфеле с правилами бота и
# живой задержкой (распределение взято у исполнимых при приходе живых ордеров). Оценка на поздних окнах.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -6)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
live=""; [ -d /home/lab/incoming/bot_data_c1 ] && live="--live-data /home/lab/incoming/bot_data_c1"
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/filter_portfolio.py $days --source bybit $live > "$OUT_DIR/filter_portfolio.txt" 2>&1
echo "код $?"
head -c 9000 "$OUT_DIR/filter_portfolio.txt" | cut -c1-230
