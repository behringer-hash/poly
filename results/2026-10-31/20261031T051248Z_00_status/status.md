# Состояние сервера записи

Время (UTC): 2026-10-31 05:12:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 2 days, 21 hours, 48 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         671         896           1         523        1234
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.50 / 0.40 / 0.32

## Данные
- файлов: 5855, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 37 МБ | 2 |
| bn_book | 242 | 3 МБ | 18 |
| bnf_agg | 242 | 52 МБ | 2 |
| bnf_book | 113 | 777 МБ | 0 |
| bnf_liq | 212 | 151 КБ | 295 |
| by_book1 | 242 | 114 МБ | 2 |
| by_liq | 225 | 118 КБ | 2285 |
| by_trade | 242 | 35 МБ | 4 |
| bys_book1 | 242 | 83 МБ | 2 |
| bys_trade | 242 | 34 МБ | 2 |
| cb_ticker | 242 | 33 МБ | 2 |
| clock | 242 | 187 КБ | 62 |
| clock_pm | 242 | 187 КБ | 38 |
| events | 224 | 71 КБ | 554 |
| events_pm | 242 | 86 КБ | 84 |
| health_cex | 242 | 3 МБ | 8 |
| health_feeds | 242 | 8 МБ | 8 |
| health_pm | 242 | 3 МБ | 9 |
| ok_trade | 242 | 46 МБ | 4 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 3 |
| pm_top | 242 | 99 МБ | 1 |
| pm_trades | 241 | 70 МБ | 1 |
| rtds | 242 | 15 МБ | 1 |
| windows | 242 | 498 КБ | 254 |

Дни с данными: 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 34, всего 284
- Polymarket CLOB: TCP 9, TLS 44, всего 89
- Polymarket gamma: TCP 3, TLS 34, всего 41

## Последние строки журнала записи
```
05:12:08 [cex] Binance 46 сд. задержка p50/p90=143.4/144.4 мс | Coinbase 36 задержка p50=88.5 мс | смещение часов +18.4 мс | lag loop p99/max=2.2/4.7 мс
05:12:08 [cex] binance_futures 64 сд. p50=148.1 мс | bybit 44 сд. p50=112.2 мс | bybit_book 118 сд. p50=110.3 мс | bybit_spot 145 сд. p50=113.1 мс | bybit_spot_book 50 сд. p50=110.3 мс | okx 10 сд. p50=150.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1886 сд. p50=145.0 мс
05:12:08 [pm] T-171.0s Up 0.21/0.22 Down 0.78/0.79 ptb=77175.9 | CLOB 7175 сообщ., задержка p50/p90=44.3/150.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793423528980 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=2.2/3.3 мс
05:12:18 [cex] Binance 30 сд. задержка p50/p90=143.3/144.3 мс | Coinbase 29 задержка p50=88.0 мс | смещение часов +18.4 мс | lag loop p99/max=2.1/2.1 мс
05:12:18 [cex] binance_futures 22 сд. p50=292.2 мс | bybit 1 сд. p50=111.5 мс | bybit_book 94 сд. p50=110.3 мс | bybit_spot 21 сд. p50=113.1 мс | bybit_spot_book 47 сд. p50=110.0 мс | okx 12 сд. p50=149.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 657 сд. p50=143.4 мс
05:12:18 [pm] T-161.0s Up 0.25/0.26 Down 0.74/0.75 ptb=77175.9 | CLOB 4414 сообщ., задержка p50/p90=41.0/42.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793423538982 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=1.4/1.9 мс
05:12:28 [cex] Binance 128 сд. задержка p50/p90=144.3/150.1 мс | Coinbase 58 задержка p50=89.2 мс | смещение часов +18.4 мс | lag loop p99/max=3.2/4.3 мс
05:12:28 [cex] binance_futures 168 сд. p50=154.0 мс | bybit 154 сд. p50=112.6 мс | bybit_book 197 сд. p50=110.3 мс | bybit_spot 202 сд. p50=113.1 мс | bybit_spot_book 145 сд. p50=110.3 мс | okx 178 сд. p50=151.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5608 сд. p50=143.9 мс
05:12:28 [pm] T-151.0s Up 0.11/0.12 Down 0.88/0.89 ptb=77175.9 | CLOB 4164 сообщ., задержка p50/p90=51.1/170.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793423548983 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=1.9/2.2 мс
05:12:38 [cex] Binance 19 сд. задержка p50/p90=143.4/144.4 мс | Coinbase 39 задержка p50=87.6 мс | смещение часов +18.4 мс | lag loop p99/max=2.2/2.3 мс
05:12:38 [cex] binance_futures 34 сд. p50=292.1 мс | bybit 13 сд. p50=112.2 мс | bybit_book 73 сд. p50=110.3 мс | bybit_spot 2 сд. p50=112.7 мс | bybit_spot_book 22 сд. p50=110.4 мс | okx 9 сд. p50=149.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 911 сд. p50=143.5 мс
05:12:38 [pm] T-141.0s Up 0.06/0.07 Down 0.93/0.94 ptb=77175.9 | CLOB 4192 сообщ., задержка p50/p90=41.2/43.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793423558984 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=1.6/1.6 мс
05:12:48 [cex] Binance 39 сд. задержка p50/p90=143.5/144.5 мс | Coinbase 33 задержка p50=87.8 мс | смещение часов +18.8 мс | lag loop p99/max=2.1/2.2 мс
05:12:48 [cex] binance_futures 23 сд. p50=292.1 мс | bybit 13 сд. p50=111.6 мс | bybit_book 49 сд. p50=110.3 мс | bybit_spot 5 сд. p50=112.3 мс | bybit_spot_book 28 сд. p50=110.1 мс | okx 14 сд. p50=150.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 711 сд. p50=143.5 мс
05:12:48 [pm] T-131.0s Up 0.05/0.06 Down 0.94/0.95 ptb=77175.9 | CLOB 2125 сообщ., задержка p50/p90=41.2/47.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793423568986 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=1.9/2.1 мс
```

Представлено версией кода: c9404c3; python 3.12.3
