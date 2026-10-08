"""Проверка собранных данных перед отправкой на анализ.

    python check_data.py            # папка data
    python check_data.py D:\\lab\\data

Читает и незакрытые (текущие) файлы - обрезанный хвост gzip просто отбрасывается.
"""
from __future__ import annotations

import glob
import io
import os
import sys
import zlib

import pandas as pd


def _decompress_gz(raw: bytes) -> bytes:
    out, pos = [], 0
    while pos < len(raw):  # несколько gzip-блоков подряд
        d = zlib.decompressobj(16 + zlib.MAX_WBITS)
        try:
            out.append(d.decompress(raw[pos:]))
        except zlib.error:
            break
        if not d.eof:
            out.append(d.flush())
            break
        pos = len(raw) - len(d.unused_data)
    return b"".join(out)


def _decompress_xz(raw: bytes) -> bytes:
    import lzma
    out, pos = [], 0
    while pos < len(raw):  # несколько xz-блоков подряд (перезапуски в тот же час)
        d = lzma.LZMADecompressor()
        try:
            out.append(d.decompress(raw[pos:]))
        except lzma.LZMAError:
            break
        if not d.eof:
            break
        pos = len(raw) - len(d.unused_data)
    return b"".join(out)


def read_file(path: str) -> pd.DataFrame:
    raw = open(path, "rb").read()
    if path.endswith(".gz"):
        raw = _decompress_gz(raw)
    elif path.endswith(".xz"):
        raw = _decompress_xz(raw)
    txt = raw.decode("utf-8", errors="ignore")
    txt = txt[: txt.rfind("\n") + 1]  # обрезанный хвост отбрасываем
    if not txt.strip():
        return pd.DataFrame()
    header = txt.split("\n", 1)[0]
    lines = [header] + [ln for ln in txt.split("\n")[1:] if ln and ln != header]  # повторные заголовки
    return pd.read_csv(io.StringIO("\n".join(lines)), low_memory=False, dtype={"tx": str, "tx_hash": str})


read_gz = read_file  # совместимость


def load(root: str, stream: str) -> pd.DataFrame:
    files = []
    for ext in ("csv.gz", "csv.xz", "csv"):
        files += glob.glob(os.path.join(root, "*", f"{stream}_??.{ext}"))
    parts = [read_file(f) for f in sorted(files)]
    parts = [p for p in parts if len(p)]
    return pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()


