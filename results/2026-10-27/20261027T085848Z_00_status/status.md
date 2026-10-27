# Состояние сервера записи

Время (UTC): 2026-10-27 08:58:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 6 days, 1 hour, 34 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         573        1060           1         451        1332
Swap:           2047         390        1657
```
- нагрузка CPU (1/5/15 мин): 0.25 / 0.40 / 0.75

## Данные
- файлов: 5831, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 36 МБ | 0 |
| bn_book | 242 | 3 МБ | 21 |
| bnf_agg | 242 | 52 МБ | 0 |
| bnf_book | 46 | 407 МБ | 0 |
| bnf_depth5 | 26 | 10 МБ | 1206699 |
| bnf_liq | 216 | 144 КБ | 3446 |
| bs_trade | 26 | 410 КБ | 1206618 |
| by_book1 | 242 | 113 МБ | 0 |
| by_liq | 228 | 107 КБ | 1390 |
| by_trade | 242 | 35 МБ | 4 |
| bys_book1 | 218 | 74 МБ | 0 |
| bys_trade | 218 | 30 МБ | 2 |
| cb_ticker | 242 | 33 МБ | 0 |
| clock | 242 | 189 КБ | 57 |
| clock_pm | 242 | 189 КБ | 4 |
| events | 231 | 74 КБ | 439 |
| events_pm | 241 | 85 КБ | 496 |
| health_cex | 242 | 3 МБ | 9 |
| health_feeds | 242 | 8 МБ | 9 |
| health_pm | 242 | 3 МБ | 8 |
| kr_trade | 26 | 887 КБ | 1206618 |
| ok_trade | 241 | 45 МБ | 0 |
| pm_depth | 242 | 50 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 2 |
| pm_top | 242 | 103 МБ | 0 |
| pm_trades | 242 | 72 МБ | 12 |
| rtds | 242 | 16 МБ | 0 |
| windows | 242 | 502 КБ | 193 |

Дни с данными: 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 42, всего 289
- Polymarket CLOB: TCP 5, TLS 43, всего 82
- Polymarket gamma: TCP 4, TLS 36, всего 43

## Последние строки журнала записи
```
08:58:08 [pm] T-111.3s Up 0.99/n/a Down n/a/0.01 ptb=79653.8 | CLOB 995 сообщ., задержка p50/p90=42.2/44.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793091488704 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.9 мс | lag loop p99/max=2.1/2.2 мс
08:58:09 [cex] Binance 29 сд. задержка p50/p90=145.0/145.3 мс | Coinbase 31 задержка p50=92.6 мс | смещение часов +22.3 мс | lag loop p99/max=2.1/2.1 мс
08:58:09 [cex] binance_futures 18 сд. p50=294.9 мс | bybit 48 сд. p50=114.0 мс | bybit_book 180 сд. p50=111.8 мс | bybit_spot 12 сд. p50=114.4 мс | bybit_spot_book 92 сд. p50=112.4 мс | okx 34 сд. p50=162.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 858 сд. p50=145.6 мс
08:58:18 [pm] T-101.3s Up 0.99/n/a Down n/a/0.01 ptb=79653.8 | CLOB 764 сообщ., задержка p50/p90=42.1/43.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793091498705 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.8 мс | lag loop p99/max=2.1/2.1 мс
08:58:19 [cex] Binance 30 сд. задержка p50/p90=145.0/146.0 мс | Coinbase 28 задержка p50=92.6 мс | смещение часов +22.3 мс | lag loop p99/max=2.2/2.3 мс
08:58:19 [cex] binance_futures 23 сд. p50=294.7 мс | bybit 10 сд. p50=113.8 мс | bybit_book 129 сд. p50=111.8 мс | bybit_spot 20 сд. p50=114.2 мс | bybit_spot_book 91 сд. p50=112.5 мс | okx 15 сд. p50=162.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 524 сд. p50=145.6 мс
08:58:28 [pm] T- 91.3s Up 0.99/n/a Down n/a/0.01 ptb=79653.8 | CLOB 1130 сообщ., задержка p50/p90=42.1/43.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793091508706 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.8 мс | lag loop p99/max=2.1/2.1 мс
08:58:29 [cex] Binance 88 сд. задержка p50/p90=145.3/151.9 мс | Coinbase 32 задержка p50=92.9 мс | смещение часов +22.3 мс | lag loop p99/max=2.1/2.2 мс
08:58:29 [cex] binance_futures 57 сд. p50=150.8 мс | bybit 98 сд. p50=115.0 мс | bybit_book 292 сд. p50=111.8 мс | bybit_spot 157 сд. p50=127.5 мс | bybit_spot_book 76 сд. p50=112.5 мс | okx 71 сд. p50=163.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3021 сд. p50=145.8 мс
08:58:38 [pm] T- 81.3s Up 0.99/n/a Down n/a/0.01 ptb=79653.8 | CLOB 914 сообщ., задержка p50/p90=42.1/43.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793091518707 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.8 мс | lag loop p99/max=2.1/2.2 мс
08:58:39 [cex] Binance 36 сд. задержка p50/p90=145.0/145.7 мс | Coinbase 54 задержка p50=93.8 мс | смещение часов +22.3 мс | lag loop p99/max=2.1/2.2 мс
08:58:39 [cex] binance_futures 22 сд. p50=294.8 мс | bybit 45 сд. p50=114.1 мс | bybit_book 305 сд. p50=111.8 мс | bybit_spot 14 сд. p50=114.5 мс | bybit_spot_book 54 сд. p50=112.5 мс | okx 12 сд. p50=162.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1130 сд. p50=145.6 мс
08:58:48 [pm] T- 71.3s Up 0.99/n/a Down n/a/0.01 ptb=79653.8 | CLOB 860 сообщ., задержка p50/p90=41.5/43.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793091528708 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.8 мс | lag loop p99/max=2.1/2.1 мс
08:58:49 [cex] Binance 23 сд. задержка p50/p90=145.1/145.9 мс | Coinbase 23 задержка p50=92.9 мс | смещение часов +22.3 мс | lag loop p99/max=2.0/2.0 мс
08:58:49 [cex] binance_futures 26 сд. p50=294.6 мс | bybit 44 сд. p50=113.7 мс | bybit_book 299 сд. p50=111.8 мс | bybit_spot 15 сд. p50=114.2 мс | bybit_spot_book 66 сд. p50=112.4 мс | okx 12 сд. p50=162.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1020 сд. p50=145.6 мс
```

Представлено версией кода: ebe82a3; python 3.12.3
