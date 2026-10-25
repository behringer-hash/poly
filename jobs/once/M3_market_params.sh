#!/usr/bin/env bash
# timeout_min: 5
# Параметры текущих 5-минутных рынков BTC в CLOB: задержка тейкера (itode), минимальный возраст заявки (oas), комиссии (fd, tbf, mbf).
set -u
"$PYTHON" - <<'PY'
import json, time, requests
H = {"User-Agent": "Mozilla/5.0"}
now = int(time.time()) // 300 * 300
for st in (now - 300, now, now + 300):
    slug = f"btc-updown-5m-{st}"
    try:
        ev = requests.get("https://gamma-api.polymarket.com/events", params={"slug": slug}, headers=H, timeout=10).json()
        m = ev[0]["markets"][0]
        cid = m["conditionId"]
        r = requests.get(f"https://clob.polymarket.com/clob-markets/{cid}", headers=H, timeout=10)
        print(f"== {slug} ({r.status_code})")
        print(json.dumps(r.json(), ensure_ascii=False)[:1500])
        print("gamma feeSchedule/fees:", json.dumps({k: m.get(k) for k in m if "fee" in k.lower() or "delay" in k.lower() or "rebate" in k.lower()}, ensure_ascii=False)[:800])
    except Exception as ex:
        print(slug, "ошибка", repr(ex)[:300])
PY
