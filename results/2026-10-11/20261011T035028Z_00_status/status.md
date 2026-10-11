# Состояние сервера записи

Время (UTC): 2026-10-11 03:50:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 20 hours, 26 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         700         899           2         522        1205
Swap:           2047          56        1991
```
- нагрузка CPU (1/5/15 мин): 0.17 / 0.14 / 0.10

## Данные
- файлов: 1640, всего 464 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 64 | 8 МБ | 1 |
| bn_book | 64 | 673 КБ | 5 |
| bnf_agg | 64 | 12 МБ | 1 |
| bnf_book | 64 | 299 МБ | 1 |
| bnf_depth5 | 64 | 26 МБ | 1 |
| bnf_liq | 53 | 32 КБ | 13 |
| bs_trade | 64 | 871 КБ | 5 |
| by_book1 | 64 | 25 МБ | 1 |
| by_liq | 54 | 31 КБ | 1660 |
| by_trade | 64 | 8 МБ | 1 |
| cb_ticker | 64 | 7 МБ | 1 |
| clock | 64 | 50 КБ | 25 |
| clock_pm | 64 | 50 КБ | 43 |
| events | 61 | 22 КБ | 652 |
| events_pm | 64 | 26 КБ | 558 |
| health_cex | 64 | 685 КБ | 1 |
| health_feeds | 64 | 2 МБ | 1 |
| health_pm | 64 | 705 КБ | 2 |
| kr_trade | 64 | 2 МБ | 3 |
| ok_trade | 64 | 10 МБ | 1 |
| pm_depth | 64 | 13 МБ | 0 |
| pm_rtt | 64 | 451 КБ | 4 |
| pm_top | 64 | 26 МБ | 0 |
| pm_trades | 64 | 18 МБ | 0 |
| rtds | 64 | 4 МБ | 0 |
| windows | 64 | 134 КБ | 53 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 38, всего 286
- Polymarket CLOB: TCP 5, TLS 38, всего 77
- Polymarket gamma: TCP 5, TLS 42, всего 53

## Последние строки журнала записи
```
03:49:45 [cex] Binance 12 сд. задержка p50/p90=142.4/143.4 мс | Coinbase 19 задержка p50=81.1 мс | смещение часов +18.5 мс | lag loop p99/max=2.0/2.1 мс
03:49:45 [cex] binance_futures 21 сд. p50=292.1 мс | bybit 39 сд. p50=113.1 мс | okx 28 сд. p50=152.5 мс | binance_futures_book 473 сд. p50=143.2 мс | binance_futures_depth 87 сд. p50=144.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 58 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=38.9 мс | bitstamp 2 сд. p50=44.4 мс
03:49:45 [pm] окно btc-updown-5m-1791690600 (2026-10-11 03:50:00 UTC): Bitcoin Up or Down - October 10, 11:50PM-11:55PM ET
03:49:55 [pm] T-  4.9s Up n/a/0.01 Down 0.99/n/a ptb=82899.2 | CLOB 1036 сообщ., задержка p50/p90=37.5/39.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791690595057 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.1/12.6 мс
03:49:55 [cex] Binance 15 сд. задержка p50/p90=142.4/143.4 мс | Coinbase 12 задержка p50=79.8 мс | смещение часов +18.5 мс | lag loop p99/max=2.0/2.2 мс
03:49:55 [cex] binance_futures 22 сд. p50=291.9 мс | bybit 8 сд. p50=112.2 мс | okx 13 сд. p50=152.0 мс | binance_futures_book 418 сд. p50=143.1 мс | binance_futures_depth 87 сд. p50=144.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 38 сд. p50=110.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 0 сд. p50=n/a мс | bitstamp 1 сд. p50=43.9 мс
03:50:05 [pm] T-294.9s Up 0.41/0.42 Down 0.58/0.59 ptb=82842.9 | CLOB 3052 сообщ., задержка p50/p90=36.5/47.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791690605058 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=3.8/7.2 мс
03:50:05 [cex] Binance 15 сд. задержка p50/p90=142.7/143.9 мс | Coinbase 32 задержка p50=79.9 мс | смещение часов +17.8 мс | lag loop p99/max=2.2/2.2 мс
03:50:05 [cex] binance_futures 19 сд. p50=291.9 мс | bybit 26 сд. p50=113.4 мс | okx 61 сд. p50=156.6 мс | binance_futures_book 709 сд. p50=143.1 мс | binance_futures_depth 88 сд. p50=144.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 61 сд. p50=110.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=40.7 мс | bitstamp 2 сд. p50=49.4 мс
03:50:15 [pm] T-284.9s Up 0.16/0.17 Down 0.83/0.84 ptb=82842.9 | CLOB 7383 сообщ., задержка p50/p90=38.1/49.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791690615059 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=3.8/4.6 мс
03:50:15 [cex] Binance 104 сд. задержка p50/p90=141.8/142.7 мс | Coinbase 46 задержка p50=80.1 мс | смещение часов +17.8 мс | lag loop p99/max=4.3/8.2 мс
03:50:15 [cex] binance_futures 122 сд. p50=145.6 мс | bybit 247 сд. p50=112.2 мс | okx 105 сд. p50=153.3 мс | binance_futures_book 6463 сд. p50=143.6 мс | binance_futures_depth 97 сд. p50=143.9 мс | binance_liq 1 сд. p50=1151.8 мс | bybit_book 206 сд. p50=109.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 19 сд. p50=49.0 мс | bitstamp 33 сд. p50=50.4 мс
03:50:25 [pm] T-274.9s Up 0.16/0.17 Down 0.83/0.84 ptb=82842.9 | CLOB 5348 сообщ., задержка p50/p90=36.9/44.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791690625061 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=1.7/1.9 мс
03:50:25 [cex] Binance 54 сд. задержка p50/p90=141.6/142.8 мс | Coinbase 6 задержка p50=79.6 мс | смещение часов +17.8 мс | lag loop p99/max=2.2/3.5 мс
03:50:25 [cex] binance_futures 39 сд. p50=291.1 мс | bybit 75 сд. p50=112.1 мс | okx 37 сд. p50=151.6 мс | binance_futures_book 1601 сд. p50=142.9 мс | binance_futures_depth 92 сд. p50=144.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 141 сд. p50=109.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 17 сд. p50=48.5 мс | bitstamp 14 сд. p50=51.3 мс
```

Представлено версией кода: 69087ca; python 3.12.3
