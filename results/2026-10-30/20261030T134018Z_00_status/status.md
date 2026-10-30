# Состояние сервера записи

Время (UTC): 2026-10-30 13:40:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 2 days, 6 hours, 16 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         653         304           1        1131        1252
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.41 / 0.42 / 0.37

## Данные
- файлов: 5839, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 39 МБ | 0 |
| bn_book | 242 | 3 МБ | 0 |
| bnf_agg | 242 | 56 МБ | 0 |
| bnf_book | 97 | 797 МБ | 0 |
| bnf_liq | 212 | 149 КБ | 66 |
| by_book1 | 242 | 119 МБ | 0 |
| by_liq | 225 | 123 КБ | 137 |
| by_trade | 242 | 39 МБ | 0 |
| bys_book1 | 242 | 88 МБ | 0 |
| bys_trade | 242 | 37 МБ | 0 |
| cb_ticker | 242 | 34 МБ | 0 |
| clock | 242 | 188 КБ | 20 |
| clock_pm | 242 | 188 КБ | 55 |
| events | 225 | 72 КБ | 3655 |
| events_pm | 241 | 87 КБ | 135 |
| health_cex | 242 | 3 МБ | 8 |
| health_feeds | 242 | 8 МБ | 8 |
| health_pm | 242 | 3 МБ | 8 |
| ok_trade | 242 | 49 МБ | 0 |
| pm_depth | 242 | 50 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 4 |
| pm_top | 242 | 102 МБ | 2 |
| pm_trades | 241 | 72 МБ | 2 |
| rtds | 242 | 16 МБ | 2 |
| windows | 242 | 500 КБ | 315 |

Дни с данными: 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 72, всего 322
- Polymarket CLOB: TCP 6, TLS 57, всего 115
- Polymarket gamma: TCP 4, TLS 62, всего 69

## Последние строки журнала записи
```
13:39:39 [cex] Binance 279 сд. задержка p50/p90=152.6/157.2 мс | Coinbase 122 задержка p50=102.5 мс | смещение часов +24.3 мс | lag loop p99/max=5.7/15.0 мс
13:39:39 [cex] binance_futures 594 сд. p50=153.4 мс | bybit 803 сд. p50=119.1 мс | bybit_book 634 сд. p50=127.9 мс | bybit_spot 589 сд. p50=118.9 мс | bybit_spot_book 376 сд. p50=115.9 мс | okx 925 сд. p50=164.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 13099 сд. p50=148.9 мс
13:39:40 [pm] T- 19.3s Up n/a/0.01 Down 0.99/n/a ptb=77106.8 | CLOB 1759 сообщ., задержка p50/p90=43.2/57.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793367580705 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.0 мс | lag loop p99/max=2.0/2.1 мс
13:39:45 [pm] окно btc-updown-5m-1793367600 (2026-10-30 13:40:00 UTC): Bitcoin Up or Down - October 30, 9:40AM-9:45AM ET
13:39:49 [cex] Binance 492 сд. задержка p50/p90=152.1/156.4 мс | Coinbase 144 задержка p50=95.8 мс | смещение часов +24.3 мс | lag loop p99/max=9.4/22.6 мс
13:39:49 [cex] binance_futures 779 сд. p50=153.1 мс | bybit 1163 сд. p50=119.4 мс | bybit_book 610 сд. p50=127.9 мс | bybit_spot 587 сд. p50=118.8 мс | bybit_spot_book 420 сд. p50=115.9 мс | okx 970 сд. p50=161.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 14047 сд. p50=149.5 мс
13:39:50 [pm] T-  9.3s Up n/a/0.01 Down 0.99/n/a ptb=77106.8 | CLOB 3891 сообщ., задержка p50/p90=43.0/63.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793367590706 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.0 мс | lag loop p99/max=2.0/49.9 мс
13:39:59 [cex] Binance 324 сд. задержка p50/p90=150.6/154.4 мс | Coinbase 96 задержка p50=93.9 мс | смещение часов +21.8 мс | lag loop p99/max=4.3/7.2 мс
13:39:59 [cex] binance_futures 652 сд. p50=152.4 мс | bybit 761 сд. p50=118.3 мс | bybit_book 653 сд. p50=127.8 мс | bybit_spot 599 сд. p50=118.6 мс | bybit_spot_book 444 сд. p50=115.8 мс | okx 829 сд. p50=161.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 12556 сд. p50=148.3 мс
13:40:00 [pm] T-299.3s Up 0.55/0.56 Down 0.44/0.45 ptb=n/a | CLOB 5388 сообщ., задержка p50/p90=66.7/502.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793367600707 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.0 мс | lag loop p99/max=1.5/5.0 мс
13:40:09 [cex] Binance 518 сд. задержка p50/p90=148.3/153.2 мс | Coinbase 193 задержка p50=93.2 мс | смещение часов +21.8 мс | lag loop p99/max=9.4/11.3 мс
13:40:09 [cex] binance_futures 918 сд. p50=150.3 мс | bybit 1332 сд. p50=116.7 мс | bybit_book 700 сд. p50=125.4 мс | bybit_spot 803 сд. p50=117.5 мс | bybit_spot_book 478 сд. p50=113.5 мс | okx 1329 сд. p50=161.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 16774 сд. p50=147.8 мс
13:40:10 [pm] T-289.3s Up 0.35/0.37 Down 0.63/0.65 ptb=77048.5 | CLOB 7397 сообщ., задержка p50/p90=689.7/726.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793367610708 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.0 мс | lag loop p99/max=4.6/6.1 мс
13:40:19 [cex] Binance 357 сд. задержка p50/p90=149.8/155.6 мс | Coinbase 175 задержка p50=92.2 мс | смещение часов +21.8 мс | lag loop p99/max=13.5/18.5 мс
13:40:19 [cex] binance_futures 700 сд. p50=151.9 мс | bybit 1206 сд. p50=117.0 мс | bybit_book 678 сд. p50=125.4 мс | bybit_spot 664 сд. p50=117.3 мс | bybit_spot_book 476 сд. p50=113.4 мс | okx 854 сд. p50=160.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 20579 сд. p50=150.4 мс
```

Представлено версией кода: b8783c2; python 3.12.3
