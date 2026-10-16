# Состояние сервера записи

Время (UTC): 2026-10-16 19:26:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 12 hours, 2 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         798        1006           2         374        1107
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.54 / 0.37 / 0.35

## Данные
- файлов: 4987, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 200 | 28 МБ | 2 |
| bn_book | 200 | 3 МБ | 2 |
| bnf_agg | 200 | 44 МБ | 2 |
| bnf_book | 118 | 557 МБ | 293892 |
| bnf_depth5 | 118 | 41 МБ | 293968 |
| bnf_liq | 180 | 126 КБ | 16 |
| bs_trade | 118 | 1 МБ | 293888 |
| by_book1 | 200 | 91 МБ | 2 |
| by_liq | 179 | 103 КБ | 16 |
| by_trade | 200 | 29 МБ | 2 |
| bys_book1 | 84 | 36 МБ | 2 |
| bys_trade | 84 | 15 МБ | 2 |
| cb_ticker | 200 | 26 МБ | 2 |
| clock | 200 | 154 КБ | 40 |
| clock_pm | 200 | 154 КБ | 60 |
| events | 189 | 60 КБ | 1216 |
| events_pm | 200 | 77 КБ | 341 |
| health_cex | 200 | 2 МБ | 4 |
| health_feeds | 200 | 7 МБ | 4 |
| health_pm | 200 | 2 МБ | 9 |
| kr_trade | 118 | 3 МБ | 293888 |
| ok_trade | 199 | 39 МБ | 2 |
| pm_depth | 200 | 40 МБ | 1 |
| pm_rtt | 200 | 1 МБ | 5 |
| pm_top | 200 | 83 МБ | 1 |
| pm_trades | 200 | 60 МБ | 1 |
| rtds | 200 | 13 МБ | 1 |
| windows | 200 | 412 КБ | 62 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 51, всего 301
- Polymarket CLOB: TCP 5, TLS 48, всего 88
- Polymarket gamma: TCP 5, TLS 38, всего 51

## Последние строки журнала записи
```
19:25:53 [cex] Binance 369 сд. задержка p50/p90=151.4/159.6 мс | Coinbase 88 задержка p50=81.3 мс | смещение часов +23.0 мс | lag loop p99/max=2.1/2.5 мс
19:25:53 [cex] binance_futures 824 сд. p50=153.9 мс | bybit 660 сд. p50=122.3 мс | bybit_book 420 сд. p50=115.2 мс | bybit_spot 496 сд. p50=117.2 мс | bybit_spot_book 247 сд. p50=114.9 мс | okx 740 сд. p50=304.1 мс | binance_liq 1 сд. p50=1151.2 мс | bybit_liq 3 сд. p50=416.1 мс
19:25:58 [pm] T-241.7s Up 0.86/0.87 Down 0.13/0.14 ptb=81380.9 | CLOB 8794 сообщ., задержка p50/p90=56.8/102.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792178758343 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=1.7/2.6 мс
19:26:03 [cex] Binance 203 сд. задержка p50/p90=148.4/149.9 мс | Coinbase 51 задержка p50=79.9 мс | смещение часов +22.4 мс | lag loop p99/max=2.4/4.1 мс
19:26:03 [cex] binance_futures 280 сд. p50=148.4 мс | bybit 268 сд. p50=116.1 мс | bybit_book 289 сд. p50=114.9 мс | bybit_spot 205 сд. p50=116.5 мс | bybit_spot_book 216 сд. p50=114.6 мс | okx 348 сд. p50=158.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:26:08 [pm] T-231.7s Up 0.83/0.84 Down 0.16/0.17 ptb=81380.9 | CLOB 7244 сообщ., задержка p50/p90=41.6/51.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792178768344 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=2.2/3.6 мс
19:26:13 [cex] Binance 36 сд. задержка p50/p90=147.2/148.3 мс | Coinbase 57 задержка p50=78.4 мс | смещение часов +22.4 мс | lag loop p99/max=2.1/2.2 мс
19:26:13 [cex] binance_futures 140 сд. p50=148.6 мс | bybit 121 сд. p50=115.7 мс | bybit_book 200 сд. p50=114.6 мс | bybit_spot 223 сд. p50=116.5 мс | bybit_spot_book 170 сд. p50=114.4 мс | okx 174 сд. p50=157.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:26:18 [pm] T-221.7s Up 0.89/0.92 Down 0.08/0.11 ptb=81380.9 | CLOB 5650 сообщ., задержка p50/p90=40.0/42.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792178778345 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=1.5/1.7 мс
19:26:23 [cex] Binance 342 сд. задержка p50/p90=155.8/160.3 мс | Coinbase 106 задержка p50=85.5 мс | смещение часов +22.4 мс | lag loop p99/max=2.1/2.1 мс
19:26:23 [cex] binance_futures 979 сд. p50=153.8 мс | bybit 461 сд. p50=122.8 мс | bybit_book 223 сд. p50=114.6 мс | bybit_spot 338 сд. p50=117.4 мс | bybit_spot_book 202 сд. p50=114.4 мс | okx 586 сд. p50=253.3 мс | binance_liq 1 сд. p50=1148.4 мс | bybit_liq 1 сд. p50=488.9 мс
19:26:28 [pm] T-211.7s Up 0.93/0.94 Down 0.06/0.07 ptb=81380.9 | CLOB 6849 сообщ., задержка p50/p90=43.5/82.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792178788346 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=2.0/2.1 мс
19:26:33 [cex] Binance 189 сд. задержка p50/p90=147.6/148.9 мс | Coinbase 79 задержка p50=81.2 мс | смещение часов +22.4 мс | lag loop p99/max=2.1/2.2 мс
19:26:33 [cex] binance_futures 296 сд. p50=148.9 мс | bybit 293 сд. p50=115.9 мс | bybit_book 264 сд. p50=114.5 мс | bybit_spot 217 сд. p50=116.7 мс | bybit_spot_book 217 сд. p50=114.3 мс | okx 221 сд. p50=157.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:26:38 [pm] T-201.7s Up 0.94/0.95 Down 0.05/0.06 ptb=81380.9 | CLOB 6530 сообщ., задержка p50/p90=42.0/84.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792178798348 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=3.0/4.7 мс
```

Представлено версией кода: 8083be6; python 3.12.3
