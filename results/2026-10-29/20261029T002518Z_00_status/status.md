# Состояние сервера записи

Время (UTC): 2026-10-29 00:25:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 17 hours, 1 minute
- синхронизация часов: yes

## Ресурсы
- диск: занято 12 ГБ из 57 ГБ, свободно 45 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         610         707           1         763        1295
Swap:           2047         304        1743
```
- нагрузка CPU (1/5/15 мин): 0.06 / 0.11 / 0.12

## Данные
- файлов: 5804, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 34 МБ | 2 |
| bn_book | 242 | 3 МБ | 16 |
| bnf_agg | 242 | 49 МБ | 2 |
| bnf_book | 60 | 372 МБ | 0 |
| bnf_liq | 209 | 136 КБ | 9228 |
| by_book1 | 242 | 109 МБ | 2 |
| by_liq | 224 | 98 КБ | 6787 |
| by_trade | 242 | 34 МБ | 2 |
| bys_book1 | 242 | 82 МБ | 2 |
| bys_trade | 242 | 32 МБ | 2 |
| cb_ticker | 242 | 32 МБ | 2 |
| clock | 242 | 187 КБ | 14 |
| clock_pm | 242 | 187 КБ | 45 |
| events | 231 | 73 КБ | 52 |
| events_pm | 240 | 83 КБ | 2986 |
| health_cex | 242 | 2 МБ | 4 |
| health_feeds | 242 | 7 МБ | 4 |
| health_pm | 242 | 3 МБ | 7 |
| ok_trade | 242 | 43 МБ | 2 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 1 |
| pm_top | 242 | 101 МБ | 1 |
| pm_trades | 242 | 71 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 499 КБ | 13 |

Дни с данными: 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 8, TLS 45, всего 294
- Polymarket CLOB: TCP 6, TLS 46, всего 90
- Polymarket gamma: TCP 3, TLS 51, всего 58

## Последние строки журнала записи
```
00:24:33 [cex] Binance 12 сд. задержка p50/p90=143.4/144.2 мс | Coinbase 6 задержка p50=88.0 мс | смещение часов +19.4 мс | lag loop p99/max=2.1/2.1 мс
00:24:33 [cex] binance_futures 22 сд. p50=294.1 мс | bybit 13 сд. p50=112.1 мс | bybit_book 107 сд. p50=111.0 мс | bybit_spot 2 сд. p50=112.8 мс | bybit_spot_book 22 сд. p50=110.7 мс | okx 23 сд. p50=157.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 233 сд. p50=144.5 мс
00:24:40 [pm] T- 19.4s Up n/a/0.00 Down 1.00/n/a ptb=81176.8 | CLOB 466 сообщ., задержка p50/p90=38.7/42.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793233480581 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.1/2.1 мс
00:24:43 [cex] Binance 176 сд. задержка p50/p90=144.6/149.2 мс | Coinbase 65 задержка p50=91.7 мс | смещение часов +19.4 мс | lag loop p99/max=6.5/20.8 мс
00:24:43 [cex] binance_futures 228 сд. p50=148.5 мс | bybit 359 сд. p50=115.6 мс | bybit_book 290 сд. p50=111.1 мс | bybit_spot 431 сд. p50=113.9 мс | bybit_spot_book 170 сд. p50=110.9 мс | okx 172 сд. p50=157.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 10539 сд. p50=145.2 мс
00:24:45 [pm] окно btc-updown-5m-1793233500 (2026-10-29 00:25:00 UTC): Bitcoin Up or Down - October 28, 8:25PM-8:30PM ET
00:24:50 [pm] T-  9.4s Up n/a/0.00 Down 1.00/n/a ptb=81176.8 | CLOB 1269 сообщ., задержка p50/p90=40.8/44.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793233490582 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.1/21.9 мс
00:24:53 [cex] Binance 14 сд. задержка p50/p90=143.3/143.6 мс | Coinbase 39 задержка p50=88.2 мс | смещение часов +19.4 мс | lag loop p99/max=2.2/4.9 мс
00:24:53 [cex] binance_futures 20 сд. p50=293.7 мс | bybit 47 сд. p50=116.2 мс | bybit_book 306 сд. p50=110.9 мс | bybit_spot 70 сд. p50=114.1 мс | bybit_spot_book 51 сд. p50=111.0 мс | okx 40 сд. p50=157.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 783 сд. p50=144.8 мс
00:25:00 [pm] T-299.4s Up 0.47/0.48 Down 0.52/0.53 ptb=n/a | CLOB 2254 сообщ., задержка p50/p90=41.3/63.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793233500584 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.2/2.4 мс
00:25:03 [cex] Binance 172 сд. задержка p50/p90=150.9/156.4 мс | Coinbase 76 задержка p50=106.3 мс | смещение часов +19.4 мс | lag loop p99/max=3.6/8.0 мс
00:25:03 [cex] binance_futures 270 сд. p50=149.8 мс | bybit 210 сд. p50=114.3 мс | bybit_book 243 сд. p50=111.0 мс | bybit_spot 215 сд. p50=119.2 мс | bybit_spot_book 73 сд. p50=111.2 мс | okx 193 сд. p50=408.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3416 сд. p50=176.5 мс
00:25:10 [pm] T-289.4s Up 0.38/0.39 Down 0.61/0.62 ptb=81129.8 | CLOB 5965 сообщ., задержка p50/p90=42.0/48.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793233510585 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.9/2.1 мс
00:25:13 [cex] Binance 11 сд. задержка p50/p90=143.7/143.9 мс | Coinbase 41 задержка p50=89.5 мс | смещение часов +19.8 мс | lag loop p99/max=2.1/2.2 мс
00:25:13 [cex] binance_futures 44 сд. p50=272.1 мс | bybit 34 сд. p50=114.8 мс | bybit_book 160 сд. p50=111.4 мс | bybit_spot 42 сд. p50=115.0 мс | bybit_spot_book 81 сд. p50=111.3 мс | okx 28 сд. p50=157.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2233 сд. p50=147.5 мс
```

Представлено версией кода: 65c4468; python 3.12.3
