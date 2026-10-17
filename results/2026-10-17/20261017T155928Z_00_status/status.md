# Состояние сервера записи

Время (UTC): 2026-10-17 15:59:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 8 hours, 35 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         877         473           2         842        1028
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.37 / 0.34 / 0.26

## Данные
- файлов: 5456, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 220 | 30 МБ | 1 |
| bn_book | 220 | 3 МБ | 83 |
| bnf_agg | 220 | 45 МБ | 1 |
| bnf_book | 118 | 557 МБ | 367862 |
| bnf_depth5 | 118 | 41 МБ | 367938 |
| bnf_liq | 193 | 133 КБ | 115 |
| bs_trade | 118 | 1 МБ | 367858 |
| by_book1 | 220 | 96 МБ | 1 |
| by_liq | 195 | 106 КБ | 95 |
| by_trade | 220 | 30 МБ | 1 |
| bys_book1 | 104 | 39 МБ | 3 |
| bys_trade | 104 | 16 МБ | 20 |
| cb_ticker | 220 | 28 МБ | 1 |
| clock | 220 | 171 КБ | 56 |
| clock_pm | 220 | 171 КБ | 20 |
| events | 209 | 69 КБ | 505 |
| events_pm | 220 | 81 КБ | 726 |
| health_cex | 220 | 2 МБ | 5 |
| health_feeds | 220 | 8 МБ | 5 |
| health_pm | 220 | 2 МБ | 8 |
| kr_trade | 118 | 3 МБ | 367858 |
| ok_trade | 219 | 39 МБ | 1 |
| pm_depth | 220 | 45 МБ | 2 |
| pm_rtt | 220 | 1 МБ | 2 |
| pm_top | 220 | 92 МБ | 2 |
| pm_trades | 220 | 65 МБ | 4 |
| rtds | 220 | 14 МБ | 2 |
| windows | 220 | 456 КБ | 263 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 37, всего 287
- Polymarket CLOB: TCP 5, TLS 37, всего 80
- Polymarket gamma: TCP 5, TLS 36, всего 48

## Последние строки журнала записи
```
15:58:39 [pm] T- 80.7s Up 0.97/0.97 Down 0.03/0.03 ptb=81227.2 | CLOB 9618 сообщ., задержка p50/p90=37.4/40.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792252719329 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=1.3/1.8 мс
15:58:41 [cex] Binance 38 сд. задержка p50/p90=150.0/150.7 мс | Coinbase 33 задержка p50=82.4 мс | смещение часов +25.9 мс | lag loop p99/max=2.0/2.1 мс
15:58:41 [cex] binance_futures 35 сд. p50=259.9 мс | bybit 101 сд. p50=119.8 мс | bybit_book 116 сд. p50=118.0 мс | bybit_spot 114 сд. p50=119.9 мс | bybit_spot_book 95 сд. p50=117.8 мс | okx 30 сд. p50=159.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:58:49 [pm] T- 70.7s Up 0.96/0.96 Down 0.04/0.04 ptb=81227.2 | CLOB 9033 сообщ., задержка p50/p90=37.0/38.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792252729330 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=1.4/2.0 мс
15:58:51 [cex] Binance 16 сд. задержка p50/p90=149.7/150.7 мс | Coinbase 32 задержка p50=83.0 мс | смещение часов +25.9 мс | lag loop p99/max=2.2/2.2 мс
15:58:51 [cex] binance_futures 23 сд. p50=300.0 мс | bybit 22 сд. p50=119.2 мс | bybit_book 102 сд. p50=117.9 мс | bybit_spot 4 сд. p50=119.7 мс | bybit_spot_book 73 сд. p50=117.7 мс | okx 23 сд. p50=159.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:58:59 [pm] T- 60.7s Up 0.97/0.97 Down 0.03/0.03 ptb=81227.2 | CLOB 6531 сообщ., задержка p50/p90=36.8/38.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792252739332 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=1.2/2.1 мс
15:59:01 [cex] Binance 9 сд. задержка p50/p90=149.7/150.3 мс | Coinbase 52 задержка p50=82.4 мс | смещение часов +25.9 мс | lag loop p99/max=2.5/3.5 мс
15:59:01 [cex] binance_futures 42 сд. p50=251.7 мс | bybit 139 сд. p50=127.2 мс | bybit_book 70 сд. p50=118.0 мс | bybit_spot 126 сд. p50=120.8 мс | bybit_spot_book 53 сд. p50=117.9 мс | okx 45 сд. p50=160.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:59:09 [pm] T- 50.7s Up 0.99/0.99 Down 0.01/0.01 ptb=81227.2 | CLOB 5064 сообщ., задержка p50/p90=37.5/40.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792252749333 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.7/5.1 мс
15:59:11 [cex] Binance 21 сд. задержка p50/p90=149.7/150.7 мс | Coinbase 41 задержка p50=82.6 мс | смещение часов +25.9 мс | lag loop p99/max=2.1/3.0 мс
15:59:11 [cex] binance_futures 30 сд. p50=300.0 мс | bybit 17 сд. p50=119.1 мс | bybit_book 95 сд. p50=118.0 мс | bybit_spot 2 сд. p50=119.9 мс | bybit_spot_book 32 сд. p50=117.9 мс | okx 16 сд. p50=159.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:59:19 [pm] T- 40.7s Up 1.00/n/a Down n/a/0.00 ptb=81227.2 | CLOB 2694 сообщ., задержка p50/p90=40.0/41.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792252759335 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.2/2.2 мс
15:59:21 [cex] Binance 7 сд. задержка p50/p90=149.8/150.8 мс | Coinbase 44 задержка p50=82.9 мс | смещение часов +25.9 мс | lag loop p99/max=2.2/2.3 мс
15:59:21 [cex] binance_futures 25 сд. p50=300.0 мс | bybit 19 сд. p50=119.2 мс | bybit_book 90 сд. p50=118.0 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 30 сд. p50=118.0 мс | okx 19 сд. p50=159.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 8083be6; python 3.12.3
