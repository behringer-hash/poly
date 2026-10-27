# Состояние сервера записи

Время (UTC): 2026-10-27 22:35:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 6 days, 15 hours, 12 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         578         807           2         696        1328
Swap:           2047         282        1765
```
- нагрузка CPU (1/5/15 мин): 0.47 / 0.23 / 0.19

## Данные
- файлов: 5815, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 2 |
| bn_book | 242 | 3 МБ | 4 |
| bnf_agg | 242 | 51 МБ | 2 |
| bnf_book | 46 | 352 МБ | 1 |
| bnf_depth5 | 12 | 5 МБ | 1255728 |
| bnf_liq | 214 | 142 КБ | 2086 |
| bs_trade | 12 | 239 КБ | 1255648 |
| by_book1 | 242 | 111 МБ | 2 |
| by_liq | 226 | 104 КБ | 1663 |
| by_trade | 242 | 35 МБ | 2 |
| bys_book1 | 232 | 77 МБ | 2 |
| bys_trade | 232 | 31 МБ | 2 |
| cb_ticker | 242 | 33 МБ | 2 |
| clock | 242 | 188 КБ | 52 |
| clock_pm | 242 | 188 КБ | 9 |
| events | 233 | 74 КБ | 262 |
| events_pm | 241 | 84 КБ | 175 |
| health_cex | 242 | 2 МБ | 10 |
| health_feeds | 242 | 7 МБ | 10 |
| health_pm | 242 | 3 МБ | 1 |
| kr_trade | 12 | 417 КБ | 1255648 |
| ok_trade | 241 | 44 МБ | 2 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 3 |
| pm_top | 242 | 102 МБ | 1 |
| pm_trades | 242 | 71 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 500 КБ | 84 |

Дни с данными: 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 290
- Polymarket CLOB: TCP 6, TLS 40, всего 88
- Polymarket gamma: TCP 4, TLS 41, всего 47

## Последние строки журнала записи
```
22:35:16 [pm] T-283.8s Up 0.23/0.24 Down 0.76/0.77 ptb=80832.5 | CLOB 7080 сообщ., задержка p50/p90=43.8/53.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793140516210 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=1.3/1.6 мс
22:35:17 [cex] Binance 96 сд. задержка p50/p90=145.6/148.1 мс | Coinbase 44 задержка p50=142.5 мс | смещение часов +22.1 мс | lag loop p99/max=1.9/1.9 мс
22:35:17 [cex] binance_futures 118 сд. p50=150.2 мс | bybit 170 сд. p50=114.7 мс | bybit_book 170 сд. p50=111.8 мс | bybit_spot 164 сд. p50=115.8 мс | bybit_spot_book 99 сд. p50=111.8 мс | okx 139 сд. p50=159.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3896 сд. p50=146.8 мс
22:35:26 [pm] T-273.8s Up 0.18/0.19 Down 0.81/0.82 ptb=80832.5 | CLOB 7979 сообщ., задержка p50/p90=44.0/52.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793140526211 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=1.7/1.9 мс
22:35:27 [cex] Binance 180 сд. задержка p50/p90=145.7/151.2 мс | Coinbase 26 задержка p50=91.9 мс | смещение часов +22.1 мс | lag loop p99/max=2.0/2.1 мс
22:35:27 [cex] binance_futures 46 сд. p50=294.4 мс | bybit 91 сд. p50=114.4 мс | bybit_book 172 сд. p50=111.8 мс | bybit_spot 92 сд. p50=114.8 мс | bybit_spot_book 96 сд. p50=111.8 мс | okx 51 сд. p50=158.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2233 сд. p50=146.3 мс
22:35:36 [pm] T-263.8s Up 0.17/0.18 Down 0.82/0.83 ptb=80832.5 | CLOB 4383 сообщ., задержка p50/p90=42.7/100.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793140536213 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.0/2.1 мс
22:35:37 [cex] Binance 16 сд. задержка p50/p90=144.9/146.0 мс | Coinbase 7 задержка p50=89.8 мс | смещение часов +22.1 мс | lag loop p99/max=2.1/2.2 мс
22:35:37 [cex] binance_futures 22 сд. p50=294.6 мс | bybit 4 сд. p50=113.9 мс | bybit_book 171 сд. p50=111.8 мс | bybit_spot 2 сд. p50=114.2 мс | bybit_spot_book 39 сд. p50=111.9 мс | okx 14 сд. p50=155.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 921 сд. p50=145.6 мс
22:35:46 [pm] T-253.8s Up 0.08/0.09 Down 0.91/0.92 ptb=80832.5 | CLOB 5453 сообщ., задержка p50/p90=47.3/101.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793140546215 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=1.3/2.2 мс
22:35:47 [cex] Binance 194 сд. задержка p50/p90=149.6/162.7 мс | Coinbase 83 задержка p50=279.4 мс | смещение часов +22.1 мс | lag loop p99/max=2.1/2.7 мс
22:35:47 [cex] binance_futures 339 сд. p50=150.4 мс | bybit 477 сд. p50=118.3 мс | bybit_book 154 сд. p50=111.9 мс | bybit_spot 201 сд. p50=116.2 мс | bybit_spot_book 80 сд. p50=112.1 мс | okx 335 сд. p50=329.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3109 сд. p50=188.6 мс
22:35:56 [pm] T-243.8s Up 0.03/0.04 Down 0.96/0.97 ptb=80832.5 | CLOB 4241 сообщ., задержка p50/p90=46.9/57.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793140556216 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=1.9/1.9 мс
22:35:57 [cex] Binance 531 сд. задержка p50/p90=151.1/161.6 мс | Coinbase 112 задержка p50=105.9 мс | смещение часов +22.1 мс | lag loop p99/max=6.9/6.9 мс
22:35:57 [cex] binance_futures 681 сд. p50=150.8 мс | bybit 819 сд. p50=116.0 мс | bybit_book 270 сд. p50=111.8 мс | bybit_spot 523 сд. p50=114.7 мс | bybit_spot_book 190 сд. p50=111.9 мс | okx 768 сд. p50=415.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 7135 сд. p50=146.4 мс
```

Представлено версией кода: adb4c8b; python 3.12.3
