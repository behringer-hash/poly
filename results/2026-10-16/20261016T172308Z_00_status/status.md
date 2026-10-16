# Состояние сервера записи

Время (UTC): 2026-10-16 17:23:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 9 hours, 59 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         565        1284           2         284        1340
Swap:           2047         243        1804
```
- нагрузка CPU (1/5/15 мин): 0.24 / 0.28 / 0.33

## Данные
- файлов: 4939, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 198 | 28 МБ | 1 |
| bn_book | 198 | 3 МБ | 3 |
| bnf_agg | 198 | 44 МБ | 1 |
| bnf_book | 118 | 557 МБ | 286482 |
| bnf_depth5 | 118 | 41 МБ | 286558 |
| bnf_liq | 178 | 130 КБ | 17 |
| bs_trade | 118 | 1 МБ | 286478 |
| by_book1 | 198 | 90 МБ | 1 |
| by_liq | 177 | 107 КБ | 216 |
| by_trade | 198 | 30 МБ | 1 |
| bys_book1 | 82 | 35 МБ | 1 |
| bys_trade | 82 | 15 МБ | 1 |
| cb_ticker | 198 | 26 МБ | 1 |
| clock | 198 | 153 КБ | 9 |
| clock_pm | 198 | 153 КБ | 29 |
| events | 187 | 60 КБ | 1172 |
| events_pm | 198 | 73 КБ | 23 |
| health_cex | 198 | 2 МБ | 5 |
| health_feeds | 198 | 7 МБ | 5 |
| health_pm | 198 | 2 МБ | 0 |
| kr_trade | 118 | 3 МБ | 286478 |
| ok_trade | 197 | 39 МБ | 1 |
| pm_depth | 198 | 40 МБ | 0 |
| pm_rtt | 198 | 1 МБ | 0 |
| pm_top | 198 | 81 МБ | 0 |
| pm_trades | 198 | 59 МБ | 0 |
| rtds | 198 | 13 МБ | 0 |
| windows | 198 | 408 КБ | 275 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 47, всего 314
- Polymarket CLOB: TCP 5, TLS 47, всего 94
- Polymarket gamma: TCP 5, TLS 54, всего 67

## Последние строки журнала записи
```
17:22:22 [cex] binance_futures 485 сд. p50=147.7 мс | bybit 510 сд. p50=115.8 мс | bybit_book 513 сд. p50=113.6 мс | bybit_spot 631 сд. p50=115.4 мс | bybit_spot_book 364 сд. p50=113.8 мс | okx 327 сд. p50=156.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:22:27 [pm] T-152.7s Up 0.82/0.83 Down 0.17/0.18 ptb=80751.7 | CLOB 13185 сообщ., задержка p50/p90=40.9/45.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792171347251 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=1.3/1.6 мс
17:22:32 [cex] Binance 268 сд. задержка p50/p90=146.7/147.9 мс | Coinbase 383 задержка p50=80.1 мс | смещение часов +21.6 мс | lag loop p99/max=2.0/2.1 мс
17:22:32 [cex] binance_futures 388 сд. p50=148.1 мс | bybit 446 сд. p50=116.0 мс | bybit_book 466 сд. p50=113.6 мс | bybit_spot 327 сд. p50=115.7 мс | bybit_spot_book 279 сд. p50=113.8 мс | okx 437 сд. p50=156.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:22:37 [pm] T-142.7s Up 0.79/0.80 Down 0.20/0.21 ptb=80751.7 | CLOB 13111 сообщ., задержка p50/p90=42.2/72.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792171357252 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=1.5/1.8 мс
17:22:42 [cex] Binance 270 сд. задержка p50/p90=146.7/148.8 мс | Coinbase 408 задержка p50=79.7 мс | смещение часов +21.6 мс | lag loop p99/max=1.9/2.5 мс
17:22:42 [cex] binance_futures 297 сд. p50=148.2 мс | bybit 353 сд. p50=115.9 мс | bybit_book 369 сд. p50=113.6 мс | bybit_spot 238 сд. p50=115.6 мс | bybit_spot_book 266 сд. p50=113.8 мс | okx 319 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:22:43 [pm] btc-updown-5m-1792171200: CLOB#0 разорван (ConnectionClosedError(Close(code=1013, reason='slow consumer: send buffer full'), Close(code=1013, reason='slow consumer: send buffer full'), True)), переподключение
17:22:47 [pm] T-132.7s Up 0.63/0.64 Down 0.36/0.37 ptb=80751.7 | CLOB 11683 сообщ., задержка p50/p90=44.9/48.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792171367254 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=2.4/22.8 мс
17:22:52 [cex] Binance 230 сд. задержка p50/p90=146.6/147.4 мс | Coinbase 310 задержка p50=81.6 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.2 мс
17:22:52 [cex] binance_futures 383 сд. p50=148.1 мс | bybit 362 сд. p50=115.8 мс | bybit_book 384 сд. p50=113.6 мс | bybit_spot 296 сд. p50=115.8 мс | bybit_spot_book 282 сд. p50=113.7 мс | okx 539 сд. p50=156.8 мс | binance_liq 1 сд. p50=1164.1 мс | bybit_liq 0 сд. p50=n/a мс
17:22:57 [pm] T-122.7s Up 0.49/0.50 Down 0.50/0.51 ptb=80751.7 | CLOB 8273 сообщ., задержка p50/p90=45.8/50.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792171377255 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=1.7/2.1 мс
17:23:02 [cex] Binance 96 сд. задержка p50/p90=146.7/150.2 мс | Coinbase 593 задержка p50=83.8 мс | смещение часов +25.2 мс | lag loop p99/max=1.9/2.0 мс
17:23:02 [cex] binance_futures 277 сд. p50=149.7 мс | bybit 342 сд. p50=116.0 мс | bybit_book 464 сд. p50=113.9 мс | bybit_spot 248 сд. p50=115.8 мс | bybit_spot_book 308 сд. p50=114.0 мс | okx 414 сд. p50=157.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:23:07 [pm] T-112.7s Up 0.58/0.59 Down 0.41/0.42 ptb=80751.7 | CLOB 10132 сообщ., задержка p50/p90=50.0/66.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792171387257 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=6.5/10.1 мс
```

Представлено версией кода: 8083be6; python 3.12.3
