#!/usr/bin/env bash
# timeout_min: 60
# Окна 29.10 с 00:00 UTC до текущего момента заново, с доп. источниками BTC (спот Binance, OKX, bookTicker фьючерса)
# для поштучного разбора кошелька 0x3048...7537 (замена P30).
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
nice -n 19 "$PYTHON" -u -W ignore window_export.py "$DATA_DIR/2026-10-29" --wallet 0x3048d65321be3497164cdfc2996f94f98a2e7537 \
    --wfrom 1793232000 --wto $(date +%s) --out "$OUT_DIR" 2>&1 | tail -8
du -sh "$OUT_DIR"
