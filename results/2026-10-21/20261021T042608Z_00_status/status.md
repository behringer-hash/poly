# Состояние сервера записи

Время (UTC): 2026-10-21 04:26:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 21 hours, 2 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 9 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         788         447           1         863        1117
Swap:           2047         474        1573
```
- нагрузка CPU (1/5/15 мин): 0.54 / 0.40 / 0.34

## Данные
- файлов: 7479, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 305 | 39 МБ | 1 |
| bn_book | 305 | 4 МБ | 34 |
| bnf_agg | 305 | 60 МБ | 1 |
| bnf_book | 118 | 557 МБ | 671862 |
| bnf_depth5 | 118 | 41 МБ | 671939 |
| bnf_liq | 266 | 171 КБ | 7181 |
| bs_trade | 118 | 1 МБ | 671858 |
| by_book1 | 305 | 127 МБ | 1 |
| by_liq | 275 | 135 КБ | 100 |
| by_trade | 305 | 39 МБ | 1 |
| bys_book1 | 189 | 63 МБ | 1 |
| bys_trade | 189 | 25 МБ | 1 |
| cb_ticker | 305 | 37 МБ | 1 |
| clock | 305 | 235 КБ | 34 |
| clock_pm | 305 | 236 КБ | 9 |
| events | 294 | 94 КБ | 459 |
| events_pm | 305 | 110 КБ | 37 |
| health_cex | 305 | 3 МБ | 9 |
| health_feeds | 305 | 10 МБ | 9 |
| health_pm | 305 | 3 МБ | 1 |
| kr_trade | 118 | 3 МБ | 671858 |
| ok_trade | 304 | 53 МБ | 1 |
| pm_depth | 305 | 61 МБ | 1 |
| pm_rtt | 305 | 2 МБ | 5 |
| pm_top | 305 | 125 МБ | 1 |
| pm_trades | 305 | 88 МБ | 1 |
| rtds | 305 | 19 МБ | 1 |
| windows | 305 | 629 КБ | 93 |

Дни с данными: 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 46, всего 295
- Polymarket CLOB: TCP 5, TLS 54, всего 95
- Polymarket gamma: TCP 5, TLS 57, всего 68

## Последние строки журнала записи
```
04:25:25 [pm] T-274.6s Up 0.48/0.49 Down 0.51/0.52 ptb=82705.0 | CLOB 7022 сообщ., задержка p50/p90=38.8/40.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792556725365 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.4 мс | lag loop p99/max=1.2/2.9 мс
04:25:28 [cex] Binance 10 сд. задержка p50/p90=142.1/143.1 мс | Coinbase 52 задержка p50=77.3 мс | смещение часов +18.0 мс | lag loop p99/max=2.2/2.3 мс
04:25:28 [cex] binance_futures 14 сд. p50=291.4 мс | bybit 1 сд. p50=111.3 мс | bybit_book 61 сд. p50=110.3 мс | bybit_spot 2 сд. p50=112.1 мс | bybit_spot_book 29 сд. p50=110.7 мс | okx 9 сд. p50=145.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:25:35 [pm] T-264.6s Up 0.76/0.77 Down 0.23/0.24 ptb=82705.0 | CLOB 8716 сообщ., задержка p50/p90=57.9/59.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792556735366 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=4.3/6.2 мс
04:25:38 [cex] Binance 82 сд. задержка p50/p90=142.1/143.3 мс | Coinbase 55 задержка p50=82.1 мс | смещение часов +24.3 мс | lag loop p99/max=2.2/2.3 мс
04:25:38 [cex] binance_futures 115 сд. p50=143.2 мс | bybit 72 сд. p50=112.4 мс | bybit_book 146 сд. p50=110.3 мс | bybit_spot 303 сд. p50=132.5 мс | bybit_spot_book 154 сд. p50=110.6 мс | okx 75 сд. p50=145.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:25:45 [pm] T-254.6s Up 0.72/0.73 Down 0.27/0.28 ptb=82705.0 | CLOB 7060 сообщ., задержка p50/p90=58.1/60.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792556745367 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=1.2/1.2 мс
04:25:48 [cex] Binance 18 сд. задержка p50/p90=148.3/148.5 мс | Coinbase 41 задержка p50=83.1 мс | смещение часов +24.3 мс | lag loop p99/max=2.1/2.2 мс
04:25:48 [cex] binance_futures 13 сд. p50=297.9 мс | bybit 1 сд. p50=117.6 мс | bybit_book 43 сд. p50=116.6 мс | bybit_spot 4 сд. p50=118.3 мс | bybit_spot_book 37 сд. p50=117.1 мс | okx 8 сд. p50=151.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:25:55 [pm] T-244.6s Up 0.78/0.79 Down 0.21/0.22 ptb=82705.0 | CLOB 5609 сообщ., задержка p50/p90=58.6/82.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792556755369 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.4 мс | lag loop p99/max=2.0/2.1 мс
04:25:58 [cex] Binance 21 сд. задержка p50/p90=148.3/149.2 мс | Coinbase 41 задержка p50=83.2 мс | смещение часов +24.3 мс | lag loop p99/max=2.0/2.1 мс
04:25:58 [cex] binance_futures 58 сд. p50=149.3 мс | bybit 43 сд. p50=118.7 мс | bybit_book 124 сд. p50=116.6 мс | bybit_spot 158 сд. p50=120.3 мс | bybit_spot_book 116 сд. p50=116.8 мс | okx 101 сд. p50=152.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:26:05 [pm] T-234.6s Up 0.69/0.70 Down 0.30/0.31 ptb=82705.0 | CLOB 9574 сообщ., задержка p50/p90=61.8/76.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792556765370 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.9/2.4 мс
04:26:08 [cex] Binance 17 сд. задержка p50/p90=148.4/148.6 мс | Coinbase 51 задержка p50=83.2 мс | смещение часов +24.3 мс | lag loop p99/max=2.2/2.4 мс
04:26:08 [cex] binance_futures 60 сд. p50=149.9 мс | bybit 37 сд. p50=118.3 мс | bybit_book 178 сд. p50=116.6 мс | bybit_spot 71 сд. p50=120.8 мс | bybit_spot_book 71 сд. p50=116.9 мс | okx 47 сд. p50=151.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 96010db; python 3.12.3
