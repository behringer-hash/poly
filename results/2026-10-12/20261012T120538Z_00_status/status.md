# Состояние сервера записи

Время (UTC): 2026-10-12 12:05:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 4 hours, 41 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         754         869           2         490        1151
Swap:           2047         105        1942
```
- нагрузка CPU (1/5/15 мин): 0.65 / 0.52 / 0.47

## Данные
- файлов: 2486, всего 622 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 97 | 10 МБ | 1 |
| bn_book | 97 | 880 КБ | 9 |
| bnf_agg | 97 | 16 МБ | 1 |
| bnf_book | 97 | 399 МБ | 0 |
| bnf_depth5 | 97 | 33 МБ | 1 |
| bnf_liq | 84 | 46 КБ | 188 |
| bs_trade | 97 | 1 МБ | 1 |
| by_book1 | 97 | 32 МБ | 1 |
| by_liq | 79 | 41 КБ | 946 |
| by_trade | 97 | 10 МБ | 1 |
| cb_ticker | 97 | 9 МБ | 1 |
| clock | 97 | 73 КБ | 39 |
| clock_pm | 97 | 73 КБ | 55 |
| events | 92 | 31 КБ | 1925 |
| events_pm | 97 | 37 КБ | 11 |
| health_cex | 97 | 1011 КБ | 5 |
| health_feeds | 97 | 4 МБ | 5 |
| health_pm | 97 | 1 МБ | 5 |
| kr_trade | 97 | 2 МБ | 3 |
| ok_trade | 97 | 14 МБ | 1 |
| pm_depth | 97 | 19 МБ | 1 |
| pm_rtt | 97 | 640 КБ | 1 |
| pm_top | 97 | 37 МБ | 1 |
| pm_trades | 97 | 26 МБ | 1 |
| rtds | 97 | 6 МБ | 1 |
| windows | 97 | 197 КБ | 274 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 44, всего 294
- Polymarket CLOB: TCP 5, TLS 49, всего 94
- Polymarket gamma: TCP 5, TLS 43, всего 55

## Последние строки журнала записи
```
12:04:51 [cex] Binance 123 сд. задержка p50/p90=159.7/164.4 мс | Coinbase 31 задержка p50=83.0 мс | смещение часов +19.7 мс | lag loop p99/max=2.2/6.3 мс
12:04:51 [cex] binance_futures 98 сд. p50=149.7 мс | bybit 90 сд. p50=114.2 мс | okx 114 сд. p50=153.9 мс | binance_futures_book 3670 сд. p50=147.7 мс | binance_futures_depth 91 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 142 сд. p50=111.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 15 сд. p50=41.6 мс | bitstamp 10 сд. p50=50.9 мс
12:05:01 [pm] T-298.2s Up 0.57/0.58 Down 0.42/0.43 ptb=n/a | CLOB 2751 сообщ., задержка p50/p90=37.5/46.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791806701844 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.9/2.4 мс
12:05:01 [cex] Binance 111 сд. задержка p50/p90=156.9/158.6 мс | Coinbase 32 задержка p50=81.6 мс | смещение часов +19.8 мс | lag loop p99/max=12.2/27.2 мс
12:05:01 [cex] binance_futures 98 сд. p50=151.4 мс | bybit 202 сд. p50=113.3 мс | okx 98 сд. p50=154.2 мс | binance_futures_book 3398 сд. p50=150.1 мс | binance_futures_depth 94 сд. p50=144.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 162 сд. p50=111.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=61.6 мс | bitstamp 5 сд. p50=53.9 мс
12:05:11 [pm] T-288.2s Up 0.69/0.70 Down 0.30/0.31 ptb=83244.7 | CLOB 8559 сообщ., задержка p50/p90=180.4/280.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791806711846 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=16.3/30.3 мс
12:05:11 [cex] Binance 197 сд. задержка p50/p90=157.1/161.6 мс | Coinbase 45 задержка p50=82.3 мс | смещение часов +19.8 мс | lag loop p99/max=8.7/36.2 мс
12:05:11 [cex] binance_futures 147 сд. p50=147.2 мс | bybit 175 сд. p50=116.0 мс | okx 151 сд. p50=154.5 мс | binance_futures_book 6313 сд. p50=152.6 мс | binance_futures_depth 95 сд. p50=144.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 217 сд. p50=112.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 14 сд. p50=68.3 мс | bitstamp 11 сд. p50=63.2 мс
12:05:21 [pm] T-278.2s Up 0.55/0.56 Down 0.44/0.45 ptb=83244.7 | CLOB 8153 сообщ., задержка p50/p90=51.7/197.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791806721847 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.7/2.0 мс
12:05:21 [cex] Binance 40 сд. задержка p50/p90=156.7/158.2 мс | Coinbase 24 задержка p50=96.2 мс | смещение часов +19.8 мс | lag loop p99/max=2.7/6.4 мс
12:05:21 [cex] binance_futures 92 сд. p50=156.7 мс | bybit 67 сд. p50=114.6 мс | okx 103 сд. p50=158.8 мс | binance_futures_book 8293 сд. p50=145.4 мс | binance_futures_depth 95 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 173 сд. p50=111.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=59.5 мс | bitstamp 4 сд. p50=46.8 мс
12:05:27 [pm] btc-updown-5m-1791806700: CLOB#0 разорван (ConnectionClosedError(Close(code=1013, reason='slow consumer: send buffer full'), Close(code=1013, reason='slow consumer: send buffer full'), True)), переподключение
12:05:31 [pm] T-268.2s Up 0.71/0.72 Down 0.28/0.29 ptb=83244.7 | CLOB 9726 сообщ., задержка p50/p90=39.4/47.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791806731849 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=2.2/7.2 мс
12:05:31 [cex] Binance 130 сд. задержка p50/p90=158.1/160.6 мс | Coinbase 49 задержка p50=82.7 мс | смещение часов +19.8 мс | lag loop p99/max=3.0/5.6 мс
12:05:31 [cex] binance_futures 188 сд. p50=148.0 мс | bybit 150 сд. p50=113.3 мс | okx 205 сд. p50=154.0 мс | binance_futures_book 6578 сд. p50=146.2 мс | binance_futures_depth 95 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 249 сд. p50=112.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 27 сд. p50=46.2 мс | bitstamp 11 сд. p50=47.1 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
