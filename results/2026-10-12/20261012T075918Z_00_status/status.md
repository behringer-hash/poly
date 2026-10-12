# Состояние сервера записи

Время (UTC): 2026-10-12 07:59:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 35 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         696         592           2         825        1209
Swap:           2047         126        1921
```
- нагрузка CPU (1/5/15 мин): 0.31 / 0.37 / 0.52

## Данные
- файлов: 2358, всего 698 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 92 | 11 МБ | 0 |
| bn_book | 92 | 885 КБ | 2 |
| bnf_agg | 92 | 16 МБ | 0 |
| bnf_book | 92 | 464 МБ | 0 |
| bnf_depth5 | 92 | 36 МБ | 0 |
| bnf_liq | 79 | 44 КБ | 1513 |
| bs_trade | 92 | 1 МБ | 2 |
| by_book1 | 92 | 35 МБ | 0 |
| by_liq | 75 | 39 КБ | 1386 |
| by_trade | 92 | 11 МБ | 0 |
| cb_ticker | 92 | 9 МБ | 0 |
| clock | 92 | 72 КБ | 18 |
| clock_pm | 92 | 71 КБ | 34 |
| events | 88 | 30 КБ | 290 |
| events_pm | 92 | 36 КБ | 455 |
| health_cex | 92 | 982 КБ | 8 |
| health_feeds | 92 | 4 МБ | 8 |
| health_pm | 92 | 1008 КБ | 8 |
| kr_trade | 92 | 2 МБ | 4 |
| ok_trade | 92 | 14 МБ | 0 |
| pm_depth | 92 | 19 МБ | 0 |
| pm_rtt | 92 | 644 КБ | 0 |
| pm_top | 92 | 38 МБ | 0 |
| pm_trades | 92 | 26 МБ | 0 |
| rtds | 92 | 6 МБ | 0 |
| windows | 92 | 192 КБ | 403 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 6, TLS 45, всего 292
- Polymarket CLOB: TCP 6, TLS 71, всего 119
- Polymarket gamma: TCP 6, TLS 64, всего 76

## Последние строки журнала записи
```
07:58:29 [cex] Binance 86 сд. задержка p50/p90=147.6/148.2 мс | Coinbase 60 задержка p50=84.6 мс | смещение часов +22.2 мс | lag loop p99/max=4.8/7.0 мс
07:58:29 [cex] binance_futures 126 сд. p50=147.9 мс | bybit 175 сд. p50=115.8 мс | okx 81 сд. p50=157.2 мс | binance_futures_book 6994 сд. p50=147.8 мс | binance_futures_depth 93 сд. p50=146.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 213 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 18 сд. p50=52.4 мс | bitstamp 0 сд. p50=n/a мс
07:58:29 [pm] T- 90.4s Up 0.47/0.48 Down 0.52/0.53 ptb=83897.4 | CLOB 14524 сообщ., задержка p50/p90=47.9/85.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791791909590 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.2 мс | lag loop p99/max=2.0/2.2 мс
07:58:39 [cex] Binance 46 сд. задержка p50/p90=147.6/155.4 мс | Coinbase 5 задержка p50=83.4 мс | смещение часов +22.2 мс | lag loop p99/max=2.3/2.3 мс
07:58:39 [cex] binance_futures 59 сд. p50=184.4 мс | bybit 40 сд. p50=115.5 мс | okx 32 сд. p50=155.9 мс | binance_futures_book 3119 сд. p50=147.0 мс | binance_futures_depth 94 сд. p50=147.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 157 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=56.3 мс | bitstamp 1 сд. p50=49.5 мс
07:58:39 [pm] T- 80.4s Up 0.59/0.60 Down 0.40/0.41 ptb=83897.4 | CLOB 11006 сообщ., задержка p50/p90=43.9/50.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791791919592 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.2 мс | lag loop p99/max=2.0/2.0 мс
07:58:49 [cex] Binance 54 сд. задержка p50/p90=147.7/148.9 мс | Coinbase 13 задержка p50=83.6 мс | смещение часов +22.2 мс | lag loop p99/max=2.1/2.6 мс
07:58:49 [cex] binance_futures 36 сд. p50=295.8 мс | bybit 37 сд. p50=115.3 мс | okx 32 сд. p50=156.1 мс | binance_futures_book 1613 сд. p50=146.9 мс | binance_futures_depth 93 сд. p50=147.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 139 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=40.6 мс | bitstamp 3 сд. p50=48.8 мс
07:58:49 [pm] T- 70.4s Up 0.68/0.69 Down 0.31/0.32 ptb=83897.4 | CLOB 14050 сообщ., задержка p50/p90=43.1/73.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791791929593 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.2 мс | lag loop p99/max=1.3/1.6 мс
07:58:59 [cex] Binance 65 сд. задержка p50/p90=147.6/148.3 мс | Coinbase 26 задержка p50=84.9 мс | смещение часов +22.7 мс | lag loop p99/max=2.9/3.7 мс
07:58:59 [cex] binance_futures 93 сд. p50=155.0 мс | bybit 200 сд. p50=115.7 мс | okx 91 сд. p50=157.9 мс | binance_futures_book 2529 сд. p50=146.9 мс | binance_futures_depth 89 сд. p50=147.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 198 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 10 сд. p50=44.8 мс | bitstamp 6 сд. p50=54.5 мс
07:58:59 [pm] T- 60.4s Up 0.41/0.42 Down 0.58/0.59 ptb=83897.4 | CLOB 14059 сообщ., задержка p50/p90=41.8/69.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791791939594 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.2 мс | lag loop p99/max=1.7/11.0 мс
07:59:09 [cex] Binance 144 сд. задержка p50/p90=147.5/149.1 мс | Coinbase 38 задержка p50=95.8 мс | смещение часов +22.7 мс | lag loop p99/max=2.2/2.2 мс
07:59:09 [cex] binance_futures 91 сд. p50=148.5 мс | bybit 178 сд. p50=117.1 мс | okx 40 сд. p50=156.4 мс | binance_futures_book 2164 сд. p50=147.7 мс | binance_futures_depth 85 сд. p50=147.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 264 сд. p50=114.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=44.2 мс | bitstamp 0 сд. p50=n/a мс
07:59:09 [pm] T- 50.4s Up 0.17/0.20 Down 0.80/0.83 ptb=83897.4 | CLOB 12822 сообщ., задержка p50/p90=41.8/53.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791791949595 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.3 мс | lag loop p99/max=2.1/4.3 мс
```

Представлено версией кода: a7854de; python 3.12.3
