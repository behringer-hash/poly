# Состояние сервера записи

Время (UTC): 2026-10-15 04:13:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 20 hours, 49 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         609         323           2        1166        1296
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.18 / 0.22 / 0.20

## Данные
- файлов: 4056, всего 982 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 161 | 21 МБ | 2 |
| bn_book | 161 | 2 МБ | 2 |
| bnf_agg | 161 | 32 МБ | 2 |
| bnf_book | 118 | 557 МБ | 152722 |
| bnf_depth5 | 118 | 41 МБ | 152798 |
| bnf_liq | 144 | 95 КБ | 32 |
| bs_trade | 118 | 1 МБ | 152718 |
| by_book1 | 161 | 67 МБ | 2 |
| by_liq | 140 | 81 КБ | 1512 |
| by_trade | 161 | 21 МБ | 2 |
| bys_book1 | 45 | 16 МБ | 2 |
| bys_trade | 45 | 7 МБ | 2 |
| cb_ticker | 161 | 19 МБ | 2 |
| clock | 161 | 124 КБ | 16 |
| clock_pm | 161 | 124 КБ | 17 |
| events | 152 | 49 КБ | 38 |
| events_pm | 161 | 57 КБ | 451 |
| health_cex | 161 | 2 МБ | 4 |
| health_feeds | 161 | 6 МБ | 4 |
| health_pm | 161 | 2 МБ | 1 |
| kr_trade | 118 | 3 МБ | 152718 |
| ok_trade | 160 | 28 МБ | 2 |
| pm_depth | 161 | 32 МБ | 1 |
| pm_rtt | 161 | 1 МБ | 3 |
| pm_top | 161 | 65 МБ | 1 |
| pm_trades | 161 | 47 МБ | 1 |
| rtds | 161 | 10 МБ | 1 |
| windows | 161 | 330 КБ | 285 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 54, всего 303
- Polymarket CLOB: TCP 5, TLS 40, всего 81
- Polymarket gamma: TCP 5, TLS 39, всего 51

## Последние строки журнала записи
```
04:13:06 [cex] binance_liq: TimeoutError() (wss://fstream.binance.com/market/stream?streams=btcusdt@forceOrder)
04:13:06 [pm] T-113.2s Up 0.33/0.34 Down 0.66/0.67 ptb=80812.0 | CLOB 12950 сообщ., задержка p50/p90=41.5/44.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792037586824 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=10.5/11.7 мс
04:13:10 [cex] binance_liq подключён: wss://fstream.binance.com/market/stream?streams=btcusdt@forceOrder
04:13:13 [cex] Binance 54 сд. задержка p50/p90=144.9/147.6 мс | Coinbase 44 задержка p50=83.1 мс | смещение часов +20.4 мс | lag loop p99/max=2.6/36.0 мс
04:13:13 [cex] binance_futures 157 сд. p50=149.7 мс | bybit 139 сд. p50=114.4 мс | bybit_book 244 сд. p50=112.0 мс | bybit_spot 139 сд. p50=114.0 мс | bybit_spot_book 127 сд. p50=111.8 мс | okx 85 сд. p50=153.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:13:16 [pm] T-103.2s Up 0.51/0.52 Down 0.48/0.49 ptb=80812.0 | CLOB 12780 сообщ., задержка p50/p90=40.9/42.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792037596825 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=1.1/2.0 мс
04:13:23 [cex] Binance 116 сд. задержка p50/p90=146.3/149.1 мс | Coinbase 58 задержка p50=83.9 мс | смещение часов +20.4 мс | lag loop p99/max=2.1/2.2 мс
04:13:23 [cex] binance_futures 215 сд. p50=148.5 мс | bybit 243 сд. p50=114.2 мс | bybit_book 248 сд. p50=112.0 мс | bybit_spot 232 сд. p50=114.0 мс | bybit_spot_book 188 сд. p50=111.9 мс | okx 122 сд. p50=153.7 мс | binance_liq 1 сд. p50=1151.7 мс | bybit_liq 0 сд. p50=n/a мс
04:13:26 [pm] T- 93.2s Up 0.84/0.86 Down 0.14/0.16 ptb=80812.0 | CLOB 14951 сообщ., задержка p50/p90=42.4/48.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792037606828 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=2.3/4.5 мс
04:13:33 [cex] Binance 327 сд. задержка p50/p90=146.2/147.3 мс | Coinbase 63 задержка p50=85.6 мс | смещение часов +21.1 мс | lag loop p99/max=1.9/2.1 мс
04:13:33 [cex] binance_futures 333 сд. p50=148.2 мс | bybit 537 сд. p50=114.7 мс | bybit_book 347 сд. p50=112.1 мс | bybit_spot 287 сд. p50=114.6 мс | bybit_spot_book 259 сд. p50=112.2 мс | okx 342 сд. p50=154.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:13:36 [pm] T- 83.2s Up 0.89/0.90 Down 0.10/0.11 ptb=80812.0 | CLOB 5717 сообщ., задержка p50/p90=41.1/50.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792037616830 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=1.8/2.2 мс
04:13:43 [cex] Binance 151 сд. задержка p50/p90=145.9/147.4 мс | Coinbase 50 задержка p50=84.1 мс | смещение часов +21.1 мс | lag loop p99/max=2.2/2.2 мс
04:13:43 [cex] binance_futures 149 сд. p50=150.2 мс | bybit 139 сд. p50=115.1 мс | bybit_book 263 сд. p50=112.6 мс | bybit_spot 207 сд. p50=115.0 мс | bybit_spot_book 162 сд. p50=112.5 мс | okx 110 сд. p50=154.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:13:46 [pm] T- 73.2s Up 0.85/0.86 Down 0.14/0.15 ptb=80812.0 | CLOB 7703 сообщ., задержка p50/p90=40.1/54.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792037626831 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=2.1/2.2 мс
```

Представлено версией кода: ec1316a; python 3.12.3
