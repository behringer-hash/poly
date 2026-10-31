# Состояние сервера записи

Время (UTC): 2026-10-31 19:40:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 3 days, 12 hours, 16 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         619         866           1         607        1286
Swap:           2047         338        1709
```
- нагрузка CPU (1/5/15 мин): 0.02 / 0.08 / 0.08

## Данные
- файлов: 5860, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 36 МБ | 1 |
| bn_book | 242 | 3 МБ | 13 |
| bnf_agg | 242 | 50 МБ | 1 |
| bnf_book | 127 | 823 МБ | 1 |
| bnf_liq | 208 | 142 КБ | 5110 |
| by_book1 | 242 | 109 МБ | 1 |
| by_liq | 222 | 112 КБ | 3378 |
| by_trade | 242 | 33 МБ | 5 |
| bys_book1 | 242 | 79 МБ | 1 |
| bys_trade | 242 | 33 МБ | 1 |
| cb_ticker | 242 | 32 МБ | 1 |
| clock | 242 | 188 КБ | 7 |
| clock_pm | 242 | 188 КБ | 46 |
| events | 223 | 72 КБ | 222 |
| events_pm | 241 | 84 КБ | 424 |
| health_cex | 242 | 3 МБ | 1 |
| health_feeds | 242 | 8 МБ | 1 |
| health_pm | 242 | 3 МБ | 2 |
| ok_trade | 242 | 43 МБ | 1 |
| pm_depth | 242 | 50 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 2 |
| pm_top | 242 | 99 МБ | 2 |
| pm_trades | 241 | 70 МБ | 2 |
| rtds | 242 | 16 МБ | 2 |
| windows | 242 | 501 КБ | 94 |

Дни с данными: 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 35, всего 285
- Polymarket CLOB: TCP 6, TLS 42, всего 88
- Polymarket gamma: TCP 5, TLS 42, всего 50

## Последние строки журнала записи
```
19:39:56 [cex] Binance 19 сд. задержка p50/p90=142.5/142.7 мс | Coinbase 32 задержка p50=87.1 мс | смещение часов +18.3 мс | lag loop p99/max=2.2/2.2 мс
19:39:56 [cex] binance_futures 13 сд. p50=291.8 мс | bybit 3 сд. p50=111.4 мс | bybit_book 40 сд. p50=109.6 мс | bybit_spot 4 сд. p50=112.1 мс | bybit_spot_book 7 сд. p50=109.4 мс | okx 11 сд. p50=146.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 424 сд. p50=143.2 мс
19:39:56 [pm] T-  3.5s Up 0.99/n/a Down n/a/0.01 ptb=77471.1 | CLOB 1881 сообщ., задержка p50/p90=36.9/40.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793475596483 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=1.7/2.1 мс
19:40:06 [cex] Binance 26 сд. задержка p50/p90=142.6/143.6 мс | Coinbase 28 задержка p50=87.0 мс | смещение часов +18.3 мс | lag loop p99/max=2.3/3.3 мс
19:40:06 [cex] binance_futures 16 сд. p50=291.8 мс | bybit 1 сд. p50=111.1 мс | bybit_book 45 сд. p50=109.9 мс | bybit_spot 2 сд. p50=112.0 мс | bybit_spot_book 6 сд. p50=109.6 мс | okx 8 сд. p50=146.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 283 сд. p50=143.2 мс
19:40:06 [pm] T-293.5s Up 0.56/0.57 Down 0.43/0.44 ptb=77476.7 | CLOB 4203 сообщ., задержка p50/p90=37.8/40.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793475606484 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.2/2.3 мс
19:40:16 [cex] Binance 23 сд. задержка p50/p90=142.5/143.4 мс | Coinbase 35 задержка p50=87.2 мс | смещение часов +18.3 мс | lag loop p99/max=2.1/2.3 мс
19:40:16 [cex] binance_futures 11 сд. p50=291.7 мс | bybit 1 сд. p50=112.0 мс | bybit_book 44 сд. p50=109.7 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 8 сд. p50=109.9 мс | okx 4 сд. p50=146.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 305 сд. p50=143.2 мс
19:40:16 [pm] T-283.5s Up 0.56/0.57 Down 0.43/0.44 ptb=77476.7 | CLOB 4448 сообщ., задержка p50/p90=37.4/40.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793475616486 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=1.9/2.1 мс
19:40:26 [cex] Binance 31 сд. задержка p50/p90=142.5/142.8 мс | Coinbase 38 задержка p50=86.9 мс | смещение часов +18.3 мс | lag loop p99/max=1.9/2.3 мс
19:40:26 [cex] binance_futures 10 сд. p50=291.9 мс | bybit 16 сд. p50=111.7 мс | bybit_book 51 сд. p50=109.7 мс | bybit_spot 6 сд. p50=112.3 мс | bybit_spot_book 11 сд. p50=110.1 мс | okx 3 сд. p50=146.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 342 сд. p50=143.2 мс
19:40:26 [pm] T-273.5s Up 0.59/0.60 Down 0.40/0.41 ptb=77476.7 | CLOB 3687 сообщ., задержка p50/p90=40.6/56.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793475626487 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=1.8/2.0 мс
19:40:36 [cex] Binance 41 сд. задержка p50/p90=144.4/145.3 мс | Coinbase 28 задержка p50=88.5 мс | смещение часов +20.2 мс | lag loop p99/max=2.1/2.1 мс
19:40:36 [cex] binance_futures 9 сд. p50=293.9 мс | bybit 1 сд. p50=113.3 мс | bybit_book 58 сд. p50=111.4 мс | bybit_spot 2 сд. p50=113.5 мс | bybit_spot_book 11 сд. p50=111.4 мс | okx 8 сд. p50=148.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 407 сд. p50=144.7 мс
19:40:36 [pm] T-263.5s Up 0.62/0.63 Down 0.37/0.38 ptb=77476.7 | CLOB 4835 сообщ., задержка p50/p90=38.8/48.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793475636489 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=1.8/2.0 мс
```

Представлено версией кода: 8047248; python 3.12.3
