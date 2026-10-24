#!/usr/bin/env bash
# timeout_min: 15
# Замечание эксперта: http_ms исполненных ордеров может включать ожидание хэша транзакции (post_order опрашивает get_trades до 30 с).
set -u
dirs=""
for r in bot_data_c1 bot_data_c1_s7 bot_data_c1_w bot_data_c2; do [ -d /home/lab/incoming/$r ] && dirs="$dirs /home/lab/incoming/$r"; done
[ -z "$dirs" ] && { echo "нет данных ботов"; exit 0; }
cd btc5m_lab || exit 0
# shellcheck disable=SC2086
"$PYTHON" -u live_http_check.py $dirs 2>&1 | cut -c1-220 | head -c 7000
