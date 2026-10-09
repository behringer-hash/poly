"""Реплей бумажной стратегии «anchor» на записанных данных (виртуальное время, без сети и без ожидания).

    python replay.py data/2026-10-07 --source binance_fut [--latencies 150,300,450,600] [--hold-s 5]

Модель та же, что в paper.py (используются те же settle_sd / norm_cdf / RollingSigma):
  * якорь - цена источника в момент, когда mid книги последний раз менялся;
  * справедливая цена стороны = Φ(inv(mid) + sgn·w·(S − якорь)/(sd·sigma_mult));
  * сигнал, если fair − ask − комиссия >= порога; не чаще раза в секунду на сторону;
  * ордер FAK доходит через L мс; цена исполнения - ask сервера Polymarket на этот момент
    (время сервера = recv − d), исполнение, если он не выше увиденного ask + переплата и объёма хватает.
Отличия от живого движка: исполнение по одному лучшему уровню (глубина не записана), нет вариантов «both/any»
и «residual», нет фильтра book_lag. Результат: по каждому варианту и задержке - доля исполнений, ц/шейр по
официальному исходу и по mid через hold-s секунд, ИИ bootstrap'ом по окнам, разбивка по дням.
"""
from __future__ import annotations

import argparse
import itertools
from dataclasses import dataclass

import numpy as np
import pandas as pd

from common import RollingSigma, norm_cdf, norm_inv
from lead_lag import FEE, PM, read
from paper import settle_sd

WINDOW = 300


@dataclass(frozen=True)
class Params:
    thr: float
    sigma_mult: float = 1.0
    slip_c: float = 0.0
    cooldown_s: float = 1.0

    @property
    def name(self) -> str:
        return f"thr{self.thr:g}_s{self.sigma_mult:g}_slip{self.slip_c:g}"


def _levels(s) -> list[tuple[float, float]]:
    if not isinstance(s, str) or not s:
        return []
    return [(float(a), float(b)) for a, b in (x.split(":") for x in s.split("|"))]


def bybit_mid(root: str) -> tuple[np.ndarray, np.ndarray]:
    """Цена Bybit как в живом боте (pm.bybit_lite): середина лучших bid/ask из orderbook.1 (поток by_book1,
    снимки и дельты), а если верх книги неизвестен или перекрещен - цена последней сделки (by_trade)."""
    bk = read(root, "by_book1", ["recv_ms", "type", "bids", "asks"])
    tr = read(root, "by_trade", ["recv_ms", "price"])
    ev = [(t, 0, ty, b, a) for t, ty, b, a in zip(bk.recv_ms, bk.type, bk.bids, bk.asks)] if len(bk) else []
    ev += [(t, 1, p, None, None) for t, p in zip(tr.recv_ms, tr.price)] if len(tr) else []
    ev.sort(key=lambda e: (e[0], e[1]))
    bid = ask = trade_px = last = None
    ts, pxs = [], []
    for t, kind, x, b, a in ev:
        if kind == 1:
            trade_px = float(x)
        else:
            snap = x == "s"
            for side, raw in (("b", b), ("a", a)):
                lv = _levels(raw)
                live = [p for p, q in lv if q > 0]
                gone = {p for p, q in lv if q == 0}
                cur = bid if side == "b" else ask
                if live:
                    cur = max(live) if side == "b" else min(live)
                elif snap or (cur is not None and cur in gone):
                    cur = None
                if side == "b":
                    bid = cur
                else:
                    ask = cur
        px = (bid + ask) / 2 if bid is not None and ask is not None and ask > bid else trade_px
        if px is None or px == last:
            continue
        last = px
        ts.append(float(t))
        pxs.append(px)
    return np.array(ts), np.array(pxs)


def load_source(root: str, name: str) -> tuple[np.ndarray, np.ndarray]:
    """Тики источника цены BTC: (recv_ms, цена), отсортированы по времени получения."""
    if name == "bybit":
        return bybit_mid(root)
    if name == "bybit_trade":
        d = read(root, "by_trade", ["recv_ms", "price"])
    elif name == "binance_fut":
        d = read(root, "bnf_agg", ["recv_ms", "price"])
    elif name == "binance":
        d = read(root, "bn_agg", ["recv_ms", "price"])
    elif name == "bitstamp":
        d = read(root, "bs_trade", ["recv_ms", "price"])
    elif name == "coinbase":
        d = read(root, "cb_ticker", ["recv_ms", "bid", "ask"])
        d = d.dropna(subset=["bid", "ask"])
        d["price"] = (d.bid + d.ask) / 2
    elif name == "rtds":
        d = read(root, "rtds", ["recv_ms", "feed", "value"])
        d = d[d.feed == "rb"].rename(columns={"value": "price"})
    else:
        raise ValueError(f"неизвестный источник {name}")
    d = d.dropna(subset=["price"]).sort_values("recv_ms", kind="stable")
    return d.recv_ms.values.astype(float), d.price.values.astype(float)


