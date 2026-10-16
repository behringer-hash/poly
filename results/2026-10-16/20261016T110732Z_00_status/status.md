# Состояние сервера записи

Время (UTC): 2026-10-16 11:07:33

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 3 hours, 43 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         468        1408           2         229        1437
Swap:           2047         256        1791
```
- нагрузка CPU (1/5/15 мин): 1.29 / 1.08 / 0.66

## Данные
- файлов: 4795, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 192 | 26 МБ | 0 |
| bn_book | 192 | 2 МБ | 2 |
| bnf_agg | 192 | 39 МБ | 0 |
| bnf_book | 118 | 557 МБ | 263947 |
| bnf_depth5 | 118 | 41 МБ | 264023 |
| bnf_liq | 172 | 118 КБ | 1436 |
| bs_trade | 118 | 1 МБ | 263943 |
| by_book1 | 192 | 82 МБ | 0 |
| by_liq | 171 | 95 КБ | 379 |
| by_trade | 192 | 26 МБ | 0 |
| bys_book1 | 76 | 29 МБ | 0 |
| bys_trade | 76 | 12 МБ | 2 |
| cb_ticker | 192 | 24 МБ | 0 |
| clock | 192 | 147 КБ | 57 |
| clock_pm | 192 | 148 КБ | 5 |
| events | 181 | 58 КБ | 215 |
| events_pm | 192 | 69 КБ | 102 |
| health_cex | 192 | 2 МБ | 2 |
| health_feeds | 192 | 7 МБ | 2 |
| health_pm | 192 | 2 МБ | 9 |
| kr_trade | 118 | 3 МБ | 263943 |
| ok_trade | 191 | 35 МБ | 0 |
| pm_depth | 192 | 38 МБ | 1 |
| pm_rtt | 192 | 1 МБ | 5 |
| pm_top | 192 | 78 МБ | 1 |
| pm_trades | 192 | 57 МБ | 1 |
| rtds | 192 | 12 МБ | 1 |
| windows | 192 | 394 КБ | 238 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 37, всего 286
- Polymarket CLOB: TCP 5, TLS 37, всего 81
- Polymarket gamma: TCP 5, TLS 36, всего 48

## Последние строки журнала записи
```
11:06:43 [pm] T-196.0s Up 0.44/0.46 Down 0.54/0.56 ptb=82182.8 | CLOB 12175 сообщ., задержка p50/p90=67.0/94.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792148803981 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=4.8/16.6 мс
11:06:48 [cex] Binance 266 сд. задержка p50/p90=159.0/159.9 мс | Coinbase 76 задержка p50=94.8 мс | смещение часов +34.5 мс | lag loop p99/max=2.7/8.7 мс
11:06:48 [cex] binance_futures 93 сд. p50=271.4 мс | bybit 81 сд. p50=129.4 мс | bybit_book 190 сд. p50=126.7 мс | bybit_spot 209 сд. p50=130.0 мс | bybit_spot_book 168 сд. p50=126.3 мс | okx 48 сд. p50=168.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
11:06:53 [pm] T-186.0s Up 0.60/0.61 Down 0.39/0.40 ptb=82182.8 | CLOB 10857 сообщ., задержка p50/p90=73.1/153.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792148813982 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=8.5/11.5 мс
11:06:58 [cex] Binance 320 сд. задержка p50/p90=159.1/161.3 мс | Coinbase 120 задержка p50=109.5 мс | смещение часов +34.5 мс | lag loop p99/max=2.2/2.5 мс
11:06:58 [cex] binance_futures 233 сд. p50=165.2 мс | bybit 141 сд. p50=129.4 мс | bybit_book 217 сд. p50=126.7 мс | bybit_spot 166 сд. p50=129.7 мс | bybit_spot_book 181 сд. p50=126.3 мс | okx 127 сд. p50=169.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
11:07:03 [pm] T-176.0s Up 0.73/0.74 Down 0.26/0.27 ptb=82182.8 | CLOB 12520 сообщ., задержка p50/p90=59.9/101.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792148823984 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=3.5/10.7 мс
11:07:08 [cex] Binance 481 сд. задержка p50/p90=159.2/160.7 мс | Coinbase 71 задержка p50=94.9 мс | смещение часов +34.5 мс | lag loop p99/max=2.8/103.8 мс
11:07:08 [cex] binance_futures 393 сд. p50=161.3 мс | bybit 1082 сд. p50=138.9 мс | bybit_book 328 сд. p50=126.7 мс | bybit_spot 319 сд. p50=129.8 мс | bybit_spot_book 348 сд. p50=126.3 мс | okx 488 сд. p50=168.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
11:07:13 [pm] T-166.0s Up 0.73/0.74 Down 0.26/0.27 ptb=82182.8 | CLOB 13171 сообщ., задержка p50/p90=51.5/55.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792148833985 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=5.0/5.2 мс
11:07:18 [cex] Binance 283 сд. задержка p50/p90=178.7/1080.6 мс | Coinbase 108 задержка p50=274.9 мс | смещение часов +34.5 мс | lag loop p99/max=30.5/908.2 мс
11:07:18 [cex] binance_futures 662 сд. p50=309.3 мс | bybit 570 сд. p50=133.8 мс | bybit_book 339 сд. p50=126.8 мс | bybit_spot 535 сд. p50=129.9 мс | bybit_spot_book 302 сд. p50=126.4 мс | okx 217 сд. p50=168.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
11:07:23 [pm] T-156.0s Up 0.52/0.53 Down 0.47/0.48 ptb=82182.8 | CLOB 11700 сообщ., задержка p50/p90=51.2/57.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792148843987 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=17.5/391.5 мс
11:07:28 [cex] Binance 172 сд. задержка p50/p90=174.4/193.9 мс | Coinbase 68 задержка p50=95.2 мс | смещение часов +34.5 мс | lag loop p99/max=9.2/37.1 мс
11:07:28 [cex] binance_futures 537 сд. p50=165.1 мс | bybit 493 сд. p50=132.9 мс | bybit_book 349 сд. p50=126.7 мс | bybit_spot 226 сд. p50=129.1 мс | bybit_spot_book 234 сд. p50=126.3 мс | okx 476 сд. p50=169.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 7b2a292; python 3.12.3
