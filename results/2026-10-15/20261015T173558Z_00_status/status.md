# Состояние сервера записи

Время (UTC): 2026-10-15 17:35:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 10 hours, 12 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         689         350           2        1115        1216
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.39 / 0.28 / 0.22

## Данные
- файлов: 4366, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 174 | 25 МБ | 1 |
| bn_book | 174 | 2 МБ | 5 |
| bnf_agg | 174 | 39 МБ | 1 |
| bnf_book | 118 | 557 МБ | 200852 |
| bnf_depth5 | 118 | 41 МБ | 200928 |
| bnf_liq | 156 | 112 КБ | 825 |
| bs_trade | 118 | 1 МБ | 200848 |
| by_book1 | 174 | 79 МБ | 1 |
| by_liq | 154 | 93 КБ | 1127 |
| by_trade | 174 | 26 МБ | 1 |
| bys_book1 | 58 | 25 МБ | 1 |
| bys_trade | 58 | 11 МБ | 3 |
| cb_ticker | 174 | 22 МБ | 1 |
| clock | 174 | 135 КБ | 58 |
| clock_pm | 174 | 135 КБ | 56 |
| events | 163 | 52 КБ | 216 |
| events_pm | 174 | 62 КБ | 548 |
| health_cex | 174 | 2 МБ | 7 |
| health_feeds | 174 | 6 МБ | 7 |
| health_pm | 174 | 2 МБ | 4 |
| kr_trade | 118 | 3 МБ | 200848 |
| ok_trade | 173 | 34 МБ | 1 |
| pm_depth | 174 | 35 МБ | 2 |
| pm_rtt | 174 | 1 МБ | 2 |
| pm_top | 174 | 72 МБ | 2 |
| pm_trades | 174 | 52 МБ | 2 |
| rtds | 174 | 11 МБ | 2 |
| windows | 174 | 360 КБ | 84 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 288
- Polymarket CLOB: TCP 5, TLS 39, всего 84
- Polymarket gamma: TCP 6, TLS 39, всего 53

## Последние строки журнала записи
```
17:35:10 [cex] Binance 22 сд. задержка p50/p90=141.6/142.7 мс | Coinbase 29 задержка p50=81.0 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/3.3 мс
17:35:10 [cex] binance_futures 27 сд. p50=290.7 мс | bybit 14 сд. p50=111.4 мс | bybit_book 114 сд. p50=109.4 мс | bybit_spot 10 сд. p50=111.7 мс | bybit_spot_book 41 сд. p50=108.7 мс | okx 20 сд. p50=156.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:35:13 [pm] T-286.3s Up 0.53/0.54 Down 0.46/0.47 ptb=82285.8 | CLOB 6059 сообщ., задержка p50/p90=42.6/189.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792085713745 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=50.3 мс | lag loop p99/max=1.5/1.5 мс
17:35:20 [cex] Binance 17 сд. задержка p50/p90=141.7/142.4 мс | Coinbase 58 задержка p50=82.5 мс | смещение часов +18.7 мс | lag loop p99/max=2.0/2.1 мс
17:35:20 [cex] binance_futures 81 сд. p50=142.9 мс | bybit 46 сд. p50=111.4 мс | bybit_book 172 сд. p50=109.3 мс | bybit_spot 86 сд. p50=111.6 мс | bybit_spot_book 80 сд. p50=108.7 мс | okx 39 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:35:23 [pm] T-276.3s Up 0.57/0.58 Down 0.42/0.43 ptb=82285.8 | CLOB 6168 сообщ., задержка p50/p90=48.8/670.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792085723747 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=50.2 мс | lag loop p99/max=2.1/2.1 мс
17:35:30 [cex] Binance 17 сд. задержка p50/p90=141.6/142.5 мс | Coinbase 41 задержка p50=81.3 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/2.2 мс
17:35:30 [cex] binance_futures 46 сд. p50=249.4 мс | bybit 108 сд. p50=111.8 мс | bybit_book 155 сд. p50=109.3 мс | bybit_spot 68 сд. p50=112.0 мс | bybit_spot_book 75 сд. p50=108.7 мс | okx 44 сд. p50=157.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:35:33 [pm] T-266.3s Up 0.66/0.67 Down 0.33/0.34 ptb=82285.8 | CLOB 8228 сообщ., задержка p50/p90=309.4/475.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792085733749 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=50.3 мс | lag loop p99/max=2.1/2.3 мс
17:35:40 [cex] Binance 174 сд. задержка p50/p90=141.9/142.9 мс | Coinbase 76 задержка p50=81.3 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/2.2 мс
17:35:40 [cex] binance_futures 200 сд. p50=142.8 мс | bybit 122 сд. p50=111.8 мс | bybit_book 218 сд. p50=109.3 мс | bybit_spot 124 сд. p50=111.5 мс | bybit_spot_book 129 сд. p50=108.6 мс | okx 197 сд. p50=158.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:35:43 [pm] T-256.2s Up 0.73/0.74 Down 0.26/0.27 ptb=82285.8 | CLOB 8130 сообщ., задержка p50/p90=52.7/558.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792085743750 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=50.4 мс | lag loop p99/max=2.1/2.4 мс
17:35:50 [cex] Binance 15 сд. задержка p50/p90=141.5/141.7 мс | Coinbase 24 задержка p50=81.1 мс | смещение часов +18.7 мс | lag loop p99/max=2.0/2.1 мс
17:35:50 [cex] binance_futures 35 сд. p50=290.7 мс | bybit 22 сд. p50=111.2 мс | bybit_book 107 сд. p50=109.3 мс | bybit_spot 7 сд. p50=111.0 мс | bybit_spot_book 54 сд. p50=108.7 мс | okx 29 сд. p50=156.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:35:53 [pm] T-246.2s Up 0.74/0.75 Down 0.25/0.26 ptb=82285.8 | CLOB 4920 сообщ., задержка p50/p90=43.4/81.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792085753751 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=50.4 мс | lag loop p99/max=2.0/2.1 мс
```

Представлено версией кода: ec1316a; python 3.12.3
