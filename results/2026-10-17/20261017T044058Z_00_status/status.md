# Состояние сервера записи

Время (UTC): 2026-10-17 04:40:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 21 hours, 17 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         852         567           2         772        1053
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.13 / 0.20 / 0.18

## Данные
- файлов: 5200, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 209 | 29 МБ | 1 |
| bn_book | 209 | 3 МБ | 76 |
| bnf_agg | 209 | 44 МБ | 1 |
| bnf_book | 118 | 557 МБ | 327152 |
| bnf_depth5 | 118 | 41 МБ | 327228 |
| bnf_liq | 187 | 128 КБ | 4060 |
| bs_trade | 118 | 1 МБ | 327148 |
| by_book1 | 209 | 91 МБ | 1 |
| by_liq | 187 | 104 КБ | 4502 |
| by_trade | 209 | 28 МБ | 3 |
| bys_book1 | 93 | 36 МБ | 1 |
| bys_trade | 93 | 14 МБ | 7 |
| cb_ticker | 209 | 27 МБ | 1 |
| clock | 209 | 162 КБ | 42 |
| clock_pm | 209 | 162 КБ | 2 |
| events | 198 | 65 КБ | 391 |
| events_pm | 209 | 77 КБ | 330 |
| health_cex | 209 | 2 МБ | 1 |
| health_feeds | 209 | 7 МБ | 1 |
| health_pm | 209 | 2 МБ | 4 |
| kr_trade | 118 | 3 МБ | 327148 |
| ok_trade | 208 | 38 МБ | 1 |
| pm_depth | 209 | 42 МБ | 0 |
| pm_rtt | 209 | 1 МБ | 0 |
| pm_top | 209 | 86 МБ | 0 |
| pm_trades | 209 | 62 МБ | 0 |
| rtds | 209 | 14 МБ | 0 |
| windows | 209 | 432 КБ | 53 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 39, всего 288
- Polymarket CLOB: TCP 5, TLS 41, всего 82
- Polymarket gamma: TCP 5, TLS 39, всего 50

## Последние строки журнала записи
```
04:40:13 [pm] T-286.6s Up 0.17/0.18 Down 0.82/0.83 ptb=81464.5 | CLOB 5297 сообщ., задержка p50/p90=38.0/41.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792212013359 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.7/2.2 мс
04:40:17 [cex] Binance 76 сд. задержка p50/p90=143.2/143.8 мс | Coinbase 27 задержка p50=75.0 мс | смещение часов +19.0 мс | lag loop p99/max=2.2/2.2 мс
04:40:17 [cex] binance_futures 42 сд. p50=292.2 мс | bybit 19 сд. p50=112.0 мс | bybit_book 47 сд. p50=110.7 мс | bybit_spot 2 сд. p50=112.5 мс | bybit_spot_book 14 сд. p50=109.8 мс | okx 6 сд. p50=152.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:40:23 [pm] T-276.6s Up 0.16/0.17 Down 0.83/0.84 ptb=81464.5 | CLOB 2773 сообщ., задержка p50/p90=37.7/39.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792212023360 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.1/2.1 мс
04:40:27 [cex] Binance 77 сд. задержка p50/p90=143.6/144.6 мс | Coinbase 38 задержка p50=75.7 мс | смещение часов +19.0 мс | lag loop p99/max=2.2/2.3 мс
04:40:27 [cex] binance_futures 36 сд. p50=292.9 мс | bybit 2 сд. p50=112.5 мс | bybit_book 18 сд. p50=111.3 мс | bybit_spot 1 сд. p50=113.4 мс | bybit_spot_book 17 сд. p50=110.6 мс | okx 8 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:40:33 [pm] T-266.6s Up 0.16/0.17 Down 0.83/0.84 ptb=81464.5 | CLOB 2339 сообщ., задержка p50/p90=37.6/38.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792212033362 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=2.2/2.4 мс
04:40:37 [cex] Binance 68 сд. задержка p50/p90=143.7/144.6 мс | Coinbase 33 задержка p50=75.7 мс | смещение часов +19.0 мс | lag loop p99/max=2.0/2.2 мс
04:40:37 [cex] binance_futures 35 сд. p50=292.7 мс | bybit 2 сд. p50=112.8 мс | bybit_book 26 сд. p50=111.3 мс | bybit_spot 3 сд. p50=112.5 мс | bybit_spot_book 16 сд. p50=110.7 мс | okx 7 сд. p50=152.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:40:43 [pm] T-256.6s Up 0.16/0.17 Down 0.83/0.84 ptb=81464.5 | CLOB 2479 сообщ., задержка p50/p90=37.5/38.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792212043363 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.7 мс | lag loop p99/max=1.7/1.8 мс
04:40:47 [cex] Binance 73 сд. задержка p50/p90=143.7/144.5 мс | Coinbase 36 задержка p50=75.5 мс | смещение часов +19.0 мс | lag loop p99/max=2.0/2.2 мс
04:40:47 [cex] binance_futures 41 сд. p50=292.8 мс | bybit 2 сд. p50=113.0 мс | bybit_book 27 сд. p50=111.2 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 21 сд. p50=110.5 мс | okx 10 сд. p50=153.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:40:53 [pm] T-246.6s Up 0.18/0.19 Down 0.81/0.82 ptb=81464.5 | CLOB 3157 сообщ., задержка p50/p90=38.0/43.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792212053364 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.7/1.9 мс
04:40:57 [cex] Binance 98 сд. задержка p50/p90=143.7/144.6 мс | Coinbase 43 задержка p50=76.3 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/2.1 мс
04:40:57 [cex] binance_futures 48 сд. p50=292.8 мс | bybit 3 сд. p50=112.5 мс | bybit_book 27 сд. p50=111.2 мс | bybit_spot 1 сд. p50=112.9 мс | bybit_spot_book 30 сд. p50=110.5 мс | okx 12 сд. p50=153.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 8083be6; python 3.12.3
