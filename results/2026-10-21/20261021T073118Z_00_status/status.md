# Состояние сервера записи

Время (UTC): 2026-10-21 07:31:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 7 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 9 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         735         385           2         973        1170
Swap:           2047         245        1802
```
- нагрузка CPU (1/5/15 мин): 0.51 / 0.45 / 0.43

## Данные
- файлов: 7552, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 308 | 40 МБ | 1 |
| bn_book | 308 | 4 МБ | 8 |
| bnf_agg | 308 | 61 МБ | 1 |
| bnf_book | 118 | 557 МБ | 682972 |
| bnf_depth5 | 118 | 41 МБ | 683048 |
| bnf_liq | 270 | 174 КБ | 32 |
| bs_trade | 118 | 1 МБ | 682968 |
| by_book1 | 308 | 128 МБ | 1 |
| by_liq | 278 | 136 КБ | 70 |
| by_trade | 308 | 40 МБ | 1 |
| bys_book1 | 192 | 65 МБ | 1 |
| bys_trade | 192 | 25 МБ | 1 |
| cb_ticker | 308 | 38 МБ | 1 |
| clock | 308 | 238 КБ | 32 |
| clock_pm | 308 | 238 КБ | 33 |
| events | 297 | 95 КБ | 535 |
| events_pm | 308 | 111 КБ | 64 |
| health_cex | 308 | 3 МБ | 1 |
| health_feeds | 308 | 10 МБ | 1 |
| health_pm | 308 | 3 МБ | 1 |
| kr_trade | 118 | 3 МБ | 682968 |
| ok_trade | 307 | 53 МБ | 1 |
| pm_depth | 308 | 61 МБ | 1 |
| pm_rtt | 308 | 2 МБ | 3 |
| pm_top | 308 | 126 МБ | 1 |
| pm_trades | 308 | 89 МБ | 1 |
| rtds | 308 | 20 МБ | 1 |
| windows | 308 | 636 КБ | 194 |

Дни с данными: 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 40, всего 289
- Polymarket CLOB: TCP 5, TLS 44, всего 92
- Polymarket gamma: TCP 5, TLS 63, всего 73

## Последние строки журнала записи
```
07:30:35 [cex] Binance 205 сд. задержка p50/p90=144.5/145.7 мс | Coinbase 62 задержка p50=78.6 мс | смещение часов +20.3 мс | lag loop p99/max=2.0/2.1 мс
07:30:35 [cex] binance_futures 269 сд. p50=147.8 мс | bybit 656 сд. p50=114.9 мс | bybit_book 293 сд. p50=112.4 мс | bybit_spot 266 сд. p50=116.2 мс | bybit_spot_book 242 сд. p50=111.7 мс | okx 297 сд. p50=147.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:30:35 [pm] T-264.0s Up 0.88/0.89 Down 0.11/0.12 ptb=82905.8 | CLOB 6880 сообщ., задержка p50/p90=40.8/89.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792567835994 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.2 мс | lag loop p99/max=2.2/2.3 мс
07:30:45 [cex] Binance 358 сд. задержка p50/p90=145.8/151.8 мс | Coinbase 69 задержка p50=78.9 мс | смещение часов +20.6 мс | lag loop p99/max=2.2/2.4 мс
07:30:45 [cex] binance_futures 428 сд. p50=148.9 мс | bybit 937 сд. p50=115.3 мс | bybit_book 474 сд. p50=112.4 мс | bybit_spot 320 сд. p50=116.9 мс | bybit_spot_book 354 сд. p50=111.7 мс | okx 784 сд. p50=147.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:30:45 [pm] T-254.0s Up 0.90/0.91 Down 0.09/0.10 ptb=82905.8 | CLOB 5971 сообщ., задержка p50/p90=44.1/91.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792567845996 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.2 мс | lag loop p99/max=1.3/1.9 мс
07:30:55 [cex] Binance 24 сд. задержка p50/p90=144.5/145.6 мс | Coinbase 25 задержка p50=77.7 мс | смещение часов +20.6 мс | lag loop p99/max=2.0/2.3 мс
07:30:55 [cex] binance_futures 69 сд. p50=260.9 мс | bybit 129 сд. p50=114.4 мс | bybit_book 245 сд. p50=112.6 мс | bybit_spot 119 сд. p50=115.5 мс | bybit_spot_book 378 сд. p50=112.0 мс | okx 127 сд. p50=147.1 мс | binance_liq 1 сд. p50=1140.9 мс | bybit_liq 0 сд. p50=n/a мс
07:30:55 [pm] T-244.0s Up 0.91/0.92 Down 0.08/0.09 ptb=82905.8 | CLOB 4657 сообщ., задержка p50/p90=43.4/49.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792567855998 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.1 мс | lag loop p99/max=2.0/2.2 мс
07:31:05 [cex] Binance 177 сд. задержка p50/p90=146.1/148.9 мс | Coinbase 35 задержка p50=78.4 мс | смещение часов +20.6 мс | lag loop p99/max=2.1/2.1 мс
07:31:05 [cex] binance_futures 276 сд. p50=148.1 мс | bybit 530 сд. p50=114.9 мс | bybit_book 310 сд. p50=112.6 мс | bybit_spot 364 сд. p50=116.3 мс | bybit_spot_book 253 сд. p50=112.0 мс | okx 360 сд. p50=147.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:31:06 [pm] T-234.0s Up 0.90/0.91 Down 0.09/0.10 ptb=82905.8 | CLOB 6746 сообщ., задержка p50/p90=43.8/57.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792567866000 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.1 мс | lag loop p99/max=1.5/2.7 мс
07:31:15 [cex] Binance 134 сд. задержка p50/p90=145.3/148.5 мс | Coinbase 38 задержка p50=78.3 мс | смещение часов +20.6 мс | lag loop p99/max=2.2/6.4 мс
07:31:15 [cex] binance_futures 295 сд. p50=147.5 мс | bybit 431 сд. p50=115.1 мс | bybit_book 283 сд. p50=112.6 мс | bybit_spot 259 сд. p50=117.9 мс | bybit_spot_book 234 сд. p50=112.0 мс | okx 338 сд. p50=147.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:31:16 [pm] T-224.0s Up 0.89/0.90 Down 0.10/0.11 ptb=82905.8 | CLOB 7550 сообщ., задержка p50/p90=43.6/46.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792567876001 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=49.1 мс | lag loop p99/max=1.9/1.9 мс
```

Представлено версией кода: 96010db; python 3.12.3
