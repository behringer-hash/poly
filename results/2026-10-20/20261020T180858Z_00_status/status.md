# Состояние сервера записи

Время (UTC): 2026-10-20 18:08:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 10 hours, 45 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         749         643           1         704        1156
Swap:           2047         478        1569
```
- нагрузка CPU (1/5/15 мин): 0.24 / 0.32 / 0.32

## Данные
- файлов: 7241, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 295 | 38 МБ | 0 |
| bn_book | 295 | 4 МБ | 15 |
| bnf_agg | 295 | 58 МБ | 0 |
| bnf_book | 118 | 557 МБ | 634832 |
| bnf_depth5 | 118 | 41 МБ | 634909 |
| bnf_liq | 257 | 168 КБ | 2468 |
| bs_trade | 118 | 1 МБ | 634828 |
| by_book1 | 295 | 122 МБ | 0 |
| by_liq | 266 | 133 КБ | 1242 |
| by_trade | 295 | 38 МБ | 0 |
| bys_book1 | 179 | 60 МБ | 0 |
| bys_trade | 179 | 24 МБ | 7 |
| cb_ticker | 295 | 36 МБ | 0 |
| clock | 295 | 227 КБ | 19 |
| clock_pm | 295 | 227 КБ | 55 |
| events | 284 | 90 КБ | 21 |
| events_pm | 295 | 106 КБ | 498 |
| health_cex | 295 | 3 МБ | 4 |
| health_feeds | 295 | 10 МБ | 4 |
| health_pm | 295 | 3 МБ | 7 |
| kr_trade | 118 | 3 МБ | 634828 |
| ok_trade | 294 | 51 МБ | 0 |
| pm_depth | 295 | 58 МБ | 1 |
| pm_rtt | 295 | 2 МБ | 1 |
| pm_top | 295 | 119 МБ | 1 |
| pm_trades | 295 | 85 МБ | 1 |
| rtds | 295 | 19 МБ | 1 |
| windows | 295 | 607 КБ | 203 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 41, всего 290
- Polymarket CLOB: TCP 5, TLS 42, всего 85
- Polymarket gamma: TCP 5, TLS 49, всего 61

## Последние строки журнала записи
```
18:08:13 [cex] binance_futures 122 сд. p50=145.7 мс | bybit 208 сд. p50=114.2 мс | bybit_book 271 сд. p50=112.4 мс | bybit_spot 229 сд. p50=113.9 мс | bybit_spot_book 175 сд. p50=112.0 мс | okx 179 сд. p50=154.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:08:19 [pm] T-100.2s Up 0.62/0.63 Down 0.37/0.38 ptb=82635.5 | CLOB 14545 сообщ., задержка p50/p90=40.6/43.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792519699844 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.3/1.5 мс
18:08:23 [cex] Binance 91 сд. задержка p50/p90=144.5/145.0 мс | Coinbase 46 задержка p50=78.1 мс | смещение часов +20.0 мс | lag loop p99/max=2.2/2.7 мс
18:08:23 [cex] binance_futures 90 сд. p50=147.4 мс | bybit 112 сд. p50=114.2 мс | bybit_book 201 сд. p50=112.5 мс | bybit_spot 44 сд. p50=113.9 мс | bybit_spot_book 100 сд. p50=112.1 мс | okx 71 сд. p50=154.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:08:29 [pm] T- 90.2s Up 0.73/0.75 Down 0.25/0.27 ptb=82635.5 | CLOB 8694 сообщ., задержка p50/p90=40.6/44.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792519709846 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.3/2.4 мс
18:08:32 [cex] binance_liq: TimeoutError() (wss://fstream.binance.com/public/stream?streams=btcusdt@forceOrder)
18:08:33 [cex] Binance 96 сд. задержка p50/p90=144.7/145.8 мс | Coinbase 41 задержка p50=78.3 мс | смещение часов +20.0 мс | lag loop p99/max=2.1/2.1 мс
18:08:33 [cex] binance_futures 147 сд. p50=145.8 мс | bybit 129 сд. p50=114.1 мс | bybit_book 246 сд. p50=112.5 мс | bybit_spot 120 сд. p50=114.1 мс | bybit_spot_book 146 сд. p50=112.1 мс | okx 124 сд. p50=154.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:08:35 [cex] binance_liq подключён: wss://fstream.binance.com/ws/btcusdt@forceOrder
18:08:39 [pm] T- 80.2s Up 0.92/0.93 Down 0.07/0.08 ptb=82635.5 | CLOB 9330 сообщ., задержка p50/p90=40.7/49.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792519719848 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/8.0 мс
18:08:43 [cex] Binance 137 сд. задержка p50/p90=144.4/145.8 мс | Coinbase 47 задержка p50=79.0 мс | смещение часов +19.7 мс | lag loop p99/max=2.0/38.6 мс
18:08:43 [cex] binance_futures 196 сд. p50=146.5 мс | bybit 465 сд. p50=114.5 мс | bybit_book 214 сд. p50=112.2 мс | bybit_spot 316 сд. p50=114.0 мс | bybit_spot_book 159 сд. p50=111.9 мс | okx 272 сд. p50=153.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:08:49 [pm] T- 70.2s Up 0.84/0.85 Down 0.15/0.16 ptb=82635.5 | CLOB 9651 сообщ., задержка p50/p90=63.6/177.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792519729849 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.9/2.2 мс
18:08:53 [cex] Binance 14 сд. задержка p50/p90=144.1/145.0 мс | Coinbase 39 задержка p50=77.8 мс | смещение часов +19.7 мс | lag loop p99/max=2.3/2.3 мс
18:08:53 [cex] binance_futures 23 сд. p50=293.6 мс | bybit 124 сд. p50=113.8 мс | bybit_book 170 сд. p50=112.2 мс | bybit_spot 44 сд. p50=113.7 мс | bybit_spot_book 85 сд. p50=111.7 мс | okx 18 сд. p50=153.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 96010db; python 3.12.3
