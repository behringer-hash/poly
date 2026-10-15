# Состояние сервера записи

Время (UTC): 2026-10-15 09:22:36

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 1 hour, 58 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         677         425           2        1052        1228
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.30 / 0.18 / 0.17

## Данные
- файлов: 4176, всего 999 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 166 | 22 МБ | 1 |
| bn_book | 166 | 2 МБ | 1 |
| bnf_agg | 166 | 33 МБ | 1 |
| bnf_book | 118 | 557 МБ | 171250 |
| bnf_depth5 | 118 | 41 МБ | 171327 |
| bnf_liq | 148 | 99 КБ | 3029 |
| bs_trade | 118 | 1 МБ | 171246 |
| by_book1 | 166 | 70 МБ | 1 |
| by_liq | 146 | 82 КБ | 726 |
| by_trade | 166 | 22 МБ | 1 |
| bys_book1 | 50 | 19 МБ | 1 |
| bys_trade | 50 | 8 МБ | 1 |
| cb_ticker | 166 | 20 МБ | 1 |
| clock | 166 | 128 КБ | 38 |
| clock_pm | 166 | 128 КБ | 36 |
| events | 157 | 51 КБ | 586 |
| events_pm | 166 | 59 КБ | 879 |
| health_cex | 166 | 2 МБ | 9 |
| health_feeds | 166 | 6 МБ | 9 |
| health_pm | 166 | 2 МБ | 6 |
| kr_trade | 118 | 3 МБ | 171246 |
| ok_trade | 165 | 29 МБ | 1 |
| pm_depth | 166 | 33 МБ | 0 |
| pm_rtt | 166 | 1 МБ | 0 |
| pm_top | 166 | 67 МБ | 0 |
| pm_trades | 166 | 49 МБ | 0 |
| rtds | 166 | 11 МБ | 0 |
| windows | 166 | 342 КБ | 333 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 53, всего 303
- Polymarket CLOB: TCP 6, TLS 52, всего 93
- Polymarket gamma: TCP 5, TLS 46, всего 58

## Последние строки журнала записи
```
09:21:49 [pm] T-190.6s Up 0.77/0.78 Down 0.22/0.23 ptb=81170.3 | CLOB 3730 сообщ., задержка p50/p90=43.7/45.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792056109406 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.8/1.8 мс
09:21:56 [cex] Binance 47 сд. задержка p50/p90=146.3/146.7 мс | Coinbase 28 задержка p50=78.7 мс | смещение часов +21.0 мс | lag loop p99/max=2.2/2.3 мс
09:21:56 [cex] binance_futures 38 сд. p50=204.1 мс | bybit 27 сд. p50=114.7 мс | bybit_book 144 сд. p50=112.8 мс | bybit_spot 33 сд. p50=114.7 мс | bybit_spot_book 67 сд. p50=112.5 мс | okx 138 сд. p50=156.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:21:59 [pm] T-180.6s Up 0.88/0.89 Down 0.11/0.12 ptb=81170.3 | CLOB 9092 сообщ., задержка p50/p90=45.1/147.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792056119407 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=2.0/4.5 мс
09:22:06 [cex] Binance 238 сд. задержка p50/p90=146.5/150.2 мс | Coinbase 97 задержка p50=77.9 мс | смещение часов +19.4 мс | lag loop p99/max=5.2/9.5 мс
09:22:06 [cex] binance_futures 393 сд. p50=146.7 мс | bybit 632 сд. p50=116.3 мс | bybit_book 308 сд. p50=111.3 мс | bybit_spot 357 сд. p50=115.2 мс | bybit_spot_book 178 сд. p50=111.0 мс | okx 602 сд. p50=161.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:22:09 [pm] T-170.6s Up 0.81/0.83 Down 0.17/0.19 ptb=81170.3 | CLOB 8244 сообщ., задержка p50/p90=44.4/51.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792056129408 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=2.8/2.8 мс
09:22:16 [cex] Binance 164 сд. задержка p50/p90=144.2/145.0 мс | Coinbase 47 задержка p50=77.3 мс | смещение часов +19.4 мс | lag loop p99/max=2.1/2.2 мс
09:22:16 [cex] binance_futures 153 сд. p50=144.6 мс | bybit 275 сд. p50=113.5 мс | bybit_book 213 сд. p50=111.2 мс | bybit_spot 204 сд. p50=113.5 мс | bybit_spot_book 120 сд. p50=110.8 мс | okx 143 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:22:19 [pm] T-160.6s Up 0.66/0.67 Down 0.33/0.34 ptb=81170.3 | CLOB 10484 сообщ., задержка p50/p90=43.8/48.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792056139410 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.7/2.1 мс
09:22:26 [cex] Binance 71 сд. задержка p50/p90=143.9/145.0 мс | Coinbase 24 задержка p50=76.7 мс | смещение часов +19.4 мс | lag loop p99/max=2.1/2.3 мс
09:22:26 [cex] binance_futures 74 сд. p50=144.5 мс | bybit 19 сд. p50=113.4 мс | bybit_book 105 сд. p50=111.0 мс | bybit_spot 51 сд. p50=113.8 мс | bybit_spot_book 53 сд. p50=110.8 мс | okx 40 сд. p50=152.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:22:29 [pm] T-150.6s Up 0.59/0.60 Down 0.40/0.41 ptb=81170.3 | CLOB 8127 сообщ., задержка p50/p90=44.1/49.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792056149411 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=2.0/2.1 мс
09:22:36 [cex] Binance 63 сд. задержка p50/p90=144.0/144.6 мс | Coinbase 39 задержка p50=77.1 мс | смещение часов +19.4 мс | lag loop p99/max=1.9/2.0 мс
09:22:36 [cex] binance_futures 56 сд. p50=144.7 мс | bybit 38 сд. p50=113.7 мс | bybit_book 109 сд. p50=111.1 мс | bybit_spot 120 сд. p50=113.3 мс | bybit_spot_book 104 сд. p50=110.8 мс | okx 61 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: ec1316a; python 3.12.3
