#!/usr/bin/env bash
# interval_min: 720
# timeout_min: 60
# Сверка настоящего движка paper.py (виртуальное время) с реплеем на сегодняшних данных: сигналы и доли исполнений.
set -u
day=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -1)
[ -z "$day" ] && { echo "нет данных"; exit 0; }
"$PYTHON" btc5m_lab/fidelity_check.py "$day" --sources bybit,coinbase --primary bybit --thr 0.03 > "$OUT_DIR/fidelity_bybit.txt" 2>&1
cat "$OUT_DIR/fidelity_bybit.txt"
