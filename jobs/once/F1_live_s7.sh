#!/usr/bin/env bash
# timeout_min: 60
# Разбор второго живого запуска (переплата 7 ц): вскрытие ордеров по этапам и живой pnl, затем что-если при другой переплате.
set -u
ulimit -v 2300000 2>/dev/null || true
D=/home/lab/incoming/bot_data_c1_s7
[ -d "$D" ] || { echo "нет $D"; exit 0; }
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -6)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/live_autopsy.py "$D" --pm-roots $days > "$OUT_DIR/autopsy_s7.txt" 2>&1
echo "== автопсия, код $?"
head -c 4500 "$OUT_DIR/autopsy_s7.txt" | cut -c1-200
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/live_slip_whatif.py "$D" --pm-roots $days > "$OUT_DIR/whatif_s7.txt" 2>&1
echo "== что-если, код $?"
head -c 3500 "$OUT_DIR/whatif_s7.txt" | cut -c1-200
