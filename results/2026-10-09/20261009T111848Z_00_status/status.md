# Состояние сервера записи

Время (UTC): 2026-10-09 11:18:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 3 hours, 54 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         667         388           2        1044        1238
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.24 / 0.16 / 0.20

## Данные
- файлов: 617, всего 268 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 24 | 4 МБ | 1 |
| bn_book | 24 | 432 КБ | 11 |
| bnf_agg | 24 | 7 МБ | 1 |
| bnf_book | 24 | 189 МБ | 1 |
| bnf_depth5 | 24 | 11 МБ | 1 |
| bnf_liq | 23 | 22 КБ | 1707 |
| bs_trade | 24 | 473 КБ | 1 |
| by_book1 | 24 | 14 МБ | 1 |
| by_liq | 21 | 23 КБ | 2119 |
| by_trade | 24 | 5 МБ | 1 |
| cb_ticker | 24 | 4 МБ | 3 |
| clock | 24 | 18 КБ | 35 |
| clock_pm | 24 | 18 КБ | 40 |
| events | 21 | 7 КБ | 482 |
| events_pm | 24 | 12 КБ | 206 |
| health_cex | 24 | 254 КБ | 1 |
| health_feeds | 24 | 958 КБ | 1 |
| health_pm | 24 | 259 КБ | 4 |
| kr_trade | 24 | 992 КБ | 1 |
| ok_trade | 24 | 7 МБ | 1 |
| pm_depth | 24 | 5 МБ | 2 |
| pm_rtt | 24 | 163 КБ | 6 |
| pm_top | 24 | 11 МБ | 2 |
| pm_trades | 24 | 7 МБ | 2 |
| rtds | 24 | 2 МБ | 2 |
| windows | 24 | 48 КБ | 255 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 45, всего 296
- Polymarket CLOB: TCP 7, TLS 47, всего 87
- Polymarket gamma: TCP 5, TLS 41, всего 53

## Последние строки журнала записи
```
11:18:04 [pm] T-115.7s Up 0.98/0.99 Down 0.01/0.02 ptb=82428.1 | CLOB 2316 сообщ., задержка p50/p90=39.8/44.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791544684326 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=2.0/2.1 мс
11:18:06 [cex] Binance 20 сд. задержка p50/p90=145.6/146.6 мс | Coinbase 12 задержка p50=84.6 мс | смещение часов +21.4 мс | lag loop p99/max=3.1/4.9 мс
11:18:06 [cex] binance_futures 45 сд. p50=146.0 мс | bybit 41 сд. p50=115.2 мс | okx 42 сд. p50=145.9 мс | binance_futures_book 1060 сд. p50=159.2 мс | binance_futures_depth 85 сд. p50=146.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 174 сд. p50=113.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 8 сд. p50=41.1 мс | bitstamp 6 сд. p50=51.6 мс
11:18:14 [pm] T-105.7s Up 0.98/0.99 Down 0.01/0.02 ptb=82428.1 | CLOB 1332 сообщ., задержка p50/p90=39.9/43.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791544694328 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=1.9/2.1 мс
11:18:16 [cex] Binance 16 сд. задержка p50/p90=145.4/145.6 мс | Coinbase 7 задержка p50=82.4 мс | смещение часов +18.9 мс | lag loop p99/max=2.1/2.1 мс
11:18:16 [cex] binance_futures 23 сд. p50=294.5 мс | bybit 26 сд. p50=115.2 мс | okx 55 сд. p50=146.2 мс | binance_futures_book 957 сд. p50=158.9 мс | binance_futures_depth 93 сд. p50=146.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 197 сд. p50=113.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=39.3 мс | bitstamp 6 сд. p50=50.7 мс
11:18:24 [pm] T- 95.7s Up 0.97/0.98 Down 0.02/0.03 ptb=82428.1 | CLOB 2785 сообщ., задержка p50/p90=65.0/338.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791544704329 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.3 мс | lag loop p99/max=2.0/2.0 мс
11:18:26 [cex] Binance 72 сд. задержка p50/p90=143.7/144.1 мс | Coinbase 13 задержка p50=81.9 мс | смещение часов +18.9 мс | lag loop p99/max=2.1/2.2 мс
11:18:26 [cex] binance_futures 97 сд. p50=145.1 мс | bybit 100 сд. p50=112.7 мс | okx 126 сд. p50=143.6 мс | binance_futures_book 4104 сд. p50=157.1 мс | binance_futures_depth 92 сд. p50=143.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 173 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 17 сд. p50=53.0 мс | bitstamp 8 сд. p50=60.8 мс
11:18:34 [pm] T- 85.7s Up 0.92/0.93 Down 0.07/0.08 ptb=82428.1 | CLOB 4888 сообщ., задержка p50/p90=271.7/416.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791544714330 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.3 мс | lag loop p99/max=1.6/1.7 мс
11:18:36 [cex] Binance 207 сд. задержка p50/p90=146.0/150.1 мс | Coinbase 48 задержка p50=84.7 мс | смещение часов +18.9 мс | lag loop p99/max=2.1/2.2 мс
11:18:36 [cex] binance_futures 205 сд. p50=148.5 мс | bybit 236 сд. p50=114.0 мс | okx 119 сд. p50=144.8 мс | binance_futures_book 5832 сд. p50=158.8 мс | binance_futures_depth 95 сд. p50=143.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 234 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 31 сд. p50=57.8 мс | bitstamp 6 сд. p50=57.9 мс
11:18:44 [pm] T- 75.7s Up 0.92/0.94 Down 0.06/0.08 ptb=82428.1 | CLOB 6445 сообщ., задержка p50/p90=45.7/134.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791544724332 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.3 мс | lag loop p99/max=2.0/2.1 мс
11:18:46 [cex] Binance 28 сд. задержка p50/p90=143.1/144.1 мс | Coinbase 38 задержка p50=81.4 мс | смещение часов +18.9 мс | lag loop p99/max=2.0/2.1 мс
11:18:46 [cex] binance_futures 35 сд. p50=291.9 мс | bybit 148 сд. p50=112.5 мс | okx 128 сд. p50=145.2 мс | binance_futures_book 2596 сд. p50=156.8 мс | binance_futures_depth 93 сд. p50=144.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 237 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 15 сд. p50=41.4 мс | bitstamp 10 сд. p50=49.5 мс
```

Представлено версией кода: 3f62835; python 3.12.3
