# Состояние сервера записи

Время (UTC): 2026-10-30 23:01:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 2 days, 15 hours, 37 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         677         632           1         784        1228
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.84 / 0.44 / 0.25

## Данные
- файлов: 5866, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 243 | 37 МБ | 1 |
| bn_book | 243 | 3 МБ | 5 |
| bnf_agg | 243 | 52 МБ | 1 |
| bnf_book | 107 | 745 МБ | 1 |
| bnf_liq | 211 | 149 КБ | 840 |
| by_book1 | 243 | 114 МБ | 1 |
| by_liq | 225 | 118 КБ | 1034 |
| by_trade | 243 | 35 МБ | 1 |
| bys_book1 | 243 | 84 МБ | 1 |
| bys_trade | 243 | 34 МБ | 1 |
| cb_ticker | 243 | 33 МБ | 1 |
| clock | 243 | 188 КБ | 19 |
| clock_pm | 243 | 187 КБ | 59 |
| events | 223 | 72 КБ | 110 |
| events_pm | 241 | 87 КБ | 144 |
| health_cex | 243 | 3 МБ | 3 |
| health_feeds | 243 | 8 МБ | 3 |
| health_pm | 243 | 3 МБ | 2 |
| ok_trade | 243 | 46 МБ | 1 |
| pm_depth | 243 | 49 МБ | 0 |
| pm_rtt | 243 | 2 МБ | 4 |
| pm_top | 243 | 99 МБ | 0 |
| pm_trades | 242 | 71 МБ | 0 |
| rtds | 243 | 15 МБ | 0 |
| windows | 243 | 499 КБ | 4 |

Дни с данными: 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 103, всего 356
- Polymarket CLOB: TCP 6, TLS 95, всего 145
- Polymarket gamma: TCP 7, TLS 129, всего 137

## Последние строки журнала записи
```
23:00:25 [cex] Binance 200 сд. задержка p50/p90=147.8/158.8 мс | Coinbase 66 задержка p50=90.7 мс | смещение часов +19.4 мс | lag loop p99/max=9.4/19.7 мс
23:00:25 [cex] binance_futures 189 сд. p50=158.2 мс | bybit 154 сд. p50=121.7 мс | bybit_book 291 сд. p50=111.2 мс | bybit_spot 155 сд. p50=123.7 мс | bybit_spot_book 90 сд. p50=111.1 мс | okx 192 сд. p50=161.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3296 сд. p50=144.7 мс
23:00:25 [pm] T-274.2s Up 0.39/0.40 Down 0.60/0.61 ptb=76818.2 | CLOB 6331 сообщ., задержка p50/p90=57.8/61.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793401225835 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.3/2.6 мс
23:00:35 [cex] Binance 90 сд. задержка p50/p90=147.9/155.9 мс | Coinbase 41 задержка p50=89.8 мс | смещение часов +19.4 мс | lag loop p99/max=12.1/15.8 мс
23:00:35 [cex] binance_futures 98 сд. p50=155.2 мс | bybit 68 сд. p50=118.3 мс | bybit_book 391 сд. p50=111.1 мс | bybit_spot 65 сд. p50=113.8 мс | bybit_spot_book 77 сд. p50=111.0 мс | okx 110 сд. p50=153.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3063 сд. p50=144.5 мс
23:00:35 [pm] T-264.2s Up 0.34/0.35 Down 0.65/0.66 ptb=76818.2 | CLOB 7186 сообщ., задержка p50/p90=57.6/59.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793401235836 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=3.6/11.6 мс
23:00:45 [cex] Binance 49 сд. задержка p50/p90=143.6/156.2 мс | Coinbase 52 задержка p50=90.1 мс | смещение часов +19.4 мс | lag loop p99/max=13.5/13.8 мс
23:00:45 [cex] binance_futures 49 сд. p50=252.5 мс | bybit 53 сд. p50=119.6 мс | bybit_book 381 сд. p50=111.1 мс | bybit_spot 68 сд. p50=114.2 мс | bybit_spot_book 57 сд. p50=111.0 мс | okx 127 сд. p50=150.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3461 сд. p50=144.0 мс
23:00:45 [pm] T-254.2s Up 0.28/0.29 Down 0.71/0.72 ptb=76818.2 | CLOB 6319 сообщ., задержка p50/p90=57.8/60.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793401245838 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.5/1.9 мс
23:00:55 [cex] Binance 34 сд. задержка p50/p90=150.9/160.1 мс | Coinbase 46 задержка p50=105.2 мс | смещение часов +35.6 мс | lag loop p99/max=2.7/2.8 мс
23:00:55 [cex] binance_futures 36 сд. p50=293.2 мс | bybit 22 сд. p50=115.2 мс | bybit_book 224 сд. p50=127.0 мс | bybit_spot 24 сд. p50=126.8 мс | bybit_spot_book 41 сд. p50=111.3 мс | okx 95 сд. p50=155.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3517 сд. p50=160.0 мс
23:00:55 [pm] T-244.2s Up 0.29/0.30 Down 0.70/0.71 ptb=76818.2 | CLOB 7751 сообщ., задержка p50/p90=57.6/58.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793401255840 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.9 мс | lag loop p99/max=1.9/4.5 мс
23:01:05 [cex] Binance 25 сд. задержка p50/p90=159.9/166.8 мс | Coinbase 54 задержка p50=105.9 мс | смещение часов +35.6 мс | lag loop p99/max=2.3/2.6 мс
23:01:05 [cex] binance_futures 41 сд. p50=280.3 мс | bybit 27 сд. p50=128.7 мс | bybit_book 243 сд. p50=127.3 мс | bybit_spot 51 сд. p50=143.1 мс | bybit_spot_book 43 сд. p50=127.2 мс | okx 50 сд. p50=166.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1319 сд. p50=160.2 мс
23:01:05 [pm] T-234.2s Up 0.27/0.28 Down 0.72/0.73 ptb=76818.2 | CLOB 5731 сообщ., задержка p50/p90=57.6/59.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793401265841 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.9 мс | lag loop p99/max=1.9/2.1 мс
```

Представлено версией кода: fcaf736; python 3.12.3
