"""Ход BTC на Binance за W мс -> пассивная заявка на покупку растущего токена по лучшему bid. Только выгрузка по записи.

    python mm_trig.py data/2026-10-12 ... --out OUT

Событие - сделка Binance (фьючерс bnf_agg / спот bn_agg, время биржи T), цена которой отличается от цены W мс назад на dS.
Правило срабатывания (с паузой 1 с на направление в окне, по моменту, когда событие дошло до нас):
  * «fair X»: сдвиг справедливой цены Up |phi(z)*w*dS/sd| >= X (z из mid книги Up, которую мы видим в момент решения;
    sd = sigma*sqrt(T-40) или sigma*sqrt(T^3/10800), w = 1 или T/60; sigma - секундная волатильность источника за 15 мин);
  * «usd X»: |dS| >= X долларов.
Заявка: покупка растущего токена (вверх - Up, вниз - Down) по лучшему bid этой стороны в видимой нам книге, SIZE шейров,
post-only (если на сервере в момент прихода ask не выше нашей цены - отклонена), живёт LIFE_MS на сервере, держим до исхода.
Профили задержек:
  * tokyo: решение = T + 19 мс (спот) / 27 мс (фьючерс); книгу видим такой, какой она была на сервере 130 мс назад;
    заявка доходит до сервера Polymarket за 120 мс;
  * stockholm: решение = фактический момент получения сделки в записи (recv_ms); книга - как она до нас доходила (recv);
    заявка доходит за 22 мс.
Очередь: back - впереди объём на нашей цене на сервере в момент прихода (верх книги; глубже - снимок pm_depth);
front - мы первые (верхняя граница). Исполнение только сделками рынка (как в mm_sim).
Выход: trg_<день>.csv.gz (по конфигурации, времени окна и цене) и trgh_<день>.csv.gz (по конфигурации и часу).
"""
from __future__ import annotations

import argparse
import math
import os

import numpy as np
import pandas as pd

from edge_maker import Depth, Trades
from edge_source import per_sec_sigma, winners_ptb
from lead_lag import PM, read
from mm_sim import _nv, side_arrays

WINDOW = 300
SIZE = 5.0
LIFE_MS = 500.0
REFR_MS = 1000.0
PX_LO, PX_HI = 0.05, 0.95
T_MIN, T_MAX = 12.0, 295.0
REBATE = 0.2 * 0.07
PROFILES = {"tokyo": dict(feed={"fut": 27.0, "spot": 19.0}, order=120.0, book_lag=130.0),
            "stockholm": dict(feed=None, order=22.0, book_lag=None)}
RULES = [("fair", 0.01), ("fair", 0.02), ("fair", 0.03), ("fair", 0.05), ("usd", 5.0), ("usd", 10.0), ("usd", 20.0)]
WS = [50, 100, 200]
T_ED, P_ED = [60, 120, 200], [0.2, 0.35, 0.5, 0.65, 0.8]


def load_src(root, stream):
    d = read(root, stream, ["recv_ms", "T", "price"]).dropna()
    d = d.sort_values("T", kind="stable")
    return d["T"].values.astype(float), d.recv_ms.values.astype(float), d.price.values.astype(float)


def candidates(T, rcv, px, W, name):
    """Сделки, где цена отличается от цены W мс назад хотя бы на $0,5: время биржи, приход, dS, источник."""
    j = np.searchsorted(T, T - W, side="right") - 1
    ok = j >= 0
    dS = np.where(ok, px - px[np.maximum(j, 0)], 0.0)
    m = np.abs(dS) >= 0.5
    return pd.DataFrame(dict(T=T[m], rcv=rcv[m], dS=dS[m], src=name))


def fills_for(tr, X, q, ahead, ta, te):
    if tr is None or te <= ta:
        return []
    ts, o, side, px, sz = tr
    i0, i1 = np.searchsorted(ts, ta, "left"), np.searchsorted(ts, te, "left")
    mirror = round(1 - q, 2)
    rem, out = SIZE, []
    for i in range(i0, i1):
        if o[i] == X and side[i] == "S":
            at, thr = abs(px[i] - q) < 1e-9, px[i] < q - 1e-9
        elif o[i] != X and side[i] == "B":
            at, thr = abs(px[i] - mirror) < 1e-9, px[i] > mirror + 1e-9
        else:
            continue
        if thr:
            out.append((ts[i], rem))
            return out
        if not at:
            continue
        ahead -= sz[i]
        if ahead < 0:
            f = min(-ahead, rem)
            ahead = 0.0
            rem -= f
            out.append((ts[i], f))
            if rem <= 1e-9:
                return out
    return out


