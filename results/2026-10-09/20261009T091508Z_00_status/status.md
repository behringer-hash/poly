# Состояние сервера записи

Время (UTC): 2026-10-09 09:15:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 1 hour, 51 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         672         904           2         521        1233
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.26 / 0.18 / 0.16

## Данные
- файлов: 566, всего 235 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 22 | 4 МБ | 2 |
| bn_book | 22 | 402 КБ | 36 |
| bnf_agg | 22 | 6 МБ | 2 |
| bnf_book | 22 | 163 МБ | 1 |
| bnf_depth5 | 22 | 10 МБ | 2 |
| bnf_liq | 22 | 21 КБ | 531 |
| bs_trade | 22 | 434 КБ | 2 |
| by_book1 | 22 | 12 МБ | 2 |
| by_liq | 19 | 23 КБ | 1137 |
| by_trade | 22 | 4 МБ | 2 |
| cb_ticker | 22 | 3 МБ | 2 |
| clock | 22 | 16 КБ | 56 |
| clock_pm | 22 | 16 КБ | 61 |
| events | 19 | 6 КБ | 579 |
| events_pm | 22 | 10 КБ | 87 |
| health_cex | 22 | 231 КБ | 2 |
| health_feeds | 22 | 869 КБ | 2 |
| health_pm | 22 | 236 КБ | 3 |
| kr_trade | 22 | 908 КБ | 4 |
| ok_trade | 22 | 6 МБ | 2 |
| pm_depth | 22 | 5 МБ | 1 |
| pm_rtt | 22 | 147 КБ | 5 |
| pm_top | 22 | 10 МБ | 1 |
| pm_trades | 22 | 7 МБ | 1 |
| rtds | 22 | 1 МБ | 1 |
| windows | 22 | 44 КБ | 34 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 43, всего 292
- Polymarket CLOB: TCP 5, TLS 45, всего 87
- Polymarket gamma: TCP 6, TLS 56, всего 68

## Последние строки журнала записи
```
09:14:25 [cex] Binance 14 сд. задержка p50/p90=142.7/143.6 мс | Coinbase 15 задержка p50=80.5 мс | смещение часов +18.8 мс | lag loop p99/max=2.2/2.2 мс
09:14:25 [cex] binance_futures 25 сд. p50=293.0 мс | bybit 28 сд. p50=112.2 мс | okx 32 сд. p50=151.5 мс | binance_futures_book 641 сд. p50=143.2 мс | binance_futures_depth 88 сд. p50=143.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 97 сд. p50=111.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=41.9 мс | bitstamp 6 сд. p50=51.8 мс
09:14:33 [pm] T- 26.7s Up 0.99/n/a Down n/a/0.01 ptb=82485.5 | CLOB 649 сообщ., задержка p50/p90=40.4/46.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791537273302 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.2 мс | lag loop p99/max=2.1/2.5 мс
09:14:35 [cex] Binance 47 сд. задержка p50/p90=143.7/145.5 мс | Coinbase 26 задержка p50=81.4 мс | смещение часов +18.8 мс | lag loop p99/max=2.0/2.0 мс
09:14:35 [cex] binance_futures 43 сд. p50=163.6 мс | bybit 57 сд. p50=114.6 мс | okx 41 сд. p50=151.4 мс | binance_futures_book 2006 сд. p50=143.5 мс | binance_futures_depth 90 сд. p50=143.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 85 сд. p50=111.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=46.9 мс | bitstamp 2 сд. p50=46.2 мс
09:14:43 [pm] T- 16.7s Up 0.99/n/a Down n/a/0.01 ptb=82485.5 | CLOB 727 сообщ., задержка p50/p90=40.2/42.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791537283303 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.2 мс | lag loop p99/max=2.1/2.1 мс
09:14:45 [cex] Binance 21 сд. задержка p50/p90=142.6/143.5 мс | Coinbase 33 задержка p50=80.9 мс | смещение часов +18.8 мс | lag loop p99/max=2.0/2.0 мс
09:14:45 [cex] binance_futures 21 сд. p50=292.9 мс | bybit 25 сд. p50=112.9 мс | okx 35 сд. p50=151.6 мс | binance_futures_book 293 сд. p50=143.2 мс | binance_futures_depth 84 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 60 сд. p50=111.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=40.8 мс | bitstamp 0 сд. p50=n/a мс
09:14:45 [pm] окно btc-updown-5m-1791537300 (2026-10-09 09:15:00 UTC): Bitcoin Up or Down - October 9, 5:15AM-5:20AM ET
09:14:53 [pm] T-  6.7s Up 0.99/n/a Down n/a/0.01 ptb=82485.5 | CLOB 766 сообщ., задержка p50/p90=40.0/41.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791537293304 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.2 мс | lag loop p99/max=4.0/27.3 мс
09:14:55 [cex] Binance 30 сд. задержка p50/p90=142.7/143.0 мс | Coinbase 15 задержка p50=80.6 мс | смещение часов +18.8 мс | lag loop p99/max=1.8/2.1 мс
09:14:55 [cex] binance_futures 19 сд. p50=292.9 мс | bybit 22 сд. p50=112.2 мс | okx 22 сд. p50=151.4 мс | binance_futures_book 331 сд. p50=143.2 мс | binance_futures_depth 89 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 59 сд. p50=111.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=43.7 мс | bitstamp 3 сд. p50=46.3 мс
09:15:03 [pm] T-296.7s Up 0.47/0.48 Down 0.52/0.53 ptb=82500.2 | CLOB 2105 сообщ., задержка p50/p90=40.1/105.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791537303306 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.1 мс | lag loop p99/max=5.4/7.5 мс
09:15:05 [cex] Binance 23 сд. задержка p50/p90=142.6/144.1 мс | Coinbase 21 задержка p50=81.2 мс | смещение часов +18.8 мс | lag loop p99/max=3.1/3.4 мс
09:15:05 [cex] binance_futures 27 сд. p50=292.9 мс | bybit 8 сд. p50=112.1 мс | okx 30 сд. p50=151.3 мс | binance_futures_book 745 сд. p50=143.2 мс | binance_futures_depth 88 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 55 сд. p50=111.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=71.0 мс | bitstamp 6 сд. p50=50.5 мс
```

Представлено версией кода: 3f62835; python 3.12.3
