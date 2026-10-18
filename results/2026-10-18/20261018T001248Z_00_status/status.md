# Состояние сервера записи

Время (UTC): 2026-10-18 00:12:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 16 hours, 48 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         839         907           2         446        1066
Swap:           2047         236        1811
```
- нагрузка CPU (1/5/15 мин): 0.15 / 0.21 / 0.19

## Данные
- файлов: 5667, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 229 | 30 МБ | 1 |
| bn_book | 229 | 3 МБ | 185 |
| bnf_agg | 229 | 45 МБ | 1 |
| bnf_book | 118 | 557 МБ | 397462 |
| bnf_depth5 | 118 | 41 МБ | 397538 |
| bnf_liq | 198 | 132 КБ | 943 |
| bs_trade | 118 | 1 МБ | 397458 |
| by_book1 | 229 | 95 МБ | 1 |
| by_liq | 203 | 108 КБ | 943 |
| by_trade | 229 | 29 МБ | 1 |
| bys_book1 | 113 | 39 МБ | 1 |
| bys_trade | 113 | 15 МБ | 5 |
| cb_ticker | 229 | 28 МБ | 1 |
| clock | 229 | 176 КБ | 12 |
| clock_pm | 229 | 176 КБ | 41 |
| events | 218 | 71 КБ | 330 |
| events_pm | 229 | 83 КБ | 405 |
| health_cex | 229 | 2 МБ | 3 |
| health_feeds | 229 | 8 МБ | 3 |
| health_pm | 229 | 2 МБ | 4 |
| kr_trade | 118 | 3 МБ | 397458 |
| ok_trade | 228 | 39 МБ | 3 |
| pm_depth | 229 | 45 МБ | 0 |
| pm_rtt | 229 | 1 МБ | 0 |
| pm_top | 229 | 92 МБ | 0 |
| pm_trades | 229 | 66 МБ | 0 |
| rtds | 229 | 15 МБ | 0 |
| windows | 229 | 471 КБ | 15 |

Дни с данными: 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 34, всего 306
- Polymarket CLOB: TCP 5, TLS 37, всего 80
- Polymarket gamma: TCP 5, TLS 36, всего 47

## Последние строки журнала записи
```
00:12:03 [pm] T-176.2s Up 0.39/0.40 Down 0.60/0.61 ptb=81302.1 | CLOB 2656 сообщ., задержка p50/p90=38.2/42.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792282323818 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.0/3.4 мс
00:12:04 [cex] Binance 8 сд. задержка p50/p90=159.4/159.4 мс | Coinbase 11 задержка p50=78.7 мс | смещение часов +19.9 мс | lag loop p99/max=2.1/2.2 мс
00:12:04 [cex] binance_futures 18 сд. p50=302.3 мс | bybit 22 сд. p50=124.7 мс | bybit_book 58 сд. p50=123.2 мс | bybit_spot 1 сд. p50=124.9 мс | bybit_spot_book 26 сд. p50=120.4 мс | okx 16 сд. p50=153.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:12:13 [pm] T-166.2s Up 0.38/0.39 Down 0.61/0.62 ptb=81302.1 | CLOB 3107 сообщ., задержка p50/p90=41.2/54.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792282333819 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.8/1.9 мс
00:12:14 [cex] Binance 47 сд. задержка p50/p90=159.5/160.3 мс | Coinbase 13 задержка p50=76.7 мс | смещение часов +19.9 мс | lag loop p99/max=2.1/2.3 мс
00:12:14 [cex] binance_futures 19 сд. p50=302.1 мс | bybit 19 сд. p50=125.4 мс | bybit_book 114 сд. p50=123.1 мс | bybit_spot 30 сд. p50=126.8 мс | bybit_spot_book 30 сд. p50=120.5 мс | okx 11 сд. p50=153.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:12:23 [pm] T-156.2s Up 0.38/0.39 Down 0.61/0.62 ptb=81302.1 | CLOB 3291 сообщ., задержка p50/p90=40.0/45.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792282343821 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.9 мс | lag loop p99/max=1.9/2.0 мс
00:12:24 [cex] Binance 21 сд. задержка p50/p90=159.4/160.3 мс | Coinbase 19 задержка p50=75.5 мс | смещение часов +19.9 мс | lag loop p99/max=2.0/2.2 мс
00:12:24 [cex] binance_futures 21 сд. p50=301.9 мс | bybit 3 сд. p50=125.6 мс | bybit_book 47 сд. p50=123.2 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 23 сд. p50=120.2 мс | okx 5 сд. p50=153.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:12:33 [pm] T-146.2s Up 0.39/0.40 Down 0.60/0.61 ptb=81302.1 | CLOB 4129 сообщ., задержка p50/p90=40.0/43.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792282353823 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.9 мс | lag loop p99/max=1.3/1.9 мс
00:12:34 [cex] Binance 21 сд. задержка p50/p90=159.4/159.5 мс | Coinbase 10 задержка p50=78.0 мс | смещение часов +19.9 мс | lag loop p99/max=2.1/2.2 мс
00:12:34 [cex] binance_futures 16 сд. p50=301.9 мс | bybit 33 сд. p50=125.3 мс | bybit_book 76 сд. p50=123.1 мс | bybit_spot 1 сд. p50=125.3 мс | bybit_spot_book 19 сд. p50=120.3 мс | okx 8 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:12:43 [pm] T-136.2s Up 0.40/0.41 Down 0.59/0.60 ptb=81302.1 | CLOB 4775 сообщ., задержка p50/p90=40.2/49.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792282363824 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.4/2.0 мс
00:12:44 [cex] Binance 7 сд. задержка p50/p90=162.0/162.1 мс | Coinbase 17 задержка p50=78.5 мс | смещение часов +22.6 мс | lag loop p99/max=2.0/2.0 мс
00:12:44 [cex] binance_futures 15 сд. p50=304.6 мс | bybit 14 сд. p50=127.9 мс | bybit_book 91 сд. p50=125.8 мс | bybit_spot 2 сд. p50=128.0 мс | bybit_spot_book 50 сд. p50=123.0 мс | okx 10 сд. p50=156.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: b24b4e3; python 3.12.3
