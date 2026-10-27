#!/usr/bin/env bash
# timeout_min: 120
# Ход Binance -> лимит на покупку растущего токена: цена заявки bid / ask-1 ц / обычный лимит по ask / post-only по ask
# (btc5m_lab/mm_trig2.py), окно 100 мс, «кто первый», пороги 2 ц, 5 ц, $5; Токио и Стокгольм. Дни до 21.10 (26.10+ - отложены).
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/2026-1* 2>/dev/null | sort | grep -v 2026-10-2[2-9])
[ -z "$days" ] && { echo "нет данных"; exit 0; }
start=$(date +%s)
for d in $days; do
  nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig2.py "$d" --out "$OUT_DIR" 2>&1 | cut -c1-200 | tail -26
  echo "  прошло $(( $(date +%s) - start )) с"
done
