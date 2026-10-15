# Состояние сервера записи

Время (UTC): 2026-10-15 22:43:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 15 hours, 19 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         694         323           2        1137        1211
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.14 / 0.17 / 0.12

## Данные
- файлов: 4486, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 179 | 25 МБ | 1 |
| bn_book | 179 | 2 МБ | 60 |
| bnf_agg | 179 | 38 МБ | 1 |
| bnf_book | 118 | 557 МБ | 219292 |
| bnf_depth5 | 118 | 41 МБ | 219368 |
| bnf_liq | 161 | 112 КБ | 1016 |
| bs_trade | 118 | 1 МБ | 219288 |
| by_book1 | 179 | 80 МБ | 1 |
| by_liq | 159 | 93 КБ | 1163 |
| by_trade | 179 | 25 МБ | 1 |
| bys_book1 | 63 | 25 МБ | 1 |
| bys_trade | 63 | 11 МБ | 5 |
| cb_ticker | 179 | 23 МБ | 1 |
| clock | 179 | 139 КБ | 60 |
| clock_pm | 179 | 139 КБ | 58 |
| events | 168 | 54 КБ | 407 |
| events_pm | 179 | 64 КБ | 129 |
| health_cex | 179 | 2 МБ | 5 |
| health_feeds | 179 | 6 МБ | 5 |
| health_pm | 179 | 2 МБ | 2 |
| kr_trade | 118 | 3 МБ | 219288 |
| ok_trade | 178 | 34 МБ | 1 |
| pm_depth | 179 | 36 МБ | -0 |
| pm_rtt | 179 | 1 МБ | 4 |
| pm_top | 179 | 74 МБ | -0 |
| pm_trades | 179 | 53 МБ | -0 |
| rtds | 179 | 12 МБ | -0 |
| windows | 179 | 370 КБ | 193 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 48, всего 296
- Polymarket CLOB: TCP 6, TLS 40, всего 83
- Polymarket gamma: TCP 6, TLS 73, всего 84

## Последние строки журнала записи
```
22:42:32 [cex] Binance 18 сд. задержка p50/p90=143.3/144.2 мс | Coinbase 76 задержка p50=79.5 мс | смещение часов +20.1 мс | lag loop p99/max=2.2/2.2 мс
22:42:32 [cex] binance_futures 64 сд. p50=143.9 мс | bybit 39 сд. p50=112.6 мс | bybit_book 171 сд. p50=110.5 мс | bybit_spot 34 сд. p50=112.9 мс | bybit_spot_book 58 сд. p50=110.5 мс | okx 33 сд. p50=158.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:42:36 [pm] T-143.7s Up 0.86/0.87 Down 0.13/0.14 ptb=82388.5 | CLOB 3672 сообщ., задержка p50/p90=40.5/41.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792104156288 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=1.7/1.9 мс
22:42:42 [cex] Binance 18 сд. задержка p50/p90=143.3/143.3 мс | Coinbase 41 задержка p50=80.2 мс | смещение часов +20.1 мс | lag loop p99/max=2.2/2.2 мс
22:42:42 [cex] binance_futures 58 сд. p50=143.9 мс | bybit 96 сд. p50=112.6 мс | bybit_book 137 сд. p50=110.4 мс | bybit_spot 43 сд. p50=113.4 мс | bybit_spot_book 56 сд. p50=110.3 мс | okx 63 сд. p50=158.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:42:46 [pm] T-133.7s Up 0.75/0.76 Down 0.24/0.25 ptb=82388.5 | CLOB 6251 сообщ., задержка p50/p90=41.6/47.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792104166290 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=1.6/1.7 мс
22:42:52 [cex] Binance 146 сд. задержка p50/p90=144.4/145.3 мс | Coinbase 66 задержка p50=81.3 мс | смещение часов +20.1 мс | lag loop p99/max=2.1/2.1 мс
22:42:52 [cex] binance_futures 168 сд. p50=145.2 мс | bybit 155 сд. p50=114.0 мс | bybit_book 135 сд. p50=110.4 мс | bybit_spot 164 сд. p50=115.9 мс | bybit_spot_book 68 сд. p50=110.3 мс | okx 100 сд. p50=158.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:42:56 [pm] T-123.7s Up 0.88/0.90 Down 0.10/0.12 ptb=82388.5 | CLOB 6358 сообщ., задержка p50/p90=43.7/65.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792104176292 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.3 мс | lag loop p99/max=1.8/2.0 мс
22:43:02 [cex] Binance 21 сд. задержка p50/p90=143.8/144.3 мс | Coinbase 40 задержка p50=79.6 мс | смещение часов +20.1 мс | lag loop p99/max=2.0/2.3 мс
22:43:02 [cex] binance_futures 316 сд. p50=143.9 мс | bybit 90 сд. p50=112.6 мс | bybit_book 237 сд. p50=110.4 мс | bybit_spot 117 сд. p50=112.7 мс | bybit_spot_book 139 сд. p50=110.4 мс | okx 150 сд. p50=158.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:43:06 [pm] T-113.7s Up 0.87/0.88 Down 0.12/0.13 ptb=82388.5 | CLOB 8413 сообщ., задержка p50/p90=40.7/42.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792104186293 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.1/4.9 мс
22:43:12 [cex] Binance 16 сд. задержка p50/p90=143.7/144.7 мс | Coinbase 41 задержка p50=79.7 мс | смещение часов +20.1 мс | lag loop p99/max=2.1/2.1 мс
22:43:12 [cex] binance_futures 20 сд. p50=292.2 мс | bybit 28 сд. p50=112.7 мс | bybit_book 201 сд. p50=110.4 мс | bybit_spot 5 сд. p50=112.9 мс | bybit_spot_book 119 сд. p50=110.4 мс | okx 66 сд. p50=158.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
22:43:16 [pm] T-103.7s Up 0.92/0.93 Down 0.07/0.08 ptb=82388.5 | CLOB 4627 сообщ., задержка p50/p90=40.7/42.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792104196294 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.8/2.0 мс
```

Представлено версией кода: ec1316a; python 3.12.3
