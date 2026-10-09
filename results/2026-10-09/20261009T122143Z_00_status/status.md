# Состояние сервера записи

Время (UTC): 2026-10-09 12:21:43

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 4 hours, 57 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         661         825           2         613        1244
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.29 / 0.27 / 0.33

## Данные
- файлов: 644, всего 306 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 25 | 5 МБ | 1 |
| bn_book | 25 | 473 КБ | 1 |
| bnf_agg | 25 | 8 МБ | 1 |
| bnf_book | 25 | 219 МБ | 0 |
| bnf_depth5 | 25 | 12 МБ | 1 |
| bnf_liq | 25 | 22 КБ | 43 |
| bs_trade | 25 | 535 КБ | 3 |
| by_book1 | 25 | 15 МБ | 1 |
| by_liq | 23 | 24 КБ | 444 |
| by_trade | 25 | 6 МБ | 1 |
| cb_ticker | 25 | 4 МБ | 1 |
| clock | 25 | 19 КБ | 55 |
| clock_pm | 25 | 19 КБ | 0 |
| events | 21 | 8 КБ | 2421 |
| events_pm | 25 | 14 КБ | 59 |
| health_cex | 25 | 266 КБ | 5 |
| health_feeds | 25 | 1008 КБ | 5 |
| health_pm | 25 | 272 КБ | 8 |
| kr_trade | 25 | 1 МБ | 1 |
| ok_trade | 25 | 8 МБ | 1 |
| pm_depth | 25 | 6 МБ | 0 |
| pm_rtt | 25 | 172 КБ | 0 |
| pm_top | 25 | 11 МБ | 0 |
| pm_trades | 25 | 8 МБ | 0 |
| rtds | 25 | 2 МБ | 0 |
| windows | 25 | 51 КБ | 39 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 43, всего 293
- Polymarket CLOB: TCP 6, TLS 49, всего 97
- Polymarket gamma: TCP 7, TLS 48, всего 60

## Последние строки журнала записи
```
12:20:54 [pm] T-245.1s Up 0.13/0.14 Down 0.86/0.87 ptb=83168.8 | CLOB 7663 сообщ., задержка p50/p90=64.7/106.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791548454857 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=2.0/2.1 мс
12:20:56 [cex] Binance 161 сд. задержка p50/p90=155.0/155.9 мс | Coinbase 65 задержка p50=83.1 мс | смещение часов +20.3 мс | lag loop p99/max=3.1/4.6 мс
12:20:56 [cex] binance_futures 341 сд. p50=146.0 мс | bybit 331 сд. p50=114.5 мс | okx 410 сд. p50=145.5 мс | binance_futures_book 7698 сд. p50=159.2 мс | binance_futures_depth 97 сд. p50=158.1 мс | binance_liq 1 сд. p50=1149.4 мс | bybit_book 380 сд. p50=112.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 84 сд. p50=62.2 мс | bitstamp 8 сд. p50=58.1 мс
12:21:04 [pm] T-235.1s Up 0.11/0.12 Down 0.88/0.89 ptb=83168.8 | CLOB 8396 сообщ., задержка p50/p90=46.4/76.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791548464858 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.8/2.9 мс
12:21:06 [cex] Binance 72 сд. задержка p50/p90=162.0/163.6 мс | Coinbase 57 задержка p50=83.3 мс | смещение часов +20.3 мс | lag loop p99/max=8.1/9.1 мс
12:21:06 [cex] binance_futures 303 сд. p50=147.5 мс | bybit 431 сд. p50=115.1 мс | okx 199 сд. p50=144.9 мс | binance_futures_book 4895 сд. p50=160.4 мс | binance_futures_depth 97 сд. p50=158.4 мс | binance_liq 1 сд. p50=1159.7 мс | bybit_book 247 сд. p50=112.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 12 сд. p50=45.9 мс | bitstamp 17 сд. p50=56.2 мс
12:21:14 [pm] T-225.1s Up 0.11/0.12 Down 0.88/0.89 ptb=83168.8 | CLOB 5877 сообщ., задержка p50/p90=93.3/184.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791548474860 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=2.1/2.1 мс
12:21:16 [cex] Binance 150 сд. задержка p50/p90=155.4/161.2 мс | Coinbase 119 задержка p50=99.1 мс | смещение часов +20.3 мс | lag loop p99/max=2.4/8.0 мс
12:21:16 [cex] binance_futures 399 сд. p50=145.6 мс | bybit 487 сд. p50=114.9 мс | okx 359 сд. p50=145.2 мс | binance_futures_book 8257 сд. p50=159.9 мс | binance_futures_depth 97 сд. p50=158.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 350 сд. p50=112.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 22 сд. p50=47.2 мс | bitstamp 7 сд. p50=53.5 мс
12:21:24 [pm] T-215.1s Up 0.14/0.15 Down 0.85/0.86 ptb=83168.8 | CLOB 6701 сообщ., задержка p50/p90=47.5/73.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791548484861 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.1/2.1 мс
12:21:26 [cex] Binance 16 сд. задержка p50/p90=154.0/154.6 мс | Coinbase 264 задержка p50=112.0 мс | смещение часов +20.3 мс | lag loop p99/max=2.2/2.3 мс
12:21:26 [cex] binance_futures 63 сд. p50=267.2 мс | bybit 101 сд. p50=114.4 мс | okx 86 сд. p50=144.8 мс | binance_futures_book 2383 сд. p50=157.7 мс | binance_futures_depth 94 сд. p50=159.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 183 сд. p50=112.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 8 сд. p50=48.8 мс | bitstamp 30 сд. p50=61.4 мс
12:21:34 [pm] T-205.1s Up 0.10/0.11 Down 0.89/0.90 ptb=83168.8 | CLOB 6660 сообщ., задержка p50/p90=46.0/225.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791548494862 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=1.2/2.0 мс
12:21:36 [cex] Binance 154 сд. задержка p50/p90=155.3/164.3 мс | Coinbase 96 задержка p50=84.6 мс | смещение часов +20.3 мс | lag loop p99/max=6.5/7.5 мс
12:21:36 [cex] binance_futures 395 сд. p50=148.4 мс | bybit 270 сд. p50=114.7 мс | okx 237 сд. p50=145.4 мс | binance_futures_book 6608 сд. p50=162.2 мс | binance_futures_depth 98 сд. p50=158.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 253 сд. p50=112.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 20 сд. p50=47.1 мс | bitstamp 28 сд. p50=57.0 мс
```

Представлено версией кода: 7642f87; python 3.12.3
