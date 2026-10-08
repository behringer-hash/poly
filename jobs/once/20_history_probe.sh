#!/usr/bin/env bash
# Какая история доступна задним числом (дампы Binance/Bybit, сделки и цены Polymarket). Выполняется один раз.
exec "$PYTHON" ops/history_probe.py