class Books:
    def __init__(self, pm: PM):
        self.by = {}
        for w, x in pm.by_w.items():
            self.by[w] = dict(st=x["srv"]["t"], s=side_arrays(x["srv"]), rt=x["rcv"]["t"], r=side_arrays(x["rcv"]))

    def view(self, w, t, kind):
        b = self.by.get(w)
        if b is None:
            return None
        tt, arr = (b["st"], b["s"]) if kind == "srv" else (b["rt"], b["r"])
        i = int(np.searchsorted(tt, t, side="right") - 1)
        if i < 0:
            return None
        return {X: (arr[X][0][i], arr[X][1][i], arr[X][2][i]) for X in "UD"}


def bucket(x, edges):
    return int(np.searchsorted(edges, x, side="right"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    for root in a.roots:
        day = os.path.basename(os.path.normpath(root))
        top = read(root, "pm_top")
        if top.empty:
            print(f"{day}: нет pm_top", flush=True)
            continue
        winners, _ = winners_ptb(root)
        pm = PM(top)
        del top
        bk = Books(pm)
        dep, tr = Depth(root), Trades(root)
        src = {}
        for name, stream in (("fut", "bnf_agg"), ("spot", "bn_agg")):
            T, rcv, px = load_src(root, stream)
            if len(T) > 1000:
                st, sv = per_sec_sigma(T, px)
                src[name] = (T, rcv, px, st, sv)
        if not src:
            print(f"{day}: нет сделок Binance", flush=True)
            continue
        agg, aggh = {}, {}
        n_orders = 0
        for W in WS:
            cands = {name: candidates(T, rcv, px, W, name) for name, (T, rcv, px, _, _) in src.items()}
            for prof, P in PROFILES.items():
                # момент решения и вид книги для каждого кандидата
                frames = []
                for name, c in cands.items():
                    c = c.copy()
                    c["t_dec"] = (c["T"] + P["feed"][name]) if P["feed"] else c["rcv"]
                    st, sv = src[name][3], src[name][4]
                    c["sigma"] = sv[np.clip(np.searchsorted(st, c["T"].values, side="right") - 1, 0, len(sv) - 1)]
                    frames.append(c)
                cc = pd.concat(frames, ignore_index=True)
                cc["w"] = (cc.t_dec // 1000 // WINDOW * WINDOW).astype(np.int64)
                cc = cc[cc.w.isin(list(winners))]
                cc["Tl"] = (cc.w + WINDOW) - cc.t_dec / 1000.0
                cc = cc[(cc.Tl > T_MIN) & (cc.Tl < T_MAX)].sort_values("t_dec", kind="stable").reset_index(drop=True)
                # mid Up в видимой книге
                kind = "rcv" if P["book_lag"] is None else "srv"
                lag = 0.0 if P["book_lag"] is None else P["book_lag"]
                mids, bids = np.full(len(cc), np.nan), {"U": np.full(len(cc), np.nan), "D": np.full(len(cc), np.nan)}
                for w, g in cc.groupby("w"):
                    b = bk.by.get(int(w))
                    if b is None:
                        continue
                    tt, arr = (b["st"], b["s"]) if kind == "srv" else (b["rt"], b["r"])
                    i = np.searchsorted(tt, g.t_dec.values - lag, side="right") - 1
                    ok = i >= 0
                    ii = np.where(ok, i, 0)
                    bu, au = arr["U"][0][ii], arr["U"][1][ii]
                    mids[g.index] = np.where(ok, (bu + au) / 2, np.nan)
                    for X in "UD":
                        bids[X][g.index] = np.where(ok, arr[X][0][ii], np.nan)
                Tl = cc.Tl.values
                sd = np.where(Tl >= 60, cc.sigma.values * np.sqrt(np.maximum(Tl - 40.0, 1e-9)),
                              cc.sigma.values * np.sqrt(Tl ** 3 / 10800.0))
                wg = np.where(Tl >= 60, 1.0, Tl / 60.0)
                good = np.isfinite(mids) & (mids > 0.01) & (mids < 0.99)
                dF = np.full(len(cc), np.nan)
                if good.any():
                    z = _nv(mids[good])
                    dF[good] = np.exp(-z * z / 2) / math.sqrt(2 * math.pi) * wg[good] * cc.dS.values[good] / sd[good]
                cc["dF"] = dF
                cc["side"] = np.where(cc.dS > 0, "U", "D")
                cc["q"] = np.where(cc.side == "U", bids["U"], bids["D"])
                for rule, thr in RULES:
                    sel = (np.abs(cc.dF) >= thr) if rule == "fair" else (np.abs(cc.dS) >= thr)
                    base = cc[sel & np.isfinite(cc.q) & cc.q.between(PX_LO, PX_HI)]
                    for sname in ("fut", "spot", "any"):
                        ev = base if sname == "any" else base[base.src == sname]
                        if ev.empty:
                            continue
                        last = {}
                        for r in ev.itertuples():
                            key = (r.w, r.side)
                            if r.t_dec - last.get(key, -1e18) < REFR_MS:
                                continue
                            last[key] = r.t_dec
                            w, X, q = int(r.w), r.side, float(r.q)
                            t_arr = r.t_dec + P["order"]
                            v = bk.view(w, t_arr, "srv")
                            Tb, pb = bucket(r.Tl, T_ED), bucket(q, P_ED)
                            hr = int((r.t_dec // 3600000) % 24)
                            won = 1.0 if (winners[w] == "Up") == (X == "U") else 0.0
                            for queue in ("back", "front"):
                                kA = (rule, thr, sname, W, prof, queue, Tb, pb)
                                kH = (rule, thr, sname, W, prof, queue, hr)
                                A = agg.setdefault(kA, [0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0])
                                H = aggh.setdefault(kH, [0, 0.0, 0.0, 0.0])
                                A[0] += 1
                                if v is None:
                                    continue
                                sb, sa, ssz = v[X]
                                if np.isfinite(sa) and sa <= q + 1e-9:
                                    A[1] += 1                      # post-only отклонила бы
                                    continue
                                A[2] += 1
                                if queue == "front":
                                    ahead = 0.0
                                elif np.isfinite(sb) and abs(sb - q) < 1e-9:
                                    ahead = ssz if np.isfinite(ssz) else 1e9
                                elif not np.isfinite(sb) or sb < q:
                                    ahead = 0.0
                                else:
                                    ahead = dep.bid_size_at(w, X, t_arr + 43.0, q)
                                    ahead = ahead if np.isfinite(ahead) else 1e9
                                fl = fills_for(tr.by.get(w), X, q, ahead, t_arr, t_arr + LIFE_MS)
                                if not fl:
                                    continue
                                qty = sum(f for _, f in fl)
                                t_f = fl[0][0]
                                v5 = bk.view(w, t_f + 5000, "srv")
                                m5 = (v5[X][0] + v5[X][1]) / 2 if v5 is not None else np.nan
                                A[3] += 1
                                A[4] += qty
                                A[5] += (won - q) * qty
                                A[6] += (m5 - q) * qty if np.isfinite(m5) else 0.0
                                A[7] += REBATE * q * (1 - q) * qty
                                H[0] += 1
                                H[1] += qty
                                H[2] += (won - q) * qty
                                H[3] += REBATE * q * (1 - q) * qty
                                n_orders += 1
        cols = ["rule", "thr", "src", "W", "prof", "queue"]
        Ad = pd.DataFrame([dict(zip(cols + ["Tb", "pb"], k), n_ev=v[0], n_rej=v[1], n_pl=v[2], n_fill=v[3], qty=v[4], out=v[5],
                                mk5=v[6], reb=v[7]) for k, v in agg.items()])
        Hd = pd.DataFrame([dict(zip(cols + ["hr"], k), n_fill=v[0], qty=v[1], out=v[2], reb=v[3]) for k, v in aggh.items()])
        Ad.insert(0, "day", day)
        Hd.insert(0, "day", day)
        Ad.to_csv(os.path.join(a.out, f"trg_{day}.csv.gz"), index=False)
        Hd.to_csv(os.path.join(a.out, f"trgh_{day}.csv.gz"), index=False)
        s = Ad[(Ad.W == 100) & (Ad.queue == "back") & (Ad.src == "any")].groupby(["prof", "rule", "thr"]).agg(
            событий=("n_ev", "sum"), исполнено=("n_fill", "sum"), шейров=("qty", "sum"), исход=("out", "sum"), доля=("reb", "sum"))
        print(f"{day}: окон {len(winners)}, исполнений (все конфигурации) {n_orders}\n{s.round(1).to_string()}", flush=True)


if __name__ == "__main__":
    main()
