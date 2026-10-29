#!/usr/bin/env bash
# timeout_min: 30
# Сводка по истории кошелька 0x3048...: типы событий (в т.ч. MAKER_REBATE / TAKER_REBATE) по дням, размеры, время в окне.
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
nice -n 19 "$PYTHON" -u wallet_hist_stats.py "$HOME/wallets/act_0x3048d653.csv.gz" --out "$OUT_DIR" 2>&1 | tail -120
