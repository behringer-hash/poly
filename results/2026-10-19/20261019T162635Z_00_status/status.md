# Состояние сервера записи

Время (UTC): 2026-10-19 16:26:35

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 5 days, 9 hours, 2 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         781         332           1         973        1124
Swap:           2047         251        1796
```
- нагрузка CPU (1/5/15 мин): 0.23 / 0.28 / 0.29

## Данные
- файлов: 6623, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 269 | 35 МБ | 1 |
| bn_book | 269 | 3 МБ | 3 |
| bnf_agg | 269 | 54 МБ | 1 |
| bnf_book | 118 | 557 МБ | 542289 |
| bnf_depth5 | 118 | 41 МБ | 542365 |
| bnf_liq | 235 | 155 КБ | 357 |
| bs_trade | 118 | 1 МБ | 542285 |
| by_book1 | 269 | 112 МБ | 1 |
| by_liq | 242 | 124 КБ | 347 |
| by_trade | 269 | 36 МБ | 0 |
| bys_book1 | 153 | 52 МБ | 1 |
| bys_trade | 153 | 21 МБ | 0 |
| cb_ticker | 269 | 33 МБ | 1 |
| clock | 269 | 207 КБ | 55 |
| clock_pm | 269 | 208 КБ | 14 |
| events | 258 | 82 КБ | 1303 |
| events_pm | 269 | 97 КБ | 331 |
| health_cex | 269 | 3 МБ | 3 |
| health_feeds | 269 | 9 МБ | 3 |
| health_pm | 269 | 3 МБ | 8 |
| kr_trade | 118 | 3 МБ | 542285 |
| ok_trade | 268 | 47 МБ | 1 |
| pm_depth | 269 | 53 МБ | 0 |
| pm_rtt | 269 | 2 МБ | 2 |
| pm_top | 269 | 109 МБ | 0 |
| pm_trades | 269 | 78 МБ | 0 |
| rtds | 269 | 17 МБ | 0 |
| windows | 269 | 554 КБ | 180 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 51, всего 301
- Polymarket CLOB: TCP 5, TLS 57, всего 104
- Polymarket gamma: TCP 6, TLS 55, всего 68

## Последние строки журнала записи
```
16:25:51 [cex] Binance 111 сд. задержка p50/p90=148.9/149.7 мс | Coinbase 65 задержка p50=86.7 мс | смещение часов +24.1 мс | lag loop p99/max=2.0/2.1 мс
16:25:51 [cex] binance_futures 176 сд. p50=148.8 мс | bybit 273 сд. p50=116.9 мс | bybit_book 196 сд. p50=116.5 мс | bybit_spot 190 сд. p50=118.9 мс | bybit_spot_book 115 сд. p50=116.0 мс | okx 182 сд. p50=156.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:25:55 [pm] T-244.4s Up 0.38/0.39 Down 0.61/0.62 ptb=81888.1 | CLOB 9391 сообщ., задержка p50/p90=50.8/54.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792427155559 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=1.4/1.4 мс
16:26:01 [cex] Binance 46 сд. задержка p50/p90=148.8/149.4 мс | Coinbase 41 задержка p50=82.6 мс | смещение часов +24.1 мс | lag loop p99/max=2.2/2.2 мс
16:26:01 [cex] binance_futures 37 сд. p50=297.0 мс | bybit 58 сд. p50=117.1 мс | bybit_book 172 сд. p50=116.4 мс | bybit_spot 44 сд. p50=119.2 мс | bybit_spot_book 92 сд. p50=116.1 мс | okx 87 сд. p50=157.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:26:05 [pm] T-234.4s Up 0.44/0.45 Down 0.55/0.56 ptb=81888.1 | CLOB 11209 сообщ., задержка p50/p90=52.3/79.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792427165561 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=9.2/24.5 мс
16:26:11 [cex] Binance 180 сд. задержка p50/p90=149.2/150.7 мс | Coinbase 104 задержка p50=94.7 мс | смещение часов +24.1 мс | lag loop p99/max=2.1/2.2 мс
16:26:11 [cex] binance_futures 197 сд. p50=148.8 мс | bybit 380 сд. p50=117.6 мс | bybit_book 229 сд. p50=116.5 мс | bybit_spot 370 сд. p50=119.1 мс | bybit_spot_book 198 сд. p50=116.0 мс | okx 245 сд. p50=156.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:26:15 [pm] T-224.4s Up 0.50/0.51 Down 0.49/0.50 ptb=81888.1 | CLOB 10152 сообщ., задержка p50/p90=54.1/94.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792427175563 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.1/3.6 мс
16:26:21 [cex] Binance 142 сд. задержка p50/p90=148.9/150.8 мс | Coinbase 48 задержка p50=85.7 мс | смещение часов +24.1 мс | lag loop p99/max=2.1/2.3 мс
16:26:21 [cex] binance_futures 254 сд. p50=148.6 мс | bybit 244 сд. p50=117.2 мс | bybit_book 192 сд. p50=116.5 мс | bybit_spot 394 сд. p50=118.6 мс | bybit_spot_book 183 сд. p50=115.9 мс | okx 281 сд. p50=156.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:26:25 [pm] T-214.4s Up 0.64/0.69 Down 0.31/0.36 ptb=81888.1 | CLOB 8984 сообщ., задержка p50/p90=51.4/95.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792427185564 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.0 мс | lag loop p99/max=2.7/3.6 мс
16:26:31 [cex] Binance 101 сд. задержка p50/p90=149.4/150.2 мс | Coinbase 64 задержка p50=82.8 мс | смещение часов +24.1 мс | lag loop p99/max=2.1/3.8 мс
16:26:31 [cex] binance_futures 318 сд. p50=149.0 мс | bybit 284 сд. p50=117.0 мс | bybit_book 205 сд. p50=116.5 мс | bybit_spot 177 сд. p50=118.7 мс | bybit_spot_book 157 сд. p50=115.9 мс | okx 230 сд. p50=157.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:26:35 [pm] T-204.4s Up 0.58/0.59 Down 0.41/0.42 ptb=81888.1 | CLOB 13045 сообщ., задержка p50/p90=178.8/329.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792427195566 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.0/4.8 мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
