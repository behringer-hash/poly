# Состояние сервера записи

Время (UTC): 2026-10-31 06:16:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 2 days, 22 hours, 52 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         527        1194           1         371        1378
Swap:           2047         339        1708
```
- нагрузка CPU (1/5/15 мин): 0.20 / 0.21 / 0.23

## Данные
- файлов: 5854, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 37 МБ | 0 |
| bn_book | 242 | 3 МБ | 10 |
| bnf_agg | 242 | 52 МБ | 0 |
| bnf_book | 114 | 791 МБ | 0 |
| bnf_liq | 212 | 151 КБ | 3216 |
| by_book1 | 242 | 114 МБ | 0 |
| by_liq | 226 | 118 КБ | 3178 |
| by_trade | 242 | 35 МБ | 0 |
| bys_book1 | 242 | 84 МБ | 0 |
| bys_trade | 242 | 35 МБ | 0 |
| cb_ticker | 242 | 33 МБ | 0 |
| clock | 242 | 187 КБ | 59 |
| clock_pm | 242 | 187 КБ | 36 |
| events | 223 | 71 КБ | 155 |
| events_pm | 240 | 86 КБ | 3206 |
| health_cex | 242 | 3 МБ | 8 |
| health_feeds | 242 | 8 МБ | 8 |
| health_pm | 242 | 3 МБ | 8 |
| ok_trade | 242 | 46 МБ | 0 |
| pm_depth | 242 | 50 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 6 |
| pm_top | 242 | 99 МБ | 2 |
| pm_trades | 241 | 70 МБ | 2 |
| rtds | 242 | 16 МБ | 2 |
| windows | 242 | 498 КБ | 104 |

Дни с данными: 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 288
- Polymarket CLOB: TCP 5, TLS 39, всего 85
- Polymarket gamma: TCP 3, TLS 36, всего 42

## Последние строки журнала записи
```
06:15:39 [cex] Binance 16 сд. задержка p50/p90=146.5/146.7 мс | Coinbase 40 задержка p50=90.9 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.3 мс
06:15:39 [cex] binance_futures 16 сд. p50=295.6 мс | bybit 5 сд. p50=114.9 мс | bybit_book 44 сд. p50=113.0 мс | bybit_spot 2 сд. p50=114.6 мс | bybit_spot_book 37 сд. p50=112.8 мс | okx 8 сд. p50=153.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 577 сд. p50=146.7 мс
06:15:39 [pm] T-260.5s Up 0.65/0.66 Down 0.34/0.35 ptb=77170.4 | CLOB 3484 сообщ., задержка p50/p90=39.7/40.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793427339521 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.0 мс | lag loop p99/max=1.9/2.2 мс
06:15:49 [cex] Binance 20 сд. задержка p50/p90=146.6/147.7 мс | Coinbase 44 задержка p50=90.9 мс | смещение часов +21.6 мс | lag loop p99/max=2.0/2.1 мс
06:15:49 [cex] binance_futures 19 сд. p50=295.6 мс | bybit 14 сд. p50=114.6 мс | bybit_book 61 сд. p50=112.8 мс | bybit_spot 5 сд. p50=115.4 мс | bybit_spot_book 37 сд. p50=113.0 мс | okx 12 сд. p50=153.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 634 сд. p50=146.7 мс
06:15:49 [pm] T-250.5s Up 0.65/0.66 Down 0.34/0.35 ptb=77170.4 | CLOB 3844 сообщ., задержка p50/p90=41.5/82.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793427349522 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.0 мс | lag loop p99/max=2.0/2.1 мс
06:15:59 [cex] Binance 20 сд. задержка p50/p90=146.6/147.5 мс | Coinbase 42 задержка p50=91.9 мс | смещение часов +21.6 мс | lag loop p99/max=2.2/2.2 мс
06:15:59 [cex] binance_futures 16 сд. p50=295.4 мс | bybit 4 сд. p50=114.8 мс | bybit_book 74 сд. p50=112.8 мс | bybit_spot 53 сд. p50=116.3 мс | bybit_spot_book 45 сд. p50=112.8 мс | okx 15 сд. p50=153.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 453 сд. p50=146.7 мс
06:15:59 [pm] T-240.5s Up 0.66/0.67 Down 0.33/0.34 ptb=77170.4 | CLOB 4162 сообщ., задержка p50/p90=41.0/42.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793427359523 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.0 мс | lag loop p99/max=1.8/2.2 мс
06:16:09 [cex] Binance 55 сд. задержка p50/p90=147.0/147.5 мс | Coinbase 30 задержка p50=90.8 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.2 мс
06:16:09 [cex] binance_futures 22 сд. p50=295.4 мс | bybit 1 сд. p50=114.7 мс | bybit_book 64 сд. p50=112.9 мс | bybit_spot 2 сд. p50=115.3 мс | bybit_spot_book 11 сд. p50=113.1 мс | okx 7 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 596 сд. p50=146.7 мс
06:16:09 [pm] T-230.5s Up 0.69/0.70 Down 0.30/0.31 ptb=77170.4 | CLOB 5218 сообщ., задержка p50/p90=41.4/49.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793427369524 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.9 мс | lag loop p99/max=1.5/4.9 мс
06:16:19 [cex] Binance 36 сд. задержка p50/p90=146.6/147.6 мс | Coinbase 25 задержка p50=91.3 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.2 мс
06:16:19 [cex] binance_futures 18 сд. p50=295.8 мс | bybit 4 сд. p50=114.5 мс | bybit_book 61 сд. p50=113.0 мс | bybit_spot 2 сд. p50=115.2 мс | bybit_spot_book 96 сд. p50=112.9 мс | okx 7 сд. p50=153.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 447 сд. p50=146.7 мс
06:16:19 [pm] T-220.5s Up 0.70/0.71 Down 0.29/0.30 ptb=77170.4 | CLOB 3205 сообщ., задержка p50/p90=40.9/41.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793427379525 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.9 мс | lag loop p99/max=1.7/1.8 мс
```

Представлено версией кода: 8047248; python 3.12.3
