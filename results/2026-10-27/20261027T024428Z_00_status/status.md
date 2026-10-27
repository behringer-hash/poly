# Состояние сервера записи

Время (UTC): 2026-10-27 02:44:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 5 days, 19 hours, 20 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         678         811           1         589        1227
Swap:           2047         293        1754
```
- нагрузка CPU (1/5/15 мин): 0.29 / 0.26 / 0.29

## Данные
- файлов: 5838, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 2 |
| bn_book | 242 | 3 МБ | 22 |
| bnf_agg | 242 | 52 МБ | 2 |
| bnf_book | 46 | 399 МБ | 2 |
| bnf_depth5 | 32 | 12 МБ | 1184238 |
| bnf_liq | 216 | 147 КБ | 20 |
| bs_trade | 32 | 473 КБ | 1184158 |
| by_book1 | 242 | 111 МБ | 2 |
| by_liq | 229 | 108 КБ | 22 |
| by_trade | 242 | 35 МБ | 4 |
| bys_book1 | 212 | 72 МБ | 2 |
| bys_trade | 212 | 29 МБ | 2 |
| cb_ticker | 242 | 33 МБ | 2 |
| clock | 242 | 188 КБ | 47 |
| clock_pm | 242 | 189 КБ | 58 |
| events | 231 | 73 КБ | 1380 |
| events_pm | 241 | 85 КБ | 405 |
| health_cex | 242 | 2 МБ | 2 |
| health_feeds | 242 | 8 МБ | 2 |
| health_pm | 242 | 3 МБ | 3 |
| kr_trade | 32 | 1 МБ | 1184158 |
| ok_trade | 241 | 45 МБ | 2 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 5 |
| pm_top | 242 | 103 МБ | 1 |
| pm_trades | 242 | 72 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 500 КБ | 324 |

Дни с данными: 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 35, всего 282
- Polymarket CLOB: TCP 5, TLS 45, всего 90
- Polymarket gamma: TCP 4, TLS 39, всего 46

## Последние строки журнала записи
```
02:43:45 [cex] Binance 47 сд. задержка p50/p90=142.5/143.5 мс | Coinbase 36 задержка p50=80.3 мс | смещение часов +19.9 мс | lag loop p99/max=2.1/2.2 мс
02:43:45 [cex] binance_futures 18 сд. p50=292.0 мс | bybit 2 сд. p50=111.3 мс | bybit_book 92 сд. p50=109.3 мс | bybit_spot 69 сд. p50=112.3 мс | bybit_spot_book 60 сд. p50=110.0 мс | okx 12 сд. p50=159.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1517 сд. p50=143.5 мс
02:43:45 [pm] T- 74.7s Up 0.99/0.99 Down 0.01/0.01 ptb=79766.3 | CLOB 3556 сообщ., задержка p50/p90=39.2/46.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793069025264 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=1.3/1.8 мс
02:43:55 [cex] Binance 32 сд. задержка p50/p90=142.7/145.0 мс | Coinbase 61 задержка p50=80.1 мс | смещение часов +19.9 мс | lag loop p99/max=2.3/3.1 мс
02:43:55 [cex] binance_futures 56 сд. p50=147.6 мс | bybit 40 сд. p50=112.5 мс | bybit_book 115 сд. p50=109.4 мс | bybit_spot 156 сд. p50=113.0 мс | bybit_spot_book 85 сд. p50=110.2 мс | okx 46 сд. p50=160.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3429 сд. p50=144.0 мс
02:43:55 [pm] T- 64.7s Up 0.99/0.99 Down 0.01/0.01 ptb=79766.3 | CLOB 5380 сообщ., задержка p50/p90=38.3/75.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793069035264 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=1.7/2.1 мс
02:44:05 [cex] Binance 46 сд. задержка p50/p90=143.7/143.9 мс | Coinbase 42 задержка p50=80.1 мс | смещение часов +19.9 мс | lag loop p99/max=2.0/6.2 мс
02:44:05 [cex] binance_futures 23 сд. p50=292.3 мс | bybit 31 сд. p50=111.9 мс | bybit_book 100 сд. p50=109.5 мс | bybit_spot 57 сд. p50=114.5 мс | bybit_spot_book 67 сд. p50=110.3 мс | okx 14 сд. p50=160.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 2 сд. p50=512.4 мс | binance_futures_book 2362 сд. p50=143.8 мс
02:44:05 [pm] T- 54.7s Up 1.00/1.00 Down 0.00/0.00 ptb=79766.3 | CLOB 2222 сообщ., задержка p50/p90=38.7/79.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793069045266 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=1.9/2.1 мс
02:44:15 [cex] Binance 32 сд. задержка p50/p90=142.8/150.8 мс | Coinbase 37 задержка p50=81.8 мс | смещение часов +19.9 мс | lag loop p99/max=2.1/4.6 мс
02:44:15 [cex] binance_futures 79 сд. p50=147.6 мс | bybit 40 сд. p50=111.9 мс | bybit_book 127 сд. p50=109.5 мс | bybit_spot 156 сд. p50=112.6 мс | bybit_spot_book 77 сд. p50=110.1 мс | okx 40 сд. p50=160.0 мс | binance_liq 1 сд. p50=1145.4 мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5322 сд. p50=144.8 мс
02:44:15 [pm] T- 44.7s Up 1.00/n/a Down n/a/0.00 ptb=79766.3 | CLOB 1329 сообщ., задержка p50/p90=38.2/39.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793069055268 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.1 мс | lag loop p99/max=2.1/2.3 мс
02:44:25 [cex] Binance 26 сд. задержка p50/p90=142.6/143.5 мс | Coinbase 59 задержка p50=81.1 мс | смещение часов +19.9 мс | lag loop p99/max=2.2/6.0 мс
02:44:25 [cex] binance_futures 40 сд. p50=159.0 мс | bybit 27 сд. p50=112.3 мс | bybit_book 95 сд. p50=109.5 мс | bybit_spot 125 сд. p50=112.6 мс | bybit_spot_book 60 сд. p50=110.2 мс | okx 71 сд. p50=162.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1965 сд. p50=144.7 мс
02:44:25 [pm] T- 34.7s Up 1.00/n/a Down n/a/0.00 ptb=79766.3 | CLOB 408 сообщ., задержка p50/p90=38.4/48.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793069065270 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=2.0/2.1 мс
```

Представлено версией кода: 80591e6; python 3.12.3
