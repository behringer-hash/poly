#!/usr/bin/env bash
# timeout_min: 170
# Стратегия 4 с реальными задержками прихода данных (замер latency_probe: Ирландия 29.10, Токио 26.10).
# Каждый день торгует модель «без этого дня» (models/lodo), как P38. F0 - как в P38 (данные мгновенно, контроль);
# R0 Ирландия (решение по данным к t-150 мс, заявка 40 мс); R1/R2 - ждать данные 200/250 мс; R3 - заявка 100 мс;
# R4 Токио (заявка 150 мс); R5 Ирландия без фильтра свежего хода BTC.
set -u
ulimit -v 4000000 2>/dev/null || true
cd btc5m_lab || exit 1
start=$(date +%s)
for b in 2026-10-16 2026-10-17 2026-10-18 2026-10-19 2026-10-20 2026-10-21 2026-10-26 2026-10-27 2026-10-28 2026-10-29; do
  [ -d "$DATA_DIR/$b" ] || continue
  nice -n 19 "$PYTHON" -u -W ignore mm_map.py "$DATA_DIR/$b" --out "$OUT_DIR" --model "models/lodo/sig_lodo_$b.npz" \
      --variants F0_v1,R0_ie,R1_ie_lat200,R2_ie_lat250,R3_ie_place100,R4_tyo,R5_ie_nofresh 2>&1 | tail -13
  echo "  прошло $(( $(date +%s) - start )) с"
  [ $(( $(date +%s) - start )) -gt 9300 ] && { echo "стоп по времени"; break; }
done
exit 0
