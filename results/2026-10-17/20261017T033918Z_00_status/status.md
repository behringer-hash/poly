# Состояние сервера записи

Время (UTC): 2026-10-17 03:39:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 20 hours, 15 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         864         558           2         769        1041
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.31 / 0.31 / 0.27

## Данные
- файлов: 5178, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 208 | 29 МБ | 0 |
| bn_book | 208 | 3 МБ | 100 |
| bnf_agg | 208 | 44 МБ | 0 |
| bnf_book | 118 | 557 МБ | 323452 |
| bnf_depth5 | 118 | 41 МБ | 323528 |
| bnf_liq | 187 | 128 КБ | 360 |
| bs_trade | 118 | 1 МБ | 323448 |
| by_book1 | 208 | 91 МБ | 0 |
| by_liq | 187 | 104 КБ | 802 |
| by_trade | 208 | 29 МБ | 0 |
| bys_book1 | 92 | 36 МБ | 0 |
| bys_trade | 92 | 14 МБ | 7 |
| cb_ticker | 208 | 27 МБ | 0 |
| clock | 208 | 161 КБ | 29 |
| clock_pm | 208 | 161 КБ | 52 |
| events | 197 | 64 КБ | 1024 |
| events_pm | 208 | 76 КБ | 255 |
| health_cex | 208 | 2 МБ | 0 |
| health_feeds | 208 | 7 МБ | 0 |
| health_pm | 208 | 2 МБ | 5 |
| kr_trade | 118 | 3 МБ | 323448 |
| ok_trade | 207 | 38 МБ | 0 |
| pm_depth | 208 | 42 МБ | 1 |
| pm_rtt | 208 | 1 МБ | 1 |
| pm_top | 208 | 86 МБ | 1 |
| pm_trades | 208 | 62 МБ | 1 |
| rtds | 208 | 13 МБ | 1 |
| windows | 208 | 430 КБ | 74 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 55, всего 304
- Polymarket CLOB: TCP 5, TLS 44, всего 85
- Polymarket gamma: TCP 5, TLS 50, всего 60

## Последние строки журнала записи
```
03:38:32 [pm] T- 87.2s Up 0.26/0.27 Down 0.73/0.74 ptb=81475.7 | CLOB 6475 сообщ., задержка p50/p90=41.3/42.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792208312806 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.4/1.5 мс
03:38:36 [cex] Binance 75 сд. задержка p50/p90=145.1/145.8 мс | Coinbase 29 задержка p50=77.6 мс | смещение часов +20.4 мс | lag loop p99/max=2.2/2.3 мс
03:38:36 [cex] binance_futures 34 сд. p50=294.2 мс | bybit 2 сд. p50=114.2 мс | bybit_book 62 сд. p50=112.0 мс | bybit_spot 38 сд. p50=115.0 мс | bybit_spot_book 22 сд. p50=112.5 мс | okx 7 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:38:42 [pm] T- 77.2s Up 0.20/0.21 Down 0.79/0.80 ptb=81475.7 | CLOB 5429 сообщ., задержка p50/p90=41.8/46.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792208322807 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.8/2.0 мс
03:38:46 [cex] Binance 82 сд. задержка p50/p90=145.1/146.1 мс | Coinbase 27 задержка p50=77.3 мс | смещение часов +20.4 мс | lag loop p99/max=2.0/2.2 мс
03:38:46 [cex] binance_futures 40 сд. p50=294.2 мс | bybit 8 сд. p50=114.3 мс | bybit_book 44 сд. p50=112.1 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 35 сд. p50=112.7 мс | okx 5 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:38:52 [pm] T- 67.2s Up 0.15/0.16 Down 0.84/0.85 ptb=81475.7 | CLOB 6248 сообщ., задержка p50/p90=41.9/48.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792208332809 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.9 мс | lag loop p99/max=1.6/1.7 мс
03:38:56 [cex] Binance 76 сд. задержка p50/p90=145.9/146.9 мс | Coinbase 29 задержка p50=77.9 мс | смещение часов +21.2 мс | lag loop p99/max=2.2/2.2 мс
03:38:56 [cex] binance_futures 39 сд. p50=295.0 мс | bybit 6 сд. p50=114.4 мс | bybit_book 71 сд. p50=112.7 мс | bybit_spot 7 сд. p50=115.0 мс | bybit_spot_book 41 сд. p50=113.4 мс | okx 10 сд. p50=155.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:39:02 [pm] T- 57.2s Up 0.28/0.29 Down 0.71/0.72 ptb=81475.7 | CLOB 7950 сообщ., задержка p50/p90=41.9/80.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792208342811 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.9 мс | lag loop p99/max=2.8/6.2 мс
03:39:06 [cex] Binance 90 сд. задержка p50/p90=145.9/147.0 мс | Coinbase 34 задержка p50=78.1 мс | смещение часов +21.2 мс | lag loop p99/max=2.1/2.1 мс
03:39:06 [cex] binance_futures 49 сд. p50=295.0 мс | bybit 5 сд. p50=114.5 мс | bybit_book 47 сд. p50=112.8 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 50 сд. p50=113.4 мс | okx 5 сд. p50=155.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:39:12 [pm] T- 47.2s Up 0.12/0.13 Down 0.87/0.88 ptb=81475.7 | CLOB 10131 сообщ., задержка p50/p90=41.5/43.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792208352812 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=1.2/1.5 мс
03:39:16 [cex] Binance 88 сд. задержка p50/p90=145.9/146.7 мс | Coinbase 27 задержка p50=77.9 мс | смещение часов +21.2 мс | lag loop p99/max=2.1/2.1 мс
03:39:16 [cex] binance_futures 53 сд. p50=295.0 мс | bybit 21 сд. p50=115.0 мс | bybit_book 42 сд. p50=112.8 мс | bybit_spot 3 сд. p50=114.5 мс | bybit_spot_book 38 сд. p50=113.5 мс | okx 6 сд. p50=155.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 8083be6; python 3.12.3
