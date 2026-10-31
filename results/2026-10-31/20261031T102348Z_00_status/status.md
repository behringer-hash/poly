# Состояние сервера записи

Время (UTC): 2026-10-31 10:23:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 3 days, 2 hours, 59 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         583         984           1         525        1322
Swap:           2047         338        1709
```
- нагрузка CPU (1/5/15 мин): 0.23 / 0.22 / 0.19

## Данные
- файлов: 5855, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 37 МБ | 1 |
| bn_book | 242 | 3 МБ | 5 |
| bnf_agg | 242 | 52 МБ | 1 |
| bnf_book | 118 | 801 МБ | 0 |
| bnf_liq | 211 | 151 КБ | 263 |
| by_book1 | 242 | 113 МБ | 1 |
| by_liq | 223 | 118 КБ | 11271 |
| by_trade | 242 | 35 МБ | 3 |
| bys_book1 | 242 | 83 МБ | 1 |
| bys_trade | 242 | 34 МБ | 5 |
| cb_ticker | 242 | 33 МБ | 1 |
| clock | 242 | 187 КБ | 34 |
| clock_pm | 242 | 187 КБ | 8 |
| events | 223 | 71 КБ | 433 |
| events_pm | 241 | 86 КБ | 951 |
| health_cex | 242 | 3 МБ | 7 |
| health_feeds | 242 | 8 МБ | 7 |
| health_pm | 242 | 3 МБ | 6 |
| ok_trade | 242 | 46 МБ | 1 |
| pm_depth | 242 | 50 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 0 |
| pm_top | 242 | 99 МБ | 0 |
| pm_trades | 241 | 70 МБ | 0 |
| rtds | 242 | 16 МБ | 0 |
| windows | 242 | 498 КБ | 344 |

Дни с данными: 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 58, всего 307
- Polymarket CLOB: TCP 5, TLS 40, всего 86
- Polymarket gamma: TCP 4, TLS 39, всего 45

## Последние строки журнала записи
```
10:23:01 [cex] Binance 32 сд. задержка p50/p90=145.5/146.5 мс | Coinbase 34 задержка p50=90.6 мс | смещение часов +21.3 мс | lag loop p99/max=2.1/2.1 мс
10:23:01 [cex] binance_futures 25 сд. p50=295.0 мс | bybit 11 сд. p50=114.3 мс | bybit_book 27 сд. p50=112.6 мс | bybit_spot 6 сд. p50=114.7 мс | bybit_spot_book 66 сд. p50=112.5 мс | okx 34 сд. p50=153.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 505 сд. p50=145.8 мс
10:23:01 [pm] T-118.3s Up 0.28/0.29 Down 0.71/0.72 ptb=77383.8 | CLOB 4904 сообщ., задержка p50/p90=43.8/56.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793442181701 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.6/2.4 мс
10:23:11 [cex] Binance 47 сд. задержка p50/p90=145.8/149.8 мс | Coinbase 54 задержка p50=91.1 мс | смещение часов +21.3 мс | lag loop p99/max=2.1/7.4 мс
10:23:11 [cex] binance_futures 82 сд. p50=149.2 мс | bybit 107 сд. p50=124.3 мс | bybit_book 74 сд. p50=112.5 мс | bybit_spot 100 сд. p50=122.4 мс | bybit_spot_book 69 сд. p50=112.6 мс | okx 58 сд. p50=153.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 888 сд. p50=146.2 мс
10:23:11 [pm] T-108.3s Up 0.18/0.19 Down 0.81/0.82 ptb=77383.8 | CLOB 4593 сообщ., задержка p50/p90=43.5/50.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793442191702 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.8/1.8 мс
10:23:21 [cex] Binance 72 сд. задержка p50/p90=143.6/148.2 мс | Coinbase 27 задержка p50=88.0 мс | смещение часов +18.1 мс | lag loop p99/max=2.1/2.4 мс
10:23:21 [cex] binance_futures 40 сд. p50=291.7 мс | bybit 25 сд. p50=115.1 мс | bybit_book 97 сд. p50=109.4 мс | bybit_spot 49 сд. p50=118.4 мс | bybit_spot_book 46 сд. p50=109.5 мс | okx 75 сд. p50=154.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2257 сд. p50=143.3 мс
10:23:21 [pm] T- 98.3s Up 0.09/0.10 Down 0.90/0.91 ptb=77383.8 | CLOB 3965 сообщ., задержка p50/p90=44.0/59.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793442201705 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.0/2.0 мс
10:23:31 [cex] Binance 22 сд. задержка p50/p90=142.3/143.3 мс | Coinbase 64 задержка p50=88.1 мс | смещение часов +18.1 мс | lag loop p99/max=2.2/2.2 мс
10:23:31 [cex] binance_futures 22 сд. p50=291.8 мс | bybit 4 сд. p50=111.5 мс | bybit_book 59 сд. p50=109.4 мс | bybit_spot 6 сд. p50=111.1 мс | bybit_spot_book 25 сд. p50=109.4 мс | okx 12 сд. p50=149.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 315 сд. p50=142.6 мс
10:23:31 [pm] T- 88.3s Up 0.07/0.08 Down 0.92/0.93 ptb=77383.8 | CLOB 3773 сообщ., задержка p50/p90=43.2/44.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793442211706 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.9/2.1 мс
10:23:41 [cex] Binance 22 сд. задержка p50/p90=142.4/143.3 мс | Coinbase 23 задержка p50=87.6 мс | смещение часов +18.1 мс | lag loop p99/max=2.1/2.2 мс
10:23:41 [cex] binance_futures 26 сд. p50=291.8 мс | bybit 11 сд. p50=111.4 мс | bybit_book 40 сд. p50=109.4 мс | bybit_spot 4 сд. p50=111.8 мс | bybit_spot_book 18 сд. p50=109.5 мс | okx 19 сд. p50=149.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 232 сд. p50=142.6 мс
10:23:41 [pm] T- 78.3s Up 0.08/0.09 Down 0.91/0.92 ptb=77383.8 | CLOB 2092 сообщ., задержка p50/p90=43.0/44.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793442221708 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.9/1.9 мс
```

Представлено версией кода: 8047248; python 3.12.3
