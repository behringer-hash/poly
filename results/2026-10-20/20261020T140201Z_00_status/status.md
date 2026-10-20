# Состояние сервера записи

Время (UTC): 2026-10-20 14:02:01

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 6 hours, 38 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         814         267           1        1008        1091
Swap:           2047         250        1797
```
- нагрузка CPU (1/5/15 мин): 0.77 / 0.72 / 0.60

## Данные
- файлов: 7144, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 291 | 37 МБ | 1 |
| bn_book | 291 | 4 МБ | 1 |
| bnf_agg | 291 | 57 МБ | 1 |
| bnf_book | 118 | 557 МБ | 620016 |
| bnf_depth5 | 118 | 41 МБ | 620092 |
| bnf_liq | 254 | 164 КБ | 1 |
| bs_trade | 118 | 1 МБ | 620012 |
| by_book1 | 291 | 119 МБ | 1 |
| by_liq | 263 | 132 КБ | 3 |
| by_trade | 291 | 37 МБ | 1 |
| bys_book1 | 175 | 58 МБ | 1 |
| bys_trade | 175 | 23 МБ | 1 |
| cb_ticker | 291 | 35 МБ | 1 |
| clock | 291 | 224 КБ | 33 |
| clock_pm | 291 | 224 КБ | 4 |
| events | 279 | 89 КБ | 2959 |
| events_pm | 290 | 105 КБ | 237 |
| health_cex | 291 | 3 МБ | 1 |
| health_feeds | 291 | 9 МБ | 1 |
| health_pm | 291 | 3 МБ | 4 |
| kr_trade | 118 | 3 МБ | 620012 |
| ok_trade | 290 | 49 МБ | 1 |
| pm_depth | 291 | 57 МБ | 2 |
| pm_rtt | 291 | 2 МБ | 6 |
| pm_top | 291 | 117 МБ | 2 |
| pm_trades | 291 | 83 МБ | 2 |
| rtds | 291 | 18 МБ | 2 |
| windows | 290 | 601 КБ | 177 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 7, TLS 75, всего 337
- Polymarket CLOB: TCP 4, TLS 68, всего 119
- Polymarket gamma: TCP 4, TLS 67, всего 80

## Последние строки журнала записи
```
14:01:17 [pm] T-222.5s Up 0.76/0.77 Down 0.23/0.24 ptb=82013.6 | CLOB 12795 сообщ., задержка p50/p90=44.6/73.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792504877493 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=1.9/3.3 мс
14:01:21 [cex] Binance 342 сд. задержка p50/p90=179.4/182.4 мс | Coinbase 73 задержка p50=106.6 мс | смещение часов +45.9 мс | lag loop p99/max=2.2/3.2 мс
14:01:21 [cex] binance_futures 777 сд. p50=174.8 мс | bybit 1373 сд. p50=140.5 мс | bybit_book 579 сд. p50=137.8 мс | bybit_spot 414 сд. p50=148.4 мс | bybit_spot_book 397 сд. p50=137.3 мс | okx 1046 сд. p50=173.8 мс | binance_liq 5 сд. p50=1172.0 мс | bybit_liq 1 сд. p50=333.3 мс
14:01:27 [pm] T-212.5s Up 0.76/0.77 Down 0.23/0.24 ptb=82013.6 | CLOB 11274 сообщ., задержка p50/p90=44.2/100.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792504887495 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=3.3/5.1 мс
14:01:31 [cex] Binance 163 сд. задержка p50/p90=179.1/181.0 мс | Coinbase 56 задержка p50=105.7 мс | смещение часов +25.9 мс | lag loop p99/max=2.2/2.7 мс
14:01:31 [cex] binance_futures 424 сд. p50=175.6 мс | bybit 615 сд. p50=139.5 мс | bybit_book 463 сд. p50=137.7 мс | bybit_spot 190 сд. p50=148.1 мс | bybit_spot_book 308 сд. p50=137.3 мс | okx 437 сд. p50=172.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:01:37 [pm] T-202.5s Up 0.91/0.92 Down 0.08/0.09 ptb=82013.6 | CLOB 10898 сообщ., задержка p50/p90=43.6/57.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792504897496 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=8.0/13.0 мс
14:01:41 [cex] Binance 1789 сд. задержка p50/p90=163.6/193.1 мс | Coinbase 241 задержка p50=105.2 мс | смещение часов +25.9 мс | lag loop p99/max=19.5/49.0 мс
14:01:41 [cex] binance_futures 2800 сд. p50=173.4 мс | bybit 4858 сд. p50=122.6 мс | bybit_book 629 сд. p50=117.9 мс | bybit_spot 1096 сд. p50=130.9 мс | bybit_spot_book 437 сд. p50=128.9 мс | okx 4643 сд. p50=155.7 мс | binance_liq 6 сд. p50=1144.8 мс | bybit_liq 21 сд. p50=301.2 мс
14:01:47 [pm] T-192.5s Up 0.92/0.93 Down 0.07/0.08 ptb=82013.6 | CLOB 6745 сообщ., задержка p50/p90=43.4/46.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792504907498 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=3.8/4.7 мс
14:01:51 [cex] Binance 416 сд. задержка p50/p90=158.8/160.5 мс | Coinbase 97 задержка p50=87.0 мс | смещение часов +25.9 мс | lag loop p99/max=1.9/2.0 мс
14:01:51 [cex] binance_futures 904 сд. p50=163.5 мс | bybit 1635 сд. p50=119.5 мс | bybit_book 722 сд. p50=131.9 мс | bybit_spot 528 сд. p50=128.2 мс | bybit_spot_book 528 сд. p50=128.6 мс | okx 1321 сд. p50=153.1 мс | binance_liq 2 сд. p50=1083.4 мс | bybit_liq 11 сд. p50=397.8 мс
14:01:57 [pm] T-182.5s Up 0.97/0.98 Down 0.02/0.03 ptb=82013.6 | CLOB 7738 сообщ., задержка p50/p90=64.4/140.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792504917499 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=2.9/3.8 мс
14:02:01 [cex] Binance 557 сд. задержка p50/p90=160.0/181.4 мс | Coinbase 105 задержка p50=90.9 мс | смещение часов +25.9 мс | lag loop p99/max=3.9/6.0 мс
14:02:01 [cex] binance_futures 1221 сд. p50=165.5 мс | bybit 1484 сд. p50=119.6 мс | bybit_book 679 сд. p50=131.9 мс | bybit_spot 519 сд. p50=128.6 мс | bybit_spot_book 464 сд. p50=128.7 мс | okx 1503 сд. p50=153.4 мс | binance_liq 3 сд. p50=1080.9 мс | bybit_liq 4 сд. p50=508.1 мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
