"""Ход BTC на Binance -> лимитная заявка на покупку растущего токена: сравнение цен заявки. Только выгрузка по записи.

    python mm_trig2.py data/2026-10-14 ... --out OUT

Триггер, профили задержек и очередь - как в mm_trig.py (окно 100 мс, источник «кто первый», пауза 1 с на направление в
окне). Способы цены заявки (5 шейров, живёт 0,5 с от прихода на сервер, позиция до исхода):
  * bid    - лучший bid видимой книги;
  * ask1   - ask видимой книги минус 1 ц (при спреде 1 ц = bid; при спреде от 2 ц - внутри спреда);
  * ask    - обычный лимит по ask видимой книги: если на сервере в момент прихода ask не выше нашей цены, заявка
             исполнится тейкером через паузу 150 мс по лучшему ask (не больше объёма на нём), с комиссией 0,07*p*(1-p);
             остаток (или вся заявка, если ask ушёл) стоит в книге по своей цене как bid. Оптимистичная граница:
             тейкерская часть по книге сервера;
  * ask_po - то же, но post-only: если ask на месте - заявку отклоняют, иначе стоит bid'ом по старому ask
             (пессимистичная граница для ask: живые ордера C1 почти не получали цену сигнала).
Пассивная часть: впереди объём на нашей цене на сервере в момент, когда заявка встала (если цена выше лучшего bid -
впереди никого), продвигается сделками рынка; сделка по худшей для продавца цене исполняет нас полностью.
Выход: t2_<день>.csv.gz (по конфигурации, времени окна, цене, спреду) и t2h_<день>.csv.gz (по конфигурации и часу).
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
PX_LO, PX_HI = 0.05, 0.95
T_MIN, T_MAX = 12.0, 295.0
FEE, REBATE = 0.07, 0.2 * 0.07
W = 100
RULES = [("fair", 0.02), ("fair", 0.05), ("usd", 5.0)]
MODES = ["bid", "ask1", "ask", "ask_po"]
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
            continue
        cands = {name: candidates(T, rcv, px, W, name) for name, (T, rcv, px, _, _) in src.items()}
        agg, aggh = {}, {}
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
                sel = (np.abs(cc.dF) >= thr) if rule == "fair" else (np.abs(cc.dS) >= thr)
                ev = cc[sel & np.isfinite(cc.bid) & np.isfinite(cc.ask) & cc.bid.between(PX_LO, PX_HI)]
                last = {}
                for r in ev.itertuples():
                    key = (r.w, r.side)
                    if r.t_dec - last.get(key, -1e18) < REFR_MS:
                        continue
                    last[key] = r.t_dec
                    w, X = int(r.w), r.side
                    t_arr = r.t_dec + P["order"]
                    t_end = t_arr + LIFE_MS
                    won = 1.0 if (winners[w] == "Up") == (X == "U") else 0.0
                    spr = round(r.ask - r.bid, 2)
                    sp = 0 if spr <= 0.01 + 1e-9 else 1
                    Tb, pb = bucket(r.Tl, T_ED), bucket(r.bid, P_ED)
                    hr = int((r.t_dec // 3600000) % 24)
                    v_arr = bk.view(w, t_arr, "srv")
                    trw = tr.by.get(w)
                    for mode in MODES:
                        q = {"bid": r.bid, "ask1": max(round(r.ask - 0.01, 2), r.bid), "ask": r.ask, "ask_po": r.ask}[mode]
                        A = agg.setdefault((rule, thr, prof, mode, Tb, pb, sp), [0, 0, 0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0])
                        H = aggh.setdefault((rule, thr, prof, mode, hr), [0.0, 0.0])
                        A[0] += 1
                        if v_arr is None:
                            continue
                        sa_arr = v_arr[X][1]
                        tk_q, tk_px, t_rest = 0.0, 0.0, t_arr
                        if np.isfinite(sa_arr) and sa_arr <= q + 1e-9:
                            if mode != "ask":              # bid, ask1, ask_po - post-only: пересекающую заявку отклоняют
                                A[1] += 1
                                continue
                            t_m = t_arr + TAKER_DELAY
                            vm = bk.view(w, t_m, "srv")
                            if vm is not None:
                                sa_m = vm[X][1]
                                asz_m = (vm["U"][2] if X == "D" else vm["D"][2])   # объём на ask стороны = объём bid другой
                                if np.isfinite(sa_m) and sa_m <= q + 1e-9 and np.isfinite(asz_m) and asz_m > 0:
                                    tk_q, tk_px = min(SIZE, float(asz_m)), float(sa_m)
                            t_rest = t_m
                        rem = SIZE - tk_q
                        mk = []
                        if rem > 1e-9 and t_rest < t_end:
                            mk = rest_fills(trw, dep, bk, w, X, q, t_rest, t_end)
                            got, mk2 = 0.0, []
                            for tf, f in mk:
                                f = min(f, rem - got)
                                if f <= 1e-9:
                                    break
                                mk2.append((tf, f))
                                got += f
                            mk = mk2
                        if tk_q > 0:
                            fee = FEE * tk_px * (1 - tk_px)
                            A[2] += 1
                            A[3] += tk_q
                            A[4] += (won - tk_px) * tk_q
                            A[5] += fee * tk_q
                            H[0] += (won - tk_px - fee) * tk_q
                        if mk:
                            qm = sum(f for _, f in mk)
                            A[6] += 1
                            A[7] += qm
                            A[8] += (won - q) * qm
                            A[9] += REBATE * q * (1 - q) * qm
                            H[0] += (won - q + REBATE * q * (1 - q)) * qm
                        H[1] += tk_q + (sum(f for _, f in mk) if mk else 0.0)
        cols = ["rule", "thr", "prof", "mode"]
        Ad = pd.DataFrame([dict(zip(cols + ["Tb", "pb", "sp"], k), n_ev=v[0], n_rej=v[1], n_tk=v[2], q_tk=v[3], out_tk=v[4], fee_tk=v[5],
                                n_mk=v[6], q_mk=v[7], out_mk=v[8], reb=v[9]) for k, v in agg.items()])
        Hd = pd.DataFrame([dict(zip(cols + ["hr"], k), pnl=v[0], qty=v[1]) for k, v in aggh.items()])
        Ad.insert(0, "day", day)
        Hd.insert(0, "day", day)
        Ad.to_csv(os.path.join(a.out, f"t2_{day}.csv.gz"), index=False)
        Hd.to_csv(os.path.join(a.out, f"t2h_{day}.csv.gz"), index=False)
        s = Ad.groupby(["prof", "rule", "thr", "mode"]).agg(ev=("n_ev", "sum"), tk=("n_tk", "sum"), mk=("n_mk", "sum"),
                                                          pnl=("out_tk", "sum"), fee=("fee_tk", "sum"), pmk=("out_mk", "sum"), reb=("reb", "sum"))
        s["итог"] = s.pnl - s.fee + s.pmk + s.reb
        print(f"{day}:\n{s[['ev', 'tk', 'mk', 'итог']].round(1).to_string()}", flush=True)


if __name__ == "__main__":
    main()
