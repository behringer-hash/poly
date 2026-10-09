# Состояние сервера записи

Время (UTC): 2026-10-09 01:59:33

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 1 day, 18 hours, 35 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         652         839           2         606        1253
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.05 / 0.14 / 0.16

## Данные
- файлов: 359, всего 289 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 14 | 4 МБ | 1 |
| bn_book | 14 | 385 КБ | 7 |
| bnf_agg | 14 | 7 МБ | 1 |
| bnf_book | 14 | 216 МБ | 0 |
| bnf_depth5 | 14 | 12 МБ | 1 |
| bnf_liq | 14 | 18 КБ | 425 |
| bs_trade | 14 | 413 КБ | 7 |
| by_book1 | 14 | 14 МБ | 1 |
| by_liq | 12 | 20 КБ | 971 |
| by_trade | 14 | 5 МБ | 1 |
| cb_ticker | 14 | 3 МБ | 1 |
| clock | 14 | 12 КБ | 52 |
| clock_pm | 14 | 12 КБ | 55 |
| events | 11 | 4 КБ | 1146 |
| events_pm | 14 | 10 КБ | 73 |
| health_cex | 14 | 167 КБ | 1 |
| health_feeds | 14 | 685 КБ | 1 |
| health_pm | 14 | 169 КБ | 3 |
| kr_trade | 14 | 910 КБ | 3 |
| ok_trade | 14 | 6 МБ | 1 |
| pm_depth | 14 | 4 МБ | 1 |
| pm_rtt | 14 | 125 КБ | 5 |
| pm_top | 14 | 9 МБ | 1 |
| pm_trades | 14 | 5 МБ | 1 |
| rtds | 14 | 1 МБ | 1 |
| windows | 14 | 31 КБ | 270 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 54, всего 304
- Polymarket CLOB: TCP 5, TLS 41, всего 83
- Polymarket gamma: TCP 5, TLS 38, всего 49

## Последние строки журнала записи
```
01:58:49 [pm] T- 70.4s Up 0.94/0.95 Down 0.05/0.06 ptb=81879.7 | CLOB 3232 сообщ., задержка p50/p90=38.6/77.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791511129579 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.9/2.0 мс
01:58:51 [cex] Binance 12 сд. задержка p50/p90=143.5/144.5 мс | Coinbase 46 задержка p50=82.5 мс | смещение часов +19.3 мс | lag loop p99/max=2.1/2.3 мс
01:58:51 [cex] binance_futures 85 сд. p50=144.9 мс | bybit 91 сд. p50=113.1 мс | okx 52 сд. p50=144.7 мс | binance_futures_book 1015 сд. p50=144.0 мс | binance_futures_depth 89 сд. p50=144.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 148 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=41.6 мс | bitstamp 3 сд. p50=47.0 мс
01:58:59 [pm] T- 60.4s Up 0.82/0.83 Down 0.17/0.18 ptb=81879.7 | CLOB 7222 сообщ., задержка p50/p90=37.8/44.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791511139580 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.2/2.2 мс
01:59:01 [cex] Binance 90 сд. задержка p50/p90=145.0/154.1 мс | Coinbase 48 задержка p50=81.3 мс | смещение часов +19.3 мс | lag loop p99/max=6.4/10.7 мс
01:59:01 [cex] binance_futures 142 сд. p50=145.6 мс | bybit 196 сд. p50=116.8 мс | okx 117 сд. p50=147.5 мс | binance_futures_book 4377 сд. p50=146.0 мс | binance_futures_depth 85 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 169 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 30 сд. p50=60.5 мс | bitstamp 30 сд. p50=69.8 мс
01:59:09 [pm] T- 50.4s Up 0.94/0.95 Down 0.05/0.06 ptb=81879.7 | CLOB 5060 сообщ., задержка p50/p90=37.4/43.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791511149581 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.5/2.0 мс
01:59:11 [cex] Binance 5 сд. задержка p50/p90=143.4/144.5 мс | Coinbase 18 задержка p50=80.7 мс | смещение часов +19.3 мс | lag loop p99/max=2.2/2.3 мс
01:59:11 [cex] binance_futures 33 сд. p50=292.5 мс | bybit 46 сд. p50=112.6 мс | okx 24 сд. p50=143.8 мс | binance_futures_book 828 сд. p50=143.8 мс | binance_futures_depth 87 сд. p50=144.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 107 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=43.2 мс | bitstamp 2 сд. p50=46.5 мс
01:59:19 [pm] T- 40.4s Up 0.98/0.99 Down 0.01/0.02 ptb=81879.7 | CLOB 3448 сообщ., задержка p50/p90=37.4/43.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791511159583 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.9/2.1 мс
01:59:21 [cex] Binance 14 сд. задержка p50/p90=143.4/143.5 мс | Coinbase 38 задержка p50=99.7 мс | смещение часов +19.3 мс | lag loop p99/max=2.3/2.3 мс
01:59:21 [cex] binance_futures 23 сд. p50=292.5 мс | bybit 58 сд. p50=112.6 мс | okx 15 сд. p50=143.8 мс | binance_futures_book 1170 сд. p50=143.8 мс | binance_futures_depth 89 сд. p50=144.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 95 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=43.1 мс | bitstamp 22 сд. p50=81.1 мс
01:59:29 [pm] T- 30.4s Up 0.99/n/a Down n/a/0.01 ptb=81879.7 | CLOB 1192 сообщ., задержка p50/p90=37.0/40.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791511169584 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.0/2.0 мс
01:59:31 [cex] Binance 15 сд. задержка p50/p90=143.4/143.6 мс | Coinbase 26 задержка p50=79.4 мс | смещение часов +19.3 мс | lag loop p99/max=2.1/2.2 мс
01:59:31 [cex] binance_futures 27 сд. p50=292.4 мс | bybit 52 сд. p50=112.6 мс | okx 29 сд. p50=143.6 мс | binance_futures_book 1461 сд. p50=143.8 мс | binance_futures_depth 84 сд. p50=144.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 122 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=39.9 мс | bitstamp 4 сд. p50=63.5 мс
```

Представлено версией кода: 46d373e; python 3.12.3
