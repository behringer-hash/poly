# Состояние сервера записи

Время (UTC): 2026-10-25 03:05:58

## Службы
- lab-collector: inactive
- lab-runner.timer: active
- uptime: up 3 weeks, 3 days, 19 hours, 42 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 10 ГБ из 57 ГБ, свободно 47 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         538         391           2        1169        1367
Swap:           2047          94        1953
```
- нагрузка CPU (1/5/15 мин): 0.00 / 0.01 / 0.00

## Данные
- файлов: 6694, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 275 | 34 МБ | 307333 |
| bn_book | 275 | 3 МБ | 307336 |
| bnf_agg | 275 | 56 МБ | 307341 |
| bnf_book | 79 | 323 МБ | 1012652 |
| bnf_depth5 | 79 | 26 МБ | 1012728 |
| bnf_liq | 240 | 152 КБ | 307554 |
| bs_trade | 79 | 824 КБ | 1012648 |
| by_book1 | 275 | 111 МБ | 307336 |
| by_liq | 250 | 116 КБ | 307556 |
| by_trade | 275 | 39 МБ | 307341 |
| bys_book1 | 198 | 66 МБ | 307331 |
| bys_trade | 198 | 28 МБ | 307341 |
| cb_ticker | 275 | 33 МБ | 307335 |
| clock | 275 | 214 КБ | 307381 |
| clock_pm | 275 | 213 КБ | 307336 |
| events | 267 | 85 КБ | 307341 |
| events_pm | 276 | 96 КБ | 307335 |
| health_cex | 275 | 3 МБ | 307349 |
| health_feeds | 275 | 9 МБ | 307349 |
| health_pm | 275 | 3 МБ | 307335 |
| kr_trade | 79 | 2 МБ | 1012648 |
| ok_trade | 274 | 45 МБ | 307329 |
| pm_depth | 275 | 54 МБ | 307336 |
| pm_rtt | 275 | 2 МБ | 307335 |
| pm_top | 275 | 112 МБ | 307337 |
| pm_trades | 275 | 79 МБ | 307335 |
| rtds | 275 | 17 МБ | 307340 |
| windows | 275 | 567 КБ | 307335 |

Дни с данными: 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 35, всего 309
- Polymarket CLOB: TCP 6, TLS 37, всего 81
- Polymarket gamma: TCP 4, TLS 34, всего 40

## Последние строки журнала записи
```
13:42:48 [cex] binance_futures 136 сд. p50=159.1 мс | bybit 231 сд. p50=117.7 мс | bybit_book 351 сд. p50=115.3 мс | bybit_spot 120 сд. p50=129.8 мс | bybit_spot_book 122 сд. p50=115.5 мс | okx 214 сд. p50=149.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:42:49 [pm] T-130.8s Up 0.04/0.05 Down 0.95/0.96 ptb=83489.2 | CLOB 5948 сообщ., задержка p50/p90=43.4/46.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590169239 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.7/1.8 мс
13:42:58 [cex] Binance 194 сд. задержка p50/p90=170.9/172.1 мс | Coinbase 84 задержка p50=81.0 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/7.6 мс
13:42:58 [cex] binance_futures 320 сд. p50=160.6 мс | bybit 599 сд. p50=141.2 мс | bybit_book 301 сд. p50=115.3 мс | bybit_spot 220 сд. p50=124.5 мс | bybit_spot_book 197 сд. p50=115.4 мс | okx 369 сд. p50=163.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:42:59 [pm] T-120.8s Up 0.01/0.02 Down 0.98/0.99 ptb=83489.2 | CLOB 5791 сообщ., задержка p50/p90=41.4/43.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590179241 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.0/2.1 мс
13:43:08 [cex] Binance 552 сд. задержка p50/p90=149.4/163.6 мс | Coinbase 78 задержка p50=80.3 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/4.0 мс
13:43:08 [cex] binance_futures 503 сд. p50=158.7 мс | bybit 665 сд. p50=117.0 мс | bybit_book 494 сд. p50=114.1 мс | bybit_spot 384 сд. p50=124.9 мс | bybit_spot_book 260 сд. p50=114.3 мс | okx 619 сд. p50=149.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:43:09 [pm] T-110.8s Up 0.16/0.17 Down 0.83/0.84 ptb=83489.2 | CLOB 13057 сообщ., задержка p50/p90=41.5/43.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590189243 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.3/4.0 мс
13:43:18 [cex] Binance 305 сд. задержка p50/p90=156.5/158.7 мс | Coinbase 97 задержка p50=83.0 мс | смещение часов +22.1 мс | lag loop p99/max=2.1/2.1 мс
13:43:18 [cex] binance_futures 366 сд. p50=160.4 мс | bybit 483 сд. p50=117.0 мс | bybit_book 465 сд. p50=114.1 мс | bybit_spot 275 сд. p50=123.8 мс | bybit_spot_book 218 сд. p50=114.3 мс | okx 371 сд. p50=148.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:43:19 [pm] T-100.8s Up 0.19/0.20 Down 0.80/0.81 ptb=83489.2 | CLOB 13971 сообщ., задержка p50/p90=41.4/42.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590199244 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.8/3.3 мс
13:43:28 [cex] Binance 262 сд. задержка p50/p90=148.2/154.1 мс | Coinbase 58 задержка p50=79.7 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/2.9 мс
13:43:28 [cex] binance_futures 254 сд. p50=149.6 мс | bybit 216 сд. p50=116.4 мс | bybit_book 433 сд. p50=114.1 мс | bybit_spot 108 сд. p50=118.7 мс | bybit_spot_book 156 сд. p50=114.3 мс | okx 323 сд. p50=148.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:43:29 [pm] T- 90.8s Up 0.35/0.36 Down 0.64/0.65 ptb=83489.2 | CLOB 14782 сообщ., задержка p50/p90=41.5/44.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590209247 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.6/2.2 мс
[run] остановка...
```

Представлено версией кода: b98a05a; python 3.12.3
