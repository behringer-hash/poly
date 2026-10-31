# Состояние сервера записи

Время (UTC): 2026-10-31 03:07:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 2 days, 19 hours, 43 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         664         728           1         698        1241
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.11 / 0.24 / 0.25

## Данные
- файлов: 5852, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 37 МБ | 2 |
| bn_book | 242 | 3 МБ | 6 |
| bnf_agg | 242 | 52 МБ | 2 |
| bnf_book | 111 | 768 МБ | 1 |
| bnf_liq | 211 | 151 КБ | 718 |
| by_book1 | 242 | 114 МБ | 2 |
| by_liq | 225 | 119 КБ | 1790 |
| by_trade | 242 | 35 МБ | 2 |
| bys_book1 | 242 | 84 МБ | 2 |
| bys_trade | 242 | 34 МБ | 6 |
| cb_ticker | 242 | 33 МБ | 2 |
| clock | 242 | 187 КБ | 24 |
| clock_pm | 242 | 187 КБ | 0 |
| events | 224 | 71 КБ | 105 |
| events_pm | 241 | 86 КБ | 284 |
| health_cex | 242 | 3 МБ | 10 |
| health_feeds | 242 | 8 МБ | 10 |
| health_pm | 242 | 3 МБ | 0 |
| ok_trade | 242 | 46 МБ | 2 |
| pm_depth | 242 | 49 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 2 |
| pm_top | 242 | 99 МБ | 0 |
| pm_trades | 241 | 70 МБ | 0 |
| rtds | 242 | 15 МБ | 0 |
| windows | 243 | 499 КБ | 155 |

Дни с данными: 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 41, всего 290
- Polymarket CLOB: TCP 5, TLS 40, всего 86
- Polymarket gamma: TCP 4, TLS 43, всего 50

## Последние строки журнала записи
```
03:06:27 [cex] Binance 24 сд. задержка p50/p90=143.6/144.5 мс | Coinbase 42 задержка p50=88.3 мс | смещение часов +19.3 мс | lag loop p99/max=2.2/2.2 мс
03:06:27 [cex] binance_futures 29 сд. p50=292.8 мс | bybit 4 сд. p50=112.4 мс | bybit_book 85 сд. p50=110.7 мс | bybit_spot 12 сд. p50=112.8 мс | bybit_spot_book 22 сд. p50=111.0 мс | okx 23 сд. p50=153.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1183 сд. p50=144.4 мс
03:06:27 [pm] T-212.1s Up 0.71/0.72 Down 0.28/0.29 ptb=77279.5 | CLOB 5450 сообщ., задержка p50/p90=41.8/43.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793415987922 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=1.4/2.0 мс
03:06:37 [cex] Binance 16 сд. задержка p50/p90=143.5/143.6 мс | Coinbase 28 задержка p50=88.0 мс | смещение часов +19.3 мс | lag loop p99/max=2.1/2.1 мс
03:06:37 [cex] binance_futures 23 сд. p50=292.8 мс | bybit 8 сд. p50=112.5 мс | bybit_book 37 сд. p50=110.7 мс | bybit_spot 3 сд. p50=112.8 мс | bybit_spot_book 17 сд. p50=110.7 мс | okx 12 сд. p50=153.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 364 сд. p50=144.3 мс
03:06:37 [pm] T-202.1s Up 0.71/0.72 Down 0.28/0.29 ptb=77279.5 | CLOB 4075 сообщ., задержка p50/p90=41.8/42.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793415997924 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.1 мс | lag loop p99/max=1.2/1.7 мс
03:06:47 [cex] Binance 25 сд. задержка p50/p90=143.5/144.5 мс | Coinbase 33 задержка p50=87.8 мс | смещение часов +18.9 мс | lag loop p99/max=1.9/2.1 мс
03:06:47 [cex] binance_futures 31 сд. p50=292.4 мс | bybit 10 сд. p50=112.4 мс | bybit_book 95 сд. p50=110.7 мс | bybit_spot 11 сд. p50=112.5 мс | bybit_spot_book 26 сд. p50=110.8 мс | okx 23 сд. p50=153.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 369 сд. p50=144.0 мс
03:06:47 [pm] T-192.1s Up 0.70/0.71 Down 0.29/0.30 ptb=77279.5 | CLOB 3146 сообщ., задержка p50/p90=41.8/42.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793416007925 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=1.9/2.0 мс
03:06:57 [cex] Binance 20 сд. задержка p50/p90=143.2/145.6 мс | Coinbase 53 задержка p50=88.5 мс | смещение часов +18.9 мс | lag loop p99/max=2.2/2.3 мс
03:06:57 [cex] binance_futures 56 сд. p50=144.4 мс | bybit 24 сд. p50=114.4 мс | bybit_book 75 сд. p50=110.3 мс | bybit_spot 150 сд. p50=113.3 мс | bybit_spot_book 32 сд. p50=110.7 мс | okx 35 сд. p50=153.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1607 сд. p50=144.0 мс
03:06:57 [pm] T-182.1s Up 0.65/0.66 Down 0.34/0.35 ptb=77279.5 | CLOB 5212 сообщ., задержка p50/p90=42.0/44.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793416017926 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=2.2/2.6 мс
03:07:07 [cex] Binance 203 сд. задержка p50/p90=144.8/151.9 мс | Coinbase 62 задержка p50=89.5 мс | смещение часов +18.9 мс | lag loop p99/max=8.1/8.7 мс
03:07:07 [cex] binance_futures 195 сд. p50=145.2 мс | bybit 150 сд. p50=113.6 мс | bybit_book 238 сд. p50=110.3 мс | bybit_spot 199 сд. p50=114.5 мс | bybit_spot_book 72 сд. p50=110.6 мс | okx 113 сд. p50=158.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3469 сд. p50=146.5 мс
03:07:07 [pm] T-172.1s Up 0.29/0.30 Down 0.70/0.71 ptb=77279.5 | CLOB 10437 сообщ., задержка p50/p90=42.1/135.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793416027928 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=2.4/16.8 мс
```

Представлено версией кода: fcaf736; python 3.12.3
