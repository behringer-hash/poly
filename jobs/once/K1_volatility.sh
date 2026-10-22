#!/usr/bin/env bash
# timeout_min: 20
# Колебания pnl: распределение результатов окон живых ботов (20 ц и 7 ц), моделирование суток и недели, вероятность стопа.
set -u
for run in bot_data_c2 bot_data_c1_w; do
  D=/home/lab/incoming/$run
  [ -d "$D" ] || { echo "нет $D"; continue; }
  echo; echo "################ $run"
  nice -n 19 "$PYTHON" -u btc5m_lab/live_pnl_volatility.py "$D" --stop 35 2>&1 | cut -c1-230 | head -c 3500
done