def q(s, p):
    s = pd.to_numeric(s, errors="coerce").dropna()
    return round(float(s.quantile(p)), 1) if len(s) else None


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "data"
    print(f"Папка: {os.path.abspath(root)}\n")

    streams = ["bn_agg", "bn_book", "cb_ticker", "bnf_agg", "by_trade", "ok_trade", "health_feeds", "clock", "health_cex", "pm_top", "pm_depth", "pm_trades", "rtds",
               "windows", "clock_pm", "health_pm", "pm_rtt", "events", "events_pm", "wallet", "paper_signals",
               "paper_fills", "paper_markouts", "paper_windows"]
    D = {}
    print(f"{'поток':16s} {'строк':>10s}  начало (UTC)          конец (UTC)")
    for s in streams:
        df = load(root, s)
        D[s] = df
        if df.empty:
            print(f"{s:16s} {'-':>10s}")
            continue
        tcol = next((c for c in ("recv_ms", "ts_ms", "recv", "ts", "logged_at", "detected") if c in df.columns), None)
        if tcol:
            t = pd.to_numeric(df[tcol], errors="coerce")
            if tcol.endswith("_ms"):
                t = t / 1000
            a = pd.to_datetime(t.min(), unit="s").strftime("%Y-%m-%d %H:%M:%S")
            b = pd.to_datetime(t.max(), unit="s").strftime("%Y-%m-%d %H:%M:%S")
        else:
            a = b = ""
        print(f"{s:16s} {len(df):>10d}  {a}   {b}")

    print("\n--- Задержки и часы")
    for name, st in (("clock", "cex"), ("clock_pm", "pm")):
        c = D[name]
        if not c.empty:
            print(f"смещение часов ({st}, источник {c.source.iloc[-1]}): медиана {q(c.offset_ms, .5)} мс, "
                  f"мин {q(c.offset_ms, 0)}, макс {q(c.offset_ms, 1)}, RTT медиана {q(c.rtt_ms, .5)} мс")
    h = D["health_cex"]
    if not h.empty:
        print(f"Binance: задержка биржа->вы p50 (медиана по 10с) {q(h.bn_lat_p50, .5)} мс, p90 {q(h.bn_lat_p90, .5)} мс; "
              f"сделок за 10 с медиана {q(h.bn_msgs, .5)}; lag loop p99 макс {q(h.lag_p99, 1)} мс")
    hf = D["health_feeds"]
    if not hf.empty:
        for feed, g in hf.groupby("feed"):
            print(f"{feed}: задержка биржа->вы p50 (медиана по 10с) {q(g.lat_p50, .5)} мс, p90 {q(g.lat_p90, .5)} мс; "
                  f"сделок за 10 с медиана {q(g.msgs, .5)}; интервалов без данных {(g.msgs == 0).mean():.1%}")
    h = D["health_pm"]
    if not h.empty:
        bad = (pd.to_numeric(h.clob_lat_p90, errors="coerce") > 500).mean()
        print(f"Polymarket CLOB: задержка сервер->вы p50 {q(h.clob_lat_p50, .5)} мс, p90 {q(h.clob_lat_p90, .5)} мс; "
              f"доля интервалов с p90>500 мс: {bad:.1%}; сообщений за 10 с медиана {q(h.clob_msgs, .5)}")
        print(f"lag event loop процесса pm: p99 медиана {q(h.lag_p99, .5)} мс, максимум {q(h.lag_max, 1)} мс")

    t = D["pm_top"]
    if not t.empty and "recv_ms" in t.columns:
        t = t.sort_values("recv_ms")
        t["gap"] = t.groupby(["w", "o"]).recv_ms.diff() / 1000
        g = t.groupby("w").gap.max()
        print(f"окон в pm_top: {t.w.nunique()}, окон с паузой в изменениях цены >15 с: {(g > 15).sum()}")
    ev = D["events_pm"]
    if not ev.empty:
        cl = ev[ev.feed.astype(str).str.startswith("clob")]
        print(f"обрывы CLOB: {(cl.event == 'disconnected').sum()}, переключений на резервное соединение: "
              f"{(cl.event == 'promoted').sum()}")
    r = D["pm_rtt"]
    if not r.empty:
        for ep, g in r.groupby("endpoint"):
            print(f"HTTPS {ep:5s}: статус {g.status.value_counts().to_dict()}, время p50 {q(g.rtt_ms, .5)} мс, "
                  f"p90 {q(g.rtt_ms, .9)} мс")
        if ((r.endpoint == "order") & (r.status == 403)).any():
            print("  ВНИМАНИЕ: сервер ордеров Polymarket отвечает 403 - вероятно, торговля из вашего региона закрыта")

    w = D["windows"]
    if not w.empty:
        both = w.dropna(subset=["official_winner", "provisional_winner"])
        agree = (both.official_winner == both.provisional_winner).mean() if len(both) else float("nan")
        print(f"\n--- Окна: {len(w)}, с официальным исходом {w.official_winner.notna().sum()}, "
              f"совпадение предварительного с официальным {agree:.1%}")

    wl = D["wallet"]
    if not wl.empty:
        tr = wl[(wl.seeded == 0) & (wl.type == "TRADE")]
        print(f"\n--- Кошелёк: новых событий {int((wl.seeded == 0).sum())}, из них сделок {len(tr)}; "
              f"типы: {wl[wl.seeded == 0].type.value_counts().to_dict()}")
        pt = D["pm_trades"]
        if len(tr) and not pt.empty:
            if "tx" in pt.columns:  # новый формат: префикс хэша, U/D, B/S
                pt = pt.assign(tx_hash=pt.tx.astype(str), outcome=pt.o.map({"U": "Up", "D": "Down"}),
                               side=pt.side.map({"B": "BUY", "S": "SELL"}))
                tr = tr.assign(tx_hash=tr.tx_hash.str[2:18])
            m = tr.merge(pt[["tx_hash", "server_ts", "outcome", "side"]], on="tx_hash", how="left",
                         suffixes=("", "_pm"))
            matched = m.groupby("tx_hash").server_ts.apply(lambda s: s.notna().any()).mean()
            mm = m.dropna(subset=["server_ts"]).drop_duplicates("tx_hash")
            lag = (pd.to_numeric(mm.ts) - mm.server_ts / 1000)
            taker = ((mm.outcome == mm.outcome_pm) & (mm.side_pm == "BUY")).mean()
            print(f"найдено в pm_trades по tx_hash: {matched:.1%}; время блока - время сервера: медиана "
                  f"{lag.median():.2f} с; доля, где кошелёк - тейкер: {taker:.1%}")

    f, mk, pw = D["paper_fills"], D["paper_markouts"], D["paper_windows"]
    if not f.empty:
        print("\n--- Бумажная торговля")
        g = f.groupby(["variant", "latency_ms"])
        res = pd.DataFrame({
            "сигналов": g.sig_id.nunique(),
            "доля_исполн": g.status.apply(lambda s: (s == "fill").mean()).round(3),
        })
        if not mk.empty:
            res["маркаут5с_ц"] = mk.groupby(["variant", "latency_ms"]).markout_net_c.mean().round(2)
        if not pw.empty:
            res["окон"] = pw.groupby(["variant", "latency_ms"]).slug.nunique()
            res["PnL_$"] = pw.groupby(["variant", "latency_ms"]).pnl.sum().round(2)
        print(res.to_string())
    print("\nГотово. Пришлите папку data целиком (можно заархивировать).")


if __name__ == "__main__":
    main()
