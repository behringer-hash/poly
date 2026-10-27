#!/usr/bin/env bash
# Панель бота (задержки, оценка триггера, заявки, последние сигналы) во втором окне терминала:
#   ./run_panel.sh live      (или dry / sign - по режиму, в котором запущен бот)
# Выход - Ctrl+C (бот при этом продолжает работать).
cd "$(dirname "$0")" || exit 1
M=${1:-live}
F="data_$M/panel.txt"
clear
while true; do
  out=$(cat "$F" 2>/dev/null || echo "нет $F - бот в режиме $M ещё не запущен (или панель отключена: jump_panel)")
  printf '\033[H'
  printf '%s\n' "$out" | sed 's/$/\x1b[K/'
  printf '\033[J'
  sleep 1
done
