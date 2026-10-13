#!/usr/bin/env bash
# timeout_min: 20
# Хвост задержек до CLOB Polymarket с этого сервера: GET /time по одному живому HTTPS-соединению раз в секунду, 10 минут,
# и для сравнения - новое соединение на каждый запрос раз в 5 с. Если у GET хвост >400 мс мал, а у живых ордеров он ~21%,
# значит задержки добавляет биржа при обработке ордера, а не сеть и не наш процесс.
set -u
"$PYTHON" - <<'PY' > "$OUT_DIR/clob_rtt_tail.txt" 2>&1
import http.client, ssl, time, statistics as st
H = "clob.polymarket.com"
ctx = ssl.create_default_context()

def pct(a, p):
    a = sorted(a); return a[min(int(len(a) * p), len(a) - 1)]

def report(name, a, fails):
    print(f"{name}: n={len(a)} ошибок={fails} медиана={st.median(a):.0f} p80={pct(a,.8):.0f} p90={pct(a,.9):.0f} "
          f"p99={pct(a,.99):.0f} макс={max(a):.0f} мс; доля >200 мс={sum(x>200 for x in a)/len(a):.1%}, >400 мс={sum(x>400 for x in a)/len(a):.1%}")

# 1) одно соединение, раз в секунду
a, fails, c = [], 0, http.client.HTTPSConnection(H, timeout=5, context=ctx)
for i in range(600):
    t0 = time.perf_counter()
    try:
        c.request("GET", "/time"); c.getresponse().read()
        a.append((time.perf_counter() - t0) * 1000)
    except Exception:
        fails += 1
        c = http.client.HTTPSConnection(H, timeout=5, context=ctx)
    time.sleep(max(0, 1 - (time.perf_counter() - t0)))
report("живое соединение, 1 Гц", a, fails)
# 2) новое соединение на запрос (включая TLS), раз в 5 с, 60 штук
b, fails = [], 0
for i in range(60):
    t0 = time.perf_counter()
    try:
        cc = http.client.HTTPSConnection(H, timeout=5, context=ctx)
        cc.request("GET", "/time"); cc.getresponse().read(); cc.close()
        b.append((time.perf_counter() - t0) * 1000)
    except Exception:
        fails += 1
    time.sleep(max(0, 5 - (time.perf_counter() - t0)))
if b:
    report("новое соединение, раз в 5 с", b, fails)
PY
cat "$OUT_DIR/clob_rtt_tail.txt"
