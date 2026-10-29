#!/usr/bin/env bash
# timeout_min: 110
# mm_map, варианты M*: мейкер как x-MoneyForWhiskas — бид только по лучшему bid и только на токен, выросший >= 3 ц за 10 с,
# снятие по ходу BTC против (>= $3 за 300 мс) на фьючерсе Binance, Bybit или Coinbase; + контроли (без фильтра хода,
# первые в очереди, обратный ход). Дни 28, 27, 26, 25, 24, 23, 22.10 (свежие первыми; при обрыве по времени — что успели).
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
start=$(date +%s)
V=M0_mom,M1_nomom,M2_mom_front,M3_mom5s2c,M4_mom_keep,M5_mom_fut,M6_mom_L01,M7_antimom,M8_nomom_front
for b in 2026-10-28 2026-10-27 2026-10-26 2026-10-25 2026-10-24 2026-10-23 2026-10-22; do
  [ -d "$DATA_DIR/$b" ] || continue
  nice -n 19 "$PYTHON" -u mm_map.py "$DATA_DIR/$b" --out "$OUT_DIR" --variants $V 2>&1 | tail -13
  echo "  прошло $(( $(date +%s) - start )) с"
  [ $(( $(date +%s) - start )) -gt 5700 ] && { echo "стоп по времени"; break; }
done
