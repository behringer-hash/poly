# Состояние сервера записи

Время (UTC): 2026-10-09 21:42:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 14 hours, 18 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         662         921           2         516        1243
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.14 / 0.13 / 0.10

## Данные
- файлов: 878, всего 356 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 34 | 6 МБ | 1 |
| bn_book | 34 | 588 КБ | 7 |
| bnf_agg | 34 | 9 МБ | 1 |
| bnf_book | 34 | 242 МБ | 1 |
| bnf_depth5 | 34 | 18 МБ | 1 |
| bnf_liq | 34 | 27 КБ | 1558 |
| bs_trade | 34 | 651 КБ | 7 |
| by_book1 | 34 | 19 МБ | 1 |
| by_liq | 31 | 27 КБ | 2092 |
| by_trade | 34 | 6 МБ | 1 |
| cb_ticker | 34 | 5 МБ | 1 |
| clock | 34 | 27 КБ | 53 |
| clock_pm | 34 | 27 КБ | 6 |
| events | 31 | 11 КБ | 337 |
| events_pm | 34 | 16 КБ | 84 |
| health_cex | 34 | 373 КБ | 5 |
| health_feeds | 34 | 1 МБ | 5 |
| health_pm | 34 | 382 КБ | 8 |
| kr_trade | 34 | 1 МБ | 9 |
| ok_trade | 34 | 9 МБ | 3 |
| pm_depth | 34 | 8 МБ | 2 |
| pm_rtt | 34 | 246 КБ | 4 |
| pm_top | 34 | 16 МБ | 2 |
| pm_trades | 34 | 11 МБ | 2 |
| rtds | 34 | 2 МБ | 2 |
| windows | 34 | 70 КБ | 383 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 38, всего 288
- Polymarket CLOB: TCP 6, TLS 40, всего 78
- Polymarket gamma: TCP 5, TLS 42, всего 58

## Последние строки журнала записи
```
21:41:39 [pm] T-200.4s Up 0.80/0.81 Down 0.19/0.20 ptb=82481.2 | CLOB 1933 сообщ., задержка p50/p90=40.5/45.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791582099597 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.3 мс | lag loop p99/max=2.0/2.1 мс
21:41:42 [cex] Binance 14 сд. задержка p50/p90=143.1/143.2 мс | Coinbase 44 задержка p50=76.8 мс | смещение часов +18.8 мс | lag loop p99/max=2.1/2.8 мс
21:41:42 [cex] binance_futures 11 сд. p50=292.2 мс | bybit 11 сд. p50=112.8 мс | okx 25 сд. p50=151.0 мс | binance_futures_book 291 сд. p50=143.1 мс | binance_futures_depth 85 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 103 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=42.3 мс | bitstamp 0 сд. p50=n/a мс
21:41:49 [pm] T-190.4s Up 0.82/0.83 Down 0.17/0.18 ptb=82481.2 | CLOB 2205 сообщ., задержка p50/p90=40.8/48.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791582109599 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.3 мс | lag loop p99/max=2.0/2.1 мс
21:41:52 [cex] Binance 16 сд. задержка p50/p90=142.9/143.1 мс | Coinbase 17 задержка p50=77.1 мс | смещение часов +18.8 мс | lag loop p99/max=2.2/2.2 мс
21:41:52 [cex] binance_futures 18 сд. p50=292.5 мс | bybit 3 сд. p50=112.5 мс | okx 21 сд. p50=150.9 мс | binance_futures_book 261 сд. p50=143.2 мс | binance_futures_depth 76 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 139 сд. p50=110.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=47.3 мс | bitstamp 1 сд. p50=44.1 мс
21:41:59 [pm] T-180.4s Up 0.83/0.84 Down 0.16/0.17 ptb=82481.2 | CLOB 1849 сообщ., задержка p50/p90=40.2/52.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791582119601 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.9 мс | lag loop p99/max=1.9/1.9 мс
21:42:02 [cex] Binance 20 сд. задержка p50/p90=142.9/143.9 мс | Coinbase 14 задержка p50=76.7 мс | смещение часов +18.8 мс | lag loop p99/max=2.5/3.1 мс
21:42:02 [cex] binance_futures 14 сд. p50=292.4 мс | bybit 6 сд. p50=112.6 мс | okx 25 сд. p50=151.2 мс | binance_futures_book 280 сд. p50=143.1 мс | binance_futures_depth 73 сд. p50=143.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 108 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=42.6 мс | bitstamp 1 сд. p50=43.7 мс
21:42:09 [pm] T-170.4s Up 0.61/0.62 Down 0.38/0.39 ptb=82481.2 | CLOB 6940 сообщ., задержка p50/p90=63.1/111.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791582129602 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.9 мс | lag loop p99/max=2.4/14.8 мс
21:42:12 [cex] Binance 36 сд. задержка p50/p90=143.0/147.5 мс | Coinbase 22 задержка p50=77.5 мс | смещение часов +18.8 мс | lag loop p99/max=2.2/3.0 мс
21:42:12 [cex] binance_futures 90 сд. p50=145.7 мс | bybit 61 сд. p50=114.9 мс | okx 21 сд. p50=151.5 мс | binance_futures_book 1913 сд. p50=143.8 мс | binance_futures_depth 88 сд. p50=143.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 199 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 15 сд. p50=44.3 мс | bitstamp 5 сд. p50=53.2 мс
21:42:19 [pm] T-160.4s Up 0.83/0.84 Down 0.16/0.17 ptb=82481.2 | CLOB 6085 сообщ., задержка p50/p90=66.8/121.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791582139604 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.0 мс | lag loop p99/max=2.0/2.6 мс
21:42:22 [cex] Binance 42 сд. задержка p50/p90=143.1/147.6 мс | Coinbase 34 задержка p50=76.7 мс | смещение часов +18.8 мс | lag loop p99/max=2.5/7.5 мс
21:42:22 [cex] binance_futures 66 сд. p50=147.1 мс | bybit 43 сд. p50=115.2 мс | okx 74 сд. p50=159.1 мс | binance_futures_book 2659 сд. p50=143.3 мс | binance_futures_depth 90 сд. p50=143.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 92 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=38.9 мс | bitstamp 8 сд. p50=50.2 мс
```

Представлено версией кода: 7642f87; python 3.12.3
