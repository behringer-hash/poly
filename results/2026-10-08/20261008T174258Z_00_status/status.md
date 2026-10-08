# Состояние сервера записи

Время (UTC): 2026-10-08 17:42:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 1 day, 10 hours, 19 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         606         679           2         814        1299
Swap:           2047           0        2047
```
- нагрузка CPU (1/5/15 мин): 0.13 / 0.21 / 0.29

## Данные
- файлов: 153, всего 337 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 6 | 5 МБ | 2 |
| bn_book | 6 | 379 КБ | 4 |
| bnf_agg | 6 | 10 МБ | 2 |
| bnf_book | 6 | 271 МБ | 0 |
| bnf_depth5 | 6 | 7 МБ | 2 |
| bnf_liq | 6 | 23 КБ | 30 |
| bs_trade | 6 | 361 КБ | 2 |
| by_book1 | 6 | 13 МБ | 2 |
| by_liq | 6 | 37 КБ | 193 |
| by_trade | 6 | 7 МБ | 2 |
| cb_ticker | 6 | 3 МБ | 2 |
| clock | 6 | 5 КБ | 18 |
| clock_pm | 6 | 5 КБ | 16 |
| events | 3 | 946 Б | 1797 |
| events_pm | 6 | 8 КБ | 24 |
| health_cex | 6 | 73 КБ | 2 |
| health_feeds | 6 | 320 КБ | 2 |
| health_pm | 6 | 72 КБ | 2 |
| kr_trade | 6 | 849 КБ | 2 |
| ok_trade | 6 | 8 МБ | 2 |
| pm_depth | 6 | 2 МБ | 0 |
| pm_rtt | 6 | 60 КБ | 0 |
| pm_top | 6 | 5 МБ | 0 |
| pm_trades | 6 | 3 МБ | 0 |
| rtds | 6 | 632 КБ | 0 |
| windows | 6 | 13 КБ | 325 |

Дни с данными: 2026-10-08

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 41, всего 291
- Polymarket CLOB: TCP 6, TLS 53, всего 96
- Polymarket gamma: TCP 5, TLS 45, всего 56

## Последние строки журнала записи
```
17:42:16 [cex] Binance 48 сд. задержка p50/p90=147.4/148.3 мс | Coinbase 59 задержка p50=85.3 мс | смещение часов +23.0 мс | lag loop p99/max=2.0/2.1 мс
17:42:16 [cex] binance_futures 77 сд. p50=260.7 мс | bybit 71 сд. p50=117.5 мс | okx 248 сд. p50=155.4 мс | binance_futures_book 3945 сд. p50=147.8 мс | binance_futures_depth 97 сд. p50=147.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 217 сд. p50=114.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 26 сд. p50=49.2 мс | bitstamp 2 сд. p50=57.4 мс
17:42:25 [pm] T-154.6s Up 0.31/0.32 Down 0.68/0.69 ptb=80799.0 | CLOB 8959 сообщ., задержка p50/p90=186.6/431.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791481345401 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.9 мс | lag loop p99/max=1.2/2.2 мс
17:42:26 [cex] Binance 198 сд. задержка p50/p90=148.0/155.4 мс | Coinbase 53 задержка p50=84.3 мс | смещение часов +23.0 мс | lag loop p99/max=3.2/6.9 мс
17:42:26 [cex] binance_futures 210 сд. p50=151.6 мс | bybit 178 сд. p50=117.9 мс | okx 208 сд. p50=158.0 мс | binance_futures_book 8243 сд. p50=148.8 мс | binance_futures_depth 97 сд. p50=147.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 273 сд. p50=114.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 24 сд. p50=49.5 мс | bitstamp 7 сд. p50=55.3 мс
17:42:32 [pm] btc-updown-5m-1791481200: CLOB#1 разорван (ConnectionClosedError(Close(code=1013, reason='slow consumer: send buffer full'), Close(code=1013, reason='slow consumer: send buffer full'), True)), переподключение
17:42:35 [pm] T-144.6s Up 0.49/0.50 Down 0.50/0.51 ptb=80799.0 | CLOB 9345 сообщ., задержка p50/p90=1419.2/1834.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791481355402 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.9 мс | lag loop p99/max=2.1/8.8 мс
17:42:36 [cex] Binance 142 сд. задержка p50/p90=149.3/153.1 мс | Coinbase 47 задержка p50=84.6 мс | смещение часов +23.0 мс | lag loop p99/max=2.0/7.6 мс
17:42:36 [cex] binance_futures 234 сд. p50=153.0 мс | bybit 255 сд. p50=117.5 мс | okx 269 сд. p50=156.3 мс | binance_futures_book 7992 сд. p50=150.0 мс | binance_futures_depth 97 сд. p50=147.6 мс | binance_liq 1 сд. p50=1149.3 мс | bybit_book 331 сд. p50=114.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 23 сд. p50=63.2 мс | bitstamp 13 сд. p50=55.5 мс
17:42:45 [pm] T-134.6s Up 0.66/0.67 Down 0.33/0.34 ptb=80799.0 | CLOB 14965 сообщ., задержка p50/p90=506.2/1058.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791481365403 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.9 мс | lag loop p99/max=1.3/1.6 мс
17:42:46 [cex] Binance 155 сд. задержка p50/p90=147.8/151.6 мс | Coinbase 83 задержка p50=84.5 мс | смещение часов +22.4 мс | lag loop p99/max=2.1/3.8 мс
17:42:46 [cex] binance_futures 275 сд. p50=149.1 мс | bybit 157 сд. p50=117.8 мс | okx 201 сд. p50=155.8 мс | binance_futures_book 5966 сд. p50=148.1 мс | binance_futures_depth 96 сд. p50=147.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 270 сд. p50=114.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 36 сд. p50=63.6 мс | bitstamp 4 сд. p50=53.2 мс
17:42:55 [pm] T-124.6s Up 0.46/0.47 Down 0.53/0.54 ptb=80799.0 | CLOB 11249 сообщ., задержка p50/p90=443.0/893.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791481375404 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.9 мс | lag loop p99/max=1.8/2.1 мс
17:42:56 [cex] Binance 124 сд. задержка p50/p90=147.2/150.1 мс | Coinbase 69 задержка p50=84.3 мс | смещение часов +22.4 мс | lag loop p99/max=2.9/6.3 мс
17:42:56 [cex] binance_futures 241 сд. p50=150.2 мс | bybit 222 сд. p50=117.2 мс | okx 206 сд. p50=154.9 мс | binance_futures_book 4452 сд. p50=147.7 мс | binance_futures_depth 95 сд. p50=147.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 264 сд. p50=114.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 37 сд. p50=53.6 мс | bitstamp 13 сд. p50=50.5 мс
```

Представлено версией кода: 46d373e; python 3.12.3
