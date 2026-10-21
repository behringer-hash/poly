# Состояние сервера записи

Время (UTC): 2026-10-21 06:29:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 23 hours, 5 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 9 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         681         455           2         957        1224
Swap:           2047         245        1802
```
- нагрузка CPU (1/5/15 мин): 0.36 / 0.40 / 0.38

## Данные
- файлов: 7550, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 308 | 39 МБ | 0 |
| bn_book | 308 | 4 МБ | 50 |
| bnf_agg | 308 | 60 МБ | 0 |
| bnf_book | 118 | 557 МБ | 679262 |
| bnf_depth5 | 118 | 41 МБ | 679339 |
| bnf_liq | 270 | 172 КБ | 25 |
| bs_trade | 118 | 1 МБ | 679258 |
| by_book1 | 308 | 127 МБ | 0 |
| by_liq | 276 | 135 КБ | 957 |
| by_trade | 308 | 39 МБ | 2 |
| bys_book1 | 192 | 64 МБ | 0 |
| bys_trade | 192 | 25 МБ | 0 |
| cb_ticker | 308 | 38 МБ | 0 |
| clock | 308 | 237 КБ | 12 |
| clock_pm | 308 | 237 КБ | 12 |
| events | 297 | 95 КБ | 907 |
| events_pm | 308 | 110 КБ | 58 |
| health_cex | 308 | 3 МБ | 2 |
| health_feeds | 308 | 10 МБ | 2 |
| health_pm | 308 | 3 МБ | 2 |
| kr_trade | 118 | 3 МБ | 679258 |
| ok_trade | 307 | 52 МБ | 0 |
| pm_depth | 308 | 61 МБ | 2 |
| pm_rtt | 308 | 2 МБ | 4 |
| pm_top | 308 | 125 МБ | 2 |
| pm_trades | 308 | 88 МБ | 2 |
| rtds | 308 | 20 МБ | 2 |
| windows | 308 | 633 КБ | 24 |

Дни с данными: 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 45, всего 295
- Polymarket CLOB: TCP 5, TLS 46, всего 89
- Polymarket gamma: TCP 5, TLS 60, всего 70

## Последние строки журнала записи
```
06:28:45 [cex] Binance 61 сд. задержка p50/p90=148.0/149.5 мс | Coinbase 46 задержка p50=83.7 мс | смещение часов +22.6 мс | lag loop p99/max=2.2/2.2 мс
06:28:45 [cex] binance_futures 116 сд. p50=148.4 мс | bybit 88 сд. p50=116.8 мс | bybit_book 77 сд. p50=114.8 мс | bybit_spot 95 сд. p50=133.2 мс | bybit_spot_book 63 сд. p50=114.4 мс | okx 99 сд. p50=149.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:28:45 [pm] T- 74.5s Up 0.28/0.29 Down 0.71/0.72 ptb=82613.2 | CLOB 10327 сообщ., задержка p50/p90=43.2/46.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792564125480 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.2/1.9 мс
06:28:55 [cex] Binance 14 сд. задержка p50/p90=147.5/148.3 мс | Coinbase 26 задержка p50=82.8 мс | смещение часов +22.6 мс | lag loop p99/max=2.1/2.8 мс
06:28:55 [cex] binance_futures 32 сд. p50=148.1 мс | bybit 4 сд. p50=116.0 мс | bybit_book 108 сд. p50=114.8 мс | bybit_spot 4 сд. p50=117.0 мс | bybit_spot_book 42 сд. p50=114.4 мс | okx 14 сд. p50=149.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:28:55 [pm] T- 64.5s Up 0.55/0.56 Down 0.44/0.45 ptb=82613.2 | CLOB 10392 сообщ., задержка p50/p90=43.7/100.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792564135482 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.7/1.9 мс
06:29:05 [cex] Binance 24 сд. задержка p50/p90=147.4/149.0 мс | Coinbase 21 задержка p50=82.7 мс | смещение часов +22.6 мс | lag loop p99/max=2.1/2.9 мс
06:29:05 [cex] binance_futures 12 сд. p50=296.4 мс | bybit 121 сд. p50=118.5 мс | bybit_book 66 сд. p50=114.9 мс | bybit_spot 63 сд. p50=118.9 мс | bybit_spot_book 78 сд. p50=114.5 мс | okx 7 сд. p50=148.9 мс | binance_liq 1 сд. p50=1154.3 мс | bybit_liq 0 сд. p50=n/a мс
06:29:05 [pm] T- 54.5s Up 0.46/0.47 Down 0.53/0.54 ptb=82613.2 | CLOB 10099 сообщ., задержка p50/p90=43.1/44.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792564145483 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.4/2.5 мс
06:29:15 [cex] Binance 25 сд. задержка p50/p90=147.5/148.3 мс | Coinbase 16 задержка p50=82.7 мс | смещение часов +22.6 мс | lag loop p99/max=2.1/2.3 мс
06:29:15 [cex] binance_futures 18 сд. p50=296.7 мс | bybit 14 сд. p50=116.3 мс | bybit_book 69 сд. p50=114.8 мс | bybit_spot 5 сд. p50=116.6 мс | bybit_spot_book 61 сд. p50=114.4 мс | okx 54 сд. p50=150.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:29:15 [pm] T- 44.5s Up 0.35/0.36 Down 0.64/0.65 ptb=82613.2 | CLOB 8930 сообщ., задержка p50/p90=43.1/47.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792564155484 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.4/2.1 мс
06:29:25 [cex] Binance 18 сд. задержка p50/p90=148.1/148.5 мс | Coinbase 30 задержка p50=83.4 мс | смещение часов +23.3 мс | lag loop p99/max=2.1/2.1 мс
06:29:25 [cex] binance_futures 17 сд. p50=296.8 мс | bybit 81 сд. p50=117.5 мс | bybit_book 111 сд. p50=115.4 мс | bybit_spot 20 сд. p50=118.0 мс | bybit_spot_book 99 сд. p50=114.9 мс | okx 69 сд. p50=149.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:29:25 [pm] T- 34.5s Up 0.53/0.54 Down 0.46/0.47 ptb=82613.2 | CLOB 10487 сообщ., задержка p50/p90=41.6/44.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792564165486 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.6/1.7 мс
```

Представлено версией кода: 96010db; python 3.12.3
