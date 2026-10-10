# Состояние сервера записи

Время (UTC): 2026-10-10 03:54:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 20 hours, 30 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         669         914           2         514        1236
Swap:           2047          21        2026
```
- нагрузка CPU (1/5/15 мин): 0.09 / 0.12 / 0.09

## Данные
- файлов: 1030, всего 377 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 40 | 6 МБ | 1 |
| bn_book | 40 | 605 КБ | 176 |
| bnf_agg | 40 | 10 МБ | 1 |
| bnf_book | 40 | 251 МБ | 1 |
| bnf_depth5 | 40 | 20 МБ | 1 |
| bnf_liq | 37 | 28 КБ | 5405 |
| bs_trade | 40 | 713 КБ | 1 |
| by_book1 | 40 | 20 МБ | 1 |
| by_liq | 36 | 28 КБ | 2924 |
| by_trade | 40 | 7 МБ | 1 |
| cb_ticker | 40 | 6 МБ | 3 |
| clock | 40 | 32 КБ | 17 |
| clock_pm | 40 | 32 КБ | 33 |
| events | 37 | 14 КБ | 517 |
| events_pm | 40 | 19 КБ | 823 |
| health_cex | 40 | 441 КБ | 3 |
| health_feeds | 40 | 2 МБ | 3 |
| health_pm | 40 | 452 КБ | 4 |
| kr_trade | 40 | 1 МБ | 5 |
| ok_trade | 40 | 9 МБ | 1 |
| pm_depth | 40 | 10 МБ | 2 |
| pm_rtt | 40 | 294 КБ | 4 |
| pm_top | 40 | 18 МБ | 2 |
| pm_trades | 40 | 12 МБ | 2 |
| rtds | 40 | 3 МБ | 2 |
| windows | 40 | 85 КБ | 43 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 35, всего 284
- Polymarket CLOB: TCP 5, TLS 38, всего 77
- Polymarket gamma: TCP 5, TLS 35, всего 46

## Последние строки журнала записи
```
03:54:04 [cex] Binance 11 сд. задержка p50/p90=154.8/155.8 мс | Coinbase 15 задержка p50=85.3 мс | смещение часов +21.5 мс | lag loop p99/max=2.3/2.8 мс
03:54:04 [cex] binance_futures 17 сд. p50=290.0 мс | bybit 2 сд. p50=115.5 мс | okx 19 сд. p50=153.0 мс | binance_futures_book 477 сд. p50=144.6 мс | binance_futures_depth 77 сд. p50=147.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 71 сд. p50=113.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 0 сд. p50=n/a мс | bitstamp 2 сд. p50=49.9 мс
03:54:12 [pm] T- 47.2s Up 0.01/0.02 Down 0.98/0.99 ptb=82514.7 | CLOB 1722 сообщ., задержка p50/p90=40.6/42.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791604452825 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.1/2.2 мс
03:54:14 [cex] Binance 11 сд. задержка p50/p90=155.0/155.8 мс | Coinbase 11 задержка p50=84.6 мс | смещение часов +21.5 мс | lag loop p99/max=2.2/2.2 мс
03:54:14 [cex] binance_futures 11 сд. p50=290.2 мс | bybit 2 сд. p50=115.3 мс | okx 10 сд. p50=153.1 мс | binance_futures_book 157 сд. p50=144.1 мс | binance_futures_depth 62 сд. p50=147.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 59 сд. p50=113.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=43.1 мс | bitstamp 0 сд. p50=n/a мс
03:54:22 [pm] T- 37.2s Up n/a/0.01 Down 0.99/n/a ptb=82514.7 | CLOB 994 сообщ., задержка p50/p90=40.6/44.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791604462825 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.1/2.4 мс
03:54:24 [cex] Binance 22 сд. задержка p50/p90=154.8/155.1 мс | Coinbase 29 задержка p50=81.5 мс | смещение часов +21.5 мс | lag loop p99/max=2.2/2.2 мс
03:54:24 [cex] binance_futures 10 сд. p50=290.1 мс | bybit 6 сд. p50=115.3 мс | okx 14 сд. p50=152.8 мс | binance_futures_book 191 сд. p50=144.2 мс | binance_futures_depth 70 сд. p50=147.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 67 сд. p50=113.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=39.4 мс | bitstamp 1 сд. p50=52.3 мс
03:54:32 [pm] T- 27.2s Up n/a/0.01 Down 0.99/n/a ptb=82514.7 | CLOB 582 сообщ., задержка p50/p90=40.6/43.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791604472826 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.0/2.2 мс
03:54:34 [cex] Binance 8 сд. задержка p50/p90=152.5/154.8 мс | Coinbase 35 задержка p50=79.6 мс | смещение часов +19.1 мс | lag loop p99/max=2.2/2.3 мс
03:54:34 [cex] binance_futures 7 сд. p50=288.2 мс | bybit 7 сд. p50=112.9 мс | okx 17 сд. p50=152.1 мс | binance_futures_book 187 сд. p50=143.5 мс | binance_futures_depth 83 сд. p50=146.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 60 сд. p50=111.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=36.7 мс | bitstamp 0 сд. p50=n/a мс
03:54:42 [pm] T- 17.2s Up n/a/0.01 Down 0.99/n/a ptb=82514.7 | CLOB 569 сообщ., задержка p50/p90=40.5/43.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791604482827 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.0/2.2 мс
03:54:44 [cex] Binance 9 сд. задержка p50/p90=152.5/152.6 мс | Coinbase 14 задержка p50=79.7 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.2 мс
03:54:44 [cex] binance_futures 8 сд. p50=287.6 мс | bybit 2 сд. p50=113.4 мс | okx 14 сд. p50=150.5 мс | binance_futures_book 171 сд. p50=141.9 мс | binance_futures_depth 73 сд. p50=145.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 61 сд. p50=111.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=41.2 мс | bitstamp 3 сд. p50=45.4 мс
03:54:45 [pm] окно btc-updown-5m-1791604500 (2026-10-10 03:55:00 UTC): Bitcoin Up or Down - October 9, 11:55PM-12:00AM ET
```

Представлено версией кода: 7642f87; python 3.12.3
