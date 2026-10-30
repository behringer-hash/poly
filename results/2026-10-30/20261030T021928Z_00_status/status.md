# Состояние сервера записи

Время (UTC): 2026-10-30 02:19:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 18 hours, 55 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         639         871           1         575        1266
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.22 / 0.24 / 0.34

## Данные
- файлов: 5829, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 38 МБ | 0 |
| bn_book | 242 | 3 МБ | 0 |
| bnf_agg | 242 | 55 МБ | 0 |
| bnf_book | 86 | 633 МБ | 0 |
| bnf_liq | 211 | 148 КБ | 47 |
| by_book1 | 242 | 115 МБ | 0 |
| by_liq | 225 | 133 КБ | 173 |
| by_trade | 242 | 37 МБ | 0 |
| bys_book1 | 242 | 87 МБ | 0 |
| bys_trade | 242 | 35 МБ | 0 |
| cb_ticker | 242 | 34 МБ | 0 |
| clock | 242 | 187 КБ | 59 |
| clock_pm | 242 | 187 КБ | 31 |
| events | 227 | 72 КБ | 9638 |
| events_pm | 241 | 84 КБ | 850 |
| health_cex | 242 | 3 МБ | 4 |
| health_feeds | 242 | 8 МБ | 4 |
| health_pm | 242 | 3 МБ | 3 |
| ok_trade | 242 | 48 МБ | 0 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 3 |
| pm_top | 242 | 100 МБ | 1 |
| pm_trades | 241 | 71 МБ | 9 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 499 КБ | 54 |

Дни с данными: 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 71, всего 321
- Polymarket CLOB: TCP 7, TLS 43, всего 80
- Polymarket gamma: TCP 4, TLS 38, всего 45

## Последние строки журнала записи
```
02:18:42 [cex] Binance 434 сд. задержка p50/p90=144.9/148.0 мс | Coinbase 164 задержка p50=102.6 мс | смещение часов +18.1 мс | lag loop p99/max=3.1/5.1 мс
02:18:42 [cex] binance_futures 529 сд. p50=145.8 мс | bybit 681 сд. p50=112.0 мс | bybit_book 576 сд. p50=109.4 мс | bybit_spot 302 сд. p50=113.4 мс | bybit_spot_book 282 сд. p50=110.6 мс | okx 649 сд. p50=267.8 мс | binance_liq 2 сд. p50=1148.0 мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 10309 сд. p50=142.5 мс
02:18:44 [pm] T- 75.2s Up 0.97/0.98 Down 0.02/0.03 ptb=76846.9 | CLOB 3868 сообщ., задержка p50/p90=41.5/53.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793326724782 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.6 мс | lag loop p99/max=2.1/2.5 мс
02:18:52 [cex] Binance 161 сд. задержка p50/p90=143.8/147.2 мс | Coinbase 92 задержка p50=90.8 мс | смещение часов +18.1 мс | lag loop p99/max=4.2/5.5 мс
02:18:52 [cex] binance_futures 169 сд. p50=151.3 мс | bybit 326 сд. p50=111.3 мс | bybit_book 459 сд. p50=109.3 мс | bybit_spot 173 сд. p50=112.8 мс | bybit_spot_book 153 сд. p50=110.5 мс | okx 110 сд. p50=155.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4563 сд. p50=142.3 мс
02:18:54 [pm] T- 65.2s Up 0.98/0.99 Down 0.01/0.02 ptb=76846.9 | CLOB 2358 сообщ., задержка p50/p90=41.5/55.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793326734784 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.6 мс | lag loop p99/max=2.1/2.1 мс
02:19:02 [cex] Binance 101 сд. задержка p50/p90=143.3/149.0 мс | Coinbase 68 задержка p50=89.8 мс | смещение часов +18.1 мс | lag loop p99/max=2.7/3.3 мс
02:19:02 [cex] binance_futures 90 сд. p50=247.5 мс | bybit 266 сд. p50=111.2 мс | bybit_book 441 сд. p50=109.4 мс | bybit_spot 148 сд. p50=111.9 мс | bybit_spot_book 136 сд. p50=109.8 мс | okx 56 сд. p50=154.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2491 сд. p50=142.4 мс
02:19:04 [pm] T- 55.2s Up 0.99/n/a Down n/a/0.01 ptb=76846.9 | CLOB 1553 сообщ., задержка p50/p90=40.5/57.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793326744785 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.6 мс | lag loop p99/max=2.1/2.2 мс
02:19:12 [cex] Binance 252 сд. задержка p50/p90=147.1/149.9 мс | Coinbase 127 задержка p50=96.7 мс | смещение часов +18.1 мс | lag loop p99/max=2.8/4.5 мс
02:19:12 [cex] binance_futures 453 сд. p50=145.6 мс | bybit 435 сд. p50=111.5 мс | bybit_book 459 сд. p50=109.4 мс | bybit_spot 282 сд. p50=115.0 мс | bybit_spot_book 191 сд. p50=110.0 мс | okx 364 сд. p50=159.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 10261 сд. p50=142.5 мс
02:19:14 [pm] T- 45.2s Up 0.99/n/a Down n/a/0.01 ptb=76846.9 | CLOB 1084 сообщ., задержка p50/p90=46.2/74.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793326754786 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.6 мс | lag loop p99/max=2.0/2.1 мс
02:19:22 [cex] Binance 96 сд. задержка p50/p90=143.5/145.0 мс | Coinbase 156 задержка p50=107.4 мс | смещение часов +18.1 мс | lag loop p99/max=4.8/5.1 мс
02:19:22 [cex] binance_futures 170 сд. p50=152.7 мс | bybit 260 сд. p50=111.3 мс | bybit_book 479 сд. p50=109.4 мс | bybit_spot 236 сд. p50=111.9 мс | bybit_spot_book 148 сд. p50=109.9 мс | okx 165 сд. p50=154.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 11118 сд. p50=142.6 мс
02:19:24 [pm] T- 35.2s Up 0.99/n/a Down n/a/0.01 ptb=76846.9 | CLOB 672 сообщ., задержка p50/p90=40.4/42.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793326764787 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.6 мс | lag loop p99/max=2.1/2.1 мс
```

Представлено версией кода: b8783c2; python 3.12.3
