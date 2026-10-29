# Состояние сервера записи

Время (UTC): 2026-10-29 10:44:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 3 hours, 20 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         539         663           1         881        1366
Swap:           2047         316        1731
```
- нагрузка CPU (1/5/15 мин): 0.28 / 0.33 / 0.26

## Данные
- файлов: 5818, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 36 МБ | 1 |
| bn_book | 242 | 3 МБ | 15 |
| bnf_agg | 242 | 50 МБ | 1 |
| bnf_book | 70 | 446 МБ | 0 |
| bnf_liq | 211 | 138 КБ | 49 |
| by_book1 | 242 | 111 МБ | 1 |
| by_liq | 224 | 100 КБ | 188 |
| by_trade | 242 | 34 МБ | 1 |
| bys_book1 | 242 | 83 МБ | 1 |
| bys_trade | 242 | 33 МБ | 1 |
| cb_ticker | 242 | 32 МБ | 1 |
| clock | 242 | 188 КБ | 5 |
| clock_pm | 242 | 188 КБ | 40 |
| events | 232 | 73 КБ | 1055 |
| events_pm | 241 | 84 КБ | 367 |
| health_cex | 242 | 3 МБ | 7 |
| health_feeds | 242 | 8 МБ | 7 |
| health_pm | 242 | 3 МБ | 1 |
| ok_trade | 242 | 43 МБ | 1 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 4 |
| pm_top | 242 | 102 МБ | 1 |
| pm_trades | 242 | 72 МБ | 4 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 500 КБ | 243 |

Дни с данными: 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 36, всего 287
- Polymarket CLOB: TCP 5, TLS 38, всего 80
- Polymarket gamma: TCP 5, TLS 36, всего 45

## Последние строки журнала записи
```
10:43:19 [cex] Binance 159 сд. задержка p50/p90=143.5/148.8 мс | Coinbase 29 задержка p50=104.3 мс | смещение часов +18.8 мс | lag loop p99/max=2.1/2.2 мс
10:43:19 [cex] binance_futures 129 сд. p50=153.8 мс | bybit 37 сд. p50=112.3 мс | bybit_book 180 сд. p50=110.3 мс | bybit_spot 162 сд. p50=116.5 мс | bybit_spot_book 85 сд. p50=111.4 мс | okx 50 сд. p50=146.5 мс | binance_liq 1 сд. p50=1146.0 мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2669 сд. p50=144.2 мс
10:43:25 [pm] T- 94.0s Up 0.08/0.08 Down 0.92/0.92 ptb=80144.4 | CLOB 6754 сообщ., задержка p50/p90=41.5/43.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793270605990 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.1/2.2 мс
10:43:29 [cex] Binance 159 сд. задержка p50/p90=143.8/145.4 мс | Coinbase 24 задержка p50=90.7 мс | смещение часов +18.8 мс | lag loop p99/max=2.1/6.7 мс
10:43:29 [cex] binance_futures 77 сд. p50=257.5 мс | bybit 39 сд. p50=112.3 мс | bybit_book 127 сд. p50=110.2 мс | bybit_spot 148 сд. p50=113.0 мс | bybit_spot_book 63 сд. p50=111.2 мс | okx 57 сд. p50=146.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1600 сд. p50=143.7 мс
10:43:35 [pm] T- 84.0s Up 0.07/0.07 Down 0.93/0.93 ptb=80144.4 | CLOB 12262 сообщ., задержка p50/p90=40.0/42.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793270615992 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.1/2.1 мс
10:43:39 [cex] Binance 132 сд. задержка p50/p90=143.5/144.4 мс | Coinbase 27 задержка p50=91.6 мс | смещение часов +18.8 мс | lag loop p99/max=2.0/2.0 мс
10:43:39 [cex] binance_futures 59 сд. p50=292.1 мс | bybit 43 сд. p50=112.8 мс | bybit_book 158 сд. p50=110.2 мс | bybit_spot 61 сд. p50=112.8 мс | bybit_spot_book 65 сд. p50=111.3 мс | okx 76 сд. p50=146.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1781 сд. p50=143.6 мс
10:43:45 [pm] T- 74.0s Up 0.06/0.06 Down 0.94/0.94 ptb=80144.4 | CLOB 5704 сообщ., задержка p50/p90=39.7/50.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793270625994 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.9/2.1 мс
10:43:49 [cex] Binance 105 сд. задержка p50/p90=143.4/144.3 мс | Coinbase 12 задержка p50=89.7 мс | смещение часов +18.8 мс | lag loop p99/max=1.7/2.2 мс
10:43:49 [cex] binance_futures 64 сд. p50=292.0 мс | bybit 30 сд. p50=112.3 мс | bybit_book 168 сд. p50=110.2 мс | bybit_spot 74 сд. p50=112.5 мс | bybit_spot_book 59 сд. p50=111.3 мс | okx 16 сд. p50=145.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1298 сд. p50=143.5 мс
10:43:55 [pm] T- 64.0s Up 0.02/0.02 Down 0.98/0.98 ptb=80144.4 | CLOB 4606 сообщ., задержка p50/p90=40.0/45.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793270635995 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.1/2.2 мс
10:43:59 [cex] Binance 120 сд. задержка p50/p90=143.4/144.8 мс | Coinbase 6 задержка p50=99.3 мс | смещение часов +18.8 мс | lag loop p99/max=2.2/3.2 мс
10:43:59 [cex] binance_futures 91 сд. p50=231.4 мс | bybit 44 сд. p50=112.2 мс | bybit_book 138 сд. p50=110.1 мс | bybit_spot 70 сд. p50=116.1 мс | bybit_spot_book 55 сд. p50=111.4 мс | okx 95 сд. p50=146.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3053 сд. p50=143.6 мс
10:44:05 [pm] T- 54.0s Up n/a/0.00 Down 1.00/n/a ptb=80144.4 | CLOB 3155 сообщ., задержка p50/p90=39.7/42.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793270645997 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.6/1.9 мс
```

Представлено версией кода: c4da76d; python 3.12.3
