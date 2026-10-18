#!/usr/bin/env bash
# timeout_min: 20
# Подгруппы живых ордеров (оба запуска): где прибыль, где убыток. Без обращения к книге, только данные бота.
set -u
A=/home/lab/incoming/bot_data_c1; B=/home/lab/incoming/bot_data_c1_s7
[ -d "$A" ] && [ -d "$B" ] || { echo "нет папок бота"; exit 0; }
"$PYTHON" -u btc5m_lab/live_subgroups.py "$A" "$B" 2>&1 | cut -c1-230 | head -c 9000
