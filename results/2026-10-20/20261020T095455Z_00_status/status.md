# Состояние сервера записи

Время (UTC): 2026-10-20 09:54:55

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 2 hours, 31 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         816         161           1        1112        1089
Swap:           2047         250        1797
```
- нагрузка CPU (1/5/15 мин): 0.28 / 0.29 / 0.32

## Данные
- файлов: 7027, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 286 | 37 МБ | 1 |
| bn_book | 286 | 4 МБ | 9 |
| bnf_agg | 286 | 57 МБ | 1 |
| bnf_book | 118 | 557 МБ | 605189 |
| bnf_depth5 | 118 | 41 МБ | 605265 |
| bnf_liq | 249 | 160 КБ | 2569 |
| bs_trade | 118 | 1 МБ | 605185 |
| by_book1 | 286 | 120 МБ | 1 |
| by_liq | 258 | 128 КБ | 1058 |
| by_trade | 286 | 38 МБ | 1 |
| bys_book1 | 170 | 58 МБ | 1 |
| bys_trade | 170 | 24 МБ | 7 |
| cb_ticker | 286 | 35 МБ | 1 |
| clock | 286 | 222 КБ | 36 |
| clock_pm | 286 | 222 КБ | 2 |
| events | 275 | 88 КБ | 124 |
| events_pm | 286 | 103 КБ | 231 |
| health_cex | 286 | 3 МБ | 5 |
| health_feeds | 286 | 9 МБ | 5 |
| health_pm | 286 | 3 МБ | 10 |
| kr_trade | 118 | 3 МБ | 605185 |
| ok_trade | 285 | 49 МБ | 1 |
| pm_depth | 286 | 58 МБ | 2 |
| pm_rtt | 286 | 2 МБ | 4 |
| pm_top | 286 | 118 МБ | 2 |
| pm_trades | 286 | 83 МБ | 4 |
| rtds | 286 | 18 МБ | 2 |
| windows | 286 | 592 КБ | 141 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 7, TLS 42, всего 292
- Polymarket CLOB: TCP 4, TLS 43, всего 84
- Polymarket gamma: TCP 4, TLS 39, всего 49

## Последние строки журнала записи
```
09:54:09 [cex] binance_futures 53 сд. p50=146.8 мс | bybit 95 сд. p50=114.3 мс | bybit_book 125 сд. p50=112.5 мс | bybit_spot 46 сд. p50=115.0 мс | bybit_spot_book 66 сд. p50=112.3 мс | okx 53 сд. p50=144.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:54:15 [pm] T- 44.7s Up 0.99/n/a Down n/a/0.01 ptb=81263.0 | CLOB 668 сообщ., задержка p50/p90=38.5/40.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792490055259 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=2.1/2.2 мс
09:54:19 [cex] Binance 116 сд. задержка p50/p90=159.4/160.2 мс | Coinbase 21 задержка p50=80.3 мс | смещение часов +19.2 мс | lag loop p99/max=2.2/2.6 мс
09:54:19 [cex] binance_futures 77 сд. p50=146.7 мс | bybit 32 сд. p50=115.5 мс | bybit_book 90 сд. p50=112.4 мс | bybit_spot 202 сд. p50=114.2 мс | bybit_spot_book 126 сд. p50=112.1 мс | okx 90 сд. p50=144.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:54:25 [pm] T- 34.7s Up 0.99/n/a Down n/a/0.01 ptb=81263.0 | CLOB 643 сообщ., задержка p50/p90=38.5/40.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792490065261 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=2.1/2.2 мс
09:54:29 [cex] Binance 32 сд. задержка p50/p90=158.1/158.4 мс | Coinbase 9 задержка p50=78.6 мс | смещение часов +19.2 мс | lag loop p99/max=2.2/2.2 мс
09:54:29 [cex] binance_futures 87 сд. p50=145.4 мс | bybit 86 сд. p50=112.6 мс | bybit_book 153 сд. p50=110.8 мс | bybit_spot 17 сд. p50=112.2 мс | bybit_spot_book 69 сд. p50=110.6 мс | okx 43 сд. p50=142.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:54:35 [pm] T- 24.7s Up 0.99/n/a Down n/a/0.01 ptb=81263.0 | CLOB 566 сообщ., задержка p50/p90=38.4/39.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792490075262 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=2.2/2.2 мс
09:54:39 [cex] Binance 98 сд. задержка p50/p90=157.8/158.9 мс | Coinbase 42 задержка p50=78.2 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.1 мс
09:54:39 [cex] binance_futures 53 сд. p50=144.7 мс | bybit 75 сд. p50=112.7 мс | bybit_book 136 сд. p50=110.9 мс | bybit_spot 118 сд. p50=112.7 мс | bybit_spot_book 109 сд. p50=110.5 мс | okx 67 сд. p50=142.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:54:45 [pm] T- 14.7s Up 0.99/n/a Down n/a/0.01 ptb=81263.0 | CLOB 424 сообщ., задержка p50/p90=38.7/41.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792490085262 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=2.2/2.4 мс
09:54:45 [pm] окно btc-updown-5m-1792490100 (2026-10-20 09:55:00 UTC): Bitcoin Up or Down - October 20, 5:55AM-6:00AM ET
09:54:49 [cex] Binance 99 сд. задержка p50/p90=157.8/160.1 мс | Coinbase 47 задержка p50=79.6 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.2 мс
09:54:49 [cex] binance_futures 126 сд. p50=147.3 мс | bybit 227 сд. p50=113.2 мс | bybit_book 210 сд. p50=110.9 мс | bybit_spot 181 сд. p50=113.1 мс | bybit_spot_book 173 сд. p50=110.6 мс | okx 151 сд. p50=143.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:54:55 [pm] T-  4.7s Up 0.99/n/a Down n/a/0.01 ptb=81263.0 | CLOB 2470 сообщ., задержка p50/p90=38.9/40.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792490095264 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=5.3/16.2 мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
