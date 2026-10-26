# Состояние сервера записи

Время (UTC): 2026-10-26 14:50:49

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 5 days, 7 hours, 26 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         525        1125           1         426        1380
Swap:           2047         289        1758
```
- нагрузка CPU (1/5/15 мин): 1.91 / 1.83 / 1.93

## Данные
- файлов: 5876, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 243 | 37 МБ | 1 |
| bn_book | 243 | 3 МБ | 3 |
| bnf_agg | 243 | 55 МБ | 1 |
| bnf_book | 47 | 523 МБ | 0 |
| bnf_depth5 | 45 | 17 МБ | 1141419 |
| bnf_liq | 218 | 148 КБ | 51 |
| bs_trade | 45 | 613 КБ | 1141339 |
| by_book1 | 243 | 114 МБ | 1 |
| by_liq | 228 | 110 КБ | 51 |
| by_trade | 243 | 38 МБ | 1 |
| bys_book1 | 200 | 72 МБ | 1 |
| bys_trade | 200 | 30 МБ | 1 |
| cb_ticker | 243 | 33 МБ | 1 |
| clock | 243 | 189 КБ | 15 |
| clock_pm | 243 | 190 КБ | 27 |
| events | 233 | 73 КБ | 5250 |
| events_pm | 242 | 85 КБ | 1037 |
| health_cex | 243 | 3 МБ | 1 |
| health_feeds | 243 | 8 МБ | 1 |
| health_pm | 243 | 3 МБ | 1 |
| kr_trade | 45 | 1 МБ | 1141339 |
| ok_trade | 242 | 48 МБ | 1 |
| pm_depth | 243 | 50 МБ | 1 |
| pm_rtt | 243 | 2 МБ | 3 |
| pm_top | 243 | 104 МБ | 1 |
| pm_trades | 243 | 72 МБ | 1 |
| rtds | 243 | 16 МБ | 1 |
| windows | 243 | 503 КБ | 45 |

Дни с данными: 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 52, всего 299
- Polymarket CLOB: TCP 5, TLS 47, всего 157
- Polymarket gamma: TCP 7, TLS 49, всего 56

## Последние строки журнала записи
```
14:50:07 [cex] Binance 151 сд. задержка p50/p90=156.8/166.0 мс | Coinbase 59 задержка p50=96.1 мс | смещение часов +33.4 мс | lag loop p99/max=11.8/12.7 мс
14:50:07 [cex] binance_futures 214 сд. p50=178.7 мс | bybit 246 сд. p50=127.6 мс | bybit_book 329 сд. p50=123.3 мс | bybit_spot 171 сд. p50=128.1 мс | bybit_spot_book 179 сд. p50=124.0 мс | okx 225 сд. p50=169.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4639 сд. p50=157.5 мс
14:50:08 [pm] T-291.6s Up 0.59/0.60 Down 0.40/0.41 ptb=80113.8 | CLOB 7728 сообщ., задержка p50/p90=55.3/59.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793026208370 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=5.8/20.5 мс
14:50:17 [cex] Binance 226 сд. задержка p50/p90=156.8/159.2 мс | Coinbase 76 задержка p50=95.8 мс | смещение часов +33.4 мс | lag loop p99/max=7.4/18.8 мс
14:50:17 [cex] binance_futures 273 сд. p50=168.5 мс | bybit 404 сд. p50=137.0 мс | bybit_book 290 сд. p50=123.2 мс | bybit_spot 149 сд. p50=128.5 мс | bybit_spot_book 133 сд. p50=124.0 мс | okx 164 сд. p50=170.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3905 сд. p50=157.7 мс
14:50:18 [pm] T-281.6s Up 0.56/0.57 Down 0.43/0.44 ptb=80113.8 | CLOB 8631 сообщ., задержка p50/p90=55.2/57.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793026218371 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=4.4/4.5 мс
14:50:27 [cex] Binance 291 сд. задержка p50/p90=157.4/186.5 мс | Coinbase 191 задержка p50=102.6 мс | смещение часов +33.4 мс | lag loop p99/max=32.3/52.7 мс
14:50:27 [cex] binance_futures 229 сд. p50=174.7 мс | bybit 244 сд. p50=126.6 мс | bybit_book 330 сд. p50=123.4 мс | bybit_spot 144 сд. p50=137.3 мс | bybit_spot_book 138 сд. p50=124.2 мс | okx 206 сд. p50=172.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 6614 сд. p50=157.5 мс
14:50:28 [pm] T-271.6s Up 0.62/0.63 Down 0.37/0.38 ptb=80113.8 | CLOB 8817 сообщ., задержка p50/p90=77.7/80.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793026228374 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=3.6/4.9 мс
14:50:37 [cex] Binance 234 сд. задержка p50/p90=158.1/178.7 мс | Coinbase 82 задержка p50=100.9 мс | смещение часов +55.7 мс | lag loop p99/max=26.1/40.7 мс
14:50:37 [cex] binance_futures 412 сд. p50=169.5 мс | bybit 375 сд. p50=127.6 мс | bybit_book 330 сд. p50=124.4 мс | bybit_spot 328 сд. p50=133.2 мс | bybit_spot_book 168 сд. p50=124.9 мс | okx 295 сд. p50=173.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 9381 сд. p50=174.6 мс
14:50:38 [pm] T-261.6s Up 0.48/0.49 Down 0.51/0.52 ptb=80113.8 | CLOB 9171 сообщ., задержка p50/p90=77.2/78.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793026238376 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=8.0/14.7 мс
14:50:47 [cex] Binance 226 сд. задержка p50/p90=179.2/187.0 мс | Coinbase 53 задержка p50=118.3 мс | смещение часов +55.7 мс | lag loop p99/max=40.6/44.6 мс
14:50:47 [cex] binance_futures 275 сд. p50=196.0 мс | bybit 402 сд. p50=151.0 мс | bybit_book 344 сд. p50=145.7 мс | bybit_spot 294 сд. p50=150.2 мс | bybit_spot_book 226 сд. p50=146.3 мс | okx 416 сд. p50=193.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 7201 сд. p50=180.2 мс
14:50:48 [pm] T-251.6s Up 0.41/0.42 Down 0.58/0.59 ptb=80113.8 | CLOB 9933 сообщ., задержка p50/p90=77.8/83.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793026248377 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=3.9/6.2 мс
```

Представлено версией кода: a091a18; python 3.12.3
