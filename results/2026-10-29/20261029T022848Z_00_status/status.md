# Состояние сервера записи

Время (UTC): 2026-10-29 02:28:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 19 hours, 4 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 45 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         613         589           1         879        1292
Swap:           2047         304        1743
```
- нагрузка CPU (1/5/15 мин): 0.17 / 0.20 / 0.25

## Данные
- файлов: 5811, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 36 МБ | 1 |
| bn_book | 242 | 3 МБ | 1 |
| bnf_agg | 242 | 52 МБ | 1 |
| bnf_book | 62 | 462 МБ | 0 |
| bnf_liq | 211 | 139 КБ | 28 |
| by_book1 | 242 | 111 МБ | 1 |
| by_liq | 225 | 102 КБ | 748 |
| by_trade | 242 | 35 МБ | 1 |
| bys_book1 | 242 | 85 МБ | 1 |
| bys_trade | 242 | 34 МБ | 1 |
| cb_ticker | 242 | 32 МБ | 1 |
| clock | 242 | 188 КБ | 46 |
| clock_pm | 242 | 188 КБ | 20 |
| events | 231 | 73 КБ | 148 |
| events_pm | 242 | 83 КБ | 1075 |
| health_cex | 242 | 2 МБ | 1 |
| health_feeds | 242 | 7 МБ | 1 |
| health_pm | 242 | 3 МБ | 6 |
| ok_trade | 242 | 45 МБ | 1 |
| pm_depth | 242 | 50 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 6 |
| pm_top | 242 | 101 МБ | 2 |
| pm_trades | 242 | 71 МБ | 4 |
| rtds | 242 | 16 МБ | 2 |
| windows | 242 | 499 КБ | 224 |

Дни с данными: 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 7, TLS 38, всего 288
- Polymarket CLOB: TCP 6, TLS 40, всего 80
- Polymarket gamma: TCP 3, TLS 34, всего 41

## Последние строки журнала записи
```
02:28:01 [pm] T-118.3s Up 0.02/0.03 Down 0.97/0.98 ptb=79934.0 | CLOB 4388 сообщ., задержка p50/p90=37.6/44.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793240881659 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.5/1.6 мс
02:28:05 [cex] Binance 189 сд. задержка p50/p90=144.4/148.0 мс | Coinbase 70 задержка p50=95.2 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/3.3 мс
02:28:05 [cex] binance_futures 154 сд. p50=150.1 мс | bybit 151 сд. p50=113.9 мс | bybit_book 352 сд. p50=111.8 мс | bybit_spot 156 сд. p50=115.2 мс | bybit_spot_book 150 сд. p50=111.5 мс | okx 174 сд. p50=158.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3609 сд. p50=144.6 мс
02:28:11 [pm] T-108.3s Up 0.01/0.02 Down 0.98/0.99 ptb=79934.0 | CLOB 2495 сообщ., задержка p50/p90=37.3/44.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793240891660 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.8/2.1 мс
02:28:15 [cex] Binance 99 сд. задержка p50/p90=143.3/149.8 мс | Coinbase 69 задержка p50=91.3 мс | смещение часов +19.1 мс | lag loop p99/max=2.0/2.1 мс
02:28:15 [cex] binance_futures 167 сд. p50=149.3 мс | bybit 144 сд. p50=112.1 мс | bybit_book 276 сд. p50=110.7 мс | bybit_spot 45 сд. p50=114.9 мс | bybit_spot_book 114 сд. p50=110.5 мс | okx 150 сд. p50=156.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2225 сд. p50=143.8 мс
02:28:21 [pm] T- 98.3s Up n/a/0.01 Down 0.99/n/a ptb=79934.0 | CLOB 1509 сообщ., задержка p50/p90=38.1/49.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793240901661 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.0/2.2 мс
02:28:25 [cex] Binance 102 сд. задержка p50/p90=149.7/150.2 мс | Coinbase 45 задержка p50=91.5 мс | смещение часов +19.1 мс | lag loop p99/max=2.2/3.4 мс
02:28:25 [cex] binance_futures 89 сд. p50=227.0 мс | bybit 85 сд. p50=112.2 мс | bybit_book 299 сд. p50=110.7 мс | bybit_spot 63 сд. p50=112.8 мс | bybit_spot_book 126 сд. p50=110.6 мс | okx 101 сд. p50=156.5 мс | binance_liq 1 сд. p50=1148.8 мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2761 сд. p50=143.9 мс
02:28:31 [pm] T- 88.3s Up n/a/0.01 Down 0.99/n/a ptb=79934.0 | CLOB 2080 сообщ., задержка p50/p90=38.3/48.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793240911662 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.9 мс | lag loop p99/max=1.8/2.0 мс
02:28:35 [cex] Binance 185 сд. задержка p50/p90=144.0/150.1 мс | Coinbase 81 задержка p50=94.5 мс | смещение часов +19.1 мс | lag loop p99/max=3.5/6.5 мс
02:28:35 [cex] binance_futures 293 сд. p50=149.3 мс | bybit 243 сд. p50=114.2 мс | bybit_book 271 сд. p50=110.7 мс | bybit_spot 289 сд. p50=117.3 мс | bybit_spot_book 161 сд. p50=110.7 мс | okx 226 сд. p50=159.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 10945 сд. p50=143.9 мс
02:28:41 [pm] T- 78.3s Up n/a/0.01 Down 0.99/n/a ptb=79934.0 | CLOB 1761 сообщ., задержка p50/p90=37.8/39.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793240921664 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.9 мс | lag loop p99/max=2.0/2.1 мс
02:28:45 [cex] Binance 108 сд. задержка p50/p90=144.0/146.3 мс | Coinbase 69 задержка p50=91.6 мс | смещение часов +19.1 мс | lag loop p99/max=2.4/11.5 мс
02:28:45 [cex] binance_futures 133 сд. p50=149.5 мс | bybit 90 сд. p50=113.0 мс | bybit_book 196 сд. p50=110.7 мс | bybit_spot 267 сд. p50=116.4 мс | bybit_spot_book 123 сд. p50=110.6 мс | okx 141 сд. p50=157.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3702 сд. p50=145.7 мс
```

Представлено версией кода: 65c4468; python 3.12.3
