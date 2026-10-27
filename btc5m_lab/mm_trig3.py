"""Ход BTC на Binance -> обычный лимит на покупку растущего токена по ask + k ц (k = 0..3) и post-only по ask, с разной
задержкой сведения на сервере. Только выгрузка по записи.

    python mm_trig3.py data/2026-10-14 ... --out OUT

Триггер, профили задержек, очередь - как в mm_trig2.py (окно 100 мс, «кто первый», пауза 1 с на направление в окне).
Заявка 5 шейров по цене q = ask видимой книги + k ц (askk) или q = ask post-only (ask_po), живёт до t_arr + 500 мс.
Тейкерская часть: если в момент сведения t_m ask сервера не выше q - берём лучший уровень (объём верха книги), затем
следующие уровни не выше q по снимку pm_depth; комиссия 0,07*p*(1-p) на каждый шейр. Остаток стоит bid'ом по q.
Момент сведения (dm):
  * d150 - приход + 150 мс (как в P8);
  * half - приход + 150 + (S - 150) / 2;
  * resp - приход + S;
  S - время обработки ордера сервером, выборка из живых ордеров C1 (http_ms - 44, 20 квантилей; общая для всех цен
  заявки одного события).
Выход: t3_<день>.csv.gz (по конфигурации, времени окна, цене, спреду), t3h_<день>.csv.gz (по конфигурации и часу),
t3o_<день>.csv.gz (по конфигурации и фактической переплате к ask сигнала, отдельно тейкер и мейкер).
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
from mm_sim import _nv
from mm_trig import PROFILES, Books, bucket, candidates, fills_for, load_src

WINDOW = 300
SIZE = 5.0
LIFE_MS = 500.0
TAKER_DELAY = 150.0
REFR_MS = 1000.0
PX_LO, PX_HI = 0.05, 0.95      # bid растущей стороны при сигнале
Q_LO, Q_HI = 0.0, 1.0          # цена заявки (как price_min / price_max бота); по умолчанию без ограничения
T_MIN, T_MAX = 12.0, 295.0
FEE, REBATE = 0.07, 0.2 * 0.07
W = 100
RULES = [("fair", 0.02), ("fair", 0.05), ("usd", 5.0)]
MODES = ["ask0", "ask1p", "ask2p", "ask3p", "ask_po"]
DMS = ["d150", "half", "resp"]
SRV_Q = np.array([195, 219, 235, 249, 261, 273, 286, 300, 317, 337, 365, 401, 454, 523, 620, 757, 950, 1211, 1567, 2392], float)
T_ED, P_ED = [60, 120, 200], [0.2, 0.35, 0.5, 0.65, 0.8]


def rest_fills(tr, dep, bk, w, X, q, t_rest, t_end):
    """Пассивная часть: впереди - объём на нашей цене на сервере в момент t_rest."""
    v = bk.view(w, t_rest, "srv")
    if v is None:
        return []
    sb, _, ssz = v[X]
    if np.isfinite(sb) and abs(sb - q) < 1e-9:
        ahead = ssz if np.isfinite(ssz) else 1e9
    elif not np.isfinite(sb) or sb < q:
        ahead = 0.0
    else:
        ahead = dep.bid_size_at(w, X, t_rest + 43.0, q)
        ahead = ahead if np.isfinite(ahead) else 1e9
    return fills_for(tr, X, q, ahead, t_rest, t_end)


def take(vm, dep, w, X, q, t_m):
    """Тейкерская часть в момент сведения: лучший ask (объём верха книги), затем уровни не выше q по снимку pm_depth."""
    sa = vm[X][1]
    asz = vm["U"][2] if X == "D" else vm["D"][2]          # объём на ask стороны = объём bid другой
    if not (np.isfinite(sa) and sa <= q + 1e-9 and np.isfinite(asz) and asz > 0):
        return []
    f0 = min(SIZE, float(asz))
    out, got = [(float(sa), f0)], f0
    x = dep.by.get((w, "D" if X == "U" else "U"))
    if got < SIZE - 1e-9 and x is not None:
        i = int(np.searchsorted(x[0], t_m + 43.0, side="right") - 1)
        if i >= 0:
            lv = sorted((round(1 - p, 2), s) for p, s in zip(x[1][i], x[2][i]) if np.isfinite(p) and np.isfinite(s))
            for p, s in lv:
                if p > sa + 1e-9 and p <= q + 1e-9 and got < SIZE - 1e-9:
                    f = min(s, SIZE - got)
                    out.append((p, f))
                    got += f
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--fair", nargs="*", type=float, help="пороги fair (ц в долях), вместо RULES")
    ap.add_argument("--modes", nargs="*", help="цены заявки, вместо MODES")
    ap.add_argument("--dms", nargs="*", help="модели момента сведения, вместо DMS")
    ap.add_argument("--tag", default="t3", help="префикс выходных файлов")
    ap.add_argument("--profiles", nargs="*", help="профили задержек (tokyo, stockholm), по умолчанию оба")
    ap.add_argument("--price-range", nargs=2, type=float, metavar=("LO", "HI"),
                    help="как в боте: сигнал - только если bid растущей стороны в [LO, HI], заявка - только если её цена в [LO, HI]")
    ap.add_argument("--tiers", nargs=2, type=float, metavar=("WEAK", "STRONG"),
                    help="рабочее правило бота: сдвиг от WEAK - лимит по ask (слабые), от STRONG - ask + 1 ц (сильные); "
                         "пауза сильных - между сильными, слабых - после любого сигнала стороны")
    a = ap.parse_args()
    global RULES, MODES, DMS, PROFILES, PX_LO, PX_HI, Q_LO, Q_HI
    if a.price_range:
        PX_LO, PX_HI = a.price_range
        Q_LO, Q_HI = a.price_range
    if a.profiles:
        PROFILES = {k: v for k, v in PROFILES.items() if k in a.profiles}
    strong = None
    if a.tiers:
        RULES, strong = [("tiers", a.tiers[0])], a.tiers[1]
    if a.fair:
        RULES = [("fair", x) for x in a.fair]
    if a.modes:
        MODES = a.modes
    if a.dms:
        DMS = a.dms
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
            continue
        cands = {name: candidates(T, rcv, px, W, name) for name, (T, rcv, px, _, _) in src.items()}
        agg, aggh, aggo = {}, {}, {}
        rng = np.random.default_rng(int(day.replace('-', '')))
        for prof, P in PROFILES.items():
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
            kind = "rcv" if P["book_lag"] is None else "srv"
            lag = 0.0 if P["book_lag"] is None else P["book_lag"]
            n = len(cc)
            mids = np.full(n, np.nan)
            vb = {X: np.full(n, np.nan) for X in "UD"}
            va = {X: np.full(n, np.nan) for X in "UD"}
            for w, g in cc.groupby("w"):
                b = bk.by.get(int(w))
                if b is None:
                    continue
                tt, arr = (b["st"], b["s"]) if kind == "srv" else (b["rt"], b["r"])
                i = np.searchsorted(tt, g.t_dec.values - lag, side="right") - 1
                ok = i >= 0
                ii = np.where(ok, i, 0)
                mids[g.index] = np.where(ok, (arr["U"][0][ii] + arr["U"][1][ii]) / 2, np.nan)
                for X in "UD":
                    vb[X][g.index] = np.where(ok, arr[X][0][ii], np.nan)
                    va[X][g.index] = np.where(ok, arr[X][1][ii], np.nan)
            Tl = cc.Tl.values
            sd = np.where(Tl >= 60, cc.sigma.values * np.sqrt(np.maximum(Tl - 40.0, 1e-9)), cc.sigma.values * np.sqrt(Tl ** 3 / 10800.0))
            wg = np.where(Tl >= 60, 1.0, Tl / 60.0)
            good = np.isfinite(mids) & (mids > 0.01) & (mids < 0.99)
            dF = np.full(n, np.nan)
            if good.any():
                z = _nv(mids[good])
                dF[good] = np.exp(-z * z / 2) / math.sqrt(2 * math.pi) * wg[good] * cc.dS.values[good] / sd[good]
            cc["dF"] = dF
            cc["side"] = np.where(cc.dS > 0, "U", "D")
            cc["bid"] = np.where(cc.side == "U", vb["U"], vb["D"])
            cc["ask"] = np.where(cc.side == "U", va["U"], va["D"])
            for rule, thr in RULES:
                sel = (np.abs(cc.dF) >= thr) if rule in ("fair", "tiers") else (np.abs(cc.dS) >= thr)
                ev = cc[sel & np.isfinite(cc.bid) & np.isfinite(cc.ask) & cc.bid.between(PX_LO, PX_HI)]
                last = {}
                for r in ev.itertuples():
                    if rule == "tiers":
                        ks, kw = (r.w, r.side, "s"), (r.w, r.side, "w")
                        if abs(r.dF) >= strong:
                            if r.t_dec - last.get(ks, -1e18) < REFR_MS:
                                continue
                            last[ks] = r.t_dec
                            modes = [("strong", "ask1p")]
                        else:
                            if r.t_dec - max(last.get(kw, -1e18), last.get(ks, -1e18)) < REFR_MS:
                                continue
                            last[kw] = r.t_dec
                            modes = [("weak", "ask0")]
                    else:
                        key = (r.w, r.side)
                        if r.t_dec - last.get(key, -1e18) < REFR_MS:
                            continue
                        last[key] = r.t_dec
                        modes = [(m, m) for m in MODES]
                    w, X = int(r.w), r.side
                    t_arr = r.t_dec + P["order"]
                    t_end = t_arr + LIFE_MS
                    won = 1.0 if (winners[w] == "Up") == (X == "U") else 0.0
                    spr = round(r.ask - r.bid, 2)
                    sp = 0 if spr <= 0.01 + 1e-9 else 1
                    Tb, pb = bucket(r.Tl, T_ED), bucket(r.bid, P_ED)
                    hr = int((r.t_dec // 3600000) % 24)
                    trw = tr.by.get(w)
                    S = SRV_Q[rng.integers(len(SRV_Q))]
                    for dm in DMS:
                        if dm.startswith("f"):         # f<D>: сведение ровно через D мс после решения (живой запуск: 0,5-1,5 с)
                            t_live = r.t_dec + float(dm[1:]) - TAKER_DELAY
                        else:
                            t_live = t_arr + {"d150": 0.0, "half": (S - TAKER_DELAY) / 2, "resp": S - TAKER_DELAY}[dm]
                        v_live = bk.view(w, t_live, "srv")
                        t_m = t_live + TAKER_DELAY
                        vm = bk.view(w, t_m, "srv")
                        for lab, mode in modes:
                            q = round(r.ask + (0.0 if mode == "ask_po" else 0.01 * int(mode[3])), 2)
                            if not (Q_LO - 1e-9 <= q <= Q_HI + 1e-9):
                                continue                   # бот не ставит заявку вне диапазона цен
                            A = agg.setdefault((rule, thr, prof, dm, lab, Tb, pb, sp), [0, 0, 0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0])
                            H = aggh.setdefault((rule, thr, prof, dm, lab, hr), [0.0, 0.0])
                            A[0] += 1
                            if v_live is None:
                                continue
                            sa_live = v_live[X][1]
                            fills, t_rest = [], t_live
                            if np.isfinite(sa_live) and sa_live <= q + 1e-9:
                                if mode == "ask_po":
                                    A[1] += 1
                                    continue
                                if vm is not None:
                                    fills = take(vm, dep, w, X, q, t_m)
                                t_rest = t_m
                            tk_q = sum(f for _, f in fills)
                            rem = SIZE - tk_q
                            mk = []
                            if rem > 1e-9 and t_rest < t_end:
                                got = 0.0
                                for tf, f in rest_fills(trw, dep, bk, w, X, q, t_rest, t_end):
                                    f = min(f, rem - got)
                                    if f <= 1e-9:
                                        break
                                    mk.append((tf, f))
                                    got += f
                            if tk_q > 0:
                                A[2] += 1
                                A[3] += tk_q
                                for p, f in fills:
                                    fee = FEE * p * (1 - p)
                                    A[4] += (won - p) * f
                                    A[5] += fee * f
                                    H[0] += (won - p - fee) * f
                                    O = aggo.setdefault((rule, thr, prof, dm, lab, "tk", int(round(100 * (p - r.ask)))), [0.0, 0.0, 0.0])
                                    O[0] += f
                                    O[1] += won * f
                                    O[2] += (won - p - fee) * f
                            if mk:
                                qm = sum(f for _, f in mk)
                                A[6] += 1
                                A[7] += qm
                                A[8] += (won - q) * qm
                                A[9] += REBATE * q * (1 - q) * qm
                                H[0] += (won - q + REBATE * q * (1 - q)) * qm
                                O = aggo.setdefault((rule, thr, prof, dm, lab, "mk", int(round(100 * (q - r.ask)))), [0.0, 0.0, 0.0])
                                O[0] += qm
                                O[1] += won * qm
                                O[2] += (won - q + REBATE * q * (1 - q)) * qm
                            H[1] += tk_q + sum(f for _, f in mk)
        cols = ["rule", "thr", "prof", "dm", "mode"]
        Ad = pd.DataFrame([dict(zip(cols + ["Tb", "pb", "sp"], k), n_ev=v[0], n_rej=v[1], n_tk=v[2], q_tk=v[3], out_tk=v[4], fee_tk=v[5],
                                n_mk=v[6], q_mk=v[7], out_mk=v[8], reb=v[9]) for k, v in agg.items()])
        Hd = pd.DataFrame([dict(zip(cols + ["hr"], k), pnl=v[0], qty=v[1]) for k, v in aggh.items()])
        Od = pd.DataFrame([dict(zip(cols + ["kind", "ov"], k), qty=v[0], won_q=v[1], pnl=v[2]) for k, v in aggo.items()])
        for x, nm in ((Ad, a.tag), (Hd, a.tag + "h"), (Od, a.tag + "o")):
            x.insert(0, "day", day)
            x.to_csv(os.path.join(a.out, f"{nm}_{day}.csv.gz"), index=False)
        s = Ad.groupby(["prof", "thr", "dm", "mode"]).agg(
            ev=("n_ev", "sum"), tk=("n_tk", "sum"), mk=("n_mk", "sum"), pnl=("out_tk", "sum"), fee=("fee_tk", "sum"),
            pmk=("out_mk", "sum"), reb=("reb", "sum"))
        s["итог"] = s.pnl - s.fee + s.pmk + s.reb
        print(f"{day}:\n{s[['ev', 'tk', 'mk', 'итог']].round(1).to_string()}", flush=True)


if __name__ == "__main__":
    main()
