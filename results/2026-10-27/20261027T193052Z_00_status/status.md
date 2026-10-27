# Состояние сервера записи

Время (UTC): 2026-10-27 19:30:52

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 6 days, 12 hours, 6 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         628         811           2         641        1277
Swap:           2047         282        1765
```
- нагрузка CPU (1/5/15 мин): 1.11 / 0.72 / 0.71

## Данные
- файлов: 5820, всего 1022 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 2 |
| bn_book | 242 | 3 МБ | 22 |
| bnf_agg | 242 | 51 МБ | 2 |
| bnf_book | 46 | 344 МБ | 0 |
| bnf_depth5 | 15 | 6 МБ | 1244622 |
| bnf_liq | 216 | 143 КБ | 3451 |
| bs_trade | 15 | 269 КБ | 1244542 |
| by_book1 | 242 | 110 МБ | 2 |
| by_liq | 226 | 104 КБ | 5384 |
| by_trade | 242 | 34 МБ | 2 |
| bys_book1 | 229 | 77 МБ | 2 |
| bys_trade | 229 | 31 МБ | 2 |
| cb_ticker | 242 | 32 МБ | 2 |
| clock | 242 | 188 КБ | 10 |
| clock_pm | 242 | 188 КБ | 27 |
| events | 233 | 74 КБ | 394 |
| events_pm | 241 | 83 КБ | 294 |
| health_cex | 242 | 2 МБ | 6 |
| health_feeds | 242 | 7 МБ | 6 |
| health_pm | 242 | 3 МБ | 7 |
| kr_trade | 15 | 503 КБ | 1244542 |
| ok_trade | 241 | 44 МБ | 2 |
| pm_depth | 242 | 49 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 1 |
| pm_top | 242 | 102 МБ | 1 |
| pm_trades | 242 | 71 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 500 КБ | 228 |

Дни с данными: 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 37, всего 285
- Polymarket CLOB: TCP 8, TLS 43, всего 90
- Polymarket gamma: TCP 4, TLS 36, всего 42

## Последние строки журнала записи
```
19:30:04 [pm] T-295.4s Up 0.39/0.40 Down 0.60/0.61 ptb=80558.9 | CLOB 4442 сообщ., задержка p50/p90=57.4/72.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793129404602 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.1/2.2 мс
19:30:05 [cex] Binance 74 сд. задержка p50/p90=155.7/159.4 мс | Coinbase 28 задержка p50=104.5 мс | смещение часов +32.6 мс | lag loop p99/max=3.2/12.0 мс
19:30:05 [cex] binance_futures 60 сд. p50=159.8 мс | bybit 44 сд. p50=126.0 мс | bybit_book 164 сд. p50=122.5 мс | bybit_spot 110 сд. p50=126.2 мс | bybit_spot_book 86 сд. p50=122.8 мс | okx 27 сд. p50=168.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3773 сд. p50=156.5 мс
19:30:14 [pm] T-285.4s Up 0.37/0.38 Down 0.62/0.63 ptb=80558.9 | CLOB 3575 сообщ., задержка p50/p90=57.3/72.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793129414603 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.5/2.5 мс
19:30:15 [cex] Binance 39 сд. задержка p50/p90=155.5/156.4 мс | Coinbase 15 задержка p50=103.3 мс | смещение часов +32.6 мс | lag loop p99/max=2.4/2.5 мс
19:30:15 [cex] binance_futures 32 сд. p50=186.9 мс | bybit 33 сд. p50=125.3 мс | bybit_book 181 сд. p50=122.5 мс | bybit_spot 6 сд. p50=124.7 мс | bybit_spot_book 57 сд. p50=122.7 мс | okx 16 сд. p50=166.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1436 сд. p50=156.7 мс
19:30:24 [pm] T-275.4s Up 0.41/0.42 Down 0.58/0.59 ptb=80558.9 | CLOB 4032 сообщ., задержка p50/p90=56.4/70.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793129424605 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.8/2.1 мс
19:30:25 [cex] Binance 33 сд. задержка p50/p90=155.5/156.4 мс | Coinbase 23 задержка p50=320.4 мс | смещение часов +32.6 мс | lag loop p99/max=2.2/2.2 мс
19:30:25 [cex] binance_futures 15 сд. p50=305.1 мс | bybit 59 сд. p50=125.9 мс | bybit_book 126 сд. p50=122.4 мс | bybit_spot 72 сд. p50=129.5 мс | bybit_spot_book 62 сд. p50=122.8 мс | okx 9 сд. p50=165.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 905 сд. p50=156.6 мс
19:30:34 [pm] T-265.4s Up 0.31/0.32 Down 0.68/0.69 ptb=80558.9 | CLOB 7695 сообщ., задержка p50/p90=57.5/73.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793129434608 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=8.3/9.1 мс
19:30:35 [cex] Binance 63 сд. задержка p50/p90=156.7/165.4 мс | Coinbase 24 задержка p50=115.4 мс | смещение часов +32.6 мс | lag loop p99/max=3.9/19.7 мс
19:30:35 [cex] binance_futures 66 сд. p50=167.5 мс | bybit 75 сд. p50=125.9 мс | bybit_book 149 сд. p50=122.5 мс | bybit_spot 73 сд. p50=133.1 мс | bybit_spot_book 70 сд. p50=122.8 мс | okx 66 сд. p50=172.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3062 сд. p50=158.5 мс
19:30:44 [pm] T-255.4s Up 0.28/0.29 Down 0.71/0.72 ptb=80558.9 | CLOB 4177 сообщ., задержка p50/p90=62.6/79.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793129444610 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.9/2.4 мс
19:30:45 [cex] Binance 24 сд. задержка p50/p90=157.6/157.7 мс | Coinbase 27 задержка p50=104.7 мс | смещение часов +34.9 мс | lag loop p99/max=2.5/2.6 мс
19:30:45 [cex] binance_futures 25 сд. p50=305.2 мс | bybit 19 сд. p50=124.7 мс | bybit_book 119 сд. p50=122.8 мс | bybit_spot 3 сд. p50=126.8 мс | bybit_spot_book 57 сд. p50=124.6 мс | okx 31 сд. p50=168.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 979 сд. p50=158.7 мс
```

Представлено версией кода: a37c7f3; python 3.12.3
