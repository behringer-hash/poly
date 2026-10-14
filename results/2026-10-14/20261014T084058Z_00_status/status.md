# Состояние сервера записи

Время (UTC): 2026-10-14 08:40:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 hour, 17 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         578         478           2        1040        1327
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.20 / 0.15 / 0.17

## Данные
- файлов: 3578, всего 925 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 141 | 18 МБ | 0 |
| bn_book | 141 | 2 МБ | 0 |
| bnf_agg | 141 | 28 МБ | 0 |
| bnf_book | 118 | 557 МБ | 82352 |
| bnf_depth5 | 118 | 41 МБ | 82428 |
| bnf_liq | 124 | 74 КБ | 106 |
| bs_trade | 118 | 1 МБ | 82348 |
| by_book1 | 141 | 58 МБ | 0 |
| by_liq | 122 | 66 КБ | 244 |
| by_trade | 141 | 19 МБ | 0 |
| bys_book1 | 25 | 10 МБ | 0 |
| bys_trade | 25 | 5 МБ | 2 |
| cb_ticker | 141 | 16 МБ | 0 |
| clock | 141 | 109 КБ | 49 |
| clock_pm | 141 | 109 КБ | 49 |
| events | 133 | 45 КБ | 759 |
| events_pm | 140 | 52 КБ | 2790 |
| health_cex | 141 | 1 МБ | 2 |
| health_feeds | 141 | 5 МБ | 2 |
| health_pm | 141 | 1 МБ | 1 |
| kr_trade | 118 | 3 МБ | 82348 |
| ok_trade | 140 | 24 МБ | 0 |
| pm_depth | 141 | 28 МБ | 1 |
| pm_rtt | 141 | 956 КБ | 5 |
| pm_top | 141 | 57 МБ | 1 |
| pm_trades | 141 | 41 МБ | 1 |
| rtds | 141 | 9 МБ | 1 |
| windows | 141 | 292 КБ | 23 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 39, всего 301
- Polymarket CLOB: TCP 5, TLS 36, всего 84
- Polymarket gamma: TCP 5, TLS 37, всего 51

## Последние строки журнала записи
```
08:40:14 [cex] Binance 72 сд. задержка p50/p90=145.1/145.4 мс | Coinbase 46 задержка p50=78.1 мс | смещение часов +20.6 мс | lag loop p99/max=2.0/2.1 мс
08:40:14 [cex] binance_futures 117 сд. p50=145.9 мс | bybit 187 сд. p50=114.1 мс | bybit_book 225 сд. p50=112.3 мс | bybit_spot 141 сд. p50=115.4 мс | bybit_spot_book 80 сд. p50=111.9 мс | okx 171 сд. p50=150.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:40:16 [pm] T-283.2s Up 0.27/0.28 Down 0.72/0.73 ptb=83627.2 | CLOB 9532 сообщ., задержка p50/p90=39.8/41.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791967216770 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=1.6/2.1 мс
08:40:24 [cex] Binance 252 сд. задержка p50/p90=145.6/147.9 мс | Coinbase 77 задержка p50=79.3 мс | смещение часов +20.6 мс | lag loop p99/max=2.1/2.2 мс
08:40:24 [cex] binance_futures 395 сд. p50=147.7 мс | bybit 414 сд. p50=118.8 мс | bybit_book 331 сд. p50=112.4 мс | bybit_spot 464 сд. p50=115.5 мс | bybit_spot_book 188 сд. p50=112.1 мс | okx 541 сд. p50=154.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:40:26 [pm] T-273.2s Up 0.44/0.45 Down 0.55/0.56 ptb=83627.2 | CLOB 11372 сообщ., задержка p50/p90=39.7/40.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791967226771 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=1.2/1.2 мс
08:40:34 [cex] Binance 56 сд. задержка p50/p90=145.1/146.1 мс | Coinbase 19 задержка p50=77.0 мс | смещение часов +20.6 мс | lag loop p99/max=2.1/2.4 мс
08:40:34 [cex] binance_futures 59 сд. p50=281.7 мс | bybit 87 сд. p50=114.3 мс | bybit_book 256 сд. p50=112.3 мс | bybit_spot 22 сд. p50=115.0 мс | bybit_spot_book 61 сд. p50=112.0 мс | okx 50 сд. p50=151.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:40:36 [pm] T-263.2s Up 0.45/0.46 Down 0.54/0.55 ptb=83627.2 | CLOB 6664 сообщ., задержка p50/p90=39.8/41.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791967236773 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=1.9/1.9 мс
08:40:44 [cex] Binance 16 сд. задержка p50/p90=145.0/146.0 мс | Coinbase 41 задержка p50=77.9 мс | смещение часов +20.6 мс | lag loop p99/max=2.2/2.2 мс
08:40:44 [cex] binance_futures 40 сд. p50=294.1 мс | bybit 45 сд. p50=114.4 мс | bybit_book 152 сд. p50=112.4 мс | bybit_spot 64 сд. p50=114.7 мс | bybit_spot_book 68 сд. p50=112.1 мс | okx 25 сд. p50=150.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:40:46 [pm] T-253.2s Up 0.44/0.45 Down 0.55/0.56 ptb=83627.2 | CLOB 5925 сообщ., задержка p50/p90=39.7/40.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791967246774 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.7 мс | lag loop p99/max=1.1/1.1 мс
08:40:54 [cex] Binance 29 сд. задержка p50/p90=145.3/145.5 мс | Coinbase 42 задержка p50=77.7 мс | смещение часов +20.6 мс | lag loop p99/max=2.1/2.3 мс
08:40:54 [cex] binance_futures 40 сд. p50=294.1 мс | bybit 57 сд. p50=113.7 мс | bybit_book 137 сд. p50=112.4 мс | bybit_spot 68 сд. p50=114.9 мс | bybit_spot_book 60 сд. p50=112.1 мс | okx 26 сд. p50=150.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:40:56 [pm] T-243.2s Up 0.35/0.36 Down 0.64/0.65 ptb=83627.2 | CLOB 9183 сообщ., задержка p50/p90=39.8/40.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791967256775 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.8 мс | lag loop p99/max=1.1/1.3 мс
```

Представлено версией кода: ec1316a; python 3.12.3
