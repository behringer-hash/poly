#!/usr/bin/env bash
# timeout_min: 40
# Запись сборщика за время живых запусков 2 и 3 бота стратегии 3 (27.10 19:40 - 28.10 01:00 UTC и 28.10 06:10 - сейчас):
# книга Polymarket (время сервера), сделки Binance - для проверки переплаты ask + k по фактическому моменту сведения заявок.
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
d27="$DATA_DIR/2026-10-27"; d28="$DATA_DIR/2026-10-28"
[ -d "$d27" ] && nice -n 19 "$PYTHON" -u export_slice.py "$d27" --t0 1793130000 --t1 1793145600 --prefix r3a --out "$OUT_DIR" 2>&1 | tail -6
[ -d "$d28" ] && nice -n 19 "$PYTHON" -u export_slice.py "$d28" --t0 1793145600 --t1 1793149200 --prefix r3b --out "$OUT_DIR" 2>&1 | tail -6
[ -d "$d28" ] && nice -n 19 "$PYTHON" -u export_slice.py "$d28" --t0 1793167800 --t1 $(date +%s) --prefix r4 --out "$OUT_DIR" 2>&1 | tail -12
