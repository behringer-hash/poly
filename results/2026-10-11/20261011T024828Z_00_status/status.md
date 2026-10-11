# Состояние сервера записи

Время (UTC): 2026-10-11 02:48:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 19 hours, 24 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         701         929           2         491        1204
Swap:           2047          56        1991
```
- нагрузка CPU (1/5/15 мин): 0.08 / 0.13 / 0.10

## Данные
- файлов: 1614, всего 446 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 63 | 8 МБ | 1 |
| bn_book | 63 | 663 КБ | 29 |
| bnf_agg | 63 | 11 МБ | 1 |
| bnf_book | 63 | 284 МБ | 1 |
| bnf_depth5 | 63 | 26 МБ | 1 |
| bnf_liq | 52 | 32 КБ | 17 |
| bs_trade | 63 | 857 КБ | 5 |
| by_book1 | 63 | 24 МБ | 1 |
| by_liq | 53 | 31 КБ | 33 |
| by_trade | 63 | 7 МБ | 1 |
| cb_ticker | 63 | 7 МБ | 1 |
| clock | 63 | 49 КБ | 56 |
| clock_pm | 63 | 49 КБ | 9 |
| events | 60 | 21 КБ | 513 |
| events_pm | 63 | 25 КБ | 146 |
| health_cex | 63 | 674 КБ | 3 |
| health_feeds | 63 | 2 МБ | 3 |
| health_pm | 63 | 693 КБ | 2 |
| kr_trade | 63 | 2 МБ | 1 |
| ok_trade | 63 | 10 МБ | 1 |
| pm_depth | 63 | 13 МБ | 0 |
| pm_rtt | 63 | 443 КБ | 2 |
| pm_top | 63 | 26 МБ | 0 |
| pm_trades | 63 | 18 МБ | 0 |
| rtds | 63 | 4 МБ | 0 |
| windows | 63 | 132 КБ | 53 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 7, TLS 39, всего 289
- Polymarket CLOB: TCP 6, TLS 36, всего 81
- Polymarket gamma: TCP 5, TLS 36, всего 47

## Последние строки журнала записи
```
02:47:44 [pm] T-135.4s Up 0.03/0.04 Down 0.96/0.97 ptb=83058.0 | CLOB 1101 сообщ., задержка p50/p90=41.0/43.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791686864556 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=2.0/2.0 мс
02:47:44 [cex] Binance 30 сд. задержка p50/p90=142.3/143.2 мс | Coinbase 16 задержка p50=79.7 мс | смещение часов +18.5 мс | lag loop p99/max=2.2/2.3 мс
02:47:44 [cex] binance_futures 13 сд. p50=291.9 мс | bybit 2 сд. p50=112.7 мс | okx 15 сд. p50=152.0 мс | binance_futures_book 442 сд. p50=143.1 мс | binance_futures_depth 81 сд. p50=144.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 49 сд. p50=110.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=44.9 мс | bitstamp 0 сд. p50=n/a мс
02:47:54 [pm] T-125.4s Up 0.01/0.02 Down 0.98/0.99 ptb=83058.0 | CLOB 1502 сообщ., задержка p50/p90=41.0/44.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791686874557 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=2.0/2.1 мс
02:47:54 [cex] Binance 32 сд. задержка p50/p90=142.3/143.3 мс | Coinbase 46 задержка p50=80.6 мс | смещение часов +18.5 мс | lag loop p99/max=2.0/2.1 мс
02:47:54 [cex] binance_futures 13 сд. p50=291.9 мс | bybit 11 сд. p50=112.5 мс | okx 20 сд. p50=152.2 мс | binance_futures_book 186 сд. p50=143.0 мс | binance_futures_depth 63 сд. p50=144.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 40 сд. p50=110.4 мс | bybit_liq 1 сд. p50=459.9 мс | kraken 1 сд. p50=39.8 мс | bitstamp 2 сд. p50=45.2 мс
02:48:04 [pm] T-115.4s Up 0.02/0.03 Down 0.97/0.98 ptb=83058.0 | CLOB 2035 сообщ., задержка p50/p90=41.7/67.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791686884558 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=2.2/3.4 мс
02:48:04 [cex] Binance 35 сд. задержка p50/p90=142.4/143.3 мс | Coinbase 41 задержка p50=80.2 мс | смещение часов +18.5 мс | lag loop p99/max=2.1/2.1 мс
02:48:04 [cex] binance_futures 79 сд. p50=144.6 мс | bybit 133 сд. p50=113.2 мс | okx 37 сд. p50=152.6 мс | binance_futures_book 1540 сд. p50=168.4 мс | binance_futures_depth 88 сд. p50=144.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 125 сд. p50=110.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=47.2 мс | bitstamp 5 сд. p50=54.2 мс
02:48:14 [pm] T-105.4s Up 0.02/0.03 Down 0.97/0.98 ptb=83058.0 | CLOB 1365 сообщ., задержка p50/p90=40.9/42.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791686894559 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=2.1/2.2 мс
02:48:14 [cex] Binance 29 сд. задержка p50/p90=142.4/143.3 мс | Coinbase 12 задержка p50=80.9 мс | смещение часов +18.5 мс | lag loop p99/max=1.9/2.0 мс
02:48:14 [cex] binance_futures 17 сд. p50=292.5 мс | bybit 26 сд. p50=112.5 мс | okx 7 сд. p50=152.2 мс | binance_futures_book 245 сд. p50=143.0 мс | binance_futures_depth 74 сд. p50=144.7 мс | binance_liq 1 сд. p50=1152.4 мс | bybit_book 91 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=44.2 мс | bitstamp 0 сд. p50=n/a мс
02:48:24 [pm] T- 95.4s Up 0.01/0.02 Down 0.98/0.99 ptb=83058.0 | CLOB 1238 сообщ., задержка p50/p90=40.5/44.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791686904561 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=2.1/2.1 мс
02:48:24 [cex] Binance 30 сд. задержка p50/p90=142.3/142.7 мс | Coinbase 9 задержка p50=80.6 мс | смещение часов +18.5 мс | lag loop p99/max=2.1/2.2 мс
02:48:24 [cex] binance_futures 16 сд. p50=291.9 мс | bybit 29 сд. p50=112.6 мс | okx 8 сд. p50=152.1 мс | binance_futures_book 208 сд. p50=143.1 мс | binance_futures_depth 76 сд. p50=144.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 122 сд. p50=110.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=38.7 мс | bitstamp 2 сд. p50=51.2 мс
```

Представлено версией кода: 69087ca; python 3.12.3
