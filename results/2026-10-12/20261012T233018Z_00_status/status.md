# Состояние сервера записи

Время (UTC): 2026-10-12 23:30:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 16 hours, 6 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         779         701           2         622        1126
Swap:           2047         108        1939
```
- нагрузка CPU (1/5/15 мин): 0.31 / 0.44 / 0.55

## Данные
- файлов: 2771, всего 871 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 108 | 13 МБ | 1 |
| bn_book | 108 | 1 МБ | 1 |
| bnf_agg | 108 | 21 МБ | 1 |
| bnf_book | 108 | 594 МБ | 1 |
| bnf_depth5 | 108 | 40 МБ | 1 |
| bnf_liq | 95 | 58 КБ | 152 |
| bs_trade | 108 | 1 МБ | 1 |
| by_book1 | 108 | 43 МБ | 1 |
| by_liq | 91 | 55 КБ | 308 |
| by_trade | 108 | 15 МБ | 1 |
| cb_ticker | 108 | 11 МБ | 1 |
| clock | 108 | 83 КБ | 15 |
| clock_pm | 108 | 83 КБ | 35 |
| events | 101 | 34 КБ | 445 |
| events_pm | 108 | 41 КБ | 752 |
| health_cex | 108 | 1 МБ | 9 |
| health_feeds | 108 | 4 МБ | 9 |
| health_pm | 108 | 1 МБ | 9 |
| kr_trade | 108 | 3 МБ | 1 |
| ok_trade | 108 | 18 МБ | 1 |
| pm_depth | 108 | 21 МБ | 1 |
| pm_rtt | 108 | 730 КБ | 1 |
| pm_top | 108 | 43 МБ | 1 |
| pm_trades | 108 | 31 МБ | 1 |
| rtds | 108 | 7 МБ | 1 |
| windows | 108 | 223 КБ | 73 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 49, всего 299
- Polymarket CLOB: TCP 5, TLS 61, всего 102
- Polymarket gamma: TCP 5, TLS 61, всего 73

## Последние строки журнала записи
```
23:29:29 [cex] binance_futures 25 сд. p50=294.4 мс | bybit 57 сд. p50=114.2 мс | okx 20 сд. p50=148.7 мс | binance_futures_book 1343 сд. p50=145.8 мс | binance_futures_depth 88 сд. p50=145.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 197 сд. p50=112.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=38.2 мс | bitstamp 0 сд. p50=n/a мс
23:29:38 [pm] T- 21.9s Up n/a/0.00 Down 1.00/n/a ptb=82024.2 | CLOB 529 сообщ., задержка p50/p90=39.0/40.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791847778101 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=2.1/2.1 мс
23:29:39 [cex] Binance 16 сд. задержка p50/p90=145.6/146.6 мс | Coinbase 28 задержка p50=82.9 мс | смещение часов +21.1 мс | lag loop p99/max=2.1/2.2 мс
23:29:39 [cex] binance_futures 51 сд. p50=259.1 мс | bybit 47 сд. p50=114.1 мс | okx 25 сд. p50=148.8 мс | binance_futures_book 2426 сд. p50=145.8 мс | binance_futures_depth 93 сд. p50=145.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 360 сд. p50=112.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 0 сд. p50=n/a мс | bitstamp 1 сд. p50=55.1 мс
23:29:45 [pm] окно btc-updown-5m-1791847800 (2026-10-12 23:30:00 UTC): Bitcoin Up or Down - October 12, 7:30PM-7:35PM ET
23:29:48 [pm] T- 11.9s Up n/a/0.00 Down 1.00/n/a ptb=82024.2 | CLOB 1054 сообщ., задержка p50/p90=37.1/40.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791847788101 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=2.8/18.6 мс
23:29:49 [cex] Binance 60 сд. задержка p50/p90=146.3/148.0 мс | Coinbase 65 задержка p50=84.0 мс | смещение часов +21.1 мс | lag loop p99/max=2.2/3.6 мс
23:29:49 [cex] binance_futures 99 сд. p50=150.6 мс | bybit 99 сд. p50=115.1 мс | okx 88 сд. p50=151.3 мс | binance_futures_book 4944 сд. p50=145.9 мс | binance_futures_depth 93 сд. p50=145.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 228 сд. p50=112.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 17 сд. p50=40.1 мс | bitstamp 3 сд. p50=60.4 мс
23:29:58 [pm] T-  1.9s Up n/a/0.00 Down 1.00/n/a ptb=82024.2 | CLOB 2159 сообщ., задержка p50/p90=36.0/39.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791847798103 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.9/2.0 мс
23:29:59 [cex] Binance 48 сд. задержка p50/p90=145.8/146.6 мс | Coinbase 54 задержка p50=83.1 мс | смещение часов +21.1 мс | lag loop p99/max=2.1/2.2 мс
23:29:59 [cex] binance_futures 50 сд. p50=255.3 мс | bybit 77 сд. p50=114.6 мс | okx 84 сд. p50=150.5 мс | binance_futures_book 2672 сд. p50=146.1 мс | binance_futures_depth 88 сд. p50=145.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 206 сд. p50=112.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 14 сд. p50=38.2 мс | bitstamp 3 сд. p50=58.5 мс
23:30:08 [pm] T-291.9s Up 0.51/0.52 Down 0.48/0.49 ptb=81939.9 | CLOB 7405 сообщ., задержка p50/p90=81.8/197.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791847808104 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=13.0/16.2 мс
23:30:09 [cex] Binance 76 сд. задержка p50/p90=145.4/152.0 мс | Coinbase 60 задержка p50=84.2 мс | смещение часов +20.0 мс | lag loop p99/max=10.9/20.7 мс
23:30:09 [cex] binance_futures 163 сд. p50=150.0 мс | bybit 257 сд. p50=114.3 мс | okx 178 сд. p50=149.6 мс | binance_futures_book 6548 сд. p50=145.4 мс | binance_futures_depth 92 сд. p50=145.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 352 сд. p50=111.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 15 сд. p50=52.6 мс | bitstamp 3 сд. p50=48.5 мс
23:30:18 [pm] T-281.9s Up 0.59/0.60 Down 0.40/0.41 ptb=81939.9 | CLOB 12692 сообщ., задержка p50/p90=37.7/214.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791847818106 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=3.2/3.3 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
