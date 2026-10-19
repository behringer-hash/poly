# Состояние сервера записи

Время (UTC): 2026-10-19 13:21:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 5 days, 5 hours, 58 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         700         534           1         850        1205
Swap:           2047         251        1796
```
- нагрузка CPU (1/5/15 мин): 0.19 / 0.27 / 0.31

## Данные
- файлов: 6550, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 266 | 34 МБ | 1 |
| bn_book | 266 | 3 МБ | 13 |
| bnf_agg | 266 | 52 МБ | 1 |
| bnf_book | 118 | 557 МБ | 531212 |
| bnf_depth5 | 118 | 41 МБ | 531289 |
| bnf_liq | 231 | 152 КБ | 2737 |
| bs_trade | 118 | 1 МБ | 531208 |
| by_book1 | 266 | 109 МБ | 1 |
| by_liq | 239 | 122 КБ | 1038 |
| by_trade | 266 | 34 МБ | 1 |
| bys_book1 | 150 | 50 МБ | 1 |
| bys_trade | 150 | 20 МБ | 1 |
| cb_ticker | 266 | 32 МБ | 1 |
| clock | 266 | 205 КБ | 48 |
| clock_pm | 266 | 205 КБ | 6 |
| events | 255 | 81 КБ | 289 |
| events_pm | 266 | 96 КБ | 172 |
| health_cex | 266 | 3 МБ | 7 |
| health_feeds | 266 | 9 МБ | 7 |
| health_pm | 266 | 3 МБ | 4 |
| kr_trade | 118 | 3 МБ | 531208 |
| ok_trade | 265 | 45 МБ | 1 |
| pm_depth | 266 | 53 МБ | 0 |
| pm_rtt | 266 | 2 МБ | 4 |
| pm_top | 266 | 107 МБ | 0 |
| pm_trades | 266 | 77 МБ | 0 |
| rtds | 266 | 17 МБ | 0 |
| windows | 266 | 548 КБ | 23 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 6, TLS 53, всего 303
- Polymarket CLOB: TCP 7, TLS 57, всего 98
- Polymarket gamma: TCP 5, TLS 61, всего 74

## Последние строки журнала записи
```
13:21:10 [cex] Binance 136 сд. задержка p50/p90=152.1/152.7 мс | Coinbase 35 задержка p50=87.2 мс | смещение часов +18.3 мс | lag loop p99/max=2.0/2.0 мс
13:21:10 [cex] binance_futures 196 сд. p50=152.5 мс | bybit 100 сд. p50=119.8 мс | bybit_book 104 сд. p50=118.1 мс | bybit_spot 125 сд. p50=120.5 мс | bybit_spot_book 77 сд. p50=117.6 мс | okx 132 сд. p50=165.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:21:13 [pm] T-226.1s Up 0.36/0.37 Down 0.63/0.64 ptb=82499.9 | CLOB 9628 сообщ., задержка p50/p90=42.4/63.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792416073945 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.2/3.2 мс
13:21:20 [cex] Binance 68 сд. задержка p50/p90=143.3/143.8 мс | Coinbase 21 задержка p50=76.2 мс | смещение часов +18.3 мс | lag loop p99/max=2.2/2.2 мс
13:21:20 [cex] binance_futures 45 сд. p50=274.8 мс | bybit 100 сд. p50=111.7 мс | bybit_book 138 сд. p50=110.6 мс | bybit_spot 8 сд. p50=112.1 мс | bybit_spot_book 49 сд. p50=110.4 мс | okx 55 сд. p50=156.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:21:23 [pm] T-216.1s Up 0.42/0.43 Down 0.57/0.58 ptb=82499.9 | CLOB 9332 сообщ., задержка p50/p90=82.0/116.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792416083946 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.2/1.6 мс
13:21:30 [cex] Binance 79 сд. задержка p50/p90=143.1/143.8 мс | Coinbase 51 задержка p50=77.0 мс | смещение часов +18.3 мс | lag loop p99/max=2.3/2.6 мс
13:21:30 [cex] binance_futures 84 сд. p50=143.8 мс | bybit 70 сд. p50=111.2 мс | bybit_book 154 сд. p50=110.6 мс | bybit_spot 153 сд. p50=112.7 мс | bybit_spot_book 89 сд. p50=110.4 мс | okx 75 сд. p50=157.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:21:33 [pm] T-206.1s Up 0.41/0.42 Down 0.58/0.59 ptb=82499.9 | CLOB 8470 сообщ., задержка p50/p90=42.4/84.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792416093947 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.7/3.1 мс
13:21:40 [cex] Binance 16 сд. задержка p50/p90=142.7/143.8 мс | Coinbase 74 задержка p50=77.8 мс | смещение часов +18.3 мс | lag loop p99/max=2.0/2.1 мс
13:21:40 [cex] binance_futures 19 сд. p50=291.9 мс | bybit 17 сд. p50=110.9 мс | bybit_book 89 сд. p50=110.5 мс | bybit_spot 2 сд. p50=112.5 мс | bybit_spot_book 42 сд. p50=110.4 мс | okx 19 сд. p50=156.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:21:43 [pm] T-196.1s Up 0.40/0.41 Down 0.59/0.60 ptb=82499.9 | CLOB 8575 сообщ., задержка p50/p90=40.4/42.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792416103948 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.1/2.3 мс
13:21:50 [cex] Binance 39 сд. задержка p50/p90=142.9/144.4 мс | Coinbase 44 задержка p50=78.8 мс | смещение часов +18.3 мс | lag loop p99/max=2.0/2.2 мс
13:21:50 [cex] binance_futures 33 сд. p50=291.8 мс | bybit 82 сд. p50=111.0 мс | bybit_book 156 сд. p50=110.5 мс | bybit_spot 57 сд. p50=113.6 мс | bybit_spot_book 69 сд. p50=110.2 мс | okx 27 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:21:53 [pm] T-186.1s Up 0.42/0.43 Down 0.57/0.58 ptb=82499.9 | CLOB 8195 сообщ., задержка p50/p90=38.6/44.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792416113949 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.1/2.1 мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
