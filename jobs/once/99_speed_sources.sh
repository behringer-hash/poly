#!/usr/bin/env bash
# timeout_min: 120
# 1) какой источник сообщает о скачке раньше всех (оси recv и exch); 2) прибыль по источникам в модели C1 (replay, L=250/300/400);
# 3) стратегия «скачок на N$ по сырым сделкам» против C1. Всё с низким приоритетом (nice 19), чтобы не мешать живому боту.
set -u
days=$(ls -d "$DATA_DIR"/20* 2>/dev/null | tail -4)
[ -z "$days" ] && { echo "нет данных"; exit 0; }
N="nice -n 19"
echo "=== 1. скорость источников"
# shellcheck disable=SC2086
$N "$PYTHON" btc5m_lab/speed_compare.py $days --sources bybit,bybit_trade,binance_fut,binance_fut_book,binance,binance_book,coinbase,bitstamp,okx,kraken \
    --N 10,20,30 --W 500,1000 > "$OUT_DIR/speed_sources.txt" 2>&1
head -c 9000 "$OUT_DIR/speed_sources.txt"
echo; echo "=== 2. прибыль по источникам (C1: порог 0.03, sigma x1, переплата 3 ц)"
for s in bybit bybit_trade binance_fut binance_fut_book binance coinbase bitstamp; do
  echo "--- $s"
  # shellcheck disable=SC2086
  $N "$PYTHON" btc5m_lab/replay.py $days --source $s --latencies 250,300,400 --thr 0.03 --sigma-mult 1 --slips 3 --exit-s 5 \
      > "$OUT_DIR/replay_$s.txt" 2>&1
  tail -n 8 "$OUT_DIR/replay_$s.txt" | cut -c1-200
done
echo; echo "=== 3. стратегия по сырым сделкам"
# shellcheck disable=SC2086
$N "$PYTHON" btc5m_lab/trade_jump.py $days --sources bybit_trade,binance_fut,binance --N 8,15,25 --W 250,500,1000 \
    --latencies 250,300,400 --slips 0,3,5 --baseline > "$OUT_DIR/trade_jump.txt" 2>&1
head -c 14000 "$OUT_DIR/trade_jump.txt"
