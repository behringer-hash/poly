# Состояние сервера записи

Время (UTC): 2026-10-17 14:57:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 7 hours, 33 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         875         484           2         833        1030
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.19 / 0.23 / 0.22

## Данные
- файлов: 5432, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 219 | 29 МБ | 2 |
| bn_book | 219 | 3 МБ | 32 |
| bnf_agg | 219 | 45 МБ | 2 |
| bnf_book | 118 | 557 МБ | 364152 |
| bnf_depth5 | 118 | 41 МБ | 364228 |
| bnf_liq | 192 | 129 КБ | 361 |
| bs_trade | 118 | 1 МБ | 364148 |
| by_book1 | 219 | 95 МБ | 2 |
| by_liq | 194 | 105 КБ | 2469 |
| by_trade | 219 | 29 МБ | 6 |
| bys_book1 | 103 | 38 МБ | 2 |
| bys_trade | 103 | 15 МБ | 12 |
| cb_ticker | 219 | 28 МБ | 2 |
| clock | 219 | 170 КБ | 37 |
| clock_pm | 219 | 170 КБ | 1 |
| events | 208 | 69 КБ | 438 |
| events_pm | 219 | 80 КБ | 13 |
| health_cex | 219 | 2 МБ | 6 |
| health_feeds | 219 | 7 МБ | 6 |
| health_pm | 219 | 2 МБ | 9 |
| kr_trade | 118 | 3 МБ | 364148 |
| ok_trade | 218 | 39 МБ | 2 |
| pm_depth | 219 | 45 МБ | 1 |
| pm_rtt | 219 | 1 МБ | 1 |
| pm_top | 219 | 91 МБ | 1 |
| pm_trades | 219 | 65 МБ | 1 |
| rtds | 219 | 14 МБ | 1 |
| windows | 219 | 454 КБ | 93 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 44, всего 295
- Polymarket CLOB: TCP 5, TLS 41, всего 87
- Polymarket gamma: TCP 5, TLS 50, всего 62

## Последние строки журнала записи
```
14:56:58 [pm] T-181.2s Up 0.73/0.74 Down 0.26/0.27 ptb=81466.3 | CLOB 8661 сообщ., задержка p50/p90=44.6/49.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792249018789 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.5/3.5 мс
14:57:01 [cex] Binance 112 сд. задержка p50/p90=144.1/145.3 мс | Coinbase 50 задержка p50=77.3 мс | смещение часов +20.2 мс | lag loop p99/max=2.8/3.0 мс
14:57:01 [cex] binance_futures 140 сд. p50=146.4 мс | bybit 214 сд. p50=114.2 мс | bybit_book 151 сд. p50=112.2 мс | bybit_spot 271 сд. p50=115.2 мс | bybit_spot_book 120 сд. p50=111.8 мс | okx 194 сд. p50=155.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:57:08 [pm] T-171.2s Up 0.68/0.69 Down 0.31/0.32 ptb=81466.3 | CLOB 7917 сообщ., задержка p50/p90=44.7/47.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792249028790 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.4/1.8 мс
14:57:11 [cex] Binance 66 сд. задержка p50/p90=149.7/150.4 мс | Coinbase 31 задержка p50=81.2 мс | смещение часов +24.9 мс | lag loop p99/max=2.3/2.4 мс
14:57:11 [cex] binance_futures 34 сд. p50=151.3 мс | bybit 21 сд. p50=119.0 мс | bybit_book 77 сд. p50=117.0 мс | bybit_spot 173 сд. p50=119.3 мс | bybit_spot_book 112 сд. p50=116.5 мс | okx 42 сд. p50=158.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:57:18 [pm] T-161.2s Up 0.72/0.73 Down 0.27/0.28 ptb=81466.3 | CLOB 3794 сообщ., задержка p50/p90=42.4/44.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792249038792 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.4/1.9 мс
14:57:21 [cex] Binance 20 сд. задержка p50/p90=148.7/149.7 мс | Coinbase 50 задержка p50=81.4 мс | смещение часов +24.9 мс | lag loop p99/max=2.1/2.2 мс
14:57:21 [cex] binance_futures 14 сд. p50=299.0 мс | bybit 1 сд. p50=118.0 мс | bybit_book 32 сд. p50=117.0 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 10 сд. p50=116.5 мс | okx 7 сд. p50=158.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:57:25 [pm] RTDS[chainlink] разорван (ConnectionClosedError(None, None, None)), переподключение через 2 с
14:57:27 [pm] RTDS[chainlink] подключён
14:57:28 [pm] T-151.2s Up 0.77/0.78 Down 0.22/0.23 ptb=81466.3 | CLOB 3559 сообщ., задержка p50/p90=43.0/45.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792249048793 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.2/16.8 мс
14:57:31 [cex] Binance 21 сд. задержка p50/p90=148.7/148.9 мс | Coinbase 23 задержка p50=80.8 мс | смещение часов +24.9 мс | lag loop p99/max=2.2/2.2 мс
14:57:31 [cex] binance_futures 9 сд. p50=299.1 мс | bybit 4 сд. p50=119.3 мс | bybit_book 49 сд. p50=117.0 мс | bybit_spot 2 сд. p50=119.1 мс | bybit_spot_book 22 сд. p50=116.6 мс | okx 3 сд. p50=158.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:57:38 [pm] T-141.2s Up 0.77/0.78 Down 0.22/0.23 ptb=81466.3 | CLOB 6620 сообщ., задержка p50/p90=41.9/44.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792249058795 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.4/3.1 мс
```

Представлено версией кода: 8083be6; python 3.12.3
