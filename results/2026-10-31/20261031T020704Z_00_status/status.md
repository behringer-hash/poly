# Состояние сервера записи

Время (UTC): 2026-10-31 02:07:04

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 2 days, 18 hours, 43 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         678         311           1        1106        1227
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.12 / 0.24 / 0.18

## Данные
- файлов: 5849, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 37 МБ | 1 |
| bn_book | 242 | 3 МБ | 21 |
| bnf_agg | 242 | 52 МБ | 1 |
| bnf_book | 110 | 768 МБ | 0 |
| bnf_liq | 211 | 150 КБ | 248 |
| by_book1 | 242 | 114 МБ | 1 |
| by_liq | 225 | 119 КБ | 175 |
| by_trade | 242 | 35 МБ | 1 |
| bys_book1 | 242 | 85 МБ | 1 |
| bys_trade | 242 | 35 МБ | 1 |
| cb_ticker | 242 | 33 МБ | 1 |
| clock | 242 | 187 КБ | 49 |
| clock_pm | 242 | 187 КБ | 26 |
| events | 223 | 71 КБ | 1449 |
| events_pm | 241 | 86 КБ | 1119 |
| health_cex | 242 | 3 МБ | 7 |
| health_feeds | 242 | 8 МБ | 7 |
| health_pm | 242 | 3 МБ | 6 |
| ok_trade | 242 | 46 МБ | 1 |
| pm_depth | 242 | 49 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 6 |
| pm_top | 242 | 99 МБ | 2 |
| pm_trades | 241 | 71 МБ | 2 |
| rtds | 242 | 15 МБ | 2 |
| windows | 242 | 497 КБ | 120 |

Дни с данными: 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 6, TLS 118, всего 852
- Polymarket CLOB: TCP 8, TLS 104, всего 143
- Polymarket gamma: TCP 5, TLS 109, всего 116

## Последние строки журнала записи
```
02:06:17 [cex] Binance 36 сд. задержка p50/p90=144.9/147.6 мс | Coinbase 50 задержка p50=89.7 мс | смещение часов +19.7 мс | lag loop p99/max=2.1/2.1 мс
02:06:17 [cex] binance_futures 120 сд. p50=147.5 мс | bybit 87 сд. p50=113.4 мс | bybit_book 362 сд. p50=111.2 мс | bybit_spot 94 сд. p50=114.0 мс | bybit_spot_book 420 сд. p50=111.3 мс | okx 20 сд. p50=146.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1533 сд. p50=144.5 мс
02:06:17 [pm] T-222.6s Up 0.62/0.63 Down 0.37/0.38 ptb=77249.9 | CLOB 4088 сообщ., задержка p50/p90=34.8/38.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793412377408 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.3 мс | lag loop p99/max=1.9/2.0 мс
02:06:27 [cex] Binance 45 сд. задержка p50/p90=143.9/145.2 мс | Coinbase 32 задержка p50=89.2 мс | смещение часов +19.7 мс | lag loop p99/max=2.1/2.1 мс
02:06:27 [cex] binance_futures 72 сд. p50=148.3 мс | bybit 50 сд. p50=113.1 мс | bybit_book 250 сд. p50=111.1 мс | bybit_spot 105 сд. p50=113.6 мс | bybit_spot_book 317 сд. p50=111.2 мс | okx 34 сд. p50=146.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3091 сд. p50=145.1 мс
02:06:27 [pm] T-212.6s Up 0.67/0.68 Down 0.32/0.33 ptb=77249.9 | CLOB 5416 сообщ., задержка p50/p90=35.2/39.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793412387409 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.3 мс | lag loop p99/max=2.0/2.6 мс
02:06:37 [cex] Binance 98 сд. задержка p50/p90=144.3/148.7 мс | Coinbase 37 задержка p50=89.6 мс | смещение часов +19.7 мс | lag loop p99/max=2.1/2.2 мс
02:06:37 [cex] binance_futures 90 сд. p50=149.2 мс | bybit 72 сд. p50=114.4 мс | bybit_book 315 сд. p50=111.2 мс | bybit_spot 147 сд. p50=115.8 мс | bybit_spot_book 500 сд. p50=111.2 мс | okx 88 сд. p50=146.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2390 сд. p50=145.4 мс
02:06:37 [pm] T-202.6s Up 0.76/0.77 Down 0.23/0.24 ptb=77249.9 | CLOB 3691 сообщ., задержка p50/p90=38.8/50.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793412397410 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.3 мс | lag loop p99/max=2.0/2.3 мс
02:06:47 [cex] Binance 164 сд. задержка p50/p90=144.4/148.5 мс | Coinbase 61 задержка p50=90.3 мс | смещение часов +19.7 мс | lag loop p99/max=2.1/4.8 мс
02:06:47 [cex] binance_futures 186 сд. p50=149.1 мс | bybit 165 сд. p50=118.9 мс | bybit_book 322 сд. p50=111.1 мс | bybit_spot 357 сд. p50=114.4 мс | bybit_spot_book 431 сд. p50=111.2 мс | okx 122 сд. p50=147.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 6745 сд. p50=144.8 мс
02:06:47 [pm] T-192.6s Up 0.79/0.80 Down 0.20/0.21 ptb=77249.9 | CLOB 4728 сообщ., задержка p50/p90=36.1/37.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793412407411 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.3 мс | lag loop p99/max=1.4/2.1 мс
02:06:57 [cex] Binance 29 сд. задержка p50/p90=143.9/144.9 мс | Coinbase 34 задержка p50=89.5 мс | смещение часов +19.7 мс | lag loop p99/max=2.1/2.1 мс
02:06:57 [cex] binance_futures 28 сд. p50=293.3 мс | bybit 2 сд. p50=112.8 мс | bybit_book 206 сд. p50=111.2 мс | bybit_spot 27 сд. p50=113.6 мс | bybit_spot_book 263 сд. p50=111.3 мс | okx 20 сд. p50=145.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 866 сд. p50=144.2 мс
02:06:57 [pm] T-182.6s Up 0.81/0.82 Down 0.18/0.19 ptb=77249.9 | CLOB 3687 сообщ., задержка p50/p90=35.9/36.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793412417413 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.3 мс | lag loop p99/max=2.1/2.2 мс
```

Представлено версией кода: fcaf736; python 3.12.3
