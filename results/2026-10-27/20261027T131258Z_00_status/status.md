# Состояние сервера записи

Время (UTC): 2026-10-27 13:12:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 6 days, 5 hours, 49 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         651         899           2         530        1254
Swap:           2047         404        1643
```
- нагрузка CPU (1/5/15 мин): 0.28 / 0.36 / 0.48

## Данные
- файлов: 5826, всего 1011 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 34 МБ | 1 |
| bn_book | 242 | 3 МБ | 9 |
| bnf_agg | 242 | 51 МБ | 1 |
| bnf_book | 46 | 337 МБ | 1 |
| bnf_depth5 | 21 | 8 МБ | 1221949 |
| bnf_liq | 216 | 143 КБ | 236 |
| bs_trade | 21 | 349 КБ | 1221868 |
| by_book1 | 242 | 110 МБ | 1 |
| by_liq | 227 | 105 КБ | 170 |
| by_trade | 242 | 34 МБ | 1 |
| bys_book1 | 223 | 74 МБ | 1 |
| bys_trade | 223 | 30 МБ | 3 |
| cb_ticker | 242 | 32 МБ | 1 |
| clock | 242 | 187 КБ | 37 |
| clock_pm | 242 | 188 КБ | 51 |
| events | 233 | 74 КБ | 472 |
| events_pm | 240 | 84 КБ | 1517 |
| health_cex | 242 | 2 МБ | 7 |
| health_feeds | 242 | 7 МБ | 7 |
| health_pm | 242 | 3 МБ | 7 |
| kr_trade | 21 | 737 КБ | 1221868 |
| ok_trade | 241 | 44 МБ | 1 |
| pm_depth | 242 | 49 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 3 |
| pm_top | 242 | 101 МБ | 1 |
| pm_trades | 242 | 71 МБ | 1 |
| rtds | 242 | 15 МБ | 1 |
| windows | 242 | 498 КБ | 143 |

Дни с данными: 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 51, всего 314
- Polymarket CLOB: TCP 5, TLS 49, всего 95
- Polymarket gamma: TCP 4, TLS 88, всего 110

## Последние строки журнала записи
```
13:12:11 [pm] T-168.8s Up 0.95/0.96 Down 0.04/0.05 ptb=80041.5 | CLOB 5892 сообщ., задержка p50/p90=41.5/49.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793106731199 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=4.8/5.1 мс
13:12:11 [cex] Binance 166 сд. задержка p50/p90=155.1/156.7 мс | Coinbase 53 задержка p50=96.1 мс | смещение часов +23.1 мс | lag loop p99/max=5.9/11.9 мс
13:12:11 [cex] binance_futures 396 сд. p50=155.3 мс | bybit 215 сд. p50=123.3 мс | bybit_book 353 сд. p50=112.9 мс | bybit_spot 169 сд. p50=119.3 мс | bybit_spot_book 160 сд. p50=113.6 мс | okx 237 сд. p50=165.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 11567 сд. p50=147.2 мс
13:12:21 [pm] T-158.8s Up 0.96/0.97 Down 0.03/0.04 ptb=80041.5 | CLOB 2861 сообщ., задержка p50/p90=41.2/42.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793106741200 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=1.8/1.9 мс
13:12:21 [cex] Binance 38 сд. задержка p50/p90=146.1/147.0 мс | Coinbase 39 задержка p50=94.8 мс | смещение часов +19.9 мс | lag loop p99/max=2.3/3.0 мс
13:12:21 [cex] binance_futures 62 сд. p50=273.1 мс | bybit 55 сд. p50=115.6 мс | bybit_book 233 сд. p50=112.8 мс | bybit_spot 73 сд. p50=116.8 мс | bybit_spot_book 82 сд. p50=113.4 мс | okx 406 сд. p50=158.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2356 сд. p50=146.7 мс
13:12:31 [pm] T-148.8s Up 0.91/0.92 Down 0.08/0.09 ptb=80041.5 | CLOB 5759 сообщ., задержка p50/p90=41.3/42.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793106751202 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=1.7/3.3 мс
13:12:31 [cex] Binance 99 сд. задержка p50/p90=143.2/144.8 мс | Coinbase 44 задержка p50=92.4 мс | смещение часов +19.9 мс | lag loop p99/max=3.2/13.3 мс
13:12:31 [cex] binance_futures 178 сд. p50=150.0 мс | bybit 139 сд. p50=112.5 мс | bybit_book 263 сд. p50=109.7 мс | bybit_spot 232 сд. p50=112.6 мс | bybit_spot_book 173 сд. p50=110.3 мс | okx 258 сд. p50=154.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 6367 сд. p50=144.1 мс
13:12:41 [pm] T-138.8s Up 0.93/0.94 Down 0.06/0.07 ptb=80041.5 | CLOB 4561 сообщ., задержка p50/p90=42.1/48.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793106761204 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=2.1/2.2 мс
13:12:41 [cex] Binance 45 сд. задержка p50/p90=143.3/144.4 мс | Coinbase 34 задержка p50=92.3 мс | смещение часов +19.9 мс | lag loop p99/max=2.1/2.2 мс
13:12:41 [cex] binance_futures 59 сд. p50=256.4 мс | bybit 64 сд. p50=112.2 мс | bybit_book 326 сд. p50=109.7 мс | bybit_spot 95 сд. p50=112.6 мс | bybit_spot_book 135 сд. p50=110.3 мс | okx 261 сд. p50=156.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2298 сд. p50=143.5 мс
13:12:51 [pm] T-128.8s Up 0.97/0.98 Down 0.02/0.03 ptb=80041.5 | CLOB 8511 сообщ., задержка p50/p90=41.3/43.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793106771206 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=1.7/2.1 мс
13:12:51 [cex] Binance 97 сд. задержка p50/p90=143.4/152.4 мс | Coinbase 44 задержка p50=92.1 мс | смещение часов +19.9 мс | lag loop p99/max=1.8/2.0 мс
13:12:51 [cex] binance_futures 111 сд. p50=148.6 мс | bybit 141 сд. p50=113.2 мс | bybit_book 443 сд. p50=109.7 мс | bybit_spot 201 сд. p50=114.8 мс | bybit_spot_book 157 сд. p50=110.3 мс | okx 121 сд. p50=153.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2786 сд. p50=148.5 мс
```

Представлено версией кода: 79ba999; python 3.12.3
