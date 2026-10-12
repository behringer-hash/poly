# Состояние сервера записи

Время (UTC): 2026-10-12 21:26:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 14 hours, 2 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         781         841           2         480        1125
Swap:           2047         108        1939
```
- нагрузка CPU (1/5/15 мин): 0.17 / 0.26 / 0.30

## Данные
- файлов: 2719, всего 746 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 106 | 12 МБ | 1 |
| bn_book | 106 | 1018 КБ | 3 |
| bnf_agg | 106 | 18 МБ | 1 |
| bnf_book | 106 | 489 МБ | 1 |
| bnf_depth5 | 106 | 38 МБ | 1 |
| bnf_liq | 93 | 53 КБ | 781 |
| bs_trade | 106 | 1 МБ | 3 |
| by_book1 | 106 | 38 МБ | 1 |
| by_liq | 89 | 46 КБ | 1177 |
| by_trade | 106 | 11 МБ | 3 |
| cb_ticker | 106 | 11 МБ | 3 |
| clock | 106 | 81 КБ | 47 |
| clock_pm | 106 | 81 КБ | 6 |
| events | 99 | 33 КБ | 169 |
| events_pm | 106 | 40 КБ | 1502 |
| health_cex | 106 | 1 МБ | 9 |
| health_feeds | 106 | 4 МБ | 9 |
| health_pm | 106 | 1 МБ | 10 |
| kr_trade | 106 | 3 МБ | 7 |
| ok_trade | 106 | 16 МБ | 1 |
| pm_depth | 106 | 21 МБ | 2 |
| pm_rtt | 106 | 714 КБ | 4 |
| pm_top | 106 | 42 МБ | 2 |
| pm_trades | 106 | 30 МБ | 2 |
| rtds | 106 | 7 МБ | 2 |
| windows | 106 | 218 КБ | 44 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 48, всего 296
- Polymarket CLOB: TCP 5, TLS 41, всего 88
- Polymarket gamma: TCP 5, TLS 40, всего 51

## Последние строки журнала записи
```
21:26:06 [pm] T-233.0s Up 0.56/0.57 Down 0.43/0.44 ptb=82865.8 | CLOB 4552 сообщ., задержка p50/p90=43.6/110.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791840366979 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=2.3/3.4 мс
21:26:07 [cex] Binance 14 сд. задержка p50/p90=143.7/144.6 мс | Coinbase 11 задержка p50=81.9 мс | смещение часов +19.0 мс | lag loop p99/max=2.0/2.1 мс
21:26:07 [cex] binance_futures 18 сд. p50=292.8 мс | bybit 38 сд. p50=112.6 мс | okx 88 сд. p50=151.2 мс | binance_futures_book 360 сд. p50=143.2 мс | binance_futures_depth 73 сд. p50=143.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 71 сд. p50=110.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 16 сд. p50=45.4 мс | bitstamp 3 сд. p50=47.4 мс
21:26:16 [pm] T-223.0s Up 0.52/0.53 Down 0.47/0.48 ptb=82865.8 | CLOB 6887 сообщ., задержка p50/p90=41.7/44.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791840376980 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=2.0/3.5 мс
21:26:17 [cex] Binance 20 сд. задержка p50/p90=143.3/143.6 мс | Coinbase 21 задержка p50=85.2 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/3.9 мс
21:26:17 [cex] binance_futures 19 сд. p50=292.9 мс | bybit 26 сд. p50=112.4 мс | okx 17 сд. p50=146.7 мс | binance_futures_book 944 сд. p50=143.1 мс | binance_futures_depth 87 сд. p50=143.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 123 сд. p50=110.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 11 сд. p50=47.0 мс | bitstamp 1 сд. p50=44.5 мс
21:26:26 [pm] T-213.0s Up 0.54/0.55 Down 0.45/0.46 ptb=82865.8 | CLOB 4100 сообщ., задержка p50/p90=41.7/44.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791840386981 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=1.8/2.0 мс
21:26:27 [cex] Binance 12 сд. задержка p50/p90=143.3/144.2 мс | Coinbase 13 задержка p50=81.7 мс | смещение часов +19.0 мс | lag loop p99/max=2.2/2.2 мс
21:26:27 [cex] binance_futures 18 сд. p50=268.0 мс | bybit 3 сд. p50=112.6 мс | okx 21 сд. p50=146.7 мс | binance_futures_book 292 сд. p50=142.9 мс | binance_futures_depth 72 сд. p50=143.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 44 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=43.5 мс | bitstamp 2 сд. p50=45.4 мс
21:26:36 [pm] T-203.0s Up 0.53/0.54 Down 0.46/0.47 ptb=82865.8 | CLOB 4105 сообщ., задержка p50/p90=41.7/44.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791840396982 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.6/2.1 мс
21:26:37 [cex] Binance 83 сд. задержка p50/p90=150.1/159.5 мс | Coinbase 34 задержка p50=81.5 мс | смещение часов +19.0 мс | lag loop p99/max=2.2/2.3 мс
21:26:37 [cex] binance_futures 97 сд. p50=153.0 мс | bybit 53 сд. p50=117.0 мс | okx 115 сд. p50=150.7 мс | binance_futures_book 1864 сд. p50=143.5 мс | binance_futures_depth 86 сд. p50=143.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 62 сд. p50=110.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 9 сд. p50=54.8 мс | bitstamp 6 сд. p50=50.5 мс
21:26:46 [pm] T-193.0s Up 0.11/0.12 Down 0.88/0.89 ptb=82865.8 | CLOB 10300 сообщ., задержка p50/p90=45.5/75.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791840406983 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=5.7/6.3 мс
21:26:47 [cex] Binance 101 сд. задержка p50/p90=147.5/150.4 мс | Coinbase 11 задержка p50=94.0 мс | смещение часов +19.0 мс | lag loop p99/max=2.2/10.9 мс
21:26:47 [cex] binance_futures 145 сд. p50=150.6 мс | bybit 98 сд. p50=113.7 мс | okx 83 сд. p50=149.7 мс | binance_futures_book 5440 сд. p50=143.1 мс | binance_futures_depth 87 сд. p50=143.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 250 сд. p50=110.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 15 сд. p50=65.1 мс | bitstamp 10 сд. p50=57.1 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
