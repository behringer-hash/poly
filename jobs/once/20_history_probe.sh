#!/usr/bin/env bash
# Какая история доступна задним числом (дампы Binance/Bybit, сделки и цены Polymarket). Версия 2: Polymarket ищется через /events.
exec "$PYTHON" ops/history_probe.py
