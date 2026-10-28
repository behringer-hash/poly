#!/usr/bin/env bash
# timeout_min: 60
# Устойчивость главных выводов P22/P23b по дням: мейкеры по глубине, минута отсчёта, ход BTC, «крупные мейкеры <- редкие
# тейкеры»; тейкеры по ярусам.
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
nice -n 19 "$PYTHON" -u -W ignore flow_wallets.py daily --store "$HOME/flow" --out "$OUT_DIR" 2>&1 | tee "$OUT_DIR/daily.txt" | tail -3
