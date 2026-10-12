# Состояние сервера записи

Время (UTC): 2026-10-12 22:28:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 15 hours, 4 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         791         771           2         539        1114
Swap:           2047         108        1939
```
- нагрузка CPU (1/5/15 мин): 0.22 / 0.40 / 0.44

## Данные
- файлов: 2745, всего 792 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 107 | 12 МБ | 2 |
| bn_book | 107 | 1 МБ | 12 |
| bnf_agg | 107 | 19 МБ | 2 |
| bnf_book | 107 | 529 МБ | 0 |
| bnf_depth5 | 107 | 39 МБ | 2 |
| bnf_liq | 94 | 53 КБ | 264 |
| bs_trade | 107 | 1 МБ | 8 |
| by_book1 | 107 | 40 МБ | 2 |
| by_liq | 90 | 47 КБ | 438 |
| by_trade | 107 | 12 МБ | 4 |
| cb_ticker | 107 | 11 МБ | 2 |
| clock | 107 | 82 КБ | 6 |
| clock_pm | 107 | 82 КБ | 27 |
| events | 100 | 34 КБ | 1430 |
| events_pm | 107 | 42 КБ | 65 |
| health_cex | 107 | 1 МБ | 10 |
| health_feeds | 107 | 4 МБ | 10 |
| health_pm | 107 | 1 МБ | 1 |
| kr_trade | 107 | 3 МБ | 8 |
| ok_trade | 107 | 16 МБ | 2 |
| pm_depth | 107 | 21 МБ | 1 |
| pm_rtt | 107 | 722 КБ | 1 |
| pm_top | 107 | 42 МБ | 1 |
| pm_trades | 107 | 31 МБ | 1 |
| rtds | 107 | 7 МБ | 1 |
| windows | 107 | 220 КБ | 334 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 7, TLS 43, всего 781
- Polymarket CLOB: TCP 5, TLS 48, всего 92
- Polymarket gamma: TCP 5, TLS 42, всего 55

## Последние строки журнала записи
```
22:27:57 [pm] T-122.5s Up 0.17/0.18 Down 0.82/0.83 ptb=82518.4 | CLOB 6272 сообщ., задержка p50/p90=56.4/160.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791844077511 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.2/1.9 мс
22:27:58 [cex] Binance 26 сд. задержка p50/p90=146.4/149.1 мс | Coinbase 54 задержка p50=84.8 мс | смещение часов +22.3 мс | lag loop p99/max=2.2/3.4 мс
22:27:58 [cex] binance_futures 36 сд. p50=198.2 мс | bybit 112 сд. p50=116.8 мс | okx 73 сд. p50=150.7 мс | binance_futures_book 1614 сд. p50=147.1 мс | binance_futures_depth 96 сд. p50=147.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 101 сд. p50=113.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=43.9 мс | bitstamp 12 сд. p50=49.1 мс
22:28:07 [pm] T-112.5s Up 0.27/0.28 Down 0.72/0.73 ptb=82518.4 | CLOB 9144 сообщ., задержка p50/p90=43.9/51.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791844087513 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.6/9.3 мс
22:28:08 [cex] Binance 52 сд. задержка p50/p90=146.5/152.4 мс | Coinbase 58 задержка p50=84.5 мс | смещение часов +22.3 мс | lag loop p99/max=2.1/3.9 мс
22:28:08 [cex] binance_futures 56 сд. p50=153.3 мс | bybit 63 сд. p50=115.8 мс | okx 79 сд. p50=150.6 мс | binance_futures_book 3326 сд. p50=147.1 мс | binance_futures_depth 96 сд. p50=147.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 143 сд. p50=113.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 20 сд. p50=46.8 мс | bitstamp 9 сд. p50=49.1 мс
22:28:17 [pm] T-102.5s Up 0.28/0.29 Down 0.71/0.72 ptb=82518.4 | CLOB 9637 сообщ., задержка p50/p90=56.7/127.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791844097514 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.1/2.2 мс
22:28:18 [cex] Binance 49 сд. задержка p50/p90=147.2/152.3 мс | Coinbase 36 задержка p50=84.1 мс | смещение часов +22.3 мс | lag loop p99/max=8.2/10.4 мс
22:28:18 [cex] binance_futures 69 сд. p50=156.4 мс | bybit 91 сд. p50=122.9 мс | okx 53 сд. p50=151.3 мс | binance_futures_book 3345 сд. p50=147.2 мс | binance_futures_depth 95 сд. p50=147.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 120 сд. p50=113.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=46.8 мс | bitstamp 13 сд. p50=48.5 мс
22:28:27 [pm] T- 92.5s Up 0.07/0.08 Down 0.92/0.93 ptb=82518.4 | CLOB 7571 сообщ., задержка p50/p90=44.2/55.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791844107516 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=5.0/5.8 мс
22:28:28 [cex] Binance 109 сд. задержка p50/p90=150.3/157.4 мс | Coinbase 59 задержка p50=86.5 мс | смещение часов +22.3 мс | lag loop p99/max=6.2/8.6 мс
22:28:28 [cex] binance_futures 141 сд. p50=150.8 мс | bybit 189 сд. p50=122.5 мс | okx 150 сд. p50=154.7 мс | binance_futures_book 5562 сд. p50=147.2 мс | binance_futures_depth 94 сд. p50=147.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 214 сд. p50=113.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 15 сд. p50=55.9 мс | bitstamp 12 сд. p50=54.5 мс
22:28:37 [pm] T- 82.5s Up 0.04/0.05 Down 0.95/0.96 ptb=82518.4 | CLOB 3860 сообщ., задержка p50/p90=44.0/46.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791844117517 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.2/1.3 мс
22:28:38 [cex] Binance 21 сд. задержка p50/p90=143.8/144.6 мс | Coinbase 44 задержка p50=83.5 мс | смещение часов +19.8 мс | lag loop p99/max=2.0/2.2 мс
22:28:38 [cex] binance_futures 31 сд. p50=293.5 мс | bybit 86 сд. p50=114.4 мс | okx 22 сд. p50=147.8 мс | binance_futures_book 1650 сд. p50=144.7 мс | binance_futures_depth 90 сд. p50=145.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 204 сд. p50=111.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=48.0 мс | bitstamp 4 сд. p50=49.9 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
