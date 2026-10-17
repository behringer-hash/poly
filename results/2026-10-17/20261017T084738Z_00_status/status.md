# Состояние сервера записи

Время (UTC): 2026-10-17 08:47:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 1 hour, 23 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         860         539           2         793        1045
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.23 / 0.25 / 0.20

## Данные
- файлов: 5290, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 213 | 29 МБ | 1 |
| bn_book | 213 | 3 МБ | 9 |
| bnf_agg | 213 | 44 МБ | 1 |
| bnf_book | 118 | 557 МБ | 341952 |
| bnf_depth5 | 118 | 41 МБ | 342028 |
| bnf_liq | 188 | 128 КБ | 3575 |
| bs_trade | 118 | 1 МБ | 341948 |
| by_book1 | 213 | 92 МБ | 1 |
| by_liq | 188 | 104 КБ | 4452 |
| by_trade | 213 | 29 МБ | 1 |
| bys_book1 | 97 | 36 МБ | 1 |
| bys_trade | 97 | 15 МБ | 9 |
| cb_ticker | 213 | 27 МБ | 1 |
| clock | 213 | 165 КБ | 25 |
| clock_pm | 213 | 165 КБ | 52 |
| events | 202 | 66 КБ | 521 |
| events_pm | 213 | 78 КБ | 1006 |
| health_cex | 213 | 2 МБ | 9 |
| health_feeds | 213 | 7 МБ | 9 |
| health_pm | 213 | 2 МБ | 1 |
| kr_trade | 118 | 3 МБ | 341948 |
| ok_trade | 212 | 39 МБ | 5 |
| pm_depth | 213 | 43 МБ | 1 |
| pm_rtt | 213 | 1 МБ | 1 |
| pm_top | 213 | 88 МБ | 1 |
| pm_trades | 213 | 63 МБ | 1 |
| rtds | 213 | 14 МБ | 1 |
| windows | 213 | 441 КБ | 94 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 290
- Polymarket CLOB: TCP 5, TLS 37, всего 76
- Polymarket gamma: TCP 5, TLS 40, всего 52

## Последние строки журнала записи
```
08:46:55 [pm] T-184.5s Up 0.56/0.57 Down 0.43/0.44 ptb=81566.9 | CLOB 5671 сообщ., задержка p50/p90=44.5/80.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792226815537 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=1.9/2.0 мс
08:46:58 [cex] Binance 60 сд. задержка p50/p90=146.8/147.8 мс | Coinbase 73 задержка p50=82.0 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/2.4 мс
08:46:58 [cex] binance_futures 54 сд. p50=295.6 мс | bybit 18 сд. p50=115.9 мс | bybit_book 71 сд. p50=114.2 мс | bybit_spot 2 сд. p50=116.4 мс | bybit_spot_book 19 сд. p50=114.1 мс | okx 12 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:47:05 [pm] T-174.5s Up 0.80/0.81 Down 0.19/0.20 ptb=81566.9 | CLOB 4137 сообщ., задержка p50/p90=44.0/54.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792226825538 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=2.1/4.3 мс
08:47:08 [cex] Binance 84 сд. задержка p50/p90=147.0/147.9 мс | Coinbase 37 задержка p50=79.7 мс | смещение часов +22.1 мс | lag loop p99/max=2.7/3.8 мс
08:47:08 [cex] binance_futures 83 сд. p50=256.4 мс | bybit 71 сд. p50=116.1 мс | bybit_book 165 сд. p50=114.1 мс | bybit_spot 150 сд. p50=117.2 мс | bybit_spot_book 38 сд. p50=114.0 мс | okx 97 сд. p50=157.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:47:15 [pm] T-164.5s Up 0.86/0.87 Down 0.13/0.14 ptb=81566.9 | CLOB 5043 сообщ., задержка p50/p90=43.5/48.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792226835540 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=2.0/2.2 мс
08:47:18 [cex] Binance 126 сд. задержка p50/p90=145.8/147.1 мс | Coinbase 27 задержка p50=77.6 мс | смещение часов +20.6 мс | lag loop p99/max=2.1/2.2 мс
08:47:18 [cex] binance_futures 70 сд. p50=294.0 мс | bybit 30 сд. p50=114.2 мс | bybit_book 179 сд. p50=112.7 мс | bybit_spot 35 сд. p50=115.1 мс | bybit_spot_book 37 сд. p50=112.8 мс | okx 38 сд. p50=157.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:47:25 [pm] T-154.5s Up 0.86/0.87 Down 0.13/0.14 ptb=81566.9 | CLOB 3461 сообщ., задержка p50/p90=42.9/44.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792226845541 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=2.1/2.1 мс
08:47:28 [cex] Binance 83 сд. задержка p50/p90=145.5/146.2 мс | Coinbase 27 задержка p50=77.2 мс | смещение часов +20.6 мс | lag loop p99/max=2.1/2.1 мс
08:47:28 [cex] binance_futures 54 сд. p50=294.0 мс | bybit 32 сд. p50=114.9 мс | bybit_book 189 сд. p50=112.7 мс | bybit_spot 13 сд. p50=115.4 мс | bybit_spot_book 22 сд. p50=112.6 мс | okx 23 сд. p50=155.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:47:35 [pm] T-144.5s Up 0.89/0.90 Down 0.10/0.11 ptb=81566.9 | CLOB 2844 сообщ., задержка p50/p90=43.1/45.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792226855543 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=1.9/2.0 мс
08:47:38 [cex] Binance 46 сд. задержка p50/p90=145.3/145.8 мс | Coinbase 25 задержка p50=77.1 мс | смещение часов +20.6 мс | lag loop p99/max=2.2/2.5 мс
08:47:38 [cex] binance_futures 50 сд. p50=294.0 мс | bybit 8 сд. p50=114.1 мс | bybit_book 223 сд. p50=112.6 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 18 сд. p50=112.5 мс | okx 5 сд. p50=154.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 8083be6; python 3.12.3
