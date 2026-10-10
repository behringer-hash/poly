#!/usr/bin/env bash
# timeout_min: 150
# Мягкие варианты (порог 0.01/0.02/0.03, sigma x1/x1.5/x2) и сравнение способов переплаты: фикс. 0-8 центов и от силы сигнала.
# Главная метрика - ц на СИГНАЛ (неисполненный = 0): выгодно ли входить с такой переплатой, а не только прибыль на шейр.
# Два прогона по Bybit: все накопленные дни и только окна после 06:50 UTC 9 октября (не использовались при выборе вариантов).
set -u
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -3)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
for mode in all forward; do
  since=0; [ "$mode" = forward ] && since=1791528600
  echo "=== Bybit, $mode"
  # shellcheck disable=SC2086
  "$PYTHON" btc5m_lab/replay.py $days --source bybit --latencies 200,300 --thr 0.01,0.02,0.03 --sigma-mult 1,1.5,2 \
      --slips 0,1,2,3,5,8,e:1:1:8,e:0.5:0:6,e:1:2:6 --exit-s 5 --since $since > "$OUT_DIR/slip_bybit_$mode.txt" 2>&1
  head -c 3000 "$OUT_DIR/slip_bybit_$mode.txt"
done
