#!/usr/bin/env bash
# timeout_min: 100
# Признаки сигнала sig_model (шаг 1 с) + цель за все дни с сырыми данными (16–21, 26–29.10) — обучение модели v2 вне сервера.
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
for b in 2026-10-16 2026-10-17 2026-10-18 2026-10-19 2026-10-20 2026-10-21 2026-10-26 2026-10-27 2026-10-28 2026-10-29; do
  [ -d "$DATA_DIR/$b" ] || continue
  nice -n 19 "$PYTHON" -u -W ignore sig_export.py "$DATA_DIR/$b" --out "$OUT_DIR" --step 10 2>&1 | tail -3
done
du -sh "$OUT_DIR"
