#!/usr/bin/env bash
# timeout_min: 20
# Проба ленты сделок data-api с кошельками: поля, takerOnly false/true, постраничность; сверка с pm_trades сборщика
# по хэшу транзакции (3 окна 28.10 после 06:10 UTC).
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
d28="$DATA_DIR/2026-10-28"
nice -n 19 "$PYTHON" -u tape_fetch.py "$d28" --out "$OUT_DIR" --wfrom 1793170800 --first 3 --modes false,true --probe 2>&1 | tail -40
ls -la "$OUT_DIR"
