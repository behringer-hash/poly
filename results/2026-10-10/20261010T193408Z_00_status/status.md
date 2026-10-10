# Состояние сервера записи

Время (UTC): 2026-10-10 19:34:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 12 hours, 10 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         705         950           2         458        1200
Swap:           2047          51        1996
```
- нагрузка CPU (1/5/15 мин): 0.09 / 0.10 / 0.09

## Данные
- файлов: 1437, всего 416 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 56 | 7 МБ | 1 |
| bn_book | 56 | 644 КБ | 11 |
| bnf_agg | 56 | 11 МБ | 1 |
| bnf_book | 56 | 268 МБ | 1 |
| bnf_depth5 | 56 | 23 МБ | 1 |
| bnf_liq | 48 | 31 КБ | 2876 |
| bs_trade | 56 | 801 КБ | 9 |
| by_book1 | 56 | 23 МБ | 1 |
| by_liq | 48 | 31 КБ | 3020 |
| by_trade | 56 | 7 МБ | 3 |
| cb_ticker | 56 | 6 МБ | 1 |
| clock | 56 | 43 КБ | 55 |
| clock_pm | 56 | 43 КБ | 8 |
| events | 53 | 19 КБ | 431 |
| events_pm | 56 | 23 КБ | 1304 |
| health_cex | 56 | 596 КБ | 5 |
| health_feeds | 56 | 2 МБ | 5 |
| health_pm | 56 | 612 КБ | 6 |
| kr_trade | 56 | 2 МБ | 7 |
| ok_trade | 56 | 10 МБ | 1 |
| pm_depth | 56 | 12 МБ | 2 |
| pm_rtt | 56 | 386 КБ | 2 |
| pm_top | 56 | 23 МБ | 4 |
| pm_trades | 56 | 16 МБ | 8 |
| rtds | 56 | 4 МБ | 2 |
| windows | 56 | 116 КБ | 33 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 37, всего 286
- Polymarket CLOB: TCP 6, TLS 37, всего 85
- Polymarket gamma: TCP 7, TLS 42, всего 55

## Последние строки журнала записи
```
19:33:20 [pm] T- 99.2s Up 0.99/n/a Down n/a/0.01 ptb=82958.9 | CLOB 841 сообщ., задержка p50/p90=37.8/39.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791660800788 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.0 мс | lag loop p99/max=2.1/2.1 мс
19:33:21 [cex] Binance 18 сд. задержка p50/p90=143.4/144.3 мс | Coinbase 25 задержка p50=81.1 мс | смещение часов +19.2 мс | lag loop p99/max=2.0/2.0 мс
19:33:21 [cex] binance_futures 22 сд. p50=293.0 мс | bybit 8 сд. p50=112.9 мс | okx 7 сд. p50=152.9 мс | binance_futures_book 298 сд. p50=143.8 мс | binance_futures_depth 82 сд. p50=145.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 121 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=40.9 мс | bitstamp 0 сд. p50=n/a мс
19:33:30 [pm] T- 89.2s Up 0.99/n/a Down n/a/0.01 ptb=82958.9 | CLOB 579 сообщ., задержка p50/p90=37.6/38.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791660810788 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.0 мс | lag loop p99/max=1.8/2.0 мс
19:33:31 [cex] Binance 48 сд. задержка p50/p90=143.4/143.6 мс | Coinbase 26 задержка p50=81.4 мс | смещение часов +19.2 мс | lag loop p99/max=2.2/2.2 мс
19:33:31 [cex] binance_futures 71 сд. p50=144.9 мс | bybit 26 сд. p50=113.4 мс | okx 51 сд. p50=153.7 мс | binance_futures_book 1241 сд. p50=144.4 мс | binance_futures_depth 92 сд. p50=145.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 215 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=40.4 мс | bitstamp 2 сд. p50=47.9 мс
19:33:40 [pm] T- 79.2s Up 0.99/n/a Down n/a/0.01 ptb=82958.9 | CLOB 374 сообщ., задержка p50/p90=37.8/39.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791660820789 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.0 мс | lag loop p99/max=2.1/2.3 мс
19:33:41 [cex] Binance 15 сд. задержка p50/p90=143.3/143.4 мс | Coinbase 29 задержка p50=81.5 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.1 мс
19:33:41 [cex] binance_futures 16 сд. p50=292.7 мс | bybit 6 сд. p50=113.7 мс | okx 9 сд. p50=153.0 мс | binance_futures_book 266 сд. p50=143.8 мс | binance_futures_depth 81 сд. p50=145.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 125 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=41.7 мс | bitstamp 3 сд. p50=46.1 мс
19:33:50 [pm] T- 69.2s Up 1.00/n/a Down n/a/0.00 ptb=82958.9 | CLOB 684 сообщ., задержка p50/p90=37.6/38.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791660830790 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.0 мс | lag loop p99/max=2.1/2.2 мс
19:33:51 [cex] Binance 76 сд. задержка p50/p90=145.9/146.5 мс | Coinbase 38 задержка p50=81.4 мс | смещение часов +19.2 мс | lag loop p99/max=2.2/2.3 мс
19:33:51 [cex] binance_futures 111 сд. p50=146.5 мс | bybit 37 сд. p50=113.7 мс | okx 145 сд. p50=154.3 мс | binance_futures_book 1024 сд. p50=144.3 мс | binance_futures_depth 98 сд. p50=145.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 133 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=46.7 мс | bitstamp 1 сд. p50=45.1 мс
19:34:00 [pm] T- 59.2s Up 1.00/n/a Down n/a/0.00 ptb=82958.9 | CLOB 1912 сообщ., задержка p50/p90=37.8/39.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791660840791 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.0 мс | lag loop p99/max=2.1/4.0 мс
19:34:01 [cex] Binance 133 сд. задержка p50/p90=144.3/146.4 мс | Coinbase 49 задержка p50=81.8 мс | смещение часов +19.2 мс | lag loop p99/max=8.8/11.2 мс
19:34:01 [cex] binance_futures 163 сд. p50=147.2 мс | bybit 270 сд. p50=116.9 мс | okx 114 сд. p50=154.9 мс | binance_futures_book 4088 сд. p50=183.6 мс | binance_futures_depth 89 сд. p50=145.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 158 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=44.8 мс | bitstamp 6 сд. p50=88.7 мс
```

Представлено версией кода: 69087ca; python 3.12.3
