# Состояние сервера записи

Время (UTC): 2026-10-30 00:15:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 16 hours, 51 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         631         880           1         574        1274
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.29 / 0.45 / 0.51

## Данные
- файлов: 5829, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 39 МБ | 1 |
| bn_book | 242 | 3 МБ | 1 |
| bnf_agg | 242 | 56 МБ | 1 |
| bnf_book | 84 | 621 МБ | 0 |
| bnf_liq | 211 | 144 КБ | 1 |
| by_book1 | 242 | 114 МБ | 1 |
| by_liq | 225 | 129 КБ | 1 |
| by_trade | 242 | 38 МБ | 1 |
| bys_book1 | 242 | 86 МБ | 1 |
| bys_trade | 242 | 35 МБ | 1 |
| cb_ticker | 242 | 33 МБ | 1 |
| clock | 242 | 187 КБ | 19 |
| clock_pm | 242 | 187 КБ | 54 |
| events | 229 | 73 КБ | 2219 |
| events_pm | 241 | 85 КБ | 139 |
| health_cex | 242 | 3 МБ | 7 |
| health_feeds | 242 | 8 МБ | 7 |
| health_pm | 242 | 3 МБ | 4 |
| ok_trade | 242 | 49 МБ | 1 |
| pm_depth | 242 | 49 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 2 |
| pm_top | 242 | 100 МБ | 2 |
| pm_trades | 241 | 71 МБ | 2 |
| rtds | 242 | 15 МБ | 2 |
| windows | 242 | 498 КБ | 14 |

Дни с данными: 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 40, всего 288
- Polymarket CLOB: TCP 5, TLS 41, всего 85
- Polymarket gamma: TCP 4, TLS 43, всего 50

## Последние строки журнала записи
```
00:15:00 [cex] Binance 300 сд. задержка p50/p90=144.1/147.2 мс | Coinbase 79 задержка p50=92.9 мс | смещение часов +19.4 мс | lag loop p99/max=2.6/4.9 мс
00:15:00 [cex] binance_futures 565 сд. p50=145.9 мс | bybit 371 сд. p50=113.2 мс | bybit_book 457 сд. p50=110.8 мс | bybit_spot 387 сд. p50=113.1 мс | bybit_spot_book 323 сд. p50=111.5 мс | okx 564 сд. p50=156.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4779 сд. p50=143.9 мс
00:15:03 [pm] T-296.3s Up 0.62/0.63 Down 0.37/0.38 ptb=77682.9 | CLOB 4200 сообщ., задержка p50/p90=39.9/53.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793319303665 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=2.1/2.2 мс
00:15:10 [cex] Binance 501 сд. задержка p50/p90=146.4/158.0 мс | Coinbase 119 задержка p50=107.9 мс | смещение часов +19.4 мс | lag loop p99/max=4.1/4.3 мс
00:15:10 [cex] binance_futures 611 сд. p50=147.6 мс | bybit 483 сд. p50=113.5 мс | bybit_book 408 сд. p50=110.9 мс | bybit_spot 438 сд. p50=113.5 мс | bybit_spot_book 265 сд. p50=111.6 мс | okx 893 сд. p50=158.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 6728 сд. p50=144.2 мс
00:15:13 [pm] T-286.3s Up 0.63/0.64 Down 0.36/0.37 ptb=77682.9 | CLOB 3411 сообщ., задержка p50/p90=42.4/87.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793319313666 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=2.0/5.3 мс
00:15:20 [cex] Binance 417 сд. задержка p50/p90=146.3/149.9 мс | Coinbase 106 задержка p50=96.0 мс | смещение часов +19.4 мс | lag loop p99/max=2.4/4.8 мс
00:15:20 [cex] binance_futures 506 сд. p50=147.8 мс | bybit 661 сд. p50=113.0 мс | bybit_book 467 сд. p50=110.8 мс | bybit_spot 467 сд. p50=113.4 мс | bybit_spot_book 277 сд. p50=111.5 мс | okx 346 сд. p50=157.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 10989 сд. p50=143.9 мс
00:15:23 [pm] T-276.3s Up 0.56/0.57 Down 0.43/0.44 ptb=77682.9 | CLOB 3390 сообщ., задержка p50/p90=47.1/61.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793319323667 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=2.2/2.3 мс
00:15:30 [cex] Binance 865 сд. задержка p50/p90=146.4/150.1 мс | Coinbase 129 задержка p50=100.4 мс | смещение часов +21.5 мс | lag loop p99/max=5.5/5.9 мс
00:15:30 [cex] binance_futures 859 сд. p50=148.1 мс | bybit 690 сд. p50=114.3 мс | bybit_book 478 сд. p50=110.9 мс | bybit_spot 505 сд. p50=113.9 мс | bybit_spot_book 334 сд. p50=111.6 мс | okx 862 сд. p50=157.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 15973 сд. p50=143.7 мс
00:15:33 [pm] T-266.3s Up 0.42/0.44 Down 0.56/0.58 ptb=77682.9 | CLOB 4466 сообщ., задержка p50/p90=39.2/50.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793319333669 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=2.0/2.0 мс
00:15:40 [cex] Binance 376 сд. задержка p50/p90=146.6/149.3 мс | Coinbase 89 задержка p50=94.4 мс | смещение часов +21.5 мс | lag loop p99/max=2.1/6.6 мс
00:15:40 [cex] binance_futures 519 сд. p50=149.5 мс | bybit 465 сд. p50=115.5 мс | bybit_book 474 сд. p50=112.9 мс | bybit_spot 510 сд. p50=115.1 мс | bybit_spot_book 343 сд. p50=113.6 мс | okx 755 сд. p50=158.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 10056 сд. p50=146.0 мс
00:15:43 [pm] T-256.3s Up 0.36/0.37 Down 0.63/0.64 ptb=77682.9 | CLOB 2513 сообщ., задержка p50/p90=46.2/57.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793319343671 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.9/2.1 мс
```

Представлено версией кода: b8783c2; python 3.12.3
