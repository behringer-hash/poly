#!/usr/bin/env bash
# interval_min: 360
# timeout_min: 120
# Проверка вперёд v2: 4 кандидата ЗАФИКСИРОВАНЫ 2026-10-10 ~11:30 UTC по данным до этого момента (job 70_slip_soft);
# оцениваются только окна после 11:30 UTC 10 октября. Покупка и удержание до конца окна (выход смотрим для сравнения).
#   C1: порог 0.03, sigma x1,   переплата 3 ц     C2: порог 0.03, sigma x1.5, переплата 3 ц
#   C3: порог 0.02, sigma x1.5, переплата 3 ц     C4: порог 0.03, sigma x2,   переплата 5 ц
# Задержка ордера 200 и 300 мс. Источник Bybit (середина книги).
set -u
SINCE=1791631800
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -3)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
for cand in "0.03 1 3" "0.03 1.5 3" "0.02 1.5 3" "0.03 2 5"; do
  set -- $cand
  echo "=== порог $1, sigma x$2, переплата $3 ц"
  # shellcheck disable=SC2086
  "$PYTHON" btc5m_lab/replay.py $days --source bybit --latencies 200,300 --thr "$1" --sigma-mult "$2" \
      --slips "$3" --exit-s 5 --since $SINCE > "$OUT_DIR/fwd2_thr$1_s$2_slip$3.txt" 2>&1
  tail -n 4 "$OUT_DIR/fwd2_thr$1_s$2_slip$3.txt"
done
