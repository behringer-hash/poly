# Состояние сервера записи

Время (UTC): 2026-10-08 15:39:06

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 1 day, 8 hours, 15 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         606         511           2         982        1299
Swap:           2047           0        2047
```
- нагрузка CPU (1/5/15 мин): 0.34 / 0.48 / 0.45

## Данные
- файлов: 102, всего 316 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 4 | 6 МБ | 0 |
| bn_book | 4 | 329 КБ | 0 |
| bnf_agg | 4 | 13 МБ | 0 |
| bnf_book | 4 | 248 МБ | 0 |
| bnf_depth5 | 4 | 5 МБ | 0 |
| bnf_liq | 4 | 21 КБ | 6 |
| bs_trade | 4 | 320 КБ | 0 |
| by_book1 | 4 | 11 МБ | 0 |
| by_liq | 4 | 65 КБ | 40 |
| by_trade | 4 | 11 МБ | 0 |
| cb_ticker | 4 | 2 МБ | 0 |
| clock | 4 | 3 КБ | 32 |
| clock_pm | 4 | 3 КБ | 30 |
| events | 2 | 874 Б | 2708 |
| events_pm | 4 | 3 КБ | 140 |
| health_cex | 4 | 48 КБ | 0 |
| health_feeds | 4 | 223 КБ | 0 |
| health_pm | 4 | 47 КБ | 2 |
| kr_trade | 4 | 688 КБ | 0 |
| ok_trade | 4 | 11 МБ | 0 |
| pm_depth | 4 | 2 МБ | 2 |
| pm_rtt | 4 | 44 КБ | 4 |
| pm_top | 4 | 4 МБ | 2 |
| pm_trades | 4 | 2 МБ | 2 |
| rtds | 4 | 460 КБ | 2 |
| windows | 4 | 9 КБ | 272 |

Дни с данными: 2026-10-08

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 38, всего 301
- Polymarket CLOB: TCP 7, TLS 42, всего 97
- Polymarket gamma: TCP 5, TLS 51, всего 64

## Последние строки журнала записи
```
15:38:24 [pm] T- 95.7s Up n/a/0.01 Down 0.99/n/a ptb=81252.9 | CLOB 3818 сообщ., задержка p50/p90=47.4/71.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791473904265 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.1 мс | lag loop p99/max=1.9/2.8 мс
15:38:24 [cex] Binance 593 сд. задержка p50/p90=146.7/149.7 мс | Coinbase 257 задержка p50=104.5 мс | смещение часов +21.8 мс | lag loop p99/max=3.5/8.8 мс
15:38:24 [cex] binance_futures 1225 сд. p50=241.6 мс | bybit 1468 сд. p50=116.5 мс | okx 1289 сд. p50=154.4 мс | binance_futures_book 9635 сд. p50=149.1 мс | binance_futures_depth 29 сд. p50=147.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 608 сд. p50=113.6 мс | bybit_liq 1 сд. p50=254.0 мс | kraken 62 сд. p50=71.2 мс | bitstamp 43 сд. p50=59.1 мс
15:38:34 [pm] T- 85.7s Up 0.05/0.06 Down 0.94/0.95 ptb=81252.9 | CLOB 5374 сообщ., задержка p50/p90=112.0/174.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791473914266 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.1 мс | lag loop p99/max=2.0/2.0 мс
15:38:34 [cex] Binance 977 сд. задержка p50/p90=148.1/152.1 мс | Coinbase 252 задержка p50=93.5 мс | смещение часов +22.0 мс | lag loop p99/max=7.7/10.2 мс
15:38:34 [cex] binance_futures 2088 сд. p50=642.2 мс | bybit 1607 сд. p50=117.5 мс | okx 1659 сд. p50=156.0 мс | binance_futures_book 10605 сд. p50=149.9 мс | binance_futures_depth 42 сд. p50=148.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 565 сд. p50=113.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 46 сд. p50=57.9 мс | bitstamp 32 сд. p50=59.4 мс
15:38:44 [pm] T- 75.7s Up 0.08/0.09 Down 0.91/0.92 ptb=81252.9 | CLOB 8269 сообщ., задержка p50/p90=75.9/141.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791473924268 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=2.1/2.8 мс
15:38:44 [cex] Binance 520 сд. задержка p50/p90=148.4/154.4 мс | Coinbase 273 задержка p50=86.4 мс | смещение часов +22.0 мс | lag loop p99/max=7.0/7.3 мс
15:38:44 [cex] binance_futures 1841 сд. p50=155.0 мс | bybit 1345 сд. p50=117.2 мс | okx 1616 сд. p50=155.3 мс | binance_futures_book 13654 сд. p50=148.5 мс | binance_futures_depth 69 сд. p50=146.8 мс | binance_liq 1 сд. p50=1163.8 мс | bybit_book 641 сд. p50=113.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 92 сд. p50=75.2 мс | bitstamp 28 сд. p50=62.0 мс
15:38:54 [pm] T- 65.7s Up 0.07/0.08 Down 0.92/0.93 ptb=81252.9 | CLOB 11074 сообщ., задержка p50/p90=50.2/102.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791473934270 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.8 мс | lag loop p99/max=2.9/3.1 мс
15:38:54 [cex] Binance 474 сд. задержка p50/p90=147.8/153.7 мс | Coinbase 193 задержка p50=91.7 мс | смещение часов +22.0 мс | lag loop p99/max=5.9/9.4 мс
15:38:54 [cex] binance_futures 1475 сд. p50=150.1 мс | bybit 1010 сд. p50=116.3 мс | okx 1468 сд. p50=154.5 мс | binance_futures_book 16333 сд. p50=148.1 мс | binance_futures_depth 89 сд. p50=146.6 мс | binance_liq 1 сд. p50=1153.5 мс | bybit_book 661 сд. p50=113.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 86 сд. p50=57.8 мс | bitstamp 26 сд. p50=59.1 мс
15:39:04 [pm] T- 55.7s Up 0.08/0.09 Down 0.91/0.92 ptb=81252.9 | CLOB 11257 сообщ., задержка p50/p90=1135.8/1650.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791473944271 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=2.4/2.8 мс
15:39:04 [cex] Binance 378 сд. задержка p50/p90=147.3/151.5 мс | Coinbase 123 задержка p50=85.2 мс | смещение часов +22.0 мс | lag loop p99/max=9.0/10.4 мс
15:39:04 [cex] binance_futures 1066 сд. p50=149.2 мс | bybit 998 сд. p50=116.6 мс | okx 1219 сд. p50=154.7 мс | binance_futures_book 15290 сд. p50=147.9 мс | binance_futures_depth 86 сд. p50=146.6 мс | binance_liq 2 сд. p50=1153.7 мс | bybit_book 639 сд. p50=113.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 79 сд. p50=56.2 мс | bitstamp 40 сд. p50=62.1 мс
```

Представлено версией кода: 46d373e; python 3.12.3
