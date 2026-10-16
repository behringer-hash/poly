#!/usr/bin/env bash
# timeout_min: 30
# Живые ордера C1 при большей переплате (k=0..10 ц к фактическому лимиту) по книге сервера и фактической задержке каждого ордера.
set -u
ulimit -v 2300000 2>/dev/null || true
[ -d /home/lab/incoming/bot_data_c1 ] || { echo "нет /home/lab/incoming/bot_data_c1"; exit 0; }
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -6)
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/live_slip_whatif.py /home/lab/incoming/bot_data_c1 --pm-roots $days > "$OUT_DIR/whatif.txt" 2>&1
echo "код $?"
head -c 7000 "$OUT_DIR/whatif.txt" | cut -c1-230
