#!/usr/bin/env bash
# Режим sign: с ключом; заявки подписываются (заранее и по сигналу), но НЕ отправляются.
# Проверяет кошелёк, signature_type, баланс и подпись; исполнение - теневое. Лимиты сняты (config_sig4_sign.json).
cd "$(dirname "$0")" || exit 1
[ -f STOP ] && { echo "есть файл STOP (аварийная остановка с прошлого запуска): удалите его командой  rm STOP  и запустите снова"; exit 1; }
if [ -z "${PM_PRIVATE_KEY:-}" ]; then
  read -r -s -p "Приватный ключ (не отображается и не сохраняется): " PM_PRIVATE_KEY; echo
  export PM_PRIVATE_KEY
fi
mkdir -p logs
python3 -u sig4_bot.py --config config_sig4_sign.json --mode sign --data-dir data_sig4_sign \
    2>&1 | tee -a "logs/sig4_sign_$(date -u +%Y%m%d_%H%M).log"
