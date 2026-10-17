# Состояние сервера записи

Время (UTC): 2026-10-17 21:07:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 13 hours, 43 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         801         986           2         405        1104
Swap:           2047         236        1811
```
- нагрузка CPU (1/5/15 мин): 0.08 / 0.17 / 0.18

## Данные
- файлов: 5597, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 226 | 30 МБ | 0 |
| bn_book | 226 | 3 МБ | 99 |
| bnf_agg | 226 | 45 МБ | 0 |
| bnf_book | 118 | 557 МБ | 386352 |
| bnf_depth5 | 118 | 41 МБ | 386428 |
| bnf_liq | 196 | 132 КБ | 10154 |
| bs_trade | 118 | 1 МБ | 386348 |
| by_book1 | 226 | 94 МБ | 0 |
| by_liq | 201 | 106 КБ | 204 |
| by_trade | 226 | 29 МБ | 0 |
| bys_book1 | 110 | 38 МБ | 0 |
| bys_trade | 110 | 15 МБ | 5 |
| cb_ticker | 226 | 28 МБ | 0 |
| clock | 226 | 174 КБ | 44 |
| clock_pm | 226 | 174 КБ | 10 |
| events | 215 | 70 КБ | 364 |
| events_pm | 226 | 82 КБ | 104 |
| health_cex | 226 | 2 МБ | 5 |
| health_feeds | 226 | 8 МБ | 5 |
| health_pm | 226 | 2 МБ | 6 |
| kr_trade | 118 | 3 МБ | 386348 |
| ok_trade | 225 | 39 МБ | 0 |
| pm_depth | 226 | 45 МБ | -0 |
| pm_rtt | 226 | 1 МБ | 4 |
| pm_top | 226 | 91 МБ | -0 |
| pm_trades | 226 | 66 МБ | -0 |
| rtds | 226 | 14 МБ | -0 |
| windows | 226 | 464 КБ | 94 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 42, всего 292
- Polymarket CLOB: TCP 5, TLS 50, всего 95
- Polymarket gamma: TCP 7, TLS 66, всего 77

## Последние строки журнала записи
```
21:06:52 [pm] T-187.8s Up 0.49/0.50 Down 0.50/0.51 ptb=81561.9 | CLOB 2276 сообщ., задержка p50/p90=38.2/46.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792271212177 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=2.0/2.1 мс
21:06:53 [cex] Binance 6 сд. задержка p50/p90=144.7/144.9 мс | Coinbase 3 задержка p50=79.4 мс | смещение часов +21.0 мс | lag loop p99/max=2.2/2.2 мс
21:06:53 [cex] binance_futures 18 сд. p50=295.1 мс | bybit 9 сд. p50=114.7 мс | bybit_book 92 сд. p50=113.1 мс | bybit_spot 4 сд. p50=114.9 мс | bybit_spot_book 78 сд. p50=112.7 мс | okx 8 сд. p50=154.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:07:02 [pm] T-177.8s Up 0.51/0.52 Down 0.48/0.49 ptb=81561.9 | CLOB 4550 сообщ., задержка p50/p90=38.1/39.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792271222179 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=1.5/1.8 мс
21:07:03 [cex] Binance 5 сд. задержка p50/p90=143.2/144.3 мс | Coinbase 8 задержка p50=75.1 мс | смещение часов +19.4 мс | lag loop p99/max=2.2/2.3 мс
21:07:03 [cex] binance_futures 20 сд. p50=293.6 мс | bybit 4 сд. p50=113.3 мс | bybit_book 95 сд. p50=111.6 мс | bybit_spot 1 сд. p50=113.5 мс | bybit_spot_book 16 сд. p50=111.4 мс | okx 6 сд. p50=152.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:07:12 [pm] T-167.8s Up 0.54/0.55 Down 0.45/0.46 ptb=81561.9 | CLOB 3677 сообщ., задержка p50/p90=38.1/39.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792271232181 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.1/2.1 мс
21:07:13 [cex] Binance 10 сд. задержка p50/p90=143.1/143.4 мс | Coinbase 17 задержка p50=77.8 мс | смещение часов +19.4 мс | lag loop p99/max=2.2/2.2 мс
21:07:13 [cex] binance_futures 8 сд. p50=293.9 мс | bybit 10 сд. p50=113.0 мс | bybit_book 105 сд. p50=111.6 мс | bybit_spot 10 сд. p50=113.0 мс | bybit_spot_book 34 сд. p50=111.3 мс | okx 12 сд. p50=152.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:07:22 [pm] T-157.8s Up 0.49/0.50 Down 0.50/0.51 ptb=81561.9 | CLOB 5222 сообщ., задержка p50/p90=186.4/261.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792271242182 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.5/1.8 мс
21:07:23 [cex] Binance 13 сд. задержка p50/p90=143.1/144.1 мс | Coinbase 17 задержка p50=289.2 мс | смещение часов +19.4 мс | lag loop p99/max=2.2/2.2 мс
21:07:23 [cex] binance_futures 12 сд. p50=294.0 мс | bybit 8 сд. p50=112.9 мс | bybit_book 90 сд. p50=111.5 мс | bybit_spot 1 сд. p50=112.8 мс | bybit_spot_book 56 сд. p50=111.3 мс | okx 10 сд. p50=153.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:07:32 [pm] T-147.8s Up 0.46/0.47 Down 0.53/0.54 ptb=81561.9 | CLOB 5373 сообщ., задержка p50/p90=41.7/68.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792271252184 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.4 мс | lag loop p99/max=1.6/1.9 мс
21:07:33 [cex] Binance 8 сд. задержка p50/p90=143.3/144.3 мс | Coinbase 11 задержка p50=76.5 мс | смещение часов +19.4 мс | lag loop p99/max=2.0/2.0 мс
21:07:33 [cex] binance_futures 19 сд. p50=293.6 мс | bybit 47 сд. p50=113.6 мс | bybit_book 103 сд. p50=111.5 мс | bybit_spot 6 сд. p50=113.3 мс | bybit_spot_book 30 сд. p50=111.4 мс | okx 7 сд. p50=152.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: b24b4e3; python 3.12.3
