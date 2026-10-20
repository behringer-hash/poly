# Состояние сервера записи

Время (UTC): 2026-10-20 04:46:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 5 days, 21 hours, 22 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         811         173           1        1104        1094
Swap:           2047         250        1797
```
- нагрузка CPU (1/5/15 мин): 0.42 / 0.31 / 0.31

## Данные
- файлов: 6907, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 281 | 37 МБ | 1 |
| bn_book | 281 | 3 МБ | 1 |
| bnf_agg | 281 | 56 МБ | 1 |
| bnf_book | 118 | 557 МБ | 586662 |
| bnf_depth5 | 118 | 41 МБ | 586738 |
| bnf_liq | 244 | 159 КБ | 1431 |
| bs_trade | 118 | 1 МБ | 586658 |
| by_book1 | 281 | 117 МБ | 1 |
| by_liq | 253 | 127 КБ | 1419 |
| by_trade | 281 | 36 МБ | 1 |
| bys_book1 | 165 | 56 МБ | 1 |
| bys_trade | 165 | 22 МБ | 1 |
| cb_ticker | 281 | 35 МБ | 1 |
| clock | 281 | 217 КБ | 26 |
| clock_pm | 281 | 218 КБ | 51 |
| events | 270 | 86 КБ | 209 |
| events_pm | 281 | 101 КБ | 344 |
| health_cex | 281 | 3 МБ | 1 |
| health_feeds | 281 | 9 МБ | 1 |
| health_pm | 281 | 3 МБ | 5 |
| kr_trade | 118 | 3 МБ | 586658 |
| ok_trade | 280 | 48 МБ | 1 |
| pm_depth | 281 | 56 МБ | 1 |
| pm_rtt | 281 | 2 МБ | 3 |
| pm_top | 281 | 115 МБ | 1 |
| pm_trades | 281 | 81 МБ | 1 |
| rtds | 281 | 18 МБ | 1 |
| windows | 281 | 581 КБ | 33 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 300
- Polymarket CLOB: TCP 4, TLS 41, всего 89
- Polymarket gamma: TCP 4, TLS 59, всего 72

## Последние строки журнала записи
```
04:45:22 [pm] T-277.7s Up 0.62/0.63 Down 0.37/0.38 ptb=81971.7 | CLOB 7506 сообщ., задержка p50/p90=38.8/55.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792471522283 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.8/1.8 мс
04:45:27 [cex] Binance 233 сд. задержка p50/p90=145.1/146.3 мс | Coinbase 31 задержка p50=80.1 мс | смещение часов +20.3 мс | lag loop p99/max=2.1/2.1 мс
04:45:27 [cex] binance_futures 143 сд. p50=145.8 мс | bybit 69 сд. p50=114.0 мс | bybit_book 163 сд. p50=111.7 мс | bybit_spot 138 сд. p50=113.6 мс | bybit_spot_book 106 сд. p50=111.1 мс | okx 160 сд. p50=155.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:45:32 [pm] T-267.7s Up 0.74/0.75 Down 0.25/0.26 ptb=81971.7 | CLOB 8088 сообщ., задержка p50/p90=38.8/42.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792471532284 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.0/2.0 мс
04:45:37 [cex] Binance 31 сд. задержка p50/p90=144.5/145.5 мс | Coinbase 39 задержка p50=78.9 мс | смещение часов +20.3 мс | lag loop p99/max=2.1/2.3 мс
04:45:37 [cex] binance_futures 22 сд. p50=294.0 мс | bybit 13 сд. p50=113.4 мс | bybit_book 112 сд. p50=111.7 мс | bybit_spot 1 сд. p50=113.4 мс | bybit_spot_book 23 сд. p50=111.1 мс | okx 36 сд. p50=154.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:45:42 [pm] T-257.7s Up 0.73/0.74 Down 0.26/0.27 ptb=81971.7 | CLOB 3942 сообщ., задержка p50/p90=38.5/40.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792471542286 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=2.4/14.9 мс
04:45:47 [cex] Binance 15 сд. задержка p50/p90=144.4/144.5 мс | Coinbase 45 задержка p50=73.9 мс | смещение часов +13.4 мс | lag loop p99/max=2.2/2.3 мс
04:45:47 [cex] binance_futures 20 сд. p50=287.2 мс | bybit 3 сд. p50=112.9 мс | bybit_book 106 сд. p50=105.2 мс | bybit_spot 1 сд. p50=106.9 мс | bybit_spot_book 24 сд. p50=111.1 мс | okx 13 сд. p50=148.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:45:52 [pm] T-247.7s Up 0.73/0.74 Down 0.26/0.27 ptb=81971.7 | CLOB 4600 сообщ., задержка p50/p90=38.7/40.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792471552287 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=3.4/4.8 мс
04:45:57 [cex] Binance 26 сд. задержка p50/p90=137.6/138.5 мс | Coinbase 41 задержка p50=72.5 мс | смещение часов +13.4 мс | lag loop p99/max=2.1/2.3 мс
04:45:57 [cex] binance_futures 20 сд. p50=287.1 мс | bybit 4 сд. p50=106.5 мс | bybit_book 80 сд. p50=104.8 мс | bybit_spot 3 сд. p50=106.7 мс | bybit_spot_book 20 сд. p50=104.1 мс | okx 15 сд. p50=147.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:46:02 [pm] T-237.7s Up 0.75/0.76 Down 0.24/0.25 ptb=81971.7 | CLOB 4756 сообщ., задержка p50/p90=38.9/44.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792471562289 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.0/4.6 мс
04:46:07 [cex] Binance 126 сд. задержка p50/p90=138.2/142.0 мс | Coinbase 48 задержка p50=73.2 мс | смещение часов +13.4 мс | lag loop p99/max=2.2/2.2 мс
04:46:07 [cex] binance_futures 78 сд. p50=142.5 мс | bybit 78 сд. p50=109.7 мс | bybit_book 95 сд. p50=104.8 мс | bybit_spot 77 сд. p50=111.8 мс | bybit_spot_book 51 сд. p50=104.5 мс | okx 68 сд. p50=148.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
