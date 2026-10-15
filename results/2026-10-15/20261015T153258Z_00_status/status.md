# Состояние сервера записи

Время (UTC): 2026-10-15 15:32:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 8 hours, 9 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         678         359           2        1116        1227
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.23 / 0.24 / 0.25

## Данные
- файлов: 4317, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 172 | 25 МБ | 1 |
| bn_book | 172 | 2 МБ | 3 |
| bnf_agg | 172 | 40 МБ | 1 |
| bnf_book | 118 | 557 МБ | 193472 |
| bnf_depth5 | 118 | 41 МБ | 193548 |
| bnf_liq | 154 | 110 КБ | 439 |
| bs_trade | 118 | 1 МБ | 193468 |
| by_book1 | 172 | 79 МБ | 1 |
| by_liq | 152 | 93 КБ | 894 |
| by_trade | 172 | 27 МБ | 1 |
| bys_book1 | 56 | 25 МБ | 1 |
| bys_trade | 56 | 11 МБ | 1 |
| cb_ticker | 172 | 22 МБ | 1 |
| clock | 172 | 133 КБ | 56 |
| clock_pm | 172 | 133 КБ | 56 |
| events | 160 | 51 КБ | 12764 |
| events_pm | 172 | 62 КБ | 252 |
| health_cex | 172 | 2 МБ | 7 |
| health_feeds | 172 | 6 МБ | 7 |
| health_pm | 172 | 2 МБ | 5 |
| kr_trade | 118 | 3 МБ | 193468 |
| ok_trade | 171 | 36 МБ | 1 |
| pm_depth | 172 | 35 МБ | 1 |
| pm_rtt | 172 | 1 МБ | 5 |
| pm_top | 172 | 71 МБ | 1 |
| pm_trades | 172 | 52 МБ | 1 |
| rtds | 172 | 11 МБ | 1 |
| windows | 172 | 355 КБ | 54 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 43, всего 291
- Polymarket CLOB: TCP 6, TLS 46, всего 89
- Polymarket gamma: TCP 5, TLS 44, всего 56

## Последние строки журнала записи
```
15:32:09 [cex] Binance 76 сд. задержка p50/p90=144.4/149.3 мс | Coinbase 52 задержка p50=86.4 мс | смещение часов +23.7 мс | lag loop p99/max=2.2/2.3 мс
15:32:09 [cex] binance_futures 317 сд. p50=148.6 мс | bybit 188 сд. p50=114.0 мс | bybit_book 328 сд. p50=114.0 мс | bybit_spot 120 сд. p50=116.8 мс | bybit_spot_book 201 сд. p50=113.7 мс | okx 198 сд. p50=161.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:32:12 [pm] T-167.3s Up 0.16/0.17 Down 0.83/0.84 ptb=82240.3 | CLOB 8716 сообщ., задержка p50/p90=44.7/49.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792078332719 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.9/2.2 мс
15:32:19 [cex] Binance 45 сд. задержка p50/p90=147.7/148.7 мс | Coinbase 41 задержка p50=87.5 мс | смещение часов +23.7 мс | lag loop p99/max=2.1/2.1 мс
15:32:19 [cex] binance_futures 259 сд. p50=148.0 мс | bybit 161 сд. p50=116.3 мс | bybit_book 329 сд. p50=114.1 мс | bybit_spot 102 сд. p50=116.1 мс | bybit_spot_book 169 сд. p50=113.9 мс | okx 139 сд. p50=162.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:32:22 [pm] T-157.3s Up 0.25/0.26 Down 0.74/0.75 ptb=82240.3 | CLOB 7642 сообщ., задержка p50/p90=44.7/49.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792078342720 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=2.0/2.2 мс
15:32:29 [cex] Binance 170 сд. задержка p50/p90=148.3/149.3 мс | Coinbase 78 задержка p50=87.6 мс | смещение часов +23.7 мс | lag loop p99/max=2.0/2.3 мс
15:32:29 [cex] binance_futures 237 сд. p50=149.1 мс | bybit 272 сд. p50=116.5 мс | bybit_book 305 сд. p50=114.1 мс | bybit_spot 140 сд. p50=116.2 мс | bybit_spot_book 163 сд. p50=113.9 мс | okx 360 сд. p50=162.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:32:32 [pm] T-147.3s Up 0.25/0.26 Down 0.74/0.75 ptb=82240.3 | CLOB 8420 сообщ., задержка p50/p90=44.7/50.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792078352722 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=1.4/2.0 мс
15:32:39 [cex] Binance 146 сд. задержка p50/p90=148.9/150.7 мс | Coinbase 71 задержка p50=87.4 мс | смещение часов +23.7 мс | lag loop p99/max=2.0/2.1 мс
15:32:39 [cex] binance_futures 313 сд. p50=148.9 мс | bybit 201 сд. p50=116.3 мс | bybit_book 377 сд. p50=114.1 мс | bybit_spot 147 сд. p50=117.1 мс | bybit_spot_book 190 сд. p50=113.9 мс | okx 362 сд. p50=162.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:32:42 [pm] T-137.3s Up 0.34/0.35 Down 0.65/0.66 ptb=82240.3 | CLOB 9361 сообщ., задержка p50/p90=44.6/50.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792078362723 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=1.7/1.7 мс
15:32:49 [cex] Binance 83 сд. задержка p50/p90=148.2/149.5 мс | Coinbase 59 задержка p50=87.5 мс | смещение часов +23.7 мс | lag loop p99/max=2.1/2.2 мс
15:32:49 [cex] binance_futures 156 сд. p50=149.5 мс | bybit 102 сд. p50=116.6 мс | bybit_book 248 сд. p50=114.1 мс | bybit_spot 105 сд. p50=116.5 мс | bybit_spot_book 146 сд. p50=113.9 мс | okx 106 сд. p50=162.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:32:52 [pm] T-127.3s Up 0.23/0.24 Down 0.76/0.77 ptb=82240.3 | CLOB 8917 сообщ., задержка p50/p90=44.3/45.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792078372725 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=1.2/1.3 мс
```

Представлено версией кода: ec1316a; python 3.12.3
