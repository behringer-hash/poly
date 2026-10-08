"""Проверка сетевого пути: прокси, DNS, время TCP- и TLS-соединения и КТО выдал сертификат.

    python net_check.py

Если сертификат Binance выдан не публичным центром сертификации, а, например,
антивирусом ("Kaspersky ... Root", "ESET SSL Filter", "Avast Web/Mail Shield",
"Bitdefender Personal CA"), значит, трафик расшифровывается и проверяется на
вашем компьютере - это частая причина задержек WebSocket.
"""
from __future__ import annotations

import os
import socket
import ssl
import time
import urllib.request

HOSTS = [
    ("stream.binance.com", 443),
    ("stream.binance.com", 9443),
    ("data-stream.binance.vision", 443),
    ("api.binance.com", 443),
    ("fstream.binance.com", 443),
    ("stream.bybit.com", 443),
    ("ws.okx.com", 8443),
    ("ws-feed.exchange.coinbase.com", 443),
    ("ws-subscriptions-clob.polymarket.com", 443),
]


def name_of(x509_name):
    d = {}
    for rdn in x509_name or ():
        for k, v in rdn:
            d[k] = v
    return d.get("organizationName") or d.get("commonName") or str(d)


def main():
    print("Прокси, которые видит Python (их же использует websockets):")
    px = urllib.request.getproxies()
    print("   ", px if px else "нет")
    for k in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "NO_PROXY"):
        v = os.environ.get(k) or os.environ.get(k.lower())
        if v:
            print(f"    переменная {k}={v}")
    try:
        import websockets
        print(f"    версия websockets: {websockets.__version__}")
    except Exception:
        pass

    ctx = ssl.create_default_context()
    print(f"\n{'хост':40s} {'IP':16s} {'TCP мс':>7s} {'TLS мс':>7s}  сертификат выдал")
    for host, port in HOSTS:
        try:
            ip = socket.getaddrinfo(host, port, socket.AF_INET)[0][4][0]
        except Exception as e:
            print(f"{host + ':' + str(port):40s} DNS ошибка: {e}")
            continue
        tcp, tls, issuer = [], [], ""
        for _ in range(4):
            try:
                t0 = time.perf_counter()
                s = socket.create_connection((ip, port), timeout=10)
                t1 = time.perf_counter()
                ss = ctx.wrap_socket(s, server_hostname=host)
                t2 = time.perf_counter()
                issuer = name_of(ss.getpeercert().get("issuer"))
                ss.close()
                tcp.append((t1 - t0) * 1000)
                tls.append((t2 - t1) * 1000)
            except Exception as e:
                issuer = f"ошибка: {e!r}"[:70]
            time.sleep(0.2)
        f = lambda xs: f"{min(xs):7.0f}" if xs else "    n/a"
        print(f"{host + ':' + str(port):40s} {ip:16s} {f(tcp)} {f(tls)}  {issuer}")
    print("\nTCP мс ~ время пути туда-обратно. Если TCP почти 0 мс - соединение перехватывается локально.")
    print("TLS мс обычно 1-2 таких времени. Сертификат должен выдавать публичный центр (DigiCert, Amazon,")
    print("Let's Encrypt, Google Trust Services, Sectigo и т.п.), а не антивирус или корпоративный прокси.")


if __name__ == "__main__":
    main()
