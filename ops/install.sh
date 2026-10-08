#!/usr/bin/env bash
# Установка сервера записи. Запускать от администратора: sudo bash /home/lab/poly/ops/install.sh
# Можно запускать повторно: уже сделанное не ломается.
set -euo pipefail
[ "$(id -u)" -eq 0 ] || { echo "Запустите через sudo."; exit 1; }
LAB_HOME=/home/lab
id lab >/dev/null 2>&1 || { echo "Нет пользователя lab. Сначала выполните шаг 1 инструкции."; exit 1; }
[ -d "$LAB_HOME/poly/.git" ] || { echo "Нет $LAB_HOME/poly. Сначала выполните шаг 5 инструкции (git clone)."; exit 1; }
OPS="$LAB_HOME/poly/ops"

echo "== 1/6 пакеты"
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get install -y -qq python3 python3-venv python3-pip git xz-utils curl util-linux >/dev/null

echo "== 2/6 файл подкачки (защита от нехватки памяти)"
if [ "$(swapon --show --noheadings | wc -l)" -eq 0 ] && [ "$(awk '/MemTotal/{print int($2/1024)}' /proc/meminfo)" -lt 3000 ]; then
  fallocate -l 2G /swapfile && chmod 600 /swapfile && mkswap /swapfile >/dev/null && swapon /swapfile
  grep -q '^/swapfile' /etc/fstab || echo '/swapfile none swap sw 0 0' >> /etc/fstab
  echo "создан swap 2 ГБ"
else
  echo "swap уже есть или памяти достаточно"
fi

echo "== 3/6 python-окружение"
sudo -u lab python3 -m venv "$LAB_HOME/venv"
sudo -u lab "$LAB_HOME/venv/bin/pip" install -q --upgrade pip
sudo -u lab "$LAB_HOME/venv/bin/pip" install -q websockets orjson requests pandas numpy pytest

echo "== 4/6 настройки и папки"
[ -f "$LAB_HOME/lab.env" ] || sudo -u lab cp "$OPS/lab.env.example" "$LAB_HOME/lab.env"
sudo -u lab mkdir -p "$LAB_HOME/data" "$LAB_HOME/state"
chmod 700 "$LAB_HOME"

echo "== 5/6 службы"
cp "$OPS"/systemd/lab-collector.service "$OPS"/systemd/lab-runner.service "$OPS"/systemd/lab-runner.timer /etc/systemd/system/
# пользователю lab разрешён ровно один привилегированный вызов: перезапуск службы записи
echo 'lab ALL=(root) NOPASSWD: /bin/systemctl restart lab-collector' > /etc/sudoers.d/lab-collector
chmod 440 /etc/sudoers.d/lab-collector
visudo -cf /etc/sudoers.d/lab-collector >/dev/null
systemctl daemon-reload

echo "== 6/6 запуск"
systemctl enable --now lab-collector
systemctl enable --now lab-runner.timer
sleep 3
systemctl --no-pager --lines=0 status lab-collector lab-runner.timer || true
echo
echo "Готово. Через 2–5 минут сервер сам выполнит первые задания и отправит отчёт в ветку server-results."
