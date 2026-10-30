#!/usr/bin/env bash
# timeout_min: 60
# Стратегия 4: предварительная проверка вперёд на 30.10 (день ещё не закончен; полный день посчитает
# jobs/recurring/20_fwd_signal_maker.sh после 00:00 UTC). Текущий час (файл пишется) пропускаем.
# v1: F0_v1, F3_v1_nofresh; v2: F1_v2, F2_v2_nofresh, F4_v2_th3, R0_ie и R5_ie_nofresh (правило бота с задержками Ирландии).
set -u
ulimit -v 4000000 2>/dev/null || true
cd btc5m_lab || exit 1
day=2026-10-30
src="$DATA_DIR/$day"
[ -d "$src" ] || { echo "нет $src"; exit 0; }
hh=$(date -u +%H)
tmp=$(mktemp -d)
mkdir -p "$tmp/$day"
for f in "$src"/*; do
  case "$(basename "$f")" in *_"$hh".csv) continue;; esac
  ln -s "$f" "$tmp/$day/"
done
echo "данные $day до $hh:00 UTC, файлов $(ls "$tmp/$day" | wc -l)"
mkdir -p "$OUT_DIR/v1" "$OUT_DIR/v2"
nice -n 19 "$PYTHON" -u -W ignore mm_map.py "$tmp/$day" --out "$OUT_DIR/v1" --model models/sig3s_v1.npz \
    --variants F0_v1,F3_v1_nofresh 2>&1 | tail -6
nice -n 19 "$PYTHON" -u -W ignore mm_map.py "$tmp/$day" --out "$OUT_DIR/v2" --model models/sig3s_v2.npz \
    --variants F1_v2,F2_v2_nofresh,F4_v2_th3,R0_ie,R5_ie_nofresh 2>&1 | tail -10
rm -rf "$tmp"
exit 0
