#!/usr/bin/env bash
# timeout_min: 10
# Путь дневного pnl второго живого запуска: почему сработал стоп по убытку.
set -u
D=/home/lab/incoming/bot_data_c1_s7
[ -d "$D" ] || { echo "нет $D"; exit 0; }
"$PYTHON" -u btc5m_lab/daypnl_path.py "$D" 2>&1 | cut -c1-200 | head -c 6000
