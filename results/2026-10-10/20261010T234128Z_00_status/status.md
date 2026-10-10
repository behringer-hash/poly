# Состояние сервера записи

Время (UTC): 2026-10-10 23:41:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 16 hours, 17 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         708         968           2         445        1197
Swap:           2047          56        1991
```
- нагрузка CPU (1/5/15 мин): 0.17 / 0.20 / 0.22

## Данные
- файлов: 1538, всего 434 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 60 | 7 МБ | 2 |
| bn_book | 60 | 653 КБ | 6 |
| bnf_agg | 60 | 11 МБ | 2 |
| bnf_book | 60 | 277 МБ | 2 |
| bnf_depth5 | 60 | 24 МБ | 2 |
| bnf_liq | 50 | 31 КБ | 7742 |
| bs_trade | 60 | 839 КБ | 4 |
| by_book1 | 60 | 24 МБ | 2 |
| by_liq | 51 | 31 КБ | 8644 |
| by_trade | 60 | 7 МБ | 6 |
| cb_ticker | 60 | 7 МБ | 2 |
| clock | 60 | 46 КБ | 22 |
| clock_pm | 60 | 46 КБ | 37 |
| events | 57 | 21 КБ | 409 |
| events_pm | 60 | 24 КБ | 884 |
| health_cex | 60 | 640 КБ | 4 |
| health_feeds | 60 | 2 МБ | 4 |
| health_pm | 60 | 658 КБ | 5 |
| kr_trade | 60 | 2 МБ | 22 |
| ok_trade | 60 | 10 МБ | 2 |
| pm_depth | 60 | 13 МБ | 1 |
| pm_rtt | 60 | 418 КБ | 3 |
| pm_top | 60 | 25 МБ | 1 |
| pm_trades | 60 | 17 МБ | 1 |
| rtds | 60 | 4 МБ | 1 |
| windows | 60 | 124 КБ | 264 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 44, всего 292
- Polymarket CLOB: TCP 5, TLS 38, всего 77
- Polymarket gamma: TCP 5, TLS 39, всего 49

## Последние строки журнала записи
```
23:40:42 [pm] T-257.0s Up 0.26/0.27 Down 0.73/0.74 ptb=82974.2 | CLOB 4627 сообщ., задержка p50/p90=37.4/38.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791675642986 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=2.1/2.1 мс
23:40:43 [cex] Binance 10 сд. задержка p50/p90=142.8/143.8 мс | Coinbase 22 задержка p50=80.4 мс | смещение часов +19.0 мс | lag loop p99/max=2.2/2.5 мс
23:40:43 [cex] binance_futures 5 сд. p50=292.0 мс | bybit 1 сд. p50=113.1 мс | okx 8 сд. p50=152.7 мс | binance_futures_book 253 сд. p50=143.1 мс | binance_futures_depth 78 сд. p50=144.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 128 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 10 сд. p50=40.5 мс | bitstamp 1 сд. p50=47.5 мс
23:40:52 [pm] T-247.0s Up 0.22/0.23 Down 0.77/0.78 ptb=82974.2 | CLOB 3072 сообщ., задержка p50/p90=37.6/38.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791675652987 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=2.0/2.1 мс
23:40:53 [cex] Binance 15 сд. задержка p50/p90=142.8/143.0 мс | Coinbase 35 задержка p50=81.0 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/2.1 мс
23:40:53 [cex] binance_futures 13 сд. p50=292.0 мс | bybit 21 сд. p50=113.1 мс | okx 37 сд. p50=153.9 мс | binance_futures_book 655 сд. p50=143.1 мс | binance_futures_depth 80 сд. p50=144.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 109 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=44.4 мс | bitstamp 1 сд. p50=44.2 мс
23:41:02 [pm] T-237.0s Up 0.30/0.31 Down 0.69/0.70 ptb=82974.2 | CLOB 5045 сообщ., задержка p50/p90=37.6/39.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791675662988 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=2.7/7.8 мс
23:41:03 [cex] Binance 7 сд. задержка p50/p90=143.0/144.0 мс | Coinbase 37 задержка p50=81.0 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/2.1 мс
23:41:03 [cex] binance_futures 50 сд. p50=143.3 мс | bybit 19 сд. p50=113.4 мс | okx 32 сд. p50=153.1 мс | binance_futures_book 806 сд. p50=143.3 мс | binance_futures_depth 76 сд. p50=144.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 95 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=39.2 мс | bitstamp 1 сд. p50=44.6 мс
23:41:12 [pm] T-227.0s Up 0.24/0.25 Down 0.75/0.76 ptb=82974.2 | CLOB 3535 сообщ., задержка p50/p90=37.5/38.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791675672990 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=1.5/1.6 мс
23:41:13 [cex] Binance 15 сд. задержка p50/p90=143.0/143.1 мс | Coinbase 8 задержка p50=80.9 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.1 мс
23:41:13 [cex] binance_futures 10 сд. p50=292.1 мс | bybit 8 сд. p50=113.3 мс | okx 5 сд. p50=152.9 мс | binance_futures_book 462 сд. p50=143.2 мс | binance_futures_depth 80 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 72 сд. p50=111.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=39.9 мс | bitstamp 0 сд. p50=n/a мс
23:41:22 [pm] T-217.0s Up 0.18/0.19 Down 0.81/0.82 ptb=82974.2 | CLOB 3322 сообщ., задержка p50/p90=37.6/41.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791675682991 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.9/2.3 мс
23:41:23 [cex] Binance 19 сд. задержка p50/p90=143.0/147.3 мс | Coinbase 31 задержка p50=81.4 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.2 мс
23:41:23 [cex] binance_futures 32 сд. p50=147.5 мс | bybit 42 сд. p50=116.4 мс | okx 8 сд. p50=152.8 мс | binance_futures_book 1496 сд. p50=143.7 мс | binance_futures_depth 79 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 77 сд. p50=111.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 0 сд. p50=n/a мс | bitstamp 2 сд. p50=46.7 мс
```

Представлено версией кода: 69087ca; python 3.12.3
