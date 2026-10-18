# Состояние сервера записи

Время (UTC): 2026-10-18 09:27:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 2 hours, 4 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         868         476           2         849        1037
Swap:           2047         236        1811
```
- нагрузка CPU (1/5/15 мин): 0.34 / 0.25 / 0.25

## Данные
- файлов: 5880, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 238 | 31 МБ | 1 |
| bn_book | 238 | 3 МБ | 20 |
| bnf_agg | 238 | 47 МБ | 1 |
| bnf_book | 118 | 557 МБ | 430772 |
| bnf_depth5 | 118 | 41 МБ | 430848 |
| bnf_liq | 205 | 136 КБ | 849 |
| bs_trade | 118 | 1 МБ | 430768 |
| by_book1 | 238 | 98 МБ | 1 |
| by_liq | 211 | 111 КБ | 851 |
| by_trade | 238 | 31 МБ | 1 |
| bys_book1 | 122 | 42 МБ | 1 |
| bys_trade | 122 | 17 МБ | 3 |
| cb_ticker | 238 | 29 МБ | 1 |
| clock | 238 | 184 КБ | 60 |
| clock_pm | 238 | 184 КБ | 29 |
| events | 227 | 73 КБ | 240 |
| events_pm | 238 | 86 КБ | 1175 |
| health_cex | 238 | 2 МБ | 9 |
| health_feeds | 238 | 8 МБ | 9 |
| health_pm | 238 | 3 МБ | 9 |
| kr_trade | 118 | 3 МБ | 430768 |
| ok_trade | 237 | 41 МБ | 1 |
| pm_depth | 238 | 47 МБ | 1 |
| pm_rtt | 238 | 2 МБ | 3 |
| pm_top | 238 | 97 МБ | 1 |
| pm_trades | 238 | 69 МБ | 1 |
| rtds | 238 | 15 МБ | 1 |
| windows | 238 | 491 КБ | 143 |

Дни с данными: 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 9, TLS 47, всего 295
- Polymarket CLOB: TCP 5, TLS 42, всего 88
- Polymarket gamma: TCP 5, TLS 47, всего 61

## Последние строки журнала записи
```
09:27:18 [cex] Binance 139 сд. задержка p50/p90=147.9/152.7 мс | Coinbase 39 задержка p50=77.7 мс | смещение часов +20.3 мс | lag loop p99/max=2.1/2.1 мс
09:27:18 [cex] binance_futures 133 сд. p50=147.0 мс | bybit 80 сд. p50=129.9 мс | bybit_book 138 сд. p50=111.8 мс | bybit_spot 150 сд. p50=116.7 мс | bybit_spot_book 64 сд. p50=111.9 мс | okx 159 сд. p50=157.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:27:18 [pm] T-161.3s Up 0.90/0.91 Down 0.09/0.10 ptb=81801.2 | CLOB 5562 сообщ., задержка p50/p90=38.8/40.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792315638694 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.0/10.1 мс
09:27:28 [cex] Binance 167 сд. задержка p50/p90=145.0/145.9 мс | Coinbase 28 задержка p50=77.8 мс | смещение часов +20.3 мс | lag loop p99/max=2.2/2.3 мс
09:27:28 [cex] binance_futures 193 сд. p50=147.0 мс | bybit 172 сд. p50=116.4 мс | bybit_book 269 сд. p50=111.9 мс | bybit_spot 264 сд. p50=115.0 мс | bybit_spot_book 277 сд. p50=111.9 мс | okx 265 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:27:28 [pm] T-151.3s Up 0.96/0.97 Down 0.03/0.04 ptb=81801.2 | CLOB 3833 сообщ., задержка p50/p90=39.3/53.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792315648695 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.9/2.0 мс
09:27:38 [cex] Binance 121 сд. задержка p50/p90=144.5/145.4 мс | Coinbase 34 задержка p50=77.5 мс | смещение часов +20.3 мс | lag loop p99/max=2.2/2.4 мс
09:27:38 [cex] binance_futures 72 сд. p50=185.6 мс | bybit 277 сд. p50=115.9 мс | bybit_book 306 сд. p50=111.8 мс | bybit_spot 113 сд. p50=114.5 мс | bybit_spot_book 297 сд. p50=111.9 мс | okx 102 сд. p50=154.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:27:38 [pm] T-141.3s Up 0.97/0.98 Down 0.02/0.03 ptb=81801.2 | CLOB 2664 сообщ., задержка p50/p90=38.1/40.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792315658696 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.0/2.1 мс
09:27:48 [cex] Binance 37 сд. задержка p50/p90=144.0/144.9 мс | Coinbase 33 задержка p50=95.1 мс | смещение часов +20.3 мс | lag loop p99/max=2.0/2.4 мс
09:27:48 [cex] binance_futures 79 сд. p50=146.7 мс | bybit 101 сд. p50=117.9 мс | bybit_book 133 сд. p50=111.9 мс | bybit_spot 171 сд. p50=117.4 мс | bybit_spot_book 185 сд. p50=111.9 мс | okx 49 сд. p50=154.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:27:48 [pm] T-131.3s Up 0.96/0.97 Down 0.03/0.04 ptb=81801.2 | CLOB 2803 сообщ., задержка p50/p90=38.7/48.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792315668697 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.2/2.9 мс
09:27:58 [cex] Binance 24 сд. задержка p50/p90=144.1/144.3 мс | Coinbase 9 задержка p50=76.7 мс | смещение часов +20.3 мс | lag loop p99/max=2.1/2.1 мс
09:27:58 [cex] binance_futures 24 сд. p50=293.5 мс | bybit 80 сд. p50=114.1 мс | bybit_book 88 сд. p50=111.8 мс | bybit_spot 6 сд. p50=114.1 мс | bybit_spot_book 30 сд. p50=111.9 мс | okx 22 сд. p50=153.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:27:58 [pm] T-121.3s Up 0.96/0.97 Down 0.03/0.04 ptb=81801.2 | CLOB 2577 сообщ., задержка p50/p90=38.5/42.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792315678699 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.0/2.2 мс
```

Представлено версией кода: b24b4e3; python 3.12.3
