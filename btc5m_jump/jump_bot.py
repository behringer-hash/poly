"""Бот стратегии 3: ход BTC на Binance -> лимитная заявка на покупку растущего токена Polymarket (BTC Up/Down 5 мин).

    python3 jump_bot.py --config config_jump_sign.json --mode dry    # без ключа, заявки не создаются
    python3 jump_bot.py --config config_jump_sign.json --mode sign   # подписывает, но не отправляет
    python3 jump_bot.py --config config_jump_live.json --mode live   # настоящие заявки (попросит ввести «ДА»)

Сигнал - jump.py: сделки фьючерса и спота Binance, ход за 100 мс, сдвиг справедливой цены от 3 ц (по ask) и от 6 ц
(по ask + 1 ц). Заявка - live_maker.MakerTrader: обычный лимит (не post-only), 5 шейров, снимается через 0,5 с,
позиция держится до исхода окна. Бумажной торговли C1 нет.

В консоли на каждый сигнал - строки СИГНАЛ и ЗАЯВКА, через 0,5 с - ИТОГ (исполнена или нет), по закрытии окна - результат
каждой исполненной заявки и итог с запуска; раз в 5 минут - строка [JUMP] о потоках Binance и числе сигналов.
Данные пишутся в --data-dir (jump_signals, maker_orders, maker_final, live_windows, windows).
"""
from __future__ import annotations

import argparse
import asyncio
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import emit, flush_console, log  # noqa: E402
from config import Config  # noqa: E402

KEEP = {"windows", "events_pm"}


def build_cfg(data_dir: str, two_clob: bool = False) -> Config:
    # paper=True нужен ради итогов окон (paper.settle -> trader.on_settle) и потоков Bybit/Coinbase для статуса;
    # сигналов C1 нет: вариантов нет, оценка отключена
    cfg = Config(data_dir=data_dir, paper=True, paper_btc_source="bybit", latencies_ms=[])
    cfg.variants = []
    cfg.backup_clob = two_clob
    cfg.slippage_ticks = 0
    cfg.status_every_sec = 600
    return cfg


def main():
    ap = argparse.ArgumentParser(description="Стратегия 3: ход Binance -> лимит на покупку растущего токена")
    ap.add_argument("--config", required=True, help="config_jump_sign.json или config_jump_live.json")
    ap.add_argument("--mode", default="dry", choices=["dry", "sign", "live"])
    ap.add_argument("--data-dir", default="")
    ap.add_argument("--two-clob", action="store_true", help="второе (резервное) соединение с книгой")
    ap.add_argument("--save-trades", action="store_true", help="писать все сделки рынка (pm_trades) - много данных")
    a = ap.parse_args()
    if sys.platform == "win32":
        os.system("")
    from live import LIVE_SCHEMAS, load_config
    lcfg = load_config(a.config)
    if str(lcfg.get("execution", "")).lower() != "jump":
        raise SystemExit("в файле настроек должно быть \"execution\": \"jump\"")
    if a.mode == "live" and lcfg.get("test_only"):
        raise SystemExit("файл настроек помечен test_only (без лимитов) - он только для режимов dry и sign")
    cfg = build_cfg(a.data_dir or f"data_{a.mode}", a.two_clob)

    import pm as PM
    from jump import JUMP_DEFAULTS, JUMP_SCHEMAS, JumpTrigger
    from live_maker import MAKER_LIVE_SCHEMAS, MakerTrader
    pmx = PM.PM(cfg)
    pmx.paper.evaluate = lambda *args, **kw: None     # сигналов C1 нет
    for sch in (LIVE_SCHEMAS, MAKER_LIVE_SCHEMAS, JUMP_SCHEMAS):
        pmx.w.schemas.update(sch)
    keep = KEEP | set(MAKER_LIVE_SCHEMAS) | set(JUMP_SCHEMAS) | {"live_windows"} | ({"pm_trades"} if a.save_trades else set())
    orig = pmx.w.write
    pmx.w.write = lambda s, r: orig(s, r) if s in keep else None

    jc = {**JUMP_DEFAULTS, **{k: v for k, v in lcfg.items() if k.startswith("jump_")}}
    if a.mode == "live":
        emit("\033[91mРЕАЛЬНАЯ ТОРГОВЛЯ (стратегия 3, ход Binance). {size} шейров на заявку, жизнь заявки {life} с; лимиты: "
             "{max_shares_per_window} шейров и ${max_spend_per_window} на окно, ${max_spend_per_day} и убыток "
             "${max_loss_per_day} за сутки, общий убыток {max_loss_total}. Аварийная остановка: файл {stop_file}.\033[0m"
             .format(life=lcfg.get("maker_life_sec", 0.5), **lcfg))
        if input("Введите ДА, чтобы начать реальную торговлю: ").strip().upper() != "ДА":
            raise SystemExit("отменено")
    trader = MakerTrader(lcfg, a.mode, pmx, pmx.w, None)
    trader.connect()
    pmx.paper.listener = trader          # итоги окон -> учёт
    pmx.maker = trader.hook              # сделки рынка -> теневое исполнение
    jt = JumpTrigger(lcfg, pmx, pmx.w, trader)
    from panel import MarketPanel
    os.makedirs(cfg.data_dir, exist_ok=True)
    panel_path = os.path.join(cfg.data_dir, "panel.txt") if jc.get("jump_panel", True) else None
    panel = MarketPanel(jt, pmx, trader, a.mode, panel_path, float(jc.get("jump_pulse_sec", 1) or 0))

    emit(f"\033[96mБот стратегии 3 запущен ({a.mode}). Ход Binance ({', '.join(jc['jump_sources'])}) за "
         f"{jc['jump_window_ms']} мс: сдвиг цены от {100 * jc['jump_thr_weak']:.0f} ц - лимит {jc['jump_price_weak']}, "
         f"от {100 * jc['jump_thr_strong']:.0f} ц - {jc['jump_price_strong']}; {lcfg['size']} шейров, живёт "
         f"{lcfg.get('maker_life_sec', 0.5)} с. Сигналы начнутся, когда наберётся волатильность "
         f"({jc['jump_sigma_min_sec']} с). Данные: {os.path.abspath(cfg.data_dir)}\033[0m")
    if panel_path:
        emit(f"Панель (обновляется раз в секунду): {os.path.abspath(panel_path)} - смотреть во втором окне: ./run_panel.sh {a.mode}")

    async def run_all():
        await asyncio.gather(pmx.main(), trader.keepalive(), trader.warm_loop(), trader.presign_loop(),
                             trader.stats_loop(), *trader.extra_tasks(), *jt.tasks(), panel.run())

    try:
        asyncio.run(run_all())
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        log("bot", f"остановка из-за ошибки: {ex!r}")
    finally:
        m = trader.mstats
        st = jt.stats
        emit(f"Итог с запуска: сигналов {m['signals']} (сильных {st['strong']}, слабых {st['weak']}), исполнено заявок "
             f"{m['filled']} ({m['shares']:.0f} шт), PnL {trader.total_pnl:+.2f}$")
        trader.shutdown()
        pmx.w.close()
        flush_console()


if __name__ == "__main__":
    main()
