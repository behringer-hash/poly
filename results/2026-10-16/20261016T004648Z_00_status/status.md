# Состояние сервера записи

Время (UTC): 2026-10-16 00:46:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 17 hours, 22 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         689         314           2        1151        1216
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.04 / 0.10 / 0.09

## Данные
- файлов: 4534, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 181 | 25 МБ | 1 |
| bn_book | 181 | 2 МБ | 3 |
| bnf_agg | 181 | 39 МБ | 1 |
| bnf_book | 118 | 557 МБ | 226702 |
| bnf_depth5 | 118 | 41 МБ | 226778 |
| bnf_liq | 163 | 112 КБ | 189 |
| bs_trade | 118 | 1 МБ | 226698 |
| by_book1 | 181 | 81 МБ | 1 |
| by_liq | 161 | 93 КБ | 923 |
| by_trade | 181 | 26 МБ | 1 |
| bys_book1 | 65 | 27 МБ | 1 |
| bys_trade | 65 | 12 МБ | 1 |
| cb_ticker | 181 | 23 МБ | 1 |
| clock | 181 | 140 КБ | 33 |
| clock_pm | 181 | 140 КБ | 32 |
| events | 170 | 55 КБ | 1276 |
| events_pm | 181 | 65 КБ | 869 |
| health_cex | 181 | 2 МБ | 5 |
| health_feeds | 181 | 6 МБ | 5 |
| health_pm | 181 | 2 МБ | 0 |
| kr_trade | 118 | 3 МБ | 226698 |
| ok_trade | 180 | 34 МБ | 1 |
| pm_depth | 181 | 37 МБ | 0 |
| pm_rtt | 181 | 1 МБ | 4 |
| pm_top | 181 | 75 МБ | 0 |
| pm_trades | 181 | 54 МБ | 0 |
| rtds | 181 | 12 МБ | 0 |
| windows | 181 | 375 КБ | 104 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 9, TLS 49, всего 299
- Polymarket CLOB: TCP 7, TLS 44, всего 83
- Polymarket gamma: TCP 5, TLS 40, всего 51

## Последние строки журнала записи
```
00:46:03 [cex] Binance 43 сд. задержка p50/p90=144.3/145.7 мс | Coinbase 37 задержка p50=80.9 мс | смещение часов +19.8 мс | lag loop p99/max=2.4/5.8 мс
00:46:03 [cex] binance_futures 229 сд. p50=145.7 мс | bybit 147 сд. p50=113.7 мс | bybit_book 424 сд. p50=111.5 мс | bybit_spot 103 сд. p50=114.5 мс | bybit_spot_book 213 сд. p50=111.2 мс | okx 124 сд. p50=158.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:46:07 [pm] T-232.7s Up 0.06/0.07 Down 0.93/0.94 ptb=82318.4 | CLOB 7804 сообщ., задержка p50/p90=40.3/51.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792111567334 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.7 мс | lag loop p99/max=4.2/6.8 мс
00:46:13 [cex] Binance 33 сд. задержка p50/p90=144.1/144.3 мс | Coinbase 36 задержка p50=79.8 мс | смещение часов +19.8 мс | lag loop p99/max=2.1/2.2 мс
00:46:13 [cex] binance_futures 218 сд. p50=145.8 мс | bybit 115 сд. p50=113.8 мс | bybit_book 424 сд. p50=111.5 мс | bybit_spot 43 сд. p50=114.5 мс | bybit_spot_book 190 сд. p50=111.2 мс | okx 120 сд. p50=158.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:46:17 [pm] T-222.7s Up 0.05/0.06 Down 0.94/0.95 ptb=82318.4 | CLOB 5846 сообщ., задержка p50/p90=39.8/106.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792111577335 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.7 мс | lag loop p99/max=1.3/2.0 мс
00:46:23 [cex] Binance 90 сд. задержка p50/p90=145.6/146.6 мс | Coinbase 57 задержка p50=81.6 мс | смещение часов +20.8 мс | lag loop p99/max=2.0/2.1 мс
00:46:23 [cex] binance_futures 278 сд. p50=147.3 мс | bybit 112 сд. p50=114.6 мс | bybit_book 324 сд. p50=112.4 мс | bybit_spot 224 сд. p50=115.1 мс | bybit_spot_book 247 сд. p50=112.1 мс | okx 94 сд. p50=159.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:46:27 [pm] T-212.7s Up 0.09/0.10 Down 0.90/0.91 ptb=82318.4 | CLOB 7862 сообщ., задержка p50/p90=74.2/103.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792111587337 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.7 мс | lag loop p99/max=1.8/2.1 мс
00:46:33 [cex] Binance 146 сд. задержка p50/p90=145.3/146.4 мс | Coinbase 112 задержка p50=82.0 мс | смещение часов +20.8 мс | lag loop p99/max=2.0/2.1 мс
00:46:33 [cex] binance_futures 474 сд. p50=146.8 мс | bybit 307 сд. p50=114.7 мс | bybit_book 399 сд. p50=112.4 мс | bybit_spot 282 сд. p50=115.0 мс | bybit_spot_book 292 сд. p50=112.1 мс | okx 284 сд. p50=159.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:46:37 [pm] T-202.7s Up 0.08/0.09 Down 0.91/0.92 ptb=82318.4 | CLOB 5395 сообщ., задержка p50/p90=41.1/52.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792111597338 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.7 мс | lag loop p99/max=1.6/2.0 мс
00:46:43 [cex] Binance 12 сд. задержка p50/p90=145.1/145.4 мс | Coinbase 45 задержка p50=81.6 мс | смещение часов +20.8 мс | lag loop p99/max=2.1/2.2 мс
00:46:43 [cex] binance_futures 299 сд. p50=146.6 мс | bybit 115 сд. p50=115.2 мс | bybit_book 318 сд. p50=112.4 мс | bybit_spot 22 сд. p50=114.7 мс | bybit_spot_book 249 сд. p50=112.2 мс | okx 99 сд. p50=159.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:46:47 [pm] T-192.7s Up 0.11/0.12 Down 0.88/0.89 ptb=82318.4 | CLOB 4526 сообщ., задержка p50/p90=42.3/53.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792111607339 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.8 мс | lag loop p99/max=2.1/2.1 мс
```

Представлено версией кода: ec1316a; python 3.12.3
