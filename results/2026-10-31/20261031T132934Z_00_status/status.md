# Состояние сервера записи

Время (UTC): 2026-10-31 13:29:34

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 3 days, 6 hours, 5 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         600         926           1         566        1305
Swap:           2047         338        1709
```
- нагрузка CPU (1/5/15 мин): 0.02 / 0.13 / 0.16

## Данные
- файлов: 5859, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 37 МБ | 1 |
| bn_book | 242 | 3 МБ | 21 |
| bnf_agg | 242 | 52 МБ | 1 |
| bnf_book | 121 | 813 МБ | 1 |
| bnf_liq | 210 | 149 КБ | 112 |
| by_book1 | 242 | 113 МБ | 1 |
| by_liq | 224 | 117 КБ | 144 |
| by_trade | 242 | 35 МБ | 1 |
| bys_book1 | 242 | 83 МБ | 1 |
| bys_trade | 242 | 34 МБ | 1 |
| cb_ticker | 242 | 33 МБ | 1 |
| clock | 242 | 188 КБ | 51 |
| clock_pm | 242 | 188 КБ | 29 |
| events | 224 | 71 КБ | 478 |
| events_pm | 241 | 85 КБ | 392 |
| health_cex | 242 | 3 МБ | 1 |
| health_feeds | 242 | 8 МБ | 1 |
| health_pm | 242 | 3 МБ | 0 |
| ok_trade | 242 | 45 МБ | 1 |
| pm_depth | 242 | 50 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 4 |
| pm_top | 242 | 100 МБ | 0 |
| pm_trades | 241 | 70 МБ | 2 |
| rtds | 242 | 16 МБ | 0 |
| windows | 242 | 499 КБ | 0 |

Дни с данными: 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 37, всего 286
- Polymarket CLOB: TCP 5, TLS 37, всего 86
- Polymarket gamma: TCP 3, TLS 37, всего 42

## Последние строки журнала записи
```
13:28:53 [cex] Binance 28 сд. задержка p50/p90=143.5/144.4 мс | Coinbase 36 задержка p50=83.8 мс | смещение часов +19.2 мс | lag loop p99/max=2.2/7.9 мс
13:28:53 [cex] binance_futures 62 сд. p50=287.1 мс | bybit 14 сд. p50=112.6 мс | bybit_book 71 сд. p50=110.5 мс | bybit_spot 34 сд. p50=113.0 мс | bybit_spot_book 146 сд. p50=110.5 мс | okx 13 сд. p50=149.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2612 сд. p50=145.9 мс
13:28:53 [pm] T- 66.7s Up n/a/0.01 Down 0.99/n/a ptb=77403.4 | CLOB 1787 сообщ., задержка p50/p90=41.8/43.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793453333306 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.0/2.2 мс
13:29:03 [cex] Binance 107 сд. задержка p50/p90=143.5/160.0 мс | Coinbase 53 задержка p50=84.5 мс | смещение часов +19.2 мс | lag loop p99/max=3.3/3.5 мс
13:29:03 [cex] binance_futures 111 сд. p50=145.5 мс | bybit 101 сд. p50=118.8 мс | bybit_book 102 сд. p50=110.4 мс | bybit_spot 109 сд. p50=129.2 мс | bybit_spot_book 118 сд. p50=110.6 мс | okx 25 сд. p50=163.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3435 сд. p50=144.7 мс
13:29:03 [pm] T- 56.7s Up n/a/0.01 Down 0.99/n/a ptb=77403.4 | CLOB 1422 сообщ., задержка p50/p90=42.7/84.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793453343307 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.2/4.1 мс
13:29:13 [cex] Binance 44 сд. задержка p50/p90=143.6/151.6 мс | Coinbase 55 задержка p50=84.6 мс | смещение часов +19.2 мс | lag loop p99/max=2.2/7.2 мс
13:29:13 [cex] binance_futures 83 сд. p50=153.8 мс | bybit 94 сд. p50=114.0 мс | bybit_book 147 сд. p50=110.4 мс | bybit_spot 135 сд. p50=114.6 мс | bybit_spot_book 101 сд. p50=110.5 мс | okx 26 сд. p50=158.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2442 сд. p50=144.8 мс
13:29:13 [pm] T- 46.7s Up n/a/0.01 Down 0.99/n/a ptb=77403.4 | CLOB 1501 сообщ., задержка p50/p90=42.1/75.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793453353308 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.1/2.1 мс
13:29:23 [cex] Binance 24 сд. задержка p50/p90=143.4/144.4 мс | Coinbase 32 задержка p50=83.8 мс | смещение часов +19.2 мс | lag loop p99/max=2.2/2.3 мс
13:29:23 [cex] binance_futures 34 сд. p50=292.6 мс | bybit 5 сд. p50=112.1 мс | bybit_book 56 сд. p50=110.4 мс | bybit_spot 13 сд. p50=112.9 мс | bybit_spot_book 53 сд. p50=110.6 мс | okx 15 сд. p50=149.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 425 сд. p50=144.1 мс
13:29:23 [pm] T- 36.7s Up n/a/0.01 Down 0.99/n/a ptb=77403.4 | CLOB 613 сообщ., задержка p50/p90=42.1/161.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793453363309 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.1/2.2 мс
13:29:33 [cex] Binance 26 сд. задержка p50/p90=143.5/144.5 мс | Coinbase 26 задержка p50=84.2 мс | смещение часов +19.2 мс | lag loop p99/max=2.2/2.3 мс
13:29:33 [cex] binance_futures 37 сд. p50=292.6 мс | bybit 10 сд. p50=112.6 мс | bybit_book 101 сд. p50=110.5 мс | bybit_spot 26 сд. p50=112.8 мс | bybit_spot_book 86 сд. p50=110.6 мс | okx 15 сд. p50=149.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 693 сд. p50=144.1 мс
13:29:33 [pm] T- 26.7s Up n/a/0.01 Down 0.99/n/a ptb=77403.4 | CLOB 723 сообщ., задержка p50/p90=41.7/43.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793453373310 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.0/2.1 мс
```

Представлено версией кода: 8047248; python 3.12.3
