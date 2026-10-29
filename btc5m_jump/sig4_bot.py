"""Бот стратегии 4: мейкер по сигналу модели (прогноз хода цены токена на 3 с по книге Polymarket и BTC на трёх биржах).

    python3 sig4_bot.py --config config_sig4_sign.json --mode dry    # без ключа, заявки не создаются
    python3 sig4_bot.py --config config_sig4_sign.json --mode sign   # подписывает, но не отправляет
    python3 sig4_bot.py --config config_sig4_live.json --mode live   # настоящие заявки (попросит ввести «ДА»)

Сигнал - sig4.py (каждые 100 мс: признаки, прогноз модели models/*.npz, условия входа и досрочного снятия).
Заявка - live_maker.MakerTrader: только на постановку (post-only), лучший bid + 1 ц при спреде >= 2 ц, иначе лучший bid,
живёт maker_life_sec; позиция держится до исхода окна. Данные - в --data-dir: sig4_signals, sig4_cancels, sig4_scores,
sig4_feeds, maker_orders, maker_final, live_windows, windows.
"""
from __future__ import annotations

import argparse
import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import emit, flush_console, log  # noqa: E402
from jump_bot import build_cfg  # noqa: E402

KEEP = {"windows", "events_pm"}


def main():
    ap = argparse.ArgumentParser(description="Стратегия 4: мейкер по сигналу модели")
    ap.add_argument("--config", required=True, help="config_sig4_sign.json или config_sig4_live.json")
    ap.add_argument("--mode", default="dry", choices=["dry", "sign", "live"])
    ap.add_argument("--data-dir", default="")
    ap.add_argument("--two-clob", action="store_true", help="второе (резервное) соединение с книгой")
    ap.add_argument("--save-trades", action="store_true", help="писать все сделки рынка (pm_trades) - много данных")
    a = ap.parse_args()
    if sys.platform == "win32":
        os.system("")
    from live import LIVE_SCHEMAS, load_config
    lcfg = load_config(a.config)
    if str(lcfg.get("execution", "")).lower() != "sig4":
        raise SystemExit("в файле настроек должно быть \"execution\": \"sig4\"")
    if a.mode == "live" and lcfg.get("test_only"):
        raise SystemExit("файл настроек помечен test_only (без лимитов) - он только для режимов dry и sign")
    cfg = build_cfg(a.data_dir or f"data_sig4_{a.mode}", a.two_clob)

    import pm as PM
    from live_maker import MAKER_LIVE_SCHEMAS, MakerTrader
    from sig4 import SIG4_DEFAULTS, SIG4_SCHEMAS, Sig4Trigger
    pmx = PM.PM(cfg)
    pmx.paper.evaluate = lambda *args, **kw: None     # сигналов C1 нет
    for sch in (LIVE_SCHEMAS, MAKER_LIVE_SCHEMAS, SIG4_SCHEMAS):
        pmx.w.schemas.update(sch)
    keep = KEEP | set(MAKER_LIVE_SCHEMAS) | set(SIG4_SCHEMAS) | {"live_windows"} | ({"pm_trades"} if a.save_trades else set())

    sc = {**SIG4_DEFAULTS, **{k: v for k, v in lcfg.items() if k.startswith("sig4_")}}
    life = lcfg.get("maker_life_sec", 1.5)
    if a.mode == "live":
        emit("\033[91mРЕАЛЬНАЯ ТОРГОВЛЯ (стратегия 4, мейкер по сигналу). {size} шейров на заявку (только на постановку), "
             "жизнь заявки {life} с; лимиты: {max_shares_per_window} шейров и ${max_spend_per_window} на окно, "
             "${max_spend_per_day} и убыток ${max_loss_per_day} за сутки, общий убыток {max_loss_total}. "
             "Аварийная остановка: файл {stop_file}.\033[0m".format(life=life, **lcfg))
        if input("Введите ДА, чтобы начать реальную торговлю: ").strip().upper() != "ДА":
            raise SystemExit("отменено")
    trader = MakerTrader(lcfg, a.mode, pmx, pmx.w, None)
    trader.connect()
    pmx.paper.listener = trader          # итоги окон -> учёт
    pmx.maker = trader.hook              # сделки рынка -> теневое исполнение
    sig = Sig4Trigger(lcfg, pmx, pmx.w, trader)
    orig = pmx.w.write

    def write(stream, row):              # книга, сделки и Chainlink движка -> признаки сигнала; на диск - только нужное
        sig.on_row(stream, row)
        if stream in keep:
            orig(stream, row)
    pmx.w.write = write

    emit(f"\033[96mБот стратегии 4 запущен ({a.mode}). Модель {os.path.basename(sig.trees.path)} ({sig.trees.n_trees} деревьев); "
         f"вход: прогноз хода стороны от {sc['sig4_thr_c']} ц и ход BTC от ${sc['sig4_fresh_usd']} за 0,3 с на любой бирже; "
         f"заявка {lcfg['size']} шт по bid (+1 ц при спреде от 2 ц), только на постановку, живёт {life} с; "
         f"окно {sc['sig4_t_min']:.0f}-{sc['sig4_t_max']:.0f} с. Торговля - с первого полного окна после запуска "
         f"(нужна история BTC с T-20 с, как при обучении). Данные: {os.path.abspath(cfg.data_dir)}\033[0m")

    async def run_all():
        await asyncio.gather(pmx.main(), trader.keepalive(), trader.warm_loop(), trader.presign_loop(),
                             trader.stats_loop(), *trader.extra_tasks(), *sig.tasks())

    try:
        asyncio.run(run_all())
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        log("bot", f"остановка из-за ошибки: {ex!r}")
    finally:
        m = trader.mstats
        emit(f"Итог с запуска: сигналов {sig.stats['signals']}, заявок {m['signals'] - m['skipped']}, исполнено "
             f"{m['filled']} ({m['shares']:.0f} шт), PnL {trader.total_pnl:+.2f}$")
        trader.shutdown()
        pmx.w.close()
        flush_console()


if __name__ == "__main__":
    main()
