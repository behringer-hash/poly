"""Бумажная торговля: проверка гипотезы "покупка устаревшего ask после тика BTC".

Модели справедливой цены (рынок резолвится по 60-секундному TWAP Chainlink):

  anchor - берём текущий mid стороны и сдвигаем его на ход BTC с момента, когда
           этот mid последний раз менялся (то есть с момента, когда рынок последний
           раз "переоценил" книгу). Не зависит от калибровки абсолютной модели.
  abs    - абсолютная вероятность P(TWAP_конец >= price_to_beat), где текущая
           цена = Binance + базис к Chainlink, с учётом уже накопленной части TWAP
           в последнюю минуту окна.

Исполнение: ордер "купить до clip шейров по цене не выше увиденного ask" (FAK,
остаток не стоит в книге). Для каждой задержки L проверяем книгу через L мс:
если ask ещё там - исполняемся по уровням книги, иначе промах. Каждый вариант ×
каждая задержка - отдельный бумажный счёт.
"""
from __future__ import annotations

import asyncio
import math

from common import clock, emit, log, norm_cdf, norm_inv, taker_fee

PAPER_SCHEMAS = {
    "paper_signals": ["sig_id", "recv", "slug", "T", "outcome", "variant", "model", "reason",
                      "ask", "ask_sz", "bid", "bid_sz", "other_bid", "other_ask", "mid",
                      "fair_anchor", "fair_abs", "edge", "btc", "btc_move_since_anchor", "anchor_age",
                      "sigma", "basis", "ptb", "obi5", "btc_age_ms", "book_age_ms"],
    "paper_fills": ["sig_id", "variant", "latency_ms", "recv_sig", "recv_check", "slug", "outcome", "limit",
                    "status", "qty", "avg_px", "fee", "ask_at_check", "ask_sz_at_check"],
    "paper_markouts": ["sig_id", "variant", "latency_ms", "outcome", "avg_px", "mid_after", "markout_net_c"],
    "paper_windows": ["slug", "variant", "latency_ms", "winner", "settled_with", "up_qty", "up_cost",
                      "down_qty", "down_cost", "fees", "pnl", "cum_pnl"],
}


def settle_sd(T: float, sigma: float):
    """Стандартное отклонение итогового TWAP60 и вес текущей цены в нём.
    T >= 60: TWAP = S(end-60) + среднее приращений -> var = σ²(T-60) + σ²·60/3.
    T < 60:  часть TWAP уже известна, текущая цена входит с весом T/60,
             var = σ²·T³/(3·60²)."""
    if T >= 60:
        return sigma * math.sqrt(T - 40.0), 1.0
    return sigma * math.sqrt(max(T, 0.5) ** 3 / (3 * 3600.0)), T / 60.0


class Account:
    def __init__(self):
        self.pos: dict[str, dict[str, list[float]]] = {}  # slug -> outcome -> [qty, cost, fee]
        self.signals = 0
        self.fills = 0
        self.misses = 0
        self.qty = 0.0
        self.mk_sum = 0.0
        self.mk_n = 0
        self.pnl = 0.0
        self.windows = 0


