# Состояние сервера записи

Время (UTC): 2026-10-14 22:03:06

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 14 hours, 39 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         610         379           2        1108        1295
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.16 / 0.14 / 0.10

## Данные
- файлов: 3908, всего 951 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 155 | 19 МБ | 1 |
| bn_book | 155 | 2 МБ | 1 |
| bnf_agg | 155 | 29 МБ | 1 |
| bnf_book | 118 | 557 МБ | 130480 |
| bnf_depth5 | 118 | 41 МБ | 130557 |
| bnf_liq | 137 | 88 КБ | 1807 |
| bs_trade | 118 | 1 МБ | 130476 |
| by_book1 | 155 | 62 МБ | 1 |
| by_liq | 134 | 71 КБ | 262 |
| by_trade | 155 | 19 МБ | 1 |
| bys_book1 | 39 | 12 МБ | 1 |
| bys_trade | 39 | 5 МБ | 1 |
| cb_ticker | 155 | 18 МБ | 1 |
| clock | 155 | 119 КБ | 27 |
| clock_pm | 155 | 119 КБ | 29 |
| events | 145 | 48 КБ | 583 |
| events_pm | 154 | 56 КБ | 392 |
| health_cex | 155 | 2 МБ | 5 |
| health_feeds | 155 | 6 МБ | 5 |
| health_pm | 155 | 2 МБ | 1 |
| kr_trade | 118 | 3 МБ | 130476 |
| ok_trade | 154 | 26 МБ | 1 |
| pm_depth | 155 | 30 МБ | 1 |
| pm_rtt | 155 | 1024 КБ | 3 |
| pm_top | 155 | 61 МБ | 1 |
| pm_trades | 155 | 45 МБ | 1 |
| rtds | 155 | 10 МБ | 1 |
| windows | 154 | 321 КБ | 211 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 36, всего 285
- Polymarket CLOB: TCP 5, TLS 46, всего 88
- Polymarket gamma: TCP 5, TLS 40, всего 53

## Последние строки журнала записи
```
22:02:20 [cex] Binance 190 сд. задержка p50/p90=142.3/143.5 мс | Coinbase 69 задержка p50=85.0 мс | смещение часов +18.2 мс | lag loop p99/max=2.1/2.2 мс
22:02:20 [cex] binance_futures 191 сд. p50=144.6 мс | bybit 324 сд. p50=112.6 мс | bybit_book 258 сд. p50=110.0 мс | bybit_spot 322 сд. p50=112.3 мс | bybit_spot_book 150 сд. p50=110.2 мс | okx 135 сд. p50=150.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:02:23 [pm] T-156.3s Up 0.18/0.19 Down 0.81/0.82 ptb=81678.3 | CLOB 14168 сообщ., задержка p50/p90=41.2/70.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792015343685 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.7 мс | lag loop p99/max=3.0/4.0 мс
22:02:30 [cex] Binance 73 сд. задержка p50/p90=145.9/149.2 мс | Coinbase 54 задержка p50=82.6 мс | смещение часов +18.2 мс | lag loop p99/max=2.0/2.1 мс
22:02:30 [cex] binance_futures 157 сд. p50=145.1 мс | bybit 216 сд. p50=112.4 мс | bybit_book 211 сд. p50=110.0 мс | bybit_spot 228 сд. p50=112.2 мс | bybit_spot_book 126 сд. p50=110.2 мс | okx 140 сд. p50=151.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:02:33 [pm] T-146.3s Up 0.15/0.16 Down 0.84/0.85 ptb=81678.3 | CLOB 6056 сообщ., задержка p50/p90=38.8/43.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792015353687 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.7 мс | lag loop p99/max=1.9/2.0 мс
22:02:40 [cex] Binance 54 сд. задержка p50/p90=143.4/144.3 мс | Coinbase 43 задержка p50=82.2 мс | смещение часов +19.6 мс | lag loop p99/max=2.2/2.2 мс
22:02:40 [cex] binance_futures 36 сд. p50=281.5 мс | bybit 71 сд. p50=113.2 мс | bybit_book 118 сд. p50=110.1 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 28 сд. p50=111.3 мс | okx 23 сд. p50=152.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:02:43 [pm] T-136.3s Up 0.18/0.19 Down 0.81/0.82 ptb=81678.3 | CLOB 7475 сообщ., задержка p50/p90=64.3/125.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792015363688 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.7 мс | lag loop p99/max=2.2/2.9 мс
22:02:50 [cex] Binance 104 сд. задержка p50/p90=143.7/144.7 мс | Coinbase 64 задержка p50=85.2 мс | смещение часов +19.6 мс | lag loop p99/max=2.1/2.2 мс
22:02:50 [cex] binance_futures 107 сд. p50=145.5 мс | bybit 189 сд. p50=113.8 мс | bybit_book 210 сд. p50=111.3 мс | bybit_spot 132 сд. p50=113.9 мс | bybit_spot_book 104 сд. p50=111.6 мс | okx 196 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:02:53 [pm] T-126.3s Up 0.05/0.06 Down 0.94/0.95 ptb=81678.3 | CLOB 6858 сообщ., задержка p50/p90=36.4/39.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792015373689 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=1.9/2.0 мс
22:03:00 [cex] Binance 87 сд. задержка p50/p90=143.8/145.0 мс | Coinbase 64 задержка p50=83.1 мс | смещение часов +19.6 мс | lag loop p99/max=2.1/2.2 мс
22:03:00 [cex] binance_futures 67 сд. p50=147.5 мс | bybit 12 сд. p50=113.3 мс | bybit_book 118 сд. p50=111.3 мс | bybit_spot 26 сд. p50=113.9 мс | bybit_spot_book 79 сд. p50=111.6 мс | okx 19 сд. p50=151.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:03:03 [pm] T-116.3s Up 0.03/0.04 Down 0.96/0.97 ptb=81678.3 | CLOB 3915 сообщ., задержка p50/p90=36.2/38.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792015383690 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=4.4/5.2 мс
```

Представлено версией кода: ec1316a; python 3.12.3
