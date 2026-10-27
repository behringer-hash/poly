"""Пульс рынка (строка в консоли раз в секунду) и панель состояния (файл panel.txt, перезаписывается раз в секунду).

Пульс: время до конца окна, bid/ask Up и Down, TWAP60 минус price to beat, спот Binance (к price to beat и за 1 с), фьючерс.
Панель - всё в одном месте, смотреть во втором окне tmux:  ./run_panel.sh live  (или: watch -t -n 1 cat data_live/panel.txt)
  * рынок: окно, книга, PTB, TWAP60, Chainlink, отставание книги Polymarket;
  * Binance: цена, ход за 100 мс и за 1 с, задержка сделок до бота (p50/p90/max за минуту), σ, сделок за минуту;
  * триггер: сколько центов сдвига цены Up даёт $1 хода сейчас, ход в $ для слабого / сильного сигнала,
    максимум |ΔF| за 10 и 60 с, число сигналов и пропусков;
  * заявки: открыто, поставлено, исполнено, время ответа сервера, траты за сутки, PnL закрытых окон;
  * последние сигналы: ход, ΔF, цена заявки, задержки биржа→бот | сигнал→отправка | ответ сервера, итог.
"""
from __future__ import annotations

import asyncio
import os
from datetime import datetime

from common import clock, emit, log
from jump import fair_shift

TIER = {"strong": "сильн.", "weak": "слаб."}
DIM, RST = "\033[90m", "\033[0m"      # пульс - серым, чтобы строки СИГНАЛ / ЗАЯВКА / ИТОГ выделялись
SRC = {"fut": "фьючерс", "spot": "спот"}


def hms(t, ms=False):
    s = datetime.fromtimestamp(t).strftime("%H:%M:%S.%f")
    return s[:-3] if ms else s[:8]


def f(x, fmt="+.1f", na="—"):
    return na if x is None else format(x, fmt)


def usd(x):
    return "—" if x is None else f"{x:+.1f}$"


def qs(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p * len(xs)))] if xs else None


