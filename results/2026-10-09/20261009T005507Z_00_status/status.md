# Состояние сервера записи

Время (UTC): 2026-10-09 00:55:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 1 day, 17 hours, 31 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         659         592           2         848        1246
Swap:           2047           0        2047
```
- нагрузка CPU (1/5/15 мин): 0.27 / 0.22 / 0.21

## Данные
- файлов: 333, всего 271 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 13 | 4 МБ | 2 |
| bn_book | 13 | 370 КБ | 2 |
| bnf_agg | 13 | 6 МБ | 2 |
| bnf_book | 13 | 203 МБ | 1 |
| bnf_depth5 | 13 | 11 МБ | 2 |
| bnf_liq | 13 | 17 КБ | 1433 |
| bs_trade | 13 | 375 КБ | 2 |
| by_book1 | 13 | 13 МБ | 2 |
| by_liq | 11 | 20 КБ | 7669 |
| by_trade | 13 | 5 МБ | 2 |
| cb_ticker | 13 | 3 МБ | 2 |
| clock | 13 | 11 КБ | 63 |
| clock_pm | 13 | 11 КБ | 63 |
| events | 10 | 4 КБ | 209 |
| events_pm | 13 | 10 КБ | 287 |
| health_cex | 13 | 154 КБ | 6 |
| health_feeds | 13 | 632 КБ | 6 |
| health_pm | 13 | 156 КБ | 8 |
| kr_trade | 13 | 881 КБ | 10 |
| ok_trade | 13 | 6 МБ | 2 |
| pm_depth | 13 | 4 МБ | 2 |
| pm_rtt | 13 | 115 КБ | 6 |
| pm_top | 13 | 9 МБ | 2 |
| pm_trades | 13 | 5 МБ | 2 |
| rtds | 13 | 1 МБ | 2 |
| windows | 13 | 28 КБ | 333 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 41, всего 290
- Polymarket CLOB: TCP 6, TLS 43, всего 84
- Polymarket gamma: TCP 5, TLS 41, всего 54

## Последние строки журнала записи
```
00:54:20 [cex] Binance 29 сд. задержка p50/p90=143.2/144.1 мс | Coinbase 36 задержка p50=77.9 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/3.5 мс
00:54:20 [cex] binance_futures 33 сд. p50=292.1 мс | bybit 65 сд. p50=113.1 мс | okx 29 сд. p50=144.0 мс | binance_futures_book 1840 сд. p50=143.7 мс | binance_futures_depth 90 сд. p50=143.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 98 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 0 сд. p50=n/a мс | bitstamp 6 сд. p50=45.2 мс
00:54:29 [pm] T- 31.0s Up 0.98/0.99 Down 0.01/0.02 ptb=81810.7 | CLOB 2682 сообщ., задержка p50/p90=40.0/42.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791507269037 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.0 мс | lag loop p99/max=1.9/2.1 мс
00:54:30 [cex] Binance 11 сд. задержка p50/p90=143.2/143.3 мс | Coinbase 37 задержка p50=81.2 мс | смещение часов +19.1 мс | lag loop p99/max=2.3/2.3 мс
00:54:30 [cex] binance_futures 26 сд. p50=292.2 мс | bybit 33 сд. p50=113.0 мс | okx 17 сд. p50=143.6 мс | binance_futures_book 722 сд. p50=143.5 мс | binance_futures_depth 81 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 112 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=39.7 мс | bitstamp 31 сд. p50=89.9 мс
00:54:39 [pm] T- 21.0s Up 0.99/n/a Down n/a/0.01 ptb=81810.7 | CLOB 1091 сообщ., задержка p50/p90=40.3/48.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791507279038 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.0 мс | lag loop p99/max=2.1/2.2 мс
00:54:40 [cex] Binance 14 сд. задержка p50/p90=143.2/148.5 мс | Coinbase 27 задержка p50=74.9 мс | смещение часов +19.1 мс | lag loop p99/max=2.2/4.4 мс
00:54:40 [cex] binance_futures 67 сд. p50=150.3 мс | bybit 71 сд. p50=125.4 мс | okx 30 сд. p50=150.6 мс | binance_futures_book 3847 сд. p50=147.4 мс | binance_futures_depth 86 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 195 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 22 сд. p50=37.5 мс | bitstamp 4 сд. p50=44.9 мс
00:54:45 [pm] окно btc-updown-5m-1791507300 (2026-10-09 00:55:00 UTC): Bitcoin Up or Down - October 8, 8:55PM-9:00PM ET
00:54:49 [pm] T- 11.0s Up 0.99/n/a Down n/a/0.01 ptb=81810.7 | CLOB 1009 сообщ., задержка p50/p90=39.8/43.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791507289039 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.0 мс | lag loop p99/max=2.2/12.9 мс
00:54:50 [cex] Binance 11 сд. задержка p50/p90=143.3/144.2 мс | Coinbase 42 задержка p50=75.2 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.1 мс
00:54:50 [cex] binance_futures 11 сд. p50=292.4 мс | bybit 34 сд. p50=112.8 мс | okx 9 сд. p50=143.4 мс | binance_futures_book 972 сд. p50=143.6 мс | binance_futures_depth 85 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 194 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 11 сд. p50=72.7 мс | bitstamp 4 сд. p50=46.5 мс
00:54:59 [pm] T-  1.0s Up 0.99/n/a Down n/a/0.01 ptb=81810.7 | CLOB 1927 сообщ., задержка p50/p90=37.0/40.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791507299041 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.0/2.2 мс
00:55:00 [cex] Binance 14 сд. задержка p50/p90=143.5/144.4 мс | Coinbase 18 задержка p50=74.7 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.2 мс
00:55:00 [cex] binance_futures 75 сд. p50=144.5 мс | bybit 110 сд. p50=113.3 мс | okx 43 сд. p50=144.4 мс | binance_futures_book 4527 сд. p50=143.8 мс | binance_futures_depth 94 сд. p50=143.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 237 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 23 сд. p50=41.9 мс | bitstamp 5 сд. p50=45.9 мс
```

Представлено версией кода: 46d373e; python 3.12.3
