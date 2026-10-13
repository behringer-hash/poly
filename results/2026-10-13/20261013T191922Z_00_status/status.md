# Состояние сервера записи

Время (UTC): 2026-10-13 19:19:22

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 6 days, 11 hours, 55 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         556         944           2         585        1349
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.13 / 0.12 / 0.14

## Данные
- файлов: 3268, всего 880 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 128 | 16 МБ | 2 |
| bn_book | 128 | 1 МБ | 22 |
| bnf_agg | 128 | 24 МБ | 2 |
| bnf_book | 118 | 557 МБ | 34256 |
| bnf_depth5 | 118 | 41 МБ | 34332 |
| bnf_liq | 112 | 70 КБ | 2402 |
| bs_trade | 118 | 1 МБ | 34252 |
| by_book1 | 128 | 50 МБ | 2 |
| by_liq | 109 | 60 КБ | 982 |
| by_trade | 128 | 15 МБ | 2 |
| bys_book1 | 12 | 4 МБ | 2 |
| bys_trade | 12 | 2 МБ | 6 |
| cb_ticker | 128 | 14 МБ | 2 |
| clock | 128 | 99 КБ | 24 |
| clock_pm | 128 | 99 КБ | 20 |
| events | 120 | 40 КБ | 565 |
| events_pm | 128 | 47 КБ | 478 |
| health_cex | 128 | 1 МБ | 2 |
| health_feeds | 128 | 5 МБ | 2 |
| health_pm | 128 | 1 МБ | 1 |
| kr_trade | 118 | 3 МБ | 34252 |
| ok_trade | 127 | 21 МБ | 4 |
| pm_depth | 128 | 25 МБ | 1 |
| pm_rtt | 128 | 855 КБ | 1 |
| pm_top | 128 | 51 МБ | 1 |
| pm_trades | 128 | 37 МБ | 1 |
| rtds | 128 | 8 МБ | 1 |
| windows | 128 | 263 КБ | 256 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 39, всего 289
- Polymarket CLOB: TCP 6, TLS 52, всего 101
- Polymarket gamma: TCP 5, TLS 43, всего 56

## Последние строки журнала записи
```
19:18:39 [cex] Binance 42 сд. задержка p50/p90=145.5/145.8 мс | Coinbase 32 задержка p50=81.4 мс | смещение часов +20.8 мс | lag loop p99/max=2.0/2.1 мс
19:18:39 [cex] binance_futures 55 сд. p50=146.2 мс | bybit 27 сд. p50=114.5 мс | bybit_book 123 сд. p50=112.7 мс | bybit_spot 72 сд. p50=115.3 мс | bybit_spot_book 45 сд. p50=112.4 мс | okx 51 сд. p50=155.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:18:39 [pm] T- 80.1s Up 0.24/0.25 Down 0.75/0.76 ptb=83099.3 | CLOB 9875 сообщ., задержка p50/p90=79.5/250.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791919119899 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.2 мс | lag loop p99/max=1.9/2.0 мс
19:18:49 [cex] Binance 24 сд. задержка p50/p90=145.1/145.4 мс | Coinbase 60 задержка p50=82.3 мс | смещение часов +20.8 мс | lag loop p99/max=2.1/2.1 мс
19:18:49 [cex] binance_futures 39 сд. p50=252.1 мс | bybit 77 сд. p50=114.5 мс | bybit_book 160 сд. p50=112.7 мс | bybit_spot 78 сд. p50=115.3 мс | bybit_spot_book 332 сд. p50=112.4 мс | okx 40 сд. p50=148.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:18:49 [pm] T- 70.1s Up 0.30/0.31 Down 0.69/0.70 ptb=83099.3 | CLOB 9448 сообщ., задержка p50/p90=40.8/50.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791919129901 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.2 мс | lag loop p99/max=1.4/1.4 мс
19:18:59 [cex] Binance 18 сд. задержка p50/p90=145.1/145.3 мс | Coinbase 65 задержка p50=82.3 мс | смещение часов +20.3 мс | lag loop p99/max=2.1/2.2 мс
19:18:59 [cex] binance_futures 27 сд. p50=148.8 мс | bybit 23 сд. p50=115.0 мс | bybit_book 122 сд. p50=112.6 мс | bybit_spot 32 сд. p50=115.2 мс | bybit_spot_book 36 сд. p50=112.3 мс | okx 22 сд. p50=148.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:18:59 [pm] T- 60.1s Up 0.35/0.41 Down 0.59/0.65 ptb=83099.3 | CLOB 9776 сообщ., задержка p50/p90=53.6/100.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791919139902 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.1 мс | lag loop p99/max=1.3/1.8 мс
19:19:09 [cex] Binance 23 сд. задержка p50/p90=144.7/145.6 мс | Coinbase 39 задержка p50=81.2 мс | смещение часов +20.3 мс | lag loop p99/max=2.1/2.2 мс
19:19:09 [cex] binance_futures 38 сд. p50=152.4 мс | bybit 39 сд. p50=116.5 мс | bybit_book 125 сд. p50=112.3 мс | bybit_spot 76 сд. p50=115.0 мс | bybit_spot_book 47 сд. p50=111.9 мс | okx 16 сд. p50=147.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:19:09 [pm] T- 50.1s Up 0.35/0.36 Down 0.64/0.65 ptb=83099.3 | CLOB 9161 сообщ., задержка p50/p90=40.8/52.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791919149904 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.1 мс | lag loop p99/max=1.5/1.7 мс
19:19:19 [cex] Binance 12 сд. задержка p50/p90=144.6/145.7 мс | Coinbase 58 задержка p50=81.1 мс | смещение часов +20.3 мс | lag loop p99/max=1.9/2.0 мс
19:19:19 [cex] binance_futures 16 сд. p50=293.5 мс | bybit 5 сд. p50=114.0 мс | bybit_book 70 сд. p50=112.3 мс | bybit_spot 4 сд. p50=113.6 мс | bybit_spot_book 33 сд. p50=111.9 мс | okx 4 сд. p50=147.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
19:19:19 [pm] T- 40.1s Up 0.26/0.27 Down 0.73/0.74 ptb=83099.3 | CLOB 7467 сообщ., задержка p50/p90=60.6/121.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791919159905 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.1 мс | lag loop p99/max=1.6/1.9 мс
```

Представлено версией кода: ec1316a; python 3.12.3
