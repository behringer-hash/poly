# Состояние сервера записи

Время (UTC): 2026-10-11 05:57:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 22 hours, 33 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         691         938           2         484        1214
Swap:           2047          61        1986
```
- нагрузка CPU (1/5/15 мин): 0.07 / 0.15 / 0.17

## Данные
- файлов: 1692, всего 468 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 66 | 8 МБ | 1 |
| bn_book | 66 | 674 КБ | 47 |
| bnf_agg | 66 | 12 МБ | 1 |
| bnf_book | 66 | 298 МБ | 1 |
| bnf_depth5 | 66 | 28 МБ | 1 |
| bnf_liq | 55 | 34 КБ | 338 |
| bs_trade | 66 | 878 КБ | 11 |
| by_book1 | 66 | 25 МБ | 1 |
| by_liq | 56 | 32 КБ | 346 |
| by_trade | 66 | 8 МБ | 3 |
| cb_ticker | 66 | 7 МБ | 3 |
| clock | 66 | 52 КБ | 1 |
| clock_pm | 66 | 51 КБ | 17 |
| events | 63 | 23 КБ | 708 |
| events_pm | 66 | 26 КБ | 881 |
| health_cex | 66 | 709 КБ | 1 |
| health_feeds | 66 | 3 МБ | 1 |
| health_pm | 66 | 729 КБ | 1 |
| kr_trade | 66 | 2 МБ | 1 |
| ok_trade | 66 | 11 МБ | 1 |
| pm_depth | 66 | 14 МБ | 1 |
| pm_rtt | 66 | 469 КБ | 5 |
| pm_top | 66 | 28 МБ | 1 |
| pm_trades | 66 | 19 МБ | 1 |
| rtds | 66 | 4 МБ | 1 |
| windows | 66 | 138 КБ | 64 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 39, всего 289
- Polymarket CLOB: TCP 5, TLS 41, всего 86
- Polymarket gamma: TCP 5, TLS 38, всего 49

## Последние строки журнала записи
```
05:56:26 [pm] T-213.9s Up 0.14/0.15 Down 0.85/0.86 ptb=82974.7 | CLOB 4428 сообщ., задержка p50/p90=39.2/45.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791698186142 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.6/2.0 мс
05:56:26 [cex] Binance 57 сд. задержка p50/p90=144.6/146.2 мс | Coinbase 11 задержка p50=80.8 мс | смещение часов +19.6 мс | lag loop p99/max=2.1/2.1 мс
05:56:26 [cex] binance_futures 54 сд. p50=147.9 мс | bybit 46 сд. p50=114.6 мс | okx 70 сд. p50=153.8 мс | binance_futures_book 1222 сд. p50=145.4 мс | binance_futures_depth 89 сд. p50=144.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 113 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=39.8 мс | bitstamp 5 сд. p50=65.8 мс
05:56:36 [pm] T-203.9s Up 0.13/0.14 Down 0.86/0.87 ptb=82974.7 | CLOB 2840 сообщ., задержка p50/p90=38.4/43.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791698196144 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.2/1.2 мс
05:56:36 [cex] Binance 21 сд. задержка p50/p90=143.4/143.7 мс | Coinbase 11 задержка p50=82.5 мс | смещение часов +19.6 мс | lag loop p99/max=1.9/1.9 мс
05:56:36 [cex] binance_futures 38 сд. p50=292.9 мс | bybit 8 сд. p50=113.9 мс | okx 91 сд. p50=153.7 мс | binance_futures_book 511 сд. p50=144.2 мс | binance_futures_depth 92 сд. p50=145.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 93 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=43.3 мс | bitstamp 0 сд. p50=n/a мс
05:56:46 [pm] T-193.9s Up 0.16/0.17 Down 0.83/0.84 ptb=82974.7 | CLOB 2868 сообщ., задержка p50/p90=39.0/51.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791698206145 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.1/2.2 мс
05:56:46 [cex] Binance 24 сд. задержка p50/p90=143.4/144.3 мс | Coinbase 4 задержка p50=81.5 мс | смещение часов +19.6 мс | lag loop p99/max=2.1/2.3 мс
05:56:46 [cex] binance_futures 34 сд. p50=293.0 мс | bybit 7 сд. p50=113.9 мс | okx 41 сд. p50=153.3 мс | binance_futures_book 504 сд. p50=144.1 мс | binance_futures_depth 84 сд. p50=145.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 67 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 9 сд. p50=43.0 мс | bitstamp 1 сд. p50=44.8 мс
05:56:56 [pm] T-183.9s Up 0.18/0.19 Down 0.81/0.82 ptb=82974.7 | CLOB 4013 сообщ., задержка p50/p90=38.6/49.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791698216147 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.8/1.9 мс
05:56:56 [cex] Binance 30 сд. задержка p50/p90=143.4/144.4 мс | Coinbase 7 задержка p50=81.6 мс | смещение часов +19.6 мс | lag loop p99/max=2.2/2.2 мс
05:56:56 [cex] binance_futures 45 сд. p50=292.9 мс | bybit 3 сд. p50=114.0 мс | okx 20 сд. p50=153.4 мс | binance_futures_book 574 сд. p50=144.2 мс | binance_futures_depth 85 сд. p50=144.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 72 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=40.6 мс | bitstamp 1 сд. p50=45.7 мс
05:57:06 [pm] T-173.9s Up 0.15/0.16 Down 0.84/0.85 ptb=82974.7 | CLOB 2062 сообщ., задержка p50/p90=37.6/52.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791698226149 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=2.1/4.0 мс
05:57:06 [cex] Binance 14 сд. задержка p50/p90=143.5/144.4 мс | Coinbase 5 задержка p50=81.4 мс | смещение часов +19.6 мс | lag loop p99/max=2.1/4.8 мс
05:57:06 [cex] binance_futures 36 сд. p50=293.0 мс | bybit 8 сд. p50=113.6 мс | okx 33 сд. p50=153.4 мс | binance_futures_book 502 сд. p50=144.2 мс | binance_futures_depth 84 сд. p50=144.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 59 сд. p50=111.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=51.6 мс | bitstamp 1 сд. p50=50.6 мс
```

Представлено версией кода: 69087ca; python 3.12.3
