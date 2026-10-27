# Состояние сервера записи

Время (UTC): 2026-10-27 07:53:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 6 days, 29 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         700         680           1         704        1205
Swap:           2047         293        1754
```
- нагрузка CPU (1/5/15 мин): 0.81 / 0.57 / 0.46

## Данные
- файлов: 5832, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 0 |
| bn_book | 242 | 3 МБ | 0 |
| bnf_agg | 242 | 52 МБ | 0 |
| bnf_book | 46 | 408 МБ | 0 |
| bnf_depth5 | 27 | 11 МБ | 1202798 |
| bnf_liq | 216 | 144 КБ | 3059 |
| bs_trade | 27 | 420 КБ | 1202718 |
| by_book1 | 242 | 114 МБ | 0 |
| by_liq | 228 | 107 КБ | 189 |
| by_trade | 242 | 36 МБ | 0 |
| bys_book1 | 217 | 74 МБ | 0 |
| bys_trade | 217 | 30 МБ | 0 |
| cb_ticker | 242 | 33 МБ | 0 |
| clock | 242 | 189 КБ | 38 |
| clock_pm | 242 | 189 КБ | 49 |
| events | 231 | 75 КБ | 4 |
| events_pm | 241 | 85 КБ | 1237 |
| health_cex | 242 | 3 МБ | 0 |
| health_feeds | 242 | 8 МБ | 0 |
| health_pm | 242 | 3 МБ | 0 |
| kr_trade | 27 | 911 КБ | 1202718 |
| ok_trade | 241 | 45 МБ | 0 |
| pm_depth | 242 | 50 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 2 |
| pm_top | 242 | 104 МБ | 0 |
| pm_trades | 242 | 72 МБ | 0 |
| rtds | 242 | 16 МБ | 0 |
| windows | 242 | 502 КБ | 133 |

Дни с данными: 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 8, TLS 98, всего 344
- Polymarket CLOB: TCP 5, TLS 45, всего 86
- Polymarket gamma: TCP 5, TLS 44, всего 54

## Последние строки журнала записи
```
07:53:08 [pm] T-112.0s Up 0.64/0.65 Down 0.35/0.36 ptb=79731.0 | CLOB 9053 сообщ., задержка p50/p90=44.5/74.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793087588013 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.5/3.8 мс
07:53:17 [cex] Binance 334 сд. задержка p50/p90=145.4/150.9 мс | Coinbase 23 задержка p50=93.2 мс | смещение часов +22.2 мс | lag loop p99/max=2.1/7.0 мс
07:53:17 [cex] binance_futures 137 сд. p50=164.8 мс | bybit 481 сд. p50=116.8 мс | bybit_book 311 сд. p50=111.7 мс | bybit_spot 162 сд. p50=115.8 мс | bybit_spot_book 141 сд. p50=112.5 мс | okx 126 сд. p50=163.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 7564 сд. p50=146.4 мс
07:53:18 [pm] T-102.0s Up 0.79/0.80 Down 0.20/0.21 ptb=79731.0 | CLOB 8091 сообщ., задержка p50/p90=39.0/46.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793087598015 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.7/2.1 мс
07:53:27 [cex] Binance 218 сд. задержка p50/p90=145.3/161.5 мс | Coinbase 29 задержка p50=92.8 мс | смещение часов +22.2 мс | lag loop p99/max=10.0/18.8 мс
07:53:27 [cex] binance_futures 116 сд. p50=180.2 мс | bybit 488 сд. p50=125.2 мс | bybit_book 278 сд. p50=111.7 мс | bybit_spot 278 сд. p50=124.0 мс | bybit_spot_book 157 сд. p50=112.6 мс | okx 123 сд. p50=167.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 6940 сд. p50=147.3 мс
07:53:28 [pm] T- 92.0s Up 0.70/0.71 Down 0.29/0.30 ptb=79731.0 | CLOB 6948 сообщ., задержка p50/p90=38.4/40.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793087608017 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.2/5.0 мс
07:53:37 [cex] Binance 159 сд. задержка p50/p90=145.8/147.1 мс | Coinbase 32 задержка p50=93.1 мс | смещение часов +22.2 мс | lag loop p99/max=2.1/2.7 мс
07:53:37 [cex] binance_futures 124 сд. p50=152.6 мс | bybit 191 сд. p50=118.3 мс | bybit_book 160 сд. p50=111.7 мс | bybit_spot 183 сд. p50=119.5 мс | bybit_spot_book 115 сд. p50=112.6 мс | okx 143 сд. p50=163.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4217 сд. p50=149.5 мс
07:53:38 [pm] T- 82.0s Up 0.63/0.64 Down 0.36/0.37 ptb=79731.0 | CLOB 10163 сообщ., задержка p50/p90=38.2/40.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793087618018 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.8/1.9 мс
07:53:39 [cex] binance_liq: TimeoutError() (wss://fstream.binance.com/ws/btcusdt@forceOrder)
07:53:42 [cex] binance_liq подключён: wss://fstream.binance.com/market/stream?streams=btcusdt@forceOrder
07:53:48 [cex] Binance 154 сд. задержка p50/p90=145.2/156.8 мс | Coinbase 31 задержка p50=92.8 мс | смещение часов +22.2 мс | lag loop p99/max=2.3/14.7 мс
07:53:48 [cex] binance_futures 82 сд. p50=219.5 мс | bybit 97 сд. p50=124.9 мс | bybit_book 191 сд. p50=111.7 мс | bybit_spot 305 сд. p50=120.3 мс | bybit_spot_book 126 сд. p50=112.6 мс | okx 74 сд. p50=166.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3359 сд. p50=146.3 мс
07:53:48 [pm] T- 72.0s Up 0.76/0.77 Down 0.23/0.24 ptb=79731.0 | CLOB 8830 сообщ., задержка p50/p90=38.7/44.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793087628020 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=3.0/4.1 мс
```

Представлено версией кода: 0bb50e0; python 3.12.3
