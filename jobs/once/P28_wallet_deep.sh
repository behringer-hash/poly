#!/usr/bin/env bash
# timeout_min: 110
# Исполнения кошелька 0x3048d653...7537 за дни записи сборщика с мс-контекстом (книга, BTC 5 источников, поток,
# позиция) + контрольная выборка 3% чужих тейкерских заявок.
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
nice -n 19 "$PYTHON" -u -W ignore wallet_deep.py 0x3048d65321be3497164cdfc2996f94f98a2e7537 --flow "$HOME/flow" \
    --raw "$DATA_DIR" "$HOME/archive_data" --out "$OUT_DIR" --ctrl 0.03 2>&1 | tail -20
du -sh "$OUT_DIR"
