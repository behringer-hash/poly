# Состояние сервера записи

Время (UTC): 2026-10-30 15:47:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 2 days, 8 hours, 23 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         650         545           1         895        1255
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.53 / 0.44 / 0.43

## Данные
- файлов: 5842, всего 2 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 40 МБ | 2 |
| bn_book | 242 | 3 МБ | 2 |
| bnf_agg | 242 | 58 МБ | 2 |
| bnf_book | 99 | 909 МБ | 0 |
| bnf_liq | 212 | 153 КБ | 162 |
| by_book1 | 242 | 122 МБ | 2 |
| by_liq | 225 | 120 КБ | 291 |
| by_trade | 242 | 41 МБ | 2 |
| bys_book1 | 242 | 88 МБ | 2 |
| bys_trade | 242 | 38 МБ | 2 |
| cb_ticker | 242 | 34 МБ | 2 |
| clock | 242 | 188 КБ | 60 |
| clock_pm | 242 | 188 КБ | 34 |
| events | 226 | 72 КБ | 6175 |
| events_pm | 241 | 85 КБ | 290 |
| health_cex | 242 | 3 МБ | 8 |
| health_feeds | 242 | 8 МБ | 8 |
| health_pm | 242 | 3 МБ | 6 |
| ok_trade | 242 | 51 МБ | 2 |
| pm_depth | 242 | 50 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 6 |
| pm_top | 242 | 102 МБ | 2 |
| pm_trades | 241 | 72 МБ | 2 |
| rtds | 242 | 16 МБ | 2 |
| windows | 242 | 501 КБ | 34 |

Дни с данными: 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 46, всего 296
- Polymarket CLOB: TCP 6, TLS 43, всего 89
- Polymarket gamma: TCP 4, TLS 58, всего 65

## Последние строки журнала записи
```
15:46:21 [cex] Binance 200 сд. задержка p50/p90=143.6/147.9 мс | Coinbase 90 задержка p50=89.7 мс | смещение часов +19.3 мс | lag loop p99/max=3.9/4.7 мс
15:46:21 [cex] binance_futures 206 сд. p50=150.1 мс | bybit 258 сд. p50=114.1 мс | bybit_book 266 сд. p50=110.6 мс | bybit_spot 185 сд. p50=114.1 мс | bybit_spot_book 139 сд. p50=111.0 мс | okx 224 сд. p50=156.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5909 сд. p50=146.6 мс
15:46:21 [pm] T-218.0s Up 0.16/0.19 Down 0.81/0.84 ptb=77403.6 | CLOB 5741 сообщ., задержка p50/p90=44.0/48.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793375181963 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.3/1.3 мс
15:46:31 [cex] Binance 228 сд. задержка p50/p90=144.4/149.1 мс | Coinbase 120 задержка p50=93.8 мс | смещение часов +19.3 мс | lag loop p99/max=6.8/12.0 мс
15:46:31 [cex] binance_futures 409 сд. p50=149.6 мс | bybit 502 сд. p50=113.3 мс | bybit_book 413 сд. p50=110.6 мс | bybit_spot 345 сд. p50=113.1 мс | bybit_spot_book 262 сд. p50=111.0 мс | okx 314 сд. p50=157.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 11998 сд. p50=143.8 мс
15:46:31 [pm] T-208.0s Up 0.16/0.17 Down 0.83/0.84 ptb=77403.6 | CLOB 8517 сообщ., задержка p50/p90=43.7/57.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793375191964 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.7/2.1 мс
15:46:41 [cex] Binance 45 сд. задержка p50/p90=143.4/144.3 мс | Coinbase 41 задержка p50=89.0 мс | смещение часов +19.3 мс | lag loop p99/max=1.8/2.1 мс
15:46:41 [cex] binance_futures 48 сд. p50=293.4 мс | bybit 52 сд. p50=112.8 мс | bybit_book 220 сд. p50=110.6 мс | bybit_spot 81 сд. p50=113.3 мс | bybit_spot_book 87 сд. p50=110.9 мс | okx 21 сд. p50=154.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1249 сд. p50=143.4 мс
15:46:41 [pm] T-198.0s Up 0.15/0.16 Down 0.84/0.85 ptb=77403.6 | CLOB 2642 сообщ., задержка p50/p90=38.7/43.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793375201965 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.0/2.1 мс
15:46:51 [cex] Binance 290 сд. задержка p50/p90=143.8/148.5 мс | Coinbase 151 задержка p50=92.1 мс | смещение часов +19.3 мс | lag loop p99/max=6.1/6.6 мс
15:46:51 [cex] binance_futures 418 сд. p50=148.2 мс | bybit 345 сд. p50=114.8 мс | bybit_book 320 сд. p50=110.7 мс | bybit_spot 402 сд. p50=113.9 мс | bybit_spot_book 164 сд. p50=111.1 мс | okx 397 сд. p50=159.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 9360 сд. p50=144.5 мс
15:46:51 [pm] T-188.0s Up 0.24/0.25 Down 0.75/0.76 ptb=77403.6 | CLOB 7036 сообщ., задержка p50/p90=40.6/61.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793375211966 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.0/2.0 мс
15:47:01 [cex] Binance 138 сд. задержка p50/p90=143.4/145.6 мс | Coinbase 88 задержка p50=89.4 мс | смещение часов +19.3 мс | lag loop p99/max=3.8/7.7 мс
15:47:01 [cex] binance_futures 189 сд. p50=148.7 мс | bybit 168 сд. p50=113.6 мс | bybit_book 261 сд. p50=110.6 мс | bybit_spot 226 сд. p50=112.9 мс | bybit_spot_book 146 сд. p50=111.0 мс | okx 156 сд. p50=157.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4318 сд. p50=143.7 мс
15:47:01 [pm] T-178.0s Up 0.16/0.17 Down 0.83/0.84 ptb=77403.6 | CLOB 6519 сообщ., задержка p50/p90=40.5/52.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793375221968 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.1/2.1 мс
```

Представлено версией кода: fcaf736; python 3.12.3
