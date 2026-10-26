#!/usr/bin/env bash
# timeout_min: 25
# Проверка maker_bot.py (без бумажной торговли) в режиме dry на живых данных, 12 минут: как выглядит консоль.
set -u
cd btc5m_lab || exit 0
python3 -c "import json; c=json.load(open('live_config_maker.example.json', encoding='utf-8')); c['test_only']=True; c['one_order_per_side']=False; c['max_open_orders']=10**6; json.dump(c, open('/tmp/mk_test.json', 'w', encoding='utf-8'))"
timeout -s INT 720 nice -n 5 "$PYTHON" -u maker_bot.py --config /tmp/mk_test.json --mode dry --data-dir "$OUT_DIR/data" > "$OUT_DIR/console.txt" 2>&1
echo "код выхода: $?"
sed 's/\x1b\[[0-9;]*m//g' "$OUT_DIR/console.txt" | grep -v "^\s*$" | tail -120 | cut -c1-260
rm -f "$OUT_DIR/console.txt"
