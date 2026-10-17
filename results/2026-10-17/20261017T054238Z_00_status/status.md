# Состояние сервера записи

Время (UTC): 2026-10-17 05:42:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 22 hours, 18 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         851         562           2         778        1054
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.13 / 0.18 / 0.21

## Данные
- файлов: 5222, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 210 | 29 МБ | 1 |
| bn_book | 210 | 3 МБ | 21 |
| bnf_agg | 210 | 44 МБ | 1 |
| bnf_book | 118 | 557 МБ | 330852 |
| bnf_depth5 | 118 | 41 МБ | 330928 |
| bnf_liq | 187 | 128 КБ | 7760 |
| bs_trade | 118 | 1 МБ | 330848 |
| by_book1 | 210 | 92 МБ | 1 |
| by_liq | 187 | 104 КБ | 8202 |
| by_trade | 210 | 29 МБ | 1 |
| bys_book1 | 94 | 36 МБ | 1 |
| bys_trade | 94 | 14 МБ | 3 |
| cb_ticker | 210 | 27 МБ | 1 |
| clock | 210 | 163 КБ | 52 |
| clock_pm | 210 | 163 КБ | 14 |
| events | 199 | 66 КБ | 424 |
| events_pm | 210 | 77 КБ | 144 |
| health_cex | 210 | 2 МБ | 9 |
| health_feeds | 210 | 7 МБ | 9 |
| health_pm | 210 | 2 МБ | 4 |
| kr_trade | 118 | 3 МБ | 330848 |
| ok_trade | 209 | 38 МБ | 1 |
| pm_depth | 210 | 43 МБ | 2 |
| pm_rtt | 210 | 1 МБ | 4 |
| pm_top | 210 | 87 МБ | 2 |
| pm_trades | 210 | 62 МБ | 2 |
| rtds | 210 | 14 МБ | 2 |
| windows | 210 | 434 КБ | 274 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 38, всего 770
- Polymarket CLOB: TCP 5, TLS 37, всего 79
- Polymarket gamma: TCP 5, TLS 42, всего 53

## Последние строки журнала записи
```
05:41:53 [pm] T-186.1s Up 0.14/0.15 Down 0.85/0.86 ptb=81489.7 | CLOB 5172 сообщ., задержка p50/p90=61.5/65.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792215713909 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.9/1.9 мс
05:41:57 [cex] Binance 126 сд. задержка p50/p90=145.2/147.1 мс | Coinbase 89 задержка p50=93.0 мс | смещение часов +19.6 мс | lag loop p99/max=2.1/2.2 мс
05:41:57 [cex] binance_futures 167 сд. p50=145.4 мс | bybit 134 сд. p50=115.3 мс | bybit_book 76 сд. p50=111.3 мс | bybit_spot 164 сд. p50=115.9 мс | bybit_spot_book 53 сд. p50=110.9 мс | okx 116 сд. p50=154.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
05:42:03 [pm] T-176.1s Up 0.12/0.13 Down 0.87/0.88 ptb=81489.7 | CLOB 3606 сообщ., задержка p50/p90=61.4/101.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792215723910 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=10.7/12.0 мс
05:42:07 [cex] Binance 54 сд. задержка p50/p90=144.3/145.2 мс | Coinbase 28 задержка p50=76.4 мс | смещение часов +19.6 мс | lag loop p99/max=5.1/5.9 мс
05:42:07 [cex] binance_futures 45 сд. p50=293.5 мс | bybit 5 сд. p50=113.3 мс | bybit_book 41 сд. p50=111.3 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 16 сд. p50=111.5 мс | okx 4 сд. p50=153.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
05:42:13 [pm] T-166.1s Up 0.11/0.12 Down 0.88/0.89 ptb=81489.7 | CLOB 2378 сообщ., задержка p50/p90=61.0/63.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792215733911 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.5/2.1 мс
05:42:17 [cex] Binance 157 сд. задержка p50/p90=144.9/146.2 мс | Coinbase 145 задержка p50=197.1 мс | смещение часов +19.6 мс | lag loop p99/max=2.1/2.2 мс
05:42:17 [cex] binance_futures 151 сд. p50=146.8 мс | bybit 28 сд. p50=115.1 мс | bybit_book 59 сд. p50=111.2 мс | bybit_spot 70 сд. p50=115.4 мс | bybit_spot_book 47 сд. p50=111.1 мс | okx 32 сд. p50=154.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
05:42:23 [pm] T-156.1s Up 0.06/0.07 Down 0.93/0.94 ptb=81489.7 | CLOB 5135 сообщ., задержка p50/p90=61.3/66.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792215743913 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.5/1.6 мс
05:42:27 [cex] Binance 81 сд. задержка p50/p90=144.2/145.2 мс | Coinbase 37 задержка p50=76.4 мс | смещение часов +19.6 мс | lag loop p99/max=2.1/2.2 мс
05:42:27 [cex] binance_futures 47 сд. p50=293.3 мс | bybit 2 сд. p50=112.9 мс | bybit_book 57 сд. p50=111.3 мс | bybit_spot 2 сд. p50=114.4 мс | bybit_spot_book 33 сд. p50=111.0 мс | okx 10 сд. p50=153.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
05:42:33 [pm] T-146.1s Up 0.04/0.05 Down 0.95/0.96 ptb=81489.7 | CLOB 2363 сообщ., задержка p50/p90=59.3/80.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792215753914 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.0/2.0 мс
05:42:37 [cex] Binance 53 сд. задержка p50/p90=144.3/145.2 мс | Coinbase 25 задержка p50=76.9 мс | смещение часов +19.6 мс | lag loop p99/max=2.2/2.5 мс
05:42:37 [cex] binance_futures 43 сд. p50=293.4 мс | bybit 5 сд. p50=112.6 мс | bybit_book 78 сд. p50=111.3 мс | bybit_spot 1 сд. p50=113.4 мс | bybit_spot_book 13 сд. p50=111.1 мс | okx 17 сд. p50=154.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 8083be6; python 3.12.3
