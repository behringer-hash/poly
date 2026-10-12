# Состояние сервера записи

Время (UTC): 2026-10-12 18:19:33

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 10 hours, 55 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         808         799           2         505        1097
Swap:           2047         105        1942
```
- нагрузка CPU (1/5/15 мин): 0.52 / 0.42 / 0.44

## Данные
- файлов: 2638, всего 710 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 103 | 11 МБ | 1 |
| bn_book | 103 | 991 КБ | 1 |
| bnf_agg | 103 | 17 МБ | 1 |
| bnf_book | 103 | 463 МБ | 1 |
| bnf_depth5 | 103 | 37 МБ | 1 |
| bnf_liq | 90 | 51 КБ | 171 |
| bs_trade | 103 | 1 МБ | 1 |
| by_book1 | 103 | 37 МБ | 1 |
| by_liq | 85 | 45 КБ | 2479 |
| by_trade | 103 | 11 МБ | 1 |
| cb_ticker | 103 | 10 МБ | 3 |
| clock | 103 | 79 КБ | 11 |
| clock_pm | 103 | 79 КБ | 31 |
| events | 95 | 33 КБ | 1439 |
| events_pm | 102 | 40 КБ | 2833 |
| health_cex | 103 | 1 МБ | 7 |
| health_feeds | 103 | 4 МБ | 7 |
| health_pm | 103 | 1 МБ | 7 |
| kr_trade | 103 | 3 МБ | 1 |
| ok_trade | 103 | 15 МБ | 1 |
| pm_depth | 103 | 20 МБ | 1 |
| pm_rtt | 103 | 689 КБ | 5 |
| pm_top | 103 | 40 МБ | 1 |
| pm_trades | 103 | 29 МБ | 1 |
| rtds | 103 | 7 МБ | 1 |
| windows | 103 | 211 КБ | 389 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 46, всего 297
- Polymarket CLOB: TCP 5, TLS 59, всего 103
- Polymarket gamma: TCP 5, TLS 46, всего 59

## Последние строки журнала записи
```
18:18:45 [pm] T- 74.7s Up 0.45/0.46 Down 0.54/0.55 ptb=82415.3 | CLOB 7707 сообщ., задержка p50/p90=549.3/764.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791829125305 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.7 мс | lag loop p99/max=2.0/3.8 мс
18:18:46 [cex] Binance 54 сд. задержка p50/p90=146.2/146.5 мс | Coinbase 36 задержка p50=85.4 мс | смещение часов +21.8 мс | lag loop p99/max=1.9/4.4 мс
18:18:46 [cex] binance_futures 114 сд. p50=147.2 мс | bybit 108 сд. p50=115.5 мс | okx 92 сд. p50=156.1 мс | binance_futures_book 6457 сд. p50=159.6 мс | binance_futures_depth 90 сд. p50=155.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 186 сд. p50=113.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 20 сд. p50=52.2 мс | bitstamp 0 сд. p50=n/a мс
18:18:55 [pm] T- 64.7s Up 0.41/0.42 Down 0.58/0.59 ptb=82415.3 | CLOB 10630 сообщ., задержка p50/p90=1340.9/1543.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791829135307 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.7 мс | lag loop p99/max=1.6/2.8 мс
18:18:56 [cex] Binance 15 сд. задержка p50/p90=145.9/146.9 мс | Coinbase 17 задержка p50=85.1 мс | смещение часов +21.8 мс | lag loop p99/max=2.5/2.7 мс
18:18:56 [cex] binance_futures 46 сд. p50=149.1 мс | bybit 12 сд. p50=114.2 мс | okx 28 сд. p50=155.7 мс | binance_futures_book 2173 сд. p50=159.5 мс | binance_futures_depth 88 сд. p50=155.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 120 сд. p50=113.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 10 сд. p50=49.2 мс | bitstamp 1 сд. p50=47.7 мс
18:19:05 [pm] T- 54.7s Up 0.19/0.20 Down 0.80/0.81 ptb=82415.3 | CLOB 9610 сообщ., задержка p50/p90=1498.2/1594.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791829145308 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.7 мс | lag loop p99/max=2.0/10.7 мс
18:19:06 [cex] Binance 17 сд. задержка p50/p90=145.9/146.1 мс | Coinbase 15 задержка p50=84.1 мс | смещение часов +21.8 мс | lag loop p99/max=2.9/3.3 мс
18:19:06 [cex] binance_futures 25 сд. p50=295.1 мс | bybit 3 сд. p50=115.2 мс | okx 35 сд. p50=155.5 мс | binance_futures_book 1958 сд. p50=159.3 мс | binance_futures_depth 83 сд. p50=155.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 121 сд. p50=115.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 19 сд. p50=48.2 мс | bitstamp 1 сд. p50=53.7 мс
18:19:15 [pm] T- 44.7s Up 0.43/0.44 Down 0.56/0.57 ptb=82415.3 | CLOB 8862 сообщ., задержка p50/p90=209.9/237.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791829155313 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.7 мс | lag loop p99/max=1.7/1.9 мс
18:19:16 [cex] Binance 38 сд. задержка p50/p90=146.3/146.9 мс | Coinbase 19 задержка p50=84.8 мс | смещение часов +21.8 мс | lag loop p99/max=2.4/9.3 мс
18:19:16 [cex] binance_futures 26 сд. p50=295.1 мс | bybit 48 сд. p50=115.1 мс | okx 12 сд. p50=155.7 мс | binance_futures_book 1651 сд. p50=159.3 мс | binance_futures_depth 90 сд. p50=155.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 161 сд. p50=115.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 15 сд. p50=43.3 мс | bitstamp 2 сд. p50=48.6 мс
18:19:25 [pm] T- 34.7s Up 0.82/0.83 Down 0.17/0.18 ptb=82415.3 | CLOB 11236 сообщ., задержка p50/p90=1741.6/1892.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791829165314 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.7 мс | lag loop p99/max=4.5/5.8 мс
18:19:26 [cex] Binance 77 сд. задержка p50/p90=146.4/153.5 мс | Coinbase 48 задержка p50=86.1 мс | смещение часов +24.5 мс | lag loop p99/max=5.0/5.4 мс
18:19:26 [cex] binance_futures 140 сд. p50=147.4 мс | bybit 233 сд. p50=116.4 мс | okx 156 сд. p50=156.9 мс | binance_futures_book 5642 сд. p50=160.0 мс | binance_futures_depth 88 сд. p50=156.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 229 сд. p50=116.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 20 сд. p50=55.3 мс | bitstamp 3 сд. p50=49.0 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
