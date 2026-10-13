#!/usr/bin/env bash
# timeout_min: 60
# Калибровка реплея по живому запуску C1 (с ~17:50 UTC 12 октября): при какой задержке матча доля исполнений реплея при переплате +3 ц
# совпадает с живой (8,4%)? Дальше по откалиброванной задержке смотрим, что дала бы большая переплата (5, 8, 12 ц, от силы сигнала).
set -u
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -2)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
since=1791827400
# shellcheck disable=SC2086
"$PYTHON" btc5m_lab/replay.py $days --source bybit --latencies 200,250,300,350,400,500,700 --thr 0.03 --sigma-mult 1 \
    --slips 0,3,5,8,12,e:1:1:8,e:1:2:12 --exit-s 5 --since $since > "$OUT_DIR/calibrate_live.txt" 2>&1
head -c 6000 "$OUT_DIR/calibrate_live.txt"
