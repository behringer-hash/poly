# Состояние сервера записи

Время (UTC): 2026-10-16 20:27:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 13 hours, 4 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         811         989           2         379        1094
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.47 / 0.33 / 0.29

## Данные
- файлов: 5009, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 201 | 28 МБ | 1 |
| bn_book | 201 | 3 МБ | 5 |
| bnf_agg | 201 | 43 МБ | 1 |
| bnf_book | 118 | 557 МБ | 297572 |
| bnf_depth5 | 118 | 41 МБ | 297648 |
| bnf_liq | 180 | 128 КБ | 1899 |
| bs_trade | 118 | 1 МБ | 297568 |
| by_book1 | 201 | 90 МБ | 1 |
| by_liq | 179 | 103 КБ | 1923 |
| by_trade | 201 | 28 МБ | 1 |
| bys_book1 | 85 | 35 МБ | 1 |
| bys_trade | 85 | 14 МБ | 1 |
| cb_ticker | 201 | 26 МБ | 1 |
| clock | 201 | 155 КБ | 34 |
| clock_pm | 201 | 155 КБ | 52 |
| events | 190 | 61 КБ | 63 |
| events_pm | 201 | 77 КБ | 58 |
| health_cex | 201 | 2 МБ | 3 |
| health_feeds | 201 | 7 МБ | 3 |
| health_pm | 201 | 2 МБ | 9 |
| kr_trade | 118 | 3 МБ | 297568 |
| ok_trade | 200 | 38 МБ | 1 |
| pm_depth | 201 | 40 МБ | 1 |
| pm_rtt | 201 | 1 МБ | 1 |
| pm_top | 201 | 83 МБ | 1 |
| pm_trades | 201 | 60 МБ | 1 |
| rtds | 201 | 13 МБ | 1 |
| windows | 201 | 415 КБ | 234 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 48, всего 297
- Polymarket CLOB: TCP 6, TLS 52, всего 93
- Polymarket gamma: TCP 5, TLS 59, всего 71

## Последние строки журнала записи
```
20:27:13 [cex] Binance 30 сд. задержка p50/p90=142.7/143.8 мс | Coinbase 69 задержка p50=74.2 мс | смещение часов +18.3 мс | lag loop p99/max=2.1/2.2 мс
20:27:13 [cex] binance_futures 18 сд. p50=213.2 мс | bybit 41 сд. p50=112.7 мс | bybit_book 119 сд. p50=110.3 мс | bybit_spot 115 сд. p50=111.9 мс | bybit_spot_book 52 сд. p50=110.4 мс | okx 35 сд. p50=153.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
20:27:18 [pm] T-161.1s Up 0.53/0.54 Down 0.46/0.47 ptb=81494.8 | CLOB 8260 сообщ., задержка p50/p90=46.7/49.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792182438885 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.5/1.8 мс
20:27:23 [cex] Binance 14 сд. задержка p50/p90=142.7/143.0 мс | Coinbase 32 задержка p50=74.1 мс | смещение часов +18.3 мс | lag loop p99/max=2.1/2.2 мс
20:27:23 [cex] binance_futures 12 сд. p50=292.1 мс | bybit 18 сд. p50=112.7 мс | bybit_book 115 сд. p50=110.3 мс | bybit_spot 4 сд. p50=111.7 мс | bybit_spot_book 34 сд. p50=110.5 мс | okx 19 сд. p50=152.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
20:27:28 [pm] T-151.1s Up 0.51/0.52 Down 0.48/0.49 ptb=81494.8 | CLOB 8436 сообщ., задержка p50/p90=47.9/60.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792182448886 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.2/1.2 мс
20:27:33 [cex] Binance 9 сд. задержка p50/p90=143.1/144.1 мс | Coinbase 41 задержка p50=74.6 мс | смещение часов +18.8 мс | lag loop p99/max=2.1/2.1 мс
20:27:33 [cex] binance_futures 5 сд. p50=292.3 мс | bybit 33 сд. p50=112.9 мс | bybit_book 100 сд. p50=110.8 мс | bybit_spot 1 сд. p50=112.0 мс | bybit_spot_book 43 сд. p50=110.8 мс | okx 19 сд. p50=152.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
20:27:38 [pm] T-141.1s Up 0.46/0.47 Down 0.53/0.54 ptb=81494.8 | CLOB 7278 сообщ., задержка p50/p90=47.1/50.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792182458888 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.1/1.2 мс
20:27:43 [cex] Binance 26 сд. задержка p50/p90=144.4/144.7 мс | Coinbase 65 задержка p50=80.1 мс | смещение часов +18.8 мс | lag loop p99/max=1.9/2.0 мс
20:27:43 [cex] binance_futures 33 сд. p50=144.0 мс | bybit 42 сд. p50=112.8 мс | bybit_book 100 сд. p50=110.9 мс | bybit_spot 152 сд. p50=112.6 мс | bybit_spot_book 83 сд. p50=110.8 мс | okx 14 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
20:27:48 [pm] T-131.1s Up 0.41/0.42 Down 0.58/0.59 ptb=81494.8 | CLOB 13526 сообщ., задержка p50/p90=47.5/52.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792182468889 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=1.4/1.9 мс
20:27:53 [cex] Binance 19 сд. задержка p50/p90=143.2/144.0 мс | Coinbase 44 задержка p50=75.6 мс | смещение часов +18.8 мс | lag loop p99/max=2.1/2.1 мс
20:27:53 [cex] binance_futures 17 сд. p50=292.1 мс | bybit 39 сд. p50=112.6 мс | bybit_book 108 сд. p50=110.9 мс | bybit_spot 115 сд. p50=112.8 мс | bybit_spot_book 99 сд. p50=110.8 мс | okx 63 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
20:27:58 [pm] T-121.1s Up 0.57/0.58 Down 0.42/0.43 ptb=81494.8 | CLOB 11464 сообщ., задержка p50/p90=46.7/48.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792182478891 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=1.7/1.8 мс
```

Представлено версией кода: 8083be6; python 3.12.3
