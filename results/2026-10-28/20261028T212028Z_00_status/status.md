# Состояние сервера записи

Время (UTC): 2026-10-28 21:20:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 13 hours, 56 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 12 ГБ из 57 ГБ, свободно 45 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         606         783           1         691        1299
Swap:           2047         304        1743
```
- нагрузка CPU (1/5/15 мин): 0.07 / 0.21 / 0.27

## Данные
- файлов: 5806, всего 1024 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 34 МБ | 1 |
| bn_book | 242 | 3 МБ | 1 |
| bnf_agg | 242 | 49 МБ | 1 |
| bnf_book | 57 | 356 МБ | 1 |
| bnf_liq | 211 | 136 КБ | 228 |
| by_book1 | 242 | 108 МБ | 1 |
| by_liq | 226 | 99 КБ | 226 |
| by_trade | 242 | 33 МБ | 1 |
| bys_book1 | 242 | 82 МБ | 1 |
| bys_trade | 242 | 32 МБ | 3 |
| cb_ticker | 242 | 32 МБ | 1 |
| clock | 242 | 187 КБ | 50 |
| clock_pm | 242 | 187 КБ | 18 |
| events | 232 | 73 КБ | 5787 |
| events_pm | 240 | 83 КБ | 1782 |
| health_cex | 242 | 2 МБ | 6 |
| health_feeds | 242 | 7 МБ | 6 |
| health_pm | 242 | 3 МБ | 8 |
| ok_trade | 242 | 43 МБ | 1 |
| pm_depth | 242 | 49 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 4 |
| pm_top | 242 | 101 МБ | 2 |
| pm_trades | 242 | 71 МБ | 2 |
| rtds | 242 | 15 МБ | 2 |
| windows | 242 | 498 КБ | 325 |

Дни с данными: 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 42, всего 293
- Polymarket CLOB: TCP 5, TLS 45, всего 92
- Polymarket gamma: TCP 6, TLS 40, всего 49

## Последние строки журнала записи
```
21:19:42 [cex] binance_futures 67 сд. p50=153.3 мс | bybit 32 сд. p50=111.4 мс | bybit_book 101 сд. p50=110.0 мс | bybit_spot 64 сд. p50=114.3 мс | bybit_spot_book 63 сд. p50=109.7 мс | okx 50 сд. p50=156.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2328 сд. p50=144.3 мс
21:19:45 [pm] окно btc-updown-5m-1793222400 (2026-10-28 21:20:00 UTC): Bitcoin Up or Down - October 28, 5:20PM-5:25PM ET
21:19:49 [pm] T- 11.0s Up 0.99/n/a Down n/a/0.01 ptb=81301.2 | CLOB 1047 сообщ., задержка p50/p90=42.8/45.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793222389022 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=2.1/2.2 мс
21:19:52 [cex] Binance 12 сд. задержка p50/p90=141.6/142.4 мс | Coinbase 59 задержка p50=88.7 мс | смещение часов +17.6 мс | lag loop p99/max=2.1/2.2 мс
21:19:52 [cex] binance_futures 17 сд. p50=291.9 мс | bybit 7 сд. p50=111.8 мс | bybit_book 57 сд. p50=109.2 мс | bybit_spot 3 сд. p50=111.1 мс | bybit_spot_book 38 сд. p50=109.1 мс | okx 8 сд. p50=154.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 738 сд. p50=142.7 мс
21:19:59 [pm] T-  1.0s Up 0.99/n/a Down n/a/0.01 ptb=81301.2 | CLOB 2329 сообщ., задержка p50/p90=43.3/112.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793222399023 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=2.1/2.2 мс
21:20:02 [cex] Binance 15 сд. задержка p50/p90=141.5/141.7 мс | Coinbase 38 задержка p50=88.3 мс | смещение часов +17.6 мс | lag loop p99/max=2.4/2.6 мс
21:20:02 [cex] binance_futures 34 сд. p50=218.3 мс | bybit 59 сд. p50=111.4 мс | bybit_book 166 сд. p50=109.2 мс | bybit_spot 57 сд. p50=117.7 мс | bybit_spot_book 63 сд. p50=109.2 мс | okx 42 сд. p50=155.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2095 сд. p50=154.0 мс
21:20:09 [pm] T-291.0s Up 0.48/0.49 Down 0.51/0.52 ptb=81322.6 | CLOB 4209 сообщ., задержка p50/p90=42.8/44.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793222409024 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=4.0/4.5 мс
21:20:12 [cex] Binance 17 сд. задержка p50/p90=141.5/142.4 мс | Coinbase 24 задержка p50=88.3 мс | смещение часов +17.6 мс | lag loop p99/max=2.1/2.2 мс
21:20:12 [cex] binance_futures 20 сд. p50=292.4 мс | bybit 40 сд. p50=110.2 мс | bybit_book 108 сд. p50=109.2 мс | bybit_spot 2 сд. p50=111.3 мс | bybit_spot_book 34 сд. p50=109.2 мс | okx 7 сд. p50=155.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 700 сд. p50=142.6 мс
21:20:19 [pm] T-281.0s Up 0.47/0.48 Down 0.52/0.53 ptb=81322.6 | CLOB 4446 сообщ., задержка p50/p90=40.3/43.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793222419026 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.3/2.0 мс
21:20:22 [cex] Binance 18 сд. задержка p50/p90=141.5/141.9 мс | Coinbase 40 задержка p50=88.8 мс | смещение часов +17.6 мс | lag loop p99/max=1.8/2.0 мс
21:20:22 [cex] binance_futures 16 сд. p50=292.2 мс | bybit 9 сд. p50=110.6 мс | bybit_book 95 сд. p50=109.2 мс | bybit_spot 4 сд. p50=111.1 мс | bybit_spot_book 36 сд. p50=109.0 мс | okx 9 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 633 сд. p50=142.7 мс
21:20:29 [pm] T-271.0s Up 0.51/0.52 Down 0.48/0.49 ptb=81322.6 | CLOB 5090 сообщ., задержка p50/p90=40.6/48.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793222429027 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.9/2.0 мс
```

Представлено версией кода: 65c4468; python 3.12.3
