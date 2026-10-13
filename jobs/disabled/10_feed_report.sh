#!/usr/bin/env bash
# interval_min: 360
# Задержки всех лент (Binance, Bybit, OKX, Kraken, Bitstamp, Coinbase, Polymarket) за последние 6 часов.
exec "$PYTHON" ops/feed_report.py 6
