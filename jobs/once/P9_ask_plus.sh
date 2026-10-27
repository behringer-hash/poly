#!/usr/bin/env bash
# timeout_min: 150
# 1) Живые ордера C1 против книги сервера: когда на самом деле сводится тейкерский ордер (btc5m_lab/c1_match_cal.py).
# 2) Ход Binance -> обычный лимит по ask + 0/1/2/3 ц и post-only по ask, три модели момента сведения (btc5m_lab/mm_trig3.py),
#    окно 100 мс, «кто первый», пороги 2 ц, 5 ц, $5; Токио и Стокгольм. Дни до 21.10, как в P8 (26.10+ - отложены).
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
start=$(date +%s)
D=/home/lab/incoming/bot_data_c1_w
cal=$(ls -d "$DATA_DIR"/2026-10-19 "$DATA_DIR"/2026-10-2[0-7] 2>/dev/null | sort)
echo "== 1. сверка живых ордеров C1: дни $(echo $cal | xargs -n1 basename 2>/dev/null | tr '\n' ' ')"
if [ -d "$D" ] && [ -n "$cal" ]; then
  nice -n 19 "$PYTHON" -u btc5m_lab/c1_match_cal.py "$D" --pm-roots $cal --out "$OUT_DIR" 2>&1 | cut -c1-220 | tail -40
else
  echo "нет $D или данных"
fi
echo "  прошло $(( $(date +%s) - start )) с"
days=$(ls -d "$DATA_DIR"/2026-1* 2>/dev/null | sort | grep -v 2026-10-2[2-9])
echo "== 2. mm_trig3"
for d in $days; do
  nice -n 19 "$PYTHON" -u btc5m_lab/mm_trig3.py "$d" --out "$OUT_DIR" 2>&1 | cut -c1-200 | tail -34
  echo "  прошло $(( $(date +%s) - start )) с"
done
