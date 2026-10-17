# Состояние сервера записи

Время (UTC): 2026-10-17 17:01:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 days, 9 hours, 37 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         870         492           2         830        1035
Swap:           2047         233        1814
```
- нагрузка CPU (1/5/15 мин): 0.24 / 0.27 / 0.24

## Данные
- файлов: 5500, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 222 | 29 МБ | 1 |
| bn_book | 222 | 3 МБ | 1 |
| bnf_agg | 222 | 44 МБ | 1 |
| bnf_book | 118 | 557 МБ | 371562 |
| bnf_depth5 | 118 | 41 МБ | 371638 |
| bnf_liq | 194 | 134 КБ | 208 |
| bs_trade | 118 | 1 МБ | 371558 |
| by_book1 | 222 | 93 МБ | 1 |
| by_liq | 196 | 107 КБ | 325 |
| by_trade | 222 | 29 МБ | 1 |
| bys_book1 | 106 | 37 МБ | 1 |
| bys_trade | 106 | 15 МБ | 1 |
| cb_ticker | 222 | 27 МБ | 1 |
| clock | 222 | 170 КБ | 6 |
| clock_pm | 222 | 170 КБ | 33 |
| events | 210 | 68 КБ | 2841 |
| events_pm | 222 | 81 КБ | 61 |
| health_cex | 222 | 2 МБ | 6 |
| health_feeds | 222 | 7 МБ | 6 |
| health_pm | 222 | 2 МБ | 7 |
| kr_trade | 118 | 3 МБ | 371558 |
| ok_trade | 221 | 39 МБ | 1 |
| pm_depth | 222 | 44 МБ | 1 |
| pm_rtt | 222 | 1 МБ | 3 |
| pm_top | 222 | 89 МБ | 1 |
| pm_trades | 222 | 65 МБ | 1 |
| rtds | 222 | 14 МБ | 1 |
| windows | 221 | 458 КБ | 304 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 43, всего 291
- Polymarket CLOB: TCP 5, TLS 45, всего 84
- Polymarket gamma: TCP 5, TLS 46, всего 58

## Последние строки журнала записи
```
17:00:19 [pm] T-280.1s Up 0.55/0.56 Down 0.44/0.45 ptb=81146.6 | CLOB 3400 сообщ., задержка p50/p90=47.5/63.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792256419878 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.9/2.2 мс
17:00:21 [cex] Binance 133 сд. задержка p50/p90=145.0/146.5 мс | Coinbase 64 задержка p50=80.3 мс | смещение часов +21.1 мс | lag loop p99/max=2.1/2.2 мс
17:00:21 [cex] binance_futures 159 сд. p50=148.4 мс | bybit 94 сд. p50=115.9 мс | bybit_book 191 сд. p50=113.0 мс | bybit_spot 210 сд. p50=115.3 мс | bybit_spot_book 133 сд. p50=112.9 мс | okx 106 сд. p50=155.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:00:29 [pm] T-270.1s Up 0.54/0.55 Down 0.45/0.46 ptb=81146.6 | CLOB 4946 сообщ., задержка p50/p90=82.6/151.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792256429879 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.8/1.9 мс
17:00:31 [cex] Binance 65 сд. задержка p50/p90=144.9/145.9 мс | Coinbase 36 задержка p50=77.7 мс | смещение часов +21.1 мс | lag loop p99/max=2.1/2.2 мс
17:00:31 [cex] binance_futures 71 сд. p50=295.1 мс | bybit 5 сд. p50=114.7 мс | bybit_book 139 сд. p50=113.0 мс | bybit_spot 12 сд. p50=115.0 мс | bybit_spot_book 45 сд. p50=112.9 мс | okx 15 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:00:39 [pm] T-260.1s Up 0.50/0.51 Down 0.49/0.50 ptb=81146.6 | CLOB 3579 сообщ., задержка p50/p90=45.0/56.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792256439881 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.9/2.1 мс
17:00:41 [cex] Binance 129 сд. задержка p50/p90=145.1/147.7 мс | Coinbase 50 задержка p50=79.8 мс | смещение часов +21.1 мс | lag loop p99/max=2.0/2.2 мс
17:00:41 [cex] binance_futures 96 сд. p50=182.7 мс | bybit 106 сд. p50=115.7 мс | bybit_book 184 сд. p50=113.0 мс | bybit_spot 219 сд. p50=115.3 мс | bybit_spot_book 104 сд. p50=112.9 мс | okx 82 сд. p50=154.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:00:49 [pm] T-250.1s Up 0.42/0.43 Down 0.57/0.58 ptb=81146.6 | CLOB 3883 сообщ., задержка p50/p90=42.3/45.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792256449883 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.9/2.1 мс
17:00:51 [cex] Binance 112 сд. задержка p50/p90=144.9/146.0 мс | Coinbase 60 задержка p50=78.1 мс | смещение часов +21.1 мс | lag loop p99/max=2.0/2.0 мс
17:00:51 [cex] binance_futures 74 сд. p50=282.4 мс | bybit 10 сд. p50=114.9 мс | bybit_book 176 сд. p50=113.1 мс | bybit_spot 136 сд. p50=115.7 мс | bybit_spot_book 95 сд. p50=112.9 мс | okx 116 сд. p50=155.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
17:00:59 [pm] T-240.1s Up 0.35/0.36 Down 0.64/0.65 ptb=81146.6 | CLOB 4236 сообщ., задержка p50/p90=46.4/75.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792256459884 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=1.8/2.1 мс
17:01:01 [cex] Binance 241 сд. задержка p50/p90=145.1/148.2 мс | Coinbase 73 задержка p50=78.8 мс | смещение часов +22.4 мс | lag loop p99/max=2.3/15.8 мс
17:01:01 [cex] binance_futures 150 сд. p50=154.3 мс | bybit 131 сд. p50=116.3 мс | bybit_book 211 сд. p50=113.1 мс | bybit_spot 167 сд. p50=115.8 мс | bybit_spot_book 119 сд. p50=113.0 мс | okx 85 сд. p50=157.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 8083be6; python 3.12.3
