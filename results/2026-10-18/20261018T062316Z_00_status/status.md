# Состояние сервера записи

Время (UTC): 2026-10-18 06:23:16

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 22 hours, 59 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         858         509           2         826        1047
Swap:           2047         236        1811
```
- нагрузка CPU (1/5/15 мин): 0.42 / 0.24 / 0.20

## Данные
- файлов: 5809, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 235 | 30 МБ | 1 |
| bn_book | 235 | 3 МБ | 23 |
| bnf_agg | 235 | 46 МБ | 1 |
| bnf_book | 118 | 557 МБ | 419690 |
| bnf_depth5 | 118 | 41 МБ | 419767 |
| bnf_liq | 203 | 135 КБ | 2101 |
| bs_trade | 118 | 1 МБ | 419686 |
| by_book1 | 235 | 97 МБ | 1 |
| by_liq | 208 | 110 КБ | 2316 |
| by_trade | 235 | 30 МБ | 5 |
| bys_book1 | 119 | 40 МБ | 1 |
| bys_trade | 119 | 16 МБ | 1 |
| cb_ticker | 235 | 29 МБ | 1 |
| clock | 235 | 181 КБ | 45 |
| clock_pm | 235 | 181 КБ | 9 |
| events | 224 | 73 КБ | 264 |
| events_pm | 235 | 85 КБ | 67 |
| health_cex | 235 | 2 МБ | 9 |
| health_feeds | 235 | 8 МБ | 9 |
| health_pm | 235 | 2 МБ | 9 |
| kr_trade | 118 | 3 МБ | 419686 |
| ok_trade | 234 | 40 МБ | 1 |
| pm_depth | 235 | 47 МБ | 1 |
| pm_rtt | 235 | 2 МБ | 1 |
| pm_top | 235 | 95 МБ | 1 |
| pm_trades | 235 | 68 МБ | 1 |
| rtds | 235 | 15 МБ | 1 |
| windows | 235 | 484 КБ | 311 |

Дни с данными: 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 43, всего 291
- Polymarket CLOB: TCP 6, TLS 45, всего 87
- Polymarket gamma: TCP 5, TLS 64, всего 75

## Последние строки журнала записи
```
06:22:27 [cex] Binance 32 сд. задержка p50/p90=144.3/144.6 мс | Coinbase 13 задержка p50=79.1 мс | смещение часов +20.1 мс | lag loop p99/max=2.1/2.2 мс
06:22:27 [cex] binance_futures 76 сд. p50=145.5 мс | bybit 61 сд. p50=137.8 мс | bybit_book 66 сд. p50=112.0 мс | bybit_spot 151 сд. p50=114.4 мс | bybit_spot_book 75 сд. p50=111.6 мс | okx 49 сд. p50=153.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:22:37 [pm] T-142.9s Up 0.23/0.24 Down 0.76/0.77 ptb=81606.3 | CLOB 5534 сообщ., задержка p50/p90=49.3/232.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792304557083 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.0/2.0 мс
06:22:37 [cex] Binance 6 сд. задержка p50/p90=144.2/145.0 мс | Coinbase 14 задержка p50=79.7 мс | смещение часов +20.1 мс | lag loop p99/max=2.2/2.5 мс
06:22:37 [cex] binance_futures 16 сд. p50=293.4 мс | bybit 11 сд. p50=113.4 мс | bybit_book 54 сд. p50=112.0 мс | bybit_spot 1 сд. p50=113.8 мс | bybit_spot_book 30 сд. p50=111.8 мс | okx 11 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:22:47 [pm] T-132.9s Up 0.17/0.18 Down 0.82/0.83 ptb=81606.3 | CLOB 7713 сообщ., задержка p50/p90=80.8/132.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792304567085 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.0/2.0 мс
06:22:47 [cex] Binance 18 сд. задержка p50/p90=144.2/145.1 мс | Coinbase 12 задержка p50=119.9 мс | смещение часов +20.1 мс | lag loop p99/max=2.0/2.0 мс
06:22:47 [cex] binance_futures 39 сд. p50=197.0 мс | bybit 28 сд. p50=124.0 мс | bybit_book 88 сд. p50=112.0 мс | bybit_spot 57 сд. p50=115.5 мс | bybit_spot_book 32 сд. p50=111.7 мс | okx 9 сд. p50=153.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:22:57 [pm] T-122.9s Up 0.28/0.29 Down 0.71/0.72 ptb=81606.3 | CLOB 9042 сообщ., задержка p50/p90=43.5/66.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792304577086 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.7/1.7 мс
06:22:57 [cex] Binance 20 сд. задержка p50/p90=144.4/145.0 мс | Coinbase 41 задержка p50=80.2 мс | смещение часов +20.1 мс | lag loop p99/max=2.2/2.2 мс
06:22:57 [cex] binance_futures 95 сд. p50=145.0 мс | bybit 56 сд. p50=121.0 мс | bybit_book 100 сд. p50=112.0 мс | bybit_spot 117 сд. p50=115.1 мс | bybit_spot_book 66 сд. p50=111.5 мс | okx 56 сд. p50=153.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:23:07 [pm] T-112.9s Up 0.22/0.23 Down 0.77/0.78 ptb=81606.3 | CLOB 9487 сообщ., задержка p50/p90=42.8/96.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792304587088 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=4.4/5.1 мс
06:23:07 [cex] Binance 8 сд. задержка p50/p90=144.2/144.5 мс | Coinbase 18 задержка p50=78.4 мс | смещение часов +20.1 мс | lag loop p99/max=2.0/2.1 мс
06:23:07 [cex] binance_futures 21 сд. p50=293.4 мс | bybit 55 сд. p50=114.3 мс | bybit_book 102 сд. p50=112.1 мс | bybit_spot 1 сд. p50=113.4 мс | bybit_spot_book 30 сд. p50=111.8 мс | okx 15 сд. p50=153.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:23:17 [pm] T-102.9s Up 0.38/0.39 Down 0.61/0.62 ptb=81606.3 | CLOB 5399 сообщ., задержка p50/p90=41.4/55.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792304597090 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.3/25.5 мс
```

Представлено версией кода: b24b4e3; python 3.12.3
