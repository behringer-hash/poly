"""Сводка бота стратегии 3 по папке данных (без pandas).

    python3 report_jump.py data_sign            # или data_dry / data_live

Показывает: сигналы по ступеням и источникам, задержку Binance, заявки и время ответа сервера, долю исполнения и
результат по ступеням (по ask - слабые сигналы 3-6 ц, по ask + 1 ц - сильные от 6 ц) и сравнение с симуляцией.
В live цена исполнения в учёте по заявке - цена заявки (верхняя граница: тейкер мог купить дешевле); точный итог -
сверка окон с Polymarket (live_windows, pnl_api).
"""
from __future__ import annotations

import csv
import glob
import io
import lzma
import os
import sys

SIM = {"ask1": "сильные (от 6 ц), ask + 1 ц: симуляция - исполняется ~21-24% сигналов, +3,9...+4,8 ц на шейр, 12-21.10; "
               "на отложенных 26-27.10 +5,3 ц",
       "ask": "слабые (3-6 ц), по ask: симуляция - исполняется ~22% сигналов, около нуля (-0,3 ц на шейр) на 12-21.10, "
              "в плюсе на 26-27.10"}
NAME = {"ask1": "ask + 1 ц (сильные)", "ask": "по ask (слабые)"}


def rows(root: str, stream: str) -> list[dict]:
    out = []
    for f in sorted(glob.glob(os.path.join(root, "**", f"{stream}_*.csv*"), recursive=True)):
        try:
            data = lzma.open(f, "rt", encoding="utf-8").read() if f.endswith(".xz") else open(f, encoding="utf-8").read()
        except Exception as ex:
            print(f"не прочитан {f}: {ex}")
            continue
        for r in csv.DictReader(io.StringIO(data)):
            if r and r.get(next(iter(r))) != next(iter(r)):      # повторный заголовок после перезапуска
                out.append(r)
    return out


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def q(xs, p):
    xs = sorted(x for x in xs if x is not None)
    return xs[min(len(xs) - 1, int(p * len(xs)))] if xs else None


def fmt(x, f=".0f"):
    return "n/a" if x is None else format(x, f)


def fee(p):
    return 0.07 * p * (1 - p)


def main(root):
    sigs, orders, final = rows(root, "jump_signals"), rows(root, "maker_orders"), rows(root, "maker_final")
    wins, wstream = rows(root, "live_windows"), rows(root, "windows")
    if not sigs:
        print("сигналов нет")
        return
    t0, t1 = min(num(s["t"]) for s in sigs), max(num(s["t"]) for s in sigs)
    hours = max((t1 - t0) / 3600, 1e-9)
    by_tier = {}
    for s in sigs:
        by_tier[s["tier"]] = by_tier.get(s["tier"], 0) + 1
    by_src = {}
    for s in sigs:
        by_src[s["src"]] = by_src.get(s["src"], 0) + 1
    print(f"сигналов {len(sigs)} за {hours:.1f} ч ({len(sigs) / hours:.0f} в час, {24 * len(sigs) / hours:.0f} в сутки): "
          f"по ступеням {by_tier}, первым сообщил {by_src}")
    for src in sorted(by_src):
        lat = [num(s["lat_ms"]) for s in sigs if s["src"] == src]
        print(f"  {src}: задержка сделки Binance до бота p50/p90 {fmt(q(lat, .5))}/{fmt(q(lat, .9))} мс")
    lag = [num(s["book_lag_ms"]) for s in sigs if s.get("book_lag_ms")]
    if lag:
        print(f"  отставание книги Polymarket при сигнале p50/p90 {fmt(q(lag, .5))}/{fmt(q(lag, .9))} мс")

    print(f"\nзаявок {len(orders)}; статусы постановки: " + str({k: sum(o["status"] == k for o in orders)
                                                                   for k in sorted({o["status"] for o in orders})}))
    errs = [o for o in orders if o.get("error")]
    if errs:
        print(f"с ошибкой {len(errs)}, первые: " + " | ".join(e["error"][:100] for e in errs[:3]))
    http = [num(o["http_ms"]) for o in orders if o.get("http_ms")]
    if http:
        print(f"ответ сервера на заявку (live) p10/p50/p75/p90: {fmt(q(http, .1))}/{fmt(q(http, .5))}/{fmt(q(http, .75))}/"
              f"{fmt(q(http, .9))} мс (по живым ордерам C1 из Стокгольма: 271/392/725/1403)")
    sign = [num(o.get("sign_ms")) for o in orders if o.get("sign_ms")]
    if sign:
        pre = sum(o.get("presigned") == "1" for o in orders)
        print(f"подпись: готовых {pre} из {len(orders)}; время p50/p90 {fmt(q(sign, .5), '.1f')}/{fmt(q(sign, .9), '.1f')} мс")

    winner = {}
    for w in wstream:
        x = w.get("official_winner") if w.get("official_winner") in ("Up", "Down") else w.get("provisional_winner")
        if x in ("Up", "Down"):
            winner[w["slug"]] = x
    for w in wins:
        if w.get("winner") in ("Up", "Down"):
            winner.setdefault(w["slug"], w["winner"])
    live = any(f.get("size_matched") not in ("", None) for f in final)
    key = "size_matched" if live else "shadow_qty"
    print(f"\nисполнение: {'фактическое (по бирже)' if live else 'теневое (по книге через shadow_match_sec и сделкам рынка)'}")
    for mode in ("ask1", "ask"):
        sel = [f for f in final if f.get("price_mode") == mode]
        if not sel:
            continue
        fills = [(f, min(num(f[key]) or 0.0, num(f["size"]))) for f in sel if (num(f[key]) or 0) > 0]
        res = shares = 0.0
        known = taker = 0
        for f, x in fills:
            w = winner.get(f["slug"])
            if w is None:
                continue
            known += 1
            tk = f.get("shadow_taker") == "1" and not live
            px = num(f.get("shadow_px")) if tk else num(f["price"])
            taker += tk
            fe = fee(px) * x if (tk or live) else 0.0       # live: считаем тейкером (верхняя оценка комиссии)
            res += ((1.0 if f["outcome"] == w else 0.0) - px) * x - fe
            shares += x
        print(f"=== {NAME[mode]}: заявок {len(sel)}, исполнено {len(fills)} ({len(fills) / max(len(sel), 1):.1%}), "
              f"шейров {sum(x for _, x in fills):.0f}" + ("" if live else f", из них сразу тейкером {taker}"))
        if known:
            print(f"    с известным исходом {known}: {res:+.2f}$, {100 * res / max(shares, 1e-9):+.2f} ц на шейр"
                  + (" (цена = цена заявки, комиссия тейкера - верхняя оценка)" if live else ""))
        print(f"    ориентир: {SIM[mode]}")
    if wins:
        api = [num(w.get("pnl_api")) for w in wins if w.get("pnl_api") not in ("", None)]
        est = sum(num(w.get("pnl_est")) or 0.0 for w in wins)
        print(f"\nокон с заявками {len(wins)}; оценка бота {est:+.2f}$" +
              (f"; сверка с Polymarket по {len(api)} окнам: {sum(api):+.2f}$" if api else ""))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data_sign")
