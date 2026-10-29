# Состояние сервера записи

Время (UTC): 2026-10-29 09:42:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 2 hours, 18 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         527         701           1         848        1378
Swap:           2047         316        1731
```
- нагрузка CPU (1/5/15 мин): 0.09 / 0.24 / 0.25

## Данные
- файлов: 5816, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 36 МБ | 2 |
| bn_book | 242 | 3 МБ | 26 |
| bnf_agg | 242 | 51 МБ | 2 |
| bnf_book | 69 | 459 МБ | 0 |
| bnf_liq | 211 | 139 КБ | 417 |
| by_book1 | 242 | 113 МБ | 2 |
| by_liq | 224 | 100 КБ | 1824 |
| by_trade | 242 | 34 МБ | 2 |
| bys_book1 | 242 | 84 МБ | 2 |
| bys_trade | 242 | 33 МБ | 2 |
| cb_ticker | 242 | 32 МБ | 2 |
| clock | 242 | 188 КБ | 56 |
| clock_pm | 242 | 188 КБ | 29 |
| events | 231 | 73 КБ | 1209 |
| events_pm | 241 | 85 КБ | 403 |
| health_cex | 242 | 3 МБ | 8 |
| health_feeds | 242 | 8 МБ | 8 |
| health_pm | 242 | 3 МБ | 3 |
| ok_trade | 242 | 44 МБ | 2 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 5 |
| pm_top | 242 | 102 МБ | 1 |
| pm_trades | 242 | 72 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 500 КБ | 54 |

Дни с данными: 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 38, всего 289
- Polymarket CLOB: TCP 9, TLS 43, всего 91
- Polymarket gamma: TCP 6, TLS 39, всего 48

## Последние строки журнала записи
```
09:41:39 [cex] Binance 106 сд. задержка p50/p90=145.1/145.9 мс | Coinbase 55 задержка p50=109.7 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/2.3 мс
09:41:39 [cex] binance_futures 105 сд. p50=154.0 мс | bybit 57 сд. p50=114.0 мс | bybit_book 159 сд. p50=111.6 мс | bybit_spot 215 сд. p50=114.6 мс | bybit_spot_book 92 сд. p50=111.9 мс | okx 63 сд. p50=149.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2001 сд. p50=147.5 мс
09:41:45 [pm] T-194.5s Up 0.93/0.94 Down 0.06/0.07 ptb=80026.9 | CLOB 4193 сообщ., задержка p50/p90=43.8/118.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793266905474 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.1/2.2 мс
09:41:49 [cex] Binance 97 сд. задержка p50/p90=145.1/146.0 мс | Coinbase 13 задержка p50=304.8 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/3.2 мс
09:41:49 [cex] binance_futures 75 сд. p50=268.7 мс | bybit 59 сд. p50=113.9 мс | bybit_book 224 сд. p50=111.8 мс | bybit_spot 152 сд. p50=115.2 мс | bybit_spot_book 113 сд. p50=113.0 мс | okx 50 сд. p50=148.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3599 сд. p50=145.6 мс
09:41:55 [pm] T-184.5s Up 0.92/0.93 Down 0.07/0.08 ptb=80026.9 | CLOB 3418 сообщ., задержка p50/p90=39.7/42.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793266915475 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.8/1.9 мс
09:41:59 [cex] Binance 89 сд. задержка p50/p90=145.1/146.1 мс | Coinbase 3 задержка p50=91.1 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/2.2 мс
09:41:59 [cex] binance_futures 55 сд. p50=293.8 мс | bybit 20 сд. p50=113.9 мс | bybit_book 158 сд. p50=111.8 мс | bybit_spot 7 сд. p50=114.5 мс | bybit_spot_book 59 сд. p50=112.9 мс | okx 19 сд. p50=147.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1925 сд. p50=145.3 мс
09:42:05 [pm] T-174.5s Up 0.88/0.89 Down 0.11/0.12 ptb=80026.9 | CLOB 6054 сообщ., задержка p50/p90=40.5/91.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793266925477 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=3.5/6.3 мс
09:42:09 [cex] Binance 221 сд. задержка p50/p90=145.4/151.7 мс | Coinbase 40 задержка p50=95.0 мс | смещение часов +20.5 мс | lag loop p99/max=11.0/11.4 мс
09:42:09 [cex] binance_futures 146 сд. p50=153.7 мс | bybit 148 сд. p50=116.2 мс | bybit_book 274 сд. p50=111.9 мс | bybit_spot 128 сд. p50=119.2 мс | bybit_spot_book 94 сд. p50=113.1 мс | okx 93 сд. p50=150.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5059 сд. p50=145.7 мс
09:42:15 [pm] T-164.5s Up 0.91/0.92 Down 0.08/0.09 ptb=80026.9 | CLOB 4399 сообщ., задержка p50/p90=40.0/74.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793266935478 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.9/1.9 мс
09:42:19 [cex] Binance 100 сд. задержка p50/p90=145.1/145.9 мс | Coinbase 3 задержка p50=93.1 мс | смещение часов +20.5 мс | lag loop p99/max=2.2/2.2 мс
09:42:19 [cex] binance_futures 47 сд. p50=293.8 мс | bybit 5 сд. p50=113.9 мс | bybit_book 96 сд. p50=111.9 мс | bybit_spot 5 сд. p50=114.5 мс | bybit_spot_book 23 сд. p50=113.1 мс | okx 4 сд. p50=147.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 464 сд. p50=145.3 мс
09:42:25 [pm] T-154.5s Up 0.92/0.93 Down 0.07/0.08 ptb=80026.9 | CLOB 2392 сообщ., задержка p50/p90=40.5/113.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793266945479 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.0/2.1 мс
```

Представлено версией кода: c4da76d; python 3.12.3
