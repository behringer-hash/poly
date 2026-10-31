#!/usr/bin/env bash
# timeout_min: 60
# Стратегия 3 (рабочее правило бота: 3 ц - ask, 6 ц - ask+1) на 30.10 и 31.10 (до текущего часа), профили Ирландия и Токио,
# сведение resp / через 0,5 с / через 1 с после решения - для сверки с запуском бота в режиме sign в Ирландии
# (30.10 17:44 - 31.10 06:00 UTC). Выход t11h_* по часам.
set -u
ulimit -v 3000000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig3.py "$DATA_DIR/2026-10-30" --out "$OUT_DIR" --tag t11 --profiles ireland tokyo \
    --tiers 0.03 0.06 --dms resp f500 f1000 2>&1 | cut -c1-200 | tail -3
day=2026-10-31; hh=$(date -u +%H)
tmp=$(mktemp -d); mkdir -p "$tmp/$day"
for f in "$DATA_DIR/$day"/*; do case "$(basename "$f")" in *_"$hh".csv) continue;; esac; ln -s "$f" "$tmp/$day/"; done
nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig3.py "$tmp/$day" --out "$OUT_DIR" --tag t11 --profiles ireland tokyo \
    --tiers 0.03 0.06 --dms resp f500 f1000 2>&1 | cut -c1-200 | tail -3
rm -rf "$tmp"
ls -la "$OUT_DIR"
exit 0