class MarketPanel:
    def __init__(self, jt, pm, trader, mode: str, path: str | None, pulse_sec: float):
        self.jt, self.pm, self.trader, self.mode = jt, pm, trader, mode
        self.path, self.pulse_sec = path, pulse_sec
        self.lag_hist = []          # отставание книги Polymarket по секундам за минуту

    # ------------------------------------------------------------------ данные
    def last_value(self, d: dict, now: float, back: int = 20):
        sec = int(now)
        for s in range(sec, sec - back, -1):
            v = d.get(s)
            if v is not None:
                return v, sec - s
        return None, None

    def snapshot(self, now: float) -> dict:
        pm, jt = self.pm, self.jt
        win = pm.current_window(now)
        x = dict(now=now, win=win)
        if win is not None:
            bu, bd = win.books["Up"], win.books["Down"]
            x.update(T=win.end - now, up=(bu.bb, bu.ba, bu.bids.get(bu.bb) if bu.bb else None, bu.asks.get(bu.ba) if bu.ba else None),
                     dn=(bd.bb, bd.ba, bd.bids.get(bd.bb) if bd.bb else None, bd.asks.get(bd.ba) if bd.ba else None),
                     mid=(bu.bb + bu.ba) / 2 if bu.bb is not None and bu.ba is not None else None,
                     ptb=getattr(win, "ptb", None), lag=getattr(win, "book_lag_ms", None))
        tw, tw_age = self.last_value(getattr(pm, "tw", {}) or {}, now)
        cl, cl_age = self.last_value(getattr(pm, "cl", {}) or {}, now)
        x.update(tw=tw, tw_age=tw_age, cl=cl, cl_age=cl_age)
        src = {}
        for name, s in jt.src.items():
            p1 = s.price_before(s.last_T - 1000) if s.last_T is not None else None
            lats = [l for t, l in s.lat_hist if t >= now - 60]
            src[name] = dict(px=s.last_px, dS=s.last_dS, d1=(s.last_px - p1) if (p1 is not None and s.last_px is not None) else None,
                             lat50=qs(lats, .5), lat90=qs(lats, .9), latmax=max(lats) if lats else None, n=len(lats),
                             sigma=s.sig.sigma(), ready=s.sigma_ready(int(jt.c["jump_sigma_min_sec"])),
                             silent=(now - s.alive) if s.alive else None)
        x["src"] = src
        return x

    # ------------------------------------------------------------------ пульс
    def state_text(self) -> str:
        """Пока набирается волатильность - сколько ждать сигналов; потом - счётчики сигналов, исполнений и PnL."""
        jt, tr = self.jt, self.trader
        need = int(jt.c["jump_sigma_min_sec"])
        left = [need - len(s.sig.diffs) for s in jt.src.values() if not s.sigma_ready(need)]
        if len(left) == len(jt.src):
            m = max(0, min(left))
            return f"σ набирается: сигналы через {m // 60}:{m % 60:02d}"
        st = jt.stats
        txt = f"сигналов {st['strong'] + st['weak']} (сильн. {st['strong']})"
        if tr is not None:
            txt += f", исполнено {tr.mstats['filled']}, PnL {tr.total_pnl:+.2f}$"
        return txt

    def pulse_line(self, x: dict) -> str:
        if x.get("win") is None:
            return f"{DIM}{hms(x['now'])} ПУЛЬС нет окна | {self.state_text()}{RST}"
        up, dn, ptb = x["up"], x["dn"], x.get("ptb")
        sp = x["src"].get("spot", {})
        fu = x["src"].get("fut", {})
        d_tw = (x["tw"] - ptb) if (x["tw"] is not None and ptb is not None) else None
        d_sp = (sp.get("px") - ptb) if (sp.get("px") is not None and ptb is not None) else None
        return (f"{DIM}{hms(x['now'])} ПУЛЬС T-{x['T']:3.0f}с | Up {f(up[0], '.2f')}/{f(up[1], '.2f')}  Down {f(dn[0], '.2f')}/{f(dn[1], '.2f')}"
                f" | TWAP60−PTB {usd(d_tw)} | спот {f(sp.get('px'), '.1f')} (−PTB {usd(d_sp)}, 1с {usd(sp.get('d1'))})"
                f" | фьюч {f(fu.get('px'), '.1f')} (1с {usd(fu.get('d1'))}) | {self.state_text()}{RST}")

    # ------------------------------------------------------------------ панель
    def panel_text(self, x: dict) -> str:
        jt, tr, now = self.jt, self.trader, x["now"]
        c = jt.c
        t0 = getattr(tr, "t_start", None) or jt.t_start
        up_s = max(0, int(now - t0))
        L = [f"btc5m_jump [{self.mode}]  {hms(now)} (время сервера)   ВРЕМЯ РАБОТЫ {up_s // 3600} ч {up_s // 60 % 60:02d} мин "
             f"{up_s % 60:02d} с (запуск {hms(t0)})   панель обновляется раз в секунду", "─" * 108]
        pos = self.positions(now) if tr is not None else []
        if tr is not None:
            unreal = sum(p["mtm"] for p in pos if p["mtm"] is not None)
            L.append(f"PnL  закрытые окна {tr.total_pnl:+.2f}$ (сегодня {tr.day_pnl:+.2f}$) | открытые позиции по mid {unreal:+.2f}$ | "
                     f"ИТОГО {tr.total_pnl + unreal:+.2f}$" + ("   (dry/sign: исполнение теневое)" if self.mode != "live" else
                                                              "   (live: окна - по сверке с Polymarket, где она уже прошла)"))
        win = x.get("win")
        if win is None:
            L.append("РЫНОК  окна нет (ждём следующее)")
        else:
            up, dn, ptb = x["up"], x["dn"], x.get("ptb")
            self.lag_hist = [(t, v) for t, v in self.lag_hist if t >= now - 60]
            if x.get("lag") is not None:
                self.lag_hist.append((now, x["lag"]))
            lags = [v for _, v in self.lag_hist]
            L.append(f"РЫНОК  окно {hms(win.start)[:5]}–{hms(win.end)[:5]}, до конца {x['T']:.0f} с")
            L.append(f"  Up   bid {f(up[0], '.2f')} × {f(up[2], '.0f')}   ask {f(up[1], '.2f')} × {f(up[3], '.0f')}      "
                     f"Down bid {f(dn[0], '.2f')} × {f(dn[2], '.0f')}   ask {f(dn[1], '.2f')} × {f(dn[3], '.0f')}      mid Up {f(x.get('mid'), '.3f')}")
            sp = x["src"].get("spot", {}).get("px")
            L.append(f"  PTB {f(ptb, '.1f')} | TWAP60 {f(x['tw'], '.1f')} (−PTB {usd(x['tw'] - ptb if x['tw'] is not None and ptb is not None else None)},"
                     f" {f(x['tw_age'], '.0f')} с назад) | Chainlink {f(x['cl'], '.1f')} | спот − Chainlink "
                     f"{usd(sp - x['cl'] if sp is not None and x['cl'] is not None else None)}")
            L.append(f"  книга Polymarket: отставание сейчас {f(x.get('lag'), '.0f')} мс, за минуту p50/p90 "
                     f"{f(qs(lags, .5), '.0f')}/{f(qs(lags, .9), '.0f')} мс")
        L.append(f"BINANCE    {'цена':>10}  {'ход ' + format(jt.W, '.0f') + ' мс':>10}  {'за 1 с':>8}  "
                 f"{'до бота p50/p90/max, мс (1 мин)':>31}  {'σ $/√с':>7}  {'сделок/мин':>10}  {'тишина':>7}")
        for name, s in x["src"].items():
            lat = f"{f(s['lat50'], '.0f')} / {f(s['lat90'], '.0f')} / {f(s['latmax'], '.0f')}"
            L.append(f"  {SRC.get(name, name):8s} {f(s['px'], '.1f'):>10}  {usd(s['dS']):>10}  {usd(s['d1']):>8}  {lat:>31}  "
                     f"{s['sigma']:6.2f}{'' if s['ready'] else '*':1}  {s['n']:>10}  {f(s['silent'], '.1f'):>5} с")
        if any(not s["ready"] for s in x["src"].values()):
            L.append(f"  * σ ещё набирается (нужно {c['jump_sigma_min_sec']} с после запуска) - сигналов по этому источнику нет")
        # триггер
        pn = {"ask": "по ask", "ask1": "ask + 1 ц"}
        L.append(f"ТРИГГЕР  ΔF = φ(z)·w·ΔS/sd; слабый от {100 * float(c['jump_thr_weak']):.0f} ц (лимит {pn.get(c['jump_price_weak'], c['jump_price_weak'])}),"
                 f" сильный от {100 * float(c['jump_thr_strong']):.0f} ц (лимит {pn.get(c['jump_price_strong'], c['jump_price_strong'])})")
        if win is not None and x.get("mid") is not None and 0.01 < x["mid"] < 0.99 and x["T"] > 1:
            parts, need = [], []
            for name, s in x["src"].items():
                sens = 100 * fair_shift(x["mid"], x["T"], s["sigma"], 1.0)
                parts.append(f"{sens:.2f} ц ({SRC.get(name, name)})")
                need.append(f"{SRC.get(name, name)}: слабый от ${100 * float(c['jump_thr_weak']) / sens:.1f}, сильный от "
                            f"${100 * float(c['jump_thr_strong']) / sens:.1f}" if sens > 0 else f"{name}: —")
            L.append(f"  сейчас $1 хода за {jt.W:.0f} мс сдвигает цену Up на " + " / ".join(parts))
            L.append("  нужен ход: " + " | ".join(need))
        ev = [e for e in jt.evals if e[0] >= now - 60]
        e10 = [e for e in ev if e[0] >= now - 10]
        def mx(es):
            if not es:
                return "—"
            e = max(es, key=lambda e: abs(e[3]))
            return f"{100 * e[3]:+.1f} ц ({SRC.get(e[1], e[1])} {e[2]:+.1f}$ в {hms(e[0])})"
        L.append(f"  макс |ΔF| за 10 с: {mx(e10)}   за 60 с: {mx(ev)}   оценок ходов ≥${float(c['jump_min_move_usd']):g} за минуту: {len(ev)}")
        st = jt.stats
        s5 = [t for t, _ in jt.sig_hist if t >= now - 300]
        s5s = sum(1 for t, k in jt.sig_hist if t >= now - 300 and k == "strong")
        L.append(f"  сигналов с запуска: сильных {st['strong']}, слабых {st['weak']} | за 5 мин: сильных {s5s}, слабых {len(s5) - s5s}"
                 f" | пропуски: книга {st['skip_book']}, время {st['skip_time']}, цена {st['skip_price']}, σ {st['skip_sigma']}")
        # позиции
        if tr is not None:
            L.append("ПОЗИЦИИ  купленные токены (держим до исхода), средняя цена без комиссии"
                     + ("; live: по цене заявки - верхняя оценка" if self.mode == "live" else ""))
            if not pos:
                L.append("  нет")
            for p in pos:
                su = p["avg"]["Up"]
                sd_ = p["avg"]["Down"]
                both = f"{su + sd_:.3f}" if su is not None and sd_ is not None else "—"
                L.append(f"  окно {hms(p['start'])[:5]}–{hms(p['start'] + 300)[:5]}  Up {p['qty']['Up']:.0f} шт по {f(su, '.3f')} | "
                         f"Down {p['qty']['Down']:.0f} шт по {f(sd_, '.3f')} | сумма средних {both} | вложено ${p['cost']:.2f} "
                         f"(комиссии ${p['fee']:.2f})")
                L.append(f"  {'':18}если Up: {p['if']['Up']:+.2f}$, если Down: {p['if']['Down']:+.2f}$ | по mid сейчас: "
                         + ("—" if p["mtm"] is None else f"{p['mtm']:+.2f}$") + (f" | ждут итога заявок: {p['pending']:.0f} шт" if p["pending"] > 1e-9 else ""))
            L.extend(self.pnl_chart(list(tr.win_hist)[-20:]))
        # заявки
        if tr is not None:
            m = tr.mstats
            hh = list(tr.http_hist)
            orders = m["signals"] - m["skipped"]
            spend_lim = tr.c.get("max_spend_per_day")
            L.append(f"ЗАЯВКИ   открыто {len(tr.open)} | сигналов {m['signals']}, поставлено {orders}, пропущено {m['skipped']}, исполнено "
                     f"{m['filled']} ({m['filled'] / max(orders, 1):.0%}), {m['shares']:.0f} шт"
                     + (f" | по книге/сделкам рынка: {m['shadow_filled']}" if self.mode == "live" else ""))
            L.append(f"  ответ сервера (последние {len(hh)}): p50/p90 {f(qs(hh, .5), '.0f')}/{f(qs(hh, .9), '.0f')} мс | траты сегодня "
                     f"${tr.day_spend:.0f}" + (f" из ${spend_lim:.0f}" if spend_lim and spend_lim < 1e8 else "")
                     + f" | PnL закрытых окон {tr.total_pnl:+.2f}$")
            if tr.stopped_reason:
                L.append(f"  !!! ЗАЯВКИ НЕ СТАВЯТСЯ: {tr.stopped_reason} (нужен перезапуск после устранения причины)")
            le = getattr(tr, "last_error", None)
            if le:
                L.append(f"  последняя ошибка постановки {hms(le[0])}: {le[1]} {le[2][:150]}")
        # последние сигналы
        L.append("ПОСЛЕДНИЕ СИГНАЛЫ  задержки: биржа→бот | сигнал→отправка | ответ сервера")
        L.append("  время         сторона ступень источ.   ход      ΔF     заявка  bid/ask     задержки, мс          итог")
        for g in reversed(jt.recent_sigs):
            info = tr.recent.get(g["sid"], {}) if tr is not None else {}
            sent = (1000 * (info["t_sent"] - g["t"])) if info.get("t_sent") else None
            http = info.get("http_ms")
            if info.get("err"):
                res = f"НЕ ПОСТАВЛЕНА: {info['err'][:70]}"
            elif info.get("done"):
                fl = info.get("filled") or 0
                res = (f"ИСПОЛНЕНА {fl:.0f} @{info.get('px', 0):.2f}" + (" тейкер" if info.get("taker") else "")) if fl > 0 else "не исполнена"
            else:
                res = info.get("status", "")
            L.append(f"  {hms(g['t'], True)}  {g['outcome']:7s} {TIER.get(g['tier'], g['tier']):7s} {SRC.get(g['src'], g['src']):8s}"
                     f" {g['move']:+6.1f}$ {100 * g['dF']:+5.1f}ц   {f(info.get('q'), '.2f'):>5}  {g['bid']:.2f}/{g['ask']:.2f}"
                     f"   {g['lat_ms']:5.0f} | {f(sent, '.0f'):>4} | {f(http, '.0f'):>5}     {res}")
        return "\n".join(L) + "\n"

    def positions(self, now: float) -> list[dict]:
        """Позиции открытых (ещё не рассчитанных) окон: шейры и средняя цена по сторонам, сценарии исхода, оценка по mid."""
        out = []
        for slug, st in list(self.trader.win_stats.items()):
            fills = st.get("fills", [])
            qty = {"Up": 0.0, "Down": 0.0}
            val = {"Up": 0.0, "Down": 0.0}
            fee = 0.0
            for fl in fills:
                qty[fl["outcome"]] += fl["qty"]
                val[fl["outcome"]] += fl["q"] * fl["qty"]
                fee += fl.get("fee", 0.0)
            pending = sum(st.get("pending", {}).values())
            if qty["Up"] + qty["Down"] <= 1e-9 and pending <= 1e-9:
                continue
            try:
                start = int(str(slug).rsplit("-", 1)[-1])
            except ValueError:
                continue
            cost = val["Up"] + val["Down"] + fee
            win = self.pm.windows.get(start) if hasattr(self.pm, "windows") else None
            mtm = None
            if win is not None:
                mids = {}
                for side in ("Up", "Down"):
                    b = win.books[side]
                    mids[side] = (b.bb + b.ba) / 2 if b.bb is not None and b.ba is not None else None
                if all(mids[k] is not None for k in mids if qty[k] > 0):
                    mtm = sum(qty[k] * mids[k] for k in mids if qty[k] > 0) - cost
            out.append(dict(start=start, qty=qty, avg={k: (val[k] / qty[k] if qty[k] > 0 else None) for k in qty}, cost=cost,
                            fee=fee, pending=pending, mtm=mtm, **{"if": {k: qty[k] - cost for k in qty}}))
        return sorted(out, key=lambda p: p["start"])

    @staticmethod
    def pnl_chart(hist: list[dict], h: int = 4) -> list[str]:
        """Столбики PnL по окнам (старые слева): вверх - плюс, вниз - минус; высота по максимуму модуля."""
        if not hist:
            return ["PnL ПО ОКНАМ  закрытых окон пока нет"]
        vals = [x["pnl_api"] if x.get("pnl_api") is not None else x["pnl"] for x in hist]
        m = max(abs(v) for v in vals) or 1.0
        pos_n = sum(v > 1e-9 for v in vals)
        neg_n = sum(v < -1e-9 for v in vals)
        L = [f"PnL ПО ОКНАМ  последние {len(vals)}: сумма {sum(vals):+.2f}$, в плюсе {pos_n}, в минусе {neg_n}, без сделок/нулевых "
             f"{len(vals) - pos_n - neg_n}; лучшее {max(vals):+.2f}$, худшее {min(vals):+.2f}$, среднее {sum(vals) / len(vals):+.2f}$"]
        for lv in range(h, 0, -1):
            thr = m * (lv - 0.5) / h
            lab = f"{m:+7.2f}" if lv == h else " " * 7
            L.append(f"  {lab} │" + "".join(" ██" if v >= thr else "   " for v in vals))
        L.append(f"  {0:7.2f} ┼" + "───" * len(vals))
        for lv in range(1, h + 1):
            thr = m * (lv - 0.5) / h
            lab = f"{-m:+7.2f}" if lv == h else " " * 7
            L.append(f"  {lab} │" + "".join(" ██" if v <= -thr else "   " for v in vals))
        first, last = hms(hist[0]["start"])[:5], hms(hist[-1]["start"])[:5]
        L.append(f"  {'':7}  " + (f" {first}".ljust(max(3 * len(vals) - 5, 7)) + last if len(vals) > 1 else f" {first}"))
        return L

    def write_panel(self, text: str):
        tmp = self.path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, self.path)

    async def run(self):
        last_pulse = 0.0
        ready = {n: False for n in self.jt.src}
        need = int(self.jt.c["jump_sigma_min_sec"])
        emit(f"\033[93m[JUMP] первые {need // 60} мин после запуска бот набирает волатильность Binance - сигналов (СИГНАЛ / ЗАЯВКА / ИТОГ) "
             f"в это время нет; в строке ПУЛЬС видно, сколько осталось\033[0m")
        while True:
            now = clock.now()
            await asyncio.sleep(1.0 - (now % 1.0) + 0.002)
            now = clock.now()
            try:
                for n, s in self.jt.src.items():
                    if not ready[n] and s.sigma_ready(need):
                        ready[n] = True
                        emit(f"\033[92m[JUMP] волатильность {SRC.get(n, n)}а Binance набрана - сигналы по нему включены\033[0m")
                x = self.snapshot(now)
                if self.pulse_sec and now - last_pulse >= self.pulse_sec - 0.01:
                    last_pulse = now
                    emit(self.pulse_line(x))
                if self.path:
                    self.write_panel(self.panel_text(x))
            except Exception as ex:          # пульс и панель не должны мешать торговле
                log("panel", f"ошибка панели: {ex!r}"[:200])
                await asyncio.sleep(5)
