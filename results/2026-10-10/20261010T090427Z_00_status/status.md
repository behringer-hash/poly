# Состояние сервера записи

Время (UTC): 2026-10-10 09:04:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 1 hour, 40 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         691         948           2         474        1215
Swap:           2047          24        2023
```
- нагрузка CPU (1/5/15 мин): 0.19 / 0.22 / 0.22

## Данные
- файлов: 1184, всего 367 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 46 | 6 МБ | 1 |
| bn_book | 46 | 615 КБ | 196 |
| bnf_agg | 46 | 10 МБ | 1 |
| bnf_book | 46 | 244 МБ | 1 |
| bnf_depth5 | 46 | 17 МБ | 1 |
| bnf_liq | 42 | 30 КБ | 2102 |
| bs_trade | 46 | 723 КБ | 3 |
| by_book1 | 46 | 20 МБ | 1 |
| by_liq | 41 | 29 КБ | 1410 |
| by_trade | 46 | 6 МБ | 1 |
| cb_ticker | 46 | 6 МБ | 1 |
| clock | 46 | 34 КБ | 33 |
| clock_pm | 46 | 34 КБ | 48 |
| events | 43 | 15 КБ | 249 |
| events_pm | 46 | 20 КБ | 66 |
| health_cex | 46 | 479 КБ | 9 |
| health_feeds | 46 | 2 МБ | 9 |
| health_pm | 46 | 491 КБ | 1 |
| kr_trade | 46 | 1 МБ | 1 |
| ok_trade | 46 | 9 МБ | 1 |
| pm_depth | 46 | 9 МБ | 1 |
| pm_rtt | 46 | 299 КБ | 1 |
| pm_top | 46 | 18 МБ | 1 |
| pm_trades | 46 | 13 МБ | 1 |
| rtds | 46 | 3 МБ | 1 |
| windows | 46 | 92 КБ | 23 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 6, TLS 39, всего 288
- Polymarket CLOB: TCP 7, TLS 40, всего 86
- Polymarket gamma: TCP 5, TLS 36, всего 47

## Последние строки журнала записи
```
09:03:45 [pm] T- 74.6s Up 0.94/0.95 Down 0.05/0.06 ptb=82766.5 | CLOB 2357 сообщ., задержка p50/p90=39.7/42.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791623025443 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=1.8/1.9 мс
09:03:47 [cex] Binance 12 сд. задержка p50/p90=153.5/153.9 мс | Coinbase 3 задержка p50=79.7 мс | смещение часов +19.8 мс | lag loop p99/max=2.1/2.1 мс
09:03:47 [cex] binance_futures 34 сд. p50=293.3 мс | bybit 3 сд. p50=114.2 мс | okx 71 сд. p50=156.0 мс | binance_futures_book 488 сд. p50=154.0 мс | binance_futures_depth 94 сд. p50=144.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 44 сд. p50=111.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=38.9 мс | bitstamp 1 сд. p50=44.9 мс
09:03:55 [pm] T- 64.6s Up 0.96/0.97 Down 0.03/0.04 ptb=82766.5 | CLOB 2291 сообщ., задержка p50/p90=38.7/43.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791623035445 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.1/2.2 мс
09:03:57 [cex] Binance 17 сд. задержка p50/p90=153.4/153.6 мс | Coinbase 12 задержка p50=78.8 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/2.2 мс
09:03:57 [cex] binance_futures 31 сд. p50=293.1 мс | bybit 7 сд. p50=112.9 мс | okx 49 сд. p50=155.6 мс | binance_futures_book 423 сд. p50=153.6 мс | binance_futures_depth 96 сд. p50=144.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 38 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=37.9 мс | bitstamp 0 сд. p50=n/a мс
09:04:05 [pm] T- 54.6s Up 0.97/0.98 Down 0.02/0.03 ptb=82766.5 | CLOB 1724 сообщ., задержка p50/p90=38.7/43.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791623045446 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/4.5 мс
09:04:07 [cex] Binance 16 сд. задержка p50/p90=152.5/153.4 мс | Coinbase 3 задержка p50=78.4 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/2.6 мс
09:04:07 [cex] binance_futures 35 сд. p50=292.2 мс | bybit 7 сд. p50=112.9 мс | okx 60 сд. p50=154.7 мс | binance_futures_book 471 сд. p50=152.9 мс | binance_futures_depth 94 сд. p50=143.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 96 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=39.2 мс | bitstamp 1 сд. p50=44.1 мс
09:04:15 [pm] T- 44.6s Up 0.98/0.99 Down 0.01/0.02 ptb=82766.5 | CLOB 1233 сообщ., задержка p50/p90=38.8/58.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791623055448 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.0/2.3 мс
09:04:17 [cex] Binance 22 сд. задержка p50/p90=152.5/153.4 мс | Coinbase 14 задержка p50=77.9 мс | смещение часов +18.7 мс | lag loop p99/max=1.8/2.1 мс
09:04:17 [cex] binance_futures 40 сд. p50=292.1 мс | bybit 14 сд. p50=113.1 мс | okx 38 сд. p50=154.7 мс | binance_futures_book 492 сд. p50=152.9 мс | binance_futures_depth 96 сд. p50=144.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 129 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=62.5 мс | bitstamp 0 сд. p50=n/a мс
09:04:25 [pm] T- 34.5s Up 0.99/n/a Down n/a/0.01 ptb=82766.5 | CLOB 891 сообщ., задержка p50/p90=38.7/41.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791623065450 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/2.1 мс
09:04:27 [cex] Binance 23 сд. задержка p50/p90=152.5/153.4 мс | Coinbase 10 задержка p50=78.4 мс | смещение часов +18.7 мс | lag loop p99/max=1.8/1.8 мс
09:04:27 [cex] binance_futures 33 сд. p50=292.1 мс | bybit 9 сд. p50=113.3 мс | okx 30 сд. p50=154.8 мс | binance_futures_book 486 сд. p50=152.8 мс | binance_futures_depth 92 сд. p50=144.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 155 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=40.9 мс | bitstamp 1 сд. p50=44.3 мс
```

Представлено версией кода: ad2ad9b; python 3.12.3
