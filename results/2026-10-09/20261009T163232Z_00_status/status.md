# Состояние сервера записи

Время (UTC): 2026-10-09 16:32:32

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 9 hours, 8 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         661         742           2         696        1244
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.17 / 0.22 / 0.25

## Данные
- файлов: 749, всего 359 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 29 | 6 МБ | 1 |
| bn_book | 29 | 575 КБ | 1 |
| bnf_agg | 29 | 9 МБ | 1 |
| bnf_book | 29 | 255 МБ | 0 |
| bnf_depth5 | 29 | 15 МБ | 1 |
| bnf_liq | 29 | 26 КБ | 321 |
| bs_trade | 29 | 626 КБ | 1 |
| by_book1 | 29 | 18 МБ | 1 |
| by_liq | 27 | 26 КБ | 323 |
| by_trade | 29 | 7 МБ | 1 |
| cb_ticker | 29 | 5 МБ | 1 |
| clock | 29 | 22 КБ | 29 |
| clock_pm | 29 | 22 КБ | 39 |
| events | 26 | 9 КБ | 104 |
| events_pm | 29 | 14 КБ | 69 |
| health_cex | 29 | 315 КБ | 3 |
| health_feeds | 29 | 1 МБ | 3 |
| health_pm | 29 | 322 КБ | 5 |
| kr_trade | 29 | 1 МБ | 3 |
| ok_trade | 29 | 9 МБ | 1 |
| pm_depth | 29 | 7 МБ | 1 |
| pm_rtt | 29 | 206 КБ | 3 |
| pm_top | 29 | 14 МБ | 1 |
| pm_trades | 29 | 9 МБ | 1 |
| rtds | 29 | 2 МБ | 1 |
| windows | 29 | 60 КБ | 298 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 48, всего 298
- Polymarket CLOB: TCP 8, TLS 52, всего 96
- Polymarket gamma: TCP 5, TLS 45, всего 56

## Последние строки журнала записи
```
16:31:46 [pm] T-193.0s Up 0.76/0.77 Down 0.23/0.24 ptb=82664.9 | CLOB 9829 сообщ., задержка p50/p90=40.9/41.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791563506991 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.3/2.0 мс
16:31:49 [cex] Binance 91 сд. задержка p50/p90=144.9/151.8 мс | Coinbase 84 задержка p50=78.6 мс | смещение часов +20.1 мс | lag loop p99/max=4.9/5.4 мс
16:31:49 [cex] binance_futures 121 сд. p50=160.8 мс | bybit 88 сд. p50=114.6 мс | okx 98 сд. p50=157.7 мс | binance_futures_book 4354 сд. p50=148.3 мс | binance_futures_depth 97 сд. p50=157.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 225 сд. p50=112.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 18 сд. p50=41.9 мс | bitstamp 19 сд. p50=50.9 мс
16:31:56 [pm] T-183.0s Up 0.69/0.70 Down 0.30/0.31 ptb=82664.9 | CLOB 9166 сообщ., задержка p50/p90=40.0/41.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791563516994 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.3/2.3 мс
16:31:59 [cex] Binance 103 сд. задержка p50/p90=144.6/150.6 мс | Coinbase 70 задержка p50=79.0 мс | смещение часов +20.1 мс | lag loop p99/max=6.7/9.5 мс
16:31:59 [cex] binance_futures 96 сд. p50=172.8 мс | bybit 121 сд. p50=115.8 мс | okx 118 сд. p50=158.3 мс | binance_futures_book 3221 сд. p50=146.1 мс | binance_futures_depth 93 сд. p50=157.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 282 сд. p50=111.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 17 сд. p50=47.3 мс | bitstamp 22 сд. p50=59.2 мс
16:32:06 [pm] T-173.0s Up 0.67/0.68 Down 0.32/0.33 ptb=82664.9 | CLOB 8425 сообщ., задержка p50/p90=40.0/41.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791563526995 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.0 мс | lag loop p99/max=1.8/2.1 мс
16:32:09 [cex] Binance 30 сд. задержка p50/p90=144.0/145.7 мс | Coinbase 100 задержка p50=79.9 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.2 мс
16:32:09 [cex] binance_futures 55 сд. p50=271.4 мс | bybit 95 сд. p50=115.0 мс | okx 99 сд. p50=160.6 мс | binance_futures_book 1560 сд. p50=144.7 мс | binance_futures_depth 96 сд. p50=157.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 234 сд. p50=111.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 17 сд. p50=47.1 мс | bitstamp 15 сд. p50=51.1 мс
16:32:16 [pm] T-163.0s Up 0.68/0.69 Down 0.31/0.32 ptb=82664.9 | CLOB 8807 сообщ., задержка p50/p90=40.0/40.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791563536997 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.4/2.1 мс
16:32:19 [cex] Binance 42 сд. задержка p50/p90=143.5/144.5 мс | Coinbase 107 задержка p50=80.5 мс | смещение часов +19.5 мс | lag loop p99/max=2.0/2.1 мс
16:32:19 [cex] binance_futures 27 сд. p50=303.0 мс | bybit 19 сд. p50=113.0 мс | okx 17 сд. p50=156.4 мс | binance_futures_book 1636 сд. p50=144.1 мс | binance_futures_depth 95 сд. p50=157.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 190 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 11 сд. p50=46.7 мс | bitstamp 14 сд. p50=67.6 мс
16:32:26 [pm] T-153.0s Up 0.91/0.92 Down 0.08/0.09 ptb=82664.9 | CLOB 7944 сообщ., задержка p50/p90=40.1/42.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791563546998 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.9/2.0 мс
16:32:29 [cex] Binance 449 сд. задержка p50/p90=144.7/149.0 мс | Coinbase 90 задержка p50=80.8 мс | смещение часов +19.5 мс | lag loop p99/max=4.7/9.4 мс
16:32:29 [cex] binance_futures 764 сд. p50=171.7 мс | bybit 618 сд. p50=115.8 мс | okx 685 сд. p50=161.6 мс | binance_futures_book 12990 сд. p50=148.0 мс | binance_futures_depth 90 сд. p50=157.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 341 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 75 сд. p50=57.9 мс | bitstamp 41 сд. p50=54.4 мс
```

Представлено версией кода: 7642f87; python 3.12.3
