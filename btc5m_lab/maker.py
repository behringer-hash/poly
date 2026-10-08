"""Бумажный мейкер: заявки на покупку обеих сторон по "справедливой цене минус запас".

Идея (как у изучаемого кошелька): стоять заявками в книге (без комиссии), быстро снимать и
переставлять их при движении BTC, держать купленное до конца окна; пара Up+Down дешевле $1 -
гарантированная прибыль.

Приближение к реальности:
  * задержки: заявка начинает действовать, а отмена - срабатывает только через place_ms /
    cancel_ms после решения бота (по нашим замерам ордер доходит до сервера за ~20-30 мс);
    время решения переводится в серверное время через смещение часов;
  * очередь: встаём В КОНЕЦ очереди на своём уровне цены. Впереди - весь объём уровня в момент
    постановки. Книга Polymarket общая: наша заявка BUY Up по q - это же ask Down по 1-q,
    поэтому уровень съедают и продажи Up по q, и покупки Down по 1-q;
  * исполнение только по реальным сделкам рынка (серверное время сделки внутри интервала жизни
    заявки): сначала съедается очередь впереди нас, потом наша заявка. Сделка "сквозь" наш уровень
    (продажа Up ниже q или покупка Down выше 1-q) означает, что уровень съеден целиком;
  * модель очереди "cons" - отмены чужих заявок впереди нас не учитываются (пессимистично),
    "prop" - при уменьшении уровня без сделок очередь впереди сокращается пропорционально;
    реальность между ними;
  * комиссия мейкера 0; ребейты не учитываются (реальный результат будет немного лучше).
"""
from __future__ import annotations

import asyncio
import math
from dataclasses import dataclass, field

from common import clock, emit, norm_cdf, norm_inv

MAKER_SCHEMAS = {
    "maker_fills": ["acct", "slug", "outcome", "price", "qty", "t_fill_srv", "t_placed_srv", "queue_at_join",
                    "fair_at_place", "mid_at_place", "T", "kind"],
    "maker_markouts": ["acct", "slug", "outcome", "price", "horizon_s", "mid", "markout_c"],
    "maker_windows": ["acct", "slug", "winner", "up_qty", "up_cost", "down_qty", "down_cost", "pairs", "pnl",
                      "cum_pnl", "fills", "quotes"],
}


@dataclass
class MVariant:
    name: str
    margin: float          # запас: заявка по справедливой цене минус margin
    queue: str = "cons"    # cons | prop
    size: float = 5.0


def maker_variants():
    out = []
    for m, tag in ((0.005, "05c"), (0.01, "1c"), (0.02, "2c")):
        for qm in ("cons", "prop"):
            out.append(MVariant(f"mm_{tag}_{qm}", m, qm))
    return out


@dataclass
class Quote:
    side: str
    price: float
    size: float
    t_active: float            # серверное время (мс), с которого заявка стоит в книге
    t_cancel: float = math.inf  # серверное время отмены
    ahead: float = 0.0          # объём впереди нас в очереди
    level_seen: float = 0.0     # объём уровня при последнем взгляде (для модели prop)
    filled: float = 0.0
    fair: float = 0.0
    mid: float = 0.0


@dataclass
class MAcct:
    v: MVariant
    quotes: dict = field(default_factory=dict)      # slug -> side -> Quote (текущая)
    retired: list = field(default_factory=list)     # отменённые, ещё способные исполниться до t_cancel
    pos: dict = field(default_factory=dict)         # slug -> side -> [qty, cost]
    last_replace: dict = field(default_factory=dict)
    pnl: float = 0.0
    fills: int = 0
    nquotes: dict = field(default_factory=dict)


