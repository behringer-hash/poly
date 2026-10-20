# Состояние сервера записи

Время (UTC): 2026-10-20 08:53:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 1 hour, 29 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         830         160           1        1099        1075
Swap:           2047         250        1797
```
- нагрузка CPU (1/5/15 мин): 0.47 / 0.40 / 0.34

## Данные
- файлов: 7003, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 285 | 38 МБ | 2 |
| bn_book | 285 | 4 МБ | 28 |
| bnf_agg | 285 | 57 МБ | 2 |
| bnf_book | 118 | 557 МБ | 601492 |
| bnf_depth5 | 118 | 41 МБ | 601568 |
| bnf_liq | 248 | 160 КБ | 179 |
| bs_trade | 118 | 1 МБ | 601488 |
| by_book1 | 285 | 120 МБ | 2 |
| by_liq | 257 | 128 КБ | 3051 |
| by_trade | 285 | 38 МБ | 2 |
| bys_book1 | 169 | 59 МБ | 2 |
| bys_trade | 169 | 24 МБ | 2 |
| cb_ticker | 285 | 35 МБ | 2 |
| clock | 285 | 221 КБ | 28 |
| clock_pm | 285 | 221 КБ | 58 |
| events | 274 | 87 КБ | 438 |
| events_pm | 285 | 104 КБ | 104 |
| health_cex | 285 | 3 МБ | 8 |
| health_feeds | 285 | 9 МБ | 8 |
| health_pm | 285 | 3 МБ | 3 |
| kr_trade | 118 | 3 МБ | 601488 |
| ok_trade | 284 | 49 МБ | 2 |
| pm_depth | 285 | 57 МБ | 1 |
| pm_rtt | 285 | 2 МБ | 3 |
| pm_top | 285 | 118 МБ | 1 |
| pm_trades | 285 | 82 МБ | 1 |
| rtds | 285 | 18 МБ | 1 |
| windows | 285 | 590 КБ | 104 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 41, всего 291
- Polymarket CLOB: TCP 4, TLS 36, всего 74
- Polymarket gamma: TCP 4, TLS 36, всего 47

## Последние строки журнала записи
```
08:52:34 [pm] T-145.3s Up 0.19/0.20 Down 0.80/0.81 ptb=81388.3 | CLOB 7359 сообщ., задержка p50/p90=34.9/36.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792486354723 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.6/2.1 мс
08:52:38 [cex] Binance 52 сд. задержка p50/p90=146.2/146.4 мс | Coinbase 19 задержка p50=80.4 мс | смещение часов +21.3 мс | lag loop p99/max=2.1/2.2 мс
08:52:38 [cex] binance_futures 50 сд. p50=262.7 мс | bybit 35 сд. p50=114.7 мс | bybit_book 184 сд. p50=112.9 мс | bybit_spot 106 сд. p50=115.4 мс | bybit_spot_book 58 сд. p50=112.7 мс | okx 81 сд. p50=159.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:52:44 [pm] T-135.3s Up 0.12/0.13 Down 0.87/0.88 ptb=81388.3 | CLOB 6633 сообщ., задержка p50/p90=35.8/45.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792486364725 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.4/1.9 мс
08:52:48 [cex] Binance 83 сд. задержка p50/p90=145.6/146.8 мс | Coinbase 20 задержка p50=82.1 мс | смещение часов +26.7 мс | lag loop p99/max=2.2/2.3 мс
08:52:48 [cex] binance_futures 88 сд. p50=156.3 мс | bybit 167 сд. p50=115.2 мс | bybit_book 230 сд. p50=113.0 мс | bybit_spot 336 сд. p50=115.2 мс | bybit_spot_book 131 сд. p50=112.7 мс | okx 109 сд. p50=159.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:52:54 [pm] T-125.3s Up 0.15/0.16 Down 0.84/0.85 ptb=81388.3 | CLOB 8928 сообщ., задержка p50/p90=35.0/37.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792486374727 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=2.1/2.8 мс
08:52:58 [cex] Binance 16 сд. задержка p50/p90=150.8/151.9 мс | Coinbase 9 задержка p50=85.4 мс | смещение часов +26.7 мс | lag loop p99/max=2.1/2.4 мс
08:52:58 [cex] binance_futures 24 сд. p50=308.5 мс | bybit 56 сд. p50=120.2 мс | bybit_book 159 сд. p50=118.3 мс | bybit_spot 62 сд. p50=120.4 мс | bybit_spot_book 50 сд. p50=118.2 мс | okx 16 сд. p50=164.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:53:04 [pm] T-115.3s Up 0.10/0.11 Down 0.89/0.90 ptb=81388.3 | CLOB 5008 сообщ., задержка p50/p90=35.3/52.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792486384728 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.1/2.2 мс
08:53:08 [cex] Binance 12 сд. задержка p50/p90=150.7/150.9 мс | Coinbase 10 задержка p50=86.4 мс | смещение часов +26.7 мс | lag loop p99/max=2.0/3.1 мс
08:53:08 [cex] binance_futures 27 сд. p50=308.6 мс | bybit 7 сд. p50=120.2 мс | bybit_book 109 сд. p50=118.3 мс | bybit_spot 1 сд. p50=120.9 мс | bybit_spot_book 35 сд. p50=118.1 мс | okx 17 сд. p50=164.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:53:14 [pm] T-105.3s Up 0.10/0.11 Down 0.89/0.90 ptb=81388.3 | CLOB 5147 сообщ., задержка p50/p90=35.1/37.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792486394729 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.9/2.3 мс
08:53:18 [cex] Binance 11 сд. задержка p50/p90=150.8/151.3 мс | Coinbase 40 задержка p50=85.8 мс | смещение часов +26.7 мс | lag loop p99/max=2.1/2.1 мс
08:53:18 [cex] binance_futures 22 сд. p50=308.6 мс | bybit 11 сд. p50=120.2 мс | bybit_book 129 сд. p50=118.3 мс | bybit_spot 11 сд. p50=120.0 мс | bybit_spot_book 47 сд. p50=118.1 мс | okx 20 сд. p50=164.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
