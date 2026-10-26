"""Точка входа: запускает три независимых процесса и перезапускает упавшие.

    python run.py                      # всё: запись бирж, Polymarket, кошелёк, бумажная торговля
    python run.py --only pm            # только Polymarket (для отладки)
    python run.py --no-paper           # только сбор данных

Остановка: Ctrl+C (данные сбрасываются на диск каждые 2 с).
"""
from __future__ import annotations

import multiprocessing as mp
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import parse_args  # noqa: E402


def _cex(cfg):
    import cex
    cex.run(cfg)


def _pm(cfg):
    import pm
    pm.run(cfg)


def _wallet(cfg):
    import wallet
    wallet.run(cfg)


EXTRA_FEEDS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "collector_extra_feeds.txt")


def add_feeds_from_file(cfg, path: str = EXTRA_FEEDS_FILE):
    """Служба записи (--no-paper): дополнительные биржевые потоки из файла рядом с run.py, через запятую или по строкам,
    # - комментарий. Так набор потоков меняется через репозиторий, без правки unit-файла службы (его меняет только
    администратор). Неизвестные имена пропускаются."""
    if cfg.paper or not os.path.exists(path):
        return []
    from feeds_extra import FEEDS
    names = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            names += [x.strip() for x in line.split("#")[0].split(",") if x.strip()]
    add = [n for n in names if n in FEEDS and n not in cfg.extra_feeds]
    cfg.extra_feeds = list(cfg.extra_feeds) + add
    skipped = [n for n in names if n not in FEEDS]
    print(f"[run] доп. потоки из {os.path.basename(path)}: {add or 'нет новых'}"
          + (f"; неизвестные пропущены: {skipped}" if skipped else ""), flush=True)
    return add


def main():
    cfg = parse_args()
    add_feeds_from_file(cfg)
    restore_console = lambda: None
    if cfg.no_quickedit:
        from common import disable_quick_edit
        restore_console = disable_quick_edit()
    os.makedirs(cfg.data_dir, exist_ok=True)
    targets = {"cex": _cex, "pm": _pm}
    if cfg.wallet_enabled:
        targets["wallet"] = _wallet
    if cfg.only:
        targets = {k: v for k, v in targets.items() if k in cfg.only}
    procs: dict[str, mp.Process] = {}

    def start(name):
        p = mp.Process(target=targets[name], args=(cfg,), name=name, daemon=False)
        p.start()
        procs[name] = p
        print(f"[run] процесс {name} запущен (pid {p.pid})", flush=True)

    for n in targets:
        start(n)
    try:
        while True:
            time.sleep(2)
            for n, p in list(procs.items()):
                if not p.is_alive():
                    print(f"[run] процесс {n} завершился (код {p.exitcode}), перезапуск через 5 с", flush=True)
                    time.sleep(5)
                    start(n)
    except KeyboardInterrupt:
        print("[run] остановка...", flush=True)
    finally:
        for p in procs.values():
            p.join(timeout=15)
            if p.is_alive():
                p.terminate()
        restore_console()


if __name__ == "__main__":
    mp.freeze_support()
    main()
