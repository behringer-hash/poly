#!/usr/bin/env bash
# timeout_min: 110
# Стратегия 4: честная симуляция модели «v2-типа» — для каждого дня модель, обученная на 9 остальных днях
# (models/lodo/sig_lodo_<день>.npz); варианты F0 (прогноз >= 5 ц + свежий ход BTC), F3 (без фильтра хода), S3 (порог 3, +1 ц).
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
start=$(date +%s)
for b in 2026-10-16 2026-10-17 2026-10-18 2026-10-19 2026-10-20 2026-10-21 2026-10-26 2026-10-27 2026-10-28 2026-10-29; do
  [ -d "$DATA_DIR/$b" ] || continue
  nice -n 19 "$PYTHON" -u -W ignore mm_map.py "$DATA_DIR/$b" --out "$OUT_DIR" --model "models/lodo/sig_lodo_$b.npz" \
      --variants F0_v1,F3_v1_nofresh,S3_th3_imp 2>&1 | tail -7
  echo "  прошло $(( $(date +%s) - start )) с"
  [ $(( $(date +%s) - start )) -gt 6000 ] && { echo "стоп по времени"; break; }
done
exit 0
