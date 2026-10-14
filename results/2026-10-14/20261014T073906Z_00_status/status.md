# Состояние сервера записи

Время (UTC): 2026-10-14 07:39:06

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 15 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         567         522           2        1006        1338
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.15 / 0.17 / 0.17

## Данные
- файлов: 3555, всего 915 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 140 | 17 МБ | 2 |
| bn_book | 140 | 2 МБ | 6 |
| bnf_agg | 140 | 26 МБ | 2 |
| bnf_book | 118 | 557 МБ | 78640 |
| bnf_depth5 | 118 | 41 МБ | 78717 |
| bnf_liq | 123 | 74 КБ | 4998 |
| bs_trade | 118 | 1 МБ | 78636 |
| by_book1 | 140 | 55 МБ | 2 |
| by_liq | 121 | 62 КБ | 1664 |
| by_trade | 140 | 17 МБ | 4 |
| bys_book1 | 24 | 8 МБ | 2 |
| bys_trade | 24 | 4 МБ | 2 |
| cb_ticker | 140 | 15 МБ | 4 |
| clock | 140 | 108 КБ | 26 |
| clock_pm | 140 | 108 КБ | 25 |
| events | 132 | 45 КБ | 107 |
| events_pm | 140 | 52 КБ | 225 |
| health_cex | 140 | 1 МБ | 2 |
| health_feeds | 140 | 5 МБ | 2 |
| health_pm | 140 | 1 МБ | 9 |
| kr_trade | 118 | 3 МБ | 78636 |
| ok_trade | 139 | 23 МБ | 2 |
| pm_depth | 140 | 28 МБ | 1 |
| pm_rtt | 140 | 948 КБ | 5 |
| pm_top | 140 | 57 МБ | 1 |
| pm_trades | 140 | 41 МБ | 1 |
| rtds | 140 | 9 МБ | 1 |
| windows | 140 | 290 КБ | 1 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 290
- Polymarket CLOB: TCP 8, TLS 54, всего 98
- Polymarket gamma: TCP 5, TLS 45, всего 65

## Последние строки журнала записи
```
07:38:24 [cex] Binance 85 сд. задержка p50/p90=145.3/145.7 мс | Coinbase 41 задержка p50=79.9 мс | смещение часов +20.2 мс | lag loop p99/max=2.1/2.2 мс
07:38:24 [cex] binance_futures 50 сд. p50=145.6 мс | bybit 66 сд. p50=114.6 мс | bybit_book 187 сд. p50=112.0 мс | bybit_spot 31 сд. p50=113.8 мс | bybit_spot_book 276 сд. p50=111.6 мс | okx 5 сд. p50=147.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:38:26 [pm] T- 93.7s Up 0.73/0.74 Down 0.26/0.27 ptb=83344.6 | CLOB 10096 сообщ., задержка p50/p90=40.8/45.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791963506268 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=1.5/1.8 мс
07:38:34 [cex] Binance 30 сд. задержка p50/p90=145.3/146.2 мс | Coinbase 32 задержка p50=80.2 мс | смещение часов +20.2 мс | lag loop p99/max=2.0/2.2 мс
07:38:34 [cex] binance_futures 58 сд. p50=146.4 мс | bybit 56 сд. p50=114.0 мс | bybit_book 163 сд. p50=111.9 мс | bybit_spot 61 сд. p50=114.7 мс | bybit_spot_book 209 сд. p50=111.6 мс | okx 9 сд. p50=147.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:38:36 [pm] T- 83.7s Up 0.81/0.82 Down 0.18/0.19 ptb=83344.6 | CLOB 9705 сообщ., задержка p50/p90=40.8/43.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791963516269 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=1.3/1.3 мс
07:38:44 [cex] Binance 30 сд. задержка p50/p90=146.9/147.9 мс | Coinbase 31 задержка p50=81.5 мс | смещение часов +21.9 мс | lag loop p99/max=2.0/2.1 мс
07:38:44 [cex] binance_futures 42 сд. p50=150.6 мс | bybit 49 сд. p50=114.7 мс | bybit_book 147 сд. p50=113.5 мс | bybit_spot 14 сд. p50=115.2 мс | bybit_spot_book 221 сд. p50=112.1 мс | okx 5 сд. p50=149.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:38:46 [pm] T- 73.7s Up 0.77/0.78 Down 0.22/0.23 ptb=83344.6 | CLOB 9549 сообщ., задержка p50/p90=41.4/44.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791963526271 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.1/2.4 мс
07:38:54 [cex] Binance 36 сд. задержка p50/p90=147.0/147.4 мс | Coinbase 28 задержка p50=82.5 мс | смещение часов +21.9 мс | lag loop p99/max=2.2/2.3 мс
07:38:54 [cex] binance_futures 36 сд. p50=295.2 мс | bybit 8 сд. p50=115.7 мс | bybit_book 114 сд. p50=113.7 мс | bybit_spot 8 сд. p50=115.9 мс | bybit_spot_book 33 сд. p50=113.5 мс | okx 10 сд. p50=149.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:38:56 [pm] T- 63.7s Up 0.70/0.71 Down 0.29/0.30 ptb=83344.6 | CLOB 7645 сообщ., задержка p50/p90=41.7/59.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791963536272 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=1.7/2.3 мс
07:39:04 [cex] Binance 93 сд. задержка p50/p90=147.1/148.2 мс | Coinbase 22 задержка p50=83.2 мс | смещение часов +21.9 мс | lag loop p99/max=2.1/3.1 мс
07:39:04 [cex] binance_futures 110 сд. p50=147.3 мс | bybit 86 сд. p50=116.9 мс | bybit_book 178 сд. p50=113.7 мс | bybit_spot 116 сд. p50=117.1 мс | bybit_spot_book 68 сд. p50=113.4 мс | okx 67 сд. p50=149.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:39:06 [pm] T- 53.7s Up 0.52/0.53 Down 0.47/0.48 ptb=83344.6 | CLOB 11306 сообщ., задержка p50/p90=41.1/42.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791963546273 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.0/4.3 мс
```

Представлено версией кода: ec1316a; python 3.12.3
