# Состояние сервера записи

Время (UTC): 2026-10-08 19:46:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 1 day, 12 hours, 22 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         644         710           2         744        1261
Swap:           2047           0        2047
```
- нагрузка CPU (1/5/15 мин): 0.14 / 0.19 / 0.20

## Данные
- файлов: 205, всего 240 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 8 | 3 МБ | 1 |
| bn_book | 8 | 327 КБ | 9 |
| bnf_agg | 8 | 6 МБ | 1 |
| bnf_book | 8 | 183 МБ | 1 |
| bnf_depth5 | 8 | 8 МБ | 1 |
| bnf_liq | 8 | 16 КБ | 106 |
| bs_trade | 8 | 319 КБ | 1 |
| by_book1 | 8 | 11 МБ | 1 |
| by_liq | 8 | 20 КБ | 472 |
| by_trade | 8 | 5 МБ | 1 |
| cb_ticker | 8 | 3 МБ | 1 |
| clock | 8 | 7 КБ | 55 |
| clock_pm | 8 | 7 КБ | 54 |
| events | 5 | 2 КБ | 1188 |
| events_pm | 8 | 5 КБ | 72 |
| health_cex | 8 | 97 КБ | 9 |
| health_feeds | 8 | 412 КБ | 9 |
| health_pm | 8 | 97 КБ | 0 |
| kr_trade | 8 | 763 КБ | 1 |
| ok_trade | 8 | 5 МБ | 1 |
| pm_depth | 8 | 3 МБ | 0 |
| pm_rtt | 8 | 76 КБ | 2 |
| pm_top | 8 | 6 МБ | 0 |
| pm_trades | 8 | 3 МБ | 0 |
| rtds | 8 | 797 КБ | 0 |
| windows | 8 | 18 КБ | 94 |

Дни с данными: 2026-10-08

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 44, всего 296
- Polymarket CLOB: TCP 5, TLS 44, всего 99
- Polymarket gamma: TCP 5, TLS 39, всего 52

## Последние строки журнала записи
```
19:45:56 [pm] T-243.5s Up 0.48/0.49 Down 0.51/0.52 ptb=81674.0 | CLOB 8457 сообщ., задержка p50/p90=241.6/316.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791488756467 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=3.2/3.4 мс
19:45:57 [cex] Binance 86 сд. задержка p50/p90=143.9/146.7 мс | Coinbase 69 задержка p50=81.5 мс | смещение часов +19.2 мс | lag loop p99/max=2.0/2.1 мс
19:45:57 [cex] binance_futures 235 сд. p50=148.6 мс | bybit 333 сд. p50=113.8 мс | okx 197 сд. p50=151.8 мс | binance_futures_book 4150 сд. p50=144.2 мс | binance_futures_depth 93 сд. p50=156.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 366 сд. p50=111.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 30 сд. p50=51.4 мс | bitstamp 13 сд. p50=48.7 мс
19:46:06 [pm] T-233.5s Up 0.46/0.47 Down 0.53/0.54 ptb=81674.0 | CLOB 8083 сообщ., задержка p50/p90=87.2/186.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791488766468 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.5/5.4 мс
19:46:07 [cex] Binance 21 сд. задержка p50/p90=143.6/143.8 мс | Coinbase 9 задержка p50=79.7 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.3 мс
19:46:07 [cex] binance_futures 36 сд. p50=292.8 мс | bybit 104 сд. p50=113.2 мс | okx 26 сд. p50=151.0 мс | binance_futures_book 1104 сд. p50=143.9 мс | binance_futures_depth 89 сд. p50=156.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 278 сд. p50=111.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 8 сд. p50=44.7 мс | bitstamp 4 сд. p50=45.8 мс
19:46:16 [pm] T-223.5s Up 0.41/0.42 Down 0.58/0.59 ptb=81674.0 | CLOB 8134 сообщ., задержка p50/p90=43.1/53.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791488776470 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.7/2.1 мс
19:46:17 [cex] Binance 40 сд. задержка p50/p90=143.8/148.1 мс | Coinbase 75 задержка p50=80.9 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.2 мс
19:46:17 [cex] binance_futures 95 сд. p50=151.7 мс | bybit 167 сд. p50=114.9 мс | okx 85 сд. p50=151.9 мс | binance_futures_book 3774 сд. p50=145.0 мс | binance_futures_depth 93 сд. p50=156.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 252 сд. p50=111.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=42.1 мс | bitstamp 6 сд. p50=48.9 мс
19:46:26 [pm] T-213.5s Up 0.40/0.41 Down 0.59/0.60 ptb=81674.0 | CLOB 8690 сообщ., задержка p50/p90=43.9/289.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791488786471 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.2/1.3 мс
19:46:27 [cex] Binance 35 сд. задержка p50/p90=143.5/150.7 мс | Coinbase 28 задержка p50=80.3 мс | смещение часов +19.2 мс | lag loop p99/max=2.2/2.2 мс
19:46:27 [cex] binance_futures 57 сд. p50=254.8 мс | bybit 150 сд. p50=113.9 мс | okx 42 сд. p50=151.4 мс | binance_futures_book 2225 сд. p50=144.2 мс | binance_futures_depth 95 сд. p50=156.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 212 сд. p50=111.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 19 сд. p50=43.6 мс | bitstamp 8 сд. p50=57.4 мс
19:46:36 [pm] T-203.5s Up 0.42/0.43 Down 0.57/0.58 ptb=81674.0 | CLOB 9134 сообщ., задержка p50/p90=44.6/605.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791488796473 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=2.0/2.0 мс
19:46:37 [cex] Binance 24 сд. задержка p50/p90=143.6/144.3 мс | Coinbase 37 задержка p50=81.7 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.1 мс
19:46:37 [cex] binance_futures 50 сд. p50=259.9 мс | bybit 106 сд. p50=112.9 мс | okx 64 сд. p50=151.6 мс | binance_futures_book 2200 сд. p50=144.1 мс | binance_futures_depth 93 сд. p50=156.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 232 сд. p50=111.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 18 сд. p50=42.8 мс | bitstamp 5 сд. p50=48.1 мс
```

Представлено версией кода: 46d373e; python 3.12.3
