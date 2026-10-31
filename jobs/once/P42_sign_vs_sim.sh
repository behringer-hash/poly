#!/usr/bin/env bash
# timeout_min: 40
# Стратегия 4: сверка бота в режиме sign (Ирландия, 30.10 14:15 UTC - 31.10) с симуляцией правила бота R6_ie_v2
# на тех же окнах: каждая заявка симуляции (orders_*.csv.gz) и прогноз (scores_*.csv.gz) для сравнения с журналами бота.
set -u
ulimit -v 4000000 2>/dev/null || true
cd btc5m_lab || exit 1
nice -n 19 "$PYTHON" -u -W ignore mm_map.py "$DATA_DIR/2026-10-30" --out "$OUT_DIR" --model models/sig3s_v2.npz \
    --variants R6_ie_v2 --dump-orders R6_ie_v2 --dump-scores R6_ie_v2 --w-from 1793369700 2>&1 | tail -4
day=2026-10-31
hh=$(date -u +%H)
tmp=$(mktemp -d); mkdir -p "$tmp/$day"
for f in "$DATA_DIR/$day"/*; do
  case "$(basename "$f")" in *_"$hh".csv) continue;; esac
  ln -s "$f" "$tmp/$day/"
done
echo "31.10 до $hh:00 UTC"
nice -n 19 "$PYTHON" -u -W ignore mm_map.py "$tmp/$day" --out "$OUT_DIR" --model models/sig3s_v2.npz \
    --variants R6_ie_v2 --dump-orders R6_ie_v2 --dump-scores R6_ie_v2 2>&1 | tail -4
rm -rf "$tmp"
ls -la "$OUT_DIR"
exit 0
