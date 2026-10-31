# Состояние сервера записи

Время (UTC): 2026-10-31 11:25:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 3 days, 4 hours, 1 minute
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         591         963           1         538        1314
Swap:           2047         338        1709
```
- нагрузка CPU (1/5/15 мин): 0.30 / 0.19 / 0.18

## Данные
- файлов: 5857, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 37 МБ | 0 |
| bn_book | 242 | 3 МБ | 23 |
| bnf_agg | 242 | 52 МБ | 0 |
| bnf_book | 119 | 796 МБ | 0 |
| bnf_liq | 211 | 151 КБ | 3441 |
| by_book1 | 242 | 113 МБ | 0 |
| by_liq | 224 | 118 КБ | 707 |
| by_trade | 242 | 35 МБ | 0 |
| bys_book1 | 242 | 85 МБ | 0 |
| bys_trade | 242 | 34 МБ | 2 |
| cb_ticker | 242 | 33 МБ | 0 |
| clock | 242 | 187 КБ | 57 |
| clock_pm | 242 | 188 КБ | 31 |
| events | 223 | 71 КБ | 381 |
| events_pm | 241 | 85 КБ | 159 |
| health_cex | 242 | 3 МБ | 6 |
| health_feeds | 242 | 8 МБ | 6 |
| health_pm | 242 | 3 МБ | 5 |
| ok_trade | 242 | 45 МБ | 0 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 1 |
| pm_top | 242 | 99 МБ | 1 |
| pm_trades | 241 | 70 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 499 КБ | 125 |

Дни с данными: 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 291
- Polymarket CLOB: TCP 6, TLS 49, всего 96
- Polymarket gamma: TCP 3, TLS 44, всего 50

## Последние строки журнала записи
```
11:24:52 [cex] Binance 26 сд. задержка p50/p90=142.3/143.2 мс | Coinbase 30 задержка p50=86.1 мс | смещение часов +18.1 мс | lag loop p99/max=2.1/2.1 мс
11:24:52 [cex] binance_futures 17 сд. p50=292.3 мс | bybit 1 сд. p50=111.1 мс | bybit_book 78 сд. p50=109.4 мс | bybit_spot 2 сд. p50=111.7 мс | bybit_spot_book 242 сд. p50=109.5 мс | okx 10 сд. p50=149.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 841 сд. p50=143.2 мс
11:24:52 [pm] T-  7.7s Up 1.00/n/a Down n/a/0.00 ptb=77320.6 | CLOB 1253 сообщ., задержка p50/p90=39.0/40.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793445892260 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.1/23.9 мс
11:25:02 [cex] Binance 21 сд. задержка p50/p90=142.3/143.3 мс | Coinbase 33 задержка p50=86.2 мс | смещение часов +18.1 мс | lag loop p99/max=2.0/2.2 мс
11:25:02 [cex] binance_futures 16 сд. p50=292.4 мс | bybit 4 сд. p50=111.6 мс | bybit_book 218 сд. p50=109.3 мс | bybit_spot 2 сд. p50=112.0 мс | bybit_spot_book 282 сд. p50=109.6 мс | okx 10 сд. p50=150.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 760 сд. p50=143.0 мс
11:25:02 [pm] T-297.7s Up 0.47/0.48 Down 0.52/0.53 ptb=n/a | CLOB 3356 сообщ., задержка p50/p90=39.1/59.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793445902261 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=2.1/2.8 мс
11:25:12 [cex] Binance 25 сд. задержка p50/p90=142.3/143.2 мс | Coinbase 80 задержка p50=216.2 мс | смещение часов +18.1 мс | lag loop p99/max=2.2/2.2 мс
11:25:12 [cex] binance_futures 18 сд. p50=292.6 мс | bybit 4 сд. p50=111.4 мс | bybit_book 198 сд. p50=109.3 мс | bybit_spot 2 сд. p50=111.2 мс | bybit_spot_book 254 сд. p50=109.5 мс | okx 10 сд. p50=149.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1002 сд. p50=143.0 мс
11:25:12 [pm] T-287.7s Up 0.55/0.56 Down 0.44/0.45 ptb=77343.8 | CLOB 6053 сообщ., задержка p50/p90=41.6/43.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793445912263 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=2.2/2.3 мс
11:25:22 [cex] Binance 43 сд. задержка p50/p90=142.2/143.6 мс | Coinbase 39 задержка p50=86.3 мс | смещение часов +18.1 мс | lag loop p99/max=2.1/2.1 мс
11:25:22 [cex] binance_futures 18 сд. p50=292.7 мс | bybit 6 сд. p50=111.2 мс | bybit_book 150 сд. p50=109.2 мс | bybit_spot 8 сд. p50=111.0 мс | bybit_spot_book 188 сд. p50=109.5 мс | okx 9 сд. p50=149.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 570 сд. p50=142.9 мс
11:25:22 [pm] T-277.7s Up 0.59/0.60 Down 0.40/0.41 ptb=77343.8 | CLOB 5234 сообщ., задержка p50/p90=41.5/42.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793445922264 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=1.6/2.0 мс
11:25:32 [cex] Binance 36 сд. задержка p50/p90=142.4/143.2 мс | Coinbase 37 задержка p50=86.3 мс | смещение часов +18.1 мс | lag loop p99/max=2.1/2.3 мс
11:25:32 [cex] binance_futures 19 сд. p50=292.5 мс | bybit 3 сд. p50=111.5 мс | bybit_book 241 сд. p50=109.2 мс | bybit_spot 10 сд. p50=111.7 мс | bybit_spot_book 275 сд. p50=109.5 мс | okx 7 сд. p50=149.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1211 сд. p50=143.0 мс
11:25:32 [pm] T-267.7s Up 0.61/0.62 Down 0.38/0.39 ptb=77343.8 | CLOB 4582 сообщ., задержка p50/p90=41.5/42.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793445932265 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=1.9/2.1 мс
```

Представлено версией кода: 8047248; python 3.12.3
