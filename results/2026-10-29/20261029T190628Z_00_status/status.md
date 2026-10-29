# Состояние сервера записи

Время (UTC): 2026-10-29 19:06:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 11 hours, 42 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         604         827           1         653        1301
Swap:           2047         320        1727
```
- нагрузка CPU (1/5/15 мин): 0.17 / 0.26 / 0.18

## Данные
- файлов: 5828, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 34 МБ | 0 |
| bn_book | 242 | 3 МБ | 0 |
| bnf_agg | 242 | 49 МБ | 0 |
| bnf_book | 79 | 470 МБ | 0 |
| bnf_liq | 212 | 135 КБ | 0 |
| by_book1 | 242 | 108 МБ | 0 |
| by_liq | 225 | 98 КБ | 587 |
| by_trade | 242 | 32 МБ | 0 |
| bys_book1 | 242 | 81 МБ | 0 |
| bys_trade | 242 | 32 МБ | 0 |
| cb_ticker | 242 | 31 МБ | 0 |
| clock | 242 | 187 КБ | 35 |
| clock_pm | 242 | 187 КБ | 4 |
| events | 231 | 73 КБ | 290 |
| events_pm | 241 | 85 КБ | 1451 |
| health_cex | 242 | 2 МБ | 2 |
| health_feeds | 242 | 8 МБ | 2 |
| health_pm | 242 | 3 МБ | 6 |
| ok_trade | 242 | 42 МБ | 0 |
| pm_depth | 242 | 49 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 0 |
| pm_top | 242 | 99 МБ | 0 |
| pm_trades | 241 | 71 МБ | 0 |
| rtds | 242 | 15 МБ | 0 |
| windows | 243 | 499 КБ | 295 |

Дни с данными: 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 36, всего 284
- Polymarket CLOB: TCP 6, TLS 45, всего 94
- Polymarket gamma: TCP 4, TLS 57, всего 63

## Последние строки журнала записи
```
19:05:40 [pm] T-259.2s Up 0.63/0.64 Down 0.36/0.37 ptb=80737.3 | CLOB 3585 сообщ., задержка p50/p90=45.7/75.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793300740821 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.8 мс | lag loop p99/max=1.8/2.1 мс
19:05:46 [cex] Binance 26 сд. задержка p50/p90=144.0/144.7 мс | Coinbase 76 задержка p50=80.7 мс | смещение часов +19.7 мс | lag loop p99/max=2.1/2.2 мс
19:05:46 [cex] binance_futures 68 сд. p50=152.3 мс | bybit 77 сд. p50=115.1 мс | bybit_book 208 сд. p50=111.0 мс | bybit_spot 93 сд. p50=114.7 мс | bybit_spot_book 94 сд. p50=111.9 мс | okx 109 сд. p50=156.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3351 сд. p50=144.8 мс
19:05:50 [pm] T-249.2s Up 0.64/0.65 Down 0.35/0.36 ptb=80737.3 | CLOB 5148 сообщ., задержка p50/p90=44.9/65.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793300750822 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.9 мс | lag loop p99/max=1.8/1.9 мс
19:05:56 [cex] Binance 22 сд. задержка p50/p90=145.1/146.0 мс | Coinbase 90 задержка p50=81.9 мс | смещение часов +20.8 мс | lag loop p99/max=2.2/3.7 мс
19:05:56 [cex] binance_futures 36 сд. p50=167.8 мс | bybit 71 сд. p50=114.3 мс | bybit_book 198 сд. p50=111.8 мс | bybit_spot 81 сд. p50=113.2 мс | bybit_spot_book 75 сд. p50=112.1 мс | okx 36 сд. p50=156.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1338 сд. p50=146.1 мс
19:06:00 [pm] T-239.2s Up 0.56/0.57 Down 0.43/0.44 ptb=80737.3 | CLOB 5312 сообщ., задержка p50/p90=45.8/80.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793300760823 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.8 мс | lag loop p99/max=2.1/12.2 мс
19:06:06 [cex] Binance 74 сд. задержка p50/p90=146.0/152.8 мс | Coinbase 83 задержка p50=81.9 мс | смещение часов +20.8 мс | lag loop p99/max=9.4/11.9 мс
19:06:06 [cex] binance_futures 98 сд. p50=154.3 мс | bybit 83 сд. p50=115.6 мс | bybit_book 202 сд. p50=112.2 мс | bybit_spot 342 сд. p50=115.5 мс | bybit_spot_book 124 сд. p50=113.1 мс | okx 119 сд. p50=159.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4294 сд. p50=145.5 мс
19:06:10 [pm] T-229.2s Up 0.47/0.48 Down 0.52/0.53 ptb=80737.3 | CLOB 6308 сообщ., задержка p50/p90=45.0/62.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793300770826 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.8 мс | lag loop p99/max=1.9/2.1 мс
19:06:16 [cex] Binance 47 сд. задержка p50/p90=145.2/145.8 мс | Coinbase 44 задержка p50=82.1 мс | смещение часов +20.8 мс | lag loop p99/max=1.9/2.0 мс
19:06:16 [cex] binance_futures 30 сд. p50=265.0 мс | bybit 89 сд. p50=114.3 мс | bybit_book 180 сд. p50=112.1 мс | bybit_spot 64 сд. p50=115.6 мс | bybit_spot_book 58 сд. p50=112.9 мс | okx 53 сд. p50=157.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1602 сд. p50=145.4 мс
19:06:20 [pm] T-219.2s Up 0.46/0.47 Down 0.53/0.54 ptb=80737.3 | CLOB 4268 сообщ., задержка p50/p90=44.6/47.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793300780827 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.9 мс | lag loop p99/max=1.8/1.8 мс
19:06:26 [cex] Binance 37 сд. задержка p50/p90=145.2/145.9 мс | Coinbase 67 задержка p50=81.8 мс | смещение часов +20.8 мс | lag loop p99/max=2.0/2.1 мс
19:06:26 [cex] binance_futures 20 сд. p50=294.2 мс | bybit 13 сд. p50=113.8 мс | bybit_book 115 сд. p50=112.0 мс | bybit_spot 61 сд. p50=114.7 мс | bybit_spot_book 46 сд. p50=113.0 мс | okx 107 сд. p50=157.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 810 сд. p50=145.3 мс
```

Представлено версией кода: b8783c2; python 3.12.3
