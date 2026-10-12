# Состояние сервера записи

Время (UTC): 2026-10-12 14:12:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 6 hours, 48 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         775         759           2         579        1130
Swap:           2047         105        1942
```
- нагрузка CPU (1/5/15 мин): 0.58 / 0.57 / 0.67

## Данные
- файлов: 2537, всего 695 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 99 | 11 МБ | 0 |
| bn_book | 99 | 952 КБ | 0 |
| bnf_agg | 99 | 17 МБ | 0 |
| bnf_book | 99 | 458 МБ | 0 |
| bnf_depth5 | 99 | 34 МБ | 0 |
| bnf_liq | 86 | 50 КБ | 97 |
| bs_trade | 99 | 1 МБ | 0 |
| by_book1 | 99 | 35 МБ | 0 |
| by_liq | 82 | 43 КБ | 99 |
| by_trade | 99 | 11 МБ | 0 |
| cb_ticker | 99 | 10 МБ | 0 |
| clock | 99 | 75 КБ | 15 |
| clock_pm | 99 | 75 КБ | 31 |
| events | 92 | 31 КБ | 9535 |
| events_pm | 99 | 38 КБ | 309 |
| health_cex | 99 | 1 МБ | 4 |
| health_feeds | 99 | 4 МБ | 4 |
| health_pm | 99 | 1 МБ | 4 |
| kr_trade | 99 | 3 МБ | 0 |
| ok_trade | 99 | 15 МБ | 0 |
| pm_depth | 99 | 19 МБ | 0 |
| pm_rtt | 99 | 658 КБ | 0 |
| pm_top | 99 | 38 МБ | 0 |
| pm_trades | 99 | 28 МБ | 0 |
| rtds | 99 | 6 МБ | 0 |
| windows | 99 | 202 КБ | 204 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 44, всего 293
- Polymarket CLOB: TCP 5, TLS 45, всего 87
- Polymarket gamma: TCP 5, TLS 43, всего 55

## Последние строки журнала записи
```
14:11:43 [pm] T-196.9s Up 0.59/0.60 Down 0.40/0.41 ptb=82914.4 | CLOB 7463 сообщ., задержка p50/p90=305.4/357.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791814303081 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.3 мс | lag loop p99/max=2.0/2.7 мс
14:11:43 [cex] Binance 240 сд. задержка p50/p90=150.7/153.8 мс | Coinbase 62 задержка p50=87.0 мс | смещение часов +23.7 мс | lag loop p99/max=5.0/6.9 мс
14:11:43 [cex] binance_futures 342 сд. p50=171.3 мс | bybit 267 сд. p50=118.7 мс | okx 334 сд. p50=158.5 мс | binance_futures_book 7010 сд. p50=149.2 мс | binance_futures_depth 97 сд. p50=148.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 425 сд. p50=115.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 62 сд. p50=65.9 мс | bitstamp 6 сд. p50=54.2 мс
14:11:53 [pm] T-186.9s Up 0.48/0.49 Down 0.51/0.52 ptb=82914.4 | CLOB 10894 сообщ., задержка p50/p90=44.4/72.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791814313082 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.3 мс | lag loop p99/max=2.8/6.4 мс
14:11:53 [cex] Binance 147 сд. задержка p50/p90=148.9/155.2 мс | Coinbase 46 задержка p50=85.6 мс | смещение часов +23.7 мс | lag loop p99/max=2.2/4.2 мс
14:11:53 [cex] binance_futures 181 сд. p50=166.9 мс | bybit 182 сд. p50=117.1 мс | okx 283 сд. p50=158.8 мс | binance_futures_book 5294 сд. p50=148.0 мс | binance_futures_depth 98 сд. p50=147.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 388 сд. p50=115.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 32 сд. p50=60.6 мс | bitstamp 2 сд. p50=61.5 мс
14:12:03 [pm] T-176.9s Up 0.45/0.46 Down 0.54/0.55 ptb=82914.4 | CLOB 7604 сообщ., задержка p50/p90=210.9/334.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791814323083 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.6 мс | lag loop p99/max=4.5/7.1 мс
14:12:03 [cex] Binance 86 сд. задержка p50/p90=149.2/160.9 мс | Coinbase 108 задержка p50=106.9 мс | смещение часов +23.7 мс | lag loop p99/max=8.3/10.0 мс
14:12:03 [cex] binance_futures 99 сд. p50=200.3 мс | bybit 137 сд. p50=117.9 мс | okx 76 сд. p50=157.6 мс | binance_futures_book 3554 сд. p50=153.1 мс | binance_futures_depth 97 сд. p50=147.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 315 сд. p50=115.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 20 сд. p50=63.1 мс | bitstamp 4 сд. p50=51.4 мс
14:12:13 [pm] T-166.9s Up 0.42/0.43 Down 0.57/0.58 ptb=82914.4 | CLOB 9849 сообщ., задержка p50/p90=59.0/220.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791814333084 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.6 мс | lag loop p99/max=2.3/4.1 мс
14:12:13 [cex] Binance 69 сд. задержка p50/p90=148.5/149.8 мс | Coinbase 67 задержка p50=85.2 мс | смещение часов +21.1 мс | lag loop p99/max=2.0/3.7 мс
14:12:13 [cex] binance_futures 87 сд. p50=239.9 мс | bybit 230 сд. p50=117.4 мс | okx 178 сд. p50=157.9 мс | binance_futures_book 3716 сд. p50=148.5 мс | binance_futures_depth 96 сд. p50=148.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 303 сд. p50=115.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 16 сд. p50=48.4 мс | bitstamp 3 сд. p50=50.8 мс
14:12:23 [pm] T-156.9s Up 0.28/0.29 Down 0.71/0.72 ptb=82914.4 | CLOB 8724 сообщ., задержка p50/p90=75.7/254.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791814343085 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.6 мс | lag loop p99/max=1.9/2.1 мс
14:12:23 [cex] Binance 201 сд. задержка p50/p90=146.8/151.2 мс | Coinbase 50 задержка p50=83.0 мс | смещение часов +21.1 мс | lag loop p99/max=3.5/7.6 мс
14:12:23 [cex] binance_futures 228 сд. p50=164.9 мс | bybit 326 сд. p50=115.3 мс | okx 212 сд. p50=157.0 мс | binance_futures_book 7779 сд. p50=145.7 мс | binance_futures_depth 97 сд. p50=145.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 343 сд. p50=113.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 32 сд. p50=69.6 мс | bitstamp 5 сд. p50=56.5 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
