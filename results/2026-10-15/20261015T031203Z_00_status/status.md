# Состояние сервера записи

Время (UTC): 2026-10-15 03:12:03

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 19 hours, 48 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         606         332           2        1162        1299
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.36 / 0.24 / 0.21

## Данные
- файлов: 4031, всего 979 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 160 | 21 МБ | 1 |
| bn_book | 160 | 2 МБ | 1 |
| bnf_agg | 160 | 32 МБ | 1 |
| bnf_book | 118 | 557 МБ | 149017 |
| bnf_depth5 | 118 | 41 МБ | 149094 |
| bnf_liq | 143 | 95 КБ | 167 |
| bs_trade | 118 | 1 МБ | 149013 |
| by_book1 | 160 | 66 МБ | 1 |
| by_liq | 140 | 80 КБ | 602 |
| by_trade | 160 | 21 МБ | 1 |
| bys_book1 | 44 | 16 МБ | 1 |
| bys_trade | 44 | 7 МБ | 1 |
| cb_ticker | 160 | 19 МБ | 1 |
| clock | 160 | 123 КБ | 1 |
| clock_pm | 160 | 123 КБ | 62 |
| events | 150 | 49 КБ | 2322 |
| events_pm | 159 | 57 КБ | 1210 |
| health_cex | 160 | 2 МБ | 1 |
| health_feeds | 160 | 6 МБ | 1 |
| health_pm | 160 | 2 МБ | 6 |
| kr_trade | 118 | 3 МБ | 149013 |
| ok_trade | 159 | 29 МБ | 1 |
| pm_depth | 160 | 31 МБ | 2 |
| pm_rtt | 160 | 1 МБ | 2 |
| pm_top | 160 | 64 МБ | 2 |
| pm_trades | 160 | 47 МБ | 2 |
| rtds | 160 | 10 МБ | 2 |
| windows | 160 | 328 КБ | 210 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 36, всего 284
- Polymarket CLOB: TCP 5, TLS 37, всего 79
- Polymarket gamma: TCP 5, TLS 41, всего 53

## Последние строки журнала записи
```
03:11:16 [pm] T-223.7s Up 0.26/0.27 Down 0.73/0.74 ptb=81204.5 | CLOB 7564 сообщ., задержка p50/p90=39.7/48.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792033876305 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=1.8/1.9 мс
03:11:23 [cex] Binance 115 сд. задержка p50/p90=143.5/144.6 мс | Coinbase 66 задержка p50=82.3 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.2 мс
03:11:23 [cex] binance_futures 155 сд. p50=144.5 мс | bybit 148 сд. p50=113.2 мс | bybit_book 260 сд. p50=110.6 мс | bybit_spot 237 сд. p50=112.9 мс | bybit_spot_book 204 сд. p50=110.4 мс | okx 147 сд. p50=152.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:11:26 [pm] T-213.7s Up 0.22/0.23 Down 0.77/0.78 ptb=81204.5 | CLOB 9688 сообщ., задержка p50/p90=40.3/48.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792033886306 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=1.1/1.1 мс
03:11:33 [cex] Binance 165 сд. задержка p50/p90=143.7/144.7 мс | Coinbase 70 задержка p50=81.9 мс | смещение часов +19.2 мс | lag loop p99/max=2.1/2.1 мс
03:11:33 [cex] binance_futures 275 сд. p50=144.4 мс | bybit 143 сд. p50=113.1 мс | bybit_book 244 сд. p50=110.6 мс | bybit_spot 299 сд. p50=112.9 мс | bybit_spot_book 219 сд. p50=110.4 мс | okx 242 сд. p50=152.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:11:36 [pm] T-203.7s Up 0.23/0.25 Down 0.75/0.77 ptb=81204.5 | CLOB 6806 сообщ., задержка p50/p90=40.2/47.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792033896307 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=1.9/2.1 мс
03:11:43 [cex] Binance 120 сд. задержка p50/p90=143.8/144.5 мс | Coinbase 56 задержка p50=81.6 мс | смещение часов +19.2 мс | lag loop p99/max=2.2/2.2 мс
03:11:43 [cex] binance_futures 122 сд. p50=145.8 мс | bybit 90 сд. p50=113.0 мс | bybit_book 237 сд. p50=110.6 мс | bybit_spot 149 сд. p50=112.9 мс | bybit_spot_book 191 сд. p50=110.4 мс | okx 109 сд. p50=152.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:11:46 [pm] T-193.7s Up 0.19/0.20 Down 0.80/0.81 ptb=81204.5 | CLOB 6970 сообщ., задержка p50/p90=39.3/43.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792033906308 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.6 мс | lag loop p99/max=1.9/2.0 мс
03:11:53 [cex] Binance 69 сд. задержка p50/p90=143.9/144.9 мс | Coinbase 51 задержка p50=82.0 мс | смещение часов +19.2 мс | lag loop p99/max=1.9/2.1 мс
03:11:53 [cex] binance_futures 154 сд. p50=144.3 мс | bybit 149 сд. p50=113.3 мс | bybit_book 260 сд. p50=110.6 мс | bybit_spot 236 сд. p50=112.9 мс | bybit_spot_book 172 сд. p50=110.4 мс | okx 125 сд. p50=152.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
03:11:56 [pm] T-183.7s Up 0.16/0.17 Down 0.83/0.84 ptb=81204.5 | CLOB 10021 сообщ., задержка p50/p90=39.3/44.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792033916309 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=1.2/1.2 мс
03:12:03 [cex] Binance 100 сд. задержка p50/p90=143.4/146.9 мс | Coinbase 42 задержка p50=81.6 мс | смещение часов +21.3 мс | lag loop p99/max=3.2/7.5 мс
03:12:03 [cex] binance_futures 169 сд. p50=144.5 мс | bybit 76 сд. p50=113.1 мс | bybit_book 175 сд. p50=110.7 мс | bybit_spot 316 сд. p50=112.9 мс | bybit_spot_book 168 сд. p50=110.5 мс | okx 115 сд. p50=152.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: ec1316a; python 3.12.3
