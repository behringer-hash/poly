# Состояние сервера записи

Время (UTC): 2026-10-14 06:37:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 6 days, 23 hours, 13 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         567         535           2         990        1338
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.25 / 0.18 / 0.17

## Данные
- файлов: 3532, всего 910 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 139 | 17 МБ | 2 |
| bn_book | 139 | 1 МБ | 12 |
| bnf_agg | 139 | 26 МБ | 0 |
| bnf_book | 118 | 557 МБ | 74942 |
| bnf_depth5 | 118 | 41 МБ | 75018 |
| bnf_liq | 123 | 74 КБ | 1299 |
| bs_trade | 118 | 1 МБ | 74938 |
| by_book1 | 139 | 55 МБ | 0 |
| by_liq | 120 | 62 КБ | 1942 |
| by_trade | 139 | 16 МБ | 0 |
| bys_book1 | 23 | 7 МБ | 0 |
| bys_trade | 23 | 3 МБ | 0 |
| cb_ticker | 139 | 15 МБ | 0 |
| clock | 139 | 108 КБ | 16 |
| clock_pm | 139 | 108 КБ | 14 |
| events | 131 | 44 КБ | 77 |
| events_pm | 139 | 52 КБ | 767 |
| health_cex | 139 | 1 МБ | 4 |
| health_feeds | 139 | 5 МБ | 4 |
| health_pm | 139 | 1 МБ | 2 |
| kr_trade | 118 | 3 МБ | 74938 |
| ok_trade | 138 | 22 МБ | 0 |
| pm_depth | 139 | 28 МБ | -0 |
| pm_rtt | 139 | 940 КБ | 2 |
| pm_top | 139 | 56 МБ | -0 |
| pm_trades | 139 | 41 МБ | -0 |
| rtds | 139 | 9 МБ | -0 |
| windows | 139 | 287 КБ | 84 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 41, всего 290
- Polymarket CLOB: TCP 9, TLS 44, всего 86
- Polymarket gamma: TCP 5, TLS 44, всего 56

## Последние строки журнала записи
```
06:36:43 [cex] Binance 13 сд. задержка p50/p90=142.1/143.1 мс | Coinbase 14 задержка p50=79.1 мс | смещение часов +17.9 мс | lag loop p99/max=2.0/2.2 мс
06:36:43 [cex] binance_futures 12 сд. p50=291.3 мс | bybit 14 сд. p50=110.6 мс | bybit_book 64 сд. p50=110.0 мс | bybit_spot 9 сд. p50=112.1 мс | bybit_spot_book 27 сд. p50=109.4 мс | okx 46 сд. p50=146.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:36:45 [pm] T-194.3s Up 0.42/0.43 Down 0.57/0.58 ptb=83383.7 | CLOB 6603 сообщ., задержка p50/p90=33.9/36.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791959805748 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.3 мс | lag loop p99/max=1.8/1.9 мс
06:36:53 [cex] Binance 9 сд. задержка p50/p90=142.0/142.3 мс | Coinbase 14 задержка p50=78.4 мс | смещение часов +17.9 мс | lag loop p99/max=2.1/2.3 мс
06:36:53 [cex] binance_futures 12 сд. p50=291.4 мс | bybit 11 сд. p50=111.2 мс | bybit_book 57 сд. p50=110.0 мс | bybit_spot 2 сд. p50=112.2 мс | bybit_spot_book 15 сд. p50=109.5 мс | okx 4 сд. p50=145.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:36:55 [pm] T-184.3s Up 0.44/0.45 Down 0.55/0.56 ptb=83383.7 | CLOB 5532 сообщ., задержка p50/p90=33.8/37.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791959815749 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.3 мс | lag loop p99/max=1.5/2.3 мс
06:37:03 [cex] Binance 124 сд. задержка p50/p90=142.3/143.4 мс | Coinbase 29 задержка p50=78.2 мс | смещение часов +17.9 мс | lag loop p99/max=2.1/3.0 мс
06:37:03 [cex] binance_futures 136 сд. p50=143.0 мс | bybit 71 сд. p50=111.6 мс | bybit_book 169 сд. p50=110.0 мс | bybit_spot 128 сд. p50=112.4 мс | bybit_spot_book 88 сд. p50=109.4 мс | okx 129 сд. p50=146.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:37:05 [pm] T-174.2s Up 0.67/0.68 Down 0.32/0.33 ptb=83383.7 | CLOB 9851 сообщ., задержка p50/p90=33.7/42.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791959825750 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=2.4/8.1 мс
06:37:13 [cex] Binance 37 сд. задержка p50/p90=143.1/144.5 мс | Coinbase 15 задержка p50=79.0 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.1 мс
06:37:13 [cex] binance_futures 38 сд. p50=173.7 мс | bybit 17 сд. p50=111.3 мс | bybit_book 119 сд. p50=110.1 мс | bybit_spot 3 сд. p50=111.7 мс | bybit_spot_book 46 сд. p50=110.1 мс | okx 38 сд. p50=146.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:37:15 [pm] T-164.2s Up 0.74/0.75 Down 0.25/0.26 ptb=83383.7 | CLOB 7322 сообщ., задержка p50/p90=35.4/37.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791959835752 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=2.1/2.2 мс
06:37:23 [cex] Binance 22 сд. задержка p50/p90=143.4/144.3 мс | Coinbase 11 задержка p50=80.9 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.3 мс
06:37:23 [cex] binance_futures 21 сд. p50=292.9 мс | bybit 8 сд. p50=112.2 мс | bybit_book 116 сд. p50=111.2 мс | bybit_spot 13 сд. p50=113.7 мс | bybit_spot_book 32 сд. p50=110.7 мс | okx 9 сд. p50=146.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:37:25 [pm] T-154.2s Up 0.65/0.66 Down 0.34/0.35 ptb=83383.7 | CLOB 8212 сообщ., задержка p50/p90=41.0/67.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791959845754 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=1.4/1.4 мс
```

Представлено версией кода: ec1316a; python 3.12.3
