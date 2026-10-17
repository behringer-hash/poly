# Состояние сервера записи

Время (UTC): 2026-10-17 22:09:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 14 hours, 45 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         818         959           2         415        1087
Swap:           2047         236        1811
```
- нагрузка CPU (1/5/15 мин): 0.10 / 0.18 / 0.23

## Данные
- файлов: 5618, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 227 | 30 МБ | 2 |
| bn_book | 227 | 3 МБ | 20 |
| bnf_agg | 227 | 45 МБ | 2 |
| bnf_book | 118 | 557 МБ | 390062 |
| bnf_depth5 | 118 | 41 МБ | 390138 |
| bnf_liq | 197 | 132 КБ | 303 |
| bs_trade | 118 | 1 МБ | 390058 |
| by_book1 | 227 | 95 МБ | 2 |
| by_liq | 201 | 115 КБ | 1431 |
| by_trade | 227 | 30 МБ | 2 |
| bys_book1 | 111 | 39 МБ | 2 |
| bys_trade | 111 | 15 МБ | 2 |
| cb_ticker | 227 | 28 МБ | 2 |
| clock | 227 | 174 КБ | 2 |
| clock_pm | 227 | 175 КБ | 31 |
| events | 215 | 71 КБ | 1014 |
| events_pm | 226 | 82 КБ | 2312 |
| health_cex | 227 | 2 МБ | 4 |
| health_feeds | 227 | 8 МБ | 4 |
| health_pm | 227 | 2 МБ | 4 |
| kr_trade | 118 | 3 МБ | 390058 |
| ok_trade | 226 | 40 МБ | 2 |
| pm_depth | 227 | 45 МБ | 0 |
| pm_rtt | 227 | 1 МБ | 4 |
| pm_top | 227 | 91 МБ | 0 |
| pm_trades | 227 | 66 МБ | 0 |
| rtds | 227 | 14 МБ | 0 |
| windows | 227 | 466 КБ | 295 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 58, всего 326
- Polymarket CLOB: TCP 5, TLS 44, всего 90
- Polymarket gamma: TCP 5, TLS 46, всего 63

## Последние строки журнала записи
```
22:08:42 [pm] T- 77.3s Up 0.64/0.65 Down 0.35/0.36 ptb=81131.0 | CLOB 8714 сообщ., задержка p50/p90=41.4/54.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792274922749 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.4/2.5 мс
22:08:44 [cex] Binance 62 сд. задержка p50/p90=160.3/160.8 мс | Coinbase 35 задержка p50=77.2 мс | смещение часов +20.1 мс | lag loop p99/max=2.1/2.6 мс
22:08:44 [cex] binance_futures 83 сд. p50=153.7 мс | bybit 112 сд. p50=125.5 мс | bybit_book 136 сд. p50=123.6 мс | bybit_spot 92 сд. p50=126.2 мс | bybit_spot_book 94 сд. p50=120.5 мс | okx 125 сд. p50=154.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:08:52 [pm] T- 67.2s Up 0.54/0.55 Down 0.45/0.46 ptb=81131.0 | CLOB 6324 сообщ., задержка p50/p90=42.8/55.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792274932750 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=2.1/2.2 мс
22:08:54 [cex] Binance 3 сд. задержка p50/p90=159.9/160.5 мс | Coinbase 30 задержка p50=76.1 мс | смещение часов +20.1 мс | lag loop p99/max=2.2/2.2 мс
22:08:54 [cex] binance_futures 22 сд. p50=302.2 мс | bybit 10 сд. p50=125.9 мс | bybit_book 86 сд. p50=123.6 мс | bybit_spot 7 сд. p50=125.4 мс | bybit_spot_book 65 сд. p50=120.4 мс | okx 9 сд. p50=153.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:09:02 [pm] T- 57.2s Up 0.50/0.51 Down 0.49/0.50 ptb=81131.0 | CLOB 6602 сообщ., задержка p50/p90=39.6/46.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792274942751 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=1.9/2.7 мс
22:09:04 [cex] Binance 5 сд. задержка p50/p90=159.6/160.6 мс | Coinbase 32 задержка p50=75.7 мс | смещение часов +20.1 мс | lag loop p99/max=2.2/2.4 мс
22:09:04 [cex] binance_futures 21 сд. p50=302.3 мс | bybit 28 сд. p50=125.3 мс | bybit_book 101 сд. p50=123.6 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 31 сд. p50=120.5 мс | okx 28 сд. p50=153.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:09:12 [pm] T- 47.2s Up 0.69/0.70 Down 0.30/0.31 ptb=81131.0 | CLOB 10309 сообщ., задержка p50/p90=38.6/41.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792274952753 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.0 мс | lag loop p99/max=1.5/1.6 мс
22:09:14 [cex] Binance 46 сд. задержка p50/p90=159.9/160.2 мс | Coinbase 44 задержка p50=76.8 мс | смещение часов +20.1 мс | lag loop p99/max=2.0/2.1 мс
22:09:14 [cex] binance_futures 43 сд. p50=156.2 мс | bybit 108 сд. p50=129.4 мс | bybit_book 206 сд. p50=123.6 мс | bybit_spot 143 сд. p50=129.1 мс | bybit_spot_book 90 сд. p50=120.5 мс | okx 26 сд. p50=153.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:09:22 [pm] T- 37.2s Up 0.88/0.89 Down 0.11/0.12 ptb=81131.0 | CLOB 9049 сообщ., задержка p50/p90=39.0/42.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792274962754 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=1.1/1.2 мс
22:09:24 [cex] Binance 4 сд. задержка p50/p90=160.5/160.5 мс | Coinbase 33 задержка p50=77.1 мс | смещение часов +20.1 мс | lag loop p99/max=2.1/2.1 мс
22:09:24 [cex] binance_futures 26 сд. p50=302.5 мс | bybit 46 сд. p50=126.1 мс | bybit_book 105 сд. p50=123.6 мс | bybit_spot 1 сд. p50=125.6 мс | bybit_spot_book 33 сд. p50=120.5 мс | okx 33 сд. p50=153.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: b24b4e3; python 3.12.3
