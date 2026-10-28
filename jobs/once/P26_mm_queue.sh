#!/usr/bin/env bash
# timeout_min: 110
# mm_map: то же правило A0 при разном месте в очереди (в конце / половина / первые) + разбивка исполнений по типу
# (по уровню / сквозь) и по объёму впереди; 4 дня (15, 18, 20, 26.10).
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
start=$(date +%s)
for b in 2026-10-15 2026-10-18 2026-10-20 2026-10-26; do
  [ -d "$DATA_DIR/$b" ] || continue
  nice -n 19 "$PYTHON" -u mm_map.py "$DATA_DIR/$b" --out "$OUT_DIR" \
      --variants Q0_back,Q1_half,Q2_front,Q2_front_noprot,Q2_front_L123 2>&1 | tail -9
  echo "  прошло $(( $(date +%s) - start )) с"
done
