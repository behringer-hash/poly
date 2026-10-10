# Состояние сервера записи

Время (UTC): 2026-10-10 16:25:42

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 9 hours, 1 minute
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         696         935           2         482        1209
Swap:           2047          44        2003
```
- нагрузка CPU (1/5/15 мин): 0.33 / 0.21 / 0.17

## Данные
- файлов: 1362, всего 409 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 53 | 7 МБ | 1 |
| bn_book | 53 | 639 КБ | 70 |
| bnf_agg | 53 | 11 МБ | 1 |
| bnf_book | 53 | 268 МБ | 1 |
| bnf_depth5 | 53 | 21 МБ | 1 |
| bnf_liq | 47 | 31 КБ | 86 |
| bs_trade | 53 | 781 КБ | 5 |
| by_book1 | 53 | 22 МБ | 1 |
| by_liq | 46 | 30 КБ | 1419 |
| by_trade | 53 | 7 МБ | 11 |
| cb_ticker | 53 | 6 МБ | 1 |
| clock | 53 | 41 КБ | 3 |
| clock_pm | 53 | 41 КБ | 16 |
| events | 50 | 18 КБ | 816 |
| events_pm | 53 | 22 КБ | 38 |
| health_cex | 53 | 561 КБ | 1 |
| health_feeds | 53 | 2 МБ | 1 |
| health_pm | 53 | 576 КБ | 2 |
| kr_trade | 53 | 2 МБ | 5 |
| ok_trade | 53 | 10 МБ | 1 |
| pm_depth | 53 | 11 МБ | 2 |
| pm_rtt | 53 | 360 КБ | 4 |
| pm_top | 53 | 21 МБ | 2 |
| pm_trades | 53 | 15 МБ | 2 |
| rtds | 53 | 3 МБ | 2 |
| windows | 53 | 109 КБ | 98 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 35, всего 282
- Polymarket CLOB: TCP 6, TLS 42, всего 85
- Polymarket gamma: TCP 5, TLS 39, всего 56

## Последние строки журнала записи
```
16:24:59 [pm] T-  0.8s Up n/a/0.01 Down 0.99/n/a ptb=82987.0 | CLOB 1565 сообщ., задержка p50/p90=41.4/49.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791649499188 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.3 мс | lag loop p99/max=1.8/2.1 мс
16:25:00 [cex] Binance 31 сд. задержка p50/p90=143.3/144.2 мс | Coinbase 28 задержка p50=81.1 мс | смещение часов +19.1 мс | lag loop p99/max=2.2/2.2 мс
16:25:00 [cex] binance_futures 24 сд. p50=292.5 мс | bybit 18 сд. p50=113.0 мс | okx 22 сд. p50=157.6 мс | binance_futures_book 881 сд. p50=143.4 мс | binance_futures_depth 83 сд. p50=145.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 63 сд. p50=111.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=42.9 мс | bitstamp 1 сд. p50=44.5 мс
16:25:09 [pm] T-290.8s Up 0.44/0.45 Down 0.55/0.56 ptb=82954.0 | CLOB 4730 сообщ., задержка p50/p90=44.1/51.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791649509190 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.2 мс | lag loop p99/max=5.9/8.8 мс
16:25:10 [cex] Binance 32 сд. задержка p50/p90=143.3/144.2 мс | Coinbase 27 задержка p50=81.1 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.2 мс
16:25:10 [cex] binance_futures 18 сд. p50=293.0 мс | bybit 15 сд. p50=113.5 мс | okx 36 сд. p50=157.3 мс | binance_futures_book 1155 сд. p50=143.6 мс | binance_futures_depth 92 сд. p50=145.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 37 сд. p50=111.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 16 сд. p50=44.1 мс | bitstamp 0 сд. p50=n/a мс
16:25:19 [pm] T-280.8s Up 0.54/0.55 Down 0.45/0.46 ptb=82954.0 | CLOB 4594 сообщ., задержка p50/p90=44.5/53.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791649519191 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.3 мс | lag loop p99/max=1.9/2.0 мс
16:25:20 [cex] Binance 21 сд. задержка p50/p90=143.3/144.2 мс | Coinbase 24 задержка p50=81.3 мс | смещение часов +19.1 мс | lag loop p99/max=2.0/2.1 мс
16:25:20 [cex] binance_futures 22 сд. p50=292.6 мс | bybit 7 сд. p50=113.5 мс | okx 14 сд. p50=157.3 мс | binance_futures_book 583 сд. p50=143.6 мс | binance_futures_depth 88 сд. p50=145.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 49 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=39.9 мс | bitstamp 1 сд. p50=48.5 мс
16:25:29 [pm] T-270.8s Up 0.58/0.59 Down 0.41/0.42 ptb=82954.0 | CLOB 5889 сообщ., задержка p50/p90=46.1/67.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791649529193 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.6 мс | lag loop p99/max=1.3/1.4 мс
16:25:30 [cex] Binance 24 сд. задержка p50/p90=143.2/143.6 мс | Coinbase 43 задержка p50=81.4 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.2 мс
16:25:30 [cex] binance_futures 26 сд. p50=292.6 мс | bybit 36 сд. p50=113.4 мс | okx 23 сд. p50=157.7 мс | binance_futures_book 679 сд. p50=143.5 мс | binance_futures_depth 85 сд. p50=145.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 100 сд. p50=111.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=47.8 мс | bitstamp 1 сд. p50=44.8 мс
16:25:39 [pm] T-260.8s Up 0.60/0.61 Down 0.39/0.40 ptb=82954.0 | CLOB 4342 сообщ., задержка p50/p90=45.3/50.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791649539195 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.6 мс | lag loop p99/max=1.8/2.0 мс
16:25:40 [cex] Binance 22 сд. задержка p50/p90=143.9/144.4 мс | Coinbase 46 задержка p50=81.8 мс | смещение часов +19.9 мс | lag loop p99/max=2.1/2.1 мс
16:25:40 [cex] binance_futures 26 сд. p50=292.6 мс | bybit 1 сд. p50=113.1 мс | okx 20 сд. p50=157.9 мс | binance_futures_book 430 сд. p50=143.5 мс | binance_futures_depth 82 сд. p50=145.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 86 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=46.2 мс | bitstamp 4 сд. p50=51.6 мс
```

Представлено версией кода: 69087ca; python 3.12.3
