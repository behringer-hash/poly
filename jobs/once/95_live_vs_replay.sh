#!/usr/bin/env bash
# timeout_min: 30
# Каждый живой ордер C1 против записанной книги Polymarket: мог ли он исполниться при задержке 100-700 мс, время «убегания» цены за лимит.
# Данные бота скопированы пользователем в /home/lab/incoming/bot_data_c1 (остаются на сервере, в отчёт идёт только сводка).
set -u
[ -d /home/lab/incoming/bot_data_c1 ] || { echo "нет /home/lab/incoming/bot_data_c1"; exit 0; }
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -2)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
# shellcheck disable=SC2086
"$PYTHON" btc5m_lab/live_vs_replay.py /home/lab/incoming/bot_data_c1 --pm-roots $days --out "$OUT_DIR/per_order.csv" \
    > "$OUT_DIR/live_vs_replay.txt" 2>&1
head -c 6000 "$OUT_DIR/live_vs_replay.txt"
