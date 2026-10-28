# Состояние сервера записи

Время (UTC): 2026-10-28 04:47:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 6 days, 21 hours, 23 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         605         363           2        1119        1300
Swap:           2047         282        1765
```
- нагрузка CPU (1/5/15 мин): 0.35 / 0.23 / 0.19

## Данные
- файлов: 5807, всего 982 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 34 МБ | 1 |
| bn_book | 242 | 3 МБ | 35 |
| bnf_agg | 242 | 50 МБ | 1 |
| bnf_book | 46 | 310 МБ | 1 |
| bnf_depth5 | 6 | 2 МБ | 1278009 |
| bnf_liq | 212 | 134 КБ | 1449 |
| bs_trade | 6 | 89 КБ | 1277928 |
| by_book1 | 242 | 109 МБ | 1 |
| by_liq | 226 | 97 КБ | 1530 |
| by_trade | 242 | 33 МБ | 3 |
| bys_book1 | 238 | 80 МБ | 1 |
| bys_trade | 238 | 32 МБ | 5 |
| cb_ticker | 242 | 32 МБ | 1 |
| clock | 242 | 188 КБ | 21 |
| clock_pm | 242 | 189 КБ | 43 |
| events | 233 | 76 КБ | 226 |
| events_pm | 241 | 85 КБ | 372 |
| health_cex | 242 | 2 МБ | 7 |
| health_feeds | 242 | 7 МБ | 7 |
| health_pm | 242 | 3 МБ | 9 |
| kr_trade | 6 | 140 КБ | 1277928 |
| ok_trade | 241 | 43 МБ | 1 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 1 |
| pm_top | 242 | 102 МБ | 1 |
| pm_trades | 242 | 71 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 501 КБ | 103 |

Дни с данными: 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 37, всего 284
- Polymarket CLOB: TCP 5, TLS 39, всего 80
- Polymarket gamma: TCP 6, TLS 41, всего 48

## Последние строки журнала записи
```
04:46:29 [pm] T-210.6s Up 0.85/0.86 Down 0.14/0.15 ptb=80883.7 | CLOB 3334 сообщ., задержка p50/p90=38.5/39.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793162789370 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=2.0/2.0 мс
04:46:30 [cex] Binance 23 сд. задержка p50/p90=142.3/142.5 мс | Coinbase 1 задержка p50=79.8 мс | смещение часов +19.4 мс | lag loop p99/max=2.0/2.1 мс
04:46:30 [cex] binance_futures 21 сд. p50=291.9 мс | bybit 4 сд. p50=110.9 мс | bybit_book 51 сд. p50=109.6 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 93 сд. p50=109.6 мс | okx 21 сд. p50=143.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 450 сд. p50=142.9 мс
04:46:39 [pm] T-200.6s Up 0.86/0.87 Down 0.13/0.14 ptb=80883.7 | CLOB 3393 сообщ., задержка p50/p90=37.4/39.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793162799371 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=2.1/2.1 мс
04:46:40 [cex] Binance 19 сд. задержка p50/p90=142.2/143.1 мс | Coinbase 10 задержка p50=80.5 мс | смещение часов +19.4 мс | lag loop p99/max=2.1/2.2 мс
04:46:40 [cex] binance_futures 16 сд. p50=291.9 мс | bybit 7 сд. p50=110.9 мс | bybit_book 66 сд. p50=109.6 мс | bybit_spot 2 сд. p50=111.6 мс | bybit_spot_book 43 сд. p50=109.5 мс | okx 96 сд. p50=143.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 622 сд. p50=143.0 мс
04:46:49 [pm] T-190.6s Up 0.79/0.80 Down 0.20/0.21 ptb=80883.7 | CLOB 7386 сообщ., задержка p50/p90=37.6/41.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793162809373 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=1.2/1.5 мс
04:46:50 [cex] Binance 31 сд. задержка p50/p90=142.3/143.5 мс | Coinbase 32 задержка p50=81.1 мс | смещение часов +19.4 мс | lag loop p99/max=2.2/8.1 мс
04:46:50 [cex] binance_futures 41 сд. p50=291.8 мс | bybit 48 сд. p50=111.2 мс | bybit_book 95 сд. p50=109.6 мс | bybit_spot 78 сд. p50=113.5 мс | bybit_spot_book 74 сд. p50=109.5 мс | okx 23 сд. p50=143.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5006 сд. p50=143.3 мс
04:46:59 [pm] T-180.6s Up 0.83/0.84 Down 0.16/0.17 ptb=80883.7 | CLOB 4341 сообщ., задержка p50/p90=37.5/39.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793162819374 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=1.7/2.0 мс
04:47:00 [cex] Binance 18 сд. задержка p50/p90=142.2/142.7 мс | Coinbase 19 задержка p50=80.1 мс | смещение часов +19.0 мс | lag loop p99/max=1.9/1.9 мс
04:47:00 [cex] binance_futures 17 сд. p50=292.5 мс | bybit 3 сд. p50=110.4 мс | bybit_book 55 сд. p50=109.5 мс | bybit_spot 2 сд. p50=112.0 мс | bybit_spot_book 37 сд. p50=109.3 мс | okx 25 сд. p50=143.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1006 сд. p50=142.7 мс
04:47:09 [pm] T-170.6s Up 0.78/0.79 Down 0.21/0.22 ptb=80883.7 | CLOB 6407 сообщ., задержка p50/p90=37.7/41.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793162829375 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=1.7/3.1 мс
04:47:10 [cex] Binance 29 сд. задержка p50/p90=141.8/142.8 мс | Coinbase 8 задержка p50=78.6 мс | смещение часов +19.0 мс | lag loop p99/max=2.0/2.2 мс
04:47:10 [cex] binance_futures 41 сд. p50=143.9 мс | bybit 27 сд. p50=111.1 мс | bybit_book 95 сд. p50=109.2 мс | bybit_spot 53 сд. p50=111.6 мс | bybit_spot_book 53 сд. p50=109.3 мс | okx 27 сд. p50=142.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2813 сд. p50=143.1 мс
```

Представлено версией кода: adb4c8b; python 3.12.3
