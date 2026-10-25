# Состояние сервера записи

Время (UTC): 2026-10-25 06:11:18

## Службы
- lab-collector: inactive
- lab-runner.timer: active
- uptime: up 3 weeks, 3 days, 22 hours, 47 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 10 ГБ из 57 ГБ, свободно 47 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         540         374           2        1184        1365
Swap:           2047          94        1953
```
- нагрузка CPU (1/5/15 мин): 0.05 / 0.02 / 0.00

## Данные
- файлов: 6613, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 272 | 34 МБ | 318453 |
| bn_book | 272 | 3 МБ | 318456 |
| bnf_agg | 272 | 56 МБ | 318461 |
| bnf_book | 76 | 319 МБ | 1023772 |
| bnf_depth5 | 76 | 25 МБ | 1023848 |
| bnf_liq | 237 | 152 КБ | 318674 |
| bs_trade | 76 | 806 КБ | 1023768 |
| by_book1 | 272 | 111 МБ | 318456 |
| by_liq | 246 | 115 КБ | 318676 |
| by_trade | 272 | 38 МБ | 318461 |
| bys_book1 | 198 | 66 МБ | 318451 |
| bys_trade | 198 | 28 МБ | 318461 |
| cb_ticker | 272 | 33 МБ | 318455 |
| clock | 272 | 211 КБ | 318501 |
| clock_pm | 272 | 211 КБ | 318456 |
| events | 263 | 83 КБ | 318461 |
| events_pm | 272 | 95 КБ | 318455 |
| health_cex | 272 | 3 МБ | 318469 |
| health_feeds | 272 | 9 МБ | 318469 |
| health_pm | 272 | 3 МБ | 318455 |
| kr_trade | 76 | 2 МБ | 1023768 |
| ok_trade | 271 | 45 МБ | 318449 |
| pm_depth | 272 | 53 МБ | 318456 |
| pm_rtt | 272 | 2 МБ | 318455 |
| pm_top | 272 | 111 МБ | 318457 |
| pm_trades | 272 | 78 МБ | 318455 |
| rtds | 272 | 17 МБ | 318460 |
| windows | 272 | 561 КБ | 318455 |

Дни с данными: 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 34, всего 301
- Polymarket CLOB: TCP 6, TLS 36, всего 78
- Polymarket gamma: TCP 5, TLS 35, всего 65

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
