#!/usr/bin/env bash
# Режим dry: без ключа, заявки не создаются; исполнение считается «теневое» (по книге и сделкам рынка).
cd "$(dirname "$0")" || exit 1
[ -f STOP ] && { echo "есть файл STOP (аварийная остановка с прошлого запуска): удалите его командой  rm STOP  и запустите снова"; exit 1; }
mkdir -p logs
python3 -u sig4_bot.py --config config_sig4_sign.json --mode dry --data-dir data_sig4_dry \
    2>&1 | tee -a "logs/sig4_dry_$(date -u +%Y%m%d_%H%M).log"
