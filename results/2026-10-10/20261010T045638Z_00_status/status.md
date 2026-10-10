# Состояние сервера записи

Время (UTC): 2026-10-10 04:56:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 21 hours, 32 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         675         558           2         865        1230
Swap:           2047          21        2026
```
- нагрузка CPU (1/5/15 мин): 0.13 / 0.15 / 0.10

## Данные
- файлов: 1056, всего 390 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 41 | 6 МБ | 2 |
| bn_book | 41 | 611 КБ | 6 |
| bnf_agg | 41 | 10 МБ | 2 |
| bnf_book | 41 | 261 МБ | 1 |
| bnf_depth5 | 41 | 21 МБ | 2 |
| bnf_liq | 38 | 28 КБ | 964 |
| bs_trade | 41 | 728 КБ | 6 |
| by_book1 | 41 | 21 МБ | 2 |
| by_liq | 37 | 28 КБ | 152 |
| by_trade | 41 | 7 МБ | 2 |
| cb_ticker | 41 | 6 МБ | 4 |
| clock | 41 | 32 КБ | 41 |
| clock_pm | 41 | 32 КБ | 54 |
| events | 38 | 14 КБ | 353 |
| events_pm | 41 | 18 КБ | 1451 |
| health_cex | 41 | 452 КБ | 2 |
| health_feeds | 41 | 2 МБ | 2 |
| health_pm | 41 | 464 КБ | 3 |
| kr_trade | 41 | 1 МБ | 4 |
| ok_trade | 41 | 9 МБ | 2 |
| pm_depth | 41 | 10 МБ | 1 |
| pm_rtt | 41 | 302 КБ | 1 |
| pm_top | 41 | 19 МБ | 1 |
| pm_trades | 41 | 13 МБ | 1 |
| rtds | 41 | 3 МБ | 1 |
| windows | 41 | 87 КБ | 214 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 43, всего 292
- Polymarket CLOB: TCP 16, TLS 54, всего 97
- Polymarket gamma: TCP 5, TLS 40, всего 51

## Последние строки журнала записи
```
04:55:53 [pm] T-246.7s Up 0.36/0.37 Down 0.63/0.64 ptb=82632.3 | CLOB 4340 сообщ., задержка p50/p90=41.6/45.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791608153345 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=1.8/1.9 мс
04:55:55 [cex] Binance 12 сд. задержка p50/p90=146.5/146.8 мс | Coinbase 22 задержка p50=84.8 мс | смещение часов +21.8 мс | lag loop p99/max=2.1/2.3 мс
04:55:55 [cex] binance_futures 16 сд. p50=295.5 мс | bybit 7 сд. p50=115.9 мс | okx 13 сд. p50=153.2 мс | binance_futures_book 213 сд. p50=141.6 мс | binance_futures_depth 79 сд. p50=147.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 71 сд. p50=113.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=51.6 мс | bitstamp 2 сд. p50=47.6 мс
04:56:03 [pm] T-236.7s Up 0.37/0.38 Down 0.62/0.63 ptb=82632.3 | CLOB 3739 сообщ., задержка p50/p90=41.7/47.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791608163347 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.1/3.0 мс
04:56:05 [cex] Binance 16 сд. задержка p50/p90=143.0/144.2 мс | Coinbase 8 задержка p50=81.7 мс | смещение часов +18.3 мс | lag loop p99/max=2.1/2.2 мс
04:56:05 [cex] binance_futures 14 сд. p50=292.1 мс | bybit 18 сд. p50=112.5 мс | okx 19 сд. p50=149.8 мс | binance_futures_book 213 сд. p50=138.2 мс | binance_futures_depth 80 сд. p50=144.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 57 сд. p50=110.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=35.7 мс | bitstamp 1 сд. p50=47.4 мс
04:56:13 [pm] T-226.7s Up 0.40/0.41 Down 0.59/0.60 ptb=82632.3 | CLOB 4280 сообщ., задержка p50/p90=51.8/147.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791608173348 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.1/2.1 мс
04:56:15 [cex] Binance 16 сд. задержка p50/p90=143.1/144.1 мс | Coinbase 9 задержка p50=81.1 мс | смещение часов +18.3 мс | lag loop p99/max=2.2/2.2 мс
04:56:15 [cex] binance_futures 15 сд. p50=292.4 мс | bybit 1 сд. p50=112.5 мс | okx 6 сд. p50=149.8 мс | binance_futures_book 265 сд. p50=138.1 мс | binance_futures_depth 80 сд. p50=144.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 43 сд. p50=110.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=35.5 мс | bitstamp 0 сд. p50=n/a мс
04:56:23 [pm] T-216.7s Up 0.34/0.35 Down 0.65/0.66 ptb=82632.3 | CLOB 3285 сообщ., задержка p50/p90=41.5/44.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791608183349 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.9/2.0 мс
04:56:25 [cex] Binance 34 сд. задержка p50/p90=143.0/143.9 мс | Coinbase 8 задержка p50=81.4 мс | смещение часов +18.3 мс | lag loop p99/max=2.1/2.1 мс
04:56:25 [cex] binance_futures 11 сд. p50=291.9 мс | bybit 20 сд. p50=112.5 мс | okx 7 сд. p50=149.7 мс | binance_futures_book 256 сд. p50=138.1 мс | binance_futures_depth 74 сд. p50=143.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 63 сд. p50=110.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 0 сд. p50=n/a мс | bitstamp 2 сд. p50=45.5 мс
04:56:33 [pm] T-206.6s Up 0.15/0.16 Down 0.84/0.85 ptb=82632.3 | CLOB 2753 сообщ., задержка p50/p90=300.0/738.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791608193351 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/2.1 мс
04:56:35 [cex] Binance 36 сд. задержка p50/p90=143.1/145.0 мс | Coinbase 25 задержка p50=83.4 мс | смещение часов +18.3 мс | lag loop p99/max=2.2/2.7 мс
04:56:35 [cex] binance_futures 57 сд. p50=150.1 мс | bybit 111 сд. p50=114.6 мс | okx 65 сд. p50=150.9 мс | binance_futures_book 2037 сд. p50=139.2 мс | binance_futures_depth 81 сд. p50=143.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 153 сд. p50=110.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=37.8 мс | bitstamp 4 сд. p50=58.4 мс
```

Представлено версией кода: 7642f87; python 3.12.3
