# Состояние сервера записи

Время (UTC): 2026-10-20 03:44:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 5 days, 20 hours, 20 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         807         185           1        1096        1098
Swap:           2047         250        1797
```
- нагрузка CPU (1/5/15 мин): 0.19 / 0.28 / 0.32

## Данные
- файлов: 6883, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 280 | 37 МБ | 1 |
| bn_book | 280 | 3 МБ | 30 |
| bnf_agg | 280 | 56 МБ | 1 |
| bnf_book | 118 | 557 МБ | 582952 |
| bnf_depth5 | 118 | 41 МБ | 583028 |
| bnf_liq | 243 | 159 КБ | 304 |
| bs_trade | 118 | 1 МБ | 582948 |
| by_book1 | 280 | 117 МБ | 1 |
| by_liq | 252 | 127 КБ | 463 |
| by_trade | 280 | 37 МБ | 7 |
| bys_book1 | 164 | 56 МБ | 1 |
| bys_trade | 164 | 23 МБ | 3 |
| cb_ticker | 280 | 34 МБ | 1 |
| clock | 280 | 217 КБ | 5 |
| clock_pm | 280 | 217 КБ | 32 |
| events | 269 | 85 КБ | 2221 |
| events_pm | 280 | 101 КБ | 1094 |
| health_cex | 280 | 3 МБ | 1 |
| health_feeds | 280 | 9 МБ | 1 |
| health_pm | 280 | 3 МБ | 6 |
| kr_trade | 118 | 3 МБ | 582948 |
| ok_trade | 279 | 48 МБ | 1 |
| pm_depth | 280 | 56 МБ | 2 |
| pm_rtt | 280 | 2 МБ | 2 |
| pm_top | 280 | 115 МБ | 2 |
| pm_trades | 280 | 81 МБ | 6 |
| rtds | 280 | 18 МБ | 2 |
| windows | 280 | 578 КБ | 403 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 36, всего 771
- Polymarket CLOB: TCP 5, TLS 38, всего 80
- Polymarket gamma: TCP 5, TLS 52, всего 63

## Последние строки журнала записи
```
03:43:31 [pm] T- 88.4s Up 0.04/0.05 Down 0.95/0.96 ptb=81949.9 | CLOB 6862 сообщ., задержка p50/p90=65.2/66.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792467811643 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.1/1.2 мс
03:43:36 [cex] Binance 88 сд. задержка p50/p90=164.4/165.2 мс | Coinbase 27 задержка p50=85.5 мс | смещение часов +25.5 мс | lag loop p99/max=2.0/2.1 мс
03:43:36 [cex] binance_futures 74 сд. p50=297.4 мс | bybit 25 сд. p50=119.3 мс | bybit_book 109 сд. p50=117.6 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 36 сд. p50=117.0 мс | okx 18 сд. p50=149.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:43:41 [pm] T- 78.4s Up 0.02/0.03 Down 0.97/0.98 ptb=81949.9 | CLOB 3921 сообщ., задержка p50/p90=65.3/67.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792467821644 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.6/1.7 мс
03:43:46 [cex] Binance 69 сд. задержка p50/p90=164.3/164.8 мс | Coinbase 30 задержка p50=85.3 мс | смещение часов +25.5 мс | lag loop p99/max=2.1/2.1 мс
03:43:46 [cex] binance_futures 74 сд. p50=298.6 мс | bybit 47 сд. p50=119.0 мс | bybit_book 81 сд. p50=117.6 мс | bybit_spot 1 сд. p50=119.0 мс | bybit_spot_book 38 сд. p50=117.2 мс | okx 17 сд. p50=149.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:43:51 [pm] T- 68.4s Up 0.01/0.02 Down 0.98/0.99 ptb=81949.9 | CLOB 2469 сообщ., задержка p50/p90=58.6/65.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792467831646 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.0/2.5 мс
03:43:56 [cex] Binance 63 сд. задержка p50/p90=164.3/165.3 мс | Coinbase 33 задержка p50=85.0 мс | смещение часов +25.5 мс | lag loop p99/max=2.1/2.1 мс
03:43:56 [cex] binance_futures 51 сд. p50=298.7 мс | bybit 33 сд. p50=119.6 мс | bybit_book 117 сд. p50=117.6 мс | bybit_spot 50 сд. p50=119.2 мс | bybit_spot_book 56 сд. p50=117.2 мс | okx 38 сд. p50=150.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:44:01 [pm] T- 58.4s Up n/a/0.01 Down 0.99/n/a ptb=81949.9 | CLOB 2384 сообщ., задержка p50/p90=58.4/67.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792467841649 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.0/3.1 мс
03:44:06 [cex] Binance 68 сд. задержка p50/p90=164.3/165.3 мс | Coinbase 23 задержка p50=85.0 мс | смещение часов +25.5 мс | lag loop p99/max=2.1/2.2 мс
03:44:06 [cex] binance_futures 60 сд. p50=298.8 мс | bybit 13 сд. p50=118.9 мс | bybit_book 87 сд. p50=117.6 мс | bybit_spot 1 сд. p50=119.7 мс | bybit_spot_book 42 сд. p50=117.1 мс | okx 18 сд. p50=149.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:44:11 [pm] T- 48.3s Up n/a/0.01 Down 0.99/n/a ptb=81949.9 | CLOB 776 сообщ., задержка p50/p90=58.0/58.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792467851651 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.1/2.2 мс
03:44:16 [cex] Binance 83 сд. задержка p50/p90=158.3/164.3 мс | Coinbase 39 задержка p50=79.2 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.1 мс
03:44:16 [cex] binance_futures 62 сд. p50=292.7 мс | bybit 2 сд. p50=118.9 мс | bybit_book 69 сд. p50=111.4 мс | bybit_spot 1 сд. p50=112.6 мс | bybit_spot_book 26 сд. p50=116.8 мс | okx 32 сд. p50=148.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
