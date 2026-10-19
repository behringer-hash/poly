# Состояние сервера записи

Время (UTC): 2026-10-19 23:38:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 5 days, 16 hours, 14 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         790         254           1        1044        1115
Swap:           2047         250        1797
```
- нагрузка CPU (1/5/15 мин): 0.48 / 0.47 / 0.37

## Данные
- файлов: 6787, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 276 | 35 МБ | 0 |
| bn_book | 276 | 3 МБ | 2 |
| bnf_agg | 276 | 54 МБ | 0 |
| bnf_book | 118 | 557 МБ | 568182 |
| bnf_depth5 | 118 | 41 МБ | 568258 |
| bnf_liq | 239 | 156 КБ | 897 |
| bs_trade | 118 | 1 МБ | 568178 |
| by_book1 | 276 | 114 МБ | 0 |
| by_liq | 248 | 125 КБ | 4714 |
| by_trade | 276 | 35 МБ | 0 |
| bys_book1 | 160 | 55 МБ | 0 |
| bys_trade | 160 | 21 МБ | 0 |
| cb_ticker | 276 | 34 МБ | 0 |
| clock | 276 | 213 КБ | 59 |
| clock_pm | 276 | 214 КБ | 18 |
| events | 265 | 84 КБ | 285 |
| events_pm | 276 | 99 КБ | 306 |
| health_cex | 276 | 3 МБ | 2 |
| health_feeds | 276 | 9 МБ | 2 |
| health_pm | 276 | 3 МБ | 8 |
| kr_trade | 118 | 3 МБ | 568178 |
| ok_trade | 275 | 47 МБ | 0 |
| pm_depth | 276 | 55 МБ | -0 |
| pm_rtt | 276 | 2 МБ | 2 |
| pm_top | 276 | 113 МБ | -0 |
| pm_trades | 276 | 79 МБ | -0 |
| rtds | 276 | 18 МБ | -0 |
| windows | 276 | 570 КБ | 64 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 44, всего 293
- Polymarket CLOB: TCP 5, TLS 42, всего 82
- Polymarket gamma: TCP 6, TLS 41, всего 52

## Последние строки журнала записи
```
23:37:19 [pm] T-160.7s Up 0.62/0.63 Down 0.37/0.38 ptb=81965.2 | CLOB 6919 сообщ., задержка p50/p90=39.9/41.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792453039335 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=3.6/4.5 мс
23:37:24 [cex] Binance 12 сд. задержка p50/p90=144.2/144.5 мс | Coinbase 27 задержка p50=76.1 мс | смещение часов +19.7 мс | lag loop p99/max=2.1/2.2 мс
23:37:24 [cex] binance_futures 12 сд. p50=294.0 мс | bybit 7 сд. p50=113.6 мс | bybit_book 187 сд. p50=111.8 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 19 сд. p50=111.7 мс | okx 11 сд. p50=157.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:37:29 [pm] T-150.7s Up 0.65/0.66 Down 0.34/0.35 ptb=81965.2 | CLOB 4365 сообщ., задержка p50/p90=39.8/41.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792453049337 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=1.8/2.0 мс
23:37:34 [cex] Binance 6 сд. задержка p50/p90=144.2/145.2 мс | Coinbase 52 задержка p50=76.4 мс | смещение часов +19.7 мс | lag loop p99/max=2.2/2.3 мс
23:37:34 [cex] binance_futures 12 сд. p50=294.1 мс | bybit 1 сд. p50=113.7 мс | bybit_book 142 сд. p50=111.8 мс | bybit_spot 2 сд. p50=113.9 мс | bybit_spot_book 12 сд. p50=111.5 мс | okx 7 сд. p50=157.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:37:39 [pm] T-140.7s Up 0.69/0.70 Down 0.30/0.31 ptb=81965.2 | CLOB 3906 сообщ., задержка p50/p90=40.0/41.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792453059339 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.1/2.2 мс
23:37:44 [cex] Binance 9 сд. задержка p50/p90=144.3/144.5 мс | Coinbase 31 задержка p50=76.6 мс | смещение часов +19.7 мс | lag loop p99/max=2.1/2.1 мс
23:37:44 [cex] binance_futures 14 сд. p50=294.0 мс | bybit 1 сд. p50=113.0 мс | bybit_book 191 сд. p50=111.8 мс | bybit_spot 4 сд. p50=114.0 мс | bybit_spot_book 197 сд. p50=111.6 мс | okx 47 сд. p50=157.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:37:49 [pm] T-130.7s Up 0.83/0.87 Down 0.13/0.17 ptb=81965.2 | CLOB 4937 сообщ., задержка p50/p90=40.2/41.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792453069340 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=1.8/4.3 мс
23:37:54 [cex] Binance 29 сд. задержка p50/p90=144.5/145.3 мс | Coinbase 27 задержка p50=76.0 мс | смещение часов +19.7 мс | lag loop p99/max=2.2/2.5 мс
23:37:54 [cex] binance_futures 5 сд. p50=294.1 мс | bybit 8 сд. p50=113.7 мс | bybit_book 86 сд. p50=111.8 мс | bybit_spot 18 сд. p50=114.0 мс | bybit_spot_book 223 сд. p50=111.6 мс | okx 19 сд. p50=157.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:37:59 [pm] T-120.7s Up 0.93/0.94 Down 0.06/0.07 ptb=81965.2 | CLOB 5747 сообщ., задержка p50/p90=40.9/44.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792453079342 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=1.4/1.6 мс
23:38:04 [cex] Binance 122 сд. задержка p50/p90=145.0/148.2 мс | Coinbase 39 задержка p50=76.6 мс | смещение часов +19.7 мс | lag loop p99/max=2.2/4.4 мс
23:38:04 [cex] binance_futures 119 сд. p50=146.0 мс | bybit 115 сд. p50=113.9 мс | bybit_book 212 сд. p50=111.8 мс | bybit_spot 82 сд. p50=114.0 мс | bybit_spot_book 311 сд. p50=111.6 мс | okx 123 сд. p50=159.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
