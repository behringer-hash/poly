# Состояние сервера записи

Время (UTC): 2026-10-12 11:05:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 3 hours, 41 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         768         704           2         641        1137
Swap:           2047         105        1942
```
- нагрузка CPU (1/5/15 мин): 0.57 / 0.45 / 0.37

## Данные
- файлов: 2459, всего 609 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 96 | 10 МБ | 1 |
| bn_book | 96 | 870 КБ | 1 |
| bnf_agg | 96 | 15 МБ | 1 |
| bnf_book | 96 | 389 МБ | 1 |
| bnf_depth5 | 96 | 32 МБ | 1 |
| bnf_liq | 83 | 45 КБ | 3 |
| bs_trade | 96 | 1 МБ | 3 |
| by_book1 | 96 | 32 МБ | 1 |
| by_liq | 78 | 40 КБ | 1074 |
| by_trade | 96 | 10 МБ | 1 |
| cb_ticker | 96 | 9 МБ | 1 |
| clock | 96 | 73 КБ | 5 |
| clock_pm | 96 | 73 КБ | 21 |
| events | 91 | 32 КБ | 537 |
| events_pm | 96 | 37 КБ | 252 |
| health_cex | 96 | 1000 КБ | 7 |
| health_feeds | 96 | 4 МБ | 7 |
| health_pm | 96 | 1 МБ | 6 |
| kr_trade | 96 | 2 МБ | 1 |
| ok_trade | 96 | 14 МБ | 1 |
| pm_depth | 96 | 18 МБ | 0 |
| pm_rtt | 96 | 633 КБ | 4 |
| pm_top | 96 | 36 МБ | 0 |
| pm_trades | 96 | 26 МБ | 0 |
| rtds | 96 | 6 МБ | 0 |
| windows | 95 | 198 КБ | 363 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 43, всего 306
- Polymarket CLOB: TCP 6, TLS 46, всего 94
- Polymarket gamma: TCP 5, TLS 43, всего 55

## Последние строки журнала записи
```
11:04:51 [pm] T-  8.8s Up n/a/0.00 Down 1.00/n/a ptb=83419.8 | CLOB 655 сообщ., задержка p50/p90=38.4/59.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791803091238 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=15.3/37.3 мс
11:04:51 [cex] Binance 23 сд. задержка p50/p90=146.2/147.1 мс | Coinbase 17 задержка p50=82.7 мс | смещение часов +21.1 мс | lag loop p99/max=2.2/2.3 мс
11:04:51 [cex] binance_futures 30 сд. p50=294.5 мс | bybit 19 сд. p50=114.2 мс | okx 21 сд. p50=154.6 мс | binance_futures_book 1229 сд. p50=145.7 мс | binance_futures_depth 94 сд. p50=146.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 160 сд. p50=113.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=39.9 мс | bitstamp 1 сд. p50=45.4 мс
11:05:01 [pm] T-298.8s Up 0.47/0.48 Down 0.52/0.53 ptb=n/a | CLOB 1751 сообщ., задержка p50/p90=57.9/60.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791803101239 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.0/2.2 мс
11:05:01 [cex] Binance 13 сд. задержка p50/p90=146.1/146.9 мс | Coinbase 15 задержка p50=82.6 мс | смещение часов +21.1 мс | lag loop p99/max=2.1/2.2 мс
11:05:01 [cex] binance_futures 25 сд. p50=294.7 мс | bybit 4 сд. p50=114.3 мс | okx 27 сд. p50=154.7 мс | binance_futures_book 1189 сд. p50=145.7 мс | binance_futures_depth 98 сд. p50=146.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 83 сд. p50=113.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=43.2 мс | bitstamp 3 сд. p50=48.7 мс
11:05:11 [pm] T-288.8s Up 0.48/0.49 Down 0.51/0.52 ptb=83350.2 | CLOB 4832 сообщ., задержка p50/p90=58.2/59.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791803111241 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=11.6/13.1 мс
11:05:11 [cex] Binance 16 сд. задержка p50/p90=146.1/147.5 мс | Coinbase 23 задержка p50=82.4 мс | смещение часов +21.1 мс | lag loop p99/max=2.3/3.1 мс
11:05:11 [cex] binance_futures 22 сд. p50=295.1 мс | bybit 9 сд. p50=114.3 мс | okx 28 сд. p50=154.9 мс | binance_futures_book 979 сд. p50=145.7 мс | binance_futures_depth 97 сд. p50=146.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 136 сд. p50=113.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 11 сд. p50=54.9 мс | bitstamp 0 сд. p50=n/a мс
11:05:21 [pm] T-278.8s Up 0.43/0.44 Down 0.56/0.57 ptb=83350.2 | CLOB 5340 сообщ., задержка p50/p90=59.8/62.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791803121242 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.1/2.1 мс
11:05:21 [cex] Binance 21 сд. задержка p50/p90=146.1/146.2 мс | Coinbase 11 задержка p50=81.4 мс | смещение часов +21.1 мс | lag loop p99/max=2.1/2.2 мс
11:05:21 [cex] binance_futures 34 сд. p50=294.8 мс | bybit 7 сд. p50=114.2 мс | okx 64 сд. p50=154.7 мс | binance_futures_book 2003 сд. p50=145.7 мс | binance_futures_depth 97 сд. p50=146.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 105 сд. p50=113.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=39.3 мс | bitstamp 0 сд. p50=n/a мс
11:05:31 [pm] T-268.8s Up 0.39/0.40 Down 0.60/0.61 ptb=83350.2 | CLOB 5580 сообщ., задержка p50/p90=59.6/61.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791803131243 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=1.4/2.0 мс
11:05:31 [cex] Binance 22 сд. задержка p50/p90=146.1/146.3 мс | Coinbase 17 задержка p50=82.3 мс | смещение часов +21.1 мс | lag loop p99/max=2.0/2.1 мс
11:05:31 [cex] binance_futures 30 сд. p50=294.5 мс | bybit 56 сд. p50=114.4 мс | okx 32 сд. p50=154.8 мс | binance_futures_book 3443 сд. p50=145.9 мс | binance_futures_depth 96 сд. p50=146.5 мс | binance_liq 1 сд. p50=1152.5 мс | bybit_book 156 сд. p50=113.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=89.8 мс | bitstamp 1 сд. p50=46.4 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
