"""Бумажный бот: отдельная программа для наблюдения за стратегией в реальном времени.

    python bot.py                                   # консоль + живой график, показывает anc_3c_by @ 150 мс
    python bot.py --show anc_2c_both@150            # какой бумажный счёт показывать подробно
    python bot.py --show all                        # показывать все счета (много строк)
    python bot.py --no-chart                        # только консоль
    python bot.py --variants anc_2c_by,anc_3c_by    # торговать только этими вариантами
    python bot.py --variants my:0.025:both          # свой вариант: имя:порог($/шейр):источник[:множитель σ]

Бот НЕ отправляет ордера. Он подключается к тем же фидам, что и сборщик данных
(книга Polymarket, Chainlink/TWAP60 через RTDS, Bybit и Coinbase), ищет сигналы
и "исполняет" их по реальной книге с задержкой L мс. Записывает только свои
сделки (папка bot_data: paper_signals / paper_fills / paper_markouts /
paper_windows / windows) - сырые рыночные данные не пишет.

Остановка: закройте окно графика или нажмите Ctrl+C в консоли.
"""
from __future__ import annotations

import argparse
import asyncio
import os
import sys
import threading
import time
from collections import deque
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import clock, emit, flush_console, log  # noqa: E402
from config import Config, Variant  # noqa: E402

KEEP_STREAMS = {"paper_signals", "paper_fills", "paper_markouts", "paper_windows", "windows", "events_pm"}


# ============================================================================ консоль
class C:
    """ANSI-цвета (в Windows 10/11 работают в PowerShell и Windows Terminal)."""
    on = True
    G, R, Y, B, M, D, X = "\033[92m", "\033[91m", "\033[93m", "\033[96m", "\033[95m", "\033[90m", "\033[0m"

    @classmethod
    def c(cls, color, s):
        return f"{color}{s}{cls.X}" if cls.on else s


def ts_ms(t: float) -> str:
    return datetime.fromtimestamp(t).strftime("%H:%M:%S.%f")[:-3]


