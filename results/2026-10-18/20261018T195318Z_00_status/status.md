# Состояние сервера записи

Время (UTC): 2026-10-18 19:53:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 12 hours, 29 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         475        1334           1         264        1430
Swap:           2047         254        1793
```
- нагрузка CPU (1/5/15 мин): 0.29 / 0.21 / 0.19

## Данные
- файлов: 6119, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 248 | 32 МБ | 0 |
| bn_book | 248 | 3 МБ | 7 |
| bnf_agg | 248 | 50 МБ | 0 |
| bnf_book | 118 | 557 МБ | 468292 |
| bnf_depth5 | 118 | 41 МБ | 468368 |
| bnf_liq | 214 | 147 КБ | 312 |
| bs_trade | 118 | 1 МБ | 468288 |
| by_book1 | 248 | 105 МБ | 0 |
| by_liq | 221 | 121 КБ | 331 |
| by_trade | 248 | 33 МБ | 0 |
| bys_book1 | 132 | 46 МБ | 0 |
| bys_trade | 132 | 19 МБ | 0 |
| cb_ticker | 248 | 30 МБ | 0 |
| clock | 248 | 192 КБ | 13 |
| clock_pm | 248 | 192 КБ | 38 |
| events | 237 | 77 КБ | 1662 |
| events_pm | 248 | 90 КБ | 142 |
| health_cex | 248 | 3 МБ | 4 |
| health_feeds | 248 | 8 МБ | 4 |
| health_pm | 248 | 3 МБ | 3 |
| kr_trade | 118 | 3 МБ | 468288 |
| ok_trade | 247 | 43 МБ | 0 |
| pm_depth | 248 | 50 МБ | 1 |
| pm_rtt | 248 | 2 МБ | 3 |
| pm_top | 248 | 102 МБ | 1 |
| pm_trades | 248 | 72 МБ | 1 |
| rtds | 248 | 16 МБ | 1 |
| windows | 248 | 514 КБ | 13 |

Дни с данными: 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 36, всего 287
- Polymarket CLOB: TCP 6, TLS 39, всего 85
- Polymarket gamma: TCP 5, TLS 37, всего 48

## Последние строки журнала записи
```
19:52:32 [cex] Binance 17 сд. задержка p50/p90=144.3/145.3 мс | Coinbase 61 задержка p50=77.9 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/2.2 мс
19:52:32 [cex] binance_futures 55 сд. p50=274.7 мс | bybit 91 сд. p50=114.5 мс | bybit_book 193 сд. p50=112.6 мс | bybit_spot 148 сд. p50=115.3 мс | bybit_spot_book 92 сд. p50=112.2 мс | okx 50 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:52:34 [pm] T-145.2s Up 0.06/0.07 Down 0.93/0.94 ptb=80888.1 | CLOB 2861 сообщ., задержка p50/p90=43.8/56.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792353154814 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=1.9/2.0 мс
19:52:42 [cex] Binance 63 сд. задержка p50/p90=144.4/145.4 мс | Coinbase 44 задержка p50=79.2 мс | смещение часов +20.5 мс | lag loop p99/max=2.2/2.2 мс
19:52:42 [cex] binance_futures 215 сд. p50=146.1 мс | bybit 148 сд. p50=115.0 мс | bybit_book 253 сд. p50=112.6 мс | bybit_spot 315 сд. p50=115.1 мс | bybit_spot_book 105 сд. p50=112.2 мс | okx 100 сд. p50=154.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:52:44 [pm] T-135.2s Up 0.06/0.07 Down 0.93/0.94 ptb=80888.1 | CLOB 3514 сообщ., задержка p50/p90=42.3/124.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792353164815 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=2.1/2.1 мс
19:52:52 [cex] Binance 18 сд. задержка p50/p90=144.3/144.6 мс | Coinbase 36 задержка p50=77.6 мс | смещение часов +20.5 мс | lag loop p99/max=2.2/2.2 мс
19:52:52 [cex] binance_futures 62 сд. p50=262.4 мс | bybit 39 сд. p50=114.7 мс | bybit_book 191 сд. p50=112.7 мс | bybit_spot 46 сд. p50=115.6 мс | bybit_spot_book 81 сд. p50=112.2 мс | okx 83 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:52:54 [pm] T-125.2s Up 0.02/0.03 Down 0.97/0.98 ptb=80888.1 | CLOB 3232 сообщ., задержка p50/p90=38.6/41.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792353174817 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.3 мс | lag loop p99/max=1.9/2.1 мс
19:53:02 [cex] Binance 16 сд. задержка p50/p90=144.3/145.3 мс | Coinbase 46 задержка p50=78.1 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/2.3 мс
19:53:02 [cex] binance_futures 31 сд. p50=294.0 мс | bybit 310 сд. p50=114.9 мс | bybit_book 204 сд. p50=112.6 мс | bybit_spot 61 сд. p50=115.3 мс | bybit_spot_book 74 сд. p50=112.2 мс | okx 23 сд. p50=154.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:53:04 [pm] T-115.2s Up 0.01/0.02 Down 0.98/0.99 ptb=80888.1 | CLOB 2244 сообщ., задержка p50/p90=40.4/54.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792353184818 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.3 мс | lag loop p99/max=2.1/2.7 мс
19:53:12 [cex] Binance 50 сд. задержка p50/p90=143.7/144.7 мс | Coinbase 50 задержка p50=76.6 мс | смещение часов +19.4 мс | lag loop p99/max=2.0/2.0 мс
19:53:12 [cex] binance_futures 121 сд. p50=145.5 мс | bybit 110 сд. p50=113.6 мс | bybit_book 199 сд. p50=111.6 мс | bybit_spot 148 сд. p50=114.8 мс | bybit_spot_book 97 сд. p50=111.4 мс | okx 51 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:53:14 [pm] T-105.2s Up 0.01/0.02 Down 0.98/0.99 ptb=80888.1 | CLOB 2953 сообщ., задержка p50/p90=39.1/99.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792353194820 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.3 мс | lag loop p99/max=2.2/2.2 мс
```

Представлено версией кода: 88f2465; python 3.12.3
