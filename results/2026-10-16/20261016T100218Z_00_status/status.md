# Состояние сервера записи

Время (UTC): 2026-10-16 10:02:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 2 hours, 38 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         561        1296           2         267        1344
Swap:           2047         241        1806
```
- нагрузка CPU (1/5/15 мин): 0.14 / 0.15 / 0.18

## Данные
- файлов: 4769, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 191 | 25 МБ | 1 |
| bn_book | 191 | 2 МБ | 13 |
| bnf_agg | 191 | 39 МБ | 1 |
| bnf_book | 118 | 557 МБ | 260032 |
| bnf_depth5 | 118 | 41 МБ | 260108 |
| bnf_liq | 172 | 116 КБ | 33 |
| bs_trade | 118 | 1 МБ | 260028 |
| by_book1 | 191 | 81 МБ | 1 |
| by_liq | 170 | 96 КБ | 35 |
| by_trade | 191 | 26 МБ | 1 |
| bys_book1 | 75 | 28 МБ | 1 |
| bys_trade | 75 | 11 МБ | 1 |
| cb_ticker | 191 | 23 МБ | 1 |
| clock | 191 | 147 КБ | 23 |
| clock_pm | 191 | 147 КБ | 31 |
| events | 179 | 58 КБ | 1620 |
| events_pm | 190 | 71 КБ | 333 |
| health_cex | 191 | 2 МБ | 1 |
| health_feeds | 191 | 7 МБ | 1 |
| health_pm | 191 | 2 МБ | 5 |
| kr_trade | 118 | 3 МБ | 260028 |
| ok_trade | 190 | 35 МБ | 1 |
| pm_depth | 191 | 38 МБ | 1 |
| pm_rtt | 191 | 1 МБ | 1 |
| pm_top | 191 | 77 МБ | 1 |
| pm_trades | 191 | 56 МБ | 1 |
| rtds | 191 | 12 МБ | 1 |
| windows | 190 | 395 КБ | 224 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 41, всего 289
- Polymarket CLOB: TCP 6, TLS 40, всего 90
- Polymarket gamma: TCP 5, TLS 41, всего 58

## Последние строки журнала записи
```
10:01:32 [pm] T-207.4s Up 0.06/0.07 Down 0.93/0.94 ptb=81927.6 | CLOB 4556 сообщ., задержка p50/p90=40.6/42.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792144892581 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=1.9/2.1 мс
10:01:37 [cex] Binance 299 сд. задержка p50/p90=148.4/160.3 мс | Coinbase 59 задержка p50=94.5 мс | смещение часов +20.7 мс | lag loop p99/max=2.1/2.2 мс
10:01:37 [cex] binance_futures 435 сд. p50=154.9 мс | bybit 530 сд. p50=116.0 мс | bybit_book 332 сд. p50=112.9 мс | bybit_spot 294 сд. p50=116.8 мс | bybit_spot_book 183 сд. p50=112.4 мс | okx 354 сд. p50=145.8 мс | binance_liq 2 сд. p50=1146.8 мс | bybit_liq 6 сд. p50=257.9 мс
10:01:42 [pm] T-197.4s Up 0.03/0.04 Down 0.96/0.97 ptb=81927.6 | CLOB 4210 сообщ., задержка p50/p90=41.0/43.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792144902582 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=2.0/2.1 мс
10:01:47 [cex] Binance 140 сд. задержка p50/p90=146.6/148.0 мс | Coinbase 58 задержка p50=83.1 мс | смещение часов +20.7 мс | lag loop p99/max=2.2/2.3 мс
10:01:47 [cex] binance_futures 188 сд. p50=149.2 мс | bybit 813 сд. p50=116.8 мс | bybit_book 333 сд. p50=112.9 мс | bybit_spot 117 сд. p50=115.8 мс | bybit_spot_book 218 сд. p50=112.4 мс | okx 279 сд. p50=145.3 мс | binance_liq 3 сд. p50=1081.3 мс | bybit_liq 2 сд. p50=152.4 мс
10:01:52 [pm] T-187.4s Up 0.05/0.06 Down 0.94/0.95 ptb=81927.6 | CLOB 3934 сообщ., задержка p50/p90=38.5/41.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792144912584 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=2.2/2.2 мс
10:01:57 [cex] Binance 60 сд. задержка p50/p90=145.4/145.8 мс | Coinbase 73 задержка p50=85.2 мс | смещение часов +18.9 мс | lag loop p99/max=2.1/2.1 мс
10:01:57 [cex] binance_futures 111 сд. p50=172.2 мс | bybit 289 сд. p50=114.6 мс | bybit_book 275 сд. p50=112.6 мс | bybit_spot 126 сд. p50=113.3 мс | bybit_spot_book 169 сд. p50=112.1 мс | okx 106 сд. p50=143.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:02:02 [pm] T-177.4s Up 0.03/0.04 Down 0.96/0.97 ptb=81927.6 | CLOB 3205 сообщ., задержка p50/p90=38.8/46.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792144922585 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=2.7/2.8 мс
10:02:07 [cex] Binance 172 сд. задержка p50/p90=144.7/145.4 мс | Coinbase 35 задержка p50=80.2 мс | смещение часов +18.9 мс | lag loop p99/max=2.0/2.1 мс
10:02:07 [cex] binance_futures 196 сд. p50=145.8 мс | bybit 467 сд. p50=113.7 мс | bybit_book 309 сд. p50=111.0 мс | bybit_spot 155 сд. p50=113.3 мс | bybit_spot_book 154 сд. p50=110.5 мс | okx 183 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:02:12 [pm] T-167.4s Up 0.01/0.02 Down 0.98/0.99 ptb=81927.6 | CLOB 2501 сообщ., задержка p50/p90=38.7/40.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792144932586 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=1.9/1.9 мс
10:02:17 [cex] Binance 33 сд. задержка p50/p90=143.6/144.7 мс | Coinbase 41 задержка p50=80.3 мс | смещение часов +18.9 мс | lag loop p99/max=2.1/2.1 мс
10:02:17 [cex] binance_futures 88 сд. p50=221.1 мс | bybit 128 сд. p50=113.0 мс | bybit_book 214 сд. p50=111.0 мс | bybit_spot 102 сд. p50=114.0 мс | bybit_spot_book 136 сд. p50=110.6 мс | okx 52 сд. p50=143.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 0bed587; python 3.12.3
