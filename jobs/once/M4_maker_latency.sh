#!/usr/bin/env bash
# timeout_min: 90
# Чувствительность мейкерского входа после сигнала C1 к задержке постановки заявки: 25/50/100/200/400 мс,
# решение сразу по сигналу, заявка живёт до 5 с. Выгрузка maker_<день>.csv.gz в OUT_DIR.
set -u
ulimit -v 2300000 2>/dev/null || true
days=$(ls -d "$DATA_DIR"/2026-10-* 2>/dev/null | sort)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
start=$(date +%s)
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/edge_maker.py $days --out "$OUT_DIR" --place-ms 25,50,100,200,400 --ds 0 \
    --modes join,improve --life-ms 5000 --no-ctl 2>&1 | cut -c1-220 | tail -c 20000
echo "время: $(( $(date +%s) - start )) с"
ls -la "$OUT_DIR"
