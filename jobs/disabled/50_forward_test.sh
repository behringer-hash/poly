#!/usr/bin/env bash
# interval_min: 720
# timeout_min: 90
# Проверка вперёд: варианты зафиксированы ЗАРАНЕЕ по данным до 2026-10-09 06:47 UTC (job 40_replay_exit), оцениваются только окна
# после 06:50 UTC, которые при выборе не использовались. Источник Bybit (середина книги), выход продажей через 5 с.
#   A: порог 0.03, sigma x2     B: порог 0.05, sigma x1.5     L = 200 и 300 мс, переплата 0 и 2 цента.
set -u
SINCE=1791528600
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -3)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
for cfg in "0.03 2" "0.05 1.5"; do
  set -- $cfg
  echo "=== порог $1, sigma x$2"
  # shellcheck disable=SC2086
  "$PYTHON" btc5m_lab/replay.py $days --source bybit --latencies 200,300 --thr "$1" --sigma-mult "$2" \
      --slip-c 0,2 --exit-s 5 --since $SINCE > "$OUT_DIR/forward_thr$1_s$2.txt" 2>&1
  sed -n '/досрочный/,$p' "$OUT_DIR/forward_thr$1_s$2.txt" | head -12
done
