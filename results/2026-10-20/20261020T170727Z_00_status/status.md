# Состояние сервера записи

Время (UTC): 2026-10-20 17:07:27

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 9 hours, 43 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         745         666           1         685        1160
Swap:           2047         479        1568
```
- нагрузка CPU (1/5/15 мин): 0.24 / 0.27 / 0.29

## Данные
- файлов: 7217, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 294 | 38 МБ | 1 |
| bn_book | 294 | 4 МБ | 7 |
| bnf_agg | 294 | 58 МБ | 1 |
| bnf_book | 118 | 557 МБ | 631142 |
| bnf_depth5 | 118 | 41 МБ | 631218 |
| bnf_liq | 257 | 167 КБ | 106 |
| bs_trade | 118 | 1 МБ | 631138 |
| by_book1 | 294 | 122 МБ | 1 |
| by_liq | 265 | 133 КБ | 866 |
| by_trade | 294 | 38 МБ | 1 |
| bys_book1 | 178 | 60 МБ | 1 |
| bys_trade | 178 | 24 МБ | 1 |
| cb_ticker | 294 | 36 МБ | 1 |
| clock | 294 | 226 КБ | 21 |
| clock_pm | 294 | 227 КБ | 55 |
| events | 282 | 89 КБ | 868 |
| events_pm | 294 | 105 КБ | 400 |
| health_cex | 294 | 3 МБ | 3 |
| health_feeds | 294 | 10 МБ | 3 |
| health_pm | 294 | 3 МБ | 7 |
| kr_trade | 118 | 3 МБ | 631138 |
| ok_trade | 293 | 51 МБ | 1 |
| pm_depth | 294 | 58 МБ | 1 |
| pm_rtt | 294 | 2 МБ | 3 |
| pm_top | 294 | 119 МБ | 1 |
| pm_trades | 294 | 84 МБ | 1 |
| rtds | 294 | 19 МБ | 1 |
| windows | 294 | 605 КБ | 114 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 61, всего 311
- Polymarket CLOB: TCP 4, TLS 40, всего 90
- Polymarket gamma: TCP 4, TLS 47, всего 58

## Последние строки журнала записи
```
17:06:39 [pm] T-200.7s Up 0.66/0.67 Down 0.33/0.34 ptb=82656.6 | CLOB 7925 сообщ., задержка p50/p90=39.2/51.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792515999298 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.6/1.7 мс
17:06:43 [cex] Binance 93 сд. задержка p50/p90=146.4/147.4 мс | Coinbase 48 задержка p50=77.5 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.1 мс
17:06:43 [cex] binance_futures 86 сд. p50=151.7 мс | bybit 130 сд. p50=117.4 мс | bybit_book 355 сд. p50=113.5 мс | bybit_spot 123 сд. p50=115.3 мс | bybit_spot_book 111 сд. p50=113.1 мс | okx 125 сд. p50=156.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:06:49 [pm] T-190.7s Up 0.78/0.79 Down 0.21/0.22 ptb=82656.6 | CLOB 8132 сообщ., задержка p50/p90=39.7/45.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792516009300 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.6/2.1 мс
17:06:53 [cex] Binance 69 сд. задержка p50/p90=146.2/147.3 мс | Coinbase 43 задержка p50=77.5 мс | смещение часов +21.6 мс | lag loop p99/max=2.2/2.2 мс
17:06:53 [cex] binance_futures 73 сд. p50=147.6 мс | bybit 147 сд. p50=115.6 мс | bybit_book 389 сд. p50=113.5 мс | bybit_spot 60 сд. p50=114.7 мс | bybit_spot_book 147 сд. p50=113.1 мс | okx 98 сд. p50=156.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:06:59 [pm] T-180.7s Up 0.87/0.88 Down 0.12/0.13 ptb=82656.6 | CLOB 8896 сообщ., задержка p50/p90=40.9/104.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792516019301 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.4/1.6 мс
17:07:03 [cex] Binance 94 сд. задержка p50/p90=146.9/148.8 мс | Coinbase 39 задержка p50=77.7 мс | смещение часов +21.6 мс | lag loop p99/max=2.4/3.3 мс
17:07:03 [cex] binance_futures 195 сд. p50=149.5 мс | bybit 417 сд. p50=119.0 мс | bybit_book 341 сд. p50=113.5 мс | bybit_spot 132 сд. p50=115.7 мс | bybit_spot_book 142 сд. p50=113.1 мс | okx 168 сд. p50=156.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:07:09 [pm] T-170.7s Up 0.91/0.92 Down 0.08/0.09 ptb=82656.6 | CLOB 6367 сообщ., задержка p50/p90=38.9/42.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792516029302 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.4/5.5 мс
17:07:13 [cex] Binance 41 сд. задержка p50/p90=149.1/151.0 мс | Coinbase 42 задержка p50=81.0 мс | смещение часов +24.7 мс | lag loop p99/max=2.2/2.7 мс
17:07:13 [cex] binance_futures 130 сд. p50=152.4 мс | bybit 348 сд. p50=117.9 мс | bybit_book 373 сд. p50=116.4 мс | bybit_spot 309 сд. p50=118.3 мс | bybit_spot_book 212 сд. p50=116.1 мс | okx 179 сд. p50=158.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:07:19 [pm] T-160.7s Up 0.92/0.93 Down 0.07/0.08 ptb=82656.6 | CLOB 9604 сообщ., задержка p50/p90=39.1/41.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792516039304 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=3.2/4.1 мс
17:07:23 [cex] Binance 40 сд. задержка p50/p90=149.1/150.3 мс | Coinbase 39 задержка p50=80.6 мс | смещение часов +24.7 мс | lag loop p99/max=2.0/2.1 мс
17:07:23 [cex] binance_futures 106 сд. p50=150.4 мс | bybit 145 сд. p50=118.2 мс | bybit_book 319 сд. p50=116.6 мс | bybit_spot 117 сд. p50=118.0 мс | bybit_spot_book 147 сд. p50=116.2 мс | okx 305 сд. p50=158.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 96010db; python 3.12.3
