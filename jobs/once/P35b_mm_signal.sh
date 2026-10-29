#!/usr/bin/env bash
# timeout_min: 110
# mm_map, варианты S*: мейкер по сигналу модели sig3s_v1 (прогноз хода mid за 3 с; обучена локально на 28–29.10):
# заявка только на постановку по лучшему bid токена при прогнозе >= порога, короткая жизнь, снятие при падении прогноза
# и по ходу BTC против на любой из трёх бирж. Дни 26–29.10 (28–29 — дни обучения модели).
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
start=$(date +%s)
V=S0_th3,S1_th2,S2_th5,S3_th3_imp,S4_th3_front,S5_th3_life05,S6_th3_life5,S7_th3_noprot,S8_th3_lat300,S9_th5_imp
for b in 2026-10-26 2026-10-27 2026-10-28 2026-10-29; do
  [ -d "$DATA_DIR/$b" ] || continue
  nice -n 19 "$PYTHON" -u -W ignore mm_map.py "$DATA_DIR/$b" --out "$OUT_DIR" --variants $V 2>&1 | tail -14
  echo "  прошло $(( $(date +%s) - start )) с"
  [ $(( $(date +%s) - start )) -gt 5700 ] && { echo "стоп по времени"; break; }
done
