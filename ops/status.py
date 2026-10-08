"""Отчёт о состоянии сервера записи (только стандартная библиотека). Пишет status.md в $OUT_DIR."""
from __future__ import annotations

import glob
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone

DATA = os.environ.get("DATA_DIR", "/home/lab/data")
OUT = os.environ.get("OUT_DIR", ".")


def sh(cmd: str, timeout: int = 20) -> str:
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return (r.stdout + r.stderr).strip()
    except Exception as e:  # noqa: BLE001
        return f"ошибка: {e}"


def size_h(n: float) -> str:
    for u in ("Б", "КБ", "МБ", "ГБ"):
        if n < 1024:
            return f"{n:.0f} {u}"
        n /= 1024
    return f"{n:.1f} ТБ"


def main():
    L = [f"# Состояние сервера записи\n", f"Время (UTC): {datetime.now(timezone.utc):%Y-%m-%d %H:%M:%S}\n"]
    L.append("## Службы")
    L.append(f"- lab-collector: {sh('systemctl is-active lab-collector')}")
    L.append(f"- lab-runner.timer: {sh('systemctl is-active lab-runner.timer')}")
    L.append(f"- uptime: {sh('uptime -p')}")
    L.append(f"- синхронизация часов: {sh('timedatectl show -p NTPSynchronized --value')}")
    L.append("\n## Ресурсы")
    du = shutil.disk_usage("/")
    L.append(f"- диск: занято {size_h(du.used)} из {size_h(du.total)}, свободно {size_h(du.free)}")
    L.append("- память:\n```\n" + sh("free -m") + "\n```")
    L.append(f"- нагрузка CPU (1/5/15 мин): {' / '.join(f'{x:.2f}' for x in os.getloadavg())}")
    L.append("\n## Данные")
    files = [f for f in glob.glob(os.path.join(DATA, "**", "*"), recursive=True) if os.path.isfile(f)]
    total = sum(os.path.getsize(f) for f in files)
    L.append(f"- файлов: {len(files)}, всего {size_h(total)}")
    now = time.time()
    by: dict[str, list] = {}
    for f in files:
        name = os.path.basename(f).rsplit("_", 1)[0]
        by.setdefault(name, []).append(f)
    L.append("\n| поток | файлов | размер | последнее обновление, с назад |\n|---|---|---|---|")
    for k in sorted(by):
        fs = by[k]
        L.append(f"| {k} | {len(fs)} | {size_h(sum(os.path.getsize(f) for f in fs))} | "
                 f"{now - max(os.path.getmtime(f) for f in fs):.0f} |")
    days = sorted({os.path.basename(os.path.dirname(f)) for f in files})
    L.append(f"\nДни с данными: {', '.join(days[-10:]) or 'нет'}")
    L.append("\n## Сеть до бирж (время ответа HTTPS, мс)")
    for name, url in (("Binance REST", "https://api.binance.com/api/v3/time"),
                      ("Polymarket CLOB", "https://clob.polymarket.com/time"),
                      ("Polymarket gamma", "https://gamma-api.polymarket.com/markets?limit=1")):
        t = sh(f"curl -s -o /dev/null -w '%{{time_connect}} %{{time_appconnect}} %{{time_total}}' --max-time 10 {url}")
        try:
            c, a, tt = (float(x) * 1000 for x in t.split())
            L.append(f"- {name}: TCP {c:.0f}, TLS {a:.0f}, всего {tt:.0f}")
        except ValueError:
            L.append(f"- {name}: {t}")
    L.append("\n## Последние строки журнала записи")
    L.append("```\n" + sh("journalctl -u lab-collector -n 15 --no-pager -o cat") + "\n```")
    L.append(f"\nПредставлено версией кода: {sh('git -C ' + os.environ.get('REPO_DIR', '.') + ' rev-parse --short HEAD')}; "
             f"python {sys.version.split()[0]}")
    with open(os.path.join(OUT, "status.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
