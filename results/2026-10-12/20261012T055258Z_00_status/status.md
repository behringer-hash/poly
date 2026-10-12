# Состояние сервера записи

Время (UTC): 2026-10-12 05:52:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 4 days, 22 hours, 29 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         698         807           1         608        1207
Swap:           2047          72        1975
```
- нагрузка CPU (1/5/15 мин): 0.10 / 0.29 / 0.33

## Данные
- файлов: 2306, всего 695 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 90 | 11 МБ | 2 |
| bn_book | 90 | 868 КБ | 16 |
| bnf_agg | 90 | 17 МБ | 2 |
| bnf_book | 90 | 466 МБ | 0 |
| bnf_depth5 | 90 | 35 МБ | 2 |
| bnf_liq | 77 | 44 КБ | 446 |
| bs_trade | 90 | 1 МБ | 10 |
| by_book1 | 90 | 34 МБ | 2 |
| by_liq | 73 | 40 КБ | 1264 |
| by_trade | 90 | 11 МБ | 2 |
| cb_ticker | 90 | 9 МБ | 2 |
| clock | 90 | 70 КБ | 6 |
| clock_pm | 90 | 70 КБ | 22 |
| events | 86 | 30 КБ | 527 |
| events_pm | 90 | 35 КБ | 44 |
| health_cex | 90 | 957 КБ | 10 |
| health_feeds | 90 | 3 МБ | 10 |
| health_pm | 90 | 984 КБ | 10 |
| kr_trade | 90 | 2 МБ | 2 |
| ok_trade | 90 | 15 МБ | 2 |
| pm_depth | 90 | 18 МБ | 1 |
| pm_rtt | 90 | 626 КБ | 3 |
| pm_top | 90 | 37 МБ | 1 |
| pm_trades | 90 | 25 МБ | 1 |
| rtds | 90 | 6 МБ | 1 |
| windows | 90 | 187 КБ | 204 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 53, всего 302
- Polymarket CLOB: TCP 6, TLS 53, всего 95
- Polymarket gamma: TCP 6, TLS 49, всего 61

## Последние строки журнала записи
```
05:52:18 [cex] Binance 60 сд. задержка p50/p90=144.5/148.8 мс | Coinbase 25 задержка p50=82.4 мс | смещение часов +20.0 мс | lag loop p99/max=2.1/6.6 мс
05:52:18 [cex] binance_futures 68 сд. p50=145.5 мс | bybit 83 сд. p50=114.4 мс | okx 51 сд. p50=155.6 мс | binance_futures_book 2293 сд. p50=144.8 мс | binance_futures_depth 96 сд. p50=156.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 91 сд. p50=111.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=43.2 мс | bitstamp 3 сд. p50=46.1 мс
05:52:18 [pm] T-161.5s Up 0.52/0.53 Down 0.47/0.48 ptb=83873.4 | CLOB 7845 сообщ., задержка p50/p90=41.0/42.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791784338498 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.7/7.7 мс
05:52:28 [cex] Binance 38 сд. задержка p50/p90=145.2/152.3 мс | Coinbase 36 задержка p50=81.9 мс | смещение часов +20.0 мс | lag loop p99/max=2.1/7.0 мс
05:52:28 [cex] binance_futures 57 сд. p50=151.1 мс | bybit 19 сд. p50=119.9 мс | okx 68 сд. p50=154.2 мс | binance_futures_book 1584 сд. p50=144.8 мс | binance_futures_depth 97 сд. p50=156.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 75 сд. p50=111.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 10 сд. p50=40.3 мс | bitstamp 4 сд. p50=47.3 мс
05:52:28 [pm] T-151.5s Up 0.64/0.65 Down 0.35/0.36 ptb=83873.4 | CLOB 7045 сообщ., задержка p50/p90=41.8/80.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791784348500 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.0/2.2 мс
05:52:38 [cex] Binance 64 сд. задержка p50/p90=144.6/145.4 мс | Coinbase 13 задержка p50=81.6 мс | смещение часов +20.0 мс | lag loop p99/max=2.2/3.1 мс
05:52:38 [cex] binance_futures 47 сд. p50=259.9 мс | bybit 59 сд. p50=114.0 мс | okx 51 сд. p50=153.9 мс | binance_futures_book 1433 сд. p50=144.7 мс | binance_futures_depth 93 сд. p50=156.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 116 сд. p50=111.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 14 сд. p50=43.0 мс | bitstamp 3 сд. p50=50.0 мс
05:52:38 [pm] T-141.5s Up 0.66/0.67 Down 0.33/0.34 ptb=83873.4 | CLOB 8269 сообщ., задержка p50/p90=37.8/54.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791784358501 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.8/2.7 мс
05:52:48 [cex] Binance 27 сд. задержка p50/p90=144.3/145.9 мс | Coinbase 25 задержка p50=81.7 мс | смещение часов +20.0 мс | lag loop p99/max=2.1/2.2 мс
05:52:48 [cex] binance_futures 43 сд. p50=145.6 мс | bybit 42 сд. p50=114.1 мс | okx 58 сд. p50=154.2 мс | binance_futures_book 5646 сд. p50=144.6 мс | binance_futures_depth 95 сд. p50=156.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 83 сд. p50=112.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=53.9 мс | bitstamp 3 сд. p50=50.6 мс
05:52:48 [pm] T-131.5s Up 0.57/0.58 Down 0.42/0.43 ptb=83873.4 | CLOB 9414 сообщ., задержка p50/p90=37.1/42.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791784368503 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=2.0/4.3 мс
05:52:58 [cex] Binance 73 сд. задержка p50/p90=147.0/148.5 мс | Coinbase 45 задержка p50=82.6 мс | смещение часов +22.0 мс | lag loop p99/max=2.9/15.4 мс
05:52:58 [cex] binance_futures 123 сд. p50=149.5 мс | bybit 112 сд. p50=116.0 мс | okx 194 сд. p50=156.4 мс | binance_futures_book 4386 сд. p50=147.2 мс | binance_futures_depth 96 сд. p50=157.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 109 сд. p50=113.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 19 сд. p50=57.5 мс | bitstamp 2 сд. p50=50.1 мс
05:52:58 [pm] T-121.5s Up 0.88/0.89 Down 0.11/0.12 ptb=83873.4 | CLOB 12251 сообщ., задержка p50/p90=44.6/134.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791784378504 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=3.5/4.0 мс
```

Представлено версией кода: 69087ca; python 3.12.3
