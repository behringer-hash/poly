#!/usr/bin/env bash
# Режим live: НАСТОЯЩИЕ заявки, с лимитами из config_jump_live.json (копия config_jump_live.example.json). Бот попросит ввести «ДА».
cd "$(dirname "$0")" || exit 1
[ -f STOP ] && { echo "есть файл STOP (аварийная остановка с прошлого запуска): удалите его командой  rm STOP  и запустите снова"; exit 1; }
[ -f config_jump_live.json ] || { echo "нет config_jump_live.json: скопируйте config_jump_live.example.json и впишите funder"; exit 1; }
if [ -z "${PM_PRIVATE_KEY:-}" ]; then
  read -r -s -p "Приватный ключ (не отображается и не сохраняется): " PM_PRIVATE_KEY; echo
  export PM_PRIVATE_KEY
fi
mkdir -p logs
python3 -u jump_bot.py --config config_jump_live.json --mode live --data-dir data_live \
    2>&1 | tee -a "logs/live_$(date -u +%Y%m%d_%H%M).log"
