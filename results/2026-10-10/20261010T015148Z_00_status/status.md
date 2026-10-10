# Состояние сервера записи

Время (UTC): 2026-10-10 01:51:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 18 hours, 27 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         664         919           2         515        1241
Swap:           2047          22        2025
```
- нагрузка CPU (1/5/15 мин): 0.31 / 0.16 / 0.14

## Данные
- файлов: 979, всего 388 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 38 | 6 МБ | 1 |
| bn_book | 38 | 610 КБ | 68 |
| bnf_agg | 38 | 10 МБ | 1 |
| bnf_book | 38 | 264 МБ | 1 |
| bnf_depth5 | 38 | 20 МБ | 1 |
| bnf_liq | 36 | 29 КБ | 18 |
| bs_trade | 38 | 713 КБ | 1 |
| by_book1 | 38 | 20 МБ | 1 |
| by_liq | 34 | 28 КБ | 103 |
| by_trade | 38 | 7 МБ | 1 |
| cb_ticker | 38 | 6 МБ | 1 |
| clock | 38 | 30 КБ | 11 |
| clock_pm | 38 | 30 КБ | 28 |
| events | 35 | 12 КБ | 1971 |
| events_pm | 38 | 19 КБ | 109 |
| health_cex | 38 | 419 КБ | 3 |
| health_feeds | 38 | 2 МБ | 3 |
| health_pm | 38 | 429 КБ | 6 |
| kr_trade | 38 | 1 МБ | 1 |
| ok_trade | 38 | 9 МБ | 1 |
| pm_depth | 38 | 9 МБ | 2 |
| pm_rtt | 38 | 279 КБ | 2 |
| pm_top | 38 | 18 МБ | 2 |
| pm_trades | 38 | 12 МБ | 2 |
| rtds | 38 | 3 МБ | 2 |
| windows | 38 | 80 КБ | 103 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 39, всего 287
- Polymarket CLOB: TCP 6, TLS 41, всего 83
- Polymarket gamma: TCP 5, TLS 51, всего 62

## Последние строки журнала записи
```
01:51:01 [pm] T-238.3s Up 0.30/0.31 Down 0.69/0.70 ptb=82647.4 | CLOB 3333 сообщ., задержка p50/p90=43.0/74.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791597061740 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.0/2.1 мс
01:51:04 [cex] Binance 17 сд. задержка p50/p90=143.7/144.8 мс | Coinbase 38 задержка p50=90.3 мс | смещение часов +18.6 мс | lag loop p99/max=2.1/2.1 мс
01:51:04 [cex] binance_futures 22 сд. p50=304.3 мс | bybit 34 сд. p50=112.4 мс | okx 35 сд. p50=151.3 мс | binance_futures_book 469 сд. p50=152.9 мс | binance_futures_depth 82 сд. p50=144.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 101 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=46.3 мс | bitstamp 1 сд. p50=44.0 мс
01:51:11 [pm] T-228.3s Up 0.42/0.43 Down 0.57/0.58 ptb=82647.4 | CLOB 5989 сообщ., задержка p50/p90=41.9/54.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791597071742 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=1.9/2.1 мс
01:51:14 [cex] Binance 44 сд. задержка p50/p90=143.7/144.5 мс | Coinbase 35 задержка p50=82.4 мс | смещение часов +18.6 мс | lag loop p99/max=2.0/2.1 мс
01:51:14 [cex] binance_futures 41 сд. p50=161.8 мс | bybit 101 сд. p50=113.8 мс | okx 31 сд. p50=152.5 мс | binance_futures_book 1315 сд. p50=153.5 мс | binance_futures_depth 87 сд. p50=144.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 99 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=41.7 мс | bitstamp 4 сд. p50=55.2 мс
01:51:21 [pm] T-218.3s Up 0.37/0.38 Down 0.62/0.63 ptb=82647.4 | CLOB 4499 сообщ., задержка p50/p90=39.7/42.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791597081743 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.0/2.1 мс
01:51:24 [cex] Binance 14 сд. задержка p50/p90=143.7/144.5 мс | Coinbase 15 задержка p50=82.4 мс | смещение часов +18.6 мс | lag loop p99/max=2.1/2.2 мс
01:51:24 [cex] binance_futures 27 сд. p50=304.3 мс | bybit 9 сд. p50=112.0 мс | okx 19 сд. p50=151.4 мс | binance_futures_book 399 сд. p50=152.8 мс | binance_futures_depth 86 сд. p50=144.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 102 сд. p50=110.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 12 сд. p50=43.6 мс | bitstamp 0 сд. p50=n/a мс
01:51:31 [pm] T-208.3s Up 0.38/0.39 Down 0.61/0.62 ptb=82647.4 | CLOB 3532 сообщ., задержка p50/p90=34.6/40.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791597091744 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.1/2.1 мс
01:51:34 [cex] Binance 7 сд. задержка p50/p90=143.7/144.0 мс | Coinbase 16 задержка p50=86.5 мс | смещение часов +18.6 мс | lag loop p99/max=2.2/2.3 мс
01:51:34 [cex] binance_futures 49 сд. p50=183.1 мс | bybit 62 сд. p50=112.8 мс | okx 51 сд. p50=152.1 мс | binance_futures_book 1389 сд. p50=153.1 мс | binance_futures_depth 91 сд. p50=144.9 мс | binance_liq 2 сд. p50=1157.9 мс | bybit_book 139 сд. p50=110.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=38.2 мс | bitstamp 1 сд. p50=44.3 мс
01:51:41 [pm] T-198.3s Up 0.23/0.24 Down 0.76/0.77 ptb=82647.4 | CLOB 6702 сообщ., задержка p50/p90=37.3/58.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791597101746 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=2.1/5.0 мс
01:51:44 [cex] Binance 14 сд. задержка p50/p90=148.7/149.7 мс | Coinbase 25 задержка p50=87.4 мс | смещение часов +23.6 мс | lag loop p99/max=2.2/2.2 мс
01:51:44 [cex] binance_futures 23 сд. p50=305.3 мс | bybit 23 сд. p50=112.1 мс | okx 24 сд. p50=156.2 мс | binance_futures_book 1203 сд. p50=157.8 мс | binance_futures_depth 87 сд. p50=149.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 87 сд. p50=115.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 10 сд. p50=44.6 мс | bitstamp 2 сд. p50=62.4 мс
```

Представлено версией кода: 7642f87; python 3.12.3
