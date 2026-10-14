# Состояние сервера записи

Время (UTC): 2026-10-14 01:28:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 6 days, 18 hours, 5 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         554         628           2         905        1351
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.05 / 0.09 / 0.13

## Данные
- файлов: 3412, всего 898 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 134 | 16 МБ | 1 |
| bn_book | 134 | 1 МБ | 12 |
| bnf_agg | 134 | 25 МБ | 1 |
| bnf_book | 118 | 557 МБ | 56432 |
| bnf_depth5 | 118 | 41 МБ | 56509 |
| bnf_liq | 118 | 72 КБ | 167 |
| bs_trade | 118 | 1 МБ | 56428 |
| by_book1 | 134 | 54 МБ | 1 |
| by_liq | 115 | 61 КБ | 738 |
| by_trade | 134 | 16 МБ | 1 |
| bys_book1 | 18 | 6 МБ | 1 |
| bys_trade | 18 | 3 МБ | 1 |
| cb_ticker | 134 | 15 МБ | 1 |
| clock | 134 | 103 КБ | 12 |
| clock_pm | 134 | 103 КБ | 10 |
| events | 126 | 42 КБ | 1718 |
| events_pm | 134 | 50 КБ | 65 |
| health_cex | 134 | 1 МБ | 5 |
| health_feeds | 134 | 5 МБ | 5 |
| health_pm | 134 | 1 МБ | 4 |
| kr_trade | 118 | 3 МБ | 56428 |
| ok_trade | 133 | 22 МБ | 1 |
| pm_depth | 134 | 27 МБ | 0 |
| pm_rtt | 134 | 902 КБ | 0 |
| pm_top | 134 | 54 МБ | 0 |
| pm_trades | 134 | 39 МБ | 0 |
| rtds | 134 | 9 МБ | 0 |
| windows | 134 | 276 КБ | 24 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 38, всего 288
- Polymarket CLOB: TCP 5, TLS 38, всего 82
- Polymarket gamma: TCP 5, TLS 38, всего 49

## Последние строки журнала записи
```
01:28:11 [cex] Binance 413 сд. задержка p50/p90=156.2/166.3 мс | Coinbase 63 задержка p50=83.3 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/2.5 мс
01:28:11 [cex] binance_futures 309 сд. p50=148.3 мс | bybit 314 сд. p50=117.6 мс | bybit_book 236 сд. p50=114.1 мс | bybit_spot 169 сд. p50=117.4 мс | bybit_spot_book 127 сд. p50=113.6 мс | okx 298 сд. p50=152.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:28:13 [pm] T-106.8s Up 0.03/0.04 Down 0.96/0.97 ptb=83307.3 | CLOB 5832 сообщ., задержка p50/p90=45.0/74.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791941293168 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.1 мс | lag loop p99/max=1.9/2.0 мс
01:28:21 [cex] Binance 104 сд. задержка p50/p90=147.3/148.2 мс | Coinbase 38 задержка p50=82.8 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/2.4 мс
01:28:21 [cex] binance_futures 121 сд. p50=148.3 мс | bybit 129 сд. p50=116.2 мс | bybit_book 235 сд. p50=114.1 мс | bybit_spot 103 сд. p50=116.2 мс | bybit_spot_book 99 сд. p50=113.4 мс | okx 187 сд. p50=150.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:28:23 [pm] T- 96.8s Up n/a/0.01 Down 0.99/n/a ptb=83307.3 | CLOB 2261 сообщ., задержка p50/p90=45.2/56.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791941303170 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.2 мс | lag loop p99/max=1.9/2.1 мс
01:28:31 [cex] Binance 14 сд. задержка p50/p90=147.2/148.2 мс | Coinbase 35 задержка p50=82.7 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/2.2 мс
01:28:31 [cex] binance_futures 56 сд. p50=148.6 мс | bybit 99 сд. p50=115.5 мс | bybit_book 316 сд. p50=114.1 мс | bybit_spot 55 сд. p50=119.7 мс | bybit_spot_book 68 сд. p50=113.6 мс | okx 39 сд. p50=149.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:28:33 [pm] T- 86.8s Up n/a/0.01 Down 0.99/n/a ptb=83307.3 | CLOB 1314 сообщ., задержка p50/p90=45.0/52.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791941313171 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.2 мс | lag loop p99/max=2.1/2.2 мс
01:28:41 [cex] Binance 123 сд. задержка p50/p90=147.4/147.7 мс | Coinbase 47 задержка p50=83.2 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/2.2 мс
01:28:41 [cex] binance_futures 189 сд. p50=147.8 мс | bybit 275 сд. p50=116.0 мс | bybit_book 433 сд. p50=114.1 мс | bybit_spot 276 сд. p50=116.6 мс | bybit_spot_book 151 сд. p50=113.5 мс | okx 134 сд. p50=149.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:28:43 [pm] T- 76.8s Up n/a/0.01 Down 0.99/n/a ptb=83307.3 | CLOB 1948 сообщ., задержка p50/p90=44.5/54.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791941323172 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.2 мс | lag loop p99/max=2.1/2.1 мс
01:28:51 [cex] Binance 33 сд. задержка p50/p90=147.0/147.2 мс | Coinbase 53 задержка p50=81.4 мс | смещение часов +20.5 мс | lag loop p99/max=2.0/2.1 мс
01:28:51 [cex] binance_futures 29 сд. p50=275.6 мс | bybit 54 сд. p50=115.1 мс | bybit_book 277 сд. p50=112.8 мс | bybit_spot 24 сд. p50=115.1 мс | bybit_spot_book 65 сд. p50=112.7 мс | okx 47 сд. p50=147.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:28:53 [pm] T- 66.8s Up n/a/0.01 Down 0.99/n/a ptb=83307.3 | CLOB 823 сообщ., задержка p50/p90=43.4/52.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791941333173 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.2 мс | lag loop p99/max=2.0/2.1 мс
```

Представлено версией кода: ec1316a; python 3.12.3
