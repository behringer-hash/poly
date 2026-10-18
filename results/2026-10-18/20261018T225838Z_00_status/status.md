# Состояние сервера записи

Время (UTC): 2026-10-18 22:58:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 15 hours, 34 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         522        1190           1         362        1383
Swap:           2047         254        1793
```
- нагрузка CPU (1/5/15 мин): 0.23 / 0.19 / 0.17

## Данные
- файлов: 6191, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 251 | 34 МБ | 1 |
| bn_book | 251 | 3 МБ | 1 |
| bnf_agg | 251 | 52 МБ | 1 |
| bnf_book | 118 | 557 МБ | 479412 |
| bnf_depth5 | 118 | 41 МБ | 479488 |
| bnf_liq | 217 | 145 КБ | 21 |
| bs_trade | 118 | 1 МБ | 479408 |
| by_book1 | 251 | 108 МБ | 1 |
| by_liq | 224 | 119 КБ | 834 |
| by_trade | 251 | 36 МБ | 1 |
| bys_book1 | 135 | 48 МБ | 1 |
| bys_trade | 135 | 20 МБ | 1 |
| cb_ticker | 251 | 31 МБ | 1 |
| clock | 251 | 195 КБ | 7 |
| clock_pm | 251 | 195 КБ | 30 |
| events | 240 | 77 КБ | 1362 |
| events_pm | 251 | 91 КБ | 142 |
| health_cex | 251 | 3 МБ | 3 |
| health_feeds | 251 | 8 МБ | 3 |
| health_pm | 251 | 3 МБ | 1 |
| kr_trade | 118 | 3 МБ | 479408 |
| ok_trade | 250 | 45 МБ | 1 |
| pm_depth | 251 | 51 МБ | 1 |
| pm_rtt | 251 | 2 МБ | 3 |
| pm_top | 251 | 104 МБ | 1 |
| pm_trades | 251 | 73 МБ | 1 |
| rtds | 251 | 16 МБ | 1 |
| windows | 251 | 520 КБ | 244 |

Дни с данными: 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 43, всего 294
- Polymarket CLOB: TCP 7, TLS 45, всего 86
- Polymarket gamma: TCP 5, TLS 41, всего 51

## Последние строки журнала записи
```
22:57:54 [cex] Binance 202 сд. задержка p50/p90=146.6/147.4 мс | Coinbase 37 задержка p50=80.1 мс | смещение часов +22.8 мс | lag loop p99/max=2.1/2.3 мс
22:57:54 [cex] binance_futures 61 сд. p50=296.2 мс | bybit 9 сд. p50=116.1 мс | bybit_book 148 сд. p50=114.7 мс | bybit_spot 3 сд. p50=116.3 мс | bybit_spot_book 42 сд. p50=114.3 мс | okx 20 сд. p50=156.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:57:56 [pm] T-123.6s Up 0.46/0.47 Down 0.53/0.54 ptb=81692.3 | CLOB 12542 сообщ., задержка p50/p90=40.6/43.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792364276404 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.1/1.2 мс
22:58:04 [cex] Binance 159 сд. задержка p50/p90=146.6/147.4 мс | Coinbase 37 задержка p50=80.4 мс | смещение часов +22.8 мс | lag loop p99/max=2.1/2.1 мс
22:58:04 [cex] binance_futures 74 сд. p50=262.2 мс | bybit 57 сд. p50=116.5 мс | bybit_book 129 сд. p50=114.8 мс | bybit_spot 141 сд. p50=117.2 мс | bybit_spot_book 50 сд. p50=114.3 мс | okx 80 сд. p50=156.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:58:06 [pm] T-113.6s Up 0.19/0.20 Down 0.80/0.81 ptb=81692.3 | CLOB 10324 сообщ., задержка p50/p90=47.4/147.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792364286405 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=2.9/5.2 мс
22:58:14 [cex] Binance 43 сд. задержка p50/p90=146.5/147.5 мс | Coinbase 48 задержка p50=79.9 мс | смещение часов +22.8 мс | lag loop p99/max=2.2/2.2 мс
22:58:14 [cex] binance_futures 62 сд. p50=171.4 мс | bybit 101 сд. p50=116.4 мс | bybit_book 115 сд. p50=114.8 мс | bybit_spot 96 сд. p50=117.4 мс | bybit_spot_book 70 сд. p50=114.2 мс | okx 64 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:58:16 [pm] T-103.6s Up 0.24/0.25 Down 0.75/0.76 ptb=81692.3 | CLOB 7678 сообщ., задержка p50/p90=42.8/52.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792364296406 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.6/1.8 мс
22:58:24 [cex] Binance 39 сд. задержка p50/p90=146.5/147.5 мс | Coinbase 34 задержка p50=80.0 мс | смещение часов +22.8 мс | lag loop p99/max=2.0/2.2 мс
22:58:24 [cex] binance_futures 27 сд. p50=296.3 мс | bybit 12 сд. p50=115.8 мс | bybit_book 82 сд. p50=114.8 мс | bybit_spot 1 сд. p50=116.6 мс | bybit_spot_book 19 сд. p50=114.4 мс | okx 15 сд. p50=156.3 мс | binance_liq 1 сд. p50=1152.2 мс | bybit_liq 0 сд. p50=n/a мс
22:58:26 [pm] T- 93.6s Up 0.18/0.19 Down 0.81/0.82 ptb=81692.3 | CLOB 9989 сообщ., задержка p50/p90=41.8/47.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792364306407 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.5/1.7 мс
22:58:34 [cex] Binance 49 сд. задержка p50/p90=143.3/146.4 мс | Coinbase 36 задержка p50=78.8 мс | смещение часов +19.5 мс | lag loop p99/max=2.0/2.1 мс
22:58:34 [cex] binance_futures 72 сд. p50=145.3 мс | bybit 60 сд. p50=113.2 мс | bybit_book 115 сд. p50=114.6 мс | bybit_spot 64 сд. p50=113.6 мс | bybit_spot_book 54 сд. p50=111.1 мс | okx 62 сд. p50=153.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:58:36 [pm] T- 83.6s Up 0.06/0.07 Down 0.93/0.94 ptb=81692.3 | CLOB 8660 сообщ., задержка p50/p90=42.0/51.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792364316409 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.9/2.0 мс
```

Представлено версией кода: 88f2465; python 3.12.3
