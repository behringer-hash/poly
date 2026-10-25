#!/usr/bin/env bash
# timeout_min: 180
# Откуда прибыль C1: устаревшая цена или моментум. Выгрузка компактных данных (сигналы при якоре со сдвигом 0-400 мс,
# состояния окна каждые 5 с, живые ордера с книгой сервера после сигнала) в OUT_DIR; статистика считается отдельно.
set -u
ulimit -v 2300000 2>/dev/null || true
days=$(ls -d "$DATA_DIR"/2026-10-* 2>/dev/null | sort)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
dirs=""
for r in bot_data_c1 bot_data_c1_s7 bot_data_c1_w bot_data_c2; do [ -d /home/lab/incoming/$r ] && dirs="$dirs /home/lab/incoming/$r"; done
echo "дни: $(echo $days | wc -w), папки ботов:$dirs"
start=$(date +%s)
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/edge_source.py $days --live-dirs $dirs --out "$OUT_DIR" 2>&1 | cut -c1-220 | tail -c 20000
echo "время: $(( $(date +%s) - start )) с"
ls -la "$OUT_DIR"
