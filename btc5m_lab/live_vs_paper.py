"""Сверка живых ордеров с бумажной моделью: доля исполнений, отбор сигналов, реализованный результат.

    python live_vs_paper.py bot_data_3c bot_data_3c_v2 [--variant anc_3c_by]

Ключ сопоставления - (sid, slug, outcome): sid сбрасывается при перезапуске бота.
"""
from __future__ import annotations

import argparse

import numpy as np
import pandas as pd

from analyze import FEE_RATE, load


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--variant", default="anc_3c_by")
    a = ap.parse_args()
    pd.set_option("display.width", 200)
    off = load(a.roots, "windows").drop_duplicates("slug", keep="last").set_index("slug").official_winner
    lo, meta = load(a.roots, "live_orders"), load(a.roots, "live_order_meta")
    k = ["sid", "slug", "outcome"]
    d = lo.merge(meta[k + ["ask_signal", "slip_c", "edge_c", "T"]], on=k, how="left")
    d = d[(d["mode"] == "live") & d.slug.map(off).notna()].copy()
    if d.empty:
        print("нет живых ордеров в режиме live")
        return
    d["filled_f"] = d.status == "matched"
    d["win"] = (d.slug.map(off) == d.outcome).astype(float)
    d["ev_sig"] = d.win - d.ask_signal - FEE_RATE * d.ask_signal * (1 - d.ask_signal)
    print(f"ордеров {len(d)}, исполнено {d.filled_f.mean():.1%}, http_ms медиана {d.http_ms.median():.0f}")
    for col, bins in (("slip_c", [-1, 0, 1, 2, 3, 5, 12]), ("edge_c", [0, 3.5, 4.5, 6, 10, 100]),
                      ("T", [0, 60, 120, 200, 300])):
        print(d.groupby(pd.cut(d[col], bins), observed=True).agg(n=("filled_f", "size"),
                                                                 fill=("filled_f", "mean")).round(3).to_string())
    print(f"\nEV на ask сигнала, ц/шейр: исполненные {100 * d[d.filled_f].ev_sig.mean():.2f}, "
          f"неисполненные {100 * d[~d.filled_f].ev_sig.mean():.2f}  (разрыв = отбор: быстрые боты разбирают сильные сигналы)")
    f = d[d.filled_f].copy()
    f["pnl"] = f.filled * (f.win - f.avg_px - FEE_RATE * f.avg_px * (1 - f.avg_px))
    w = f.groupby("slug").agg(p=("pnl", "sum"), q=("filled", "sum"))
    idx = np.random.default_rng(0).integers(0, len(w), (3000, len(w)))
    s = 100 * w.p.values[idx].sum(1) / w.q.values[idx].sum(1)
    print(f"реализовано: {100 * f.pnl.sum() / f.filled.sum():.2f} ц/шейр, 95% ИИ по окнам "
          f"[{np.percentile(s, 2.5):.1f}; {np.percentile(s, 97.5):.1f}], окон {len(w)}, PnL ${f.pnl.sum():.2f}")
    pf = load(a.roots, "paper_fills")
    pf = pf[pf.variant == a.variant].rename(columns={"sig_id": "sid"})
    for L in sorted(pf.latency_ms.unique()):
        p = pf[pf.latency_ms == L][k + ["status"]].rename(columns={"status": "p"})
        m = d.merge(p, on=k)
        print(f"бумага L={int(L)} мс: исполнений {(m.p == 'fill').mean():.1%} (живых {m.filled_f.mean():.1%})")


if __name__ == "__main__":
    main()
