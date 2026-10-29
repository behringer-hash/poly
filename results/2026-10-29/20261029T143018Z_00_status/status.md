# Состояние сервера записи

Время (UTC): 2026-10-29 14:30:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 7 hours, 6 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         569         903           1         610        1336
Swap:           2047         321        1726
```
- нагрузка CPU (1/5/15 мин): 0.08 / 0.23 / 0.59

## Данные
- файлов: 5824, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 2 |
| bn_book | 242 | 3 МБ | 6 |
| bnf_agg | 242 | 50 МБ | 2 |
| bnf_book | 74 | 496 МБ | 0 |
| bnf_liq | 211 | 135 КБ | 136 |
| by_book1 | 242 | 111 МБ | 2 |
| by_liq | 225 | 98 КБ | 747 |
| by_trade | 242 | 34 МБ | 2 |
| bys_book1 | 242 | 84 МБ | 2 |
| bys_trade | 242 | 33 МБ | 2 |
| cb_ticker | 242 | 32 МБ | 2 |
| clock | 242 | 188 КБ | 46 |
| clock_pm | 242 | 188 КБ | 21 |
| events | 233 | 73 КБ | 1251 |
| events_pm | 241 | 86 КБ | 241 |
| health_cex | 242 | 3 МБ | 6 |
| health_feeds | 242 | 8 МБ | 6 |
| health_pm | 242 | 3 МБ | 9 |
| ok_trade | 242 | 43 МБ | 2 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 3 |
| pm_top | 242 | 101 МБ | 1 |
| pm_trades | 242 | 72 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 499 КБ | 225 |

Дни с данными: 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 39, всего 288
- Polymarket CLOB: TCP 5, TLS 44, всего 99
- Polymarket gamma: TCP 4, TLS 42, всего 53

## Последние строки журнала записи
```
14:29:32 [cex] binance_futures 100 сд. p50=152.1 мс | bybit 119 сд. p50=114.4 мс | bybit_book 254 сд. p50=111.7 мс | bybit_spot 123 сд. p50=114.3 мс | bybit_spot_book 106 сд. p50=112.1 мс | okx 115 сд. p50=149.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4226 сд. p50=145.1 мс
14:29:38 [pm] T- 21.7s Up n/a/0.01 Down 0.99/n/a ptb=80313.6 | CLOB 1533 сообщ., задержка p50/p90=39.2/41.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793284178322 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.2/2.2 мс
14:29:42 [cex] Binance 79 сд. задержка p50/p90=144.7/149.1 мс | Coinbase 63 задержка p50=80.3 мс | смещение часов +19.8 мс | lag loop p99/max=2.1/2.8 мс
14:29:42 [cex] binance_futures 67 сд. p50=148.8 мс | bybit 22 сд. p50=114.0 мс | bybit_book 163 сд. p50=111.5 мс | bybit_spot 76 сд. p50=115.7 мс | bybit_spot_book 87 сд. p50=112.0 мс | okx 75 сд. p50=148.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1573 сд. p50=144.6 мс
14:29:45 [pm] окно btc-updown-5m-1793284200 (2026-10-29 14:30:00 UTC): Bitcoin Up or Down - October 29, 10:30AM-10:35AM ET
14:29:48 [pm] T- 11.7s Up n/a/0.01 Down 0.99/n/a ptb=80313.6 | CLOB 1351 сообщ., задержка p50/p90=38.6/40.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793284188324 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.3/11.8 мс
14:29:52 [cex] Binance 132 сд. задержка p50/p90=146.0/151.6 мс | Coinbase 84 задержка p50=81.4 мс | смещение часов +19.8 мс | lag loop p99/max=2.0/2.0 мс
14:29:52 [cex] binance_futures 78 сд. p50=150.9 мс | bybit 73 сд. p50=113.9 мс | bybit_book 217 сд. p50=111.5 мс | bybit_spot 87 сд. p50=113.8 мс | bybit_spot_book 99 сд. p50=112.0 мс | okx 81 сд. p50=148.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1639 сд. p50=145.2 мс
14:29:58 [pm] T-  1.7s Up n/a/0.01 Down 0.99/n/a ptb=80313.6 | CLOB 1820 сообщ., задержка p50/p90=38.4/42.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793284198325 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=1.7/2.1 мс
14:30:02 [cex] Binance 296 сд. задержка p50/p90=159.2/175.7 мс | Coinbase 148 задержка p50=94.6 мс | смещение часов +19.8 мс | lag loop p99/max=9.0/14.6 мс
14:30:02 [cex] binance_futures 335 сд. p50=150.0 мс | bybit 303 сд. p50=115.0 мс | bybit_book 263 сд. p50=111.6 мс | bybit_spot 272 сд. p50=120.6 мс | bybit_spot_book 139 сд. p50=112.1 мс | okx 209 сд. p50=412.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3500 сд. p50=153.6 мс
14:30:08 [pm] T-291.7s Up 0.59/0.60 Down 0.40/0.41 ptb=80292.1 | CLOB 7581 сообщ., задержка p50/p90=37.4/39.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793284208326 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=23.8/28.4 мс
14:30:12 [cex] Binance 255 сд. задержка p50/p90=148.3/160.1 мс | Coinbase 94 задержка p50=81.6 мс | смещение часов +19.8 мс | lag loop p99/max=5.4/5.9 мс
14:30:12 [cex] binance_futures 305 сд. p50=148.0 мс | bybit 347 сд. p50=114.3 мс | bybit_book 379 сд. p50=111.6 мс | bybit_spot 356 сд. p50=115.7 мс | bybit_spot_book 203 сд. p50=112.0 мс | okx 238 сд. p50=320.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5307 сд. p50=145.7 мс
14:30:18 [pm] T-281.7s Up 0.67/0.68 Down 0.32/0.33 ptb=80292.1 | CLOB 6702 сообщ., задержка p50/p90=40.5/54.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793284218327 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.3/2.5 мс
```

Представлено версией кода: c6a21a2; python 3.12.3
