# Состояние сервера записи

Время (UTC): 2026-10-17 23:11:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 15 hours, 47 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         840         933           2         419        1065
Swap:           2047         236        1811
```
- нагрузка CPU (1/5/15 мин): 0.28 / 0.25 / 0.26

## Данные
- файлов: 5642, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 228 | 30 МБ | 2 |
| bn_book | 228 | 3 МБ | 2 |
| bnf_agg | 228 | 45 МБ | 2 |
| bnf_book | 118 | 557 МБ | 393762 |
| bnf_depth5 | 118 | 41 МБ | 393838 |
| bnf_liq | 197 | 132 КБ | 3445 |
| bs_trade | 118 | 1 МБ | 393758 |
| by_book1 | 228 | 95 МБ | 2 |
| by_liq | 202 | 108 КБ | 1747 |
| by_trade | 228 | 29 МБ | 2 |
| bys_book1 | 112 | 39 МБ | 2 |
| bys_trade | 112 | 15 МБ | 2 |
| cb_ticker | 228 | 28 МБ | 2 |
| clock | 228 | 175 КБ | 8 |
| clock_pm | 228 | 175 КБ | 36 |
| events | 217 | 70 КБ | 387 |
| events_pm | 227 | 83 КБ | 1159 |
| health_cex | 228 | 2 МБ | 2 |
| health_feeds | 228 | 8 МБ | 2 |
| health_pm | 228 | 2 МБ | 4 |
| kr_trade | 118 | 3 МБ | 393758 |
| ok_trade | 227 | 39 МБ | 2 |
| pm_depth | 228 | 45 МБ | 2 |
| pm_rtt | 228 | 1 МБ | 2 |
| pm_top | 228 | 92 МБ | 2 |
| pm_trades | 228 | 66 МБ | 2 |
| rtds | 228 | 14 МБ | 2 |
| windows | 228 | 469 КБ | 34 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 40, всего 313
- Polymarket CLOB: TCP 5, TLS 39, всего 82
- Polymarket gamma: TCP 5, TLS 41, всего 56

## Последние строки журнала записи
```
23:10:23 [pm] T-276.7s Up 0.58/0.59 Down 0.41/0.42 ptb=81222.7 | CLOB 4873 сообщ., задержка p50/p90=41.0/43.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792278623280 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.9 мс | lag loop p99/max=1.8/2.0 мс
23:10:24 [cex] Binance 28 сд. задержка p50/p90=158.8/159.8 мс | Coinbase 24 задержка p50=81.1 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/2.2 мс
23:10:24 [cex] binance_futures 20 сд. p50=301.4 мс | bybit 8 сд. p50=124.2 мс | bybit_book 71 сд. p50=122.5 мс | bybit_spot 44 сд. p50=125.9 мс | bybit_spot_book 53 сд. p50=119.4 мс | okx 16 сд. p50=152.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:10:33 [pm] T-266.7s Up 0.64/0.65 Down 0.35/0.36 ptb=81222.7 | CLOB 6546 сообщ., задержка p50/p90=41.6/46.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792278633281 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.9 мс | lag loop p99/max=1.2/1.2 мс
23:10:34 [cex] Binance 38 сд. задержка p50/p90=158.7/159.6 мс | Coinbase 14 задержка p50=74.9 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/2.2 мс
23:10:34 [cex] binance_futures 19 сд. p50=301.3 мс | bybit 5 сд. p50=123.9 мс | bybit_book 67 сд. p50=122.6 мс | bybit_spot 2 сд. p50=124.6 мс | bybit_spot_book 40 сд. p50=119.4 мс | okx 7 сд. p50=152.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:10:43 [pm] T-256.7s Up 0.63/0.64 Down 0.36/0.37 ptb=81222.7 | CLOB 4941 сообщ., задержка p50/p90=41.7/47.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792278643283 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.3/1.4 мс
23:10:44 [cex] Binance 24 сд. задержка p50/p90=158.8/159.3 мс | Coinbase 5 задержка p50=76.3 мс | смещение часов +19.0 мс | lag loop p99/max=2.2/2.2 мс
23:10:44 [cex] binance_futures 14 сд. p50=301.0 мс | bybit 4 сд. p50=124.2 мс | bybit_book 50 сд. p50=122.6 мс | bybit_spot 1 сд. p50=124.0 мс | bybit_spot_book 32 сд. p50=119.4 мс | okx 7 сд. p50=152.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:10:53 [pm] T-246.7s Up 0.64/0.65 Down 0.35/0.36 ptb=81222.7 | CLOB 3379 сообщ., задержка p50/p90=41.2/46.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792278653284 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.1/2.2 мс
23:10:54 [cex] Binance 46 сд. задержка p50/p90=158.6/159.6 мс | Coinbase 24 задержка p50=75.7 мс | смещение часов +19.0 мс | lag loop p99/max=1.9/2.1 мс
23:10:54 [cex] binance_futures 18 сд. p50=301.1 мс | bybit 2 сд. p50=124.4 мс | bybit_book 61 сд. p50=122.5 мс | bybit_spot 31 сд. p50=125.6 мс | bybit_spot_book 40 сд. p50=119.5 мс | okx 16 сд. p50=152.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:11:03 [pm] T-236.7s Up 0.77/0.78 Down 0.22/0.23 ptb=81222.7 | CLOB 7892 сообщ., задержка p50/p90=42.0/48.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792278663285 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.7/2.5 мс
23:11:04 [cex] Binance 122 сд. задержка p50/p90=159.2/160.2 мс | Coinbase 69 задержка p50=75.4 мс | смещение часов +19.4 мс | lag loop p99/max=2.3/2.7 мс
23:11:04 [cex] binance_futures 104 сд. p50=153.5 мс | bybit 133 сд. p50=126.7 мс | bybit_book 163 сд. p50=122.8 мс | bybit_spot 196 сд. p50=126.0 мс | bybit_spot_book 145 сд. p50=119.6 мс | okx 178 сд. p50=153.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: b24b4e3; python 3.12.3
