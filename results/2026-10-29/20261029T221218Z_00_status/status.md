# Состояние сервера записи

Время (UTC): 2026-10-29 22:12:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 14 hours, 48 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         626         954           1         504        1279
Swap:           2047         319        1728
```
- нагрузка CPU (1/5/15 мин): 0.39 / 0.54 / 0.54

## Данные
- файлов: 5829, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 36 МБ | 0 |
| bn_book | 242 | 3 МБ | 0 |
| bnf_agg | 242 | 52 МБ | 0 |
| bnf_book | 82 | 581 МБ | 0 |
| bnf_liq | 212 | 140 КБ | 2 |
| by_book1 | 242 | 112 МБ | 0 |
| by_liq | 225 | 112 КБ | 4 |
| by_trade | 242 | 36 МБ | 0 |
| bys_book1 | 242 | 85 МБ | 0 |
| bys_trade | 242 | 34 МБ | 0 |
| cb_ticker | 242 | 32 МБ | 0 |
| clock | 242 | 187 КБ | 49 |
| clock_pm | 242 | 187 КБ | 22 |
| events | 229 | 73 КБ | 4348 |
| events_pm | 242 | 85 КБ | 58 |
| health_cex | 242 | 3 МБ | 8 |
| health_feeds | 242 | 8 МБ | 8 |
| health_pm | 242 | 3 МБ | 6 |
| ok_trade | 242 | 46 МБ | 0 |
| pm_depth | 242 | 49 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 4 |
| pm_top | 242 | 100 МБ | 2 |
| pm_trades | 241 | 71 МБ | 2 |
| rtds | 242 | 15 МБ | 2 |
| windows | 242 | 498 КБ | 225 |

Дни с данными: 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 48, всего 298
- Polymarket CLOB: TCP 6, TLS 46, всего 89
- Polymarket gamma: TCP 5, TLS 35, всего 43

## Последние строки журнала записи
```
22:11:32 [pm] T-207.4s Up 0.65/0.68 Down 0.32/0.35 ptb=78612.6 | CLOB 8332 сообщ., задержка p50/p90=44.8/49.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793311892554 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.0/2.1 мс
22:11:38 [cex] Binance 271 сд. задержка p50/p90=152.5/157.3 мс | Coinbase 157 задержка p50=82.9 мс | смещение часов +22.0 мс | lag loop p99/max=6.3/20.3 мс
22:11:38 [cex] binance_futures 515 сд. p50=156.1 мс | bybit 846 сд. p50=119.5 мс | bybit_book 613 сд. p50=113.2 мс | bybit_spot 378 сд. p50=118.4 мс | bybit_spot_book 252 сд. p50=114.0 мс | okx 320 сд. p50=159.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 7699 сд. p50=163.0 мс
22:11:42 [pm] T-197.4s Up 0.75/0.76 Down 0.24/0.25 ptb=78612.6 | CLOB 10852 сообщ., задержка p50/p90=45.6/60.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793311902556 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.2/1.2 мс
22:11:48 [cex] Binance 339 сд. задержка p50/p90=146.7/151.0 мс | Coinbase 92 задержка p50=83.2 мс | смещение часов +22.0 мс | lag loop p99/max=4.1/4.7 мс
22:11:48 [cex] binance_futures 474 сд. p50=150.7 мс | bybit 594 сд. p50=115.9 мс | bybit_book 572 сд. p50=113.2 мс | bybit_spot 442 сд. p50=116.3 мс | bybit_spot_book 314 сд. p50=114.1 мс | okx 822 сд. p50=161.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 11304 сд. p50=149.0 мс
22:11:52 [pm] T-187.4s Up 0.79/0.80 Down 0.20/0.21 ptb=78612.6 | CLOB 8143 сообщ., задержка p50/p90=45.0/63.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793311912557 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=2.2/2.7 мс
22:11:58 [cex] Binance 291 сд. задержка p50/p90=147.5/149.7 мс | Coinbase 121 задержка p50=82.8 мс | смещение часов +22.0 мс | lag loop p99/max=8.7/9.6 мс
22:11:58 [cex] binance_futures 355 сд. p50=151.8 мс | bybit 750 сд. p50=116.1 мс | bybit_book 581 сд. p50=113.3 мс | bybit_spot 701 сд. p50=116.8 мс | bybit_spot_book 328 сд. p50=114.1 мс | okx 456 сд. p50=160.3 мс | binance_liq 1 сд. p50=1153.0 мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 12105 сд. p50=147.5 мс
22:12:02 [pm] T-177.4s Up 0.90/0.91 Down 0.09/0.10 ptb=78612.6 | CLOB 10167 сообщ., задержка p50/p90=45.8/47.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793311922559 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.6 мс | lag loop p99/max=3.3/4.9 мс
22:12:08 [cex] Binance 184 сд. задержка p50/p90=148.6/168.9 мс | Coinbase 119 задержка p50=82.9 мс | смещение часов +22.0 мс | lag loop p99/max=9.6/14.7 мс
22:12:08 [cex] binance_futures 349 сд. p50=151.7 мс | bybit 639 сд. p50=116.0 мс | bybit_book 510 сд. p50=113.3 мс | bybit_spot 555 сд. p50=116.3 мс | bybit_spot_book 528 сд. p50=114.1 мс | okx 478 сд. p50=162.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 8342 сд. p50=149.6 мс
22:12:12 [pm] T-167.4s Up 0.95/0.96 Down 0.04/0.05 ptb=78612.6 | CLOB 7088 сообщ., задержка p50/p90=46.2/63.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793311932560 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=2.0/2.1 мс
22:12:18 [cex] Binance 754 сд. задержка p50/p90=149.5/156.6 мс | Coinbase 192 задержка p50=82.3 мс | смещение часов +22.0 мс | lag loop p99/max=14.7/21.4 мс
22:12:18 [cex] binance_futures 1321 сд. p50=151.7 мс | bybit 1478 сд. p50=119.0 мс | bybit_book 549 сд. p50=113.3 мс | bybit_spot 731 сд. p50=117.8 мс | bybit_spot_book 350 сд. p50=114.3 мс | okx 1524 сд. p50=166.3 мс | binance_liq 2 сд. p50=1152.2 мс | bybit_liq 3 сд. p50=349.3 мс | binance_futures_book 20345 сд. p50=149.8 мс
```

Представлено версией кода: b8783c2; python 3.12.3
