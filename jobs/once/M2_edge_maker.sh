#!/usr/bin/env bash
# timeout_min: 120
# Вход лимитной заявкой (мейкером) после сигнала C1 и в контрольные моменты без сигнала: исполнение по сделкам рынка
# с очередью. Выгрузка maker_<день>.csv.gz в OUT_DIR; статистика считается отдельно.
set -u
ulimit -v 2300000 2>/dev/null || true
days=$(ls -d "$DATA_DIR"/2026-10-* 2>/dev/null | sort)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
start=$(date +%s)
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/edge_maker.py $days --out "$OUT_DIR" 2>&1 | cut -c1-220 | tail -c 20000
echo "время: $(( $(date +%s) - start )) с"
ls -la "$OUT_DIR"
