#!/usr/bin/env bash
# timeout_min: 150
# Порог сигнала от -1 до 3,5 ц и три цены заявки (лучший bid, bid + 1 ц, ask в момент сигнала): выгрузка trig_*.csv.gz.
set -u
ulimit -v 2300000 2>/dev/null || true
days=$(ls -d "$DATA_DIR"/2026-10-* 2>/dev/null | sort)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
start=$(date +%s)
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/edge_trigger.py $days --out "$OUT_DIR" 2>&1 | cut -c1-260 | tail -c 20000
echo "время: $(( $(date +%s) - start )) с"
du -sh "$OUT_DIR"; ls "$OUT_DIR" | wc -l
