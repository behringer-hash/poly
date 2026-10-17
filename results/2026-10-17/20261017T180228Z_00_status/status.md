# Состояние сервера записи

Время (UTC): 2026-10-17 18:02:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 10 hours, 38 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         876         481           2         835        1029
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.45 / 0.28 / 0.21

## Данные
- файлов: 5525, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 223 | 29 МБ | 0 |
| bn_book | 223 | 3 МБ | 25 |
| bnf_agg | 223 | 44 МБ | 0 |
| bnf_book | 118 | 557 МБ | 375242 |
| bnf_depth5 | 118 | 41 МБ | 375318 |
| bnf_liq | 195 | 132 КБ | 687 |
| bs_trade | 118 | 1 МБ | 375238 |
| by_book1 | 223 | 93 МБ | 0 |
| by_liq | 197 | 106 КБ | 2971 |
| by_trade | 223 | 29 МБ | 0 |
| bys_book1 | 107 | 38 МБ | 0 |
| bys_trade | 107 | 15 МБ | 0 |
| cb_ticker | 223 | 28 МБ | 0 |
| clock | 223 | 171 КБ | 59 |
| clock_pm | 223 | 171 КБ | 26 |
| events | 212 | 69 КБ | 75 |
| events_pm | 222 | 82 КБ | 1060 |
| health_cex | 223 | 2 МБ | 4 |
| health_feeds | 223 | 7 МБ | 4 |
| health_pm | 223 | 2 МБ | 8 |
| kr_trade | 118 | 3 МБ | 375238 |
| ok_trade | 222 | 39 МБ | 0 |
| pm_depth | 223 | 44 МБ | 2 |
| pm_rtt | 223 | 1 МБ | 4 |
| pm_top | 223 | 90 МБ | 2 |
| pm_trades | 223 | 65 МБ | 2 |
| rtds | 223 | 14 МБ | 2 |
| windows | 223 | 458 КБ | 141 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 41, всего 289
- Polymarket CLOB: TCP 5, TLS 40, всего 84
- Polymarket gamma: TCP 5, TLS 45, всего 64

## Последние строки журнала записи
```
18:01:40 [pm] T-199.6s Up 0.77/0.78 Down 0.22/0.23 ptb=81274.0 | CLOB 4030 сообщ., задержка p50/p90=39.5/45.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792260100429 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.0/2.1 мс
18:01:42 [cex] Binance 57 сд. задержка p50/p90=144.9/145.1 мс | Coinbase 45 задержка p50=78.3 мс | смещение часов +21.1 мс | lag loop p99/max=2.0/2.3 мс
18:01:42 [cex] binance_futures 65 сд. p50=295.1 мс | bybit 2 сд. p50=114.9 мс | bybit_book 80 сд. p50=113.1 мс | bybit_spot 2 сд. p50=114.9 мс | bybit_spot_book 67 сд. p50=112.7 мс | okx 39 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:01:50 [pm] T-189.6s Up 0.78/0.79 Down 0.21/0.22 ptb=81274.0 | CLOB 2500 сообщ., задержка p50/p90=38.8/40.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792260110430 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.1/2.1 мс
18:01:52 [cex] Binance 63 сд. задержка p50/p90=144.9/145.9 мс | Coinbase 31 задержка p50=77.8 мс | смещение часов +21.1 мс | lag loop p99/max=2.0/2.4 мс
18:01:52 [cex] binance_futures 65 сд. p50=295.1 мс | bybit 12 сд. p50=114.6 мс | bybit_book 76 сд. p50=113.2 мс | bybit_spot 3 сд. p50=115.0 мс | bybit_spot_book 52 сд. p50=112.7 мс | okx 61 сд. p50=154.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:02:00 [pm] T-179.6s Up 0.88/0.89 Down 0.11/0.12 ptb=81274.0 | CLOB 3652 сообщ., задержка p50/p90=39.7/46.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792260120431 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.2/3.1 мс
18:02:02 [cex] Binance 139 сд. задержка p50/p90=145.1/146.1 мс | Coinbase 35 задержка p50=78.2 мс | смещение часов +21.1 мс | lag loop p99/max=3.1/3.5 мс
18:02:02 [cex] binance_futures 64 сд. p50=295.2 мс | bybit 10 сд. p50=115.5 мс | bybit_book 82 сд. p50=113.1 мс | bybit_spot 62 сд. p50=115.6 мс | bybit_spot_book 65 сд. p50=112.6 мс | okx 148 сд. p50=154.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:02:10 [pm] T-169.6s Up 0.91/0.92 Down 0.08/0.09 ptb=81274.0 | CLOB 2539 сообщ., задержка p50/p90=58.8/400.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792260130433 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=3.1/4.7 мс
18:02:12 [cex] Binance 199 сд. задержка p50/p90=145.8/159.6 мс | Coinbase 48 задержка p50=79.2 мс | смещение часов +21.1 мс | lag loop p99/max=2.3/3.5 мс
18:02:12 [cex] binance_futures 175 сд. p50=153.6 мс | bybit 198 сд. p50=148.1 мс | bybit_book 133 сд. p50=113.2 мс | bybit_spot 100 сд. p50=131.4 мс | bybit_spot_book 89 сд. p50=112.7 мс | okx 515 сд. p50=390.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:02:20 [pm] T-159.6s Up 0.92/0.93 Down 0.07/0.08 ptb=81274.0 | CLOB 2330 сообщ., задержка p50/p90=41.7/43.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792260140434 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.1/2.3 мс
18:02:22 [cex] Binance 84 сд. задержка p50/p90=144.9/145.8 мс | Coinbase 35 задержка p50=77.9 мс | смещение часов +21.1 мс | lag loop p99/max=2.1/2.2 мс
18:02:22 [cex] binance_futures 68 сд. p50=295.1 мс | bybit 16 сд. p50=115.2 мс | bybit_book 82 сд. p50=113.1 мс | bybit_spot 12 сд. p50=114.9 мс | bybit_spot_book 44 сд. p50=112.7 мс | okx 16 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 8083be6; python 3.12.3
