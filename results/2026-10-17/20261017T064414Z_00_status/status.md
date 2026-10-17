# Состояние сервера записи

Время (UTC): 2026-10-17 06:44:14

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 23 hours, 20 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         861         549           2         782        1044
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.42 / 0.31 / 0.23

## Данные
- файлов: 5244, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 211 | 30 МБ | 1 |
| bn_book | 211 | 3 МБ | 12 |
| bnf_agg | 211 | 44 МБ | 1 |
| bnf_book | 118 | 557 МБ | 334548 |
| bnf_depth5 | 118 | 41 МБ | 334625 |
| bnf_liq | 187 | 128 КБ | 11457 |
| bs_trade | 118 | 1 МБ | 334544 |
| by_book1 | 211 | 92 МБ | 1 |
| by_liq | 187 | 104 КБ | 11899 |
| by_trade | 211 | 29 МБ | 1 |
| bys_book1 | 95 | 36 МБ | 1 |
| bys_trade | 95 | 14 МБ | 5 |
| cb_ticker | 211 | 27 МБ | 1 |
| clock | 211 | 163 КБ | 63 |
| clock_pm | 211 | 164 КБ | 21 |
| events | 200 | 66 КБ | 450 |
| events_pm | 211 | 78 КБ | 366 |
| health_cex | 211 | 2 МБ | 5 |
| health_feeds | 211 | 7 МБ | 5 |
| health_pm | 211 | 2 МБ | 9 |
| kr_trade | 118 | 3 МБ | 334544 |
| ok_trade | 210 | 38 МБ | 3 |
| pm_depth | 211 | 43 МБ | 1 |
| pm_rtt | 211 | 1 МБ | 1 |
| pm_top | 211 | 87 МБ | 1 |
| pm_trades | 211 | 62 МБ | 1 |
| rtds | 211 | 14 МБ | 1 |
| windows | 211 | 436 КБ | 191 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 34, всего 281
- Polymarket CLOB: TCP 5, TLS 37, всего 144
- Polymarket gamma: TCP 5, TLS 38, всего 50

## Последние строки журнала записи
```
06:43:27 [cex] Binance 145 сд. задержка p50/p90=144.3/145.3 мс | Coinbase 30 задержка p50=76.3 мс | смещение часов +19.5 мс | lag loop p99/max=2.2/2.2 мс
06:43:27 [cex] binance_futures 45 сд. p50=293.4 мс | bybit 4 сд. p50=113.1 мс | bybit_book 37 сд. p50=111.2 мс | bybit_spot 2 сд. p50=113.9 мс | bybit_spot_book 13 сд. p50=111.1 мс | okx 7 сд. p50=153.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:43:34 [pm] T- 85.6s Up 0.97/0.98 Down 0.02/0.03 ptb=81487.6 | CLOB 3395 сообщ., задержка p50/p90=44.6/103.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792219414442 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=2.0/2.0 мс
06:43:37 [cex] Binance 170 сд. задержка p50/p90=144.3/145.1 мс | Coinbase 31 задержка p50=76.3 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.1 мс
06:43:37 [cex] binance_futures 85 сд. p50=251.4 мс | bybit 18 сд. p50=113.1 мс | bybit_book 100 сд. p50=111.1 мс | bybit_spot 71 сд. p50=113.4 мс | bybit_spot_book 45 сд. p50=111.1 мс | okx 46 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:43:44 [pm] T- 75.6s Up 0.95/0.96 Down 0.04/0.05 ptb=81487.6 | CLOB 3393 сообщ., задержка p50/p90=42.8/53.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792219424444 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=1.4/1.6 мс
06:43:47 [cex] Binance 146 сд. задержка p50/p90=144.3/145.1 мс | Coinbase 29 задержка p50=76.2 мс | смещение часов +19.5 мс | lag loop p99/max=2.0/2.1 мс
06:43:47 [cex] binance_futures 46 сд. p50=293.3 мс | bybit 16 сд. p50=113.8 мс | bybit_book 73 сд. p50=111.1 мс | bybit_spot 2 сд. p50=112.8 мс | bybit_spot_book 16 сд. p50=111.3 мс | okx 4 сд. p50=153.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:43:54 [pm] T- 65.6s Up 0.47/0.51 Down 0.49/0.53 ptb=81487.6 | CLOB 3453 сообщ., задержка p50/p90=45.4/81.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792219434445 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=2.1/2.6 мс
06:43:57 [cex] Binance 219 сд. задержка p50/p90=144.4/147.6 мс | Coinbase 51 задержка p50=76.5 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.2 мс
06:43:57 [cex] binance_futures 130 сд. p50=148.9 мс | bybit 179 сд. p50=114.4 мс | bybit_book 147 сд. p50=111.1 мс | bybit_spot 173 сд. p50=114.6 мс | bybit_spot_book 86 сд. p50=111.0 мс | okx 132 сд. p50=155.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:44:04 [pm] T- 55.6s Up 0.99/n/a Down n/a/0.01 ptb=81487.6 | CLOB 10083 сообщ., задержка p50/p90=201.3/445.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792219444447 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=5.4/17.0 мс
06:44:07 [cex] Binance 313 сд. задержка p50/p90=167.7/180.3 мс | Coinbase 108 задержка p50=79.1 мс | смещение часов +19.5 мс | lag loop p99/max=4.0/7.5 мс
06:44:07 [cex] binance_futures 238 сд. p50=151.9 мс | bybit 185 сд. p50=115.6 мс | bybit_book 67 сд. p50=111.2 мс | bybit_spot 122 сд. p50=116.7 мс | bybit_spot_book 44 сд. p50=111.1 мс | okx 180 сд. p50=419.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:44:14 [pm] T- 45.6s Up 0.99/n/a Down n/a/0.01 ptb=81487.6 | CLOB 1842 сообщ., задержка p50/p90=51.1/184.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792219454448 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=1.8/2.1 мс
```

Представлено версией кода: 8083be6; python 3.12.3
