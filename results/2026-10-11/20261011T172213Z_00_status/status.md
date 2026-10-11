# Состояние сервера записи

Время (UTC): 2026-10-11 17:22:13

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 4 days, 9 hours, 58 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         690         807           1         616        1215
Swap:           2047          61        1986
```
- нагрузка CPU (1/5/15 мин): 0.46 / 0.29 / 0.26

## Данные
- файлов: 1997, всего 516 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 78 | 9 МБ | 1 |
| bn_book | 78 | 730 КБ | 1 |
| bnf_agg | 78 | 13 МБ | 1 |
| bnf_book | 78 | 329 МБ | 0 |
| bnf_depth5 | 78 | 28 МБ | 1 |
| bnf_liq | 66 | 37 КБ | 67 |
| bs_trade | 78 | 962 КБ | 1 |
| by_book1 | 78 | 28 МБ | 1 |
| by_liq | 62 | 35 КБ | 67 |
| by_trade | 78 | 9 МБ | 1 |
| cb_ticker | 78 | 8 МБ | 3 |
| clock | 78 | 59 КБ | 35 |
| clock_pm | 78 | 59 КБ | 50 |
| events | 75 | 26 КБ | 662 |
| events_pm | 78 | 31 КБ | 405 |
| health_cex | 78 | 815 КБ | 1 |
| health_feeds | 78 | 3 МБ | 1 |
| health_pm | 78 | 840 КБ | 9 |
| kr_trade | 78 | 2 МБ | 1 |
| ok_trade | 78 | 12 МБ | 1 |
| pm_depth | 78 | 15 МБ | 1 |
| pm_rtt | 78 | 525 КБ | 1 |
| pm_top | 78 | 30 МБ | 1 |
| pm_trades | 78 | 21 МБ | 1 |
| rtds | 78 | 5 МБ | 1 |
| windows | 78 | 160 КБ | 38 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 44, всего 297
- Polymarket CLOB: TCP 8, TLS 41, всего 86
- Polymarket gamma: TCP 6, TLS 55, всего 70

## Последние строки журнала записи
```
17:21:31 [cex] Binance 87 сд. задержка p50/p90=146.2/148.4 мс | Coinbase 45 задержка p50=83.0 мс | смещение часов +20.6 мс | lag loop p99/max=2.1/2.3 мс
17:21:31 [cex] binance_futures 217 сд. p50=149.1 мс | bybit 257 сд. p50=115.8 мс | okx 134 сд. p50=155.3 мс | binance_futures_book 3225 сд. p50=145.2 мс | binance_futures_depth 94 сд. p50=144.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 213 сд. p50=112.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 18 сд. p50=43.7 мс | bitstamp 2 сд. p50=47.7 мс
17:21:32 [pm] T-208.0s Up 0.81/0.82 Down 0.18/0.19 ptb=83863.5 | CLOB 5866 сообщ., задержка p50/p90=37.0/38.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791739292015 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.9 мс | lag loop p99/max=1.9/2.1 мс
17:21:41 [cex] Binance 27 сд. задержка p50/p90=145.6/146.7 мс | Coinbase 39 задержка p50=82.9 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/2.2 мс
17:21:41 [cex] binance_futures 33 сд. p50=294.3 мс | bybit 39 сд. p50=114.5 мс | okx 36 сд. p50=154.2 мс | binance_futures_book 662 сд. p50=144.9 мс | binance_futures_depth 96 сд. p50=145.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 138 сд. p50=112.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 9 сд. p50=45.0 мс | bitstamp 2 сд. p50=47.0 мс
17:21:42 [pm] T-198.0s Up 0.82/0.83 Down 0.17/0.18 ptb=83863.5 | CLOB 4287 сообщ., задержка p50/p90=36.8/37.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791739302017 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.8 мс | lag loop p99/max=1.7/1.8 мс
17:21:51 [cex] Binance 25 сд. задержка p50/p90=145.7/146.0 мс | Coinbase 47 задержка p50=81.9 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/2.2 мс
17:21:51 [cex] binance_futures 45 сд. p50=294.3 мс | bybit 59 сд. p50=115.0 мс | okx 32 сд. p50=154.2 мс | binance_futures_book 791 сд. p50=144.9 мс | binance_futures_depth 94 сд. p50=145.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 202 сд. p50=112.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=44.8 мс | bitstamp 4 сд. p50=57.3 мс
17:21:52 [pm] T-188.0s Up 0.82/0.83 Down 0.17/0.18 ptb=83863.5 | CLOB 4122 сообщ., задержка p50/p90=37.0/38.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791739312019 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.8 мс | lag loop p99/max=2.0/2.1 мс
17:22:01 [cex] Binance 40 сд. задержка p50/p90=146.9/147.3 мс | Coinbase 26 задержка p50=82.1 мс | смещение часов +20.5 мс | lag loop p99/max=2.0/2.1 мс
17:22:01 [cex] binance_futures 80 сд. p50=224.6 мс | bybit 78 сд. p50=115.1 мс | okx 72 сд. p50=156.0 мс | binance_futures_book 1956 сд. p50=145.1 мс | binance_futures_depth 92 сд. p50=145.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 162 сд. p50=112.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 8 сд. p50=63.6 мс | bitstamp 0 сд. p50=n/a мс
17:22:02 [pm] T-178.0s Up 0.81/0.82 Down 0.18/0.19 ptb=83863.5 | CLOB 4757 сообщ., задержка p50/p90=36.8/37.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791739322020 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=1.7/2.1 мс
17:22:11 [cex] Binance 77 сд. задержка p50/p90=146.1/152.7 мс | Coinbase 28 задержка p50=83.5 мс | смещение часов +20.5 мс | lag loop p99/max=4.7/9.6 мс
17:22:11 [cex] binance_futures 115 сд. p50=158.3 мс | bybit 86 сд. p50=114.9 мс | okx 139 сд. p50=155.0 мс | binance_futures_book 3308 сд. p50=145.9 мс | binance_futures_depth 95 сд. p50=145.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 198 сд. p50=112.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 16 сд. p50=47.1 мс | bitstamp 6 сд. p50=54.9 мс
17:22:12 [pm] T-168.0s Up 0.72/0.73 Down 0.27/0.28 ptb=83863.5 | CLOB 6151 сообщ., задержка p50/p90=36.8/37.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791739332022 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=1.9/2.1 мс
```

Представлено версией кода: 69087ca; python 3.12.3
