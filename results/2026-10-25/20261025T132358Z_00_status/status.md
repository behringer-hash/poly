# Состояние сервера записи

Время (UTC): 2026-10-25 13:23:58

## Службы
- lab-collector: inactive
- lab-runner.timer: active
- uptime: up 3 weeks, 4 days, 6 hours, 0 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 10 ГБ из 57 ГБ, свободно 47 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         543         167           2        1389        1362
Swap:           2047          94        1953
```
- нагрузка CPU (1/5/15 мин): 0.00 / 0.00 / 0.00

## Данные
- файлов: 6437, всего 1016 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 265 | 34 МБ | 344413 |
| bn_book | 265 | 3 МБ | 344416 |
| bnf_agg | 265 | 55 МБ | 344421 |
| bnf_book | 69 | 309 МБ | 1049732 |
| bnf_depth5 | 69 | 23 МБ | 1049808 |
| bnf_liq | 233 | 150 КБ | 344634 |
| bs_trade | 69 | 764 КБ | 1049728 |
| by_book1 | 265 | 109 МБ | 344416 |
| by_liq | 242 | 114 КБ | 344636 |
| by_trade | 265 | 38 МБ | 344421 |
| bys_book1 | 198 | 66 МБ | 344411 |
| bys_trade | 198 | 28 МБ | 344421 |
| cb_ticker | 265 | 32 МБ | 344415 |
| clock | 265 | 206 КБ | 344461 |
| clock_pm | 265 | 205 КБ | 344416 |
| events | 256 | 80 КБ | 344421 |
| events_pm | 265 | 92 КБ | 344415 |
| health_cex | 265 | 3 МБ | 344429 |
| health_feeds | 265 | 8 МБ | 344429 |
| health_pm | 265 | 3 МБ | 344415 |
| kr_trade | 69 | 2 МБ | 1049728 |
| ok_trade | 264 | 45 МБ | 344409 |
| pm_depth | 265 | 52 МБ | 344416 |
| pm_rtt | 265 | 2 МБ | 344415 |
| pm_top | 265 | 108 МБ | 344417 |
| pm_trades | 265 | 77 МБ | 344415 |
| rtds | 265 | 17 МБ | 344420 |
| windows | 265 | 547 КБ | 344415 |

Дни с данными: 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 6, TLS 38, всего 288
- Polymarket CLOB: TCP 6, TLS 37, всего 78
- Polymarket gamma: TCP 4, TLS 34, всего 42

## Последние строки журнала записи
```
13:42:48 [cex] binance_futures 136 сд. p50=159.1 мс | bybit 231 сд. p50=117.7 мс | bybit_book 351 сд. p50=115.3 мс | bybit_spot 120 сд. p50=129.8 мс | bybit_spot_book 122 сд. p50=115.5 мс | okx 214 сд. p50=149.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:42:49 [pm] T-130.8s Up 0.04/0.05 Down 0.95/0.96 ptb=83489.2 | CLOB 5948 сообщ., задержка p50/p90=43.4/46.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590169239 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.7/1.8 мс
13:42:58 [cex] Binance 194 сд. задержка p50/p90=170.9/172.1 мс | Coinbase 84 задержка p50=81.0 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/7.6 мс
13:42:58 [cex] binance_futures 320 сд. p50=160.6 мс | bybit 599 сд. p50=141.2 мс | bybit_book 301 сд. p50=115.3 мс | bybit_spot 220 сд. p50=124.5 мс | bybit_spot_book 197 сд. p50=115.4 мс | okx 369 сд. p50=163.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:42:59 [pm] T-120.8s Up 0.01/0.02 Down 0.98/0.99 ptb=83489.2 | CLOB 5791 сообщ., задержка p50/p90=41.4/43.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590179241 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.0/2.1 мс
13:43:08 [cex] Binance 552 сд. задержка p50/p90=149.4/163.6 мс | Coinbase 78 задержка p50=80.3 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/4.0 мс
13:43:08 [cex] binance_futures 503 сд. p50=158.7 мс | bybit 665 сд. p50=117.0 мс | bybit_book 494 сд. p50=114.1 мс | bybit_spot 384 сд. p50=124.9 мс | bybit_spot_book 260 сд. p50=114.3 мс | okx 619 сд. p50=149.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:43:09 [pm] T-110.8s Up 0.16/0.17 Down 0.83/0.84 ptb=83489.2 | CLOB 13057 сообщ., задержка p50/p90=41.5/43.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590189243 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.3/4.0 мс
13:43:18 [cex] Binance 305 сд. задержка p50/p90=156.5/158.7 мс | Coinbase 97 задержка p50=83.0 мс | смещение часов +22.1 мс | lag loop p99/max=2.1/2.1 мс
13:43:18 [cex] binance_futures 366 сд. p50=160.4 мс | bybit 483 сд. p50=117.0 мс | bybit_book 465 сд. p50=114.1 мс | bybit_spot 275 сд. p50=123.8 мс | bybit_spot_book 218 сд. p50=114.3 мс | okx 371 сд. p50=148.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:43:19 [pm] T-100.8s Up 0.19/0.20 Down 0.80/0.81 ptb=83489.2 | CLOB 13971 сообщ., задержка p50/p90=41.4/42.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590199244 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.8/3.3 мс
13:43:28 [cex] Binance 262 сд. задержка p50/p90=148.2/154.1 мс | Coinbase 58 задержка p50=79.7 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/2.9 мс
13:43:28 [cex] binance_futures 254 сд. p50=149.6 мс | bybit 216 сд. p50=116.4 мс | bybit_book 433 сд. p50=114.1 мс | bybit_spot 108 сд. p50=118.7 мс | bybit_spot_book 156 сд. p50=114.3 мс | okx 323 сд. p50=148.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:43:29 [pm] T- 90.8s Up 0.35/0.36 Down 0.64/0.65 ptb=83489.2 | CLOB 14782 сообщ., задержка p50/p90=41.5/44.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590209247 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.6/2.2 мс
[run] остановка...
```

Представлено версией кода: b98a05a; python 3.12.3
