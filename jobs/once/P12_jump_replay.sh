#!/usr/bin/env bash
# timeout_min: 90
# Бот стратегии 3 (btc5m_jump/jump.py) на записи сборщика: сколько сигналов дал бы его триггер в Стокгольме -
# сверка с n_ev симуляции mm_trig3 (P10: 20.10, P11: 26.10) и выгрузка сигналов рабочей настройки 3 ц / 6 ц.
set -u
ulimit -v 3000000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
start=$(date +%s)
days=$(ls -d "$DATA_DIR"/2026-10-20 "$DATA_DIR"/2026-10-26 2>/dev/null)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
cd btc5m_jump || exit 1
nice -n 19 "$PYTHON" -u tools/replay_day.py $days --out "$OUT_DIR" 2>&1 | cut -c1-400 | tail -30
echo "  прошло $(( $(date +%s) - start )) с"
