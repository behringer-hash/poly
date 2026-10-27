# Состояние сервера записи

Время (UTC): 2026-10-27 04:47:35

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 5 days, 21 hours, 23 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         703         790           1         590        1202
Swap:           2047         293        1754
```
- нагрузка CPU (1/5/15 мин): 0.58 / 0.41 / 0.34

## Данные
- файлов: 5835, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 2 |
| bn_book | 242 | 3 МБ | 18 |
| bnf_agg | 242 | 51 МБ | 2 |
| bnf_book | 46 | 364 МБ | 0 |
| bnf_depth5 | 30 | 12 МБ | 1191625 |
| bnf_liq | 216 | 146 КБ | 2572 |
| bs_trade | 30 | 458 КБ | 1191545 |
| by_book1 | 242 | 111 МБ | 2 |
| by_liq | 228 | 108 КБ | 5362 |
| by_trade | 242 | 34 МБ | 2 |
| bys_book1 | 214 | 72 МБ | 2 |
| bys_trade | 214 | 29 МБ | 2 |
| cb_ticker | 242 | 33 МБ | 2 |
| clock | 242 | 188 КБ | 56 |
| clock_pm | 242 | 189 КБ | 5 |
| events | 231 | 74 КБ | 125 |
| events_pm | 241 | 84 КБ | 1013 |
| health_cex | 242 | 2 МБ | 8 |
| health_feeds | 242 | 8 МБ | 8 |
| health_pm | 242 | 3 МБ | 9 |
| kr_trade | 30 | 990 КБ | 1191545 |
| ok_trade | 241 | 45 МБ | 2 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 3 |
| pm_top | 242 | 103 МБ | 1 |
| pm_trades | 242 | 72 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 501 КБ | 121 |

Дни с данными: 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 37, всего 285
- Polymarket CLOB: TCP 6, TLS 50, всего 91
- Polymarket gamma: TCP 4, TLS 46, всего 53

## Последние строки журнала записи
```
04:46:46 [cex] Binance 269 сд. задержка p50/p90=145.1/149.3 мс | Coinbase 219 задержка p50=102.3 мс | смещение часов +20.5 мс | lag loop p99/max=3.6/5.0 мс
04:46:46 [cex] binance_futures 102 сд. p50=147.6 мс | bybit 85 сд. p50=114.0 мс | bybit_book 173 сд. p50=110.3 мс | bybit_spot 81 сд. p50=117.7 мс | bybit_spot_book 87 сд. p50=110.4 мс | okx 91 сд. p50=160.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1962 сд. p50=144.7 мс
04:46:46 [pm] T-193.6s Up 0.71/0.72 Down 0.28/0.29 ptb=79517.4 | CLOB 13099 сообщ., задержка p50/p90=44.3/46.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793076406362 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.9 мс | lag loop p99/max=6.0/15.6 мс
04:46:56 [cex] Binance 100 сд. задержка p50/p90=143.4/144.4 мс | Coinbase 50 задержка p50=92.3 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/2.1 мс
04:46:56 [cex] binance_futures 78 сд. p50=159.0 мс | bybit 50 сд. p50=113.1 мс | bybit_book 172 сд. p50=110.3 мс | bybit_spot 195 сд. p50=113.2 мс | bybit_spot_book 90 сд. p50=110.4 мс | okx 170 сд. p50=160.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2906 сд. p50=144.6 мс
04:46:56 [pm] T-183.6s Up 0.57/0.58 Down 0.42/0.43 ptb=79517.4 | CLOB 7507 сообщ., задержка p50/p90=45.3/50.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793076416363 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.8/1.8 мс
04:47:06 [cex] Binance 40 сд. задержка p50/p90=143.3/144.3 мс | Coinbase 196 задержка p50=180.4 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/2.1 мс
04:47:06 [cex] binance_futures 27 сд. p50=292.9 мс | bybit 6 сд. p50=112.5 мс | bybit_book 213 сд. p50=110.3 мс | bybit_spot 15 сд. p50=112.2 мс | bybit_spot_book 38 сд. p50=110.4 мс | okx 99 сд. p50=160.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 815 сд. p50=144.1 мс
04:47:06 [pm] T-173.6s Up 0.64/0.65 Down 0.35/0.36 ptb=79517.4 | CLOB 10457 сообщ., задержка p50/p90=44.4/46.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793076426365 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.2/1.3 мс
04:47:16 [cex] Binance 38 сд. задержка p50/p90=143.3/144.1 мс | Coinbase 103 задержка p50=120.4 мс | смещение часов +20.5 мс | lag loop p99/max=2.2/2.6 мс
04:47:16 [cex] binance_futures 21 сд. p50=293.2 мс | bybit 26 сд. p50=112.3 мс | bybit_book 168 сд. p50=110.3 мс | bybit_spot 12 сд. p50=112.5 мс | bybit_spot_book 50 сд. p50=110.3 мс | okx 36 сд. p50=160.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 779 сд. p50=144.2 мс
04:47:16 [pm] T-163.6s Up 0.66/0.67 Down 0.33/0.34 ptb=79517.4 | CLOB 7805 сообщ., задержка p50/p90=44.3/45.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793076436367 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.7/2.1 мс
04:47:26 [cex] Binance 74 сд. задержка p50/p90=143.6/146.0 мс | Coinbase 43 задержка p50=91.0 мс | смещение часов +20.5 мс | lag loop p99/max=2.2/2.4 мс
04:47:26 [cex] binance_futures 29 сд. p50=292.8 мс | bybit 10 сд. p50=112.0 мс | bybit_book 92 сд. p50=110.3 мс | bybit_spot 16 сд. p50=112.3 мс | bybit_spot_book 40 сд. p50=110.4 мс | okx 36 сд. p50=160.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1376 сд. p50=144.3 мс
04:47:26 [pm] T-153.6s Up 0.70/0.71 Down 0.29/0.30 ptb=79517.4 | CLOB 7600 сообщ., задержка p50/p90=44.3/46.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793076446368 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.6 мс | lag loop p99/max=1.1/1.8 мс
```

Представлено версией кода: 80591e6; python 3.12.3
