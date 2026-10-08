#!/usr/bin/env bash
# interval_min: 60
# Отчёт о состоянии сервера: службы, диск, память, объём данных, задержки до бирж.
exec "$PYTHON" ops/status.py
