# Состояние сервера записи

Время (UTC): 2026-10-16 21:29:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 14 hours, 5 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         812         986           2         386        1093
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.16 / 0.22 / 0.24

## Данные
- файлов: 5034, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 202 | 28 МБ | 2 |
| bn_book | 202 | 3 МБ | 18 |
| bnf_agg | 202 | 43 МБ | 2 |
| bnf_book | 118 | 557 МБ | 301272 |
| bnf_depth5 | 118 | 41 МБ | 301348 |
| bnf_liq | 181 | 126 КБ | 2206 |
| bs_trade | 118 | 1 МБ | 301268 |
| by_book1 | 202 | 90 МБ | 2 |
| by_liq | 181 | 103 КБ | 248 |
| by_trade | 202 | 28 МБ | 4 |
| bys_book1 | 86 | 35 МБ | 2 |
| bys_trade | 86 | 15 МБ | 4 |
| cb_ticker | 202 | 26 МБ | 2 |
| clock | 202 | 156 КБ | 45 |
| clock_pm | 202 | 156 КБ | 61 |
| events | 191 | 61 КБ | 371 |
| events_pm | 202 | 76 КБ | 116 |
| health_cex | 202 | 2 МБ | 4 |
| health_feeds | 202 | 7 МБ | 4 |
| health_pm | 202 | 2 МБ | 8 |
| kr_trade | 118 | 3 МБ | 301268 |
| ok_trade | 201 | 38 МБ | 2 |
| pm_depth | 202 | 41 МБ | 1 |
| pm_rtt | 202 | 1 МБ | 1 |
| pm_top | 202 | 83 МБ | 1 |
| pm_trades | 202 | 60 МБ | 6 |
| rtds | 202 | 13 МБ | 1 |
| windows | 202 | 417 КБ | 4 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 35, всего 286
- Polymarket CLOB: TCP 5, TLS 39, всего 80
- Polymarket gamma: TCP 5, TLS 38, всего 49

## Последние строки журнала записи
```
21:28:49 [pm] T- 70.6s Up 0.01/0.02 Down 0.98/0.99 ptb=81658.3 | CLOB 2792 сообщ., задержка p50/p90=59.1/63.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792186129429 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.6/2.0 мс
21:28:54 [cex] Binance 11 сд. задержка p50/p90=144.9/145.4 мс | Coinbase 58 задержка p50=76.1 мс | смещение часов +19.7 мс | lag loop p99/max=2.0/2.4 мс
21:28:54 [cex] binance_futures 14 сд. p50=293.8 мс | bybit 25 сд. p50=113.4 мс | bybit_book 73 сд. p50=112.5 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 34 сд. p50=112.7 мс | okx 9 сд. p50=154.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:28:59 [pm] T- 60.6s Up 0.01/0.02 Down 0.98/0.99 ptb=81658.3 | CLOB 2177 сообщ., задержка p50/p90=58.8/108.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792186139431 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=1.4/1.6 мс
21:29:04 [cex] Binance 22 сд. задержка p50/p90=144.5/145.2 мс | Coinbase 101 задержка p50=75.9 мс | смещение часов +19.7 мс | lag loop p99/max=2.0/2.6 мс
21:29:04 [cex] binance_futures 42 сд. p50=147.2 мс | bybit 99 сд. p50=113.2 мс | bybit_book 90 сд. p50=111.8 мс | bybit_spot 202 сд. p50=114.0 мс | bybit_spot_book 55 сд. p50=111.7 мс | okx 89 сд. p50=154.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:29:09 [pm] T- 50.6s Up n/a/0.01 Down 0.99/n/a ptb=81658.3 | CLOB 1709 сообщ., задержка p50/p90=59.2/63.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792186149432 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=1.6/1.7 мс
21:29:14 [cex] Binance 35 сд. задержка p50/p90=144.3/144.5 мс | Coinbase 30 задержка p50=75.6 мс | смещение часов +19.7 мс | lag loop p99/max=2.0/2.1 мс
21:29:14 [cex] binance_futures 33 сд. p50=144.3 мс | bybit 27 сд. p50=113.0 мс | bybit_book 59 сд. p50=111.7 мс | bybit_spot 25 сд. p50=113.5 мс | bybit_spot_book 58 сд. p50=111.6 мс | okx 15 сд. p50=153.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:29:19 [pm] T- 40.6s Up n/a/0.00 Down 1.00/n/a ptb=81658.3 | CLOB 824 сообщ., задержка p50/p90=58.7/59.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792186159433 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=1.7/1.9 мс
21:29:24 [cex] Binance 34 сд. задержка p50/p90=144.4/144.7 мс | Coinbase 48 задержка p50=75.9 мс | смещение часов +19.7 мс | lag loop p99/max=2.0/2.2 мс
21:29:24 [cex] binance_futures 18 сд. p50=293.4 мс | bybit 39 сд. p50=114.0 мс | bybit_book 53 сд. p50=111.7 мс | bybit_spot 1 сд. p50=113.4 мс | bybit_spot_book 26 сд. p50=111.7 мс | okx 20 сд. p50=154.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:29:29 [pm] T- 30.6s Up n/a/0.00 Down 1.00/n/a ptb=81658.3 | CLOB 637 сообщ., задержка p50/p90=58.6/59.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792186169434 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.1/2.1 мс
21:29:34 [cex] Binance 6 сд. задержка p50/p90=144.1/144.1 мс | Coinbase 37 задержка p50=75.9 мс | смещение часов +19.7 мс | lag loop p99/max=1.9/1.9 мс
21:29:34 [cex] binance_futures 14 сд. p50=293.5 мс | bybit 14 сд. p50=113.4 мс | bybit_book 60 сд. p50=111.7 мс | bybit_spot 7 сд. p50=113.0 мс | bybit_spot_book 24 сд. p50=111.9 мс | okx 19 сд. p50=153.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 8083be6; python 3.12.3
