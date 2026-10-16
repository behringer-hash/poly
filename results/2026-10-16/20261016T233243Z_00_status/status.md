# Состояние сервера записи

Время (UTC): 2026-10-16 23:32:43

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 16 hours, 8 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         831         962           2         395        1074
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.25 / 0.27 / 0.24

## Данные
- файлов: 5082, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 204 | 28 МБ | 1 |
| bn_book | 204 | 3 МБ | 34 |
| bnf_agg | 204 | 43 МБ | 1 |
| bnf_book | 118 | 557 МБ | 308657 |
| bnf_depth5 | 118 | 41 МБ | 308734 |
| bnf_liq | 183 | 126 КБ | 124 |
| bs_trade | 118 | 1 МБ | 308653 |
| by_book1 | 204 | 90 МБ | 1 |
| by_liq | 183 | 103 КБ | 947 |
| by_trade | 204 | 28 МБ | 1 |
| bys_book1 | 88 | 35 МБ | 1 |
| bys_trade | 88 | 14 МБ | 3 |
| cb_ticker | 204 | 26 МБ | 1 |
| clock | 204 | 158 КБ | 50 |
| clock_pm | 204 | 158 КБ | 5 |
| events | 193 | 64 КБ | 337 |
| events_pm | 204 | 75 КБ | 334 |
| health_cex | 204 | 2 МБ | 7 |
| health_feeds | 204 | 7 МБ | 7 |
| health_pm | 204 | 2 МБ | 1 |
| kr_trade | 118 | 3 МБ | 308653 |
| ok_trade | 203 | 38 МБ | 1 |
| pm_depth | 204 | 41 МБ | 1 |
| pm_rtt | 204 | 1 МБ | 1 |
| pm_top | 204 | 84 МБ | 1 |
| pm_trades | 204 | 61 МБ | 1 |
| rtds | 204 | 13 МБ | 1 |
| windows | 204 | 421 КБ | 308 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 45, всего 295
- Polymarket CLOB: TCP 5, TLS 41, всего 79
- Polymarket gamma: TCP 5, TLS 45, всего 56

## Последние строки журнала записи
```
23:31:55 [cex] Binance 115 сд. задержка p50/p90=145.1/147.5 мс | Coinbase 46 задержка p50=76.0 мс | смещение часов +19.1 мс | lag loop p99/max=2.2/2.2 мс
23:31:55 [cex] binance_futures 168 сд. p50=145.2 мс | bybit 278 сд. p50=113.3 мс | bybit_book 158 сд. p50=110.8 мс | bybit_spot 185 сд. p50=113.6 мс | bybit_spot_book 125 сд. p50=111.3 мс | okx 128 сд. p50=153.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:32:00 [pm] T-179.5s Up 0.25/0.26 Down 0.74/0.75 ptb=81553.8 | CLOB 2990 сообщ., задержка p50/p90=39.4/41.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792193520544 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.9/6.2 мс
23:32:05 [cex] Binance 33 сд. задержка p50/p90=145.0/146.4 мс | Coinbase 57 задержка p50=75.6 мс | смещение часов +19.1 мс | lag loop p99/max=2.0/2.1 мс
23:32:05 [cex] binance_futures 82 сд. p50=145.1 мс | bybit 76 сд. p50=116.4 мс | bybit_book 111 сд. p50=110.8 мс | bybit_spot 137 сд. p50=115.4 мс | bybit_spot_book 52 сд. p50=111.2 мс | okx 96 сд. p50=155.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:32:10 [pm] T-169.5s Up 0.14/0.15 Down 0.85/0.86 ptb=81553.8 | CLOB 5165 сообщ., задержка p50/p90=39.8/46.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792193530545 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.7/2.2 мс
23:32:15 [cex] Binance 62 сд. задержка p50/p90=144.4/144.6 мс | Coinbase 32 задержка p50=75.2 мс | смещение часов +19.1 мс | lag loop p99/max=1.9/2.2 мс
23:32:15 [cex] binance_futures 21 сд. p50=292.7 мс | bybit 5 сд. p50=112.5 мс | bybit_book 95 сд. p50=110.8 мс | bybit_spot 38 сд. p50=114.2 мс | bybit_spot_book 90 сд. p50=111.2 мс | okx 28 сд. p50=153.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:32:20 [pm] T-159.5s Up 0.14/0.15 Down 0.85/0.86 ptb=81553.8 | CLOB 2388 сообщ., задержка p50/p90=39.3/41.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792193540547 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.6/2.2 мс
23:32:25 [cex] Binance 9 сд. задержка p50/p90=143.9/144.0 мс | Coinbase 42 задержка p50=75.6 мс | смещение часов +19.1 мс | lag loop p99/max=2.2/2.2 мс
23:32:25 [cex] binance_futures 24 сд. p50=293.3 мс | bybit 4 сд. p50=112.8 мс | bybit_book 97 сд. p50=110.8 мс | bybit_spot 2 сд. p50=112.9 мс | bybit_spot_book 38 сд. p50=111.3 мс | okx 8 сд. p50=153.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:32:30 [pm] T-149.5s Up 0.18/0.19 Down 0.81/0.82 ptb=81553.8 | CLOB 3075 сообщ., задержка p50/p90=40.1/45.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792193550548 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.0/2.1 мс
23:32:35 [cex] Binance 13 сд. задержка p50/p90=143.9/144.8 мс | Coinbase 33 задержка p50=74.6 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.1 мс
23:32:35 [cex] binance_futures 30 сд. p50=292.7 мс | bybit 43 сд. p50=112.8 мс | bybit_book 87 сд. p50=110.8 мс | bybit_spot 163 сд. p50=114.0 мс | bybit_spot_book 81 сд. p50=111.2 мс | okx 6 сд. p50=153.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:32:40 [pm] T-139.4s Up 0.14/0.15 Down 0.85/0.86 ptb=81553.8 | CLOB 3838 сообщ., задержка p50/p90=39.5/510.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792193560550 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.2/2.4 мс
```

Представлено версией кода: 8083be6; python 3.12.3