class Paper:
    def __init__(self, cfg, pm, writer):
        self.cfg = cfg
        self.pm = pm
        self.w = writer
        self.acc = {(v.name, L): Account() for v in cfg.variants for L in cfg.latencies_ms}
        self.last_sig: dict[tuple, float] = {}
        self.sig_id = 0
        self.skipped_stale = 0
        self.listener = None  # внешний наблюдатель (консоль/график бота): on_signal/on_fill/on_markout/on_settle

    # ------------------------------------------------------------------ модель
    def prob_up_abs(self, win, now: float, T: float, sigma: float):
        pm = self.pm
        if win.ptb is None or pm.bn_mid is None or pm.basis is None:
            return None
        S = pm.bn_mid + pm.basis
        if T >= 60:
            mean, sd = S, sigma * math.sqrt(T - 40.0)
        else:
            a = win.end - 60
            nowsec = int(now + pm.offset_ms / 1000)
            known = [pm.cl.get(s, S) for s in range(a, min(nowsec, win.end))]
            rest = 60 - len(known)
            mean = (sum(known) + rest * S) / 60.0
            sd = sigma * math.sqrt(max(rest, 0.5) ** 3 / (3 * 3600.0))
        return norm_cdf((mean - win.ptb) / sd)

    @staticmethod
    def obi5(win, outcome):
        b = win.books[outcome]
        bl, al = b.levels(5)
        sb = sum(s for _, s in bl)
        sa = sum(s for _, s in al)
        return (sb - sa) / (sb + sa) if sb + sa > 0 else 0.0

    # ------------------------------------------------------------------ сигналы
    def evaluate(self, now: float, reason: str):
        cfg, pm = self.cfg, self.pm
        win = pm.current_window(now)
        if win is None or not win.ready() or not pm.src:
            return
        # живы ли источники цены (фид молчит дольше нормы - по нему не торгуем)
        alive = {k: (now - s["alive"] <= cfg.src_max_age.get(k, 3.0) and s["px"] is not None)
                 for k, s in pm.src.items()}
        primary = cfg.paper_btc_source
        if not any(alive.values()):
            self.skipped_stale += 1
            return
        T = win.end - now
        if T < cfg.min_T or now - win.start < cfg.min_elapsed:
            return
        # наша копия книги отстаёт от сервера (обрыв, перегрузка канала) - "устаревшие" ask в ней
        # не настоящие, сигналы по ней ложные; не торгуем ни на бумаге, ни вживую
        if win.book_lag_ms is not None and win.book_lag_ms > cfg.max_book_lag_ms:
            self.skipped_lag = getattr(self, "skipped_lag", 0) + 1
            return
        sigma = pm.sigma.sigma()
        sd, wgt = settle_sd(T, sigma)
        p_abs = self.prob_up_abs(win, now, T, sigma)
        for outcome, sgn, other in (("Up", 1, "Down"), ("Down", -1, "Up")):
            b = win.books[outcome]
            # книга этой стороны давно не обновлялась - поток завис (или биржа стоит): её ask не настоящий
            if now - b.last_update > cfg.max_book_age_ms / 1000:
                continue
            ask, bid = b.ba, b.bb
            if ask is None or bid is None or not (cfg.price_lo <= ask <= cfg.price_hi):
                continue
            mid = (ask + bid) / 2
            fee = taker_fee(ask, cfg.fee_rate)
            if b.z0_mid != mid:  # обратная функция нормального распределения - дорогая, считаем при смене mid
                b.z0_mid, b.z0 = mid, norm_inv(mid)
            z0 = b.z0

            def moves(anchors):
                """Ход цены каждого источника от якоря; None - источник недоступен."""
                def move(name):
                    s = pm.src.get(name)
                    a = anchors.get(name)
                    if not alive.get(name) or a is None:
                        return None
                    return s["px"] - a
                d = {}
                for name in ("bybit", "coinbase", "binance", primary):
                    d[name] = move(name)
                m_by, m_cb = d.get("bybit"), d.get("coinbase")
                # "both": меньший из двух ходов в пользу стороны (оба должны подтверждать)
                # "any": по источнику, где ход в пользу стороны больше всего (первый дошедший тик)
                avail = [m for m in (m_by, m_cb, d.get("binance")) if m is not None]
                d["any"] = (sgn * max(sgn * m for m in avail)) if avail else None
                d["both"] = None if m_by is None or m_cb is None else sgn * min(sgn * m_by, sgn * m_cb)
                d["primary"] = d.get(primary)
                return d

            dS_by_src = moves(b.anchor_px)
            dS_res = moves(b.anchor_px_res) if any(v.anchor == "residual" for v in cfg.variants) else {}
            dS = dS_by_src["primary"] if dS_by_src["primary"] is not None else 0.0
            fair_anc = norm_cdf(z0 + sgn * wgt * dS / sd)
            fair_abs = None if p_abs is None else (p_abs if sgn > 0 else 1 - p_abs)
            fired = []
            for v in cfg.variants:
                if v.model == "imbalance":
                    if reason != "binance_fut_book" or pm.fut_qi is None or sgn * pm.fut_qi < v.qi_min:
                        continue
                    prev = pm.fut_qi_prev
                    if prev is not None and sgn * prev >= v.qi_min:   # порог этого варианта уже был пересечён раньше
                        continue
                    if (v.v_price_lo and ask < v.v_price_lo) or (v.v_price_hi and ask > v.v_price_hi):
                        continue
                    if v.qi_confirm_k > 0:
                        mv = pm.momentum_move("binance_fut", 150)
                        sgm = pm.momentum_sigma("binance_fut")
                        if mv is None or sgm is None or sgn * mv < v.qi_confirm_k * sgm * 0.15 ** 0.5:
                            continue
                    key = (v.name, win.slug, outcome)
                    if now - self.last_sig.get(key, 0.0) < v.cooldown:
                        continue
                    self.last_sig[key] = now
                    fired.append((v, 0.0, sgn * pm.fut_qi))
                    continue
                if v.model == "momentum":
                    srcs = ("binance", "binance_fut") if v.mom_src == "binance_any" else (v.mom_src,)
                    if reason not in srcs:          # срабатываем только в момент прихода тика своего источника
                        continue
                    if (v.v_price_lo and ask < v.v_price_lo) or (v.v_price_hi and ask > v.v_price_hi):
                        continue
                    mv = pm.momentum_move(v.mom_src, v.mom_window_ms)
                    if v.mom_k > 0:
                        sgm = pm.momentum_sigma(v.mom_src)
                        if sgm is None:
                            continue
                        thr = v.mom_k * sgm * (v.mom_window_ms / 1000) ** 0.5
                    else:
                        thr = v.mom_usd
                    if mv is None or sgn * mv < thr:
                        continue
                    key = (v.name, win.slug, outcome)
                    if now - self.last_sig.get(key, 0.0) < v.cooldown:
                        continue
                    self.last_sig[key] = now
                    fired.append((v, 0.0, sgn * mv))
                    continue
                if v.model == "anchor":
                    dv = (dS_res if v.anchor == "residual" else dS_by_src).get(v.source)
                    if dv is None:
                        continue
                    fair = norm_cdf(z0 + sgn * wgt * dv / (sd * v.sigma_mult))
                else:
                    fair = fair_abs
                if fair is None:
                    continue
                edge = fair - ask - fee
                if edge < v.edge_thr:
                    continue
                key = (v.name, win.slug, outcome)
                if now - self.last_sig.get(key, 0.0) < v.cooldown:
                    continue
                self.last_sig[key] = now
                fired.append((v, edge, dv if v.model == "anchor" else dS))
            if not fired:
                continue
            ob = win.books[other]
            feats = (ask, b.asks.get(ask), bid, b.bids.get(bid), ob.bb, ob.ba, mid, fair_anc, fair_abs)
            obi = self.obi5(win, outcome)
            for v, edge, dv_used in fired:
                self.sig_id += 1
                sid = self.sig_id
                self.w.write("paper_signals", (
                    sid, now, win.slug, round(T, 3), outcome, v.name, v.model, reason, *feats, edge, pm.bn_mid,
                    dv_used, (now - b.anchor_ts) if b.anchor_ts else None, sigma, pm.basis, win.ptb, obi,
                    (now - pm.bn_recv) * 1000, (now - b.last_update) * 1000))
                limit = round(ask + (v.slip_c / 100 if v.model in ("momentum", "imbalance") else cfg.slippage_ticks * 0.01), 2)
                if self.listener is not None:
                    self.listener.on_signal(dict(
                        sid=sid, t=now, slug=win.slug, start=win.start, T=T, outcome=outcome, variant=v.name,
                        source=v.source, reason=reason, ask=ask, ask_sz=b.asks.get(ask), bid=bid, mid=mid,
                        fair=(norm_cdf(z0 + sgn * wgt * dv_used / (sd * v.sigma_mult)) if v.model == "anchor"
                              else ask if v.model in ("momentum", "imbalance") else fair_abs),
                        edge=edge, fee=taker_fee(ask, cfg.fee_rate), move=dv_used,
                        anchor_age=(now - b.anchor_ts) if b.anchor_ts else None, limit=limit))
                loop = asyncio.get_running_loop()
                for L in cfg.latencies_ms:
                    self.acc[(v.name, L)].signals += 1
                    loop.call_later(L / 1000, self.check_fill, sid, v, L, now, win, outcome, limit)

    # ------------------------------------------------------------------ исполнение
    def check_fill(self, sid, v, L, t_sig, win, outcome, limit):
        cfg = self.cfg
        now = clock.now()
        b = win.books[outcome]
        acc = self.acc[(v.name, L)]
        qty = cost = fee = 0.0
        if b.ready:
            for px in sorted(p for p in b.asks if p <= limit + 1e-9):
                take = min(b.asks[px], v.clip - qty)
                if take <= 0:
                    break
                qty += take
                cost += take * px
                fee += take * taker_fee(px, cfg.fee_rate)
        ok = qty >= cfg.min_fill - 1e-9
        top_ask = b.ba
        if not ok:
            acc.misses += 1
            self.w.write("paper_fills", (sid, v.name, L, t_sig, now, win.slug, outcome, limit, "miss",
                                         0, None, 0, top_ask, b.asks.get(top_ask) if top_ask else None))
            if self.listener is not None:
                self.listener.on_fill(dict(sid=sid, variant=v.name, L=L, t=now, t_sig=t_sig, slug=win.slug,
                                           start=win.start, outcome=outcome, status="miss", qty=0.0, avg=None,
                                           fee=0.0, limit=limit, ask_now=top_ask, pos=None))
            return
        avg = cost / qty
        acc.fills += 1
        acc.qty += qty
        p = acc.pos.setdefault(win.slug, {"Up": [0.0, 0.0, 0.0], "Down": [0.0, 0.0, 0.0]})[outcome]
        p[0] += qty
        p[1] += cost
        p[2] += fee
        self.w.write("paper_fills", (sid, v.name, L, t_sig, now, win.slug, outcome, limit, "fill",
                                     round(qty, 4), round(avg, 5), round(fee, 5), top_ask,
                                     b.asks.get(top_ask) if top_ask else None))
        if self.listener is not None:
            self.listener.on_fill(dict(sid=sid, variant=v.name, L=L, t=now, t_sig=t_sig, slug=win.slug,
                                       start=win.start, outcome=outcome, status="fill", qty=qty, avg=avg, fee=fee,
                                       limit=limit, ask_now=top_ask, pos=acc.pos.get(win.slug)))
        asyncio.get_running_loop().call_later(cfg.markout_sec, self.markout, sid, v, L, win, outcome, avg, fee / qty)

    def markout(self, sid, v, L, win, outcome, avg, fee_ps):
        mid = win.books[outcome].mid()
        if mid is None:
            return
        mk = (mid - avg - fee_ps) * 100
        acc = self.acc[(v.name, L)]
        acc.mk_sum += mk
        acc.mk_n += 1
        self.w.write("paper_markouts", (sid, v.name, L, outcome, round(avg, 5), mid, round(mk, 3)))
        if self.listener is not None:
            self.listener.on_markout(dict(sid=sid, variant=v.name, L=L, outcome=outcome, avg=avg, mid=mid, mk=mk))

    # ------------------------------------------------------------------ расчёт окна
    def settle(self, win, winner: str, used: str):
        any_pos = False
        results = {}
        for (name, L), acc in self.acc.items():
            pos = acc.pos.pop(win.slug, None)
            if not pos:
                continue
            any_pos = True
            up, dn = pos["Up"], pos["Down"]
            payout = up[0] if winner == "Up" else dn[0]
            pnl = payout - up[1] - dn[1] - up[2] - dn[2]
            acc.pnl += pnl
            acc.windows += 1
            self.w.write("paper_windows", (win.slug, name, L, winner, used, round(up[0], 3), round(up[1], 4),
                                           round(dn[0], 3), round(dn[1], 4), round(up[2] + dn[2], 4),
                                           round(pnl, 4), round(acc.pnl, 4)))
            results[(name, L)] = dict(pos=pos, pnl=pnl, cum=acc.pnl, fees=up[2] + dn[2])
        if self.listener is not None:
            self.listener.on_settle(win, winner, used, results)
        elif any_pos:
            log("paper", f"окно {win.slug} закрыто, победитель {winner} ({used})")
            self.print_summary()

    def print_summary(self):
        lines = ["вариант      задерж.  сигналы  исполн.  доля   маркаут5с(ц)  окон   PnL $"]
        for (name, L), a in self.acc.items():
            tried = a.fills + a.misses
            fr = a.fills / tried if tried else 0
            mk = a.mk_sum / a.mk_n if a.mk_n else float("nan")
            lines.append(f"{name:11s} {L:5d}мс  {a.signals:7d}  {a.fills:7d}  {fr:5.0%}  {mk:12.2f}  "
                         f"{a.windows:5d}  {a.pnl:+8.2f}")
        emit("\n".join(lines))
