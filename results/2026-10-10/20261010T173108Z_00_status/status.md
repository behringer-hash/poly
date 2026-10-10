# Состояние сервера записи

Время (UTC): 2026-10-10 17:31:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 10 hours, 7 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         708         978           2         427        1197
Swap:           2047          51        1996
```
- нагрузка CPU (1/5/15 мин): 0.17 / 0.37 / 0.30

## Данные
- файлов: 1386, всего 415 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 54 | 7 МБ | 1 |
| bn_book | 54 | 641 КБ | 107 |
| bnf_agg | 54 | 11 МБ | 1 |
| bnf_book | 54 | 271 МБ | 1 |
| bnf_depth5 | 54 | 22 МБ | 1 |
| bnf_liq | 47 | 31 КБ | 4012 |
| bs_trade | 54 | 797 КБ | 1 |
| by_book1 | 54 | 22 МБ | 1 |
| by_liq | 46 | 30 КБ | 5345 |
| by_trade | 54 | 7 МБ | 1 |
| cb_ticker | 54 | 6 МБ | 1 |
| clock | 54 | 42 КБ | 54 |
| clock_pm | 54 | 41 КБ | 2 |
| events | 51 | 18 КБ | 350 |
| events_pm | 54 | 23 КБ | 817 |
| health_cex | 54 | 574 КБ | 7 |
| health_feeds | 54 | 2 МБ | 7 |
| health_pm | 54 | 589 КБ | 8 |
| kr_trade | 54 | 2 МБ | 5 |
| ok_trade | 54 | 10 МБ | 3 |
| pm_depth | 54 | 11 МБ | 2 |
| pm_rtt | 54 | 371 КБ | 4 |
| pm_top | 54 | 22 МБ | 2 |
| pm_trades | 54 | 15 МБ | 2 |
| rtds | 54 | 4 МБ | 2 |
| windows | 54 | 111 КБ | 64 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 38, всего 290
- Polymarket CLOB: TCP 6, TLS 42, всего 88
- Polymarket gamma: TCP 5, TLS 37, всего 49

## Последние строки журнала записи
```
17:30:19 [pm] T-280.3s Up 0.48/0.49 Down 0.51/0.52 ptb=82976.3 | CLOB 3363 сообщ., задержка p50/p90=39.7/44.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791653419739 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.4 мс | lag loop p99/max=1.8/2.1 мс
17:30:20 [cex] Binance 22 сд. задержка p50/p90=145.7/145.9 мс | Coinbase 30 задержка p50=86.0 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.1 мс
17:30:20 [cex] binance_futures 17 сд. p50=293.3 мс | bybit 5 сд. p50=115.3 мс | okx 8 сд. p50=157.9 мс | binance_futures_book 535 сд. p50=145.9 мс | binance_futures_depth 83 сд. p50=146.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 42 сд. p50=113.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=42.9 мс | bitstamp 3 сд. p50=54.8 мс
17:30:29 [pm] T-270.3s Up 0.46/0.47 Down 0.53/0.54 ptb=82976.3 | CLOB 5056 сообщ., задержка p50/p90=41.5/94.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791653429740 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.4 мс | lag loop p99/max=2.1/2.1 мс
17:30:30 [cex] Binance 39 сд. задержка p50/p90=145.8/146.7 мс | Coinbase 19 задержка p50=83.7 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.1 мс
17:30:30 [cex] binance_futures 14 сд. p50=295.1 мс | bybit 4 сд. p50=115.9 мс | okx 7 сд. p50=160.2 мс | binance_futures_book 701 сд. p50=146.2 мс | binance_futures_depth 89 сд. p50=147.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 34 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=45.5 мс | bitstamp 8 сд. p50=53.6 мс
17:30:39 [pm] T-260.3s Up 0.46/0.47 Down 0.53/0.54 ptb=82976.3 | CLOB 1980 сообщ., задержка p50/p90=40.4/80.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791653439741 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.2 мс | lag loop p99/max=2.1/2.2 мс
17:30:40 [cex] Binance 30 сд. задержка p50/p90=145.8/146.7 мс | Coinbase 29 задержка p50=82.6 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.1 мс
17:30:40 [cex] binance_futures 23 сд. p50=295.1 мс | bybit 6 сд. p50=115.9 мс | okx 9 сд. p50=159.9 мс | binance_futures_book 654 сд. p50=146.3 мс | binance_futures_depth 85 сд. p50=147.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 39 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=44.8 мс | bitstamp 4 сд. p50=53.7 мс
17:30:49 [pm] T-250.3s Up 0.48/0.49 Down 0.51/0.52 ptb=82976.3 | CLOB 2572 сообщ., задержка p50/p90=39.9/49.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791653449743 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.2 мс | lag loop p99/max=1.7/1.9 мс
17:30:50 [cex] Binance 15 сд. задержка p50/p90=145.8/146.0 мс | Coinbase 21 задержка p50=83.1 мс | смещение часов +21.6 мс | lag loop p99/max=2.0/2.2 мс
17:30:50 [cex] binance_futures 15 сд. p50=295.0 мс | bybit 5 сд. p50=115.4 мс | okx 11 сд. p50=160.1 мс | binance_futures_book 653 сд. p50=146.3 мс | binance_futures_depth 88 сд. p50=147.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 34 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=44.9 мс | bitstamp 3 сд. p50=52.2 мс
17:30:59 [pm] T-240.3s Up 0.48/0.49 Down 0.51/0.52 ptb=82976.3 | CLOB 2554 сообщ., задержка p50/p90=40.1/51.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791653459744 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.4 мс | lag loop p99/max=1.4/2.1 мс
17:31:00 [cex] Binance 25 сд. задержка p50/p90=145.7/145.9 мс | Coinbase 18 задержка p50=83.7 мс | смещение часов +21.6 мс | lag loop p99/max=2.2/2.2 мс
17:31:00 [cex] binance_futures 13 сд. p50=295.1 мс | bybit 10 сд. p50=115.4 мс | okx 8 сд. p50=159.9 мс | binance_futures_book 948 сд. p50=146.3 мс | binance_futures_depth 90 сд. p50=147.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 56 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=42.9 мс | bitstamp 1 сд. p50=50.3 мс
```

Представлено версией кода: 69087ca; python 3.12.3
