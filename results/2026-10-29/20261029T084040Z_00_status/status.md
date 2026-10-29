# Состояние сервера записи

Время (UTC): 2026-10-29 08:40:40

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 1 hour, 16 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         522         751           1         802        1383
Swap:           2047         316        1731
```
- нагрузка CPU (1/5/15 мин): 0.33 / 0.23 / 0.24

## Данные
- файлов: 5817, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 1 |
| bn_book | 242 | 3 МБ | 19 |
| bnf_agg | 242 | 51 МБ | 1 |
| bnf_book | 68 | 438 МБ | 1 |
| bnf_liq | 212 | 139 КБ | 1725 |
| by_book1 | 242 | 112 МБ | 1 |
| by_liq | 224 | 100 КБ | 1139 |
| by_trade | 242 | 34 МБ | 1 |
| bys_book1 | 242 | 83 МБ | 1 |
| bys_trade | 242 | 33 МБ | 1 |
| cb_ticker | 242 | 32 МБ | 7 |
| clock | 242 | 188 КБ | 35 |
| clock_pm | 242 | 188 КБ | 9 |
| events | 231 | 73 КБ | 503 |
| events_pm | 242 | 83 КБ | 87 |
| health_cex | 242 | 3 МБ | 1 |
| health_feeds | 242 | 8 МБ | 1 |
| health_pm | 242 | 3 МБ | 5 |
| ok_trade | 242 | 44 МБ | 1 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 5 |
| pm_top | 242 | 102 МБ | 1 |
| pm_trades | 242 | 72 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 500 КБ | 5 |

Дни с данными: 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 40, всего 290
- Polymarket CLOB: TCP 5, TLS 41, всего 87
- Polymarket gamma: TCP 5, TLS 37, всего 46

## Последние строки журнала записи
```
08:39:54 [pm] T-  5.0s Up n/a/0.01 Down 0.99/n/a ptb=79950.5 | CLOB 2484 сообщ., задержка p50/p90=39.1/50.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793263194961 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.1/25.2 мс
08:39:58 [cex] Binance 133 сд. задержка p50/p90=144.7/147.5 мс | Coinbase 9 задержка p50=93.1 мс | смещение часов +20.1 мс | lag loop p99/max=2.2/9.1 мс
08:39:58 [cex] binance_futures 75 сд. p50=149.9 мс | bybit 55 сд. p50=115.8 мс | bybit_book 178 сд. p50=111.3 мс | bybit_spot 133 сд. p50=117.6 мс | bybit_spot_book 58 сд. p50=112.6 мс | okx 67 сд. p50=147.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2579 сд. p50=148.1 мс
08:40:04 [pm] T-295.0s Up 0.35/0.36 Down 0.64/0.65 ptb=79944.1 | CLOB 3001 сообщ., задержка p50/p90=36.7/41.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793263204963 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=3.3/4.0 мс
08:40:08 [cex] Binance 53 сд. задержка p50/p90=144.5/145.6 мс | Coinbase 27 задержка p50=92.9 мс | смещение часов +18.9 мс | lag loop p99/max=2.3/2.6 мс
08:40:08 [cex] binance_futures 29 сд. p50=293.3 мс | bybit 27 сд. p50=113.1 мс | bybit_book 117 сд. p50=111.3 мс | bybit_spot 2 сд. p50=113.5 мс | bybit_spot_book 36 сд. p50=112.3 мс | okx 15 сд. p50=146.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 397 сд. p50=144.4 мс
08:40:14 [pm] T-285.0s Up 0.31/0.32 Down 0.68/0.69 ptb=79944.1 | CLOB 6487 сообщ., задержка p50/p90=36.4/37.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793263214965 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.1/4.6 мс
08:40:18 [cex] Binance 59 сд. задержка p50/p90=143.7/143.9 мс | Coinbase 29 задержка p50=90.9 мс | смещение часов +18.9 мс | lag loop p99/max=2.2/2.7 мс
08:40:18 [cex] binance_futures 54 сд. p50=176.8 мс | bybit 38 сд. p50=114.9 мс | bybit_book 129 сд. p50=110.1 мс | bybit_spot 109 сд. p50=115.1 мс | bybit_spot_book 41 сд. p50=111.3 мс | okx 74 сд. p50=147.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2190 сд. p50=144.2 мс
08:40:24 [pm] T-275.0s Up 0.30/0.31 Down 0.69/0.70 ptb=79944.1 | CLOB 7300 сообщ., задержка p50/p90=46.1/207.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793263224966 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.1/2.4 мс
08:40:28 [cex] Binance 33 сд. задержка p50/p90=143.5/144.2 мс | Coinbase 5 задержка p50=90.1 мс | смещение часов +18.9 мс | lag loop p99/max=2.1/2.2 мс
08:40:28 [cex] binance_futures 47 сд. p50=292.1 мс | bybit 2 сд. p50=111.9 мс | bybit_book 109 сд. p50=110.1 мс | bybit_spot 88 сд. p50=113.3 мс | bybit_spot_book 53 сд. p50=111.4 мс | okx 15 сд. p50=146.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1696 сд. p50=143.7 мс
08:40:34 [pm] T-265.0s Up 0.27/0.28 Down 0.72/0.73 ptb=79944.1 | CLOB 3876 сообщ., задержка p50/p90=38.3/44.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793263234968 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.3/1.8 мс
08:40:38 [cex] Binance 23 сд. задержка p50/p90=143.4/143.8 мс | Coinbase 1 задержка p50=90.8 мс | смещение часов +18.9 мс | lag loop p99/max=2.1/2.1 мс
08:40:38 [cex] binance_futures 29 сд. p50=292.2 мс | bybit 27 сд. p50=111.7 мс | bybit_book 91 сд. p50=110.1 мс | bybit_spot 2 сд. p50=113.5 мс | bybit_spot_book 30 сд. p50=111.5 мс | okx 11 сд. p50=145.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 672 сд. p50=143.6 мс
```

Представлено версией кода: c4da76d; python 3.12.3
