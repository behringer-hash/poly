# Состояние сервера записи

Время (UTC): 2026-10-08 22:51:57

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 1 day, 15 hours, 28 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         660         640           2         800        1245
Swap:           2047           0        2047
```
- нагрузка CPU (1/5/15 мин): 0.15 / 0.15 / 0.16

## Данные
- файлов: 283, всего 228 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 11 | 3 МБ | 1 |
| bn_book | 11 | 329 КБ | 3 |
| bnf_agg | 11 | 6 МБ | 1 |
| bnf_book | 11 | 168 МБ | 0 |
| bnf_depth5 | 11 | 10 МБ | 1 |
| bnf_liq | 11 | 16 КБ | 2389 |
| bs_trade | 11 | 399 КБ | 1 |
| by_book1 | 11 | 11 МБ | 1 |
| by_liq | 11 | 20 КБ | 279 |
| by_trade | 11 | 4 МБ | 3 |
| cb_ticker | 11 | 3 МБ | 1 |
| clock | 11 | 9 КБ | 50 |
| clock_pm | 11 | 9 КБ | 48 |
| events | 8 | 3 КБ | 552 |
| events_pm | 11 | 9 КБ | 36 |
| health_cex | 11 | 131 КБ | 8 |
| health_feeds | 11 | 545 КБ | 8 |
| health_pm | 11 | 133 КБ | 10 |
| kr_trade | 11 | 743 КБ | 3 |
| ok_trade | 11 | 5 МБ | 1 |
| pm_depth | 11 | 4 МБ | 2 |
| pm_rtt | 11 | 100 КБ | 2 |
| pm_top | 11 | 8 МБ | 2 |
| pm_trades | 11 | 4 МБ | 2 |
| rtds | 11 | 1 МБ | 2 |
| windows | 11 | 25 КБ | 24 |

Дни с данными: 2026-10-08

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 289
- Polymarket CLOB: TCP 5, TLS 44, всего 81
- Polymarket gamma: TCP 5, TLS 43, всего 54

## Последние строки журнала записи
```
22:51:18 [pm] T-222.0s Up 0.18/0.19 Down 0.81/0.82 ptb=81865.5 | CLOB 4482 сообщ., задержка p50/p90=48.6/177.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791499878002 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=1.9/2.4 мс
22:51:19 [cex] Binance 13 сд. задержка p50/p90=142.8/143.8 мс | Coinbase 52 задержка p50=79.4 мс | смещение часов +18.6 мс | lag loop p99/max=4.7/7.1 мс
22:51:19 [cex] binance_futures 78 сд. p50=147.5 мс | bybit 141 сд. p50=113.9 мс | okx 49 сд. p50=150.2 мс | binance_futures_book 3063 сд. p50=143.8 мс | binance_futures_depth 93 сд. p50=143.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 139 сд. p50=110.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=42.1 мс | bitstamp 9 сд. p50=48.3 мс
22:51:21 [pm] RTDS[rtds_binance] разорван (ConnectionClosedOK(Close(code=1001, reason='Going away'), Close(code=1001, reason='Going away'), True)), переподключение через 2 с
22:51:23 [pm] RTDS[rtds_binance] подключён
22:51:28 [pm] T-212.0s Up 0.19/0.20 Down 0.80/0.81 ptb=81865.5 | CLOB 4329 сообщ., задержка p50/p90=41.7/94.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791499888003 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.1/52.5 мс
22:51:29 [cex] Binance 47 сд. задержка p50/p90=143.0/143.9 мс | Coinbase 58 задержка p50=79.8 мс | смещение часов +18.6 мс | lag loop p99/max=2.2/2.3 мс
22:51:29 [cex] binance_futures 51 сд. p50=247.8 мс | bybit 20 сд. p50=112.4 мс | okx 53 сд. p50=150.7 мс | binance_futures_book 2494 сд. p50=143.2 мс | binance_futures_depth 86 сд. p50=143.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 221 сд. p50=110.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 11 сд. p50=36.7 мс | bitstamp 4 сд. p50=45.5 мс
22:51:38 [pm] T-202.0s Up 0.13/0.14 Down 0.86/0.87 ptb=81865.5 | CLOB 4696 сообщ., задержка p50/p90=66.7/124.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791499898004 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.0/2.2 мс
22:51:39 [cex] Binance 10 сд. задержка p50/p90=142.7/144.0 мс | Coinbase 43 задержка p50=79.7 мс | смещение часов +18.6 мс | lag loop p99/max=2.1/2.1 мс
22:51:39 [cex] binance_futures 29 сд. p50=292.3 мс | bybit 83 сд. p50=112.6 мс | okx 24 сд. p50=150.2 мс | binance_futures_book 1210 сд. p50=143.1 мс | binance_futures_depth 91 сд. p50=143.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 232 сд. p50=110.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 11 сд. p50=40.7 мс | bitstamp 3 сд. p50=44.2 мс
22:51:48 [pm] T-192.0s Up 0.13/0.14 Down 0.86/0.87 ptb=81865.5 | CLOB 2833 сообщ., задержка p50/p90=39.5/44.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791499908006 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=1.9/1.9 мс
22:51:49 [cex] Binance 15 сд. задержка p50/p90=142.8/143.8 мс | Coinbase 50 задержка p50=79.6 мс | смещение часов +18.6 мс | lag loop p99/max=2.0/2.1 мс
22:51:49 [cex] binance_futures 29 сд. p50=292.3 мс | bybit 9 сд. p50=111.7 мс | okx 22 сд. p50=150.2 мс | binance_futures_book 608 сд. p50=143.0 мс | binance_futures_depth 91 сд. p50=143.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 85 сд. p50=110.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=42.7 мс | bitstamp 14 сд. p50=45.5 мс
22:51:58 [pm] T-182.0s Up 0.06/0.07 Down 0.93/0.94 ptb=81865.5 | CLOB 3707 сообщ., задержка p50/p90=40.1/155.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791499918008 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=1.9/2.0 мс
```

Представлено версией кода: 46d373e; python 3.12.3
