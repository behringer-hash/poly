# Состояние сервера записи

Время (UTC): 2026-10-29 23:14:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 15 hours, 50 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         637         969           1         479        1268
Swap:           2047         319        1728
```
- нагрузка CPU (1/5/15 мин): 0.26 / 0.32 / 0.38

## Данные
- файлов: 5826, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 36 МБ | 0 |
| bn_book | 242 | 3 МБ | 4 |
| bnf_agg | 242 | 52 МБ | 0 |
| bnf_book | 83 | 556 МБ | 0 |
| bnf_liq | 211 | 139 КБ | 336 |
| by_book1 | 242 | 112 МБ | 0 |
| by_liq | 225 | 110 КБ | 340 |
| by_trade | 242 | 35 МБ | 0 |
| bys_book1 | 242 | 84 МБ | 0 |
| bys_trade | 242 | 34 МБ | 0 |
| cb_ticker | 242 | 32 МБ | 0 |
| clock | 242 | 187 КБ | 8 |
| clock_pm | 242 | 187 КБ | 41 |
| events | 228 | 73 КБ | 8058 |
| events_pm | 240 | 87 КБ | 1391 |
| health_cex | 242 | 3 МБ | 8 |
| health_feeds | 242 | 8 МБ | 8 |
| health_pm | 242 | 3 МБ | 3 |
| ok_trade | 242 | 45 МБ | 0 |
| pm_depth | 242 | 49 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 1 |
| pm_top | 242 | 100 МБ | 1 |
| pm_trades | 241 | 71 МБ | 5 |
| rtds | 242 | 15 МБ | 1 |
| windows | 242 | 498 КБ | 182 |

Дни с данными: 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 35, всего 283
- Polymarket CLOB: TCP 6, TLS 40, всего 83
- Polymarket gamma: TCP 4, TLS 38, всего 45

## Последние строки журнала записи
```
23:13:19 [cex] Binance 203 сд. задержка p50/p90=148.4/157.8 мс | Coinbase 73 задержка p50=79.2 мс | смещение часов +19.4 мс | lag loop p99/max=4.7/5.8 мс
23:13:19 [cex] binance_futures 216 сд. p50=151.4 мс | bybit 228 сд. p50=115.6 мс | bybit_book 381 сд. p50=110.7 мс | bybit_spot 492 сд. p50=114.2 мс | bybit_spot_book 161 сд. p50=111.7 мс | okx 235 сд. p50=157.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5784 сд. p50=145.7 мс
23:13:23 [pm] T- 96.9s Up 0.95/0.96 Down 0.04/0.05 ptb=78618.8 | CLOB 9180 сообщ., задержка p50/p90=44.4/49.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793315603105 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.4/1.4 мс
23:13:29 [cex] Binance 205 сд. задержка p50/p90=144.6/148.4 мс | Coinbase 84 задержка p50=79.7 мс | смещение часов +19.4 мс | lag loop p99/max=9.3/9.5 мс
23:13:29 [cex] binance_futures 287 сд. p50=150.8 мс | bybit 207 сд. p50=113.2 мс | bybit_book 389 сд. p50=110.7 мс | bybit_spot 225 сд. p50=114.2 мс | bybit_spot_book 161 сд. p50=111.8 мс | okx 215 сд. p50=157.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 9952 сд. p50=145.1 мс
23:13:33 [pm] T- 86.9s Up 0.97/0.98 Down 0.02/0.03 ptb=78618.8 | CLOB 5210 сообщ., задержка p50/p90=38.5/42.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793315613107 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.6/1.9 мс
23:13:39 [cex] Binance 123 сд. задержка p50/p90=144.7/149.7 мс | Coinbase 65 задержка p50=80.8 мс | смещение часов +19.4 мс | lag loop p99/max=5.4/11.9 мс
23:13:39 [cex] binance_futures 222 сд. p50=152.6 мс | bybit 178 сд. p50=113.0 мс | bybit_book 348 сд. p50=110.7 мс | bybit_spot 196 сд. p50=116.8 мс | bybit_spot_book 127 сд. p50=111.7 мс | okx 197 сд. p50=158.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 7263 сд. p50=143.9 мс
23:13:43 [pm] T- 76.9s Up 0.97/0.98 Down 0.02/0.03 ptb=78618.8 | CLOB 3600 сообщ., задержка p50/p90=38.2/39.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793315623108 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.0/2.1 мс
23:13:49 [cex] Binance 97 сд. задержка p50/p90=144.4/145.3 мс | Coinbase 48 задержка p50=78.0 мс | смещение часов +19.4 мс | lag loop p99/max=2.3/6.2 мс
23:13:49 [cex] binance_futures 165 сд. p50=149.3 мс | bybit 183 сд. p50=113.4 мс | bybit_book 359 сд. p50=110.7 мс | bybit_spot 103 сд. p50=113.3 мс | bybit_spot_book 122 сд. p50=111.6 мс | okx 131 сд. p50=156.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5348 сд. p50=143.6 мс
23:13:53 [pm] T- 66.9s Up 0.99/n/a Down n/a/0.01 ptb=78618.8 | CLOB 1333 сообщ., задержка p50/p90=38.5/51.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793315633109 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.9/2.1 мс
23:13:59 [cex] Binance 65 сд. задержка p50/p90=143.6/144.5 мс | Coinbase 33 задержка p50=78.2 мс | смещение часов +19.4 мс | lag loop p99/max=2.1/2.2 мс
23:13:59 [cex] binance_futures 62 сд. p50=271.4 мс | bybit 169 сд. p50=112.7 мс | bybit_book 367 сд. p50=110.6 мс | bybit_spot 4 сд. p50=112.8 мс | bybit_spot_book 70 сд. p50=111.6 мс | okx 31 сд. p50=155.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 945 сд. p50=143.5 мс
23:14:03 [pm] T- 56.9s Up 0.99/n/a Down n/a/0.01 ptb=78618.8 | CLOB 1161 сообщ., задержка p50/p90=38.2/65.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793315643111 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.2/2.9 мс
```

Представлено версией кода: b8783c2; python 3.12.3
