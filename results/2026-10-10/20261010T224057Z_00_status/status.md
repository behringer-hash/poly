# Состояние сервера записи

Время (UTC): 2026-10-10 22:40:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 15 hours, 17 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         694         937           2         482        1211
Swap:           2047          51        1996
```
- нагрузка CPU (1/5/15 мин): 0.03 / 0.12 / 0.10

## Данные
- файлов: 1514, всего 436 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 59 | 7 МБ | 2 |
| bn_book | 59 | 652 КБ | 6 |
| bnf_agg | 59 | 11 МБ | 2 |
| bnf_book | 59 | 281 МБ | 0 |
| bnf_depth5 | 59 | 24 МБ | 2 |
| bnf_liq | 50 | 31 КБ | 4112 |
| bs_trade | 59 | 875 КБ | 2 |
| by_book1 | 59 | 23 МБ | 2 |
| by_liq | 51 | 31 КБ | 5014 |
| by_trade | 59 | 7 МБ | 4 |
| cb_ticker | 59 | 7 МБ | 2 |
| clock | 59 | 46 КБ | 18 |
| clock_pm | 59 | 46 КБ | 32 |
| events | 56 | 20 КБ | 444 |
| events_pm | 59 | 25 КБ | 1435 |
| health_cex | 59 | 629 КБ | 4 |
| health_feeds | 59 | 2 МБ | 4 |
| health_pm | 59 | 647 КБ | 4 |
| kr_trade | 59 | 2 МБ | 6 |
| ok_trade | 59 | 10 МБ | 2 |
| pm_depth | 59 | 12 МБ | 2 |
| pm_rtt | 59 | 411 КБ | 2 |
| pm_top | 59 | 25 МБ | 2 |
| pm_trades | 59 | 17 МБ | 2 |
| rtds | 59 | 4 МБ | 2 |
| windows | 59 | 122 КБ | 114 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 45, всего 294
- Polymarket CLOB: TCP 6, TLS 41, всего 84
- Polymarket gamma: TCP 8, TLS 58, всего 70

## Последние строки журнала записи
```
22:40:12 [pm] T-287.5s Up 0.42/0.43 Down 0.57/0.58 ptb=82988.1 | CLOB 3125 сообщ., задержка p50/p90=41.7/43.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791672012461 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.1/2.2 мс
22:40:13 [cex] Binance 7 сд. задержка p50/p90=143.8/144.8 мс | Coinbase 20 задержка p50=77.1 мс | смещение часов +19.7 мс | lag loop p99/max=2.0/2.1 мс
22:40:13 [cex] binance_futures 13 сд. p50=292.6 мс | bybit 4 сд. p50=114.1 мс | okx 8 сд. p50=153.2 мс | binance_futures_book 337 сд. p50=143.8 мс | binance_futures_depth 76 сд. p50=145.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 42 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=43.5 мс | bitstamp 3 сд. p50=52.5 мс
22:40:22 [pm] T-277.5s Up 0.42/0.43 Down 0.57/0.58 ptb=82988.1 | CLOB 2075 сообщ., задержка p50/p90=41.8/44.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791672022462 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.0/2.0 мс
22:40:23 [cex] Binance 14 сд. задержка p50/p90=143.8/144.7 мс | Coinbase 29 задержка p50=77.1 мс | смещение часов +19.7 мс | lag loop p99/max=1.8/2.1 мс
22:40:23 [cex] binance_futures 13 сд. p50=292.8 мс | bybit 3 сд. p50=114.1 мс | okx 6 сд. p50=153.8 мс | binance_futures_book 353 сд. p50=143.8 мс | binance_futures_depth 73 сд. p50=145.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 52 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=44.1 мс | bitstamp 0 сд. p50=n/a мс
22:40:32 [pm] T-267.5s Up 0.36/0.37 Down 0.63/0.64 ptb=82988.1 | CLOB 3460 сообщ., задержка p50/p90=43.0/50.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791672032463 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=1.9/2.1 мс
22:40:33 [cex] Binance 34 сд. задержка p50/p90=143.8/144.7 мс | Coinbase 37 задержка p50=77.0 мс | смещение часов +19.7 мс | lag loop p99/max=2.1/2.1 мс
22:40:33 [cex] binance_futures 6 сд. p50=293.7 мс | bybit 4 сд. p50=113.9 мс | okx 7 сд. p50=153.4 мс | binance_futures_book 279 сд. p50=143.8 мс | binance_futures_depth 74 сд. p50=145.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 65 сд. p50=111.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=44.5 мс | bitstamp 2 сд. p50=49.6 мс
22:40:42 [pm] T-257.5s Up 0.35/0.36 Down 0.64/0.65 ptb=82988.1 | CLOB 3770 сообщ., задержка p50/p90=42.1/44.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791672042465 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=1.8/2.0 мс
22:40:43 [cex] Binance 11 сд. задержка p50/p90=143.9/145.4 мс | Coinbase 35 задержка p50=78.2 мс | смещение часов +21.2 мс | lag loop p99/max=2.0/2.1 мс
22:40:43 [cex] binance_futures 7 сд. p50=293.2 мс | bybit 0 сд. p50=n/a мс | okx 8 сд. p50=153.4 мс | binance_futures_book 406 сд. p50=144.0 мс | binance_futures_depth 85 сд. p50=145.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 78 сд. p50=111.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 0 сд. p50=n/a мс | bitstamp 0 сд. p50=n/a мс
22:40:52 [pm] T-247.5s Up 0.73/0.74 Down 0.26/0.27 ptb=82988.1 | CLOB 4340 сообщ., задержка p50/p90=406.4/457.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791672052466 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.8 мс | lag loop p99/max=1.3/2.0 мс
22:40:53 [cex] Binance 98 сд. задержка p50/p90=146.1/148.8 мс | Coinbase 62 задержка p50=80.0 мс | смещение часов +21.2 мс | lag loop p99/max=2.1/2.1 мс
22:40:53 [cex] binance_futures 143 сд. p50=147.0 мс | bybit 155 сд. p50=116.8 мс | okx 115 сд. p50=156.7 мс | binance_futures_book 1861 сд. p50=145.6 мс | binance_futures_depth 84 сд. p50=146.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 159 сд. p50=113.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 22 сд. p50=47.6 мс | bitstamp 9 сд. p50=51.0 мс
```

Представлено версией кода: 69087ca; python 3.12.3
