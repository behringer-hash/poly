# Состояние сервера записи

Время (UTC): 2026-10-15 19:38:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 12 hours, 15 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         691         342           2        1122        1214
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.22 / 0.15 / 0.10

## Данные
- файлов: 4414, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 176 | 25 МБ | 0 |
| bn_book | 176 | 2 МБ | 0 |
| bnf_agg | 176 | 38 МБ | 0 |
| bnf_book | 118 | 557 МБ | 208232 |
| bnf_depth5 | 118 | 41 МБ | 208308 |
| bnf_liq | 158 | 112 КБ | 1042 |
| bs_trade | 118 | 1 МБ | 208228 |
| by_book1 | 176 | 79 МБ | 0 |
| by_liq | 156 | 92 КБ | 636 |
| by_trade | 176 | 25 МБ | 0 |
| bys_book1 | 60 | 25 МБ | 0 |
| bys_trade | 60 | 11 МБ | 0 |
| cb_ticker | 176 | 22 МБ | 0 |
| clock | 176 | 136 КБ | 0 |
| clock_pm | 176 | 136 КБ | 61 |
| events | 165 | 53 КБ | 431 |
| events_pm | 176 | 63 КБ | 1277 |
| health_cex | 176 | 2 МБ | 7 |
| health_feeds | 176 | 6 МБ | 7 |
| health_pm | 176 | 2 МБ | 3 |
| kr_trade | 118 | 3 МБ | 208228 |
| ok_trade | 175 | 34 МБ | 0 |
| pm_depth | 176 | 36 МБ | 1 |
| pm_rtt | 176 | 1 МБ | 1 |
| pm_top | 176 | 73 МБ | 1 |
| pm_trades | 176 | 53 МБ | 1 |
| rtds | 176 | 11 МБ | 1 |
| windows | 176 | 364 КБ | 144 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 43, всего 307
- Polymarket CLOB: TCP 8, TLS 53, всего 129
- Polymarket gamma: TCP 5, TLS 41, всего 58

## Последние строки журнала записи
```
19:38:10 [cex] Binance 24 сд. задержка p50/p90=142.3/143.5 мс | Coinbase 55 задержка p50=82.0 мс | смещение часов +19.0 мс | lag loop p99/max=1.9/1.9 мс
19:38:10 [cex] binance_futures 94 сд. p50=143.8 мс | bybit 144 сд. p50=111.8 мс | bybit_book 190 сд. p50=109.2 мс | bybit_spot 162 сд. p50=111.9 мс | bybit_spot_book 136 сд. p50=109.4 мс | okx 115 сд. p50=157.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:38:14 [pm] T-105.2s Up 0.04/0.05 Down 0.95/0.96 ptb=82346.1 | CLOB 2550 сообщ., задержка p50/p90=41.0/43.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792093094755 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.0 мс | lag loop p99/max=2.0/2.2 мс
19:38:20 [cex] Binance 26 сд. задержка p50/p90=142.3/143.1 мс | Coinbase 39 задержка p50=81.8 мс | смещение часов +19.0 мс | lag loop p99/max=2.0/2.0 мс
19:38:20 [cex] binance_futures 42 сд. p50=291.1 мс | bybit 7 сд. p50=111.1 мс | bybit_book 122 сд. p50=109.2 мс | bybit_spot 7 сд. p50=111.4 мс | bybit_spot_book 48 сд. p50=109.5 мс | okx 43 сд. p50=157.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:38:24 [pm] T- 95.2s Up 0.05/0.06 Down 0.94/0.95 ptb=82346.1 | CLOB 3089 сообщ., задержка p50/p90=41.5/45.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792093104756 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=1.9/2.1 мс
19:38:30 [cex] Binance 101 сд. задержка p50/p90=143.4/143.9 мс | Coinbase 123 задержка p50=195.8 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/2.1 мс
19:38:30 [cex] binance_futures 91 сд. p50=143.9 мс | bybit 99 сд. p50=111.8 мс | bybit_book 141 сд. p50=109.2 мс | bybit_spot 137 сд. p50=112.5 мс | bybit_spot_book 104 сд. p50=109.4 мс | okx 67 сд. p50=157.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:38:34 [pm] T- 85.2s Up 0.01/0.02 Down 0.98/0.99 ptb=82346.1 | CLOB 2743 сообщ., задержка p50/p90=42.8/55.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792093114757 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=1.9/2.0 мс
19:38:40 [cex] Binance 21 сд. задержка p50/p90=143.1/143.4 мс | Coinbase 89 задержка p50=82.3 мс | смещение часов +19.0 мс | lag loop p99/max=1.9/2.1 мс
19:38:40 [cex] binance_futures 81 сд. p50=144.1 мс | bybit 138 сд. p50=113.2 мс | bybit_book 146 сд. p50=109.3 мс | bybit_spot 113 сд. p50=113.2 мс | bybit_spot_book 84 сд. p50=109.5 мс | okx 63 сд. p50=157.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:38:44 [pm] T- 75.2s Up 0.04/0.05 Down 0.95/0.96 ptb=82346.1 | CLOB 2459 сообщ., задержка p50/p90=42.3/64.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792093124758 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=2.1/2.2 мс
19:38:50 [cex] Binance 115 сд. задержка p50/p90=142.6/143.6 мс | Coinbase 61 задержка p50=81.8 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/2.1 мс
19:38:50 [cex] binance_futures 147 сд. p50=144.0 мс | bybit 115 сд. p50=111.3 мс | bybit_book 203 сд. p50=109.2 мс | bybit_spot 96 сд. p50=112.0 мс | bybit_spot_book 97 сд. p50=109.4 мс | okx 148 сд. p50=157.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:38:54 [pm] T- 65.2s Up 0.05/0.06 Down 0.94/0.95 ptb=82346.1 | CLOB 3214 сообщ., задержка p50/p90=41.1/43.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792093134760 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=1.9/2.1 мс
```

Представлено версией кода: ec1316a; python 3.12.3
