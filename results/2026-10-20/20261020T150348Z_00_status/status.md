# Состояние сервера записи

Время (UTC): 2026-10-20 15:03:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 7 hours, 39 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         838         225           1        1027        1067
Swap:           2047         250        1797
```
- нагрузка CPU (1/5/15 мин): 0.16 / 0.49 / 0.49

## Данные
- файлов: 7170, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 292 | 38 МБ | 1 |
| bn_book | 292 | 4 МБ | 1 |
| bnf_agg | 292 | 58 МБ | 1 |
| bnf_book | 118 | 557 МБ | 623722 |
| bnf_depth5 | 118 | 41 МБ | 623798 |
| bnf_liq | 255 | 166 КБ | 79 |
| bs_trade | 118 | 1 МБ | 623718 |
| by_book1 | 292 | 120 МБ | 1 |
| by_liq | 264 | 132 КБ | 37 |
| by_trade | 292 | 38 МБ | 1 |
| bys_book1 | 176 | 59 МБ | 1 |
| bys_trade | 176 | 23 МБ | 1 |
| cb_ticker | 292 | 35 МБ | 1 |
| clock | 292 | 225 КБ | 47 |
| clock_pm | 292 | 225 КБ | 17 |
| events | 280 | 89 КБ | 1213 |
| events_pm | 292 | 104 КБ | 55 |
| health_cex | 292 | 3 МБ | 5 |
| health_feeds | 292 | 9 МБ | 5 |
| health_pm | 292 | 3 МБ | 9 |
| kr_trade | 118 | 3 МБ | 623718 |
| ok_trade | 291 | 50 МБ | 1 |
| pm_depth | 292 | 57 МБ | 2 |
| pm_rtt | 292 | 2 МБ | 2 |
| pm_top | 292 | 118 МБ | 2 |
| pm_trades | 292 | 84 МБ | 13 |
| rtds | 292 | 18 МБ | 2 |
| windows | 292 | 600 КБ | 132 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 35, всего 288
- Polymarket CLOB: TCP 4, TLS 40, всего 82
- Polymarket gamma: TCP 4, TLS 38, всего 54

## Последние строки журнала записи
```
15:03:01 [cex] Binance 60 сд. задержка p50/p90=146.5/147.0 мс | Coinbase 68 задержка p50=81.5 мс | смещение часов +20.3 мс | lag loop p99/max=2.1/2.1 мс
15:03:01 [cex] binance_futures 155 сд. p50=189.0 мс | bybit 187 сд. p50=116.4 мс | bybit_book 282 сд. p50=114.3 мс | bybit_spot 47 сд. p50=115.9 мс | bybit_spot_book 104 сд. p50=114.2 мс | okx 91 сд. p50=150.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:03:08 [pm] T-112.0s Up n/a/0.01 Down 0.99/n/a ptb=83226.2 | CLOB 822 сообщ., задержка p50/p90=40.9/43.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792508588043 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.4 мс | lag loop p99/max=2.1/2.2 мс
15:03:11 [cex] Binance 310 сд. задержка p50/p90=144.5/147.9 мс | Coinbase 85 задержка p50=81.1 мс | смещение часов +20.3 мс | lag loop p99/max=2.1/2.1 мс
15:03:11 [cex] binance_futures 393 сд. p50=146.6 мс | bybit 948 сд. p50=114.7 мс | bybit_book 401 сд. p50=112.0 мс | bybit_spot 267 сд. p50=114.0 мс | bybit_spot_book 254 сд. p50=111.9 мс | okx 454 сд. p50=148.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 1 сд. p50=448.7 мс
15:03:18 [pm] T-102.0s Up n/a/0.01 Down 0.99/n/a ptb=83226.2 | CLOB 1056 сообщ., задержка p50/p90=40.7/42.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792508598044 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.4 мс | lag loop p99/max=2.1/2.1 мс
15:03:21 [cex] Binance 425 сд. задержка p50/p90=144.4/145.3 мс | Coinbase 99 задержка p50=84.8 мс | смещение часов +20.3 мс | lag loop p99/max=2.2/2.3 мс
15:03:21 [cex] binance_futures 499 сд. p50=146.2 мс | bybit 697 сд. p50=114.3 мс | bybit_book 481 сд. p50=111.9 мс | bybit_spot 325 сд. p50=113.7 мс | bybit_spot_book 397 сд. p50=111.9 мс | okx 542 сд. p50=148.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:03:28 [pm] T- 92.0s Up n/a/0.00 Down 1.00/n/a ptb=83226.2 | CLOB 1417 сообщ., задержка p50/p90=41.0/43.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792508608045 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.4 мс | lag loop p99/max=2.0/2.1 мс
15:03:31 [cex] Binance 184 сд. задержка p50/p90=144.4/145.7 мс | Coinbase 76 задержка p50=79.9 мс | смещение часов +20.3 мс | lag loop p99/max=3.0/4.3 мс
15:03:31 [cex] binance_futures 380 сд. p50=146.6 мс | bybit 352 сд. p50=114.0 мс | bybit_book 420 сд. p50=111.9 мс | bybit_spot 230 сд. p50=113.9 мс | bybit_spot_book 305 сд. p50=112.0 мс | okx 395 сд. p50=148.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:03:38 [pm] T- 82.0s Up n/a/0.00 Down 1.00/n/a ptb=83226.2 | CLOB 1356 сообщ., задержка p50/p90=40.5/42.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792508618047 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=2.0/2.1 мс
15:03:41 [cex] Binance 103 сд. задержка p50/p90=144.3/145.2 мс | Coinbase 77 задержка p50=79.9 мс | смещение часов +20.3 мс | lag loop p99/max=2.2/2.3 мс
15:03:41 [cex] binance_futures 224 сд. p50=147.4 мс | bybit 271 сд. p50=113.8 мс | bybit_book 299 сд. p50=112.0 мс | bybit_spot 197 сд. p50=113.5 мс | bybit_spot_book 213 сд. p50=111.9 мс | okx 171 сд. p50=147.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:03:48 [pm] T- 72.0s Up n/a/0.00 Down 1.00/n/a ptb=83226.2 | CLOB 785 сообщ., задержка p50/p90=40.4/43.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792508628048 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=2.2/2.2 мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
