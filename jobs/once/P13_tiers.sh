#!/usr/bin/env bash
# timeout_min: 120
# Рабочее правило бота стратегии 3 целиком: сдвиг от 3 ц - лимит по ask (слабые), от 6 ц - ask + 1 ц (сильные);
# пауза сильных - между сильными, слабых - после любого сигнала стороны (mm_trig3.py --tiers), модель сведения resp,
# Токио и Стокгольм, все дни записи. Плюс прогон триггера бота (btc5m_jump/tools/replay_day.py) на 20.10 - сверка числа сигналов.
set -u
ulimit -v 3000000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
start=$(date +%s)
days=$(ls -d "$DATA_DIR"/2026-1* 2>/dev/null | sort)
for d in $days; do
  nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig3.py "$d" --out "$OUT_DIR" --tag t6 --tiers 0.03 0.06 --dms resp 2>&1 | cut -c1-200 | tail -12
  echo "  прошло $(( $(date +%s) - start )) с"
done
d20=$(ls -d "$DATA_DIR"/2026-10-20 2>/dev/null)
[ -n "$d20" ] && (cd btc5m_jump && nice -n 19 "$PYTHON" -u tools/replay_day.py "$d20" --out "$OUT_DIR" 2>&1 | cut -c1-300 | tail -6)
echo "  прошло $(( $(date +%s) - start )) с"
