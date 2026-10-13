#!/usr/bin/env bash
# timeout_min: 60
# v2: чтение записей игнорирует повторные заголовки (перезапуск сборщика дописывает их в файлы)
# Какой источник сообщает о скачке раньше всех (оси recv и exch). Лимит памяти и низкий приоритет: сервер маленький (1,9 ГБ), на нём живой бот.
set -u
ulimit -v 1500000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -4)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/speed_compare.py $days --sources bybit,bybit_trade,binance_fut,binance,binance_book,coinbase,bitstamp,okx,kraken \
    --N 10,20,30 --W 500,1000 > "$OUT_DIR/speed_sources.txt" 2>&1
echo "код $?"
head -c 12000 "$OUT_DIR/speed_sources.txt"
