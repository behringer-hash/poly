# Состояние сервера записи

Время (UTC): 2026-10-13 01:31:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 18 hours, 7 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         747         907           1         437        1158
Swap:           2047         179        1868
```
- нагрузка CPU (1/5/15 мин): 0.45 / 0.54 / 0.71

## Данные
- файлов: 2823, всего 893 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 110 | 14 МБ | 1 |
| bn_book | 110 | 1 МБ | 1 |
| bnf_agg | 110 | 22 МБ | 1 |
| bnf_book | 110 | 609 МБ | 0 |
| bnf_depth5 | 110 | 41 МБ | 1 |
| bnf_liq | 97 | 62 КБ | 435 |
| bs_trade | 110 | 1 МБ | 1 |
| by_book1 | 110 | 44 МБ | 1 |
| by_liq | 93 | 54 КБ | 819 |
| by_trade | 110 | 15 МБ | 1 |
| cb_ticker | 110 | 12 МБ | 1 |
| clock | 110 | 85 КБ | 43 |
| clock_pm | 110 | 85 КБ | 3 |
| events | 103 | 35 КБ | 682 |
| events_pm | 110 | 42 КБ | 976 |
| health_cex | 110 | 1 МБ | 7 |
| health_feeds | 110 | 4 МБ | 7 |
| health_pm | 110 | 1 МБ | 9 |
| kr_trade | 110 | 3 МБ | 1 |
| ok_trade | 110 | 19 МБ | 1 |
| pm_depth | 110 | 22 МБ | 1 |
| pm_rtt | 110 | 744 КБ | 3 |
| pm_top | 110 | 44 МБ | 1 |
| pm_trades | 110 | 31 МБ | 1 |
| rtds | 110 | 7 МБ | 1 |
| windows | 110 | 227 КБ | 103 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 53, всего 301
- Polymarket CLOB: TCP 5, TLS 60, всего 100
- Polymarket gamma: TCP 5, TLS 51, всего 62

## Последние строки журнала записи
```
01:30:59 [pm] T-240.7s Up 0.39/0.40 Down 0.60/0.61 ptb=81996.7 | CLOB 9328 сообщ., задержка p50/p90=40.9/42.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791855059324 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.5/2.9 мс
01:31:00 [cex] Binance 50 сд. задержка p50/p90=145.5/146.1 мс | Coinbase 28 задержка p50=82.7 мс | смещение часов +20.9 мс | lag loop p99/max=2.4/2.6 мс
01:31:00 [cex] binance_futures 107 сд. p50=150.6 мс | bybit 61 сд. p50=116.3 мс | okx 113 сд. p50=149.2 мс | binance_futures_book 2098 сд. p50=147.3 мс | binance_futures_depth 94 сд. p50=145.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 230 сд. p50=112.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 17 сд. p50=42.9 мс | bitstamp 6 сд. p50=56.4 мс
01:31:09 [pm] T-230.7s Up 0.49/0.50 Down 0.50/0.51 ptb=81996.7 | CLOB 10128 сообщ., задержка p50/p90=42.2/49.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791855069325 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=5.0/14.4 мс
01:31:10 [cex] Binance 159 сд. задержка p50/p90=148.0/150.8 мс | Coinbase 38 задержка p50=85.4 мс | смещение часов +23.6 мс | lag loop p99/max=2.7/3.0 мс
01:31:10 [cex] binance_futures 188 сд. p50=153.0 мс | bybit 215 сд. p50=117.5 мс | okx 219 сд. p50=151.9 мс | binance_futures_book 7288 сд. p50=148.8 мс | binance_futures_depth 98 сд. p50=148.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 360 сд. p50=115.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 45 сд. p50=57.1 мс | bitstamp 7 сд. p50=52.1 мс
01:31:19 [pm] T-220.7s Up 0.48/0.49 Down 0.51/0.52 ptb=81996.7 | CLOB 11496 сообщ., задержка p50/p90=42.4/59.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791855079327 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.8/2.0 мс
01:31:20 [cex] Binance 64 сд. задержка p50/p90=148.0/154.7 мс | Coinbase 49 задержка p50=86.3 мс | смещение часов +23.6 мс | lag loop p99/max=2.2/3.9 мс
01:31:20 [cex] binance_futures 112 сд. p50=158.0 мс | bybit 143 сд. p50=117.9 мс | okx 136 сд. p50=153.0 мс | binance_futures_book 6502 сд. p50=148.9 мс | binance_futures_depth 95 сд. p50=148.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 263 сд. p50=115.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 27 сд. p50=58.6 мс | bitstamp 8 сд. p50=63.9 мс
01:31:29 [pm] T-210.7s Up 0.45/0.46 Down 0.54/0.55 ptb=81996.7 | CLOB 10986 сообщ., задержка p50/p90=40.8/43.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791855089329 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=4.5/24.6 мс
01:31:30 [cex] Binance 92 сд. задержка p50/p90=149.2/156.3 мс | Coinbase 47 задержка p50=85.9 мс | смещение часов +23.6 мс | lag loop p99/max=2.0/2.2 мс
01:31:30 [cex] binance_futures 146 сд. p50=155.2 мс | bybit 209 сд. p50=118.0 мс | okx 137 сд. p50=152.4 мс | binance_futures_book 5152 сд. p50=148.8 мс | binance_futures_depth 96 сд. p50=148.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 248 сд. p50=115.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 42 сд. p50=47.8 мс | bitstamp 6 сд. p50=52.2 мс
01:31:39 [pm] T-200.7s Up 0.65/0.66 Down 0.34/0.35 ptb=81996.7 | CLOB 12731 сообщ., задержка p50/p90=41.4/46.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791855099330 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.9/4.6 мс
01:31:40 [cex] Binance 128 сд. задержка p50/p90=148.3/150.4 мс | Coinbase 57 задержка p50=86.0 мс | смещение часов +23.6 мс | lag loop p99/max=3.0/3.3 мс
01:31:40 [cex] binance_futures 221 сд. p50=153.6 мс | bybit 169 сд. p50=117.9 мс | okx 237 сд. p50=154.1 мс | binance_futures_book 4419 сд. p50=148.7 мс | binance_futures_depth 98 сд. p50=148.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 307 сд. p50=115.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 47 сд. p50=49.1 мс | bitstamp 5 сд. p50=59.8 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
