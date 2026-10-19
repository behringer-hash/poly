# Состояние сервера записи

Время (UTC): 2026-10-19 07:12:21

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 23 hours, 48 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         609         702           1         766        1296
Swap:           2047         252        1795
```
- нагрузка CPU (1/5/15 мин): 0.48 / 0.30 / 0.22

## Данные
- файлов: 6406, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 260 | 33 МБ | 1 |
| bn_book | 260 | 3 МБ | 15 |
| bnf_agg | 260 | 51 МБ | 1 |
| bnf_book | 118 | 557 МБ | 509035 |
| bnf_depth5 | 118 | 41 МБ | 509112 |
| bnf_liq | 226 | 148 КБ | 629 |
| bs_trade | 118 | 1 МБ | 509031 |
| by_book1 | 260 | 105 МБ | 1 |
| by_liq | 232 | 119 КБ | 2117 |
| by_trade | 260 | 33 МБ | 1 |
| bys_book1 | 144 | 47 МБ | 1 |
| bys_trade | 144 | 19 МБ | 7 |
| cb_ticker | 260 | 31 МБ | 1 |
| clock | 260 | 200 КБ | 7 |
| clock_pm | 260 | 200 КБ | 28 |
| events | 249 | 79 КБ | 18 |
| events_pm | 260 | 94 КБ | 490 |
| health_cex | 260 | 3 МБ | 3 |
| health_feeds | 260 | 9 МБ | 3 |
| health_pm | 260 | 3 МБ | 9 |
| kr_trade | 118 | 3 МБ | 509031 |
| ok_trade | 259 | 44 МБ | 1 |
| pm_depth | 260 | 51 МБ | 1 |
| pm_rtt | 260 | 2 МБ | 3 |
| pm_top | 260 | 105 МБ | 1 |
| pm_trades | 260 | 75 МБ | 1 |
| rtds | 260 | 16 МБ | 1 |
| windows | 260 | 535 КБ | 138 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 39, всего 288
- Polymarket CLOB: TCP 5, TLS 42, всего 87
- Polymarket gamma: TCP 5, TLS 41, всего 54

## Последние строки журнала записи
```
07:11:40 [pm] T-199.5s Up 0.11/0.12 Down 0.88/0.89 ptb=82792.7 | CLOB 5468 сообщ., задержка p50/p90=38.6/42.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792393900548 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=2.3/3.4 мс
07:11:47 [cex] Binance 14 сд. задержка p50/p90=144.0/145.0 мс | Coinbase 2 задержка p50=75.2 мс | смещение часов +19.1 мс | lag loop p99/max=2.0/2.2 мс
07:11:47 [cex] binance_futures 38 сд. p50=292.6 мс | bybit 9 сд. p50=111.7 мс | bybit_book 63 сд. p50=110.1 мс | bybit_spot 6 сд. p50=113.0 мс | bybit_spot_book 125 сд. p50=111.1 мс | okx 28 сд. p50=157.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:11:50 [pm] T-189.5s Up 0.16/0.17 Down 0.83/0.84 ptb=82792.7 | CLOB 4798 сообщ., задержка p50/p90=39.5/75.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792393910549 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.4 мс | lag loop p99/max=2.0/2.5 мс
07:11:57 [cex] Binance 134 сд. задержка p50/p90=144.8/146.0 мс | Coinbase 43 задержка p50=76.7 мс | смещение часов +19.1 мс | lag loop p99/max=2.2/2.4 мс
07:11:57 [cex] binance_futures 112 сд. p50=145.1 мс | bybit 204 сд. p50=112.2 мс | bybit_book 136 сд. p50=110.2 мс | bybit_spot 287 сд. p50=113.6 мс | bybit_spot_book 136 сд. p50=111.1 мс | okx 133 сд. p50=158.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:11:59 [cex] binance_liq: TimeoutError() (wss://fstream.binance.com/market/stream?streams=btcusdt@forceOrder)
07:12:00 [pm] T-179.4s Up 0.25/0.26 Down 0.74/0.75 ptb=82792.7 | CLOB 7798 сообщ., задержка p50/p90=42.9/44.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792393920551 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.4 мс | lag loop p99/max=1.5/5.0 мс
07:12:02 [cex] binance_liq подключён: wss://fstream.binance.com/market/stream?streams=btcusdt@forceOrder
07:12:07 [cex] Binance 82 сд. задержка p50/p90=144.6/145.7 мс | Coinbase 18 задержка p50=76.0 мс | смещение часов +19.1 мс | lag loop p99/max=7.4/33.1 мс
07:12:07 [cex] binance_futures 69 сд. p50=146.0 мс | bybit 52 сд. p50=111.7 мс | bybit_book 178 сд. p50=110.1 мс | bybit_spot 140 сд. p50=113.4 мс | bybit_spot_book 107 сд. p50=111.1 мс | okx 46 сд. p50=157.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:12:10 [pm] T-169.4s Up 0.17/0.18 Down 0.82/0.83 ptb=82792.7 | CLOB 7566 сообщ., задержка p50/p90=44.9/64.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792393930552 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.4 мс | lag loop p99/max=7.6/16.8 мс
07:12:17 [cex] Binance 24 сд. задержка p50/p90=144.0/144.2 мс | Coinbase 47 задержка p50=85.7 мс | смещение часов +17.8 мс | lag loop p99/max=2.1/2.2 мс
07:12:17 [cex] binance_futures 65 сд. p50=144.3 мс | bybit 97 сд. p50=111.7 мс | bybit_book 129 сд. p50=110.0 мс | bybit_spot 68 сд. p50=113.7 мс | bybit_spot_book 107 сд. p50=110.9 мс | okx 121 сд. p50=157.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
07:12:20 [pm] T-159.4s Up 0.16/0.17 Down 0.83/0.84 ptb=82792.7 | CLOB 5894 сообщ., задержка p50/p90=43.4/46.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792393940554 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.4 мс | lag loop p99/max=1.8/1.9 мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
