# Состояние сервера записи

Время (UTC): 2026-10-30 04:23:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 1 day, 20 hours, 59 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         640         840           1         608        1265
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.25 / 0.22 / 0.27

## Данные
- файлов: 5830, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 38 МБ | 0 |
| bn_book | 242 | 3 МБ | 4 |
| bnf_agg | 242 | 54 МБ | 0 |
| bnf_book | 88 | 639 МБ | 0 |
| bnf_liq | 211 | 144 КБ | 99 |
| by_book1 | 242 | 114 МБ | 0 |
| by_liq | 226 | 119 КБ | 244 |
| by_trade | 242 | 36 МБ | 0 |
| bys_book1 | 242 | 85 МБ | 0 |
| bys_trade | 242 | 35 МБ | 0 |
| cb_ticker | 242 | 33 МБ | 0 |
| clock | 242 | 188 КБ | 41 |
| clock_pm | 242 | 188 КБ | 11 |
| events | 225 | 72 КБ | 3293 |
| events_pm | 241 | 85 КБ | 120 |
| health_cex | 242 | 3 МБ | 4 |
| health_feeds | 242 | 8 МБ | 4 |
| health_pm | 242 | 3 МБ | 3 |
| ok_trade | 242 | 47 МБ | 0 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 3 |
| pm_top | 242 | 100 МБ | 1 |
| pm_trades | 241 | 71 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 498 КБ | 184 |

Дни с данными: 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 42, всего 293
- Polymarket CLOB: TCP 5, TLS 40, всего 81
- Polymarket gamma: TCP 3, TLS 37, всего 45

## Последние строки журнала записи
```
04:22:23 [cex] Binance 130 сд. задержка p50/p90=148.1/152.2 мс | Coinbase 65 задержка p50=86.1 мс | смещение часов +22.7 мс | lag loop p99/max=4.6/7.2 мс
04:22:23 [cex] binance_futures 243 сд. p50=151.4 мс | bybit 122 сд. p50=116.1 мс | bybit_book 357 сд. p50=113.9 мс | bybit_spot 226 сд. p50=117.2 мс | bybit_spot_book 150 сд. p50=114.9 мс | okx 245 сд. p50=160.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 11376 сд. p50=146.8 мс
04:22:25 [pm] T-154.2s Up 0.17/0.18 Down 0.82/0.83 ptb=78147.1 | CLOB 10332 сообщ., задержка p50/p90=43.7/50.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793334145838 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.3 мс | lag loop p99/max=1.3/1.8 мс
04:22:33 [cex] Binance 90 сд. задержка p50/p90=147.6/156.2 мс | Coinbase 65 задержка p50=85.9 мс | смещение часов +21.2 мс | lag loop p99/max=3.6/7.7 мс
04:22:33 [cex] binance_futures 153 сд. p50=152.9 мс | bybit 115 сд. p50=114.7 мс | bybit_book 326 сд. p50=112.6 мс | bybit_spot 282 сд. p50=115.9 мс | bybit_spot_book 139 сд. p50=114.6 мс | okx 177 сд. p50=159.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4931 сд. p50=150.1 мс
04:22:35 [pm] T-144.2s Up 0.18/0.19 Down 0.81/0.82 ptb=78147.1 | CLOB 8520 сообщ., задержка p50/p90=43.2/50.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793334155840 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.5 мс | lag loop p99/max=2.3/2.7 мс
04:22:43 [cex] Binance 88 сд. задержка p50/p90=147.1/148.2 мс | Coinbase 48 задержка p50=84.6 мс | смещение часов +21.2 мс | lag loop p99/max=5.7/8.7 мс
04:22:43 [cex] binance_futures 207 сд. p50=153.7 мс | bybit 84 сд. p50=115.2 мс | bybit_book 290 сд. p50=112.4 мс | bybit_spot 213 сд. p50=115.0 мс | bybit_spot_book 132 сд. p50=113.4 мс | okx 118 сд. p50=158.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5074 сд. p50=147.8 мс
04:22:45 [pm] T-134.2s Up 0.14/0.15 Down 0.85/0.86 ptb=78147.1 | CLOB 7701 сообщ., задержка p50/p90=42.8/44.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793334165841 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.5 мс | lag loop p99/max=1.4/1.8 мс
04:22:53 [cex] Binance 86 сд. задержка p50/p90=147.5/148.1 мс | Coinbase 74 задержка p50=85.0 мс | смещение часов +21.2 мс | lag loop p99/max=2.4/4.7 мс
04:22:53 [cex] binance_futures 167 сд. p50=154.1 мс | bybit 142 сд. p50=114.5 мс | bybit_book 273 сд. p50=112.4 мс | bybit_spot 270 сд. p50=116.3 мс | bybit_spot_book 117 сд. p50=113.5 мс | okx 156 сд. p50=158.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4631 сд. p50=145.7 мс
04:22:55 [pm] T-124.2s Up 0.29/0.30 Down 0.70/0.71 ptb=78147.1 | CLOB 10718 сообщ., задержка p50/p90=43.3/118.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793334175843 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.5 мс | lag loop p99/max=1.7/2.1 мс
04:23:03 [cex] Binance 146 сд. задержка p50/p90=146.9/151.1 мс | Coinbase 50 задержка p50=84.8 мс | смещение часов +21.2 мс | lag loop p99/max=2.2/5.0 мс
04:23:03 [cex] binance_futures 144 сд. p50=148.6 мс | bybit 114 сд. p50=115.4 мс | bybit_book 207 сд. p50=112.4 мс | bybit_spot 131 сд. p50=115.2 мс | bybit_spot_book 88 сд. p50=113.4 мс | okx 94 сд. p50=158.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1800 сд. p50=145.7 мс
04:23:05 [pm] T-114.2s Up 0.23/0.24 Down 0.76/0.77 ptb=78147.1 | CLOB 6869 сообщ., задержка p50/p90=43.8/47.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793334185844 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=41.5 мс | lag loop p99/max=1.7/24.1 мс
```

Представлено версией кода: b8783c2; python 3.12.3
