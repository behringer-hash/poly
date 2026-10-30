# Состояние сервера записи

Время (UTC): 2026-10-30 05:25:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 22 hours, 1 minute
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         632         591           1         865        1273
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.17 / 0.26 / 0.28

## Данные
- файлов: 5832, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 38 МБ | 1 |
| bn_book | 242 | 3 МБ | 5 |
| bnf_agg | 242 | 54 МБ | 1 |
| bnf_book | 89 | 641 МБ | 0 |
| bnf_liq | 211 | 145 КБ | 794 |
| by_book1 | 242 | 114 МБ | 1 |
| by_liq | 225 | 120 КБ | 575 |
| by_trade | 242 | 36 МБ | 1 |
| bys_book1 | 242 | 85 МБ | 1 |
| bys_trade | 242 | 35 МБ | 3 |
| cb_ticker | 242 | 33 МБ | 1 |
| clock | 242 | 188 КБ | 9 |
| clock_pm | 242 | 188 КБ | 41 |
| events | 226 | 72 КБ | 181 |
| events_pm | 242 | 85 КБ | 374 |
| health_cex | 242 | 3 МБ | 3 |
| health_feeds | 242 | 8 МБ | 3 |
| health_pm | 242 | 3 МБ | 1 |
| ok_trade | 242 | 47 МБ | 1 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 3 |
| pm_top | 242 | 101 МБ | 1 |
| pm_trades | 241 | 71 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 499 КБ | 334 |

Дни с данными: 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 35, всего 285
- Polymarket CLOB: TCP 6, TLS 39, всего 83
- Polymarket gamma: TCP 4, TLS 37, всего 43

## Последние строки журнала записи
```
05:24:24 [cex] binance_futures 60 сд. p50=277.1 мс | bybit 78 сд. p50=115.2 мс | bybit_book 230 сд. p50=112.8 мс | bybit_spot 30 сд. p50=115.1 мс | bybit_spot_book 55 сд. p50=113.3 мс | okx 70 сд. p50=157.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1336 сд. p50=145.6 мс
05:24:26 [pm] T- 33.6s Up 0.99/n/a Down n/a/0.01 ptb=78424.6 | CLOB 925 сообщ., задержка p50/p90=40.1/41.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793337866379 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=2.1/2.1 мс
05:24:34 [cex] Binance 110 сд. задержка p50/p90=150.2/156.0 мс | Coinbase 59 задержка p50=85.3 мс | смещение часов +21.4 мс | lag loop p99/max=2.0/4.1 мс
05:24:34 [cex] binance_futures 181 сд. p50=149.4 мс | bybit 160 сд. p50=116.7 мс | bybit_book 256 сд. p50=112.8 мс | bybit_spot 121 сд. p50=115.9 мс | bybit_spot_book 89 сд. p50=113.2 мс | okx 106 сд. p50=158.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2814 сд. p50=147.5 мс
05:24:36 [pm] T- 23.6s Up 0.99/n/a Down n/a/0.01 ptb=78424.6 | CLOB 1623 сообщ., задержка p50/p90=42.6/48.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793337876380 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.3 мс | lag loop p99/max=1.8/2.2 мс
05:24:44 [cex] Binance 137 сд. задержка p50/p90=146.7/151.2 мс | Coinbase 55 задержка p50=85.3 мс | смещение часов +21.4 мс | lag loop p99/max=2.8/8.1 мс
05:24:44 [cex] binance_futures 189 сд. p50=153.2 мс | bybit 128 сд. p50=115.1 мс | bybit_book 312 сд. p50=112.8 мс | bybit_spot 161 сд. p50=120.9 мс | bybit_spot_book 94 сд. p50=113.2 мс | okx 189 сд. p50=158.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 6130 сд. p50=149.4 мс
05:24:45 [pm] окно btc-updown-5m-1793337900 (2026-10-30 05:25:00 UTC): Bitcoin Up or Down - October 30, 1:25AM-1:30AM ET
05:24:46 [pm] T- 13.6s Up 0.99/n/a Down n/a/0.01 ptb=78424.6 | CLOB 1649 сообщ., задержка p50/p90=42.5/46.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793337886382 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=1.9/2.1 мс
05:24:54 [cex] Binance 208 сд. задержка p50/p90=153.6/155.7 мс | Coinbase 57 задержка p50=85.3 мс | смещение часов +21.4 мс | lag loop p99/max=6.8/7.3 мс
05:24:54 [cex] binance_futures 196 сд. p50=153.1 мс | bybit 162 сд. p50=116.9 мс | bybit_book 262 сд. p50=112.8 мс | bybit_spot 327 сд. p50=115.8 мс | bybit_spot_book 97 сд. p50=113.2 мс | okx 254 сд. p50=161.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4787 сд. p50=147.7 мс
05:24:56 [pm] T-  3.6s Up 1.00/n/a Down n/a/0.00 ptb=78424.6 | CLOB 3533 сообщ., задержка p50/p90=42.2/84.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793337896383 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=5.5/11.3 мс
05:25:04 [cex] Binance 136 сд. задержка p50/p90=147.1/152.8 мс | Coinbase 66 задержка p50=84.9 мс | смещение часов +20.4 мс | lag loop p99/max=3.8/4.6 мс
05:25:04 [cex] binance_futures 141 сд. p50=154.9 мс | bybit 117 сд. p50=114.7 мс | bybit_book 319 сд. p50=112.1 мс | bybit_spot 167 сд. p50=115.3 мс | bybit_spot_book 128 сд. p50=112.8 мс | okx 102 сд. p50=157.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5923 сд. p50=144.6 мс
05:25:06 [pm] T-293.6s Up 0.27/0.28 Down 0.72/0.73 ptb=78465.9 | CLOB 6676 сообщ., задержка p50/p90=38.7/40.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793337906384 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=6.6/16.4 мс
```

Представлено версией кода: b8783c2; python 3.12.3
