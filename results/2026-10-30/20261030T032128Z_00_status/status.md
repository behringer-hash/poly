# Состояние сервера записи

Время (UTC): 2026-10-30 03:21:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 19 hours, 57 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         632         880           1         576        1273
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.44 / 0.30 / 0.30

## Данные
- файлов: 5830, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 37 МБ | 2 |
| bn_book | 242 | 3 МБ | 2 |
| bnf_agg | 242 | 53 МБ | 2 |
| bnf_book | 87 | 616 МБ | 0 |
| bnf_liq | 211 | 143 КБ | 366 |
| by_book1 | 242 | 113 МБ | 2 |
| by_liq | 225 | 118 КБ | 724 |
| by_trade | 242 | 35 МБ | 2 |
| bys_book1 | 242 | 85 МБ | 2 |
| bys_trade | 242 | 35 МБ | 4 |
| cb_ticker | 242 | 33 МБ | 2 |
| clock | 242 | 187 КБ | 28 |
| clock_pm | 242 | 188 КБ | 0 |
| events | 226 | 72 КБ | 13359 |
| events_pm | 242 | 85 КБ | 924 |
| health_cex | 242 | 3 МБ | 6 |
| health_feeds | 242 | 8 МБ | 6 |
| health_pm | 242 | 3 МБ | 2 |
| ok_trade | 242 | 46 МБ | 2 |
| pm_depth | 242 | 50 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 2 |
| pm_top | 242 | 100 МБ | 0 |
| pm_trades | 241 | 71 МБ | 0 |
| rtds | 242 | 16 МБ | 0 |
| windows | 242 | 499 КБ | 25 |

Дни с данными: 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 44, всего 293
- Polymarket CLOB: TCP 6, TLS 50, всего 92
- Polymarket gamma: TCP 5, TLS 59, всего 65

## Последние строки журнала записи
```
03:20:42 [cex] Binance 102 сд. задержка p50/p90=143.8/149.5 мс | Coinbase 235 задержка p50=90.1 мс | смещение часов +18.5 мс | lag loop p99/max=2.0/2.1 мс
03:20:42 [cex] binance_futures 90 сд. p50=149.2 мс | bybit 54 сд. p50=112.0 мс | bybit_book 205 сд. p50=109.7 мс | bybit_spot 55 сд. p50=111.8 мс | bybit_spot_book 62 сд. p50=110.7 мс | okx 121 сд. p50=155.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4547 сд. p50=142.6 мс
03:20:45 [pm] T-254.7s Up 0.58/0.59 Down 0.41/0.42 ptb=77191.6 | CLOB 7517 сообщ., задержка p50/p90=45.2/87.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793330445308 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.8 мс | lag loop p99/max=1.1/1.2 мс
03:20:52 [cex] Binance 198 сд. задержка p50/p90=145.6/149.8 мс | Coinbase 144 задержка p50=92.1 мс | смещение часов +18.5 мс | lag loop p99/max=2.7/5.7 мс
03:20:52 [cex] binance_futures 164 сд. p50=147.4 мс | bybit 142 сд. p50=114.5 мс | bybit_book 200 сд. p50=109.7 мс | bybit_spot 285 сд. p50=112.7 мс | bybit_spot_book 141 сд. p50=110.6 мс | okx 208 сд. p50=156.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3986 сд. p50=143.0 мс
03:20:55 [pm] T-244.7s Up 0.52/0.53 Down 0.47/0.48 ptb=77191.6 | CLOB 10411 сообщ., задержка p50/p90=44.8/47.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793330455309 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.8 мс | lag loop p99/max=2.0/6.0 мс
03:21:02 [cex] Binance 148 сд. задержка p50/p90=147.3/147.9 мс | Coinbase 89 задержка p50=90.4 мс | смещение часов +20.2 мс | lag loop p99/max=2.2/6.3 мс
03:21:02 [cex] binance_futures 140 сд. p50=149.7 мс | bybit 85 сд. p50=113.3 мс | bybit_book 248 сд. p50=110.0 мс | bybit_spot 123 сд. p50=114.0 мс | bybit_spot_book 112 сд. p50=111.0 мс | okx 63 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3821 сд. p50=144.7 мс
03:21:05 [pm] T-234.7s Up 0.46/0.47 Down 0.53/0.54 ptb=77191.6 | CLOB 9640 сообщ., задержка p50/p90=45.1/47.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793330465311 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.9 мс | lag loop p99/max=1.8/4.6 мс
03:21:12 [cex] Binance 135 сд. задержка p50/p90=145.9/148.7 мс | Coinbase 114 задержка p50=93.0 мс | смещение часов +20.2 мс | lag loop p99/max=2.0/2.1 мс
03:21:12 [cex] binance_futures 115 сд. p50=152.4 мс | bybit 51 сд. p50=113.4 мс | bybit_book 180 сд. p50=111.4 мс | bybit_spot 210 сд. p50=113.8 мс | bybit_spot_book 103 сд. p50=112.4 мс | okx 169 сд. p50=157.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5766 сд. p50=144.3 мс
03:21:15 [pm] T-224.7s Up 0.46/0.48 Down 0.52/0.54 ptb=77191.6 | CLOB 10140 сообщ., задержка p50/p90=45.8/53.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793330475312 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.9 мс | lag loop p99/max=1.3/2.3 мс
03:21:22 [cex] Binance 84 сд. задержка p50/p90=146.1/148.4 мс | Coinbase 65 задержка p50=91.3 мс | смещение часов +20.2 мс | lag loop p99/max=2.2/10.2 мс
03:21:22 [cex] binance_futures 126 сд. p50=156.8 мс | bybit 78 сд. p50=113.9 мс | bybit_book 228 сд. p50=111.4 мс | bybit_spot 241 сд. p50=114.1 мс | bybit_spot_book 150 сд. p50=112.4 мс | okx 108 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 7418 сд. p50=144.7 мс
03:21:25 [pm] T-214.7s Up 0.60/0.61 Down 0.39/0.40 ptb=77191.6 | CLOB 9847 сообщ., задержка p50/p90=53.0/85.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793330485314 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.9 мс | lag loop p99/max=2.8/4.2 мс
```

Представлено версией кода: b8783c2; python 3.12.3
