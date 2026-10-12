# Состояние сервера записи

Время (UTC): 2026-10-12 20:24:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 13 hours, 1 minute
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         783         893           2         426        1122
Swap:           2047         108        1939
```
- нагрузка CPU (1/5/15 мин): 0.13 / 0.36 / 0.37

## Данные
- файлов: 2692, всего 737 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 105 | 12 МБ | 1 |
| bn_book | 105 | 1010 КБ | 62 |
| bnf_agg | 105 | 18 МБ | 1 |
| bnf_book | 105 | 481 МБ | 1 |
| bnf_depth5 | 105 | 38 МБ | 1 |
| bnf_liq | 92 | 53 КБ | 357 |
| bs_trade | 105 | 1 МБ | 5 |
| by_book1 | 105 | 38 МБ | 1 |
| by_liq | 88 | 46 КБ | 357 |
| by_trade | 105 | 12 МБ | 1 |
| cb_ticker | 105 | 11 МБ | 3 |
| clock | 105 | 80 КБ | 26 |
| clock_pm | 105 | 80 КБ | 47 |
| events | 97 | 34 КБ | 1600 |
| events_pm | 105 | 40 КБ | 526 |
| health_cex | 105 | 1 МБ | 9 |
| health_feeds | 105 | 4 МБ | 9 |
| health_pm | 105 | 1 МБ | 1 |
| kr_trade | 105 | 3 МБ | 1 |
| ok_trade | 105 | 16 МБ | 1 |
| pm_depth | 105 | 21 МБ | 1 |
| pm_rtt | 105 | 706 КБ | 3 |
| pm_top | 105 | 41 МБ | 1 |
| pm_trades | 105 | 29 МБ | 1 |
| rtds | 105 | 7 МБ | 1 |
| windows | 105 | 215 КБ | 204 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 35, всего 286
- Polymarket CLOB: TCP 5, TLS 39, всего 86
- Polymarket gamma: TCP 5, TLS 39, всего 52

## Последние строки журнала записи
```
20:24:17 [cex] Binance 22 сд. задержка p50/p90=144.1/145.0 мс | Coinbase 29 задержка p50=82.4 мс | смещение часов +19.8 мс | lag loop p99/max=2.0/2.1 мс
20:24:17 [cex] binance_futures 24 сд. p50=294.1 мс | bybit 19 сд. p50=113.1 мс | okx 21 сд. p50=147.6 мс | binance_futures_book 1279 сд. p50=144.2 мс | binance_futures_depth 86 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 135 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=54.5 мс | bitstamp 3 сд. p50=45.1 мс
20:24:26 [pm] T- 33.6s Up 0.03/0.04 Down 0.96/0.97 ptb=82975.4 | CLOB 3748 сообщ., задержка p50/p90=40.9/57.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791836666447 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.9/2.1 мс
20:24:27 [cex] Binance 24 сд. задержка p50/p90=144.1/145.1 мс | Coinbase 24 задержка p50=82.3 мс | смещение часов +19.8 мс | lag loop p99/max=2.1/2.2 мс
20:24:27 [cex] binance_futures 31 сд. p50=294.1 мс | bybit 10 сд. p50=112.7 мс | okx 77 сд. p50=147.6 мс | binance_futures_book 923 сд. p50=144.1 мс | binance_futures_depth 89 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 124 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 9 сд. p50=41.9 мс | bitstamp 3 сд. p50=47.6 мс
20:24:36 [pm] T- 23.6s Up n/a/0.01 Down 0.99/n/a ptb=82975.4 | CLOB 2909 сообщ., задержка p50/p90=39.4/58.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791836676448 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.8/2.1 мс
20:24:37 [cex] Binance 16 сд. задержка p50/p90=144.7/146.7 мс | Coinbase 23 задержка p50=82.7 мс | смещение часов +20.5 мс | lag loop p99/max=2.2/2.2 мс
20:24:37 [cex] binance_futures 67 сд. p50=147.5 мс | bybit 43 сд. p50=113.6 мс | okx 60 сд. p50=148.2 мс | binance_futures_book 1294 сд. p50=144.8 мс | binance_futures_depth 91 сд. p50=145.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 143 сд. p50=111.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 0 сд. p50=n/a мс | bitstamp 3 сд. p50=47.0 мс
20:24:45 [pm] окно btc-updown-5m-1791836700 (2026-10-12 20:25:00 UTC): Bitcoin Up or Down - October 12, 4:25PM-4:30PM ET
20:24:46 [pm] T- 13.6s Up n/a/0.01 Down 0.99/n/a ptb=82975.4 | CLOB 1125 сообщ., задержка p50/p90=39.1/40.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791836686450 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=2.0/15.4 мс
20:24:47 [cex] Binance 17 сд. задержка p50/p90=144.7/145.2 мс | Coinbase 23 задержка p50=83.7 мс | смещение часов +20.5 мс | lag loop p99/max=2.2/2.3 мс
20:24:47 [cex] binance_futures 24 сд. p50=294.8 мс | bybit 13 сд. p50=113.7 мс | okx 19 сд. p50=148.3 мс | binance_futures_book 512 сд. p50=144.8 мс | binance_futures_depth 85 сд. p50=145.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 122 сд. p50=112.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 13 сд. p50=43.3 мс | bitstamp 4 сд. p50=48.8 мс
20:24:56 [pm] T-  3.5s Up n/a/0.01 Down 0.99/n/a ptb=82975.4 | CLOB 1841 сообщ., задержка p50/p90=39.5/42.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791836696451 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.6/1.7 мс
20:24:57 [cex] Binance 6 сд. задержка p50/p90=145.1/145.9 мс | Coinbase 20 задержка p50=83.0 мс | смещение часов +20.5 мс | lag loop p99/max=2.3/2.3 мс
20:24:57 [cex] binance_futures 27 сд. p50=294.8 мс | bybit 75 сд. p50=113.8 мс | okx 27 сд. p50=148.2 мс | binance_futures_book 659 сд. p50=144.8 мс | binance_futures_depth 91 сд. p50=145.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 142 сд. p50=112.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=38.8 мс | bitstamp 2 сд. p50=52.4 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
