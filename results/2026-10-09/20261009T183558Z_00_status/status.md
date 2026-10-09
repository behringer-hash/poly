# Состояние сервера записи

Время (UTC): 2026-10-09 18:35:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 11 hours, 12 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         655         737           2         707        1250
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.18 / 0.15 / 0.19

## Данные
- файлов: 801, всего 367 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 31 | 6 МБ | 1 |
| bn_book | 31 | 579 КБ | 3 |
| bnf_agg | 31 | 9 МБ | 1 |
| bnf_book | 31 | 258 МБ | 1 |
| bnf_depth5 | 31 | 16 МБ | 1 |
| bnf_liq | 31 | 27 КБ | 7 |
| bs_trade | 31 | 628 КБ | 1 |
| by_book1 | 31 | 18 МБ | 1 |
| by_liq | 29 | 27 КБ | 41 |
| by_trade | 31 | 7 МБ | 1 |
| cb_ticker | 31 | 5 МБ | 1 |
| clock | 31 | 24 КБ | 53 |
| clock_pm | 31 | 24 КБ | 4 |
| events | 28 | 10 КБ | 546 |
| events_pm | 31 | 14 КБ | 461 |
| health_cex | 31 | 338 КБ | 7 |
| health_feeds | 31 | 1 МБ | 7 |
| health_pm | 31 | 346 КБ | 10 |
| kr_trade | 31 | 1 МБ | 1 |
| ok_trade | 31 | 9 МБ | 1 |
| pm_depth | 31 | 7 МБ | 2 |
| pm_rtt | 31 | 222 КБ | 2 |
| pm_top | 31 | 15 МБ | 2 |
| pm_trades | 31 | 10 МБ | 2 |
| rtds | 31 | 2 МБ | 2 |
| windows | 31 | 64 КБ | 143 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 35, всего 293
- Polymarket CLOB: TCP 7, TLS 41, всего 79
- Polymarket gamma: TCP 5, TLS 40, всего 52

## Последние строки журнала записи
```
18:35:10 [cex] Binance 515 сд. задержка p50/p90=155.7/166.9 мс | Coinbase 152 задержка p50=87.8 мс | смещение часов +23.7 мс | lag loop p99/max=7.6/16.2 мс
18:35:10 [cex] binance_futures 820 сд. p50=162.5 мс | bybit 942 сд. p50=125.5 мс | okx 1129 сд. p50=933.4 мс | binance_futures_book 8974 сд. p50=148.6 мс | binance_futures_depth 98 сд. p50=148.0 мс | binance_liq 4 сд. p50=1130.8 мс | bybit_book 263 сд. p50=115.9 мс | bybit_liq 6 сд. p50=551.3 мс | kraken 73 сд. p50=80.9 мс | bitstamp 21 сд. p50=66.9 мс
18:35:18 [pm] T-282.0s Up 0.19/0.20 Down 0.80/0.81 ptb=82405.6 | CLOB 7848 сообщ., задержка p50/p90=630.9/774.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791570918015 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=2.3/3.1 мс
18:35:20 [cex] Binance 264 сд. задержка p50/p90=150.3/155.1 мс | Coinbase 55 задержка p50=83.9 мс | смещение часов +23.7 мс | lag loop p99/max=2.2/7.9 мс
18:35:20 [cex] binance_futures 216 сд. p50=153.5 мс | bybit 520 сд. p50=118.6 мс | okx 269 сд. p50=161.5 мс | binance_futures_book 6016 сд. p50=149.1 мс | binance_futures_depth 97 сд. p50=148.1 мс | binance_liq 3 сд. p50=1060.3 мс | bybit_book 294 сд. p50=115.9 мс | bybit_liq 2 сд. p50=615.4 мс | kraken 36 сд. p50=55.7 мс | bitstamp 14 сд. p50=55.2 мс
18:35:28 [pm] T-272.0s Up 0.15/0.16 Down 0.84/0.85 ptb=82405.6 | CLOB 5597 сообщ., задержка p50/p90=39.5/61.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791570928016 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=1.2/2.0 мс
18:35:30 [cex] Binance 22 сд. задержка p50/p90=148.7/149.5 мс | Coinbase 46 задержка p50=82.3 мс | смещение часов +23.7 мс | lag loop p99/max=2.0/2.1 мс
18:35:30 [cex] binance_futures 74 сд. p50=249.9 мс | bybit 70 сд. p50=117.7 мс | okx 29 сд. p50=160.7 мс | binance_futures_book 1338 сд. p50=148.3 мс | binance_futures_depth 96 сд. p50=148.1 мс | binance_liq 2 сд. p50=1156.2 мс | bybit_book 180 сд. p50=115.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 9 сд. p50=47.8 мс | bitstamp 2 сд. p50=53.0 мс
18:35:38 [pm] T-262.0s Up 0.15/0.16 Down 0.84/0.85 ptb=82405.6 | CLOB 3104 сообщ., задержка p50/p90=39.6/66.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791570938018 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=2.1/2.2 мс
18:35:40 [cex] Binance 15 сд. задержка p50/p90=147.9/148.8 мс | Coinbase 39 задержка p50=81.5 мс | смещение часов +23.7 мс | lag loop p99/max=2.2/2.3 мс
18:35:40 [cex] binance_futures 52 сд. p50=296.9 мс | bybit 62 сд. p50=117.9 мс | okx 34 сд. p50=160.7 мс | binance_futures_book 1099 сд. p50=148.2 мс | binance_futures_depth 97 сд. p50=148.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 125 сд. p50=115.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 23 сд. p50=45.5 мс | bitstamp 0 сд. p50=n/a мс
18:35:48 [pm] T-252.0s Up 0.13/0.14 Down 0.86/0.87 ptb=82405.6 | CLOB 2805 сообщ., задержка p50/p90=39.5/112.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791570948019 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=1.5/1.9 мс
18:35:50 [cex] Binance 20 сд. задержка p50/p90=147.9/149.0 мс | Coinbase 73 задержка p50=82.8 мс | смещение часов +23.7 мс | lag loop p99/max=2.1/3.6 мс
18:35:50 [cex] binance_futures 70 сд. p50=207.5 мс | bybit 63 сд. p50=118.0 мс | okx 24 сд. p50=160.4 мс | binance_futures_book 2078 сд. p50=149.9 мс | binance_futures_depth 95 сд. p50=148.2 мс | binance_liq 2 сд. p50=1159.0 мс | bybit_book 93 сд. p50=116.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=50.5 мс | bitstamp 3 сд. p50=50.4 мс
18:35:58 [pm] T-242.0s Up 0.11/0.12 Down 0.88/0.89 ptb=82405.6 | CLOB 5380 сообщ., задержка p50/p90=43.8/114.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791570958022 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=1.7/1.7 мс
```

Представлено версией кода: 7642f87; python 3.12.3
