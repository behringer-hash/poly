# Состояние сервера записи

Время (UTC): 2026-10-18 15:38:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 8 hours, 14 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         536        1230           2         324        1369
Swap:           2047         244        1803
```
- нагрузка CPU (1/5/15 мин): 0.45 / 0.26 / 0.20

## Данные
- файлов: 6023, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 244 | 32 МБ | 2 |
| bn_book | 244 | 3 МБ | 2 |
| bnf_agg | 244 | 49 МБ | 2 |
| bnf_book | 118 | 557 МБ | 453002 |
| bnf_depth5 | 118 | 41 МБ | 453078 |
| bnf_liq | 210 | 138 КБ | 168 |
| bs_trade | 118 | 1 МБ | 452998 |
| by_book1 | 244 | 102 МБ | 2 |
| by_liq | 217 | 113 КБ | 411 |
| by_trade | 244 | 32 МБ | 2 |
| bys_book1 | 128 | 44 МБ | 2 |
| bys_trade | 128 | 18 МБ | 2 |
| cb_ticker | 244 | 30 МБ | 2 |
| clock | 244 | 189 КБ | 41 |
| clock_pm | 244 | 189 КБ | 4 |
| events | 233 | 75 КБ | 1445 |
| events_pm | 244 | 88 КБ | 952 |
| health_cex | 244 | 3 МБ | 6 |
| health_feeds | 244 | 8 МБ | 6 |
| health_pm | 244 | 3 МБ | 6 |
| kr_trade | 118 | 3 МБ | 452998 |
| ok_trade | 243 | 42 МБ | 2 |
| pm_depth | 244 | 49 МБ | 2 |
| pm_rtt | 244 | 2 МБ | -0 |
| pm_top | 244 | 100 МБ | -0 |
| pm_trades | 244 | 71 МБ | -0 |
| rtds | 244 | 16 МБ | -0 |
| windows | 244 | 504 КБ | 174 |

Дни с данными: 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 7, TLS 55, всего 306
- Polymarket CLOB: TCP 6, TLS 44, всего 90
- Polymarket gamma: TCP 5, TLS 43, всего 66

## Последние строки журнала записи
```
15:37:41 [cex] Binance 140 сд. задержка p50/p90=145.4/147.0 мс | Coinbase 76 задержка p50=81.3 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.1 мс
15:37:41 [cex] binance_futures 121 сд. p50=147.6 мс | bybit 233 сд. p50=119.8 мс | bybit_book 214 сд. p50=113.6 мс | bybit_spot 151 сд. p50=116.1 мс | bybit_spot_book 107 сд. p50=113.1 мс | okx 134 сд. p50=155.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:37:41 [pm] T-138.1s Up 0.25/0.26 Down 0.74/0.75 ptb=81058.3 | CLOB 8476 сообщ., задержка p50/p90=42.0/46.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792337861908 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=1.9/2.1 мс
15:37:51 [cex] Binance 83 сд. задержка p50/p90=145.3/145.8 мс | Coinbase 23 задержка p50=78.6 мс | смещение часов +20.6 мс | lag loop p99/max=2.2/2.3 мс
15:37:51 [cex] binance_futures 75 сд. p50=147.4 мс | bybit 147 сд. p50=115.4 мс | bybit_book 211 сд. p50=112.9 мс | bybit_spot 64 сд. p50=115.3 мс | bybit_spot_book 93 сд. p50=112.5 мс | okx 87 сд. p50=154.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:37:51 [pm] T-128.1s Up 0.12/0.13 Down 0.87/0.88 ptb=81058.3 | CLOB 7726 сообщ., задержка p50/p90=42.6/45.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792337871910 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=1.8/2.0 мс
15:38:01 [cex] Binance 17 сд. задержка p50/p90=144.3/145.3 мс | Coinbase 25 задержка p50=78.5 мс | смещение часов +20.6 мс | lag loop p99/max=2.1/2.2 мс
15:38:01 [cex] binance_futures 23 сд. p50=294.0 мс | bybit 205 сд. p50=115.1 мс | bybit_book 240 сд. p50=112.6 мс | bybit_spot 46 сд. p50=114.4 мс | bybit_spot_book 86 сд. p50=112.2 мс | okx 26 сд. p50=154.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:38:01 [pm] T-118.1s Up 0.19/0.20 Down 0.80/0.81 ptb=81058.3 | CLOB 6715 сообщ., задержка p50/p90=43.6/62.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792337881912 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=1.8/1.9 мс
15:38:11 [cex] Binance 61 сд. задержка p50/p90=144.4/146.8 мс | Coinbase 48 задержка p50=79.5 мс | смещение часов +20.6 мс | lag loop p99/max=2.1/2.2 мс
15:38:11 [cex] binance_futures 112 сд. p50=145.8 мс | bybit 63 сд. p50=114.7 мс | bybit_book 140 сд. p50=112.7 мс | bybit_spot 108 сд. p50=114.7 мс | bybit_spot_book 89 сд. p50=112.1 мс | okx 103 сд. p50=154.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:38:11 [pm] T-108.1s Up 0.13/0.14 Down 0.86/0.87 ptb=81058.3 | CLOB 7479 сообщ., задержка p50/p90=43.2/68.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792337891914 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=1.8/2.1 мс
15:38:21 [cex] Binance 121 сд. задержка p50/p90=144.7/144.9 мс | Coinbase 34 задержка p50=78.5 мс | смещение часов +20.6 мс | lag loop p99/max=2.2/2.2 мс
15:38:21 [cex] binance_futures 201 сд. p50=146.0 мс | bybit 222 сд. p50=115.4 мс | bybit_book 257 сд. p50=112.6 мс | bybit_spot 216 сд. p50=114.5 мс | bybit_spot_book 142 сд. p50=112.1 мс | okx 129 сд. p50=154.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:38:21 [pm] T- 98.1s Up 0.06/0.07 Down 0.93/0.94 ptb=81058.3 | CLOB 7346 сообщ., задержка p50/p90=42.1/49.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792337901915 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.1/2.1 мс
```

Представлено версией кода: eab44f6; python 3.12.3
