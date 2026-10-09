# Состояние сервера записи

Время (UTC): 2026-10-09 15:30:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 8 hours, 6 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         657         744           2         698        1248
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.29 / 0.27 / 0.32

## Данные
- файлов: 723, всего 368 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 28 | 5 МБ | 0 |
| bn_book | 28 | 565 КБ | 0 |
| bnf_agg | 28 | 10 МБ | 0 |
| bnf_book | 28 | 266 МБ | 0 |
| bnf_depth5 | 28 | 14 МБ | 0 |
| bnf_liq | 28 | 25 КБ | 227 |
| bs_trade | 28 | 597 КБ | 2 |
| by_book1 | 28 | 18 МБ | 0 |
| by_liq | 26 | 26 КБ | 1307 |
| by_trade | 28 | 7 МБ | 0 |
| cb_ticker | 28 | 5 МБ | 0 |
| clock | 28 | 22 КБ | 15 |
| clock_pm | 28 | 22 КБ | 24 |
| events | 25 | 8 КБ | 1209 |
| events_pm | 28 | 13 КБ | 300 |
| health_cex | 28 | 304 КБ | 9 |
| health_feeds | 28 | 1 МБ | 9 |
| health_pm | 28 | 310 КБ | 10 |
| kr_trade | 28 | 1 МБ | 0 |
| ok_trade | 28 | 9 МБ | 0 |
| pm_depth | 28 | 6 МБ | 2 |
| pm_rtt | 28 | 198 КБ | 6 |
| pm_top | 28 | 13 МБ | 2 |
| pm_trades | 28 | 9 МБ | 2 |
| rtds | 28 | 2 МБ | 2 |
| windows | 28 | 58 КБ | 165 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 45, всего 295
- Polymarket CLOB: TCP 6, TLS 49, всего 100
- Polymarket gamma: TCP 5, TLS 49, всего 62

## Последние строки журнала записи
```
15:30:06 [pm] T-293.5s Up 0.38/0.39 Down 0.61/0.62 ptb=82852.4 | CLOB 6179 сообщ., задержка p50/p90=97.5/307.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791559806484 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=21.8/46.7 мс
15:30:08 [cex] Binance 89 сд. задержка p50/p90=144.2/152.3 мс | Coinbase 54 задержка p50=81.3 мс | смещение часов +19.5 мс | lag loop p99/max=8.4/8.6 мс
15:30:08 [cex] binance_futures 156 сд. p50=148.7 мс | bybit 155 сд. p50=114.0 мс | okx 92 сд. p50=157.7 мс | binance_futures_book 4718 сд. p50=144.2 мс | binance_futures_depth 98 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 172 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 31 сд. p50=55.7 мс | bitstamp 5 сд. p50=51.1 мс
15:30:16 [pm] T-283.5s Up 0.41/0.42 Down 0.58/0.59 ptb=82852.4 | CLOB 7478 сообщ., задержка p50/p90=1150.7/1477.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791559816485 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=2.1/2.9 мс
15:30:18 [cex] Binance 87 сд. задержка p50/p90=144.0/147.1 мс | Coinbase 53 задержка p50=80.2 мс | смещение часов +19.5 мс | lag loop p99/max=3.2/4.6 мс
15:30:18 [cex] binance_futures 158 сд. p50=152.6 мс | bybit 157 сд. p50=114.8 мс | okx 85 сд. p50=158.3 мс | binance_futures_book 4443 сд. p50=144.3 мс | binance_futures_depth 94 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 161 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 20 сд. p50=47.7 мс | bitstamp 5 сд. p50=60.3 мс
15:30:26 [pm] T-273.5s Up 0.38/0.39 Down 0.61/0.62 ptb=82852.4 | CLOB 12180 сообщ., задержка p50/p90=444.7/805.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791559826486 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=2.0/3.2 мс
15:30:28 [cex] Binance 75 сд. задержка p50/p90=144.2/151.6 мс | Coinbase 60 задержка p50=80.5 мс | смещение часов +19.5 мс | lag loop p99/max=2.3/2.6 мс
15:30:28 [cex] binance_futures 158 сд. p50=154.6 мс | bybit 132 сд. p50=114.8 мс | okx 27 сд. p50=158.1 мс | binance_futures_book 5330 сд. p50=145.1 мс | binance_futures_depth 93 сд. p50=154.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 212 сд. p50=111.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 31 сд. p50=46.8 мс | bitstamp 2 сд. p50=47.7 мс
15:30:36 [pm] T-263.5s Up 0.43/0.44 Down 0.56/0.57 ptb=82852.4 | CLOB 8845 сообщ., задержка p50/p90=47.2/278.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791559836488 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=1.7/1.9 мс
15:30:38 [cex] Binance 119 сд. задержка p50/p90=145.0/146.6 мс | Coinbase 46 задержка p50=81.1 мс | смещение часов +20.4 мс | lag loop p99/max=3.8/5.0 мс
15:30:38 [cex] binance_futures 214 сд. p50=150.8 мс | bybit 232 сд. p50=114.5 мс | okx 156 сд. p50=158.9 мс | binance_futures_book 6319 сд. p50=146.4 мс | binance_futures_depth 97 сд. p50=155.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 210 сд. p50=112.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 44 сд. p50=49.1 мс | bitstamp 7 сд. p50=51.7 мс
15:30:46 [pm] T-253.5s Up 0.65/0.66 Down 0.34/0.35 ptb=82852.4 | CLOB 10703 сообщ., задержка p50/p90=1230.4/1299.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791559846489 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=2.0/2.3 мс
15:30:48 [cex] Binance 126 сд. задержка p50/p90=144.5/145.7 мс | Coinbase 48 задержка p50=82.2 мс | смещение часов +20.4 мс | lag loop p99/max=3.4/6.1 мс
15:30:48 [cex] binance_futures 144 сд. p50=153.0 мс | bybit 165 сд. p50=115.0 мс | okx 120 сд. p50=158.2 мс | binance_futures_book 3240 сд. p50=145.9 мс | binance_futures_depth 94 сд. p50=155.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 196 сд. p50=112.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 32 сд. p50=57.0 мс | bitstamp 7 сд. p50=54.0 мс
```

Представлено версией кода: 7642f87; python 3.12.3
