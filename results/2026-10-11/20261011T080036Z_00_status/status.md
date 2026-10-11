# Состояние сервера записи

Время (UTC): 2026-10-11 08:00:36

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 4 days, 36 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         693         883           2         537        1212
Swap:           2047          61        1986
```
- нагрузка CPU (1/5/15 мин): 0.63 / 0.29 / 0.20

## Данные
- файлов: 1765, всего 438 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 69 | 7 МБ | 1 |
| bn_book | 69 | 672 КБ | 7 |
| bnf_agg | 69 | 11 МБ | 1 |
| bnf_book | 69 | 278 МБ | 0 |
| bnf_depth5 | 69 | 23 МБ | 1 |
| bnf_liq | 57 | 34 КБ | 1400 |
| bs_trade | 69 | 867 КБ | 7 |
| by_book1 | 69 | 24 МБ | 1 |
| by_liq | 58 | 32 КБ | 3385 |
| by_trade | 69 | 7 МБ | 3 |
| cb_ticker | 69 | 7 МБ | 3 |
| clock | 69 | 52 КБ | 16 |
| clock_pm | 68 | 53 КБ | 48 |
| events | 65 | 23 КБ | 173 |
| events_pm | 68 | 27 КБ | 1509 |
| health_cex | 69 | 712 КБ | 9 |
| health_feeds | 69 | 3 МБ | 9 |
| health_pm | 69 | 733 КБ | 8 |
| kr_trade | 69 | 2 МБ | 1 |
| ok_trade | 69 | 10 МБ | 1 |
| pm_depth | 69 | 13 МБ | 2 |
| pm_rtt | 69 | 449 КБ | 2 |
| pm_top | 69 | 26 МБ | 2 |
| pm_trades | 69 | 18 МБ | 2 |
| rtds | 69 | 4 МБ | 2 |
| windows | 69 | 140 КБ | 30 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 44, всего 293
- Polymarket CLOB: TCP 6, TLS 42, всего 88
- Polymarket gamma: TCP 5, TLS 41, всего 54

## Последние строки журнала записи
```
07:59:47 [pm] T- 12.8s Up 0.99/n/a Down n/a/0.01 ptb=82935.8 | CLOB 820 сообщ., задержка p50/p90=37.9/47.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791705587189 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/4.1 мс
07:59:47 [cex] Binance 15 сд. задержка p50/p90=143.7/144.8 мс | Coinbase 16 задержка p50=82.6 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.2 мс
07:59:47 [cex] binance_futures 14 сд. p50=292.4 мс | bybit 10 сд. p50=112.8 мс | okx 17 сд. p50=153.0 мс | binance_futures_book 283 сд. p50=143.9 мс | binance_futures_depth 80 сд. p50=145.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 120 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 0 сд. p50=n/a мс | bitstamp 1 сд. p50=51.1 мс
07:59:57 [pm] T-  2.8s Up 0.99/n/a Down n/a/0.01 ptb=82935.8 | CLOB 1472 сообщ., задержка p50/p90=45.0/46.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791705597190 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.2/2.2 мс
07:59:57 [cex] Binance 22 сд. задержка p50/p90=143.8/144.0 мс | Coinbase 20 задержка p50=84.0 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.2 мс
07:59:57 [cex] binance_futures 14 сд. p50=292.3 мс | bybit 9 сд. p50=112.6 мс | okx 20 сд. p50=152.8 мс | binance_futures_book 241 сд. p50=143.7 мс | binance_futures_depth 77 сд. p50=145.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 110 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=46.1 мс | bitstamp 1 сд. p50=45.1 мс
08:00:07 [pm] T-292.8s Up 0.69/0.70 Down 0.30/0.31 ptb=82941.3 | CLOB 5256 сообщ., задержка p50/p90=46.5/55.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791705607191 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=16.3/28.1 мс
08:00:07 [cex] Binance 31 сд. задержка p50/p90=143.7/175.5 мс | Coinbase 38 задержка p50=84.0 мс | смещение часов +18.8 мс | lag loop p99/max=2.9/7.4 мс
08:00:07 [cex] binance_futures 68 сд. p50=180.0 мс | bybit 42 сд. p50=117.4 мс | okx 99 сд. p50=153.0 мс | binance_futures_book 2181 сд. p50=144.4 мс | binance_futures_depth 82 сд. p50=145.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 103 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 29 сд. p50=45.3 мс | bitstamp 13 сд. p50=69.2 мс
08:00:17 [pm] T-282.8s Up 0.81/0.82 Down 0.18/0.19 ptb=82941.3 | CLOB 5817 сообщ., задержка p50/p90=47.4/196.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791705617192 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.8/9.0 мс
08:00:17 [cex] Binance 73 сд. задержка p50/p90=144.0/150.1 мс | Coinbase 30 задержка p50=83.5 мс | смещение часов +18.8 мс | lag loop p99/max=2.2/2.3 мс
08:00:17 [cex] binance_futures 97 сд. p50=146.2 мс | bybit 69 сд. p50=113.4 мс | okx 64 сд. p50=153.0 мс | binance_futures_book 1431 сд. p50=143.8 мс | binance_futures_depth 89 сд. p50=145.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 81 сд. p50=110.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 28 сд. p50=45.8 мс | bitstamp 1 сд. p50=50.0 мс
08:00:27 [pm] T-272.8s Up 0.89/0.90 Down 0.10/0.11 ptb=82941.3 | CLOB 4608 сообщ., задержка p50/p90=46.2/67.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791705627194 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.8/1.9 мс
08:00:27 [cex] Binance 77 сд. задержка p50/p90=144.4/145.3 мс | Coinbase 22 задержка p50=84.5 мс | смещение часов +18.8 мс | lag loop p99/max=2.2/2.3 мс
08:00:27 [cex] binance_futures 80 сд. p50=154.3 мс | bybit 335 сд. p50=114.8 мс | okx 130 сд. p50=153.0 мс | binance_futures_book 2915 сд. p50=144.0 мс | binance_futures_depth 88 сд. p50=145.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 290 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 32 сд. p50=44.0 мс | bitstamp 4 сд. p50=53.9 мс
```

Представлено версией кода: 69087ca; python 3.12.3
