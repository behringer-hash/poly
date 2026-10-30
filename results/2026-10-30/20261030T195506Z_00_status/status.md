# Состояние сервера записи

Время (UTC): 2026-10-30 19:55:06

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 2 days, 12 hours, 31 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         675         296           1        1122        1230
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.45 / 0.44 / 0.39

## Данные
- файлов: 5843, всего 2 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 40 МБ | 0 |
| bn_book | 242 | 4 МБ | 0 |
| bnf_agg | 242 | 57 МБ | 0 |
| bnf_book | 103 | 942 МБ | 0 |
| bnf_liq | 212 | 152 КБ | 151 |
| by_book1 | 242 | 122 МБ | 0 |
| by_liq | 225 | 119 КБ | 271 |
| by_trade | 242 | 40 МБ | 0 |
| bys_book1 | 242 | 90 МБ | 0 |
| bys_trade | 242 | 38 МБ | 0 |
| cb_ticker | 242 | 35 МБ | 0 |
| clock | 242 | 189 КБ | 48 |
| clock_pm | 242 | 189 КБ | 23 |
| events | 223 | 71 КБ | 2151 |
| events_pm | 241 | 86 КБ | 1504 |
| health_cex | 242 | 3 МБ | 2 |
| health_feeds | 242 | 8 МБ | 2 |
| health_pm | 242 | 3 МБ | 1 |
| ok_trade | 242 | 50 МБ | 0 |
| pm_depth | 242 | 51 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 1 |
| pm_top | 242 | 102 МБ | 1 |
| pm_trades | 241 | 71 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 501 КБ | 272 |

Дни с данными: 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 8, TLS 170, всего 421
- Polymarket CLOB: TCP 18, TLS 143, всего 207
- Polymarket gamma: TCP 6, TLS 117, всего 123

## Последние строки журнала записи
```
19:54:23 [cex] binance_futures 767 сд. p50=156.2 мс | bybit 728 сд. p50=118.1 мс | bybit_book 355 сд. p50=110.8 мс | bybit_spot 307 сд. p50=113.8 мс | bybit_spot_book 157 сд. p50=112.6 мс | okx 569 сд. p50=186.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 9508 сд. p50=145.6 мс
19:54:24 [pm] T- 35.8s Up 0.99/n/a Down n/a/0.01 ptb=76704.7 | CLOB 2358 сообщ., задержка p50/p90=42.3/44.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793390064175 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.1/3.7 мс
19:54:33 [cex] Binance 187 сд. задержка p50/p90=143.1/146.1 мс | Coinbase 121 задержка p50=85.7 мс | смещение часов +18.3 мс | lag loop p99/max=8.3/8.7 мс
19:54:33 [cex] binance_futures 224 сд. p50=146.5 мс | bybit 300 сд. p50=112.8 мс | bybit_book 423 сд. p50=110.1 мс | bybit_spot 530 сд. p50=112.9 мс | bybit_spot_book 154 сд. p50=110.4 мс | okx 209 сд. p50=156.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 7652 сд. p50=144.5 мс
19:54:34 [pm] T- 25.8s Up 0.99/n/a Down n/a/0.01 ptb=76704.7 | CLOB 1943 сообщ., задержка p50/p90=42.3/49.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793390074177 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.1/2.2 мс
19:54:43 [cex] Binance 214 сд. задержка p50/p90=144.4/147.4 мс | Coinbase 94 задержка p50=85.8 мс | смещение часов +18.3 мс | lag loop p99/max=5.4/6.5 мс
19:54:43 [cex] binance_futures 365 сд. p50=144.3 мс | bybit 604 сд. p50=112.8 мс | bybit_book 454 сд. p50=110.1 мс | bybit_spot 347 сд. p50=112.2 мс | bybit_spot_book 223 сд. p50=110.4 мс | okx 378 сд. p50=156.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 11819 сд. p50=143.6 мс
19:54:44 [pm] T- 15.8s Up 0.99/n/a Down n/a/0.01 ptb=76704.7 | CLOB 1635 сообщ., задержка p50/p90=42.3/45.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793390084178 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=2.1/2.6 мс
19:54:45 [pm] окно btc-updown-5m-1793390100 (2026-10-30 19:55:00 UTC): Bitcoin Up or Down - October 30, 3:55PM-4:00PM ET
19:54:53 [cex] Binance 188 сд. задержка p50/p90=143.5/148.8 мс | Coinbase 78 задержка p50=86.0 мс | смещение часов +18.3 мс | lag loop p99/max=2.9/3.0 мс
19:54:53 [cex] binance_futures 248 сд. p50=145.1 мс | bybit 226 сд. p50=112.6 мс | bybit_book 341 сд. p50=110.1 мс | bybit_spot 303 сд. p50=113.1 мс | bybit_spot_book 155 сд. p50=110.4 мс | okx 208 сд. p50=156.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 7891 сд. p50=143.8 мс
19:54:54 [pm] T-  5.8s Up 0.99/n/a Down n/a/0.01 ptb=76704.7 | CLOB 3611 сообщ., задержка p50/p90=40.4/88.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793390094180 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=3.4/4.2 мс
19:55:03 [cex] Binance 401 сд. задержка p50/p90=145.2/149.4 мс | Coinbase 161 задержка p50=90.9 мс | смещение часов +18.3 мс | lag loop p99/max=6.8/14.3 мс
19:55:03 [cex] binance_futures 749 сд. p50=145.5 мс | bybit 803 сд. p50=113.0 мс | bybit_book 461 сд. p50=110.2 мс | bybit_spot 479 сд. p50=114.7 мс | bybit_spot_book 279 сд. p50=110.5 мс | okx 645 сд. p50=162.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 14306 сд. p50=146.5 мс
19:55:04 [pm] T-295.8s Up 0.53/0.54 Down 0.46/0.47 ptb=76766.3 | CLOB 9083 сообщ., задержка p50/p90=41.8/54.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793390104181 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=5.4/5.5 мс
```

Представлено версией кода: fcaf736; python 3.12.3
