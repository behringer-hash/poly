# Состояние сервера записи

Время (UTC): 2026-10-27 12:11:05

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 6 days, 4 hours, 47 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         620         994           2         465        1285
Swap:           2047         404        1643
```
- нагрузка CPU (1/5/15 мин): 0.58 / 0.57 / 0.49

## Данные
- файлов: 5826, всего 995 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 34 МБ | 1 |
| bn_book | 242 | 3 МБ | 21 |
| bnf_agg | 242 | 50 МБ | 1 |
| bnf_book | 46 | 324 МБ | 0 |
| bnf_depth5 | 22 | 9 МБ | 1218236 |
| bnf_liq | 215 | 144 КБ | 3290 |
| bs_trade | 22 | 369 КБ | 1218155 |
| by_book1 | 242 | 109 МБ | 1 |
| by_liq | 227 | 106 КБ | 3312 |
| by_trade | 242 | 34 МБ | 3 |
| bys_book1 | 222 | 73 МБ | 1 |
| bys_trade | 222 | 29 МБ | 1 |
| cb_ticker | 242 | 32 МБ | 1 |
| clock | 242 | 187 КБ | 13 |
| clock_pm | 242 | 188 КБ | 27 |
| events | 232 | 74 КБ | 230 |
| events_pm | 241 | 84 КБ | 35 |
| health_cex | 242 | 2 МБ | 3 |
| health_feeds | 242 | 7 МБ | 3 |
| health_pm | 242 | 3 МБ | 3 |
| kr_trade | 22 | 779 КБ | 1218155 |
| ok_trade | 241 | 44 МБ | 1 |
| pm_depth | 242 | 49 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 5 |
| pm_top | 242 | 101 МБ | 1 |
| pm_trades | 242 | 71 МБ | 1 |
| rtds | 242 | 15 МБ | 1 |
| windows | 242 | 498 КБ | 301 |

Дни с данными: 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 39, всего 286
- Polymarket CLOB: TCP 5, TLS 41, всего 85
- Polymarket gamma: TCP 4, TLS 42, всего 49

## Последние строки журнала записи
```
12:10:21 [cex] Binance 42 сд. задержка p50/p90=142.9/143.7 мс | Coinbase 37 задержка p50=97.8 мс | смещение часов +20.0 мс | lag loop p99/max=2.1/2.2 мс
12:10:21 [cex] binance_futures 17 сд. p50=293.0 мс | bybit 27 сд. p50=111.8 мс | bybit_book 113 сд. p50=109.8 мс | bybit_spot 2 сд. p50=112.2 мс | bybit_spot_book 47 сд. p50=110.5 мс | okx 11 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 293 сд. p50=143.7 мс
12:10:30 [pm] btc-updown-5m-1793103000: CLOB#1 разорван (ConnectionClosedError(Close(code=1013, reason='slow consumer: send buffer full'), Close(code=1013, reason='slow consumer: send buffer full'), True)), переподключение
12:10:30 [pm] T-269.4s Up 0.85/0.86 Down 0.14/0.15 ptb=79727.6 | CLOB 5437 сообщ., задержка p50/p90=44.2/104.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793103030605 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=2.0/14.8 мс
12:10:31 [cex] Binance 126 сд. задержка p50/p90=143.3/147.1 мс | Coinbase 36 задержка p50=99.3 мс | смещение часов +20.0 мс | lag loop p99/max=7.6/15.2 мс
12:10:31 [cex] binance_futures 119 сд. p50=145.9 мс | bybit 116 сд. p50=112.9 мс | bybit_book 152 сд. p50=109.8 мс | bybit_spot 225 сд. p50=125.0 мс | bybit_spot_book 205 сд. p50=110.4 мс | okx 133 сд. p50=153.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3910 сд. p50=149.9 мс
12:10:40 [pm] T-259.4s Up 0.79/0.81 Down 0.19/0.21 ptb=79727.6 | CLOB 4924 сообщ., задержка p50/p90=41.9/59.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793103040607 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=1.4/1.7 мс
12:10:41 [cex] Binance 48 сд. задержка p50/p90=142.9/143.4 мс | Coinbase 35 задержка p50=99.6 мс | смещение часов +20.0 мс | lag loop p99/max=2.2/12.6 мс
12:10:41 [cex] binance_futures 66 сд. p50=157.6 мс | bybit 114 сд. p50=113.8 мс | bybit_book 155 сд. p50=109.8 мс | bybit_spot 115 сд. p50=124.8 мс | bybit_spot_book 98 сд. p50=110.3 мс | okx 41 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3727 сд. p50=144.3 мс
12:10:50 [pm] T-249.4s Up 0.81/0.82 Down 0.18/0.19 ptb=79727.6 | CLOB 8079 сообщ., задержка p50/p90=41.6/45.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793103050609 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=1.4/1.6 мс
12:10:51 [cex] Binance 50 сд. задержка p50/p90=143.1/146.5 мс | Coinbase 22 задержка p50=94.2 мс | смещение часов +20.0 мс | lag loop p99/max=2.1/2.3 мс
12:10:51 [cex] binance_futures 67 сд. p50=219.5 мс | bybit 89 сд. p50=112.3 мс | bybit_book 206 сд. p50=109.8 мс | bybit_spot 37 сд. p50=113.3 мс | bybit_spot_book 71 сд. p50=110.4 мс | okx 35 сд. p50=153.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2402 сд. p50=144.0 мс
12:11:00 [pm] T-239.4s Up 0.80/0.81 Down 0.19/0.20 ptb=79727.6 | CLOB 4478 сообщ., задержка p50/p90=41.6/50.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793103060610 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=1.7/2.0 мс
12:11:01 [cex] Binance 22 сд. задержка p50/p90=143.1/143.8 мс | Coinbase 17 задержка p50=92.8 мс | смещение часов +20.2 мс | lag loop p99/max=2.2/3.2 мс
12:11:01 [cex] binance_futures 22 сд. p50=293.1 мс | bybit 15 сд. p50=112.6 мс | bybit_book 114 сд. p50=109.9 мс | bybit_spot 5 сд. p50=111.8 мс | bybit_spot_book 95 сд. p50=110.5 мс | okx 66 сд. p50=153.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 664 сд. p50=144.0 мс
```

Представлено версией кода: f7c6584; python 3.12.3
