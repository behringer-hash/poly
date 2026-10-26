# Состояние сервера записи

Время (UTC): 2026-10-26 18:29:27

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 5 days, 11 hours, 5 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         636        1066           1         374        1269
Swap:           2047         293        1754
```
- нагрузка CPU (1/5/15 мин): 0.11 / 0.33 / 0.40

## Данные
- файлов: 5844, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 1 |
| bn_book | 242 | 3 МБ | 15 |
| bnf_agg | 242 | 51 МБ | 1 |
| bnf_book | 46 | 350 МБ | 0 |
| bnf_depth5 | 40 | 15 МБ | 1154537 |
| bnf_liq | 216 | 145 КБ | 1667 |
| bs_trade | 40 | 558 КБ | 1154457 |
| by_book1 | 242 | 109 МБ | 1 |
| by_liq | 228 | 108 КБ | 2355 |
| by_trade | 242 | 34 МБ | 1 |
| bys_book1 | 204 | 70 МБ | 1 |
| bys_trade | 204 | 28 МБ | 5 |
| cb_ticker | 242 | 32 МБ | 1 |
| clock | 242 | 188 КБ | 42 |
| clock_pm | 242 | 188 КБ | 52 |
| events | 230 | 72 КБ | 445 |
| events_pm | 241 | 85 КБ | 93 |
| health_cex | 242 | 2 МБ | 7 |
| health_feeds | 242 | 8 МБ | 7 |
| health_pm | 242 | 3 МБ | 6 |
| kr_trade | 40 | 1 МБ | 1154457 |
| ok_trade | 241 | 45 МБ | 7 |
| pm_depth | 242 | 49 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 0 |
| pm_top | 242 | 102 МБ | 0 |
| pm_trades | 242 | 72 МБ | 6 |
| rtds | 242 | 16 МБ | 0 |
| windows | 242 | 500 КБ | 22 |

Дни с данными: 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 36, всего 283
- Polymarket CLOB: TCP 5, TLS 38, всего 82
- Polymarket gamma: TCP 4, TLS 36, всего 43

## Последние строки журнала записи
```
18:28:40 [cex] Binance 77 сд. задержка p50/p90=141.8/142.7 мс | Coinbase 102 задержка p50=81.7 мс | смещение часов +19.0 мс | lag loop p99/max=2.0/2.2 мс
18:28:40 [cex] binance_futures 99 сд. p50=153.2 мс | bybit 103 сд. p50=111.7 мс | bybit_book 203 сд. p50=108.7 мс | bybit_spot 95 сд. p50=112.5 мс | bybit_spot_book 92 сд. p50=109.2 мс | okx 47 сд. p50=155.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1589 сд. p50=142.6 мс
18:28:40 [pm] T- 79.3s Up 0.02/0.03 Down 0.97/0.98 ptb=80157.8 | CLOB 5604 сообщ., задержка p50/p90=39.8/43.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793039320750 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=1.9/1.9 мс
18:28:50 [cex] Binance 59 сд. задержка p50/p90=142.1/142.6 мс | Coinbase 34 задержка p50=79.9 мс | смещение часов +19.5 мс | lag loop p99/max=2.2/2.2 мс
18:28:50 [cex] binance_futures 41 сд. p50=292.0 мс | bybit 23 сд. p50=111.3 мс | bybit_book 69 сд. p50=109.2 мс | bybit_spot 4 сд. p50=111.5 мс | bybit_spot_book 39 сд. p50=109.6 мс | okx 7 сд. p50=155.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 389 сд. p50=142.7 мс
18:28:50 [pm] T- 69.2s Up 0.02/0.03 Down 0.97/0.98 ptb=80157.8 | CLOB 2599 сообщ., задержка p50/p90=39.3/40.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793039330751 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=1.7/1.9 мс
18:29:00 [cex] Binance 71 сд. задержка p50/p90=142.2/142.8 мс | Coinbase 66 задержка p50=82.1 мс | смещение часов +19.5 мс | lag loop p99/max=2.0/2.1 мс
18:29:00 [cex] binance_futures 48 сд. p50=292.0 мс | bybit 21 сд. p50=111.5 мс | bybit_book 111 сд. p50=109.3 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 34 сд. p50=109.8 мс | okx 7 сд. p50=155.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 418 сд. p50=143.0 мс
18:29:00 [pm] T- 59.2s Up n/a/0.01 Down 0.99/n/a ptb=80157.8 | CLOB 2852 сообщ., задержка p50/p90=40.1/122.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793039340753 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=2.0/2.1 мс
18:29:10 [cex] Binance 57 сд. задержка p50/p90=142.3/143.2 мс | Coinbase 59 задержка p50=84.4 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.1 мс
18:29:10 [cex] binance_futures 65 сд. p50=285.8 мс | bybit 90 сд. p50=111.9 мс | bybit_book 121 сд. p50=109.3 мс | bybit_spot 147 сд. p50=112.9 мс | bybit_spot_book 83 сд. p50=109.7 мс | okx 11 сд. p50=155.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2070 сд. p50=144.3 мс
18:29:10 [pm] T- 49.2s Up n/a/0.01 Down 0.99/n/a ptb=80157.8 | CLOB 1225 сообщ., задержка p50/p90=39.6/56.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793039350755 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=2.1/2.1 мс
18:29:20 [cex] Binance 897 сд. задержка p50/p90=142.7/143.6 мс | Coinbase 57 задержка p50=81.9 мс | смещение часов +19.5 мс | lag loop p99/max=2.2/2.2 мс
18:29:20 [cex] binance_futures 66 сд. p50=292.0 мс | bybit 24 сд. p50=112.1 мс | bybit_book 105 сд. p50=109.3 мс | bybit_spot 47 сд. p50=114.4 мс | bybit_spot_book 63 сд. p50=109.6 мс | okx 53 сд. p50=155.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3031 сд. p50=143.4 мс
18:29:20 [pm] T- 39.2s Up n/a/0.01 Down 0.99/n/a ptb=80157.8 | CLOB 928 сообщ., задержка p50/p90=39.3/40.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793039360756 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=2.1/2.1 мс
```

Представлено версией кода: 80591e6; python 3.12.3
