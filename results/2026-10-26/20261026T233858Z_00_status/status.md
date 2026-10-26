# Состояние сервера записи

Время (UTC): 2026-10-26 23:38:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 5 days, 16 hours, 15 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         670         881           1         526        1235
Swap:           2047         293        1754
```
- нагрузка CPU (1/5/15 мин): 0.44 / 0.42 / 0.35

## Данные
- файлов: 5840, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 1 |
| bn_book | 242 | 3 МБ | 55 |
| bnf_agg | 242 | 52 МБ | 1 |
| bnf_book | 46 | 376 МБ | 1 |
| bnf_depth5 | 35 | 13 МБ | 1173109 |
| bnf_liq | 216 | 146 КБ | 82 |
| bs_trade | 35 | 501 КБ | 1173028 |
| by_book1 | 242 | 110 МБ | 1 |
| by_liq | 229 | 108 КБ | 269 |
| by_trade | 242 | 35 МБ | 3 |
| bys_book1 | 209 | 71 МБ | 1 |
| bys_trade | 209 | 28 МБ | 3 |
| cb_ticker | 242 | 33 МБ | 1 |
| clock | 242 | 188 КБ | 45 |
| clock_pm | 242 | 189 КБ | 55 |
| events | 230 | 72 КБ | 1103 |
| events_pm | 241 | 84 КБ | 356 |
| health_cex | 242 | 2 МБ | 5 |
| health_feeds | 242 | 8 МБ | 5 |
| health_pm | 242 | 3 МБ | 4 |
| kr_trade | 35 | 1 МБ | 1173028 |
| ok_trade | 241 | 45 МБ | 1 |
| pm_depth | 242 | 49 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 4 |
| pm_top | 242 | 103 МБ | 2 |
| pm_trades | 242 | 72 МБ | 2 |
| rtds | 242 | 16 МБ | 2 |
| windows | 242 | 500 КБ | 294 |

Дни с данными: 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 39, всего 285
- Polymarket CLOB: TCP 5, TLS 40, всего 82
- Polymarket gamma: TCP 5, TLS 38, всего 44

## Последние строки журнала записи
```
23:38:13 [cex] Binance 10 сд. задержка p50/p90=148.5/149.5 мс | Coinbase 32 задержка p50=85.6 мс | смещение часов +21.0 мс | lag loop p99/max=2.3/3.1 мс
23:38:13 [cex] binance_futures 25 сд. p50=298.4 мс | bybit 22 сд. p50=117.4 мс | bybit_book 252 сд. p50=115.3 мс | bybit_spot 2 сд. p50=118.0 мс | bybit_spot_book 37 сд. p50=116.3 мс | okx 19 сд. p50=165.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1265 сд. p50=149.5 мс
23:38:13 [pm] T-106.4s Up 0.81/0.82 Down 0.18/0.19 ptb=79995.4 | CLOB 7461 сообщ., задержка p50/p90=42.9/45.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793057893600 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.5 мс | lag loop p99/max=1.3/1.7 мс
23:38:23 [cex] Binance 9 сд. задержка p50/p90=143.9/144.8 мс | Coinbase 42 задержка p50=82.7 мс | смещение часов +21.0 мс | lag loop p99/max=2.1/2.2 мс
23:38:23 [cex] binance_futures 16 сд. p50=293.8 мс | bybit 20 сд. p50=112.5 мс | bybit_book 106 сд. p50=110.7 мс | bybit_spot 110 сд. p50=117.4 мс | bybit_spot_book 42 сд. p50=111.5 мс | okx 18 сд. p50=161.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1407 сд. p50=144.9 мс
23:38:23 [pm] T- 96.4s Up 0.89/0.90 Down 0.10/0.11 ptb=79995.4 | CLOB 6228 сообщ., задержка p50/p90=43.0/44.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793057903602 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.5 мс | lag loop p99/max=1.2/2.1 мс
23:38:33 [cex] Binance 7 сд. задержка p50/p90=144.0/144.7 мс | Coinbase 53 задержка p50=83.1 мс | смещение часов +21.0 мс | lag loop p99/max=2.1/2.2 мс
23:38:33 [cex] binance_futures 15 сд. p50=294.4 мс | bybit 24 сд. p50=112.6 мс | bybit_book 119 сд. p50=110.7 мс | bybit_spot 2 сд. p50=113.1 мс | bybit_spot_book 28 сд. p50=111.6 мс | okx 14 сд. p50=160.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1326 сд. p50=144.7 мс
23:38:33 [pm] T- 86.4s Up 0.86/0.87 Down 0.13/0.14 ptb=79995.4 | CLOB 4174 сообщ., задержка p50/p90=43.0/45.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793057913604 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.5 мс | lag loop p99/max=1.9/2.0 мс
23:38:43 [cex] Binance 10 сд. задержка p50/p90=143.8/144.2 мс | Coinbase 47 задержка p50=82.4 мс | смещение часов +21.0 мс | lag loop p99/max=2.3/3.1 мс
23:38:43 [cex] binance_futures 18 сд. p50=293.8 мс | bybit 30 сд. p50=113.5 мс | bybit_book 90 сд. p50=110.7 мс | bybit_spot 2 сд. p50=114.2 мс | bybit_spot_book 25 сд. p50=111.6 мс | okx 8 сд. p50=161.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 862 сд. p50=144.8 мс
23:38:43 [pm] T- 76.4s Up 0.88/0.89 Down 0.11/0.12 ptb=79995.4 | CLOB 3828 сообщ., задержка p50/p90=42.8/44.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793057923605 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.5 мс | lag loop p99/max=2.1/2.2 мс
23:38:53 [cex] Binance 7 сд. задержка p50/p90=143.7/144.2 мс | Coinbase 32 задержка p50=81.7 мс | смещение часов +21.0 мс | lag loop p99/max=2.2/2.6 мс
23:38:53 [cex] binance_futures 16 сд. p50=294.5 мс | bybit 5 сд. p50=112.4 мс | bybit_book 154 сд. p50=110.7 мс | bybit_spot 50 сд. p50=114.5 мс | bybit_spot_book 44 сд. p50=111.5 мс | okx 13 сд. p50=160.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1358 сд. p50=144.8 мс
23:38:53 [pm] T- 66.4s Up 0.92/0.93 Down 0.07/0.08 ptb=79995.4 | CLOB 4616 сообщ., задержка p50/p90=43.2/48.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793057933607 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.5 мс | lag loop p99/max=1.8/1.9 мс
```

Представлено версией кода: 80591e6; python 3.12.3
