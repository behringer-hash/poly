# Состояние сервера записи

Время (UTC): 2026-10-20 06:49:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 5 days, 23 hours, 25 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         807         156           1        1126        1099
Swap:           2047         250        1797
```
- нагрузка CPU (1/5/15 мин): 0.30 / 0.36 / 0.31

## Данные
- файлов: 6955, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 283 | 37 МБ | 1 |
| bn_book | 283 | 3 МБ | 3 |
| bnf_agg | 283 | 57 МБ | 1 |
| bnf_book | 118 | 557 МБ | 594082 |
| bnf_depth5 | 118 | 41 МБ | 594158 |
| bnf_liq | 246 | 161 КБ | 514 |
| bs_trade | 118 | 1 МБ | 594078 |
| by_book1 | 283 | 118 МБ | 1 |
| by_liq | 255 | 128 КБ | 2809 |
| by_trade | 283 | 36 МБ | 1 |
| bys_book1 | 167 | 57 МБ | 1 |
| bys_trade | 167 | 23 МБ | 1 |
| cb_ticker | 283 | 35 МБ | 1 |
| clock | 283 | 219 КБ | 3 |
| clock_pm | 283 | 219 КБ | 28 |
| events | 272 | 87 КБ | 516 |
| events_pm | 283 | 102 КБ | 563 |
| health_cex | 283 | 3 МБ | 9 |
| health_feeds | 283 | 9 МБ | 9 |
| health_pm | 283 | 3 МБ | 5 |
| kr_trade | 118 | 3 МБ | 594078 |
| ok_trade | 282 | 49 МБ | 1 |
| pm_depth | 283 | 57 МБ | 0 |
| pm_rtt | 283 | 2 МБ | 5 |
| pm_top | 283 | 117 МБ | 0 |
| pm_trades | 283 | 82 МБ | 0 |
| rtds | 283 | 18 МБ | 0 |
| windows | 283 | 585 КБ | 313 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 36, всего 287
- Polymarket CLOB: TCP 4, TLS 42, всего 79
- Polymarket gamma: TCP 4, TLS 39, всего 50

## Последние строки журнала записи
```
06:49:07 [cex] Binance 19 сд. задержка p50/p90=158.4/159.4 мс | Coinbase 28 задержка p50=78.1 мс | смещение часов +19.3 мс | lag loop p99/max=2.2/2.2 мс
06:49:07 [cex] binance_futures 23 сд. p50=303.5 мс | bybit 12 сд. p50=112.0 мс | bybit_book 81 сд. p50=110.9 мс | bybit_spot 5 сд. p50=112.8 мс | bybit_spot_book 23 сд. p50=110.6 мс | okx 8 сд. p50=153.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:49:13 [pm] T- 46.4s Up n/a/0.01 Down 0.99/n/a ptb=81756.7 | CLOB 615 сообщ., задержка p50/p90=38.6/39.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792478953611 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.6 мс | lag loop p99/max=2.2/2.2 мс
06:49:17 [cex] Binance 16 сд. задержка p50/p90=158.4/159.4 мс | Coinbase 35 задержка p50=77.7 мс | смещение часов +19.3 мс | lag loop p99/max=2.1/2.2 мс
06:49:17 [cex] binance_futures 20 сд. p50=303.6 мс | bybit 6 сд. p50=112.1 мс | bybit_book 49 сд. p50=110.9 мс | bybit_spot 1 сд. p50=112.5 мс | bybit_spot_book 12 сд. p50=110.7 мс | okx 10 сд. p50=153.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:49:23 [pm] T- 36.4s Up n/a/0.01 Down 0.99/n/a ptb=81756.7 | CLOB 592 сообщ., задержка p50/p90=38.6/39.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792478963611 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.6 мс | lag loop p99/max=2.1/2.1 мс
06:49:27 [cex] Binance 30 сд. задержка p50/p90=158.4/159.5 мс | Coinbase 40 задержка p50=79.1 мс | смещение часов +19.3 мс | lag loop p99/max=2.1/2.1 мс
06:49:27 [cex] binance_futures 27 сд. p50=303.5 мс | bybit 6 сд. p50=112.6 мс | bybit_book 85 сд. p50=110.8 мс | bybit_spot 69 сд. p50=113.3 мс | bybit_spot_book 58 сд. p50=110.6 мс | okx 10 сд. p50=153.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:49:33 [pm] T- 26.4s Up n/a/0.01 Down 0.99/n/a ptb=81756.7 | CLOB 552 сообщ., задержка p50/p90=39.0/68.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792478973612 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.6 мс | lag loop p99/max=2.1/2.1 мс
06:49:37 [cex] Binance 160 сд. задержка p50/p90=159.0/163.9 мс | Coinbase 54 задержка p50=80.6 мс | смещение часов +19.3 мс | lag loop p99/max=2.1/2.1 мс
06:49:37 [cex] binance_futures 163 сд. p50=157.2 мс | bybit 237 сд. p50=114.9 мс | bybit_book 119 сд. p50=110.8 мс | bybit_spot 106 сд. p50=113.3 мс | bybit_spot_book 61 сд. p50=110.7 мс | okx 141 сд. p50=161.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:49:43 [pm] T- 16.4s Up n/a/0.01 Down 0.99/n/a ptb=81756.7 | CLOB 490 сообщ., задержка p50/p90=38.8/40.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792478983613 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.6 мс | lag loop p99/max=2.1/2.2 мс
06:49:45 [pm] окно btc-updown-5m-1792479000 (2026-10-20 06:50:00 UTC): Bitcoin Up or Down - October 20, 2:50AM-2:55AM ET
06:49:47 [cex] Binance 85 сд. задержка p50/p90=158.6/159.2 мс | Coinbase 36 задержка p50=77.7 мс | смещение часов +17.0 мс | lag loop p99/max=2.1/2.2 мс
06:49:47 [cex] binance_futures 78 сд. p50=155.9 мс | bybit 33 сд. p50=112.4 мс | bybit_book 125 сд. p50=110.8 мс | bybit_spot 87 сд. p50=113.3 мс | bybit_spot_book 67 сд. p50=110.4 мс | okx 47 сд. p50=154.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
