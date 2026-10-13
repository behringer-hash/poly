# Состояние сервера записи

Время (UTC): 2026-10-13 15:11:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 6 days, 7 hours, 48 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         527        1006           2         552        1378
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.20 / 0.23 / 0.20

## Данные
- файлов: 3172, всего 869 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 124 | 15 МБ | 2 |
| bn_book | 124 | 1 МБ | 12 |
| bnf_agg | 124 | 23 МБ | 2 |
| bnf_book | 118 | 557 МБ | 19412 |
| bnf_depth5 | 118 | 41 МБ | 19488 |
| bnf_liq | 110 | 68 КБ | 603 |
| bs_trade | 118 | 1 МБ | 19408 |
| by_book1 | 124 | 48 МБ | 2 |
| by_liq | 104 | 59 КБ | 3096 |
| by_trade | 124 | 15 МБ | 2 |
| bys_book1 | 8 | 3 МБ | 2 |
| bys_trade | 8 | 2 МБ | 2 |
| cb_ticker | 124 | 13 МБ | 2 |
| clock | 124 | 95 КБ | 56 |
| clock_pm | 124 | 95 КБ | 56 |
| events | 115 | 39 КБ | 7035 |
| events_pm | 124 | 46 КБ | 40 |
| health_cex | 124 | 1 МБ | 10 |
| health_feeds | 124 | 5 МБ | 10 |
| health_pm | 124 | 1 МБ | 9 |
| kr_trade | 118 | 3 МБ | 19408 |
| ok_trade | 123 | 20 МБ | 2 |
| pm_depth | 124 | 24 МБ | 1 |
| pm_rtt | 124 | 823 КБ | 5 |
| pm_top | 124 | 49 МБ | 1 |
| pm_trades | 124 | 36 МБ | 1 |
| rtds | 124 | 8 МБ | 1 |
| windows | 124 | 254 КБ | 144 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 41, всего 291
- Polymarket CLOB: TCP 5, TLS 40, всего 91
- Polymarket gamma: TCP 8, TLS 51, всего 69

## Последние строки журнала записи
```
15:11:18 [pm] RTDS[rtds_binance] разорван (ConnectionClosedOK(Close(code=1001, reason='Going away'), Close(code=1001, reason='Going away'), True)), переподключение через 2 с
15:11:20 [pm] RTDS[rtds_binance] подключён
15:11:20 [pm] RTDS[chainlink] подключён
15:11:27 [cex] Binance 198 сд. задержка p50/p90=146.6/148.5 мс | Coinbase 71 задержка p50=79.7 мс | смещение часов +20.7 мс | lag loop p99/max=2.0/2.0 мс
15:11:27 [cex] binance_futures 217 сд. p50=146.1 мс | bybit 202 сд. p50=117.8 мс | bybit_book 231 сд. p50=112.8 мс | bybit_spot 379 сд. p50=115.2 мс | bybit_spot_book 181 сд. p50=112.4 мс | okx 233 сд. p50=155.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:11:27 [pm] T-212.1s Up 0.55/0.56 Down 0.44/0.45 ptb=83467.1 | CLOB 9516 сообщ., задержка p50/p90=67.3/114.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791904287859 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=1.7/3.5 мс
15:11:37 [cex] Binance 132 сд. задержка p50/p90=146.0/146.9 мс | Coinbase 61 задержка p50=81.1 мс | смещение часов +20.7 мс | lag loop p99/max=1.8/2.1 мс
15:11:37 [cex] binance_futures 164 сд. p50=145.9 мс | bybit 82 сд. p50=116.4 мс | bybit_book 197 сд. p50=112.8 мс | bybit_spot 127 сд. p50=115.4 мс | bybit_spot_book 144 сд. p50=112.3 мс | okx 191 сд. p50=155.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:11:37 [pm] T-202.1s Up 0.72/0.73 Down 0.27/0.28 ptb=83467.1 | CLOB 8849 сообщ., задержка p50/p90=61.2/64.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791904297860 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=2.1/5.1 мс
15:11:47 [cex] Binance 121 сд. задержка p50/p90=145.6/147.0 мс | Coinbase 63 задержка p50=80.7 мс | смещение часов +20.7 мс | lag loop p99/max=2.1/2.2 мс
15:11:47 [cex] binance_futures 204 сд. p50=146.8 мс | bybit 177 сд. p50=114.8 мс | bybit_book 246 сд. p50=112.8 мс | bybit_spot 217 сд. p50=115.7 мс | bybit_spot_book 162 сд. p50=112.4 мс | okx 187 сд. p50=156.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:11:47 [pm] T-192.1s Up 0.70/0.71 Down 0.29/0.30 ptb=83467.1 | CLOB 8251 сообщ., задержка p50/p90=61.4/64.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791904307861 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.6 мс | lag loop p99/max=1.7/1.7 мс
15:11:57 [cex] Binance 13 сд. задержка p50/p90=145.1/146.1 мс | Coinbase 32 задержка p50=79.3 мс | смещение часов +20.7 мс | lag loop p99/max=1.9/2.2 мс
15:11:57 [cex] binance_futures 62 сд. p50=184.8 мс | bybit 32 сд. p50=114.4 мс | bybit_book 202 сд. p50=112.8 мс | bybit_spot 66 сд. p50=115.0 мс | bybit_spot_book 78 сд. p50=112.4 мс | okx 40 сд. p50=155.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:11:57 [pm] T-182.1s Up 0.73/0.74 Down 0.26/0.27 ptb=83467.1 | CLOB 5977 сообщ., задержка p50/p90=61.2/66.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791904317863 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=1.1/1.2 мс
```

Представлено версией кода: ec1316a; python 3.12.3
