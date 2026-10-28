#!/usr/bin/env bash
# timeout_min: 240
# Кто кому платит: ленты с кошельками (P21, ~/tapes) + запись сборщика (мс) по всем дням -> ~/flow (по дням),
# затем сводка: ярусы кошельков, «мейкер <- тейкер», поток тейкеров по времени / размеру / ходу BTC / цене.
set -u
ulimit -v 3000000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
cd btc5m_lab || exit 1
start=$(date +%s)
for d in $(ls -d "$DATA_DIR"/2026-10-* 2>/dev/null | sort); do
  b=$(basename "$d")
  [ -f "$HOME/tapes/tape_${b}.csv.gz" ] || { echo "$b: нет ленты"; continue; }
  nice -n 19 "$PYTHON" -u flow_wallets.py prep "$d" --tapes "$HOME/tapes" --store "$HOME/flow" 2>&1 | tail -4
  echo "  прошло $(( $(date +%s) - start )) с"
done
nice -n 19 "$PYTHON" -u flow_wallets.py agg --store "$HOME/flow" --out "$OUT_DIR" 2>&1 | tee "$OUT_DIR/agg.txt" | tail -5
du -sh "$HOME/flow"; ls -la "$OUT_DIR"
