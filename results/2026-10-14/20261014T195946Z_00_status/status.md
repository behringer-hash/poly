# Состояние сервера записи

Время (UTC): 2026-10-14 19:59:46

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 12 hours, 35 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         583         395           2        1120        1322
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.36 / 0.19 / 0.14

## Данные
- файлов: 3841, всего 967 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 152 | 20 МБ | 1 |
| bn_book | 152 | 2 МБ | 13 |
| bnf_agg | 152 | 30 МБ | 1 |
| bnf_book | 118 | 557 МБ | 123080 |
| bnf_depth5 | 118 | 41 МБ | 123157 |
| bnf_liq | 135 | 87 КБ | 231 |
| bs_trade | 118 | 1 МБ | 123076 |
| by_book1 | 152 | 65 МБ | 1 |
| by_liq | 132 | 71 КБ | 2546 |
| by_trade | 152 | 20 МБ | 1 |
| bys_book1 | 36 | 14 МБ | 1 |
| bys_trade | 36 | 7 МБ | 1 |
| cb_ticker | 152 | 19 МБ | 1 |
| clock | 152 | 118 КБ | 5 |
| clock_pm | 152 | 119 КБ | 3 |
| events | 143 | 48 КБ | 262 |
| events_pm | 152 | 55 КБ | 194 |
| health_cex | 152 | 2 МБ | 5 |
| health_feeds | 152 | 6 МБ | 5 |
| health_pm | 152 | 2 МБ | 3 |
| kr_trade | 118 | 3 МБ | 123076 |
| ok_trade | 151 | 27 МБ | 3 |
| pm_depth | 152 | 31 МБ | 1 |
| pm_rtt | 152 | 1 МБ | 3 |
| pm_top | 152 | 63 МБ | 1 |
| pm_trades | 152 | 45 МБ | 1 |
| rtds | 152 | 10 МБ | 1 |
| windows | 152 | 316 КБ | 432 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 37, всего 287
- Polymarket CLOB: TCP 6, TLS 40, всего 83
- Polymarket gamma: TCP 5, TLS 36, всего 48

## Последние строки журнала записи
```
19:58:59 [cex] binance_futures 26 сд. p50=293.1 мс | bybit 245 сд. p50=115.5 мс | bybit_book 133 сд. p50=110.1 мс | bybit_spot 237 сд. p50=112.5 мс | bybit_spot_book 95 сд. p50=110.1 мс | okx 24 сд. p50=163.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:59:02 [pm] T- 57.3s Up n/a/0.01 Down 0.99/n/a ptb=81720.8 | CLOB 5820 сообщ., задержка p50/p90=36.7/39.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792007942663 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.1 мс | lag loop p99/max=2.0/5.0 мс
19:59:09 [cex] Binance 226 сд. задержка p50/p90=142.9/143.7 мс | Coinbase 137 задержка p50=80.0 мс | смещение часов +18.6 мс | lag loop p99/max=2.3/3.3 мс
19:59:09 [cex] binance_futures 285 сд. p50=145.1 мс | bybit 397 сд. p50=112.8 мс | bybit_book 379 сд. p50=110.2 мс | bybit_spot 288 сд. p50=113.7 мс | bybit_spot_book 211 сд. p50=110.1 мс | okx 249 сд. p50=162.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:59:12 [pm] T- 47.3s Up n/a/0.01 Down 0.99/n/a ptb=81720.8 | CLOB 1602 сообщ., задержка p50/p90=36.6/37.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792007952665 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=1.9/2.2 мс
19:59:19 [cex] Binance 105 сд. задержка p50/p90=142.8/143.6 мс | Coinbase 78 задержка p50=77.4 мс | смещение часов +18.6 мс | lag loop p99/max=2.1/2.1 мс
19:59:19 [cex] binance_futures 68 сд. p50=145.5 мс | bybit 132 сд. p50=112.8 мс | bybit_book 248 сд. p50=110.2 мс | bybit_spot 112 сд. p50=112.4 мс | bybit_spot_book 140 сд. p50=110.2 мс | okx 76 сд. p50=162.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:59:22 [pm] T- 37.3s Up n/a/0.01 Down 0.99/n/a ptb=81720.8 | CLOB 1117 сообщ., задержка p50/p90=36.5/37.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792007962667 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=2.1/2.3 мс
19:59:29 [cex] Binance 42 сд. задержка p50/p90=142.6/142.9 мс | Coinbase 95 задержка p50=77.2 мс | смещение часов +18.6 мс | lag loop p99/max=2.2/2.2 мс
19:59:29 [cex] binance_futures 28 сд. p50=293.2 мс | bybit 41 сд. p50=112.6 мс | bybit_book 164 сд. p50=110.2 мс | bybit_spot 104 сд. p50=112.5 мс | bybit_spot_book 87 сд. p50=110.3 мс | okx 21 сд. p50=162.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:59:32 [pm] T- 27.3s Up n/a/0.01 Down 0.99/n/a ptb=81720.8 | CLOB 993 сообщ., задержка p50/p90=36.7/38.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792007972668 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=2.0/2.0 мс
19:59:39 [cex] Binance 69 сд. задержка p50/p90=142.7/143.8 мс | Coinbase 79 задержка p50=76.5 мс | смещение часов +18.9 мс | lag loop p99/max=2.1/2.1 мс
19:59:39 [cex] binance_futures 57 сд. p50=176.4 мс | bybit 47 сд. p50=112.7 мс | bybit_book 245 сд. p50=110.2 мс | bybit_spot 121 сд. p50=112.5 мс | bybit_spot_book 102 сд. p50=110.2 мс | okx 34 сд. p50=162.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:59:42 [pm] T- 17.3s Up n/a/0.01 Down 0.99/n/a ptb=81720.8 | CLOB 470 сообщ., задержка p50/p90=36.6/37.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792007982669 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=2.1/2.2 мс
19:59:45 [pm] окно btc-updown-5m-1792008000 (2026-10-14 20:00:00 UTC): Bitcoin Up or Down - October 14, 4:00PM-4:05PM ET
```

Представлено версией кода: ec1316a; python 3.12.3
