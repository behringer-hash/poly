# Состояние сервера записи

Время (UTC): 2026-10-09 23:45:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 16 hours, 22 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         669         900           2         529        1236
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.28 / 0.15 / 0.13

## Данные
- файлов: 928, всего 366 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 36 | 6 МБ | 1 |
| bn_book | 36 | 598 КБ | 1 |
| bnf_agg | 36 | 9 МБ | 1 |
| bnf_book | 36 | 247 МБ | 1 |
| bnf_depth5 | 36 | 19 МБ | 1 |
| bnf_liq | 34 | 27 КБ | 8967 |
| bs_trade | 36 | 748 КБ | 1 |
| by_book1 | 36 | 19 МБ | 1 |
| by_liq | 33 | 28 КБ | 1611 |
| by_trade | 36 | 6 МБ | 1 |
| cb_ticker | 36 | 5 МБ | 1 |
| clock | 36 | 28 КБ | 25 |
| clock_pm | 36 | 28 КБ | 40 |
| events | 33 | 12 КБ | 414 |
| events_pm | 36 | 17 КБ | 606 |
| health_cex | 36 | 396 КБ | 5 |
| health_feeds | 36 | 1 МБ | 5 |
| health_pm | 36 | 405 КБ | 6 |
| kr_trade | 36 | 1 МБ | 1 |
| ok_trade | 36 | 9 МБ | 1 |
| pm_depth | 36 | 9 МБ | 0 |
| pm_rtt | 36 | 262 КБ | 0 |
| pm_top | 36 | 17 МБ | 0 |
| pm_trades | 36 | 11 МБ | 0 |
| rtds | 36 | 3 МБ | 0 |
| windows | 36 | 75 КБ | 114 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 40, всего 288
- Polymarket CLOB: TCP 6, TLS 40, всего 83
- Polymarket gamma: TCP 5, TLS 46, всего 58

## Последние строки журнала записи
```
23:45:10 [pm] T-289.3s Up 0.66/0.67 Down 0.33/0.34 ptb=82559.1 | CLOB 3861 сообщ., задержка p50/p90=43.1/43.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791589510669 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=4.2/7.5 мс
23:45:13 [cex] Binance 22 сд. задержка p50/p90=142.9/143.5 мс | Coinbase 47 задержка p50=79.8 мс | смещение часов +20.7 мс | lag loop p99/max=2.0/2.1 мс
23:45:13 [cex] binance_futures 27 сд. p50=289.7 мс | bybit 30 сд. p50=114.3 мс | okx 23 сд. p50=153.0 мс | binance_futures_book 702 сд. p50=140.1 мс | binance_futures_depth 95 сд. p50=157.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 84 сд. p50=112.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=41.9 мс | bitstamp 0 сд. p50=n/a мс
23:45:20 [pm] T-279.3s Up 0.65/0.66 Down 0.34/0.35 ptb=82559.1 | CLOB 4171 сообщ., задержка p50/p90=41.5/43.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791589520671 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.9/1.9 мс
23:45:23 [cex] Binance 15 сд. задержка p50/p90=142.9/143.8 мс | Coinbase 36 задержка p50=79.0 мс | смещение часов +20.7 мс | lag loop p99/max=2.1/2.2 мс
23:45:23 [cex] binance_futures 26 сд. p50=290.9 мс | bybit 8 сд. p50=114.4 мс | okx 10 сд. p50=153.2 мс | binance_futures_book 680 сд. p50=140.0 мс | binance_futures_depth 91 сд. p50=157.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 36 сд. p50=112.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=39.2 мс | bitstamp 4 сд. p50=51.2 мс
23:45:30 [pm] T-269.3s Up 0.77/0.78 Down 0.22/0.23 ptb=82559.1 | CLOB 4738 сообщ., задержка p50/p90=41.1/42.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791589530673 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.0/2.1 мс
23:45:33 [cex] Binance 14 сд. задержка p50/p90=142.9/143.4 мс | Coinbase 48 задержка p50=78.9 мс | смещение часов +19.8 мс | lag loop p99/max=2.2/2.2 мс
23:45:33 [cex] binance_futures 20 сд. p50=291.0 мс | bybit 2 сд. p50=115.0 мс | okx 25 сд. p50=152.8 мс | binance_futures_book 490 сд. p50=140.0 мс | binance_futures_depth 89 сд. p50=157.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 73 сд. p50=112.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=44.1 мс | bitstamp 2 сд. p50=52.0 мс
23:45:40 [pm] T-259.3s Up 0.86/0.87 Down 0.13/0.14 ptb=82559.1 | CLOB 4225 сообщ., задержка p50/p90=41.1/43.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791589540674 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.4/2.6 мс
23:45:43 [cex] Binance 94 сд. задержка p50/p90=143.2/145.2 мс | Coinbase 56 задержка p50=78.5 мс | смещение часов +19.8 мс | lag loop p99/max=2.8/5.2 мс
23:45:43 [cex] binance_futures 80 сд. p50=148.4 мс | bybit 124 сд. p50=116.3 мс | okx 96 сд. p50=152.3 мс | binance_futures_book 2549 сд. p50=139.9 мс | binance_futures_depth 92 сд. p50=156.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 51 сд. p50=111.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 18 сд. p50=63.3 мс | bitstamp 4 сд. p50=51.6 мс
23:45:50 [pm] T-249.3s Up 0.86/0.87 Down 0.13/0.14 ptb=82559.1 | CLOB 1747 сообщ., задержка p50/p90=41.1/41.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791589550676 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.9/1.9 мс
23:45:53 [cex] Binance 14 сд. задержка p50/p90=142.0/142.2 мс | Coinbase 18 задержка p50=77.7 мс | смещение часов +19.8 мс | lag loop p99/max=2.0/2.2 мс
23:45:53 [cex] binance_futures 23 сд. p50=290.1 мс | bybit 16 сд. p50=113.3 мс | okx 17 сд. p50=152.0 мс | binance_futures_book 554 сд. p50=139.1 мс | binance_futures_depth 89 сд. p50=156.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 51 сд. p50=111.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=40.8 мс | bitstamp 3 сд. p50=71.2 мс
```

Представлено версией кода: 7642f87; python 3.12.3
