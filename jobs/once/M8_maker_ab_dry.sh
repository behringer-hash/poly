#!/usr/bin/env bash
# timeout_min: 25
# Проверка режима A/B (bid+1 и по ask случайно) в maker_bot.py, dry на живых данных, 12 минут.
set -u
cd btc5m_lab || exit 0
python3 -c "import json; c=json.load(open('live_config_maker.example.json', encoding='utf-8')); c.update(test_only=True, one_order_per_side=False, max_open_orders=10**6, maker_price='ab', ab_modes=['improve','ask'], max_spend_per_window=1e9, max_shares_per_window=1e9, max_orders_per_window=10**6, max_spend_per_day=1e9); json.dump(c, open('/tmp/mk_ab.json', 'w', encoding='utf-8'))"
timeout -s INT 720 nice -n 5 "$PYTHON" -u maker_bot.py --config /tmp/mk_ab.json --mode dry --data-dir "$OUT_DIR/data" > "$OUT_DIR/console.txt" 2>&1
echo "код выхода: $?"
sed 's/\x1b\[[0-9;]*m//g' "$OUT_DIR/console.txt" | grep -v "^\s*$" | grep -v "\[pm\] RTDS\|подключён" | tail -150 | cut -c1-280
rm -f "$OUT_DIR/console.txt"
