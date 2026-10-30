# Состояние сервера записи

Время (UTC): 2026-10-30 18:53:09

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 2 days, 11 hours, 29 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         668         399           1        1025        1237
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.68 / 0.39 / 0.31

## Данные
- файлов: 5842, всего 2 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 39 МБ | 0 |
| bn_book | 242 | 3 МБ | 2 |
| bnf_agg | 242 | 55 МБ | 0 |
| bnf_book | 102 | 864 МБ | 0 |
| bnf_liq | 212 | 158 КБ | 10 |
| by_book1 | 242 | 119 МБ | 0 |
| by_liq | 225 | 131 КБ | 10 |
| by_trade | 242 | 38 МБ | 1 |
| bys_book1 | 242 | 88 МБ | 2 |
| bys_trade | 242 | 37 МБ | 2 |
| cb_ticker | 242 | 34 МБ | 2 |
| clock | 242 | 189 КБ | 22 |
| clock_pm | 242 | 189 КБ | 58 |
| events | 223 | 71 КБ | 1669 |
| events_pm | 241 | 86 КБ | 546 |
| health_cex | 242 | 3 МБ | 6 |
| health_feeds | 242 | 8 МБ | 6 |
| health_pm | 242 | 3 МБ | 4 |
| ok_trade | 242 | 48 МБ | 1 |
| pm_depth | 242 | 51 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 0 |
| pm_top | 242 | 102 МБ | 0 |
| pm_trades | 241 | 72 МБ | 2 |
| rtds | 242 | 16 МБ | 0 |
| windows | 242 | 501 КБ | 215 |

Дни с данными: 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 7, TLS 134, всего 873
- Polymarket CLOB: TCP 9, TLS 123, всего 170
- Polymarket gamma: TCP 5, TLS 121, всего 128

## Последние строки журнала записи
```
18:52:23 [cex] Binance 2462 сд. задержка p50/p90=195.1/242.1 мс | Coinbase 642 задержка p50=223.2 мс | смещение часов +23.1 мс | lag loop p99/max=83.1/93.7 мс
18:52:23 [cex] binance_futures 3017 сд. p50=190.2 мс | bybit 6526 сд. p50=246.9 мс | bybit_book 406 сд. p50=114.8 мс | bybit_spot 1949 сд. p50=140.5 мс | bybit_spot_book 252 сд. p50=115.5 мс | okx 1637 сд. p50=649.3 мс | binance_liq 3 сд. p50=693.0 мс | bybit_liq 12 сд. p50=309.0 мс | binance_futures_book 19953 сд. p50=160.2 мс
18:52:23 [pm] T-156.4s Up n/a/0.01 Down 0.99/n/a ptb=76570.7 | CLOB 5392 сообщ., задержка p50/p90=43.6/51.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793386343611 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.1/2.5 мс
18:52:33 [cex] Binance 2312 сд. задержка p50/p90=150.6/164.6 мс | Coinbase 548 задержка p50=105.6 мс | смещение часов +23.1 мс | lag loop p99/max=29.4/41.8 мс
18:52:33 [cex] binance_futures 2920 сд. p50=154.0 мс | bybit 3544 сд. p50=117.3 мс | bybit_book 789 сд. p50=114.7 мс | bybit_spot 1195 сд. p50=120.4 мс | bybit_spot_book 528 сд. p50=115.4 мс | okx 8202 сд. p50=166.9 мс | binance_liq 7 сд. p50=1075.6 мс | bybit_liq 141 сд. p50=392.8 мс | binance_futures_book 33653 сд. p50=148.1 мс
18:52:33 [pm] T-146.4s Up n/a/0.01 Down 0.99/n/a ptb=76570.7 | CLOB 3092 сообщ., задержка p50/p90=43.3/53.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793386353613 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.1/3.8 мс
18:52:43 [cex] Binance 595 сд. задержка p50/p90=148.7/155.2 мс | Coinbase 238 задержка p50=95.2 мс | смещение часов +23.1 мс | lag loop p99/max=4.9/6.2 мс
18:52:43 [cex] binance_futures 743 сд. p50=151.5 мс | bybit 1274 сд. p50=116.9 мс | bybit_book 634 сд. p50=114.5 мс | bybit_spot 685 сд. p50=118.6 мс | bybit_spot_book 331 сд. p50=115.1 мс | okx 662 сд. p50=161.0 мс | binance_liq 3 сд. p50=1094.7 мс | bybit_liq 7 сд. p50=311.4 мс | binance_futures_book 15726 сд. p50=150.5 мс
18:52:43 [pm] T-136.4s Up n/a/0.01 Down 0.99/n/a ptb=76570.7 | CLOB 2117 сообщ., задержка p50/p90=42.5/51.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793386363615 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.1/2.1 мс
18:52:53 [cex] Binance 1140 сд. задержка p50/p90=147.0/156.7 мс | Coinbase 495 задержка p50=110.9 мс | смещение часов +20.3 мс | lag loop p99/max=19.7/46.6 мс
18:52:53 [cex] binance_futures 1488 сд. p50=151.7 мс | bybit 3290 сд. p50=123.1 мс | bybit_book 707 сд. p50=111.7 мс | bybit_spot 1110 сд. p50=117.5 мс | bybit_spot_book 407 сд. p50=112.8 мс | okx 2449 сд. p50=164.9 мс | binance_liq 8 сд. p50=1051.6 мс | bybit_liq 56 сд. p50=345.1 мс | binance_futures_book 19244 сд. p50=145.1 мс
18:52:53 [pm] T-126.4s Up n/a/0.01 Down 0.99/n/a ptb=76570.7 | CLOB 2063 сообщ., задержка p50/p90=42.2/43.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793386373616 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.0/2.0 мс
18:53:03 [cex] Binance 517 сд. задержка p50/p90=146.2/151.5 мс | Coinbase 230 задержка p50=94.7 мс | смещение часов +20.3 мс | lag loop p99/max=3.3/4.3 мс
18:53:03 [cex] binance_futures 857 сд. p50=148.3 мс | bybit 1036 сд. p50=113.9 мс | bybit_book 600 сд. p50=111.7 мс | bybit_spot 503 сд. p50=115.2 мс | bybit_spot_book 323 сд. p50=112.4 мс | okx 752 сд. p50=158.2 мс | binance_liq 5 сд. p50=1101.0 мс | bybit_liq 17 сд. p50=328.0 мс | binance_futures_book 15993 сд. p50=145.7 мс
18:53:03 [pm] T-116.4s Up n/a/0.01 Down 0.99/n/a ptb=76570.7 | CLOB 2586 сообщ., задержка p50/p90=42.5/56.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793386383619 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.1/3.1 мс
```

Представлено версией кода: fcaf736; python 3.12.3
