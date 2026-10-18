# Состояние сервера записи

Время (UTC): 2026-10-18 14:36:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 7 hours, 13 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         539        1260           2         291        1366
Swap:           2047         255        1792
```
- нагрузка CPU (1/5/15 мин): 0.22 / 0.13 / 0.15

## Данные
- файлов: 5999, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 243 | 32 МБ | 1 |
| bn_book | 243 | 3 МБ | 5 |
| bnf_agg | 243 | 50 МБ | 1 |
| bnf_book | 118 | 557 МБ | 449312 |
| bnf_depth5 | 118 | 41 МБ | 449388 |
| bnf_liq | 209 | 139 КБ | 285 |
| bs_trade | 118 | 1 МБ | 449308 |
| by_book1 | 243 | 103 МБ | 1 |
| by_liq | 216 | 115 КБ | 287 |
| by_trade | 243 | 33 МБ | 1 |
| bys_book1 | 127 | 45 МБ | 1 |
| bys_trade | 127 | 18 МБ | 3 |
| cb_ticker | 243 | 30 МБ | 1 |
| clock | 243 | 188 КБ | 39 |
| clock_pm | 243 | 188 КБ | 3 |
| events | 232 | 75 КБ | 1044 |
| events_pm | 243 | 87 КБ | 1238 |
| health_cex | 243 | 2 МБ | 7 |
| health_feeds | 243 | 8 МБ | 7 |
| health_pm | 243 | 3 МБ | 5 |
| kr_trade | 118 | 3 МБ | 449308 |
| ok_trade | 242 | 43 МБ | 1 |
| pm_depth | 243 | 49 МБ | 1 |
| pm_rtt | 243 | 2 МБ | 3 |
| pm_top | 243 | 99 МБ | 1 |
| pm_trades | 243 | 70 МБ | 1 |
| rtds | 243 | 16 МБ | 1 |
| windows | 243 | 502 КБ | 263 |

Дни с данными: 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 8, TLS 45, всего 294
- Polymarket CLOB: TCP 5, TLS 38, всего 89
- Polymarket gamma: TCP 5, TLS 38, всего 49

## Последние строки журнала записи
```
14:36:10 [cex] Binance 80 сд. задержка p50/p90=145.7/146.9 мс | Coinbase 60 задержка p50=80.1 мс | смещение часов +21.6 мс | lag loop p99/max=3.2/3.8 мс
14:36:10 [cex] binance_futures 250 сд. p50=146.8 мс | bybit 298 сд. p50=118.2 мс | bybit_book 308 сд. p50=113.1 мс | bybit_spot 190 сд. p50=115.7 мс | bybit_spot_book 180 сд. p50=113.2 мс | okx 192 сд. p50=155.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:36:11 [pm] T-228.7s Up 0.38/0.40 Down 0.60/0.62 ptb=81051.4 | CLOB 8847 сообщ., задержка p50/p90=44.3/46.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792334171338 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=2.9/26.6 мс
14:36:20 [cex] Binance 175 сд. задержка p50/p90=145.8/146.7 мс | Coinbase 55 задержка p50=78.4 мс | смещение часов +19.5 мс | lag loop p99/max=2.2/2.2 мс
14:36:20 [cex] binance_futures 254 сд. p50=146.6 мс | bybit 263 сд. p50=122.9 мс | bybit_book 300 сд. p50=113.1 мс | bybit_spot 218 сд. p50=115.7 мс | bybit_spot_book 179 сд. p50=113.1 мс | okx 355 сд. p50=155.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:36:21 [pm] T-218.7s Up 0.46/0.47 Down 0.53/0.54 ptb=81051.4 | CLOB 5602 сообщ., задержка p50/p90=44.2/49.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792334181341 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=1.1/1.2 мс
14:36:30 [cex] Binance 82 сд. задержка p50/p90=144.2/145.0 мс | Coinbase 62 задержка p50=80.0 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.2 мс
14:36:30 [cex] binance_futures 249 сд. p50=144.9 мс | bybit 234 сд. p50=116.6 мс | bybit_book 337 сд. p50=111.0 мс | bybit_spot 222 сд. p50=113.6 мс | bybit_spot_book 152 сд. p50=111.1 мс | okx 259 сд. p50=153.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:36:31 [pm] T-208.7s Up 0.42/0.43 Down 0.57/0.58 ptb=81051.4 | CLOB 6535 сообщ., задержка p50/p90=44.2/46.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792334191343 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=1.9/2.0 мс
14:36:40 [cex] Binance 48 сд. задержка p50/p90=143.5/143.8 мс | Coinbase 50 задержка p50=77.2 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.2 мс
14:36:40 [cex] binance_futures 137 сд. p50=145.5 мс | bybit 124 сд. p50=114.3 мс | bybit_book 282 сд. p50=111.0 мс | bybit_spot 200 сд. p50=113.6 мс | bybit_spot_book 109 сд. p50=111.1 мс | okx 139 сд. p50=153.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:36:41 [pm] T-198.7s Up 0.46/0.47 Down 0.53/0.54 ptb=81051.4 | CLOB 6765 сообщ., задержка p50/p90=44.6/48.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792334201344 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=1.1/1.2 мс
14:36:50 [cex] Binance 59 сд. задержка p50/p90=143.7/144.6 мс | Coinbase 49 задержка p50=76.7 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.2 мс
14:36:50 [cex] binance_futures 116 сд. p50=145.2 мс | bybit 219 сд. p50=115.5 мс | bybit_book 243 сд. p50=111.0 мс | bybit_spot 109 сд. p50=113.8 мс | bybit_spot_book 120 сд. p50=111.1 мс | okx 174 сд. p50=153.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:36:51 [pm] T-188.7s Up 0.56/0.57 Down 0.43/0.44 ptb=81051.4 | CLOB 6317 сообщ., задержка p50/p90=45.0/51.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792334211346 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=1.2/2.1 мс
```

Представлено версией кода: eab44f6; python 3.12.3
