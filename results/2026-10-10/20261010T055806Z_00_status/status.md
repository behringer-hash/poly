# Состояние сервера записи

Время (UTC): 2026-10-10 05:58:06

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 22 hours, 34 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         681         551           2         866        1224
Swap:           2047          21        2026
```
- нагрузка CPU (1/5/15 мин): 0.26 / 0.19 / 0.13

## Данные
- файлов: 1082, всего 389 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 42 | 6 МБ | 2 |
| bn_book | 42 | 612 КБ | 52 |
| bnf_agg | 42 | 10 МБ | 2 |
| bnf_book | 42 | 258 МБ | 2 |
| bnf_depth5 | 42 | 21 МБ | 2 |
| bnf_liq | 39 | 29 КБ | 265 |
| bs_trade | 42 | 731 КБ | 4 |
| by_book1 | 42 | 21 МБ | 2 |
| by_liq | 38 | 28 КБ | 50 |
| by_trade | 42 | 7 МБ | 2 |
| cb_ticker | 42 | 6 МБ | 4 |
| clock | 42 | 33 КБ | 42 |
| clock_pm | 42 | 33 КБ | 55 |
| events | 39 | 14 КБ | 1601 |
| events_pm | 42 | 19 КБ | 51 |
| health_cex | 42 | 463 КБ | 10 |
| health_feeds | 42 | 2 МБ | 10 |
| health_pm | 42 | 475 КБ | 1 |
| kr_trade | 42 | 1 МБ | 4 |
| ok_trade | 42 | 9 МБ | 2 |
| pm_depth | 42 | 10 МБ | 1 |
| pm_rtt | 42 | 310 КБ | 1 |
| pm_top | 42 | 19 МБ | 1 |
| pm_trades | 42 | 13 МБ | 1 |
| rtds | 42 | 3 МБ | 1 |
| windows | 42 | 89 КБ | 182 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 36, всего 284
- Polymarket CLOB: TCP 5, TLS 39, всего 84
- Polymarket gamma: TCP 5, TLS 38, всего 50

## Последние строки журнала записи
```
05:57:23 [pm] T-156.1s Up 0.95/0.96 Down 0.04/0.05 ptb=82707.9 | CLOB 2297 сообщ., задержка p50/p90=44.6/47.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791611843853 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.1 мс | lag loop p99/max=2.0/2.0 мс
05:57:25 [cex] Binance 17 сд. задержка p50/p90=144.2/146.8 мс | Coinbase 30 задержка p50=83.2 мс | смещение часов +22.4 мс | lag loop p99/max=2.2/2.2 мс
05:57:25 [cex] binance_futures 44 сд. p50=293.0 мс | bybit 51 сд. p50=116.4 мс | okx 41 сд. p50=152.3 мс | binance_futures_book 1047 сд. p50=157.0 мс | binance_futures_depth 90 сд. p50=145.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 70 сд. p50=112.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 19 сд. p50=42.7 мс | bitstamp 2 сд. p50=60.0 мс
05:57:33 [pm] T-146.1s Up 0.96/0.97 Down 0.03/0.04 ptb=82707.9 | CLOB 2526 сообщ., задержка p50/p90=44.5/46.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791611853855 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.1 мс | lag loop p99/max=1.8/1.8 мс
05:57:35 [cex] Binance 5 сд. задержка p50/p90=146.7/147.6 мс | Coinbase 34 задержка p50=85.5 мс | смещение часов +22.4 мс | lag loop p99/max=1.9/1.9 мс
05:57:35 [cex] binance_futures 25 сд. p50=296.2 мс | bybit 28 сд. p50=116.4 мс | okx 18 сд. p50=153.6 мс | binance_futures_book 314 сд. p50=159.0 мс | binance_futures_depth 87 сд. p50=146.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 163 сд. p50=114.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=39.9 мс | bitstamp 0 сд. p50=n/a мс
05:57:43 [pm] T-136.1s Up 0.97/0.98 Down 0.02/0.03 ptb=82707.9 | CLOB 1467 сообщ., задержка p50/p90=44.5/46.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791611863856 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.8/2.0 мс
05:57:45 [cex] Binance 11 сд. задержка p50/p90=146.9/147.7 мс | Coinbase 12 задержка p50=85.2 мс | смещение часов +22.4 мс | lag loop p99/max=2.1/2.2 мс
05:57:45 [cex] binance_futures 20 сд. p50=295.6 мс | bybit 33 сд. p50=117.2 мс | okx 17 сд. p50=153.7 мс | binance_futures_book 301 сд. p50=159.0 мс | binance_futures_depth 89 сд. p50=146.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 141 сд. p50=114.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=39.2 мс | bitstamp 1 сд. p50=49.5 мс
05:57:53 [pm] T-126.1s Up 0.97/0.98 Down 0.02/0.03 ptb=82707.9 | CLOB 1529 сообщ., задержка p50/p90=44.5/46.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791611873857 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/2.2 мс
05:57:55 [cex] Binance 24 сд. задержка p50/p90=146.7/147.6 мс | Coinbase 2 задержка p50=85.4 мс | смещение часов +22.4 мс | lag loop p99/max=2.1/2.1 мс
05:57:55 [cex] binance_futures 20 сд. p50=295.5 мс | bybit 28 сд. p50=116.5 мс | okx 70 сд. p50=155.1 мс | binance_futures_book 420 сд. p50=159.0 мс | binance_futures_depth 89 сд. p50=146.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 79 сд. p50=114.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 8 сд. p50=40.6 мс | bitstamp 1 сд. p50=49.4 мс
05:58:03 [pm] T-116.1s Up 0.97/0.98 Down 0.02/0.03 ptb=82707.9 | CLOB 1217 сообщ., задержка p50/p90=44.6/49.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791611883858 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.2/5.0 мс
05:58:05 [cex] Binance 22 сд. задержка p50/p90=146.9/147.6 мс | Coinbase 11 задержка p50=86.0 мс | смещение часов +22.4 мс | lag loop p99/max=2.1/2.2 мс
05:58:05 [cex] binance_futures 26 сд. p50=295.5 мс | bybit 11 сд. p50=116.2 мс | okx 23 сд. p50=153.7 мс | binance_futures_book 457 сд. p50=159.0 мс | binance_futures_depth 93 сд. p50=146.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 66 сд. p50=114.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=40.0 мс | bitstamp 2 сд. p50=50.9 мс
```

Представлено версией кода: 7642f87; python 3.12.3
