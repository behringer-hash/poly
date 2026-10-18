#!/usr/bin/env bash
# timeout_min: 60
# Разложение разрыва «бумага против жизни» на ордерах двух живых запусков (переплата 3 ц и 7 ц).
set -u
ulimit -v 2300000 2>/dev/null || true
days12=$(ls -d "$DATA_DIR"/2026-10-12 "$DATA_DIR"/2026-10-13 2>/dev/null)
days7=$(ls -d "$DATA_DIR"/2026-10-16 "$DATA_DIR"/2026-10-17 "$DATA_DIR"/2026-10-18 2>/dev/null)
if [ -d /home/lab/incoming/bot_data_c1 ] && [ -n "$days12" ]; then
  echo "=== запуск 1 (доплата 3 ц) ==="
  # shellcheck disable=SC2086
  nice -n 19 "$PYTHON" -u btc5m_lab/live_decompose.py /home/lab/incoming/bot_data_c1 --pm-roots $days12 2>&1 | cut -c1-200 | head -c 3500
fi
if [ -d /home/lab/incoming/bot_data_c1_s7 ] && [ -n "$days7" ]; then
  echo; echo "=== запуск 2 (доплата 7 ц) ==="
  # shellcheck disable=SC2086
  nice -n 19 "$PYTHON" -u btc5m_lab/live_decompose.py /home/lab/incoming/bot_data_c1_s7 --pm-roots $days7 2>&1 | cut -c1-200 | head -c 3500
fi
