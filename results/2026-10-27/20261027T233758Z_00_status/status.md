# Состояние сервера записи

Время (UTC): 2026-10-27 23:37:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 6 days, 16 hours, 14 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         581         804           2         694        1324
Swap:           2047         282        1765
```
- нагрузка CPU (1/5/15 мин): 0.27 / 0.19 / 0.18

## Данные
- файлов: 5813, всего 1018 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 0 |
| bn_book | 242 | 3 МБ | 27 |
| bnf_agg | 242 | 51 МБ | 0 |
| bnf_book | 46 | 338 МБ | 0 |
| bnf_depth5 | 11 | 5 МБ | 1259448 |
| bnf_liq | 213 | 141 КБ | 2590 |
| bs_trade | 11 | 212 КБ | 1259368 |
| by_book1 | 242 | 111 МБ | 0 |
| by_liq | 226 | 103 КБ | 316 |
| by_trade | 242 | 34 МБ | 0 |
| bys_book1 | 233 | 78 МБ | 0 |
| bys_trade | 233 | 31 МБ | 13 |
| cb_ticker | 242 | 32 МБ | 2 |
| clock | 242 | 188 КБ | 23 |
| clock_pm | 242 | 188 КБ | 42 |
| events | 233 | 75 КБ | 148 |
| events_pm | 241 | 83 КБ | 651 |
| health_cex | 242 | 2 МБ | 0 |
| health_feeds | 242 | 7 МБ | 0 |
| health_pm | 242 | 3 МБ | 2 |
| kr_trade | 11 | 378 КБ | 1259368 |
| ok_trade | 241 | 44 МБ | 0 |
| pm_depth | 242 | 50 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 4 |
| pm_top | 242 | 102 МБ | 2 |
| pm_trades | 242 | 71 МБ | 2 |
| rtds | 242 | 16 МБ | 2 |
| windows | 242 | 500 КБ | 264 |

Дни с данными: 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 39, всего 285
- Polymarket CLOB: TCP 6, TLS 42, всего 86
- Polymarket gamma: TCP 4, TLS 38, всего 44

## Последние строки журнала записи
```
23:37:16 [pm] T-163.3s Up 0.78/0.79 Down 0.21/0.22 ptb=80710.4 | CLOB 8165 сообщ., задержка p50/p90=40.4/41.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793144236727 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.8 мс | lag loop p99/max=1.7/1.9 мс
23:37:18 [cex] Binance 262 сд. задержка p50/p90=141.1/142.1 мс | Coinbase 31 задержка p50=88.6 мс | смещение часов +17.9 мс | lag loop p99/max=2.1/3.5 мс
23:37:18 [cex] binance_futures 116 сд. p50=143.3 мс | bybit 103 сд. p50=109.9 мс | bybit_book 131 сд. p50=107.5 мс | bybit_spot 160 сд. p50=111.4 мс | bybit_spot_book 99 сд. p50=107.9 мс | okx 101 сд. p50=143.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2111 сд. p50=143.4 мс
23:37:26 [pm] T-153.3s Up 0.81/0.82 Down 0.18/0.19 ptb=80710.4 | CLOB 5113 сообщ., задержка p50/p90=40.2/41.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793144246728 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.8 мс | lag loop p99/max=1.3/2.0 мс
23:37:28 [cex] Binance 131 сд. задержка p50/p90=144.4/148.3 мс | Coinbase 3 задержка p50=88.1 мс | смещение часов +17.9 мс | lag loop p99/max=2.2/4.8 мс
23:37:28 [cex] binance_futures 80 сд. p50=142.4 мс | bybit 23 сд. p50=109.6 мс | bybit_book 106 сд. p50=107.6 мс | bybit_spot 52 сд. p50=110.7 мс | bybit_spot_book 55 сд. p50=107.9 мс | okx 43 сд. p50=142.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1994 сд. p50=142.5 мс
23:37:36 [pm] T-143.3s Up 0.85/0.86 Down 0.14/0.15 ptb=80710.4 | CLOB 3591 сообщ., задержка p50/p90=40.4/42.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793144256729 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.8 мс | lag loop p99/max=2.1/2.2 мс
23:37:38 [cex] Binance 44 сд. задержка p50/p90=142.3/143.3 мс | Coinbase 12 задержка p50=90.2 мс | смещение часов +17.7 мс | lag loop p99/max=2.0/2.3 мс
23:37:38 [cex] binance_futures 46 сд. p50=146.3 мс | bybit 28 сд. p50=109.9 мс | bybit_book 75 сд. p50=107.4 мс | bybit_spot 30 сд. p50=109.9 мс | bybit_spot_book 47 сд. p50=107.9 мс | okx 79 сд. p50=142.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1025 сд. p50=141.4 мс
23:37:46 [pm] T-133.3s Up 0.84/0.85 Down 0.15/0.16 ptb=80710.4 | CLOB 5598 сообщ., задержка p50/p90=40.7/49.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793144266731 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.9 мс | lag loop p99/max=1.3/2.0 мс
23:37:48 [cex] Binance 34 сд. задержка p50/p90=140.9/142.7 мс | Coinbase 10 задержка p50=87.1 мс | смещение часов +17.7 мс | lag loop p99/max=2.2/2.2 мс
23:37:48 [cex] binance_futures 32 сд. p50=290.1 мс | bybit 13 сд. p50=109.7 мс | bybit_book 92 сд. p50=107.4 мс | bybit_spot 22 сд. p50=111.5 мс | bybit_spot_book 51 сд. p50=107.8 мс | okx 13 сд. p50=141.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1632 сд. p50=141.5 мс
23:37:56 [pm] T-123.3s Up 0.85/0.86 Down 0.14/0.15 ptb=80710.4 | CLOB 2951 сообщ., задержка p50/p90=40.4/41.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793144276733 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.9 мс | lag loop p99/max=1.9/2.1 мс
23:37:58 [cex] Binance 9 сд. задержка p50/p90=140.4/140.6 мс | Coinbase 3 задержка p50=87.0 мс | смещение часов +17.7 мс | lag loop p99/max=2.1/2.1 мс
23:37:58 [cex] binance_futures 19 сд. p50=290.2 мс | bybit 3 сд. p50=109.6 мс | bybit_book 67 сд. p50=107.5 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 40 сд. p50=107.7 мс | okx 16 сд. p50=141.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 632 сд. p50=141.2 мс
```

Представлено версией кода: adb4c8b; python 3.12.3
