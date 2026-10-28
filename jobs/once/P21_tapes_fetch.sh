#!/usr/bin/env bash
# timeout_min: 300
# 1) Копия сырых данных сборщика 15–21.10 в ~/archive_data (сервер удаляет данные старше KEEP_DAYS=14 дней;
#    15.10 удалится ~29.10). Только копирование, ничего не удаляется.
# 2) Ленты сделок с кошельками (data-api /trades, takerOnly false и true) по всем окнам дней записи сборщика ->
#    ~/tapes/tape_<день>.csv.gz (в git не попадают). В отчёт - сводка по дням.
set -u
ulimit -v 3000000 2>/dev/null || true
ARCH="$HOME/archive_data"; TAPES="$HOME/tapes"
mkdir -p "$ARCH" "$TAPES"
echo "== копия старых дней"
for d in $(ls -d "$DATA_DIR"/2026-10-1[5-9] "$DATA_DIR"/2026-10-2[01] 2>/dev/null); do
  b=$(basename "$d")
  if [ -d "$ARCH/$b" ]; then echo "  $b уже есть"; continue; fi
  cp -a "$d" "$ARCH/$b" && echo "  $b: $(du -sh "$ARCH/$b" | cut -f1)"
done
df -h "$HOME" | tail -1
echo "== ленты"
cd btc5m_lab || exit 1
start=$(date +%s)
for d in $(ls -d "$DATA_DIR"/2026-10-* 2>/dev/null | sort); do
  b=$(basename "$d")
  if [ -f "$TAPES/tape_${b}_windows.csv" ] && [ "$b" != "$(date -u +%F)" ]; then echo "  $b уже есть"; continue; fi
  nice -n 19 "$PYTHON" -u tape_fetch.py "$d" --out "$TAPES" --modes false,true --limit 1000 --threads 3 2>&1 | tail -2
  cp "$TAPES/tape_${b}_windows.csv" "$OUT_DIR/" 2>/dev/null
  echo "  прошло $(( $(date +%s) - start )) с"
done
ls -la "$TAPES"; du -sh "$TAPES" "$ARCH"
