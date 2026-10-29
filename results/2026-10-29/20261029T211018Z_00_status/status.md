# Состояние сервера записи

Время (UTC): 2026-10-29 21:10:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 13 hours, 46 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         620        1006           1         458        1285
Swap:           2047         319        1728
```
- нагрузка CPU (1/5/15 мин): 0.36 / 0.88 / 0.88

## Данные
- файлов: 5827, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 36 МБ | 0 |
| bn_book | 242 | 3 МБ | 2 |
| bnf_agg | 242 | 53 МБ | 0 |
| bnf_book | 81 | 564 МБ | 0 |
| bnf_liq | 211 | 136 КБ | 152 |
| by_book1 | 242 | 111 МБ | 0 |
| by_liq | 225 | 110 КБ | 52 |
| by_trade | 242 | 37 МБ | 0 |
| bys_book1 | 242 | 84 МБ | 0 |
| bys_trade | 242 | 34 МБ | 0 |
| cb_ticker | 242 | 32 МБ | 0 |
| clock | 242 | 187 КБ | 18 |
| clock_pm | 242 | 187 КБ | 56 |
| events | 230 | 74 КБ | 628 |
| events_pm | 241 | 87 КБ | 1017 |
| health_cex | 242 | 3 МБ | 0 |
| health_feeds | 242 | 8 МБ | 0 |
| health_pm | 242 | 3 МБ | 7 |
| ok_trade | 242 | 46 МБ | 0 |
| pm_depth | 242 | 49 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 1 |
| pm_top | 242 | 100 МБ | 1 |
| pm_trades | 241 | 71 МБ | 1 |
| rtds | 242 | 15 МБ | 1 |
| windows | 242 | 498 КБ | 43 |

Дни с данными: 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 51, всего 303
- Polymarket CLOB: TCP 14, TLS 68, всего 112
- Polymarket gamma: TCP 3, TLS 42, всего 48

## Последние строки журнала записи
```
21:09:38 [cex] Binance 649 сд. задержка p50/p90=148.2/156.0 мс | Coinbase 203 задержка p50=82.9 мс | смещение часов +19.7 мс | lag loop p99/max=3.5/11.0 мс
21:09:38 [cex] binance_futures 847 сд. p50=147.7 мс | bybit 2351 сд. p50=119.6 мс | bybit_book 597 сд. p50=111.0 мс | bybit_spot 769 сд. p50=115.3 мс | bybit_spot_book 387 сд. p50=112.0 мс | okx 643 сд. p50=159.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 11200 сд. p50=149.7 мс
21:09:41 [pm] T- 18.0s Up 1.00/n/a Down n/a/0.00 ptb=78796.3 | CLOB 989 сообщ., задержка p50/p90=41.0/42.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793308181972 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.1 мс | lag loop p99/max=2.0/2.2 мс
21:09:45 [pm] окно btc-updown-5m-1793308200 (2026-10-29 21:10:00 UTC): Bitcoin Up or Down - October 29, 5:10PM-5:15PM ET
21:09:48 [cex] Binance 459 сд. задержка p50/p90=145.7/149.0 мс | Coinbase 113 задержка p50=80.5 мс | смещение часов +19.7 мс | lag loop p99/max=2.3/6.7 мс
21:09:48 [cex] binance_futures 572 сд. p50=147.9 мс | bybit 985 сд. p50=113.3 мс | bybit_book 517 сд. p50=111.0 мс | bybit_spot 452 сд. p50=114.6 мс | bybit_spot_book 330 сд. p50=111.9 мс | okx 516 сд. p50=157.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 8824 сд. p50=144.9 мс
21:09:51 [pm] T-  8.0s Up 1.00/n/a Down n/a/0.00 ptb=78796.3 | CLOB 1902 сообщ., задержка p50/p90=40.6/48.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793308191973 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.1 мс | lag loop p99/max=20.9/30.6 мс
21:09:58 [cex] Binance 411 сд. задержка p50/p90=145.6/149.9 мс | Coinbase 272 задержка p50=82.1 мс | смещение часов +19.7 мс | lag loop p99/max=7.5/9.5 мс
21:09:58 [cex] binance_futures 531 сд. p50=146.5 мс | bybit 992 сд. p50=113.3 мс | bybit_book 461 сд. p50=111.0 мс | bybit_spot 524 сд. p50=114.8 мс | bybit_spot_book 318 сд. p50=111.8 мс | okx 500 сд. p50=157.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 11614 сд. p50=146.3 мс
21:10:01 [pm] T-298.0s Up 0.54/0.55 Down 0.45/0.46 ptb=n/a | CLOB 5107 сообщ., задержка p50/p90=41.7/50.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793308201983 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.1 мс | lag loop p99/max=7.9/20.7 мс
21:10:08 [cex] Binance 387 сд. задержка p50/p90=145.9/148.9 мс | Coinbase 100 задержка p50=79.8 мс | смещение часов +20.2 мс | lag loop p99/max=9.9/13.8 мс
21:10:08 [cex] binance_futures 343 сд. p50=149.3 мс | bybit 1164 сд. p50=113.9 мс | bybit_book 635 сд. p50=111.6 мс | bybit_spot 600 сд. p50=114.7 мс | bybit_spot_book 409 сд. p50=112.3 мс | okx 370 сд. p50=157.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 9315 сд. p50=150.0 мс
21:10:11 [pm] T-288.0s Up 0.42/0.43 Down 0.57/0.58 ptb=79047.9 | CLOB 10592 сообщ., задержка p50/p90=43.8/62.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793308211984 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.1 мс | lag loop p99/max=2.4/9.3 мс
21:10:18 [cex] Binance 531 сд. задержка p50/p90=146.6/151.8 мс | Coinbase 118 задержка p50=80.4 мс | смещение часов +20.2 мс | lag loop p99/max=7.7/7.9 мс
21:10:18 [cex] binance_futures 601 сд. p50=148.7 мс | bybit 1212 сд. p50=115.6 мс | bybit_book 528 сд. p50=111.6 мс | bybit_spot 731 сд. p50=114.8 мс | bybit_spot_book 393 сд. p50=112.4 мс | okx 875 сд. p50=160.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 16645 сд. p50=147.4 мс
```

Представлено версией кода: b8783c2; python 3.12.3
