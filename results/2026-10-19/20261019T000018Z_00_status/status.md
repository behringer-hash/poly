# Состояние сервера записи

Время (UTC): 2026-10-19 00:00:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 16 hours, 36 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         535        1201           1         339        1370
Swap:           2047         254        1793
```
- нагрузка CPU (1/5/15 мин): 0.59 / 0.22 / 0.17

## Данные
- файлов: 6232, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 253 | 32 МБ | 1 |
| bn_book | 253 | 3 МБ | 1 |
| bnf_agg | 253 | 49 МБ | 1 |
| bnf_book | 118 | 557 МБ | 483112 |
| bnf_depth5 | 118 | 41 МБ | 483188 |
| bnf_liq | 218 | 145 КБ | 1789 |
| bs_trade | 118 | 1 МБ | 483108 |
| by_book1 | 253 | 102 МБ | 1 |
| by_liq | 225 | 119 КБ | 1311 |
| by_trade | 253 | 32 МБ | 1 |
| bys_book1 | 137 | 45 МБ | 1 |
| bys_trade | 137 | 18 МБ | 1 |
| cb_ticker | 253 | 30 МБ | 1 |
| clock | 252 | 196 КБ | 21 |
| clock_pm | 252 | 196 КБ | 42 |
| events | 241 | 78 КБ | 566 |
| events_pm | 252 | 92 КБ | 557 |
| health_cex | 253 | 3 МБ | 3 |
| health_feeds | 253 | 8 МБ | 3 |
| health_pm | 253 | 3 МБ | 10 |
| kr_trade | 118 | 3 МБ | 483108 |
| ok_trade | 252 | 42 МБ | 1 |
| pm_depth | 253 | 50 МБ | 2 |
| pm_rtt | 253 | 2 МБ | 2 |
| pm_top | 253 | 101 МБ | 2 |
| pm_trades | 253 | 73 МБ | 2 |
| rtds | 253 | 16 МБ | 2 |
| windows | 252 | 522 КБ | 254 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 40, всего 288
- Polymarket CLOB: TCP 6, TLS 49, всего 88
- Polymarket gamma: TCP 5, TLS 47, всего 57

## Последние строки журнала записи
```
23:59:34 [cex] binance_futures 210 сд. p50=145.3 мс | bybit 593 сд. p50=123.1 мс | bybit_book 162 сд. p50=110.6 мс | bybit_spot 152 сд. p50=113.6 мс | bybit_spot_book 79 сд. p50=110.1 мс | okx 172 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:59:36 [pm] T- 23.1s Up 0.99/n/a Down n/a/0.01 ptb=81934.6 | CLOB 691 сообщ., задержка p50/p90=58.5/60.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792367976899 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=2.1/2.2 мс
23:59:44 [cex] Binance 341 сд. задержка p50/p90=142.7/143.4 мс | Coinbase 43 задержка p50=76.9 мс | смещение часов +18.6 мс | lag loop p99/max=2.0/2.2 мс
23:59:44 [cex] binance_futures 137 сд. p50=144.2 мс | bybit 195 сд. p50=112.5 мс | bybit_book 146 сд. p50=110.6 мс | bybit_spot 208 сд. p50=113.0 мс | bybit_spot_book 104 сд. p50=110.0 мс | okx 129 сд. p50=152.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:59:45 [pm] окно btc-updown-5m-1792368000 (2026-10-19 00:00:00 UTC): Bitcoin Up or Down - October 18, 8:00PM-8:05PM ET
23:59:46 [pm] T- 13.1s Up 1.00/n/a Down n/a/0.00 ptb=81934.6 | CLOB 892 сообщ., задержка p50/p90=57.2/59.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792367986901 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=2.2/12.5 мс
23:59:54 [cex] Binance 386 сд. задержка p50/p90=142.6/143.4 мс | Coinbase 39 задержка p50=75.5 мс | смещение часов +18.6 мс | lag loop p99/max=2.2/2.3 мс
23:59:54 [cex] binance_futures 166 сд. p50=144.2 мс | bybit 95 сд. p50=112.4 мс | bybit_book 109 сд. p50=110.7 мс | bybit_spot 139 сд. p50=112.8 мс | bybit_spot_book 64 сд. p50=110.0 мс | okx 116 сд. p50=153.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:59:56 [pm] T-  3.1s Up 1.00/n/a Down n/a/0.00 ptb=81934.6 | CLOB 2160 сообщ., задержка p50/p90=36.9/57.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792367996902 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=2.0/2.0 мс
00:00:04 [cex] Binance 190 сд. задержка p50/p90=141.9/143.7 мс | Coinbase 100 задержка p50=80.2 мс | смещение часов +17.4 мс | lag loop p99/max=3.5/5.6 мс
00:00:04 [cex] binance_futures 168 сд. p50=149.5 мс | bybit 184 сд. p50=111.5 мс | bybit_book 280 сд. p50=109.7 мс | bybit_spot 200 сд. p50=111.8 мс | bybit_spot_book 213 сд. p50=109.2 мс | okx 157 сд. p50=151.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:00:06 [pm] T-293.1s Up 0.25/0.26 Down 0.74/0.75 ptb=82024.9 | CLOB 8062 сообщ., задержка p50/p90=37.3/39.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792368006904 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=13.9/17.5 мс
00:00:14 [cex] Binance 272 сд. задержка p50/p90=141.4/142.2 мс | Coinbase 54 задержка p50=75.1 мс | смещение часов +17.4 мс | lag loop p99/max=2.6/2.8 мс
00:00:14 [cex] binance_futures 156 сд. p50=178.4 мс | bybit 141 сд. p50=110.9 мс | bybit_book 260 сд. p50=109.5 мс | bybit_spot 110 сд. p50=112.5 мс | bybit_spot_book 98 сд. p50=108.9 мс | okx 52 сд. p50=151.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:00:16 [pm] T-283.1s Up 0.30/0.31 Down 0.69/0.70 ptb=82024.9 | CLOB 6176 сообщ., задержка p50/p90=36.6/38.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792368016905 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=2.0/2.5 мс
```

Представлено версией кода: 88f2465; python 3.12.3
