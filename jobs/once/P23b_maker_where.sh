#!/usr/bin/env bash
# timeout_min: 180
# Повтор P23 с исправленным ключом транзакции. Где зарабатывают мейкеры: повтор prep (ключ транзакции, чтобы связать мейкеров с мс-заявками тейкеров), затем agg2:
# глубина x время, глубина x ярус тейкера, ход BTC до сделки, размер заявки, профили лучших/крупнейших мейкеров.
set -u
ulimit -v 3000000 2>/dev/null || true
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
cd btc5m_lab || exit 1
start=$(date +%s)
for d in $(ls -d "$DATA_DIR"/2026-10-* 2>/dev/null | sort); do
  b=$(basename "$d")
  [ -f "$HOME/tapes/tape_${b}.csv.gz" ] || continue
  nice -n 19 "$PYTHON" -u flow_wallets.py prep "$d" --tapes "$HOME/tapes" --store "$HOME/flow" 2>&1 | tail -1
done
echo "prep: $(( $(date +%s) - start )) с"
nice -n 19 "$PYTHON" -u flow_wallets.py agg2 --store "$HOME/flow" --out "$OUT_DIR" 2>&1 | tee "$OUT_DIR/agg2.txt" | tail -3
echo "всего: $(( $(date +%s) - start )) с"
