# Состояние сервера записи

Время (UTC): 2026-10-28 18:52:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 11 hours, 28 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         602         283           1        1195        1303
Swap:           2047         304        1743
```
- нагрузка CPU (1/5/15 мин): 0.40 / 0.30 / 0.29

## Данные
- файлов: 5805, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 37 МБ | 0 |
| bn_book | 242 | 3 МБ | 0 |
| bnf_agg | 242 | 55 МБ | 0 |
| bnf_book | 54 | 560 МБ | 0 |
| bnf_liq | 211 | 139 КБ | 36 |
| by_book1 | 242 | 115 МБ | 0 |
| by_liq | 226 | 100 КБ | 365 |
| by_trade | 242 | 40 МБ | 0 |
| bys_book1 | 242 | 87 МБ | 0 |
| bys_trade | 242 | 37 МБ | 0 |
| cb_ticker | 242 | 33 МБ | 0 |
| clock | 242 | 188 КБ | 60 |
| clock_pm | 242 | 188 КБ | 25 |
| events | 233 | 74 КБ | 1719 |
| events_pm | 241 | 83 КБ | 1422 |
| health_cex | 242 | 3 МБ | 8 |
| health_feeds | 242 | 7 МБ | 8 |
| health_pm | 242 | 3 МБ | 1 |
| ok_trade | 242 | 48 МБ | 0 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 5 |
| pm_top | 242 | 103 МБ | 1 |
| pm_trades | 242 | 72 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 501 КБ | 175 |

Дни с данными: 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 38, всего 300
- Polymarket CLOB: TCP 5, TLS 54, всего 100
- Polymarket gamma: TCP 5, TLS 44, всего 55

## Последние строки журнала записи
```
18:51:40 [cex] Binance 413 сд. задержка p50/p90=156.0/158.6 мс | Coinbase 98 задержка p50=91.0 мс | смещение часов +18.4 мс | lag loop p99/max=5.6/6.5 мс
18:51:40 [cex] binance_futures 625 сд. p50=145.4 мс | bybit 808 сд. p50=113.0 мс | bybit_book 575 сд. p50=109.8 мс | bybit_spot 552 сд. p50=113.5 мс | bybit_spot_book 377 сд. p50=110.4 мс | okx 935 сд. p50=158.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 17981 сд. p50=166.7 мс
18:51:47 [pm] T-192.4s Up 0.15/0.18 Down 0.82/0.85 ptb=81012.2 | CLOB 1683 сообщ., задержка p50/p90=64.9/97.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793213507614 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=2.0/2.0 мс
18:51:50 [cex] Binance 183 сд. задержка p50/p90=155.2/157.9 мс | Coinbase 70 задержка p50=90.5 мс | смещение часов +18.4 мс | lag loop p99/max=3.6/4.9 мс
18:51:50 [cex] binance_futures 315 сд. p50=145.1 мс | bybit 446 сд. p50=112.3 мс | bybit_book 605 сд. p50=109.8 мс | bybit_spot 343 сд. p50=113.1 мс | bybit_spot_book 361 сд. p50=110.2 мс | okx 444 сд. p50=157.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 11800 сд. p50=158.5 мс
18:51:57 [pm] T-182.4s Up 0.14/0.16 Down 0.84/0.86 ptb=81012.2 | CLOB 4754 сообщ., задержка p50/p90=40.9/48.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793213517616 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=1.3/1.7 мс
18:52:00 [cex] Binance 204 сд. задержка p50/p90=154.4/158.0 мс | Coinbase 98 задержка p50=90.3 мс | смещение часов +18.4 мс | lag loop p99/max=5.3/8.5 мс
18:52:00 [cex] binance_futures 321 сд. p50=144.5 мс | bybit 490 сд. p50=111.8 мс | bybit_book 610 сд. p50=109.7 мс | bybit_spot 513 сд. p50=113.3 мс | bybit_spot_book 362 сд. p50=110.1 мс | okx 396 сд. p50=156.6 мс | binance_liq 1 сд. p50=1156.4 мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 10521 сд. p50=157.6 мс
18:52:07 [pm] T-172.4s Up 0.21/0.22 Down 0.78/0.79 ptb=81012.2 | CLOB 3539 сообщ., задержка p50/p90=46.1/72.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793213527617 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.9 мс | lag loop p99/max=2.1/2.1 мс
18:52:10 [cex] Binance 246 сд. задержка p50/p90=154.6/158.7 мс | Coinbase 90 задержка p50=92.8 мс | смещение часов +18.4 мс | lag loop p99/max=5.5/7.9 мс
18:52:10 [cex] binance_futures 261 сд. p50=144.9 мс | bybit 450 сд. p50=112.0 мс | bybit_book 610 сд. p50=109.8 мс | bybit_spot 457 сд. p50=113.8 мс | bybit_spot_book 352 сд. p50=110.2 мс | okx 494 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 10937 сд. p50=159.1 мс
18:52:17 [pm] T-162.4s Up 0.11/0.12 Down 0.88/0.89 ptb=81012.2 | CLOB 4183 сообщ., задержка p50/p90=44.2/66.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793213537618 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.9 мс | lag loop p99/max=2.1/2.1 мс
18:52:20 [cex] Binance 191 сд. задержка p50/p90=154.9/156.9 мс | Coinbase 83 задержка p50=90.2 мс | смещение часов +18.4 мс | lag loop p99/max=3.8/5.2 мс
18:52:20 [cex] binance_futures 290 сд. p50=145.1 мс | bybit 431 сд. p50=112.0 мс | bybit_book 504 сд. p50=109.8 мс | bybit_spot 354 сд. p50=113.4 мс | bybit_spot_book 341 сд. p50=110.2 мс | okx 500 сд. p50=156.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 14033 сд. p50=156.7 мс
18:52:27 [pm] T-152.4s Up 0.23/0.24 Down 0.76/0.77 ptb=81012.2 | CLOB 4642 сообщ., задержка p50/p90=42.5/66.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793213547620 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.9 мс | lag loop p99/max=1.8/2.1 мс
```

Представлено версией кода: a66af29; python 3.12.3
