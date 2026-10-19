# Состояние сервера записи

Время (UTC): 2026-10-19 15:24:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 5 days, 8 hours, 1 minute
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         765         360           1         960        1140
Swap:           2047         251        1796
```
- нагрузка CPU (1/5/15 мин): 0.29 / 0.29 / 0.38

## Данные
- файлов: 6598, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 268 | 35 МБ | 0 |
| bn_book | 268 | 3 МБ | 4 |
| bnf_agg | 268 | 54 МБ | 0 |
| bnf_book | 118 | 557 МБ | 538592 |
| bnf_depth5 | 118 | 41 МБ | 538669 |
| bnf_liq | 233 | 159 КБ | 2092 |
| bs_trade | 118 | 1 МБ | 538588 |
| by_book1 | 268 | 111 МБ | 0 |
| by_liq | 241 | 124 КБ | 158 |
| by_trade | 268 | 35 МБ | 0 |
| bys_book1 | 152 | 52 МБ | 0 |
| bys_trade | 152 | 21 МБ | 0 |
| cb_ticker | 268 | 33 МБ | 0 |
| clock | 268 | 207 КБ | 49 |
| clock_pm | 268 | 207 КБ | 6 |
| events | 257 | 82 КБ | 255 |
| events_pm | 268 | 96 КБ | 722 |
| health_cex | 268 | 3 МБ | 6 |
| health_feeds | 268 | 9 МБ | 6 |
| health_pm | 268 | 3 МБ | 2 |
| kr_trade | 118 | 3 МБ | 538588 |
| ok_trade | 267 | 47 МБ | 0 |
| pm_depth | 268 | 53 МБ | 2 |
| pm_rtt | 268 | 2 МБ | 2 |
| pm_top | 268 | 109 МБ | 2 |
| pm_trades | 268 | 77 МБ | 2 |
| rtds | 268 | 17 МБ | 2 |
| windows | 268 | 552 КБ | 293 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 38, всего 288
- Polymarket CLOB: TCP 5, TLS 45, всего 88
- Polymarket gamma: TCP 5, TLS 47, всего 60

## Последние строки журнала записи
```
15:24:11 [cex] binance_futures 253 сд. p50=145.2 мс | bybit 165 сд. p50=112.1 мс | bybit_book 290 сд. p50=111.8 мс | bybit_spot 175 сд. p50=114.4 мс | bybit_spot_book 163 сд. p50=111.1 мс | okx 369 сд. p50=158.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:24:15 [pm] T- 45.0s Up 1.00/n/a Down n/a/0.00 ptb=82192.9 | CLOB 525 сообщ., задержка p50/p90=62.3/76.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792423455014 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.1 мс | lag loop p99/max=2.1/2.1 мс
15:24:21 [cex] Binance 97 сд. задержка p50/p90=144.1/148.9 мс | Coinbase 56 задержка p50=77.6 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.1 мс
15:24:21 [cex] binance_futures 133 сд. p50=199.1 мс | bybit 58 сд. p50=112.1 мс | bybit_book 194 сд. p50=112.0 мс | bybit_spot 57 сд. p50=117.5 мс | bybit_spot_book 52 сд. p50=111.3 мс | okx 40 сд. p50=157.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:24:25 [pm] T- 35.0s Up 1.00/n/a Down n/a/0.00 ptb=82192.9 | CLOB 365 сообщ., задержка p50/p90=62.0/65.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792423465015 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.1 мс | lag loop p99/max=2.1/2.5 мс
15:24:31 [cex] Binance 189 сд. задержка p50/p90=144.2/145.8 мс | Coinbase 51 задержка p50=78.5 мс | смещение часов +19.5 мс | lag loop p99/max=2.2/2.2 мс
15:24:31 [cex] binance_futures 242 сд. p50=145.5 мс | bybit 124 сд. p50=112.2 мс | bybit_book 225 сд. p50=111.9 мс | bybit_spot 122 сд. p50=114.3 мс | bybit_spot_book 154 сд. p50=111.3 мс | okx 289 сд. p50=158.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:24:35 [pm] T- 25.0s Up 1.00/n/a Down n/a/0.00 ptb=82192.9 | CLOB 439 сообщ., задержка p50/p90=62.3/66.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792423475017 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.9 мс | lag loop p99/max=2.1/2.1 мс
15:24:41 [cex] Binance 237 сд. задержка p50/p90=144.5/149.8 мс | Coinbase 90 задержка p50=81.0 мс | смещение часов +19.5 мс | lag loop p99/max=2.2/2.3 мс
15:24:41 [cex] binance_futures 325 сд. p50=149.0 мс | bybit 290 сд. p50=112.7 мс | bybit_book 262 сд. p50=111.9 мс | bybit_spot 283 сд. p50=114.4 мс | bybit_spot_book 152 сд. p50=111.4 мс | okx 354 сд. p50=159.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:24:45 [pm] T- 15.0s Up 1.00/n/a Down n/a/0.00 ptb=82192.9 | CLOB 374 сообщ., задержка p50/p90=62.0/66.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792423485018 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.9 мс | lag loop p99/max=2.0/2.1 мс
15:24:45 [pm] окно btc-updown-5m-1792423500 (2026-10-19 15:25:00 UTC): Bitcoin Up or Down - October 19, 11:25AM-11:30AM ET
15:24:51 [cex] Binance 81 сд. задержка p50/p90=151.3/152.8 мс | Coinbase 66 задержка p50=78.4 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.2 мс
15:24:51 [cex] binance_futures 243 сд. p50=152.7 мс | bybit 98 сд. p50=112.1 мс | bybit_book 223 сд. p50=112.0 мс | bybit_spot 97 сд. p50=115.6 мс | bybit_spot_book 101 сд. p50=111.3 мс | okx 172 сд. p50=158.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
15:24:55 [pm] T-  5.0s Up 1.00/n/a Down n/a/0.00 ptb=82192.9 | CLOB 2337 сообщ., задержка p50/p90=39.6/61.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792423495019 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.9 мс | lag loop p99/max=1.9/2.1 мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
