#!/usr/bin/env bash
# timeout_min: 300
# Мейкер по карте потока (mm_map.py): лесенка от лучшего bid (0-3 ц) на обе стороны + снятие «ударяемой» стороны по
# ходу фьючерса Binance (>= 4 $ за 300 мс, отмена через 175 мс), варианты A0-A8, все дни записи сборщика.
set -u
ulimit -v 3000000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
cd btc5m_lab || exit 1
start=$(date +%s)
for d in $(ls -d "$DATA_DIR"/2026-10-* 2>/dev/null | sort); do
  [ "$(basename "$d")" = "$(date -u +%F)" ] && continue          # текущий день не полный
  nice -n 19 "$PYTHON" -u mm_map.py "$d" --out "$OUT_DIR" 2>&1 | tail -13
  echo "  прошло $(( $(date +%s) - start )) с"
done
ls -la "$OUT_DIR" | tail -5
