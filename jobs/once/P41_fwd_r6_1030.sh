#!/usr/bin/env bash
# timeout_min: 30
# Стратегия 4: R6_ie_v2 (правило бота в Ирландии: модель v2, задержки IE) на 30.10 - дополнение к 20_fwd (с 31.10 входит в него).
set -u
ulimit -v 4000000 2>/dev/null || true
cd btc5m_lab || exit 1
[ -d "$DATA_DIR/2026-10-30" ] || { echo "нет данных"; exit 0; }
nice -n 19 "$PYTHON" -u -W ignore mm_map.py "$DATA_DIR/2026-10-30" --out "$OUT_DIR" --variants R6_ie_v2,F1_v2 2>&1 | tail -6
exit 0
