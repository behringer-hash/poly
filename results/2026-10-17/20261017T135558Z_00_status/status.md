# Состояние сервера записи

Время (UTC): 2026-10-17 13:55:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 6 hours, 32 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         871         493           2         828        1034
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.08 / 0.21 / 0.24

## Данные
- файлов: 5408, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 218 | 29 МБ | 1 |
| bn_book | 218 | 3 МБ | 5 |
| bnf_agg | 218 | 45 МБ | 1 |
| bnf_book | 118 | 557 МБ | 360452 |
| bnf_depth5 | 118 | 41 МБ | 360528 |
| bnf_liq | 191 | 129 КБ | 795 |
| bs_trade | 118 | 1 МБ | 360448 |
| by_book1 | 218 | 94 МБ | 1 |
| by_liq | 193 | 104 КБ | 1470 |
| by_trade | 218 | 29 МБ | 1 |
| bys_book1 | 102 | 38 МБ | 1 |
| bys_trade | 102 | 15 МБ | 1 |
| cb_ticker | 218 | 28 МБ | 1 |
| clock | 218 | 169 КБ | 26 |
| clock_pm | 218 | 169 КБ | 52 |
| events | 207 | 68 КБ | 186 |
| events_pm | 218 | 80 КБ | 768 |
| health_cex | 218 | 2 МБ | 7 |
| health_feeds | 218 | 7 МБ | 7 |
| health_pm | 218 | 2 МБ | 8 |
| kr_trade | 118 | 3 МБ | 360448 |
| ok_trade | 217 | 39 МБ | 3 |
| pm_depth | 218 | 44 МБ | 0 |
| pm_rtt | 218 | 1 МБ | 4 |
| pm_top | 218 | 91 МБ | 0 |
| pm_trades | 218 | 64 МБ | 0 |
| rtds | 218 | 14 МБ | 0 |
| windows | 218 | 452 КБ | 142 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 39, всего 290
- Polymarket CLOB: TCP 5, TLS 47, всего 93
- Polymarket gamma: TCP 5, TLS 46, всего 57

## Последние строки журнала записи
```
13:55:10 [cex] Binance 51 сд. задержка p50/p90=142.9/143.8 мс | Coinbase 41 задержка p50=75.3 мс | смещение часов +18.6 мс | lag loop p99/max=2.3/8.6 мс
13:55:10 [cex] binance_futures 44 сд. p50=149.7 мс | bybit 77 сд. p50=113.2 мс | bybit_book 102 сд. p50=110.7 мс | bybit_spot 191 сд. p50=114.2 мс | bybit_spot_book 68 сд. p50=110.2 мс | okx 52 сд. p50=153.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:55:18 [pm] T-281.7s Up 0.16/0.17 Down 0.83/0.84 ptb=81415.2 | CLOB 7032 сообщ., задержка p50/p90=37.9/45.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792245318261 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=1.5/1.5 мс
13:55:20 [cex] Binance 17 сд. задержка p50/p90=142.7/142.9 мс | Coinbase 30 задержка p50=74.8 мс | смещение часов +18.6 мс | lag loop p99/max=1.8/1.9 мс
13:55:20 [cex] binance_futures 15 сд. p50=292.3 мс | bybit 6 сд. p50=112.2 мс | bybit_book 47 сд. p50=110.8 мс | bybit_spot 32 сд. p50=112.7 мс | bybit_spot_book 31 сд. p50=110.2 мс | okx 28 сд. p50=153.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:55:28 [pm] T-271.7s Up 0.18/0.19 Down 0.81/0.82 ptb=81415.2 | CLOB 4339 сообщ., задержка p50/p90=37.9/41.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792245328262 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=1.7/2.1 мс
13:55:30 [cex] Binance 16 сд. задержка p50/p90=142.8/143.0 мс | Coinbase 45 задержка p50=74.6 мс | смещение часов +18.6 мс | lag loop p99/max=2.0/2.2 мс
13:55:30 [cex] binance_futures 17 сд. p50=292.2 мс | bybit 4 сд. p50=111.5 мс | bybit_book 73 сд. p50=110.7 мс | bybit_spot 3 сд. p50=112.8 мс | bybit_spot_book 22 сд. p50=110.4 мс | okx 6 сд. p50=153.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:55:38 [pm] T-261.7s Up 0.23/0.24 Down 0.76/0.77 ptb=81415.2 | CLOB 2786 сообщ., задержка p50/p90=37.8/41.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792245338264 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=2.0/2.0 мс
13:55:40 [cex] Binance 10 сд. задержка p50/p90=144.0/145.0 мс | Coinbase 27 задержка p50=76.2 мс | смещение часов +19.9 мс | lag loop p99/max=1.9/2.1 мс
13:55:40 [cex] binance_futures 11 сд. p50=293.2 мс | bybit 35 сд. p50=114.0 мс | bybit_book 95 сд. p50=111.9 мс | bybit_spot 3 сд. p50=114.2 мс | bybit_spot_book 20 сд. p50=111.6 мс | okx 13 сд. p50=154.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:55:48 [pm] T-251.7s Up 0.27/0.29 Down 0.71/0.73 ptb=81415.2 | CLOB 6143 сообщ., задержка p50/p90=38.8/59.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792245348265 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=1.3/2.0 мс
13:55:50 [cex] Binance 53 сд. задержка p50/p90=144.5/144.7 мс | Coinbase 25 задержка p50=76.1 мс | смещение часов +19.9 мс | lag loop p99/max=2.1/2.1 мс
13:55:50 [cex] binance_futures 14 сд. p50=293.4 мс | bybit 16 сд. p50=115.6 мс | bybit_book 57 сд. p50=111.9 мс | bybit_spot 53 сд. p50=115.1 мс | bybit_spot_book 43 сд. p50=111.4 мс | okx 26 сд. p50=154.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:55:58 [pm] T-241.7s Up 0.34/0.35 Down 0.65/0.66 ptb=81415.2 | CLOB 6034 сообщ., задержка p50/p90=37.5/40.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792245358269 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=2.1/2.5 мс
```

Представлено версией кода: 8083be6; python 3.12.3
