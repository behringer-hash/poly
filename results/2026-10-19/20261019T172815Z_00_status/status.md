# Состояние сервера записи

Время (UTC): 2026-10-19 17:28:15

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 5 days, 10 hours, 4 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         701         399           1         986        1204
Swap:           2047         250        1797
```
- нагрузка CPU (1/5/15 мин): 0.25 / 0.32 / 0.28

## Данные
- файлов: 6646, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 270 | 35 МБ | 0 |
| bn_book | 270 | 3 МБ | 0 |
| bnf_agg | 270 | 54 МБ | 0 |
| bnf_book | 118 | 557 МБ | 545989 |
| bnf_depth5 | 118 | 41 МБ | 546066 |
| bnf_liq | 236 | 155 КБ | 171 |
| bs_trade | 118 | 1 МБ | 545985 |
| by_book1 | 270 | 112 МБ | 0 |
| by_liq | 242 | 124 КБ | 4048 |
| by_trade | 270 | 35 МБ | 0 |
| bys_book1 | 154 | 53 МБ | 0 |
| bys_trade | 154 | 21 МБ | 0 |
| cb_ticker | 270 | 33 МБ | 0 |
| clock | 270 | 208 КБ | 0 |
| clock_pm | 270 | 209 КБ | 26 |
| events | 259 | 82 КБ | 999 |
| events_pm | 270 | 97 КБ | 753 |
| health_cex | 270 | 3 МБ | 2 |
| health_feeds | 270 | 9 МБ | 2 |
| health_pm | 270 | 3 МБ | 8 |
| kr_trade | 118 | 3 МБ | 545985 |
| ok_trade | 269 | 47 МБ | 0 |
| pm_depth | 270 | 54 МБ | 0 |
| pm_rtt | 270 | 2 МБ | 0 |
| pm_top | 270 | 110 МБ | 0 |
| pm_trades | 270 | 78 МБ | 0 |
| rtds | 270 | 17 МБ | 0 |
| windows | 270 | 557 КБ | 281 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 39, всего 290
- Polymarket CLOB: TCP 5, TLS 40, всего 94
- Polymarket gamma: TCP 5, TLS 49, всего 61

## Последние строки журнала записи
```
17:27:32 [cex] Binance 15 сд. задержка p50/p90=143.5/144.4 мс | Coinbase 44 задержка p50=77.4 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/2.2 мс
17:27:32 [cex] binance_futures 38 сд. p50=147.8 мс | bybit 48 сд. p50=113.3 мс | bybit_book 92 сд. p50=111.4 мс | bybit_spot 97 сд. p50=113.6 мс | bybit_spot_book 136 сд. p50=110.9 мс | okx 89 сд. p50=151.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:27:36 [pm] T-143.9s Up 0.74/0.75 Down 0.25/0.26 ptb=81901.6 | CLOB 5274 сообщ., задержка p50/p90=39.0/45.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792430856096 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.1/2.1 мс
17:27:42 [cex] Binance 83 сд. задержка p50/p90=143.7/144.5 мс | Coinbase 48 задержка p50=77.6 мс | смещение часов +19.0 мс | lag loop p99/max=2.2/2.3 мс
17:27:42 [cex] binance_futures 82 сд. p50=145.4 мс | bybit 107 сд. p50=113.3 мс | bybit_book 149 сд. p50=111.4 мс | bybit_spot 72 сд. p50=113.3 мс | bybit_spot_book 157 сд. p50=110.8 мс | okx 67 сд. p50=151.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:27:46 [pm] T-133.9s Up 0.83/0.84 Down 0.16/0.17 ptb=81901.6 | CLOB 8911 сообщ., задержка p50/p90=39.0/51.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792430866097 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=1.9/2.0 мс
17:27:52 [cex] Binance 94 сд. задержка p50/p90=143.8/144.5 мс | Coinbase 59 задержка p50=78.4 мс | смещение часов +19.0 мс | lag loop p99/max=1.9/2.0 мс
17:27:52 [cex] binance_futures 136 сд. p50=145.5 мс | bybit 171 сд. p50=113.4 мс | bybit_book 170 сд. p50=111.3 мс | bybit_spot 114 сд. p50=113.5 мс | bybit_spot_book 155 сд. p50=110.9 мс | okx 170 сд. p50=152.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:27:56 [pm] T-123.9s Up 0.92/0.93 Down 0.07/0.08 ptb=81901.6 | CLOB 5964 сообщ., задержка p50/p90=40.4/42.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792430876099 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=1.5/2.1 мс
17:28:02 [cex] Binance 68 сд. задержка p50/p90=143.5/144.4 мс | Coinbase 38 задержка p50=77.4 мс | смещение часов +19.0 мс | lag loop p99/max=2.8/3.2 мс
17:28:02 [cex] binance_futures 52 сд. p50=146.0 мс | bybit 56 сд. p50=113.0 мс | bybit_book 164 сд. p50=111.3 мс | bybit_spot 55 сд. p50=113.3 мс | bybit_spot_book 158 сд. p50=110.9 мс | okx 29 сд. p50=151.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:28:06 [pm] T-113.9s Up 0.96/0.97 Down 0.03/0.04 ptb=81901.6 | CLOB 3793 сообщ., задержка p50/p90=40.4/42.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792430886101 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=3.2/6.1 мс
17:28:12 [cex] Binance 19 сд. задержка p50/p90=143.5/144.4 мс | Coinbase 28 задержка p50=77.8 мс | смещение часов +19.0 мс | lag loop p99/max=1.9/2.1 мс
17:28:12 [cex] binance_futures 33 сд. p50=293.2 мс | bybit 51 сд. p50=112.8 мс | bybit_book 101 сд. p50=111.5 мс | bybit_spot 4 сд. p50=113.2 мс | bybit_spot_book 244 сд. p50=110.9 мс | okx 16 сд. p50=150.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:28:16 [pm] T-103.9s Up 0.98/0.99 Down 0.01/0.02 ptb=81901.6 | CLOB 2548 сообщ., задержка p50/p90=40.3/42.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792430896104 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=2.1/2.7 мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
