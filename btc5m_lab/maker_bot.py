"""Бот мейкерского исполнения сигнала C1 без бумажной торговли: только сигнал и лимитные заявки.

    python3 maker_bot.py --config config_sign_test.json --mode dry    # без ключа, заявки не создаются
    python3 maker_bot.py --config config_sign_test.json --mode sign   # подписывает, но не отправляет
    python3 maker_bot.py --config config_live.json --mode live        # настоящие заявки (попросит ввести «ДА»)

Сигнал считает тот же движок, что у C1 (paper.py, модель anchor): BTC на Bybit сдвинулся с момента последнего
изменения книги так, что справедливая цена минус ask минус комиссия не меньше порога. Бумажных сделок нет:
по сигналу работает только live_maker.MakerTrader (пассивная заявка, снятие через maker_life_sec).

В консоли на каждый сигнал - строка СИГНАЛ и строка ЗАЯВКА (цена, bid/ask, очередь, результат постановки), через
maker_life_sec - строка ИТОГ (исполнена или нет, сколько, через сколько мс), по закрытии окна - результат каждой
исполненной заявки и итог с запуска. Данные пишутся в --data-dir (maker_orders, maker_final, live_windows, сигналы).
"""
from __future__ import annotations

import argparse
import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import emit, flush_console, log  # noqa: E402
from config import Config, Variant  # noqa: E402

KEEP = {"windows", "events_pm", "paper_signals"}


def build_cfg(lcfg: dict, data_dir: str, two_clob: bool = False) -> Config:
    v = Variant(lcfg["variant"], "anchor", float(lcfg.get("signal_edge", 0.035)),
                source=str(lcfg.get("signal_source", "bybit")), sigma_mult=float(lcfg.get("signal_sigma_mult", 1.0)),
                cooldown=float(lcfg.get("signal_cooldown_sec", 1.0)))
    cfg = Config(data_dir=data_dir, paper=True, paper_btc_source="bybit", latencies_ms=[])  # без бумажных сделок
    cfg.variants = [v]
    cfg.backup_clob = two_clob
    cfg.slippage_ticks = 0
    cfg.status_every_sec = 600          # служебная строка о связи раз в 10 минут
    return cfg


def main():
    ap = argparse.ArgumentParser(description="Мейкерское исполнение сигнала C1 (без бумажной торговли)")
    ap.add_argument("--config", required=True, help="файл настроек (config_sign_test.json или config_live.json)")
    ap.add_argument("--mode", default="dry", choices=["dry", "sign", "live"])
    ap.add_argument("--data-dir", default="")
    ap.add_argument("--two-clob", action="store_true", help="второе (резервное) соединение с книгой")
    ap.add_argument("--save-trades", action="store_true", help="писать все сделки рынка (pm_trades) - много данных")
    a = ap.parse_args()
    if sys.platform == "win32":
        os.system("")
    from live import LIVE_SCHEMAS, load_config
    lcfg = load_config(a.config)
    if str(lcfg.get("execution", "maker")).lower() != "maker":
        raise SystemExit("в файле настроек должно быть \"execution\": \"maker\"")
    if a.mode == "live" and lcfg.get("test_only"):
        raise SystemExit("файл настроек помечен test_only (без лимитов) - он только для режимов dry и sign")
    cfg = build_cfg(lcfg, a.data_dir or f"data_{a.mode}", a.two_clob)

    import pm as PM
    from live_maker import MAKER_LIVE_SCHEMAS, MakerTrader
    pmx = PM.PM(cfg)
    pmx.w.schemas.update(LIVE_SCHEMAS)
    pmx.w.schemas.update(MAKER_LIVE_SCHEMAS)
    keep = KEEP | set(MAKER_LIVE_SCHEMAS) | {"live_windows"} | ({"pm_trades"} if a.save_trades else set())
    orig = pmx.w.write
    pmx.w.write = lambda s, r: orig(s, r) if s in keep else None

    if a.mode == "live":
        emit("\033[91mРЕАЛЬНАЯ ТОРГОВЛЯ (мейкер). Вариант {variant}, {size} шейров на заявку, жизнь заявки {life} с; лимиты: "
             "{max_shares_per_window} шейров и ${max_spend_per_window} на окно, ${max_spend_per_day} и убыток "
             "${max_loss_per_day} за сутки, общий убыток {max_loss_total}. Аварийная остановка: файл {stop_file}.\033[0m"
             .format(life=lcfg.get("maker_life_sec", 2.0), **lcfg))
        if input("Введите ДА, чтобы начать реальную торговлю: ").strip().upper() != "ДА":
            raise SystemExit("отменено")
    trader = MakerTrader(lcfg, a.mode, pmx, pmx.w, None)
    trader.connect()
    pmx.paper.listener = trader          # сигналы -> заявки; итоги окон -> учёт
    pmx.maker = trader.hook              # сделки рынка -> теневое исполнение

    v = cfg.variants[0]
    emit(f"\033[96mМейкерский бот запущен ({a.mode}). Сигнал {v.name}: порог {100 * v.edge_thr:.1f} ц, источник {v.source}, "
         f"sigma x{v.sigma_mult:g}; заявка {lcfg.get('maker_price', 'improve')}, живёт {lcfg.get('maker_life_sec', 2.0)} с. "
         f"Данные: {os.path.abspath(cfg.data_dir)}\033[0m")

    async def run_all():
        await asyncio.gather(pmx.main(), trader.keepalive(), trader.warm_loop(), trader.presign_loop(), *trader.extra_tasks())

    try:
        asyncio.run(run_all())
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        log("bot", f"остановка из-за ошибки: {ex!r}")
    finally:
        m = trader.mstats
        emit(f"Итог с запуска: сигналов {m['signals']}, исполнено заявок {m['filled']} ({m['shares']:.0f} шт), "
             f"PnL {trader.total_pnl:+.2f}$")
        trader.shutdown()
        pmx.w.close()
        flush_console()


if __name__ == "__main__":
    main()