class BotUI:
    """Получает события бумажного движка, печатает их и передаёт на график."""

    def __init__(self, cfg, pm, show: str, chart=None):
        self.cfg, self.pm, self.chart = cfg, pm, chart
        self.show_all = show == "all"
        if self.show_all:
            self.main = (cfg.variants[0].name, cfg.latencies_ms[0])
        else:
            name, _, lat = show.partition("@")
            self.main = (name, int(lat or 150))
            if name not in {v.name for v in cfg.variants}:
                raise SystemExit(f"вариант {name} не найден; доступны: {', '.join(v.name for v in cfg.variants)}")
            if self.main[1] not in cfg.latencies_ms:
                raise SystemExit(f"задержки {self.main[1]} мс нет в --latencies {cfg.latencies_ms}")
        self.windows_done = 0

    def shown(self, variant, L=None):
        if self.show_all:
            return True
        return variant == self.main[0] and (L is None or L == self.main[1])

    # ---- события движка
    def on_signal(self, s):
        if self.chart is not None and s["variant"] == self.main[0]:
            self.chart.add_signal(s)
        if not self.shown(s["variant"]):
            return
        src = {"bybit": "Bybit", "coinbase": "Coinbase", "both": "Bybit+Coinbase"}.get(s["source"], s["source"])
        age = f"{s['anchor_age']:.1f} с" if s["anchor_age"] is not None else "?"
        emit(C.c(C.Y, f"{ts_ms(s['t'])} СИГНАЛ #{s['sid']} [{s['variant']}] (бумага) покупка {s['outcome']:4s}") +
             f" ask {s['ask']:.2f} (на уровне {s['ask_sz'] or 0:.0f} шт) | справедливая {s['fair']:.3f}"
             f" | edge {100 * s['edge']:+.1f}ц после комиссии {100 * s['fee']:.1f}ц"
             f" | {src} {s['move']:+.2f}$ с переоценки книги {age} назад | T-{s['T']:.0f} с")

    def on_fill(self, f):
        if (f["variant"], f["L"]) == self.main and self.chart is not None:
            self.chart.add_fill(f)
        if not self.shown(f["variant"], f["L"]):
            return
        dt = 1000 * (f["t"] - f["t_sig"])
        tag = f"#{f['sid']} [{f['variant']} @{f['L']}мс]"
        if f["status"] == "fill":
            p = f["pos"] or {}
            u, d = p.get("Up", [0, 0, 0]), p.get("Down", [0, 0, 0])
            emit(C.c(C.G, f"{ts_ms(f['t'])}   └ БУМАГА: ИСПОЛНЕНО {tag}") +
                 f" через {dt:.0f} мс: {f['qty']:.0f} шт {f['outcome']} по {f['avg']:.3f}, комиссия ${f['fee']:.2f}"
                 f" | позиция окна: Up {u[0]:.0f} шт (ср. {u[1] / u[0] if u[0] else 0:.3f})"
                 f", Down {d[0]:.0f} шт (ср. {d[1] / d[0] if d[0] else 0:.3f})")
        else:
            now_ask = f"{f['ask_now']:.2f}" if f["ask_now"] is not None else "нет"
            emit(C.c(C.R, f"{ts_ms(f['t'])}   └ БУМАГА: ПРОМАХ {tag}") +
                 f" через {dt:.0f} мс: ask по {f['limit']:.2f} уже снят, лучший ask сейчас {now_ask}")

    def on_markout(self, m):
        if not self.shown(m["variant"], m["L"]):
            return
        col = C.G if m["mk"] > 0 else C.R
        emit(C.c(C.D, f"{ts_ms(clock.now())}   └ #{m['sid']} [{m['variant']} @{m['L']}мс] через "
                      f"{self.cfg.markout_sec:.0f} с mid {m['mid']:.3f} → ") + C.c(col, f"{m['mk']:+.1f}ц/шейр"))

    def on_settle(self, win, winner, used, results):
        try:
            self._on_settle(win, winner, used, results)
        except Exception as ex:
            log("bot", f"ошибка вывода итогов окна: {ex!r}")

    def _on_settle(self, win, winner, used, results):
        self.windows_done += 1
        r = results.get(self.main)
        acc = self.pm.paper.acc[self.main]
        how = {"provisional": "по TWAP60", "provisional_calc": "по TWAP60, посчитанному по Chainlink",
               "provisional_book": "по книге - TWAP60 недоступен", "official": "официально"}.get(used, used)
        head = f"══ ОКНО {datetime.fromtimestamp(win.start).strftime('%H:%M')} закрыто: победил {winner} ({how})"
        if r:
            up, dn = r["pos"]["Up"], r["pos"]["Down"]
            col = C.G if r["pnl"] >= 0 else C.R
            emit(C.c(C.B, head) + f" | [{self.main[0]} @{self.main[1]}мс] Up {up[0]:.0f} шт, Down {dn[0]:.0f} шт,"
                 f" комиссии ${r['fees']:.2f} → " + C.c(col, f"PnL {r['pnl']:+.2f}$") +
                 f" | итого {acc.pnl:+.2f}$ за {acc.windows} окон с позицией")
        else:
            emit(C.c(C.B, head) + f" | [{self.main[0]} @{self.main[1]}мс] сделок не было | итого {acc.pnl:+.2f}$")
        if self.chart is not None:
            self.chart.add_window_result(win.start, r["pnl"] if r else 0.0, acc.pnl, winner)
        if self.show_all or self.windows_done % 3 == 1:
            self.pm.paper.print_summary()

    # ---- периодический статус
    def position(self, slug):
        acc = self.pm.paper.acc[self.main]
        return acc.pos.get(slug)

    def mtm(self, win):
        """Текущая оценка позиции окна по mid с учётом комиссий."""
        p = self.position(win.slug)
        if not p:
            return 0.0, 0.0, 0.0
        val = 0.0
        for oc in ("Up", "Down"):
            m = win.books[oc].mid() or win.books[oc].ba or win.books[oc].bb or 0.0
            val += p[oc][0] * m
        cost = sum(p[oc][1] + p[oc][2] for oc in ("Up", "Down"))
        return p["Up"][0], p["Down"][0], val - cost

    async def status_loop(self):
        while True:
            await asyncio.sleep(5)
            now = clock.now()
            win = self.pm.current_window(now)
            if win is None:
                continue
            u, d = win.books["Up"], win.books["Down"]
            src = self.pm.src
            by = (src.get("bybit") or {}).get("px")
            cb = (src.get("coinbase") or {}).get("px")
            base = win.ptb
            rel = (lambda x: f"{x - base:+.1f}$" if (x is not None and base is not None) else "n/a")
            qu, qd, m = self.mtm(win)
            acc = self.pm.paper.acc[self.main]
            f = lambda x: f"{x:.2f}" if x is not None else "n/a"
            lag = win.book_lag_ms
            lag_txt = f"книга +{lag:.0f} мс" if lag is not None else "книга ?"
            if lag is not None and lag > self.cfg.max_book_lag_ms:
                lag_txt = C.c(C.R, lag_txt + " (отстаёт - сигналы отключены)")
            mem = self.pm.rss_mb()
            lag_now = self.pm.lag.q.q(0.99)
            sys_txt = (f"память {mem:.0f} МБ | " if mem else "") + (f"loop p99 {lag_now:.0f} мс" if lag_now else "")
            if lag_now and lag_now > 200:
                sys_txt = C.c(C.R, sys_txt + " (процессор не успевает)")
            tw_age = (now - max(self.pm.tw)) if self.pm.tw else None
            tw_txt = f"TWAP60 {tw_age:.0f} с назад" if tw_age is not None else "TWAP60 нет"
            if tw_age is not None and tw_age > 15:
                tw_txt = C.c(C.R, tw_txt + " (поток молчит!)")
            emit(C.c(C.D, f"{ts_ms(now)} [статус] T-{win.end - now:5.1f} с | Up {f(u.bb)}/{f(u.ba)} Down {f(d.bb)}/{f(d.ba)}"
                          f" | BTC−ptb: Bybit {rel(by)}, Coinbase {rel(cb)} | [{self.main[0]} @{self.main[1]}мс]"
                          f" позиция Up {qu:.0f}/Down {qd:.0f}, оценка {m:+.2f}$ | итого {acc.pnl:+.2f}$ | ") + lag_txt + " | " + tw_txt + " | " + sys_txt)


