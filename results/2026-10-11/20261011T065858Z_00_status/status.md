# Состояние сервера записи

Время (UTC): 2026-10-11 06:58:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 23 hours, 35 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         706         850           2         557        1199
Swap:           2047          61        1986
```
- нагрузка CPU (1/5/15 мин): 0.23 / 0.16 / 0.10

## Данные
- файлов: 1718, всего 467 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 67 | 8 МБ | 1 |
| bn_book | 67 | 674 КБ | 120 |
| bnf_agg | 67 | 12 МБ | 1 |
| bnf_book | 67 | 295 МБ | 1 |
| bnf_depth5 | 67 | 28 МБ | 1 |
| bnf_liq | 56 | 34 КБ | 721 |
| bs_trade | 67 | 884 КБ | 3 |
| by_book1 | 67 | 25 МБ | 1 |
| by_liq | 57 | 32 КБ | 723 |
| by_trade | 67 | 8 МБ | 1 |
| cb_ticker | 67 | 7 МБ | 1 |
| clock | 67 | 52 КБ | 21 |
| clock_pm | 67 | 52 КБ | 40 |
| events | 64 | 24 КБ | 110 |
| events_pm | 67 | 26 КБ | 2667 |
| health_cex | 67 | 720 КБ | 1 |
| health_feeds | 67 | 3 МБ | 1 |
| health_pm | 67 | 740 КБ | 10 |
| kr_trade | 67 | 2 МБ | 1 |
| ok_trade | 67 | 11 МБ | 1 |
| pm_depth | 67 | 14 МБ | 2 |
| pm_rtt | 67 | 477 КБ | 2 |
| pm_top | 67 | 27 МБ | 2 |
| pm_trades | 67 | 19 МБ | 2 |
| rtds | 67 | 5 МБ | 2 |
| windows | 67 | 140 КБ | 384 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 36, всего 285
- Polymarket CLOB: TCP 6, TLS 40, всего 85
- Polymarket gamma: TCP 5, TLS 37, всего 48

## Последние строки журнала записи
```
06:58:16 [pm] T-103.3s Up 0.96/0.97 Down 0.03/0.04 ptb=83065.5 | CLOB 1146 сообщ., задержка p50/p90=36.5/38.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791701896671 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=2.2/2.2 мс
06:58:16 [cex] Binance 16 сд. задержка p50/p90=143.2/144.0 мс | Coinbase 12 задержка p50=83.6 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.3 мс
06:58:16 [cex] binance_futures 23 сд. p50=292.8 мс | bybit 10 сд. p50=113.3 мс | okx 9 сд. p50=152.6 мс | binance_futures_book 195 сд. p50=143.8 мс | binance_futures_depth 73 сд. p50=144.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 90 сд. p50=111.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=43.0 мс | bitstamp 0 сд. p50=n/a мс
06:58:26 [pm] T- 93.3s Up 0.94/0.95 Down 0.05/0.06 ptb=83065.5 | CLOB 3236 сообщ., задержка p50/p90=36.2/42.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791701906673 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=2.1/5.6 мс
06:58:26 [cex] Binance 18 сд. задержка p50/p90=143.0/144.0 мс | Coinbase 12 задержка p50=83.1 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.2 мс
06:58:26 [cex] binance_futures 51 сд. p50=223.6 мс | bybit 118 сд. p50=118.2 мс | okx 16 сд. p50=153.1 мс | binance_futures_book 1920 сд. p50=147.6 мс | binance_futures_depth 79 сд. p50=144.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 88 сд. p50=111.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=57.3 мс | bitstamp 0 сд. p50=n/a мс
06:58:36 [pm] T- 83.3s Up 0.95/0.96 Down 0.04/0.05 ptb=83065.5 | CLOB 1692 сообщ., задержка p50/p90=36.1/38.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791701916674 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=1.8/1.8 мс
06:58:36 [cex] Binance 13 сд. задержка p50/p90=143.0/144.1 мс | Coinbase 4 задержка p50=83.2 мс | смещение часов +19.8 мс | lag loop p99/max=2.2/2.2 мс
06:58:36 [cex] binance_futures 32 сд. p50=292.7 мс | bybit 21 сд. p50=113.5 мс | okx 11 сд. p50=153.0 мс | binance_futures_book 469 сд. p50=143.9 мс | binance_futures_depth 81 сд. p50=144.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 42 сд. p50=111.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=39.9 мс | bitstamp 0 сд. p50=n/a мс
06:58:46 [pm] T- 73.3s Up 0.97/0.98 Down 0.02/0.03 ptb=83065.5 | CLOB 2464 сообщ., задержка p50/p90=36.4/41.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791701926676 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=2.0/2.2 мс
06:58:46 [cex] Binance 18 сд. задержка p50/p90=143.6/143.8 мс | Coinbase 11 задержка p50=84.2 мс | смещение часов +19.8 мс | lag loop p99/max=2.0/2.1 мс
06:58:46 [cex] binance_futures 28 сд. p50=293.1 мс | bybit 36 сд. p50=114.2 мс | okx 13 сд. p50=154.0 мс | binance_futures_book 1252 сд. p50=144.6 мс | binance_futures_depth 82 сд. p50=145.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 55 сд. p50=111.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 13 сд. p50=40.4 мс | bitstamp 2 сд. p50=49.5 мс
06:58:56 [pm] T- 63.3s Up 0.98/0.99 Down 0.01/0.02 ptb=83065.5 | CLOB 1272 сообщ., задержка p50/p90=36.0/38.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791701936677 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=2.0/2.0 мс
06:58:56 [cex] Binance 15 сд. задержка p50/p90=143.6/144.6 мс | Coinbase 13 задержка p50=84.1 мс | смещение часов +19.8 мс | lag loop p99/max=2.1/2.2 мс
06:58:56 [cex] binance_futures 22 сд. p50=293.1 мс | bybit 7 сд. p50=113.8 мс | okx 16 сд. p50=153.5 мс | binance_futures_book 620 сд. p50=144.4 мс | binance_futures_depth 83 сд. p50=145.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 62 сд. p50=111.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=42.7 мс | bitstamp 2 сд. p50=46.4 мс
```

Представлено версией кода: 69087ca; python 3.12.3
