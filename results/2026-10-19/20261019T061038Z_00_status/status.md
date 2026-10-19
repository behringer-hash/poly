# Состояние сервера записи

Время (UTC): 2026-10-19 06:10:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 22 hours, 46 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         545         815           1         717        1360
Swap:           2047         253        1794
```
- нагрузка CPU (1/5/15 мин): 0.17 / 0.18 / 0.18

## Данные
- файлов: 6381, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 259 | 33 МБ | 1 |
| bn_book | 259 | 3 МБ | 11 |
| bnf_agg | 259 | 50 МБ | 1 |
| bnf_book | 118 | 557 МБ | 505332 |
| bnf_depth5 | 118 | 41 МБ | 505409 |
| bnf_liq | 225 | 147 КБ | 125 |
| bs_trade | 118 | 1 МБ | 505328 |
| by_book1 | 259 | 105 МБ | 1 |
| by_liq | 231 | 119 КБ | 904 |
| by_trade | 259 | 33 МБ | 1 |
| bys_book1 | 143 | 47 МБ | 1 |
| bys_trade | 143 | 19 МБ | 1 |
| cb_ticker | 259 | 31 МБ | 1 |
| clock | 259 | 199 КБ | 56 |
| clock_pm | 259 | 199 КБ | 12 |
| events | 247 | 79 КБ | 1814 |
| events_pm | 259 | 93 КБ | 361 |
| health_cex | 259 | 3 МБ | 1 |
| health_feeds | 259 | 9 МБ | 1 |
| health_pm | 259 | 3 МБ | 8 |
| kr_trade | 118 | 3 МБ | 505328 |
| ok_trade | 258 | 44 МБ | 1 |
| pm_depth | 259 | 51 МБ | 0 |
| pm_rtt | 259 | 2 МБ | 0 |
| pm_top | 259 | 104 МБ | 0 |
| pm_trades | 259 | 74 МБ | 0 |
| rtds | 259 | 16 МБ | 0 |
| windows | 259 | 532 КБ | 95 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 10, TLS 52, всего 301
- Polymarket CLOB: TCP 6, TLS 47, всего 93
- Polymarket gamma: TCP 5, TLS 46, всего 58

## Последние строки журнала записи
```
06:09:49 [pm] T- 10.0s Up 0.99/n/a Down n/a/0.01 ptb=82685.5 | CLOB 2045 сообщ., задержка p50/p90=44.2/58.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792390189973 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.2/28.1 мс
06:09:57 [cex] Binance 76 сд. задержка p50/p90=140.6/141.5 мс | Coinbase 54 задержка p50=78.1 мс | смещение часов +16.8 мс | lag loop p99/max=2.2/2.2 мс
06:09:57 [cex] binance_futures 240 сд. p50=142.4 мс | bybit 582 сд. p50=116.3 мс | bybit_book 310 сд. p50=108.8 мс | bybit_spot 288 сд. p50=111.0 мс | bybit_spot_book 125 сд. p50=108.2 мс | okx 173 сд. p50=155.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:09:59 [pm] T-  0.0s Up 0.99/n/a Down n/a/0.01 ptb=82685.5 | CLOB 3768 сообщ., задержка p50/p90=44.3/46.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792390199975 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=2.1/2.2 мс
06:10:07 [cex] Binance 133 сд. задержка p50/p90=140.9/142.2 мс | Coinbase 47 задержка p50=75.3 мс | смещение часов +16.8 мс | lag loop p99/max=2.3/2.9 мс
06:10:07 [cex] binance_futures 209 сд. p50=142.2 мс | bybit 574 сд. p50=113.7 мс | bybit_book 209 сд. p50=108.8 мс | bybit_spot 244 сд. p50=111.0 мс | bybit_spot_book 179 сд. p50=108.2 мс | okx 177 сд. p50=155.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:10:09 [pm] T-290.0s Up 0.29/0.30 Down 0.70/0.71 ptb=82695.6 | CLOB 10575 сообщ., задержка p50/p90=44.6/56.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792390209976 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.0 мс | lag loop p99/max=18.6/19.7 мс
06:10:17 [cex] Binance 112 сд. задержка p50/p90=141.0/142.4 мс | Coinbase 40 задержка p50=74.1 мс | смещение часов +16.8 мс | lag loop p99/max=2.2/2.2 мс
06:10:17 [cex] binance_futures 179 сд. p50=142.0 мс | bybit 424 сд. p50=113.0 мс | bybit_book 186 сд. p50=108.8 мс | bybit_spot 283 сд. p50=110.9 мс | bybit_spot_book 155 сд. p50=108.2 мс | okx 136 сд. p50=155.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:10:19 [pm] T-280.0s Up 0.30/0.31 Down 0.69/0.70 ptb=82695.6 | CLOB 9603 сообщ., задержка p50/p90=44.1/45.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792390219978 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=4.6/6.2 мс
06:10:27 [cex] Binance 127 сд. задержка p50/p90=140.9/141.4 мс | Coinbase 37 задержка p50=75.3 мс | смещение часов +16.8 мс | lag loop p99/max=1.9/2.2 мс
06:10:27 [cex] binance_futures 128 сд. p50=142.3 мс | bybit 265 сд. p50=111.4 мс | bybit_book 190 сд. p50=108.8 мс | bybit_spot 128 сд. p50=110.9 мс | bybit_spot_book 145 сд. p50=108.2 мс | okx 129 сд. p50=155.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:10:29 [pm] T-270.0s Up 0.23/0.24 Down 0.76/0.77 ptb=82695.6 | CLOB 8777 сообщ., задержка p50/p90=43.7/46.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792390229979 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=2.1/2.4 мс
06:10:37 [cex] Binance 22 сд. задержка p50/p90=140.5/140.7 мс | Coinbase 36 задержка p50=73.8 мс | смещение часов +16.8 мс | lag loop p99/max=2.1/2.1 мс
06:10:37 [cex] binance_futures 58 сд. p50=210.2 мс | bybit 66 сд. p50=110.6 мс | bybit_book 110 сд. p50=108.8 мс | bybit_spot 101 сд. p50=110.6 мс | bybit_spot_book 80 сд. p50=108.2 мс | okx 26 сд. p50=155.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 88f2465; python 3.12.3
