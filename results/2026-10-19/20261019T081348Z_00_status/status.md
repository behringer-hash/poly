# Состояние сервера записи

Время (UTC): 2026-10-19 08:13:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 5 days, 49 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         662         625           1         796        1243
Swap:           2047         252        1795
```
- нагрузка CPU (1/5/15 мин): 0.35 / 0.37 / 0.39

## Данные
- файлов: 6431, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 261 | 33 МБ | 2 |
| bn_book | 261 | 3 МБ | 27 |
| bnf_agg | 261 | 51 МБ | 2 |
| bnf_book | 118 | 557 МБ | 512722 |
| bnf_depth5 | 118 | 41 МБ | 512798 |
| bnf_liq | 227 | 149 КБ | 206 |
| bs_trade | 118 | 1 МБ | 512718 |
| by_book1 | 261 | 106 МБ | 2 |
| by_liq | 234 | 120 КБ | 384 |
| by_trade | 261 | 33 МБ | 2 |
| bys_book1 | 145 | 49 МБ | 2 |
| bys_trade | 145 | 19 МБ | 2 |
| cb_ticker | 261 | 31 МБ | 2 |
| clock | 261 | 201 КБ | 6 |
| clock_pm | 261 | 201 КБ | 26 |
| events | 250 | 79 КБ | 516 |
| events_pm | 261 | 94 КБ | 166 |
| health_cex | 261 | 3 МБ | 10 |
| health_feeds | 261 | 9 МБ | 10 |
| health_pm | 261 | 3 МБ | 6 |
| kr_trade | 118 | 3 МБ | 512718 |
| ok_trade | 260 | 44 МБ | 2 |
| pm_depth | 261 | 52 МБ | 2 |
| pm_rtt | 261 | 2 МБ | 4 |
| pm_top | 261 | 105 МБ | 2 |
| pm_trades | 261 | 75 МБ | 2 |
| rtds | 261 | 17 МБ | 2 |
| windows | 261 | 537 КБ | 74 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 34, всего 283
- Polymarket CLOB: TCP 5, TLS 37, всего 113
- Polymarket gamma: TCP 5, TLS 36, всего 46

## Последние строки журнала записи
```
08:13:01 [pm] T-118.9s Up 0.97/0.98 Down 0.02/0.03 ptb=82535.3 | CLOB 3089 сообщ., задержка p50/p90=38.7/75.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792397581077 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.2/2.6 мс
08:13:08 [cex] Binance 11 сд. задержка p50/p90=144.4/145.2 мс | Coinbase 5 задержка p50=76.5 мс | смещение часов +19.8 мс | lag loop p99/max=2.1/2.1 мс
08:13:08 [cex] binance_futures 54 сд. p50=293.3 мс | bybit 74 сд. p50=112.1 мс | bybit_book 145 сд. p50=110.8 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 88 сд. p50=111.8 мс | okx 34 сд. p50=158.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:13:11 [pm] T-108.9s Up 0.98/0.99 Down 0.01/0.02 ptb=82535.3 | CLOB 2299 сообщ., задержка p50/p90=38.2/39.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792397591080 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.1/2.5 мс
08:13:18 [cex] Binance 13 сд. задержка p50/p90=144.3/145.2 мс | Coinbase 5 задержка p50=77.3 мс | смещение часов +19.8 мс | lag loop p99/max=2.0/2.1 мс
08:13:18 [cex] binance_futures 51 сд. p50=293.2 мс | bybit 35 сд. p50=112.6 мс | bybit_book 104 сд. p50=110.8 мс | bybit_spot 4 сд. p50=113.9 мс | bybit_spot_book 124 сд. p50=111.8 мс | okx 61 сд. p50=158.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:13:21 [pm] T- 98.9s Up 0.98/0.99 Down 0.01/0.02 ptb=82535.3 | CLOB 1913 сообщ., задержка p50/p90=38.4/40.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792397601081 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.1/2.1 мс
08:13:28 [cex] Binance 38 сд. задержка p50/p90=144.5/145.4 мс | Coinbase 38 задержка p50=77.4 мс | смещение часов +19.8 мс | lag loop p99/max=2.2/2.3 мс
08:13:28 [cex] binance_futures 80 сд. p50=149.3 мс | bybit 99 сд. p50=114.9 мс | bybit_book 137 сд. p50=110.7 мс | bybit_spot 110 сд. p50=114.2 мс | bybit_spot_book 267 сд. p50=111.7 мс | okx 100 сд. p50=159.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:13:31 [pm] T- 88.9s Up 0.99/n/a Down n/a/0.01 ptb=82535.3 | CLOB 1698 сообщ., задержка p50/p90=38.2/40.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792397611082 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.9/2.1 мс
08:13:38 [cex] Binance 18 сд. задержка p50/p90=144.3/144.9 мс | Coinbase 39 задержка p50=79.5 мс | смещение часов +19.8 мс | lag loop p99/max=2.1/2.3 мс
08:13:38 [cex] binance_futures 94 сд. p50=152.9 мс | bybit 186 сд. p50=112.6 мс | bybit_book 161 сд. p50=110.8 мс | bybit_spot 237 сд. p50=114.6 мс | bybit_spot_book 154 сд. p50=111.7 мс | okx 82 сд. p50=158.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:13:41 [pm] T- 78.9s Up 0.99/n/a Down n/a/0.01 ptb=82535.3 | CLOB 1113 сообщ., задержка p50/p90=38.4/41.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792397621083 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.1/2.1 мс
08:13:48 [cex] Binance 20 сд. задержка p50/p90=144.2/145.3 мс | Coinbase 17 задержка p50=79.1 мс | смещение часов +18.9 мс | lag loop p99/max=2.1/2.9 мс
08:13:48 [cex] binance_futures 76 сд. p50=156.0 мс | bybit 180 сд. p50=115.4 мс | bybit_book 118 сд. p50=110.0 мс | bybit_spot 122 сд. p50=113.6 мс | bybit_spot_book 161 сд. p50=111.2 мс | okx 49 сд. p50=157.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
