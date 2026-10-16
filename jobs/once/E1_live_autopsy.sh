#!/usr/bin/env bash
# timeout_min: 30
# Вскрытие живых ордеров C1: на каком этапе умирает ордер (сигнал/отправка/путь/ответ), статусы, ошибки, живой pnl по закрытым окнам.
set -u
ulimit -v 2300000 2>/dev/null || true
[ -d /home/lab/incoming/bot_data_c1 ] || { echo "нет /home/lab/incoming/bot_data_c1"; exit 0; }
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -6)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/live_autopsy.py /home/lab/incoming/bot_data_c1 --pm-roots $days > "$OUT_DIR/autopsy.txt" 2>&1
echo "код $?"
head -c 7000 "$OUT_DIR/autopsy.txt" | cut -c1-230
