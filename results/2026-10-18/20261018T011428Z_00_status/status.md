# Состояние сервера записи

Время (UTC): 2026-10-18 01:14:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 17 hours, 50 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         849         549           2         795        1057
Swap:           2047         236        1811
```
- нагрузка CPU (1/5/15 мин): 0.39 / 0.26 / 0.20

## Данные
- файлов: 5691, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 230 | 30 МБ | 1 |
| bn_book | 230 | 3 МБ | 26 |
| bnf_agg | 230 | 45 МБ | 1 |
| bnf_book | 118 | 557 МБ | 401162 |
| bnf_depth5 | 118 | 41 МБ | 401238 |
| bnf_liq | 199 | 133 КБ | 2814 |
| bs_trade | 118 | 1 МБ | 401158 |
| by_book1 | 230 | 95 МБ | 1 |
| by_liq | 205 | 109 КБ | 643 |
| by_trade | 230 | 29 МБ | 3 |
| bys_book1 | 114 | 39 МБ | 1 |
| bys_trade | 114 | 16 МБ | 3 |
| cb_ticker | 230 | 28 МБ | 1 |
| clock | 230 | 177 КБ | 19 |
| clock_pm | 230 | 177 КБ | 47 |
| events | 219 | 71 КБ | 361 |
| events_pm | 229 | 83 КБ | 1355 |
| health_cex | 230 | 2 МБ | 1 |
| health_feeds | 230 | 8 МБ | 1 |
| health_pm | 230 | 2 МБ | 2 |
| kr_trade | 118 | 3 МБ | 401158 |
| ok_trade | 229 | 40 МБ | 1 |
| pm_depth | 230 | 46 МБ | 0 |
| pm_rtt | 230 | 1 МБ | 2 |
| pm_top | 230 | 93 МБ | 0 |
| pm_trades | 230 | 67 МБ | 7 |
| rtds | 230 | 15 МБ | 0 |
| windows | 230 | 473 КБ | 228 |

Дни с данными: 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 34, всего 284
- Polymarket CLOB: TCP 5, TLS 36, всего 132
- Polymarket gamma: TCP 5, TLS 39, всего 50

## Последние строки журнала записи
```
01:13:44 [pm] T- 75.6s Up 0.03/0.03 Down 0.97/0.97 ptb=81466.7 | CLOB 4300 сообщ., задержка p50/p90=41.5/66.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792286024355 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.6/2.0 мс
01:13:45 [cex] Binance 12 сд. задержка p50/p90=143.1/143.2 мс | Coinbase 16 задержка p50=75.0 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.1 мс
01:13:45 [cex] binance_futures 18 сд. p50=292.3 мс | bybit 11 сд. p50=112.9 мс | bybit_book 50 сд. p50=110.9 мс | bybit_spot 1 сд. p50=112.6 мс | bybit_spot_book 19 сд. p50=110.6 мс | okx 7 сд. p50=152.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:13:54 [pm] T- 65.6s Up 0.03/0.03 Down 0.97/0.97 ptb=81466.7 | CLOB 4915 сообщ., задержка p50/p90=40.5/49.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792286034356 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.9/2.1 мс
01:13:55 [cex] Binance 15 сд. задержка p50/p90=143.0/144.0 мс | Coinbase 26 задержка p50=77.2 мс | смещение часов +19.1 мс | lag loop p99/max=2.2/2.3 мс
01:13:55 [cex] binance_futures 13 сд. p50=292.6 мс | bybit 5 сд. p50=112.4 мс | bybit_book 48 сд. p50=110.8 мс | bybit_spot 2 сд. p50=113.2 мс | bybit_spot_book 29 сд. p50=110.5 мс | okx 8 сд. p50=152.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:14:04 [pm] T- 55.6s Up 0.01/0.01 Down 0.99/0.99 ptb=81466.7 | CLOB 6266 сообщ., задержка p50/p90=43.6/79.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792286044358 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=16.7/24.6 мс
01:14:05 [cex] Binance 79 сд. задержка p50/p90=143.5/145.4 мс | Coinbase 28 задержка p50=75.7 мс | смещение часов +19.1 мс | lag loop p99/max=6.2/6.4 мс
01:14:05 [cex] binance_futures 27 сд. p50=290.8 мс | bybit 62 сд. p50=113.5 мс | bybit_book 138 сд. p50=110.8 мс | bybit_spot 131 сд. p50=115.1 мс | bybit_spot_book 64 сд. p50=110.7 мс | okx 48 сд. p50=156.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:14:14 [pm] T- 45.6s Up n/a/0.00 Down 1.00/n/a ptb=81466.7 | CLOB 2010 сообщ., задержка p50/p90=39.8/43.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792286054360 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.0/2.4 мс
01:14:15 [cex] Binance 22 сд. задержка p50/p90=143.2/143.3 мс | Coinbase 6 задержка p50=75.1 мс | смещение часов +19.1 мс | lag loop p99/max=2.0/2.1 мс
01:14:15 [cex] binance_futures 14 сд. p50=292.3 мс | bybit 6 сд. p50=112.6 мс | bybit_book 134 сд. p50=110.9 мс | bybit_spot 2 сд. p50=113.0 мс | bybit_spot_book 39 сд. p50=110.6 мс | okx 21 сд. p50=152.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:14:24 [pm] T- 35.6s Up n/a/0.00 Down 1.00/n/a ptb=81466.7 | CLOB 917 сообщ., задержка p50/p90=39.5/41.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792286064361 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.1/2.2 мс
01:14:25 [cex] Binance 38 сд. задержка p50/p90=143.1/144.1 мс | Coinbase 10 задержка p50=75.9 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.2 мс
01:14:25 [cex] binance_futures 16 сд. p50=292.3 мс | bybit 12 сд. p50=112.4 мс | bybit_book 147 сд. p50=110.8 мс | bybit_spot 1 сд. p50=113.0 мс | bybit_spot_book 22 сд. p50=110.5 мс | okx 18 сд. p50=153.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: b24b4e3; python 3.12.3
