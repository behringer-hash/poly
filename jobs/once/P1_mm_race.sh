#!/usr/bin/env bash
# timeout_min: 150
# Хронометраж для маркет-мейкинга (btc5m_lab/mm_race.py): скачки BTC на фьючерсе Binance, когда на Polymarket съедают
# устаревшие котировки, когда книга переоценивается и когда о скачке узнали бы мы по каждому источнику.
# Выход: race_<день>.csv.gz в OUT_DIR (строка на скачок), статистика считается отдельно.
set -u
ulimit -v 2300000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
days=$(ls -d "$DATA_DIR"/2026-1* 2>/dev/null | sort)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
echo "дни: $(for d in $days; do basename $d; done | tr '\n' ' ')"
start=$(date +%s)
# shellcheck disable=SC2086
nice -n 19 "$PYTHON" -u btc5m_lab/mm_race.py $days --out "$OUT_DIR" --N 10 --W 1000 --min-gap 0.02 2>&1 | cut -c1-400 | tail -c 12000
echo "время: $(( $(date +%s) - start )) с"
ls -la "$OUT_DIR"
