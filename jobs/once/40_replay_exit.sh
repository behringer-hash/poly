#!/usr/bin/env bash
# timeout_min: 120
# Вход по сигналу «anchor» и ДОСРОЧНЫЙ выход (продажа тейкером по bid с комиссией) через 2/5/10/30/60 с, реальное состояние книги
# Polymarket в момент матча. Источники: Bybit (середина книги), Coinbase, Binance futures; последние 2 дня записи.
# В отчёте: топ вариантов, проверка на отложенной выборке (подбор на первой половине окон, оценка на второй).
set -u
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -2)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
for src in bybit coinbase binance_fut; do
  echo "=== $src"
  # shellcheck disable=SC2086
  "$PYTHON" btc5m_lab/replay.py $days --source "$src" --latencies 200,300,450 --thr 0.02,0.03,0.05 \
      --sigma-mult 1,1.5,2 --slip-c 0,2 --exit-s 2,5,10,30,60 > "$OUT_DIR/exit_$src.txt" 2>&1
  sed -n '/досрочный/,$p' "$OUT_DIR/exit_$src.txt" | head -60
done
