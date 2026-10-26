#!/usr/bin/env bash
# timeout_min: 170
# P4 = P3 + очередь «back» по верху книги сервера (снимки глубины раз в 500 мс занижали очередь). Симуляция простого маркет-мейкера (btc5m_lab/mm_sim.py): заявки в лучших bid Up и Down, очередь конец/начало,
# снятие по сигналу Bybit (нет / 3 ц / 1,5 ц), лимит остатка 10 шейров. Выход: mmwin_/mmfill_<день>.csv.gz в OUT_DIR.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/2026-1* 2>/dev/null | sort)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
start=$(date +%s)
for d in $(echo $days | tr " " "\n" | grep -v 2026-10-26); do
  nice -n 19 "$PYTHON" -u btc5m_lab/mm_sim.py "$d" --out "$OUT_DIR" 2>&1 | cut -c1-300 | tail -12
done
echo "время: $(( $(date +%s) - start )) с"
ls -la "$OUT_DIR"
