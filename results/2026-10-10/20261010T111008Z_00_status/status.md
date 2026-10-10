# Состояние сервера записи

Время (UTC): 2026-10-10 11:10:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 3 hours, 46 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         697         982           2         435        1208
Swap:           2047          38        2009
```
- нагрузка CPU (1/5/15 мин): 0.09 / 0.10 / 0.10

## Данные
- файлов: 1234, всего 376 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 48 | 6 МБ | 2 |
| bn_book | 48 | 620 КБ | 20 |
| bnf_agg | 48 | 10 МБ | 2 |
| bnf_book | 48 | 249 МБ | 1 |
| bnf_depth5 | 48 | 18 МБ | 2 |
| bnf_liq | 43 | 30 КБ | 1494 |
| bs_trade | 48 | 737 КБ | 6 |
| by_book1 | 48 | 20 МБ | 2 |
| by_liq | 43 | 29 КБ | 1074 |
| by_trade | 48 | 7 МБ | 2 |
| cb_ticker | 48 | 6 МБ | 2 |
| clock | 48 | 36 КБ | 8 |
| clock_pm | 48 | 36 КБ | 24 |
| events | 45 | 16 КБ | 271 |
| events_pm | 47 | 21 КБ | 2278 |
| health_cex | 48 | 502 КБ | 10 |
| health_feeds | 48 | 2 МБ | 10 |
| health_pm | 48 | 515 КБ | 10 |
| kr_trade | 48 | 2 МБ | 2 |
| ok_trade | 48 | 9 МБ | 4 |
| pm_depth | 48 | 10 МБ | 2 |
| pm_rtt | 48 | 316 КБ | 4 |
| pm_top | 48 | 19 МБ | 2 |
| pm_trades | 48 | 13 МБ | 2 |
| rtds | 48 | 3 МБ | 2 |
| windows | 48 | 97 КБ | 93 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 38, всего 289
- Polymarket CLOB: TCP 5, TLS 39, всего 87
- Polymarket gamma: TCP 5, TLS 40, всего 51

## Последние строки журнала записи
```
11:09:28 [cex] Binance 27 сд. задержка p50/p90=158.1/159.0 мс | Coinbase 10 задержка p50=80.6 мс | смещение часов +21.5 мс | lag loop p99/max=2.2/2.2 мс
11:09:28 [cex] binance_futures 31 сд. p50=294.7 мс | bybit 4 сд. p50=115.6 мс | okx 23 сд. p50=144.8 мс | binance_futures_book 406 сд. p50=146.0 мс | binance_futures_depth 87 сд. p50=146.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 58 сд. p50=113.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=39.0 мс | bitstamp 1 сд. p50=49.2 мс
11:09:36 [pm] T- 23.5s Up n/a/0.01 Down 0.99/n/a ptb=82764.9 | CLOB 1470 сообщ., задержка p50/p90=40.2/52.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791630576548 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=2.1/2.1 мс
11:09:38 [cex] Binance 20 сд. задержка p50/p90=145.9/158.1 мс | Coinbase 19 задержка p50=81.2 мс | смещение часов +21.5 мс | lag loop p99/max=2.1/2.2 мс
11:09:38 [cex] binance_futures 30 сд. p50=294.7 мс | bybit 3 сд. p50=115.9 мс | okx 22 сд. p50=145.1 мс | binance_futures_book 212 сд. p50=145.9 мс | binance_futures_depth 88 сд. p50=146.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 48 сд. p50=113.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=39.5 мс | bitstamp 6 сд. p50=50.5 мс
11:09:45 [pm] окно btc-updown-5m-1791630600 (2026-10-10 11:10:00 UTC): Bitcoin Up or Down - October 10, 7:10AM-7:15AM ET
11:09:46 [pm] T- 13.4s Up n/a/0.01 Down 0.99/n/a ptb=82764.9 | CLOB 786 сообщ., задержка p50/p90=39.1/41.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791630586550 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=2.1/8.9 мс
11:09:48 [cex] Binance 29 сд. задержка p50/p90=145.8/146.8 мс | Coinbase 28 задержка p50=81.6 мс | смещение часов +21.5 мс | lag loop p99/max=2.0/2.2 мс
11:09:48 [cex] binance_futures 30 сд. p50=294.7 мс | bybit 2 сд. p50=115.5 мс | okx 19 сд. p50=144.9 мс | binance_futures_book 360 сд. p50=146.0 мс | binance_futures_depth 88 сд. p50=146.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 60 сд. p50=113.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=40.5 мс | bitstamp 1 сд. p50=47.6 мс
11:09:56 [pm] T-  3.4s Up n/a/0.01 Down 0.99/n/a ptb=82764.9 | CLOB 1450 сообщ., задержка p50/p90=38.2/41.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791630596551 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.0/2.1 мс
11:09:58 [cex] Binance 22 сд. задержка p50/p90=145.7/146.1 мс | Coinbase 6 задержка p50=80.2 мс | смещение часов +21.5 мс | lag loop p99/max=2.0/2.3 мс
11:09:58 [cex] binance_futures 27 сд. p50=294.7 мс | bybit 28 сд. p50=116.0 мс | okx 28 сд. p50=145.2 мс | binance_futures_book 602 сд. p50=145.9 мс | binance_futures_depth 90 сд. p50=146.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 84 сд. p50=113.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 10 сд. p50=39.6 мс | bitstamp 3 сд. p50=50.9 мс
11:10:06 [pm] T-293.4s Up 0.39/0.40 Down 0.60/0.61 ptb=82761.9 | CLOB 2322 сообщ., задержка p50/p90=38.6/48.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791630606552 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=8.1/10.2 мс
11:10:08 [cex] Binance 26 сд. задержка p50/p90=144.1/145.5 мс | Coinbase 10 задержка p50=80.2 мс | смещение часов +19.7 мс | lag loop p99/max=3.7/3.7 мс
11:10:08 [cex] binance_futures 29 сд. p50=293.3 мс | bybit 3 сд. p50=113.4 мс | okx 28 сд. p50=143.4 мс | binance_futures_book 1569 сд. p50=144.4 мс | binance_futures_depth 90 сд. p50=145.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 77 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=38.8 мс | bitstamp 1 сд. p50=47.5 мс
```

Представлено версией кода: 3ffd786; python 3.12.3
