# Состояние сервера записи

Время (UTC): 2026-10-28 10:58:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 3 hours, 34 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         616         281           2        1192        1289
Swap:           2047         277        1770
```
- нагрузка CPU (1/5/15 мин): 0.19 / 0.17 / 0.17

## Данные
- файлов: 5793, всего 997 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 36 МБ | 2 |
| bn_book | 242 | 3 МБ | 4 |
| bnf_agg | 242 | 50 МБ | 2 |
| bnf_book | 46 | 321 МБ | 0 |
| bnf_liq | 209 | 133 КБ | 190 |
| by_book1 | 242 | 109 МБ | 2 |
| by_liq | 225 | 97 КБ | 6278 |
| by_trade | 242 | 33 МБ | 2 |
| bys_book1 | 242 | 83 МБ | 2 |
| bys_trade | 242 | 32 МБ | 4 |
| cb_ticker | 242 | 32 МБ | 2 |
| clock | 242 | 189 КБ | 42 |
| clock_pm | 242 | 189 КБ | 62 |
| events | 233 | 74 КБ | 697 |
| events_pm | 241 | 84 КБ | 40 |
| health_cex | 242 | 3 МБ | 4 |
| health_feeds | 242 | 7 МБ | 4 |
| health_pm | 242 | 3 МБ | 6 |
| ok_trade | 241 | 43 МБ | 2 |
| pm_depth | 242 | 50 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 6 |
| pm_top | 242 | 103 МБ | 2 |
| pm_trades | 242 | 71 МБ | 2 |
| rtds | 242 | 16 МБ | 2 |
| windows | 242 | 502 КБ | 293 |

Дни с данными: 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 36, всего 287
- Polymarket CLOB: TCP 6, TLS 40, всего 88
- Polymarket gamma: TCP 4, TLS 43, всего 49

## Последние строки журнала записи
```
10:57:42 [pm] T-137.3s Up 0.19/0.20 Down 0.80/0.81 ptb=81433.9 | CLOB 7557 сообщ., задержка p50/p90=42.8/45.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793185062668 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=1.2/1.2 мс
10:57:44 [cex] Binance 133 сд. задержка p50/p90=146.1/147.1 мс | Coinbase 1 задержка p50=91.6 мс | смещение часов +21.0 мс | lag loop p99/max=2.0/2.1 мс
10:57:44 [cex] binance_futures 59 сд. p50=294.7 мс | bybit 87 сд. p50=114.6 мс | bybit_book 87 сд. p50=112.2 мс | bybit_spot 171 сд. p50=114.7 мс | bybit_spot_book 78 сд. p50=112.5 мс | okx 43 сд. p50=159.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1948 сд. p50=145.9 мс
10:57:52 [pm] T-127.3s Up 0.10/0.11 Down 0.89/0.90 ptb=81433.9 | CLOB 5141 сообщ., задержка p50/p90=37.8/43.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793185072670 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.0/2.5 мс
10:57:54 [cex] Binance 130 сд. задержка p50/p90=144.6/146.2 мс | Coinbase 8 задержка p50=93.6 мс | смещение часов +19.4 мс | lag loop p99/max=2.0/2.2 мс
10:57:54 [cex] binance_futures 59 сд. p50=293.1 мс | bybit 41 сд. p50=112.9 мс | bybit_book 135 сд. p50=110.7 мс | bybit_spot 6 сд. p50=112.7 мс | bybit_spot_book 63 сд. p50=111.0 мс | okx 49 сд. p50=157.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 647 сд. p50=144.3 мс
10:58:02 [pm] T-117.3s Up 0.08/0.09 Down 0.91/0.92 ptb=81433.9 | CLOB 3972 сообщ., задержка p50/p90=37.6/43.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793185082671 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.7/1.8 мс
10:58:04 [cex] Binance 107 сд. задержка p50/p90=144.6/145.7 мс | Coinbase 6 задержка p50=89.9 мс | смещение часов +19.4 мс | lag loop p99/max=2.2/2.2 мс
10:58:04 [cex] binance_futures 48 сд. p50=293.6 мс | bybit 17 сд. p50=112.5 мс | bybit_book 109 сд. p50=110.8 мс | bybit_spot 3 сд. p50=112.5 мс | bybit_spot_book 34 сд. p50=110.9 мс | okx 13 сд. p50=157.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 391 сд. p50=144.3 мс
10:58:12 [pm] T-107.3s Up 0.08/0.09 Down 0.91/0.92 ptb=81433.9 | CLOB 3396 сообщ., задержка p50/p90=37.4/39.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793185092672 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.2/1.2 мс
10:58:14 [cex] Binance 110 сд. задержка p50/p90=144.6/145.5 мс | Coinbase 8 задержка p50=89.6 мс | смещение часов +19.4 мс | lag loop p99/max=2.0/2.2 мс
10:58:14 [cex] binance_futures 48 сд. p50=293.3 мс | bybit 12 сд. p50=112.1 мс | bybit_book 135 сд. p50=110.7 мс | bybit_spot 1 сд. p50=112.5 мс | bybit_spot_book 43 сд. p50=111.0 мс | okx 7 сд. p50=157.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 359 сд. p50=144.2 мс
10:58:22 [pm] T- 97.3s Up 0.05/0.06 Down 0.94/0.95 ptb=81433.9 | CLOB 3311 сообщ., задержка p50/p90=37.9/105.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793185102674 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.3/2.0 мс
10:58:24 [cex] Binance 163 сд. задержка p50/p90=144.8/148.0 мс | Coinbase 14 задержка p50=101.3 мс | смещение часов +19.4 мс | lag loop p99/max=2.1/2.9 мс
10:58:24 [cex] binance_futures 93 сд. p50=153.4 мс | bybit 149 сд. p50=116.7 мс | bybit_book 152 сд. p50=110.7 мс | bybit_spot 117 сд. p50=118.0 мс | bybit_spot_book 59 сд. p50=110.8 мс | okx 109 сд. p50=160.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2973 сд. p50=144.5 мс
```

Представлено версией кода: adb4c8b; python 3.12.3