class MakerPaper:
    def __init__(self, cfg, pm, writer, show=None):
        self.cfg, self.pm, self.w = cfg, pm, writer
        self.acc = {v.name: MAcct(v) for v in maker_variants()}
        self.show = show or "mm_1c_cons"
        self.place_ms = 25.0
        self.cancel_ms = 25.0
        self.min_replace_ms = 150.0
        self.max_side_qty = 60.0
        self.max_imbalance = 30.0
        self.stop_T = 10.0

    # ---------------------------------------------------------------- справедливая цена
    def fair(self, win, side, now):
        """Справедливая цена стороны по книге и ходу BTC с последней переоценки книги.
        Для заявок на покупку берём самый НЕБЛАГОПРИЯТНЫЙ ход среди источников: любой тик против
        нас сразу опускает справедливую цену и снимает заявку."""
        from paper import settle_sd
        b = win.books[side]
        mid = b.mid()
        if mid is None:
            return None, None
        sgn = 1 if side == "Up" else -1
        T = win.end - now
        sd, wgt = settle_sd(T, self.pm.sigma.sigma())
        moves = []
        for name, s in self.pm.src.items():
            a = b.anchor_px.get(name)
            if a is None or s.get("px") is None:
                continue
            if now - s.get("alive", 0) > self.cfg.src_max_age.get(name, 3.0):
                continue
            moves.append(sgn * (s["px"] - a))
        if not moves:
            return None, mid
        adverse = min(moves)
        z0 = norm_inv(min(max(mid, 0.005), 0.995))
        return norm_cdf(z0 + wgt * adverse / sd), mid

    # ---------------------------------------------------------------- постановка / снятие
    def srv_now(self, now):
        return now * 1000 + self.pm.offset_ms

    def _cancel(self, a, slug, side, now):
        q = a.quotes.get(slug, {}).pop(side, None)
        if q is not None:
            q.t_cancel = self.srv_now(now) + self.cancel_ms
            a.retired.append((slug, q))

    def requote(self, now):
        win = self.pm.current_window(now)
        if win is None or not win.ready():
            return
        T = win.end - now
        bad_book = ((win.book_lag_ms is not None and win.book_lag_ms > self.cfg.max_book_lag_ms) or
                    any(now - win.books[s].last_update > self.cfg.max_book_age_ms / 1000 for s in ("Up", "Down")))
        for a in self.acc.values():
            slug = win.slug
            pos = a.pos.setdefault(slug, {"Up": [0.0, 0.0], "Down": [0.0, 0.0]})
            for side in ("Up", "Down"):
                cur = a.quotes.get(slug, {}).get(side)
                if cur is not None and a.v.queue == "prop":
                    # уровень уменьшился не из-за сделок - часть очереди впереди отменилась
                    lvl_now = win.books[side].bids.get(cur.price, 0.0)
                    if cur.level_seen > 0 and lvl_now < cur.level_seen:
                        cur.ahead *= lvl_now / cur.level_seen
                    cur.level_seen = lvl_now
                target = None
                fair, mid = (None, None)
                if not bad_book and T > self.stop_T:
                    fair, mid = self.fair(win, side, now)
                    b = win.books[side]
                    other = "Down" if side == "Up" else "Up"
                    heavy = pos[side][0] - pos[other][0] >= self.max_imbalance
                    if (fair is not None and 0.08 <= fair <= 0.92 and b.ba is not None and not heavy
                            and pos[side][0] + a.v.size <= self.max_side_qty):
                        q = math.floor((fair - a.v.margin) * 100 + 1e-9) / 100
                        q = min(q, round(b.ba - 0.01, 2))          # только мейкер: ниже лучшего ask
                        if 0.02 <= q <= 0.97:
                            target = round(q, 2)
                if cur is not None and (target is None or cur.price > target + 1e-9):
                    self._cancel(a, slug, side, now)       # заявка стала слишком дорогой - снимаем сразу
                    cur = None
                if target is None:
                    continue
                if cur is not None and abs(cur.price - target) < 1e-9:
                    continue
                last = a.last_replace.get((slug, side), 0)
                if cur is not None and (now - last) * 1000 < self.min_replace_ms:
                    continue                                # поднять заявку можно не чаще раза в 150 мс
                if cur is not None:
                    self._cancel(a, slug, side, now)
                lvl = win.books[side].bids.get(target, 0.0)
                qn = Quote(side, target, a.v.size, self.srv_now(now) + self.place_ms, ahead=lvl, level_seen=lvl,
                           fair=fair or 0.0, mid=mid or 0.0)
                a.quotes.setdefault(slug, {})[side] = qn
                a.last_replace[(slug, side)] = now
                a.nquotes[slug] = a.nquotes.get(slug, 0) + 1

    # ---------------------------------------------------------------- сделки рынка
    def on_trade(self, win, token, taker_side, price, size, srv_ts):
        """Сделка рынка: token - сторона, на которой прошла сделка, taker_side - B/S тейкера."""
        now = clock.now()
        try:
            price, size, srv_ts = float(price), float(size), float(srv_ts)
        except (TypeError, ValueError):
            return
        for a in self.acc.values():
            cands = [(win.slug, q) for q in a.quotes.get(win.slug, {}).values()]
            cands += [(s, q) for s, q in a.retired if s == win.slug]
            for slug, q in cands:
                if q.filled >= q.size - 1e-9 or not (q.t_active <= srv_ts < q.t_cancel):
                    continue
                other = "Down" if q.side == "Up" else "Up"
                at_level = through = False
                if token == q.side and taker_side == "S":
                    at_level = abs(price - q.price) < 1e-9
                    through = price < q.price - 1e-9
                elif token == other and taker_side == "B":
                    mirror = round(1 - q.price, 2)
                    at_level = abs(price - mirror) < 1e-9
                    through = price > mirror + 1e-9
                if not (at_level or through):
                    continue
                if at_level:
                    q.level_seen = max(0.0, q.level_seen - size)  # это уменьшение уровня - сделка, а не отмена
                if through:
                    got = q.size - q.filled
                    q.ahead = 0.0
                else:
                    q.ahead -= size
                    if q.ahead >= 0:
                        continue
                    got = min(q.size - q.filled, -q.ahead)
                    q.ahead = 0.0
                q.filled += got
                self._fill(a, win, q, got, srv_ts, now, "through" if through else "queue")
        # отменённые и полностью исполненные заявки старше 5 с больше не нужны
        cutoff = self.srv_now(now) - 5000
        for a in self.acc.values():
            a.retired = [(s, q) for s, q in a.retired if q.t_cancel > cutoff and q.filled < q.size - 1e-9]

    def _fill(self, a, win, q, qty, srv_ts, now, kind):
        pos = a.pos.setdefault(win.slug, {"Up": [0.0, 0.0], "Down": [0.0, 0.0]})
        pos[q.side][0] += qty
        pos[q.side][1] += qty * q.price
        a.fills += 1
        T = win.end - now
        self.w.write("maker_fills", (a.v.name, win.slug, q.side, q.price, round(qty, 4), int(srv_ts), int(q.t_active),
                                     round(q.ahead, 2), round(q.fair, 4), round(q.mid, 4), round(T, 1), kind))
        if a.v.name == self.show:
            up, dn = pos["Up"], pos["Down"]
            emit(f"\033[96m[MAKER {a.v.name}] купили {q.side} {qty:.1f} шт по {q.price:.2f} ({'сквозь уровень' if kind == 'through' else 'по очереди'}), "
                 f"справедливая была {q.fair:.3f} | позиция окна Up {up[0]:.0f} (ср. {up[1] / up[0] if up[0] else 0:.3f}) / "
                 f"Down {dn[0]:.0f} (ср. {dn[1] / dn[0] if dn[0] else 0:.3f}) | T-{T:.0f} с\033[0m")
        loop = asyncio.get_event_loop()
        for h in (5, 30):
            loop.call_later(h, self._markout, a.v.name, win, q.side, q.price, h)

    def _markout(self, acct, win, side, price, h):
        mid = win.books[side].mid()
        mk = None if mid is None else round(100 * (mid - price), 3)
        self.w.write("maker_markouts", (acct, win.slug, side, price, h, mid, mk))

    # ---------------------------------------------------------------- итог окна
    def settle(self, win, winner):
        lines = []
        for a in self.acc.values():
            a.quotes.pop(win.slug, None)
            pos = a.pos.pop(win.slug, None)
            nq = a.nquotes.pop(win.slug, 0)
            if not pos or (pos["Up"][0] == 0 and pos["Down"][0] == 0):
                self.w.write("maker_windows", (a.v.name, win.slug, winner, 0, 0, 0, 0, 0, 0, round(a.pnl, 4), 0, nq))
                continue
            up, dn = pos["Up"], pos["Down"]
            payout = up[0] if winner == "Up" else dn[0]
            pnl = payout - up[1] - dn[1]
            a.pnl += pnl
            pairs = min(up[0], dn[0])
            self.w.write("maker_windows", (a.v.name, win.slug, winner, round(up[0], 4), round(up[1], 4), round(dn[0], 4),
                                           round(dn[1], 4), round(pairs, 4), round(pnl, 4), round(a.pnl, 4),
                                           a.fills, nq))
            lines.append(f"{a.v.name}: Up {up[0]:.0f}/Down {dn[0]:.0f}, PnL {pnl:+.2f}$, итого {a.pnl:+.2f}$")
        if lines:
            emit("\033[96m[MAKER] окно закрыто, победил " + winner + " | " + " | ".join(lines) + "\033[0m")
