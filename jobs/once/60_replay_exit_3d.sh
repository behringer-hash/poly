#!/usr/bin/env bash
# timeout_min: 150
# Повтор проверки досрочного выхода на всех накопленных данных (последние 3 суток, ~500 окон): Bybit, Coinbase, Binance futures.
# В таблицах теперь есть число исполнений (исп_шт) и разбивка цсигнал по дням.
set -u
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -3)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
for src in bybit coinbase binance_fut; do
  echo "=== $src"
  # shellcheck disable=SC2086
  "$PYTHON" btc5m_lab/replay.py $days --source "$src" --latencies 200,300,450 --thr 0.02,0.03,0.05 \
      --sigma-mult 1,1.5,2 --slip-c 0,2 --exit-s 2,5,10,30,60 > "$OUT_DIR/exit3d_$src.txt" 2>&1
  sed -n '/досрочный/,$p' "$OUT_DIR/exit3d_$src.txt" | head -50
done
