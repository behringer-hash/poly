# Состояние сервера записи

Время (UTC): 2026-10-17 19:03:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 11 hours, 40 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         882         471           2         840        1023
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.21 / 0.24 / 0.19

## Данные
- файлов: 5548, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 224 | 29 МБ | 2 |
| bn_book | 224 | 3 МБ | 16 |
| bnf_agg | 224 | 45 МБ | 2 |
| bnf_book | 118 | 557 МБ | 378932 |
| bnf_depth5 | 118 | 41 МБ | 379008 |
| bnf_liq | 196 | 132 КБ | 2734 |
| bs_trade | 118 | 1 МБ | 378928 |
| by_book1 | 224 | 93 МБ | 2 |
| by_liq | 198 | 106 КБ | 2717 |
| by_trade | 224 | 29 МБ | 2 |
| bys_book1 | 108 | 38 МБ | 2 |
| bys_trade | 108 | 15 МБ | 2 |
| cb_ticker | 224 | 28 МБ | 2 |
| clock | 224 | 172 КБ | 63 |
| clock_pm | 224 | 172 КБ | 29 |
| events | 212 | 70 КБ | 287 |
| events_pm | 223 | 81 КБ | 389 |
| health_cex | 224 | 2 МБ | 4 |
| health_feeds | 224 | 8 МБ | 4 |
| health_pm | 224 | 2 МБ | 7 |
| kr_trade | 118 | 3 МБ | 378928 |
| ok_trade | 223 | 39 МБ | 2 |
| pm_depth | 224 | 44 МБ | 1 |
| pm_rtt | 224 | 1 МБ | 3 |
| pm_top | 224 | 90 МБ | 1 |
| pm_trades | 224 | 65 МБ | 1 |
| rtds | 224 | 14 МБ | 1 |
| windows | 224 | 460 КБ | 112 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 42, всего 292
- Polymarket CLOB: TCP 5, TLS 40, всего 80
- Polymarket gamma: TCP 5, TLS 41, всего 54

## Последние строки журнала записи
```
19:03:10 [pm] T-109.0s Up 0.94/0.95 Down 0.05/0.06 ptb=81413.3 | CLOB 4067 сообщ., задержка p50/p90=40.5/44.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792263790965 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.8/2.0 мс
19:03:12 [cex] Binance 198 сд. задержка p50/p90=145.1/145.9 мс | Coinbase 44 задержка p50=78.2 мс | смещение часов +21.1 мс | lag loop p99/max=2.1/2.4 мс
19:03:12 [cex] binance_futures 41 сд. p50=295.3 мс | bybit 29 сд. p50=115.1 мс | bybit_book 205 сд. p50=113.2 мс | bybit_spot 19 сд. p50=116.3 мс | bybit_spot_book 258 сд. p50=112.9 мс | okx 96 сд. p50=154.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:03:20 [pm] T- 99.0s Up 0.95/0.96 Down 0.04/0.05 ptb=81413.3 | CLOB 2926 сообщ., задержка p50/p90=43.2/54.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792263800967 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.7/1.9 мс
19:03:22 [cex] Binance 15 сд. задержка p50/p90=144.9/146.0 мс | Coinbase 31 задержка p50=77.7 мс | смещение часов +21.1 мс | lag loop p99/max=2.2/2.2 мс
19:03:22 [cex] binance_futures 18 сд. p50=295.7 мс | bybit 27 сд. p50=115.4 мс | bybit_book 181 сд. p50=113.2 мс | bybit_spot 23 сд. p50=114.9 мс | bybit_spot_book 283 сд. p50=112.9 мс | okx 69 сд. p50=154.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:03:30 [pm] T- 89.0s Up 0.88/0.89 Down 0.11/0.12 ptb=81413.3 | CLOB 3205 сообщ., задержка p50/p90=45.3/67.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792263810969 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.1/3.2 мс
19:03:32 [cex] Binance 23 сд. задержка p50/p90=145.0/146.3 мс | Coinbase 40 задержка p50=78.1 мс | смещение часов +21.1 мс | lag loop p99/max=2.1/2.2 мс
19:03:32 [cex] binance_futures 31 сд. p50=295.2 мс | bybit 143 сд. p50=118.0 мс | bybit_book 130 сд. p50=113.1 мс | bybit_spot 101 сд. p50=117.2 мс | bybit_spot_book 179 сд. p50=113.0 мс | okx 112 сд. p50=158.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:03:40 [pm] T- 79.0s Up 0.92/0.93 Down 0.07/0.08 ptb=81413.3 | CLOB 2855 сообщ., задержка p50/p90=39.8/42.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792263820970 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.8/2.1 мс
19:03:42 [cex] Binance 39 сд. задержка p50/p90=145.3/146.2 мс | Coinbase 34 задержка p50=78.5 мс | смещение часов +21.1 мс | lag loop p99/max=1.9/2.0 мс
19:03:42 [cex] binance_futures 95 сд. p50=146.8 мс | bybit 84 сд. p50=118.2 мс | bybit_book 70 сд. p50=113.2 мс | bybit_spot 125 сд. p50=115.6 мс | bybit_spot_book 69 сд. p50=113.0 мс | okx 59 сд. p50=155.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:03:50 [pm] T- 69.0s Up 0.73/0.76 Down 0.24/0.27 ptb=81413.3 | CLOB 5345 сообщ., задержка p50/p90=40.1/47.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792263830971 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.5/1.7 мс
19:03:52 [cex] Binance 20 сд. задержка p50/p90=144.9/145.4 мс | Coinbase 34 задержка p50=77.7 мс | смещение часов +21.1 мс | lag loop p99/max=2.0/2.2 мс
19:03:52 [cex] binance_futures 19 сд. p50=295.2 мс | bybit 5 сд. p50=115.2 мс | bybit_book 46 сд. p50=113.2 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 44 сд. p50=113.1 мс | okx 10 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 8083be6; python 3.12.3
