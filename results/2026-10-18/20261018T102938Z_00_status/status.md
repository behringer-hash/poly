# Состояние сервера записи

Время (UTC): 2026-10-18 10:29:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 3 hours, 5 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         867         471           2         855        1038
Swap:           2047         236        1811
```
- нагрузка CPU (1/5/15 мин): 0.09 / 0.35 / 0.33

## Данные
- файлов: 5902, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 239 | 31 МБ | 0 |
| bn_book | 239 | 3 МБ | 0 |
| bnf_agg | 239 | 47 МБ | 0 |
| bnf_book | 118 | 557 МБ | 434472 |
| bnf_depth5 | 118 | 41 МБ | 434548 |
| bnf_liq | 205 | 139 КБ | 2900 |
| bs_trade | 118 | 1 МБ | 434468 |
| by_book1 | 239 | 98 МБ | 0 |
| by_liq | 211 | 113 КБ | 2902 |
| by_trade | 239 | 30 МБ | 0 |
| bys_book1 | 123 | 43 МБ | 0 |
| bys_trade | 123 | 17 МБ | 0 |
| cb_ticker | 239 | 29 МБ | 0 |
| clock | 239 | 184 КБ | 11 |
| clock_pm | 239 | 185 КБ | 39 |
| events | 228 | 74 КБ | 455 |
| events_pm | 239 | 87 КБ | 503 |
| health_cex | 239 | 2 МБ | 9 |
| health_feeds | 239 | 8 МБ | 9 |
| health_pm | 239 | 3 МБ | 8 |
| kr_trade | 118 | 3 МБ | 434468 |
| ok_trade | 238 | 41 МБ | 0 |
| pm_depth | 239 | 48 МБ | 2 |
| pm_rtt | 239 | 2 МБ | 4 |
| pm_top | 239 | 97 МБ | 2 |
| pm_trades | 239 | 69 МБ | 14 |
| rtds | 239 | 15 МБ | 2 |
| windows | 239 | 493 КБ | 63 |

Дни с данными: 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 37, всего 286
- Polymarket CLOB: TCP 5, TLS 37, всего 79
- Polymarket gamma: TCP 5, TLS 37, всего 50

## Последние строки журнала записи
```
10:28:49 [cex] Binance 112 сд. задержка p50/p90=143.9/149.0 мс | Coinbase 52 задержка p50=79.1 мс | смещение часов +19.9 мс | lag loop p99/max=2.2/2.2 мс
10:28:49 [cex] binance_futures 198 сд. p50=149.2 мс | bybit 39 сд. p50=117.8 мс | bybit_book 76 сд. p50=111.5 мс | bybit_spot 72 сд. p50=119.0 мс | bybit_spot_book 145 сд. p50=111.6 мс | okx 130 сд. p50=155.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:28:49 [pm] T- 70.8s Up 0.99/n/a Down n/a/0.01 ptb=82077.7 | CLOB 1369 сообщ., задержка p50/p90=38.6/41.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792319329226 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=2.1/2.1 мс
10:28:59 [cex] Binance 255 сд. задержка p50/p90=143.8/144.2 мс | Coinbase 35 задержка p50=77.1 мс | смещение часов +19.9 мс | lag loop p99/max=2.1/2.2 мс
10:28:59 [cex] binance_futures 64 сд. p50=293.2 мс | bybit 67 сд. p50=120.0 мс | bybit_book 87 сд. p50=111.4 мс | bybit_spot 107 сд. p50=114.1 мс | bybit_spot_book 171 сд. p50=111.7 мс | okx 77 сд. p50=154.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:28:59 [pm] T- 60.8s Up 0.99/n/a Down n/a/0.01 ptb=82077.7 | CLOB 865 сообщ., задержка p50/p90=38.5/87.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792319339227 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=2.2/2.2 мс
10:29:09 [cex] Binance 96 сд. задержка p50/p90=143.7/144.7 мс | Coinbase 11 задержка p50=77.9 мс | смещение часов +19.9 мс | lag loop p99/max=2.0/2.1 мс
10:29:09 [cex] binance_futures 42 сд. p50=293.3 мс | bybit 47 сд. p50=114.0 мс | bybit_book 92 сд. p50=111.5 мс | bybit_spot 80 сд. p50=114.0 мс | bybit_spot_book 204 сд. p50=111.6 мс | okx 23 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:29:09 [pm] T- 50.8s Up 0.99/n/a Down n/a/0.01 ptb=82077.7 | CLOB 751 сообщ., задержка p50/p90=38.7/39.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792319349228 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=2.1/2.2 мс
10:29:19 [cex] Binance 55 сд. задержка p50/p90=144.3/145.3 мс | Coinbase 7 задержка p50=77.2 мс | смещение часов +19.9 мс | lag loop p99/max=2.0/2.1 мс
10:29:19 [cex] binance_futures 64 сд. p50=161.7 мс | bybit 142 сд. p50=115.5 мс | bybit_book 124 сд. p50=111.5 мс | bybit_spot 58 сд. p50=114.5 мс | bybit_spot_book 187 сд. p50=111.5 мс | okx 72 сд. p50=154.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:29:19 [pm] T- 40.8s Up 0.99/n/a Down n/a/0.01 ptb=82077.7 | CLOB 695 сообщ., задержка p50/p90=38.6/39.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792319359230 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.1/2.1 мс
10:29:29 [cex] Binance 383 сд. задержка p50/p90=143.7/144.6 мс | Coinbase 29 задержка p50=78.2 мс | смещение часов +18.9 мс | lag loop p99/max=2.2/2.2 мс
10:29:29 [cex] binance_futures 154 сд. p50=146.4 мс | bybit 240 сд. p50=123.4 мс | bybit_book 125 сд. p50=111.4 мс | bybit_spot 435 сд. p50=114.6 мс | bybit_spot_book 180 сд. p50=111.5 мс | okx 133 сд. p50=153.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:29:29 [pm] T- 30.8s Up 0.99/n/a Down n/a/0.01 ptb=82077.7 | CLOB 726 сообщ., задержка p50/p90=38.7/39.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792319369232 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.0/2.2 мс
```

Представлено версией кода: b24b4e3; python 3.12.3