# ============================================================================ график
class LiveChart:
    """Живой график текущего окна (как в wallet_strategy_monitor): цены Up/Down,
    BTC относительно price to beat, позиция и оценка PnL бота, итог по окнам.
    Данные дописываются из потока asyncio под Lock, рисует главный поток."""

    def __init__(self, title: str, redraw_ms: int = 500, snapshot: str | None = None):
        self.lock = threading.Lock()
        self.title = title
        self.redraw_ms = redraw_ms
        self.snapshot = snapshot
        self.start = None
        self.ptb = None
        self.t = deque(maxlen=3000)
        self.ub, self.ua, self.db, self.da = (deque(maxlen=3000) for _ in range(4))
        self.bt, self.by, self.cb = deque(maxlen=3000), deque(maxlen=3000), deque(maxlen=3000)
        self.pr = deque(maxlen=3000)  # основной источник, если это не Bybit/Coinbase
        self.primary_name = None
        self.pt, self.pu, self.pd, self.pm = deque(maxlen=3000), deque(maxlen=3000), deque(maxlen=3000), deque(maxlen=3000)
        self.fills, self.misses, self.signals = [], [], []
        self.live = []  # реальные исполнения (живой тест)
        self.hist = deque(maxlen=60)  # (start, pnl окна, итого, победитель)
        self.last_winner = None
        self.stopped = False

    def reset(self, start, ptb):
        with self.lock:
            self.start, self.ptb = start, ptb
            for q in (self.t, self.ub, self.ua, self.db, self.da, self.bt, self.by, self.cb, self.pr, self.pt, self.pu,
                      self.pd, self.pm):
                q.clear()
            self.fills, self.misses, self.signals = [], [], []
            self.live = []

    def add_live(self, start, x, px, outcome, qty):
        with self.lock:
            if start == self.start:
                self.live.append((x, px, outcome, qty))

    def push(self, win, now, by, cb, pos, primary=None):
        with self.lock:
            if self.start != win.start:
                return
            if self.ptb is None and win.ptb is not None:
                self.ptb = win.ptb
            x = now - win.start
            u, d = win.books["Up"], win.books["Down"]
            self.t.append(x)
            self.ub.append(u.bb)
            self.ua.append(u.ba)
            self.db.append(d.bb)
            self.da.append(d.ba)
            self.bt.append(x)
            self.by.append(by)
            self.cb.append(cb)
            self.pr.append(primary)
            self.pt.append(x)
            self.pu.append(pos[0])
            self.pd.append(pos[1])
            self.pm.append(pos[2])

    def add_signal(self, s):
        with self.lock:
            if s["start"] == self.start:
                self.signals.append((s["t"] - s["start"], s["ask"], s["outcome"]))

    def add_fill(self, f):
        with self.lock:
            if f["start"] != self.start:
                return
            x = f["t"] - f["start"]
            if f["status"] == "fill":
                self.fills.append((x, f["avg"], f["outcome"], f["qty"]))
            else:
                self.misses.append((x, f["limit"], f["outcome"]))

    def add_window_result(self, start, pnl, cum, winner):
        with self.lock:
            self.hist.append((start, pnl, cum, winner))
            self.last_winner = winner

    # ---- отрисовка (только из главного потока)
    def _draw(self, axs):
        a1, a2, a3, a4, a3b, a4b = axs
        for a in axs:
            a.clear()
        with self.lock:
            t = list(self.t)
            ub, ua, db, da = list(self.ub), list(self.ua), list(self.db), list(self.da)
            bt, by, cb, pr = list(self.bt), list(self.by), list(self.cb), list(self.pr)
            pt, pu, pd, pm = list(self.pt), list(self.pu), list(self.pd), list(self.pm)
            fills, misses, sigs = list(self.fills), list(self.misses), list(self.signals)
            live = list(self.live)
            hist = list(self.hist)
            start, ptb = self.start, self.ptb
        nn = lambda v: [x if x is not None else float("nan") for x in v]
        # 1) цены
        if t:
            a1.fill_between(t, nn(ub), nn(ua), step="post", color="tab:green", alpha=0.25, lw=0)
            a1.step(t, nn(ua), where="post", color="tab:green", lw=0.8, label="Up ask/bid")
            a1.fill_between(t, nn(db), nn(da), step="post", color="tab:red", alpha=0.2, lw=0)
            a1.step(t, nn(da), where="post", color="tab:red", lw=0.8, label="Down ask/bid")
        for x, px, oc in sigs:
            a1.plot(x, px, ".", color="tab:olive", ms=4)
        for x, px, oc, q in fills:
            a1.scatter(x, px, marker="^" if oc == "Up" else "v", s=30 + q * 1.5,
                       color="tab:green" if oc == "Up" else "tab:red", edgecolors="k", lw=0.6, zorder=5)
        for x, px, oc in misses:
            a1.scatter(x, px, marker="x", s=30, color="0.4", zorder=4)
        for x, px, oc, q in live:
            a1.scatter(x, px, marker="*", s=160, color="magenta", edgecolors="k", lw=0.6, zorder=6)
        a1.set_ylim(0, 1)
        a1.set_xlim(0, 300)
        a1.set_ylabel("цена токена")
        a1.grid(alpha=0.3)
        a1.legend(loc="upper left", fontsize=7, ncol=2)
        left = f"T-{300 - t[-1]:.0f} с" if t else ""
        when = datetime.fromtimestamp(start).strftime("%H:%M") if start else "—"
        a1.set_title(f"{self.title} | окно {when} {left} | ▲▼ исполнения, × промахи, · сигналы, ★ реальные", fontsize=9)
        # 2) BTC относительно price to beat
        base = ptb if ptb is not None else next((x for x in by + cb + pr if x is not None), None)
        if base is not None and bt:
            a2.plot(bt, [x - base if x is not None else float("nan") for x in by], color="tab:orange", lw=0.8,
                    label="Bybit")
            a2.plot(bt, [x - base if x is not None else float("nan") for x in cb], color="tab:blue", lw=0.8,
                    label="Coinbase")
            if self.primary_name and any(x is not None for x in pr):
                a2.plot(bt, [x - base if x is not None else float("nan") for x in pr], color="tab:purple", lw=0.8,
                        label=self.primary_name)
            a2.axhline(0, color="k", lw=0.5)
            a2.legend(loc="upper left", fontsize=7, ncol=2)
        a2.set_xlim(0, 300)
        a2.set_ylabel("BTC − ptb, $" if ptb is not None else "BTC, $ (от первого)")
        a2.grid(alpha=0.3)
        # 3) позиция и оценка PnL окна
        if pt:
            a3.step(pt, pu, where="post", color="tab:green", label="шейров Up")
            a3.step(pt, pd, where="post", color="tab:red", label="шейров Down")
            a3b.plot(pt, pm, color="k", lw=0.9, label="оценка PnL окна, $")
            a3b.axhline(0, color="k", lw=0.4, ls=":")
            a3b.set_ylabel("$")
            a3b.legend(loc="upper right", fontsize=7)
            a3b.yaxis.set_label_position("right")
        a3.set_xlim(0, 300)
        a3.set_xlabel("секунды окна")
        a3.set_ylabel("шейры")
        a3.grid(alpha=0.3)
        a3.legend(loc="upper left", fontsize=7)
        # 4) итог по окнам
        if hist:
            xs = list(range(len(hist)))
            a4.bar(xs, [h[1] for h in hist], color=["tab:green" if h[1] >= 0 else "tab:red" for h in hist])
            a4b.plot(xs, [h[2] for h in hist], color="k", lw=1.2)
            a4b.set_ylabel("итого, $")
            a4b.yaxis.set_label_position("right")
            a4.set_xticks(xs[:: max(1, len(xs) // 10)])
            a4.set_xticklabels([datetime.fromtimestamp(h[0]).strftime("%H:%M") for h in hist][:: max(1, len(xs) // 10)],
                               fontsize=7)
        a4.set_ylabel("PnL окна, $")
        a4.set_title("результат по окнам (столбцы) и накопленный итог (линия)", fontsize=8)
        a4.grid(alpha=0.3)

    def show_blocking(self):
        import matplotlib
        if self.snapshot:
            matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axs = plt.subplots(4, 1, figsize=(11, 10), gridspec_kw={"height_ratios": [3, 1.3, 1.3, 1.2]})
        axs = list(axs) + [axs[2].twinx(), axs[3].twinx()]  # правые оси создаём один раз
        fig.canvas.manager.set_window_title("Бумажный бот BTC 5m") if hasattr(fig.canvas, "manager") and \
            fig.canvas.manager else None
        if self.snapshot:  # режим без экрана: периодически сохраняем картинку
            while not self.stopped:
                time.sleep(5)
                self._draw(axs)
                fig.tight_layout()
                fig.savefig(self.snapshot, dpi=90)
            return
        from matplotlib.animation import FuncAnimation

        def redraw(_):
            try:
                self._draw(axs)
                fig.tight_layout()
            except Exception as ex:  # график не должен ронять бота
                log("chart", f"ошибка отрисовки: {ex!r}")

        anim = FuncAnimation(fig, redraw, interval=self.redraw_ms, cache_frame_data=False)  # noqa: F841
        plt.show()


# ============================================================================ запуск
def parse():
    p = argparse.ArgumentParser(description="Бумажный бот BTC 5m (наблюдение в реальном времени)")
    p.add_argument("--show", default="anc_3c_by@150", help="какой счёт показывать: вариант@задержка или all")
    p.add_argument("--variants", default="", help="варианты через запятую: имя из config.py или имя:порог:источник")
    p.add_argument("--latencies", default="50,150,300,600")
    p.add_argument("--paper-btc-source", default="bybit", choices=["bybit", "coinbase", "binance", "rtds"])
    p.add_argument("--data-dir", default="bot_data")
    p.add_argument("--no-chart", action="store_true")
    p.add_argument("--binance-fut", action="store_true",
                   help="подключить фьючерс Binance - источник для моментум-вариантов (mom*_bnf, mom2_bnany)")
    p.add_argument("--binance-fut-book", action="store_true",
                   help="подключить верх книги фьючерса Binance с объёмами - для вариантов imbalance (imb90, imb95, imb90_m1)")
    p.add_argument("--binance-source", action="store_true",
                   help="подключить Binance (bookTicker) как ещё один источник цены BTC - для варианта anc_3c_any_s15")
    p.add_argument("--maker", action="store_true", help="бумажный мейкер: заявки на покупку обеих сторон (maker.py)")
    p.add_argument("--maker-show", default="mm_1c_cons", help="какой мейкерский счёт показывать подробно")
    p.add_argument("--single-clob", action="store_true",
                   help="одно соединение с книгой вместо двух (вдвое меньше нагрузки на процессор)")
    p.add_argument("--clip", type=float, default=50.0,
                   help="размер бумажного ордера, шейров (по умолчанию 50; для сравнения с живым тестом можно 5)")
    p.add_argument("--no-color", action="store_true")
    p.add_argument("--live", default="", help="файл настроек живого теста (см. live_config.example.json)")
    p.add_argument("--mode", default="dry", choices=["dry", "sign", "live"],
                   help="dry - ничего не подписывать; sign - подписывать, не отправлять; live - реальные ордера")
    p.add_argument("--chart-snapshot", default="", help=argparse.SUPPRESS)  # отладка без экрана
    a = p.parse_args()
    cfg = Config(data_dir=a.data_dir, paper=True, paper_btc_source=a.paper_btc_source,
                 latencies_ms=[int(x) for x in a.latencies.split(",") if x.strip()])
    cfg.status_every_sec = 30
    cfg.backup_clob = not a.single_clob
    cfg.paper_binance = a.binance_source
    cfg.paper_binance_fut = a.binance_fut
    cfg.paper_binance_fut_book = a.binance_fut_book
    cfg.maker = a.maker
    cfg.maker_show = a.maker_show
    if a.maker:
        KEEP_STREAMS.update({"maker_fills", "maker_markouts", "maker_windows", "pm_trades"})
    cfg.only = []  # type: ignore[attr-defined]
    cfg.no_quickedit = False  # type: ignore[attr-defined]
    if a.variants:
        known = {v.name: v for v in cfg.variants}
        chosen = []
        for item in a.variants.split(","):
            item = item.strip()
            if not item:
                continue
            if item in known:
                chosen.append(known[item])
            elif item.count(":") in (2, 3):
                parts = item.split(":")
                name, thr, src = parts[:3]
                mult = float(parts[3]) if len(parts) == 4 else 1.0
                chosen.append(Variant(name, "anchor", float(thr), source=src, sigma_mult=mult))
            else:
                raise SystemExit(f"не понял вариант '{item}'")
        cfg.variants = chosen
    for v in cfg.variants:
        v.clip = a.clip
    return cfg, a


def main():
    cfg, a = parse()
    C.on = not a.no_color
    if sys.platform == "win32":
        os.system("")  # включает ANSI-цвета в консоли Windows
    import pm as PM
    pmx = PM.PM(cfg)
    orig_write = pmx.w.write
    pmx.w.write = lambda s, r: orig_write(s, r) if s in KEEP_STREAMS else None  # сырые данные не пишем
    chart = None if (a.no_chart and not a.chart_snapshot) else LiveChart("", snapshot=a.chart_snapshot or None)
    ui = BotUI(cfg, pmx, a.show, chart)
    if chart is not None:
        chart.title = f"[{ui.main[0]} @{ui.main[1]}мс]"
        if cfg.paper_btc_source not in ("bybit", "coinbase"):
            chart.primary_name = cfg.paper_btc_source
    trader = None
    if a.live:
        from live import LIVE_SCHEMAS, Fanout, LiveTrader, load_config
        lcfg = load_config(a.live)
        if lcfg["variant"] not in {v.name for v in cfg.variants}:
            raise SystemExit(f"вариант {lcfg['variant']} из конфига не торгуется ботом (--variants)")
        pmx.w.schemas.update(LIVE_SCHEMAS)
        KEEP_STREAMS.update(set(LIVE_SCHEMAS) | {"pm_trades"})  # pm_trades - найти свои сделки
        if a.mode == "live":
            emit(C.c(C.R, "РЕАЛЬНАЯ ТОРГОВЛЯ. Вариант {variant}, {size} шейров на ордер; лимиты: {max_orders_per_window} "
                          "ордеров и ${max_spend_per_window} на окно, ${max_spend_per_day} и убыток ${max_loss_per_day} "
                          "за сутки. Аварийная остановка: создать файл {stop_file} в папке программы.".format(**lcfg)))
            if input("Введите ДА, чтобы начать реальную торговлю: ").strip().upper() != "ДА":
                raise SystemExit("отменено")
        emit(C.c(C.M, f"Бумажные счета торгуют клипом {a.clip:.0f} шейров (ключ --clip); живые ордера - "
                      f"{lcfg['size']} шейров (size в {a.live}). Живые ордера в консоли помечены [LIVE ...]."))
        trader = LiveTrader(lcfg, a.mode, pmx, pmx.w, ui)
        trader.connect()
        pmx.paper.listener = Fanout(ui, trader)
    else:
        pmx.paper.listener = ui

    async def sampler():
        cur = None
        while True:
            await asyncio.sleep(0.25)
            now = clock.now()
            win = pmx.current_window(now)
            if win is None or chart is None:
                continue
            if cur != win.start:
                cur = win.start
                chart.reset(win.start, win.ptb)
            s = pmx.src
            chart.push(win, now, (s.get("bybit") or {}).get("px"), (s.get("coinbase") or {}).get("px"), ui.mtm(win),
                       pmx.bn_mid if cfg.paper_btc_source not in ("bybit", "coinbase") else None)

    async def run_all():
        emit(C.c(C.B, f"Бумажный бот запущен. Варианты: {', '.join(v.name for v in cfg.variants)}; "
                      f"задержки: {cfg.latencies_ms} мс; подробно показываю [{ui.main[0]} @{ui.main[1]}мс]. "
                      f"Сделки пишутся в {os.path.abspath(cfg.data_dir)}"))
        extra = [trader.keepalive(), trader.warm_loop(), trader.presign_loop()] if trader is not None else []
        await asyncio.gather(pmx.main(), sampler(), ui.status_loop(), *extra)

    def worker():
        try:
            asyncio.run(run_all())
        except Exception as ex:
            log("bot", f"остановка из-за ошибки: {ex!r}")

    try:
        if chart is None:
            worker()
        else:
            th = threading.Thread(target=worker, daemon=True)
            th.start()
            chart.show_blocking()
    except KeyboardInterrupt:
        pass
    finally:
        if chart is not None:
            chart.stopped = True
        emit("Итоги бумажных счетов:")
        pmx.paper.print_summary()
        if trader is not None:
            trader.shutdown()
        pmx.w.close()
        flush_console()


if __name__ == "__main__":
    main()