def collect_signals(pm_top: pd.DataFrame, src_t: np.ndarray, src_px: np.ndarray, params: list[Params], *,
                    max_age_ms: float = 1000, max_book_lag_ms: float = 400, min_T: float = 5, min_elapsed: float = 3,
                    lo: float = 0.05, hi: float = 0.95) -> list[dict]:
    """Проходит по событиям (изменения цен Up и тики источника) в порядке получения и собирает сигналы."""
    u = pm_top[pm_top.o == "U"].sort_values("recv_ms", kind="stable")
    pt, pw = u.recv_ms.values.astype(float), u.w.values.astype(np.int64)
    pbid, pask = u.bid.values.astype(float), u.ask.values.astype(float)
    pd_ = u.d.values.astype(float)
    times = np.concatenate([pt, src_t])
    kind = np.concatenate([np.zeros(len(pt), np.int8), np.ones(len(src_t), np.int8)])
    order = np.argsort(times, kind="stable")
    rs = RollingSigma(900, 5.0)
    out: list[dict] = []
    last_sig: dict[tuple, float] = {}
    inv_cache: dict[float, float] = {}
    bid = ask = mid = np.nan
    cur_d = 0.0
    w_cur = -1
    anchor = None
    last_px = last_ts = None
    n_pm = len(pt)

    def evaluate(t: float):
        if anchor is None or last_px is None or not (np.isfinite(bid) and np.isfinite(ask)):
            return
        w = int(t // 1000 // WINDOW * WINDOW)
        if w != w_cur or t - last_ts > max_age_ms or cur_d > max_book_lag_ms:   # лаг книги: как в движке, по такой книге не торгуем
            return
        T = w + WINDOW - t / 1000
        if T < min_T or t / 1000 - w < min_elapsed:
            return
        sd, wgt = settle_sd(T, rs.sigma())
        dS = last_px - anchor
        for sgn in (1, -1):
            a = ask if sgn > 0 else 1 - bid
            b = bid if sgn > 0 else 1 - ask
            if not (lo <= a <= hi):
                continue
            m = round((a + b) / 2, 6)
            z0 = inv_cache.get(m)
            if z0 is None:
                z0 = inv_cache[m] = norm_inv(m)
            fee = FEE * a * (1 - a)
            for p in params:
                edge = norm_cdf(z0 + sgn * wgt * dS / (sd * p.sigma_mult)) - a - fee
                if edge < p.thr:
                    continue
                key = (p, w, sgn)
                if t - last_sig.get(key, -1e18) < p.cooldown_s * 1000:
                    continue
                last_sig[key] = t
                out.append(dict(p=p, w=w, sgn=sgn, t=t, view=a, edge=edge))

    for i in order:
        t = times[i]
        if kind[i] == 1:
            px = src_px[i - n_pm]
            rs.update(t / 1000, px)
            last_px, last_ts = px, t
            evaluate(t)
            continue
        j = i
        w = int(pw[j])
        if w != w_cur:                       # новое окно: состояние книги и якорь начинаются заново
            w_cur, mid, anchor = w, np.nan, None
            bid = ask = np.nan
        moved = pbid[j] != bid and not (np.isnan(pbid[j]) and np.isnan(bid)) or \
            pask[j] != ask and not (np.isnan(pask[j]) and np.isnan(ask))
        bid, ask = pbid[j], pask[j]
        cur_d = pd_[j]
        if np.isfinite(bid) and np.isfinite(ask):
            new_mid = (bid + ask) / 2
            if new_mid != mid:
                mid = new_mid
                if last_px is not None:
                    anchor = last_px
        if moved:
            evaluate(t)
    return out


def execute(sigs: list[dict], pm: PM, winners: dict[int, str], latencies: list[int], *, hold_s: float = 5,
            clip: float = 5, min_fill: float = 5, view: str = "srv", exit_s: tuple = (), exit_ms: float = 205
            ) -> pd.DataFrame:
    """Исполнение сигналов с задержками. view="srv" - состояние книги на сервере Polymarket в момент матча (реально);
    view="rcv" - то, что к этому моменту дошло до нас (так проверяет исполнение бумажный движок, оптимистично).
    exit_s - моменты досрочного выхода (секунды после матча входа): продажа тейкером по bid сервера через exit_ms
    после решения о выходе, с комиссией на выходе; если bid пуст или объёма мало - держим до экспирации."""
    rows = []
    for s in sigs:
        p, w, sgn, t = s["p"], s["w"], s["sgn"], s["t"]
        limit = round(s["view"] + p.slip_c / 100, 4)
        win = winners.get(w)
        for L in latencies:
            m = pm.state(w, t + L, view)
            e = pm.state(w, t + L + hold_s * 1000, view)
            fill, px, qty = False, np.nan, 0.0
            if m is not None:
                if sgn > 0:
                    px, size = m[1], m[3]
                else:
                    px, size = (1 - m[0] if np.isfinite(m[0]) else np.nan), m[2]
                if np.isfinite(px) and np.isfinite(size) and px <= limit + 1e-9 and min(clip, size) >= min_fill - 1e-9:
                    fill, qty = True, min(clip, size)
            mk = settle = np.nan
            xs = {f"x{h:g}": np.nan for h in exit_s}
            if fill:
                fee = FEE * px * (1 - px)
                if e is not None and np.isfinite(e[0]) and np.isfinite(e[1]):
                    em = (e[0] + e[1]) / 2
                    mk = ((em if sgn > 0 else 1 - em) - px - fee) * 100
                if win is not None:
                    settle = ((1.0 if (win == "Up") == (sgn > 0) else 0.0) - px - fee) * 100
                for h in exit_s:
                    x = pm.state(w, t + L + h * 1000 + exit_ms, view)
                    bid_t = bsz_t = np.nan
                    if x is not None:
                        bid_t, bsz_t = (x[0], x[2]) if sgn > 0 else ((1 - x[1]) if np.isfinite(x[1]) else np.nan, x[3])
                    if np.isfinite(bid_t) and np.isfinite(bsz_t) and bsz_t >= qty:
                        xs[f"x{h:g}"] = (bid_t - px - fee - FEE * bid_t * (1 - bid_t)) * 100
                    else:
                        xs[f"x{h:g}"] = settle                # выйти нечем - держим до экспирации
            rows.append(dict(variant=p.name, L=L, w=w, day=int(w // 86400), fill=fill, px=px, qty=qty, mk=mk,
                             settle=settle, **xs))
    return pd.DataFrame(rows)


def summarize(df: pd.DataFrame, clip: float = 5, n_boot: int = 1500, seed: int = 0) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    out = []
    for (v, L), d in df.groupby(["variant", "L"]):
        f = d[d.fill & d.settle.notna()]
        pnl = np.where(d.fill & d.settle.notna(), d.settle * d.qty / clip, 0.0)   # ц на «шейр попытки»
        g = pd.DataFrame({"w": d.w.values, "v": pnl}).groupby("w").v.agg(["sum", "size"])
        idx = rng.integers(0, len(g), (n_boot, len(g)))
        bs = g["sum"].values[idx].sum(1) / g["size"].values[idx].sum(1)
        per_day = d.assign(v=pnl).groupby("day").v.mean()
        out.append(dict(вариант=v, L=L, сигн=len(d), окон=d.w.nunique(), исполн=round(d.fill.mean(), 3),
                        цшейр_расчёт=round(f.settle.mean(), 2) if len(f) else np.nan,
                        цшейр_маркаут=round(d[d.fill].mk.mean(), 2) if d.fill.any() else np.nan,
                        цсигнал=round(pnl.mean(), 2), ИИ_низ=round(np.percentile(bs, 2.5), 2),
                        ИИ_верх=round(np.percentile(bs, 97.5), 2),
                        дни=" ".join(f"{x:+.1f}" for x in per_day.values)))
    return pd.DataFrame(out)


def summarize_exit(df: pd.DataFrame, exit_s, clip: float = 5, n_boot: int = 1500, seed: int = 0) -> pd.DataFrame:
    """ц на «шейр попытки» для стратегии «вход - досрочный выход через h секунд» (неисполненные ордера = 0)."""
    rng = np.random.default_rng(seed)
    out = []
    for (v, L), d in df.groupby(["variant", "L"]):
        for h in exit_s:
            col = f"x{h:g}"
            ok = d.fill & d[col].notna()
            pnl = np.where(ok, d[col].fillna(0) * d.qty / clip, 0.0)
            g = pd.DataFrame({"w": d.w.values, "v": pnl}).groupby("w").v.agg(["sum", "size"])
            idx = rng.integers(0, len(g), (n_boot, len(g)))
            bs = g["sum"].values[idx].sum(1) / g["size"].values[idx].sum(1)
            out.append(dict(вариант=v, L=L, выход_с=h, сигн=len(d), окон=d.w.nunique(), исполн=round(d.fill.mean(), 3),
                            цшейр_исп=round(d.loc[ok, col].mean(), 2) if ok.any() else np.nan,
                            цсигнал=round(pnl.mean(), 2), ИИ_низ=round(np.percentile(bs, 2.5), 2),
                            ИИ_верх=round(np.percentile(bs, 97.5), 2)))
    return pd.DataFrame(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+", help="папки с данными (по одной на день или одна на всё)")
    ap.add_argument("--source", default="binance_fut", help="bybit (середина книги, как в боте) | bybit_trade | coinbase | binance_fut | binance | bitstamp | rtds")
    ap.add_argument("--latencies", default="150,300,450,600")
    ap.add_argument("--thr", default="0.01,0.02,0.03,0.05")
    ap.add_argument("--sigma-mult", default="0.75,1,1.5")
    ap.add_argument("--slip-c", default="0,3")
    ap.add_argument("--hold-s", type=float, default=5)
    ap.add_argument("--view", default="srv", choices=["srv", "rcv"],
                    help="srv - книга на сервере в момент матча (реально); rcv - как проверяет бумажный движок (оптимистично)")
    ap.add_argument("--exit-s", default="", help="досрочный выход через N секунд после входа, через запятую (2,5,10,30,60)")
    a = ap.parse_args()
    pd.set_option("display.width", 250)
    exit_s = tuple(float(x) for x in a.exit_s.split(",") if x)
    params = [Params(float(t), float(s), float(sl)) for t, s, sl in itertools.product(
        a.thr.split(","), a.sigma_mult.split(","), a.slip_c.split(","))]
    lat = [int(x) for x in a.latencies.split(",")]
    res = []
    for root in a.roots:
        pm_top = read(root, "pm_top")
        wn = read(root, "windows").drop_duplicates("slug", keep="last")
        winners = dict(zip(wn.start.astype(int), wn.official_winner))
        t, px = load_source(root, a.source)
        sigs = collect_signals(pm_top, t, px, params)
        res.append(execute(sigs, PM(pm_top), winners, lat, hold_s=a.hold_s, view=a.view, exit_s=exit_s))
        print(f"{root}: тиков {len(t)}, сигналов {len(sigs)}")
    allr = pd.concat(res, ignore_index=True)
    print(summarize(allr).to_string(index=False))
    if exit_s:
        ex = summarize_exit(allr, exit_s)
        print("\n=== досрочный выход (продажа по bid с комиссией), топ-30 по нижней границе ИИ ===")
        print(ex.sort_values("ИИ_низ", ascending=False).head(30).to_string(index=False))
        print(f"\nстрок с ИИ_низ > 0: {int((ex.ИИ_низ > 0).sum())} из {len(ex)}  (при {len(ex)} сравнениях часть таких строк случайна)")
        # проверка на отложенной выборке: варианты выбираем по первой половине окон, оцениваем на второй
        cut = sorted(allr.w.unique())[len(allr.w.unique()) // 2]
        tr = summarize_exit(allr[allr.w < cut], exit_s, n_boot=500).set_index(["вариант", "L", "выход_с"])
        te = summarize_exit(allr[allr.w >= cut], exit_s, n_boot=500).set_index(["вариант", "L", "выход_с"])
        j = tr[["окон", "исполн", "цсигнал", "ИИ_низ"]].join(te[["окон", "исполн", "цсигнал", "ИИ_низ", "ИИ_верх"]],
                                                             lsuffix="_обуч", rsuffix="_тест")
        top = j.sort_values("цсигнал_обуч", ascending=False).head(15)
        print("\n=== отложенная выборка: топ-15 по первой половине окон, результат на второй ===")
        print(top.round(2).to_string())
        print(f"\nвсе {len(j)} вариантов: средний цсигнал обуч {j.цсигнал_обуч.mean():.2f}, тест {j.цсигнал_тест.mean():.2f}; "
              f"у топ-15 по обуч.: тест {top.цсигнал_тест.mean():.2f}")
        print("\n=== средний цсигнал по выходу и задержке (все варианты) ===")
        print(ex.pivot_table(index="выход_с", columns="L", values="цсигнал", aggfunc="mean").round(2).to_string())


if __name__ == "__main__":
    main()
