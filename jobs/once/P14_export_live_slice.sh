#!/usr/bin/env bash
# timeout_min: 30
# Кусок записи сборщика за 27.10 15:55-18:15 UTC (живой запуск бота стратегии 3 из Токио): книга Polymarket (время сервера),
# сделки Binance и Polymarket - для разбора цены токена вокруг живых сигналов локально (btc5m_lab/export_slice.py).
set -u
ulimit -v 3000000 2>/dev/null || true
d=$(ls -d "$DATA_DIR"/2026-10-27 2>/dev/null)
[ -z "$d" ] && { echo "нет данных за 27.10"; exit 0; }
cd btc5m_lab || exit 1
nice -n 19 "$PYTHON" -u export_slice.py "$d" --t0 1793116500 --t1 1793124900 --out "$OUT_DIR" 2>&1 | tail -30
