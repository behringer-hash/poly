# Состояние сервера записи

Время (UTC): 2026-10-17 10:51:12

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 3 hours, 27 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         860         519           2         813        1045
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.34 / 0.20 / 0.19

## Данные
- файлов: 5337, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 215 | 29 МБ | 1 |
| bn_book | 215 | 3 МБ | 3 |
| bnf_agg | 215 | 44 МБ | 1 |
| bnf_book | 118 | 557 МБ | 349366 |
| bnf_depth5 | 118 | 41 МБ | 349442 |
| bnf_liq | 189 | 128 КБ | 130 |
| bs_trade | 118 | 1 МБ | 349362 |
| by_book1 | 215 | 93 МБ | 1 |
| by_liq | 190 | 104 КБ | 3023 |
| by_trade | 215 | 29 МБ | 1 |
| bys_book1 | 99 | 38 МБ | 1 |
| bys_trade | 99 | 15 МБ | 1 |
| cb_ticker | 215 | 27 МБ | 1 |
| clock | 215 | 167 КБ | 3 |
| clock_pm | 215 | 167 КБ | 30 |
| events | 204 | 67 КБ | 1166 |
| events_pm | 215 | 79 КБ | 38 |
| health_cex | 215 | 2 МБ | 3 |
| health_feeds | 215 | 7 МБ | 3 |
| health_pm | 215 | 2 МБ | 4 |
| kr_trade | 118 | 3 МБ | 349362 |
| ok_trade | 214 | 39 МБ | 1 |
| pm_depth | 215 | 44 МБ | 0 |
| pm_rtt | 215 | 1 МБ | 2 |
| pm_top | 215 | 89 МБ | 0 |
| pm_trades | 215 | 64 МБ | 0 |
| rtds | 215 | 14 МБ | 0 |
| windows | 215 | 446 КБ | 127 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 43, всего 293
- Polymarket CLOB: TCP 5, TLS 44, всего 86
- Polymarket gamma: TCP 18, TLS 52, всего 64

## Последние строки журнала записи
```
10:50:26 [pm] T-273.4s Up 0.40/0.41 Down 0.59/0.60 ptb=81548.2 | CLOB 5415 сообщ., задержка p50/p90=40.4/42.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792234226628 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.0/2.3 мс
10:50:29 [cex] Binance 77 сд. задержка p50/p90=145.7/146.6 мс | Coinbase 38 задержка p50=78.3 мс | смещение часов +21.4 мс | lag loop p99/max=2.1/2.2 мс
10:50:29 [cex] binance_futures 68 сд. p50=248.6 мс | bybit 42 сд. p50=114.9 мс | bybit_book 96 сд. p50=113.1 мс | bybit_spot 111 сд. p50=116.0 мс | bybit_spot_book 95 сд. p50=112.8 мс | okx 27 сд. p50=157.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:50:36 [pm] T-263.4s Up 0.48/0.49 Down 0.51/0.52 ptb=81548.2 | CLOB 6594 сообщ., задержка p50/p90=40.3/66.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792234236630 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.9/13.2 мс
10:50:39 [cex] Binance 13 сд. задержка p50/p90=145.8/146.1 мс | Coinbase 29 задержка p50=78.3 мс | смещение часов +21.4 мс | lag loop p99/max=2.1/2.2 мс
10:50:39 [cex] binance_futures 34 сд. p50=146.6 мс | bybit 29 сд. p50=115.0 мс | bybit_book 160 сд. p50=113.1 мс | bybit_spot 78 сд. p50=115.4 мс | bybit_spot_book 112 сд. p50=112.8 мс | okx 24 сд. p50=156.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:50:46 [pm] T-253.4s Up 0.52/0.53 Down 0.47/0.48 ptb=81548.2 | CLOB 5237 сообщ., задержка p50/p90=39.9/59.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792234246631 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=1.9/2.0 мс
10:50:49 [cex] Binance 19 сд. задержка p50/p90=145.9/146.0 мс | Coinbase 32 задержка p50=77.4 мс | смещение часов +21.4 мс | lag loop p99/max=2.3/2.4 мс
10:50:49 [cex] binance_futures 10 сд. p50=295.1 мс | bybit 27 сд. p50=114.8 мс | bybit_book 118 сд. p50=113.2 мс | bybit_spot 4 сд. p50=115.2 мс | bybit_spot_book 152 сд. p50=112.8 мс | okx 28 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:50:56 [pm] T-243.4s Up 0.50/0.51 Down 0.49/0.50 ptb=81548.2 | CLOB 3909 сообщ., задержка p50/p90=39.0/40.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792234256633 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=2.2/2.3 мс
10:50:59 [cex] Binance 12 сд. задержка p50/p90=145.5/145.6 мс | Coinbase 26 задержка p50=77.6 мс | смещение часов +21.4 мс | lag loop p99/max=2.2/2.2 мс
10:50:59 [cex] binance_futures 7 сд. p50=294.8 мс | bybit 4 сд. p50=114.8 мс | bybit_book 93 сд. p50=113.2 мс | bybit_spot 7 сд. p50=115.5 мс | bybit_spot_book 204 сд. p50=112.9 мс | okx 7 сд. p50=156.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:51:06 [pm] T-233.4s Up 0.45/0.46 Down 0.54/0.55 ptb=81548.2 | CLOB 4333 сообщ., задержка p50/p90=39.2/40.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792234266635 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=2.1/3.9 мс
10:51:09 [cex] Binance 18 сд. задержка p50/p90=145.7/146.6 мс | Coinbase 30 задержка p50=77.5 мс | смещение часов +17.8 мс | lag loop p99/max=2.0/2.1 мс
10:51:09 [cex] binance_futures 9 сд. p50=295.4 мс | bybit 10 сд. p50=114.9 мс | bybit_book 122 сд. p50=113.2 мс | bybit_spot 9 сд. p50=116.5 мс | bybit_spot_book 238 сд. p50=112.8 мс | okx 8 сд. p50=156.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 8083be6; python 3.12.3
