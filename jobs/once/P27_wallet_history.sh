#!/usr/bin/env bash
# timeout_min: 110
# Вся история кошелька 0x3048d653...7537 (x-MoneyForWhiskas) через data-api /activity: по окнам и по дням.
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
nice -n 19 "$PYTHON" -u wallet_history.py 0x3048d65321be3497164cdfc2996f94f98a2e7537 --out "$OUT_DIR" \
    --store "$HOME/wallets" --since 2025-01-01 2>&1 | tail -70
ls -la "$OUT_DIR" "$HOME/wallets"
