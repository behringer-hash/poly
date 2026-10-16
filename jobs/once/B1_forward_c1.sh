#!/usr/bin/env bash
# timeout_min: 60
# v2: лимит памяти 2.3 ГБ (1.5 мало для pandas + данных дня), по одному дню освобождаем память
# Проверка вперёд: C1 (Bybit, порог 0.03, sigma x1) на данных ПОСЛЕ 12:00 UTC 13 октября (после всех выборов вариантов и анализов A1/A2).
# Показываем задержки 250/300/400 и переплаты 0/3/5 ц; результат по дням, чтобы видеть устойчивость.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -4)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/replay.py $days --source bybit --latencies 250,300,400 --thr 0.03 --sigma-mult 1 --slips 0,3,5 --exit-s 5 \
    --since 1791892800 > "$OUT_DIR/forward_c1.txt" 2>&1
echo "код $?"
head -c 6000 "$OUT_DIR/forward_c1.txt"
