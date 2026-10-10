# Состояние сервера записи

Время (UTC): 2026-10-10 13:20:17

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 5 hours, 56 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         692         973           2         448        1213
Swap:           2047          44        2003
```
- нагрузка CPU (1/5/15 мин): 0.21 / 0.22 / 0.23

## Данные
- файлов: 1284, всего 387 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 50 | 6 МБ | 1 |
| bn_book | 50 | 624 КБ | 50 |
| bnf_agg | 50 | 10 МБ | 1 |
| bnf_book | 50 | 254 МБ | 1 |
| bnf_depth5 | 50 | 20 МБ | 1 |
| bnf_liq | 44 | 30 КБ | 818 |
| bs_trade | 50 | 753 КБ | 12 |
| by_book1 | 50 | 20 МБ | 1 |
| by_liq | 43 | 29 КБ | 8884 |
| by_trade | 50 | 7 МБ | 1 |
| cb_ticker | 50 | 6 МБ | 1 |
| clock | 50 | 38 КБ | 3 |
| clock_pm | 50 | 38 КБ | 21 |
| events | 47 | 16 КБ | 206 |
| events_pm | 50 | 21 КБ | 88 |
| health_cex | 50 | 527 КБ | 7 |
| health_feeds | 50 | 2 МБ | 7 |
| health_pm | 50 | 541 КБ | 9 |
| kr_trade | 50 | 2 МБ | 1 |
| ok_trade | 50 | 9 МБ | 1 |
| pm_depth | 50 | 10 МБ | 1 |
| pm_rtt | 50 | 337 КБ | 1 |
| pm_top | 50 | 20 МБ | 1 |
| pm_trades | 50 | 14 МБ | 1 |
| rtds | 50 | 3 МБ | 1 |
| windows | 50 | 102 КБ | 133 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 46, всего 302
- Polymarket CLOB: TCP 6, TLS 39, всего 93
- Polymarket gamma: TCP 5, TLS 39, всего 51

## Последние строки журнала записи
```
13:19:29 [cex] binance_futures 90 сд. p50=155.5 мс | bybit 43 сд. p50=114.4 мс | okx 82 сд. p50=144.8 мс | binance_futures_book 2131 сд. p50=157.2 мс | binance_futures_depth 90 сд. p50=158.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 66 сд. p50=112.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 12 сд. p50=38.0 мс | bitstamp 1 сд. p50=47.6 мс
13:19:37 [pm] T- 22.4s Up 0.99/n/a Down n/a/0.01 ptb=82749.1 | CLOB 546 сообщ., задержка p50/p90=38.3/51.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791638377641 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=2.1/2.1 мс
13:19:39 [cex] Binance 19 сд. задержка p50/p90=144.9/145.3 мс | Coinbase 43 задержка p50=82.0 мс | смещение часов +20.5 мс | lag loop p99/max=2.3/3.3 мс
13:19:39 [cex] binance_futures 76 сд. p50=154.8 мс | bybit 13 сд. p50=114.1 мс | okx 9 сд. p50=144.0 мс | binance_futures_book 959 сд. p50=157.1 мс | binance_futures_depth 89 сд. p50=158.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 50 сд. p50=112.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 16 сд. p50=37.7 мс | bitstamp 1 сд. p50=47.4 мс
13:19:45 [pm] окно btc-updown-5m-1791638400 (2026-10-10 13:20:00 UTC): Bitcoin Up or Down - October 10, 9:20AM-9:25AM ET
13:19:47 [pm] T- 12.4s Up 0.99/n/a Down n/a/0.01 ptb=82749.1 | CLOB 630 сообщ., задержка p50/p90=38.3/42.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791638387642 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=2.3/27.5 мс
13:19:49 [cex] Binance 19 сд. задержка p50/p90=144.7/145.0 мс | Coinbase 24 задержка p50=83.1 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/2.2 мс
13:19:49 [cex] binance_futures 43 сд. p50=154.4 мс | bybit 16 сд. p50=114.5 мс | okx 16 сд. p50=144.0 мс | binance_futures_book 815 сд. p50=157.1 мс | binance_futures_depth 83 сд. p50=158.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 49 сд. p50=112.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=44.1 мс | bitstamp 1 сд. p50=48.1 мс
13:19:57 [pm] T-  2.4s Up 0.99/n/a Down n/a/0.01 ptb=82749.1 | CLOB 1279 сообщ., задержка p50/p90=40.1/44.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791638397643 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=2.0/2.0 мс
13:19:59 [cex] Binance 21 сд. задержка p50/p90=144.8/145.8 мс | Coinbase 40 задержка p50=81.3 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/2.3 мс
13:19:59 [cex] binance_futures 16 сд. p50=302.8 мс | bybit 1 сд. p50=113.9 мс | okx 13 сд. p50=143.8 мс | binance_futures_book 350 сд. p50=156.9 мс | binance_futures_depth 82 сд. p50=158.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 33 сд. p50=112.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=40.8 мс | bitstamp 4 сд. p50=46.6 мс
13:20:07 [pm] T-292.4s Up 0.60/0.61 Down 0.39/0.40 ptb=82770.3 | CLOB 2636 сообщ., задержка p50/p90=42.6/63.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791638407644 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=18.4/34.3 мс
13:20:09 [cex] Binance 12 сд. задержка p50/p90=144.7/144.9 мс | Coinbase 21 задержка p50=81.6 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/5.4 мс
13:20:09 [cex] binance_futures 20 сд. p50=302.8 мс | bybit 23 сд. p50=114.7 мс | okx 17 сд. p50=144.2 мс | binance_futures_book 453 сд. p50=157.0 мс | binance_futures_depth 80 сд. p50=158.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 59 сд. p50=112.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=40.7 мс | bitstamp 1 сд. p50=50.1 мс
13:20:17 [pm] T-282.4s Up 0.63/0.64 Down 0.36/0.37 ptb=82770.3 | CLOB 2668 сообщ., задержка p50/p90=41.1/51.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791638417646 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=2.2/2.2 мс
```

Представлено версией кода: 69087ca; python 3.12.3
