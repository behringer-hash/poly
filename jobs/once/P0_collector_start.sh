#!/usr/bin/env bash
# timeout_min: 15
# Включение службы записи и проверка, что пишутся все потоки, прежде всего Binance (спот: bn_agg, bn_book;
# фьючерс: bnf_agg, bnf_book). Раннер уже перезапустил службу, если менялся код записи (run.py) - здесь только проверка
# и запуск, если служба всё ещё не активна. Плюс нагрузка на CPU (на этом же сервере работает бот).
set -u
echo "== служба: $(systemctl is-active lab-collector) / автозапуск: $(systemctl is-enabled lab-collector 2>&1)"
systemctl show lab-collector -p ActiveEnterTimestamp -p NRestarts -p MainPID 2>/dev/null
systemctl cat lab-collector 2>/dev/null | grep -E "^ExecStart"
if [ "$(systemctl is-active lab-collector)" != "active" ]; then
  echo "служба не активна - запускаю"
  sudo -n /bin/systemctl restart lab-collector && echo "запущена" || echo "ЗАПУСК НЕ РАЗРЕШЁН (sudoers)"
fi
sleep 150
echo "== через 150 с: $(systemctl is-active lab-collector)"
systemctl show lab-collector -p ActiveEnterTimestamp -p NRestarts 2>/dev/null
D="$DATA_DIR/$(date -u +%F)"
echo "== свежесть потоков в $D (возраст последней записи, с; строк в текущем часовом файле)"
now=$(date +%s)
for f in $(ls "$D"/*.csv 2>/dev/null | sort); do
  age=$(( now - $(stat -c %Y "$f") ))
  printf "%-28s возраст %4s с, строк %8s\n" "$(basename "$f")" "$age" "$(wc -l < "$f")"
done
echo "== ожидаемые потоки Binance:"
for s in bn_agg bn_book bnf_agg bnf_book; do
  f=$(ls -t "$D"/${s}_*.csv 2>/dev/null | head -1)
  if [ -z "$f" ]; then echo "$s: НЕТ ФАЙЛА"; continue; fi
  n1=$(wc -l < "$f"); sleep 10; n2=$(wc -l < "$f")
  echo "$s: +$((n2 - n1)) строк за 10 с; последняя строка: $(tail -1 "$f" | cut -c1-120)"
done
echo "== задержки из журнала записи (последние строки [cex]):"
journalctl -u lab-collector -n 300 --no-pager 2>/dev/null | grep -E "\[cex\]|доп. потоки|ошибк|error" | tail -6 | cut -c1-400
echo "== нагрузка"
cat /proc/loadavg
vmstat 2 5 | tail -6
ps -eo pid,user,pcpu,pmem,etime,args --sort=-pcpu | grep -E "python|PID" | head -8 | cut -c1-160
