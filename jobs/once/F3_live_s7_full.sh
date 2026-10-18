#!/usr/bin/env bash
# timeout_min: 60
# v1. Полный разбор живого запуска с переплатой 7 ц (после остановки по общему убытку): путь pnl, вскрытие ордеров, что-если.
set -u
ulimit -v 2300000 2>/dev/null || true
D=/home/lab/incoming/bot_data_c1_s7
[ -d "$D" ] || { echo "нет $D"; exit 0; }
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -6)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
nice -n 19 "$PYTHON" -u btc5m_lab/daypnl_path.py "$D" > "$OUT_DIR/path.txt" 2>&1
echo "== путь pnl, код $?"
head -c 3500 "$OUT_DIR/path.txt" | cut -c1-200
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/live_autopsy.py "$D" --pm-roots $days > "$OUT_DIR/autopsy.txt" 2>&1
echo "== автопсия, код $?"
head -c 3500 "$OUT_DIR/autopsy.txt" | cut -c1-200
