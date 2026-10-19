# Состояние сервера записи

Время (UTC): 2026-10-19 09:15:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 5 days, 1 hour, 51 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         667         613           1         804        1238
Swap:           2047         252        1795
```
- нагрузка CPU (1/5/15 мин): 0.40 / 0.28 / 0.28

## Данные
- файлов: 6455, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 262 | 33 МБ | 2 |
| bn_book | 262 | 3 МБ | 6 |
| bnf_agg | 262 | 51 МБ | 2 |
| bnf_book | 118 | 557 МБ | 516412 |
| bnf_depth5 | 118 | 41 МБ | 516488 |
| bnf_liq | 228 | 149 КБ | 872 |
| bs_trade | 118 | 1 МБ | 516408 |
| by_book1 | 262 | 107 МБ | 2 |
| by_liq | 235 | 120 КБ | 495 |
| by_trade | 262 | 33 МБ | 2 |
| bys_book1 | 146 | 49 МБ | 2 |
| bys_trade | 146 | 20 МБ | 2 |
| cb_ticker | 262 | 31 МБ | 2 |
| clock | 262 | 202 КБ | 6 |
| clock_pm | 262 | 202 КБ | 27 |
| events | 251 | 80 КБ | 260 |
| events_pm | 262 | 94 КБ | 297 |
| health_cex | 262 | 3 МБ | 10 |
| health_feeds | 262 | 9 МБ | 10 |
| health_pm | 262 | 3 МБ | 5 |
| kr_trade | 118 | 3 МБ | 516408 |
| ok_trade | 261 | 44 МБ | 2 |
| pm_depth | 262 | 52 МБ | 1 |
| pm_rtt | 262 | 2 МБ | 1 |
| pm_top | 262 | 106 МБ | 1 |
| pm_trades | 262 | 75 МБ | 1 |
| rtds | 262 | 17 МБ | 1 |
| windows | 262 | 539 КБ | 104 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 63, всего 314
- Polymarket CLOB: TCP 5, TLS 44, всего 92
- Polymarket gamma: TCP 6, TLS 44, всего 57

## Последние строки журнала записи
```
09:14:38 [cex] Binance 16 сд. задержка p50/p90=143.2/144.0 мс | Coinbase 52 задержка p50=76.4 мс | смещение часов +19.0 мс | lag loop p99/max=2.0/2.1 мс
09:14:38 [cex] binance_futures 218 сд. p50=148.1 мс | bybit 89 сд. p50=113.1 мс | bybit_book 119 сд. p50=111.2 мс | bybit_spot 102 сд. p50=113.0 мс | bybit_spot_book 117 сд. p50=110.7 мс | okx 83 сд. p50=157.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:14:41 [pm] T- 18.4s Up 0.99/n/a Down n/a/0.01 ptb=82676.5 | CLOB 560 сообщ., задержка p50/p90=41.1/42.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792401281647 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.9 мс | lag loop p99/max=2.2/2.2 мс
09:14:45 [pm] окно btc-updown-5m-1792401300 (2026-10-19 09:15:00 UTC): Bitcoin Up or Down - October 19, 5:15AM-5:20AM ET
09:14:48 [cex] Binance 18 сд. задержка p50/p90=143.2/144.2 мс | Coinbase 28 задержка p50=76.2 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/2.2 мс
09:14:48 [cex] binance_futures 80 сд. p50=146.2 мс | bybit 51 сд. p50=113.2 мс | bybit_book 148 сд. p50=111.2 мс | bybit_spot 11 сд. p50=113.4 мс | bybit_spot_book 57 сд. p50=110.7 мс | okx 44 сд. p50=157.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:14:51 [pm] T-  8.4s Up 0.99/n/a Down n/a/0.01 ptb=82676.5 | CLOB 1852 сообщ., задержка p50/p90=42.7/45.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792401291649 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.9 мс | lag loop p99/max=2.0/28.3 мс
09:14:58 [cex] Binance 37 сд. задержка p50/p90=143.2/144.3 мс | Coinbase 33 задержка p50=75.3 мс | смещение часов +19.0 мс | lag loop p99/max=2.0/2.1 мс
09:14:58 [cex] binance_futures 33 сд. p50=292.5 мс | bybit 70 сд. p50=112.0 мс | bybit_book 85 сд. p50=111.2 мс | bybit_spot 295 сд. p50=113.0 мс | bybit_spot_book 136 сд. p50=110.8 мс | okx 54 сд. p50=157.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:15:01 [pm] T-298.3s Up 0.43/0.44 Down 0.56/0.57 ptb=82740.9 | CLOB 2614 сообщ., задержка p50/p90=40.5/55.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792401301654 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.9 мс | lag loop p99/max=2.0/2.6 мс
09:15:08 [cex] Binance 86 сд. задержка p50/p90=143.2/144.1 мс | Coinbase 33 задержка p50=76.4 мс | смещение часов +19.0 мс | lag loop p99/max=3.3/3.9 мс
09:15:08 [cex] binance_futures 84 сд. p50=145.8 мс | bybit 51 сд. p50=112.4 мс | bybit_book 92 сд. p50=111.3 мс | bybit_spot 75 сд. p50=113.3 мс | bybit_spot_book 70 сд. p50=110.9 мс | okx 61 сд. p50=157.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:15:11 [pm] T-288.3s Up 0.36/0.37 Down 0.63/0.64 ptb=82740.9 | CLOB 5956 сообщ., задержка p50/p90=40.5/42.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792401311655 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.8 мс | lag loop p99/max=6.1/8.7 мс
09:15:18 [cex] Binance 88 сд. задержка p50/p90=144.8/147.7 мс | Coinbase 28 задержка p50=77.5 мс | смещение часов +20.7 мс | lag loop p99/max=2.3/2.3 мс
09:15:18 [cex] binance_futures 85 сд. p50=149.2 мс | bybit 171 сд. p50=113.9 мс | bybit_book 187 сд. p50=112.8 мс | bybit_spot 277 сд. p50=115.2 мс | bybit_spot_book 111 сд. p50=112.3 мс | okx 60 сд. p50=159.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
