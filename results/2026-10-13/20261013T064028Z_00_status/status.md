# Состояние сервера записи

Время (UTC): 2026-10-13 06:40:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 23 hours, 16 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         740         925           1         424        1165
Swap:           2047         203        1844
```
- нагрузка CPU (1/5/15 мин): 0.46 / 0.57 / 0.54

## Данные
- файлов: 2951, всего 892 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 115 | 14 МБ | 1 |
| bn_book | 115 | 1 МБ | 27 |
| bnf_agg | 115 | 21 МБ | 1 |
| bnf_book | 115 | 598 МБ | 0 |
| bnf_depth5 | 115 | 44 МБ | 1 |
| bnf_liq | 101 | 64 КБ | 4595 |
| bs_trade | 115 | 1 МБ | 1 |
| by_book1 | 115 | 45 МБ | 1 |
| by_liq | 97 | 58 КБ | 4595 |
| by_trade | 115 | 14 МБ | 1 |
| cb_ticker | 115 | 12 МБ | 1 |
| clock | 115 | 89 КБ | 45 |
| clock_pm | 115 | 89 КБ | 6 |
| events | 108 | 37 КБ | 313 |
| events_pm | 115 | 44 КБ | 500 |
| health_cex | 115 | 1 МБ | 3 |
| health_feeds | 115 | 4 МБ | 3 |
| health_pm | 115 | 1 МБ | 4 |
| kr_trade | 115 | 3 МБ | 7 |
| ok_trade | 115 | 19 МБ | 3 |
| pm_depth | 115 | 23 МБ | 0 |
| pm_rtt | 115 | 783 КБ | 2 |
| pm_top | 115 | 47 МБ | 0 |
| pm_trades | 115 | 34 МБ | 0 |
| rtds | 115 | 7 МБ | 0 |
| windows | 115 | 238 КБ | 173 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 51, всего 300
- Polymarket CLOB: TCP 5, TLS 44, всего 91
- Polymarket gamma: TCP 5, TLS 66, всего 80

## Последние строки журнала записи
```
06:39:44 [cex] Binance 18 сд. задержка p50/p90=146.1/146.9 мс | Coinbase 43 задержка p50=81.2 мс | смещение часов +18.1 мс | lag loop p99/max=2.2/2.2 мс
06:39:44 [cex] binance_futures 24 сд. p50=295.3 мс | bybit 8 сд. p50=115.1 мс | okx 14 сд. p50=155.8 мс | binance_futures_book 547 сд. p50=147.1 мс | binance_futures_depth 89 сд. p50=146.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 86 сд. p50=113.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=39.5 мс | bitstamp 1 сд. p50=51.8 мс
06:39:45 [pm] окно btc-updown-5m-1791873600 (2026-10-13 06:40:00 UTC): Bitcoin Up or Down - October 13, 2:40AM-2:45AM ET
06:39:52 [pm] T-  7.7s Up 1.00/n/a Down n/a/0.00 ptb=83609.0 | CLOB 1263 сообщ., задержка p50/p90=41.3/44.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791873592335 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=9.8/26.1 мс
06:39:54 [cex] Binance 52 сд. задержка p50/p90=142.1/142.9 мс | Coinbase 39 задержка p50=77.2 мс | смещение часов +18.1 мс | lag loop p99/max=2.1/2.2 мс
06:39:54 [cex] binance_futures 27 сд. p50=291.2 мс | bybit 5 сд. p50=111.8 мс | okx 15 сд. p50=151.3 мс | binance_futures_book 438 сд. p50=142.9 мс | binance_futures_depth 89 сд. p50=142.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 94 сд. p50=109.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=39.7 мс | bitstamp 3 сд. p50=56.2 мс
06:40:02 [pm] T-297.7s Up 0.32/0.33 Down 0.67/0.68 ptb=83624.9 | CLOB 3892 сообщ., задержка p50/p90=44.8/56.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791873602336 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=6.4/13.3 мс
06:40:04 [cex] Binance 116 сд. задержка p50/p90=142.7/152.5 мс | Coinbase 40 задержка p50=77.5 мс | смещение часов +18.1 мс | lag loop p99/max=3.6/5.1 мс
06:40:04 [cex] binance_futures 135 сд. p50=155.8 мс | bybit 161 сд. p50=121.8 мс | okx 90 сд. p50=166.2 мс | binance_futures_book 5904 сд. p50=143.1 мс | binance_futures_depth 92 сд. p50=142.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 192 сд. p50=109.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 36 сд. p50=43.4 мс | bitstamp 7 сд. p50=55.4 мс
06:40:12 [pm] T-287.7s Up 0.38/0.39 Down 0.61/0.62 ptb=83624.9 | CLOB 7882 сообщ., задержка p50/p90=46.4/65.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791873612337 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=1.6/1.9 мс
06:40:14 [cex] Binance 67 сд. задержка p50/p90=141.9/142.9 мс | Coinbase 27 задержка p50=77.7 мс | смещение часов +18.1 мс | lag loop p99/max=2.1/2.1 мс
06:40:14 [cex] binance_futures 59 сд. p50=291.2 мс | bybit 34 сд. p50=111.5 мс | okx 11 сд. p50=151.3 мс | binance_futures_book 728 сд. p50=143.0 мс | binance_futures_depth 96 сд. p50=142.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 122 сд. p50=109.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=36.6 мс | bitstamp 3 сд. p50=48.5 мс
06:40:22 [pm] T-277.7s Up 0.35/0.36 Down 0.64/0.65 ptb=83624.9 | CLOB 5678 сообщ., задержка p50/p90=50.9/75.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791873622338 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.6/2.2 мс
06:40:24 [cex] Binance 28 сд. задержка p50/p90=141.9/142.9 мс | Coinbase 28 задержка p50=80.3 мс | смещение часов +18.1 мс | lag loop p99/max=2.1/2.2 мс
06:40:24 [cex] binance_futures 50 сд. p50=278.2 мс | bybit 10 сд. p50=111.4 мс | okx 22 сд. p50=151.5 мс | binance_futures_book 1298 сд. p50=143.2 мс | binance_futures_depth 91 сд. p50=142.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 126 сд. p50=109.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=40.8 мс | bitstamp 2 сд. p50=47.0 мс
```

Представлено версией кода: 3861824; python 3.12.3
