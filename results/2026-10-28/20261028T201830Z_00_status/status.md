# Состояние сервера записи

Время (UTC): 2026-10-28 20:18:30

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 12 hours, 54 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 12 ГБ из 57 ГБ, свободно 45 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         628         735           1         717        1277
Swap:           2047         304        1743
```
- нагрузка CPU (1/5/15 мин): 1.40 / 1.50 / 1.41

## Данные
- файлов: 5829, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 243 | 35 МБ | 0 |
| bn_book | 243 | 3 МБ | 6 |
| bnf_agg | 243 | 50 МБ | 0 |
| bnf_book | 56 | 385 МБ | 0 |
| bnf_liq | 212 | 138 КБ | 38 |
| by_book1 | 243 | 109 МБ | 0 |
| by_liq | 227 | 101 КБ | 207 |
| by_trade | 243 | 35 МБ | 0 |
| bys_book1 | 243 | 83 МБ | 0 |
| bys_trade | 243 | 33 МБ | 0 |
| cb_ticker | 243 | 32 МБ | 0 |
| clock | 243 | 188 КБ | 22 |
| clock_pm | 243 | 188 КБ | 53 |
| events | 233 | 74 КБ | 2069 |
| events_pm | 241 | 83 КБ | 2260 |
| health_cex | 243 | 2 МБ | 8 |
| health_feeds | 243 | 7 МБ | 8 |
| health_pm | 243 | 3 МБ | 1 |
| ok_trade | 243 | 44 МБ | 0 |
| pm_depth | 243 | 50 МБ | 1 |
| pm_rtt | 243 | 2 МБ | 3 |
| pm_top | 243 | 101 МБ | 1 |
| pm_trades | 243 | 71 МБ | 1 |
| rtds | 243 | 16 МБ | 1 |
| windows | 243 | 500 КБ | 297 |

Дни с данными: 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 36, всего 284
- Polymarket CLOB: TCP 5, TLS 38, всего 80
- Polymarket gamma: TCP 5, TLS 65, всего 78

## Последние строки журнала записи
```
20:17:41 [cex] Binance 155 сд. задержка p50/p90=167.1/183.0 мс | Coinbase 55 задержка p50=114.3 мс | смещение часов +41.9 мс | lag loop p99/max=21.5/28.0 мс
20:17:41 [cex] binance_futures 205 сд. p50=177.2 мс | bybit 257 сд. p50=142.1 мс | bybit_book 272 сд. p50=133.2 мс | bybit_spot 341 сд. p50=138.2 мс | bybit_spot_book 222 сд. p50=133.9 мс | okx 151 сд. p50=180.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 9748 сд. p50=166.9 мс
20:17:48 [pm] T-131.5s Up 0.07/0.08 Down 0.92/0.93 ptb=81246.2 | CLOB 4458 сообщ., задержка p50/p90=54.0/60.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793218668506 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.8 мс | lag loop p99/max=2.4/3.0 мс
20:17:51 [cex] Binance 286 сд. задержка p50/p90=176.9/180.4 мс | Coinbase 97 задержка p50=114.5 мс | смещение часов +41.9 мс | lag loop p99/max=16.6/17.0 мс
20:17:51 [cex] binance_futures 188 сд. p50=177.8 мс | bybit 158 сд. p50=136.2 мс | bybit_book 285 сд. p50=133.1 мс | bybit_spot 181 сд. p50=145.4 мс | bybit_spot_book 191 сд. p50=133.8 мс | okx 266 сд. p50=184.4 мс | binance_liq 2 сд. p50=1172.0 мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 7660 сд. p50=179.1 мс
20:17:58 [pm] T-121.5s Up 0.03/0.04 Down 0.96/0.97 ptb=81246.2 | CLOB 2856 сообщ., задержка p50/p90=54.2/97.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793218678507 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.8 мс | lag loop p99/max=2.1/2.3 мс
20:18:01 [cex] Binance 79 сд. задержка p50/p90=171.0/189.5 мс | Coinbase 59 задержка p50=120.0 мс | смещение часов +41.9 мс | lag loop p99/max=11.7/12.2 мс
20:18:01 [cex] binance_futures 138 сд. p50=189.1 мс | bybit 266 сд. p50=135.4 мс | bybit_book 260 сд. p50=133.1 мс | bybit_spot 200 сд. p50=138.7 мс | bybit_spot_book 148 сд. p50=133.8 мс | okx 181 сд. p50=181.2 мс | binance_liq 1 сд. p50=1031.1 мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3812 сд. p50=172.3 мс
20:18:08 [pm] T-111.5s Up 0.04/0.05 Down 0.95/0.96 ptb=81246.2 | CLOB 2975 сообщ., задержка p50/p90=54.2/60.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793218688509 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.8 мс | lag loop p99/max=3.2/5.3 мс
20:18:11 [cex] Binance 61 сд. задержка p50/p90=165.9/177.3 мс | Coinbase 50 задержка p50=112.3 мс | смещение часов +33.6 мс | lag loop p99/max=15.8/18.9 мс
20:18:11 [cex] binance_futures 84 сд. p50=268.1 мс | bybit 85 сд. p50=135.3 мс | bybit_book 269 сд. p50=133.0 мс | bybit_spot 188 сд. p50=137.5 мс | bybit_spot_book 132 сд. p50=133.6 мс | okx 53 сд. p50=179.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4635 сд. p50=166.0 мс
20:18:18 [pm] T-101.5s Up 0.02/0.03 Down 0.97/0.98 ptb=81246.2 | CLOB 3113 сообщ., задержка p50/p90=53.5/56.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793218698512 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.7 мс | lag loop p99/max=1.9/2.1 мс
20:18:21 [cex] Binance 56 сд. задержка p50/p90=171.4/183.4 мс | Coinbase 47 задержка p50=105.8 мс | смещение часов +33.6 мс | lag loop p99/max=2.3/22.4 мс
20:18:21 [cex] binance_futures 55 сд. p50=289.9 мс | bybit 129 сд. p50=156.4 мс | bybit_book 182 сд. p50=124.9 мс | bybit_spot 98 сд. p50=137.8 мс | bybit_spot_book 98 сд. p50=125.4 мс | okx 43 сд. p50=171.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1601 сд. p50=158.4 мс
20:18:28 [pm] T- 91.5s Up n/a/0.01 Down 0.99/n/a ptb=81246.2 | CLOB 2286 сообщ., задержка p50/p90=56.0/71.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793218708514 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=2.7/8.5 мс
```

Представлено версией кода: 65c4468; python 3.12.3
