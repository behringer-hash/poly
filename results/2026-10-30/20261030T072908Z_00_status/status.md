# Состояние сервера записи

Время (UTC): 2026-10-30 07:29:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 2 days, 5 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         641         547           1         900        1264
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.33 / 0.22 / 0.21

## Данные
- файлов: 5833, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 37 МБ | 1 |
| bn_book | 242 | 3 МБ | 3 |
| bnf_agg | 242 | 53 МБ | 1 |
| bnf_book | 91 | 642 МБ | 0 |
| bnf_liq | 211 | 142 КБ | 4753 |
| by_book1 | 242 | 113 МБ | 1 |
| by_liq | 225 | 118 КБ | 851 |
| by_trade | 242 | 35 МБ | 1 |
| bys_book1 | 242 | 84 МБ | 1 |
| bys_trade | 242 | 34 МБ | 1 |
| cb_ticker | 242 | 33 МБ | 1 |
| clock | 242 | 188 КБ | 9 |
| clock_pm | 242 | 188 КБ | 41 |
| events | 226 | 73 КБ | 467 |
| events_pm | 241 | 86 КБ | 344 |
| health_cex | 242 | 3 МБ | 3 |
| health_feeds | 242 | 8 МБ | 3 |
| health_pm | 242 | 3 МБ | 1 |
| ok_trade | 242 | 46 МБ | 1 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 3 |
| pm_top | 242 | 101 МБ | 1 |
| pm_trades | 241 | 72 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 499 КБ | 5 |

Дни с данными: 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 289
- Polymarket CLOB: TCP 5, TLS 39, всего 82
- Polymarket gamma: TCP 3, TLS 36, всего 43

## Последние строки журнала записи
```
07:28:25 [cex] Binance 159 сд. задержка p50/p90=146.4/160.9 мс | Coinbase 57 задержка p50=85.0 мс | смещение часов +20.5 мс | lag loop p99/max=12.0/15.0 мс
07:28:25 [cex] binance_futures 184 сд. p50=154.7 мс | bybit 140 сд. p50=114.7 мс | bybit_book 202 сд. p50=111.8 мс | bybit_spot 248 сд. p50=116.0 мс | bybit_spot_book 104 сд. p50=112.2 мс | okx 265 сд. p50=158.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 11567 сд. p50=144.6 мс
07:28:27 [pm] T- 92.6s Up 0.53/0.55 Down 0.45/0.47 ptb=78340.4 | CLOB 14563 сообщ., задержка p50/p90=41.2/42.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793345307449 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=1.7/2.6 мс
07:28:35 [cex] Binance 119 сд. задержка p50/p90=146.1/146.7 мс | Coinbase 36 задержка p50=84.6 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/2.2 мс
07:28:35 [cex] binance_futures 30 сд. p50=294.0 мс | bybit 12 сд. p50=113.8 мс | bybit_book 87 сд. p50=111.8 мс | bybit_spot 8 сд. p50=114.0 мс | bybit_spot_book 21 сд. p50=112.1 мс | okx 35 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1358 сд. p50=144.5 мс
07:28:37 [pm] T- 82.5s Up 0.38/0.39 Down 0.61/0.62 ptb=78340.4 | CLOB 12218 сообщ., задержка p50/p90=43.7/45.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793345317450 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=1.8/2.1 мс
07:28:45 [cex] Binance 65 сд. задержка p50/p90=145.5/146.6 мс | Coinbase 37 задержка p50=84.4 мс | смещение часов +20.5 мс | lag loop p99/max=1.9/2.1 мс
07:28:45 [cex] binance_futures 34 сд. p50=294.0 мс | bybit 8 сд. p50=113.8 мс | bybit_book 122 сд. p50=111.8 мс | bybit_spot 2 сд. p50=114.5 мс | bybit_spot_book 15 сд. p50=111.9 мс | okx 40 сд. p50=157.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 6145 сд. p50=144.6 мс
07:28:47 [pm] T- 72.5s Up 0.38/0.39 Down 0.61/0.62 ptb=78340.4 | CLOB 10356 сообщ., задержка p50/p90=43.9/76.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793345327452 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=2.1/2.1 мс
07:28:55 [cex] Binance 145 сд. задержка p50/p90=147.7/150.1 мс | Coinbase 86 задержка p50=87.3 мс | смещение часов +20.5 мс | lag loop p99/max=2.1/7.6 мс
07:28:55 [cex] binance_futures 162 сд. p50=151.4 мс | bybit 108 сд. p50=114.7 мс | bybit_book 133 сд. p50=111.9 мс | bybit_spot 222 сд. p50=115.8 мс | bybit_spot_book 76 сд. p50=112.0 мс | okx 162 сд. p50=160.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4378 сд. p50=146.9 мс
07:28:57 [pm] T- 62.5s Up 0.05/0.06 Down 0.94/0.95 ptb=78340.4 | CLOB 11903 сообщ., задержка p50/p90=43.4/44.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793345337453 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=1.8/1.9 мс
07:29:05 [cex] Binance 225 сд. задержка p50/p90=151.5/154.6 мс | Coinbase 69 задержка p50=85.8 мс | смещение часов +21.1 мс | lag loop p99/max=9.0/10.0 мс
07:29:05 [cex] binance_futures 434 сд. p50=151.4 мс | bybit 121 сд. p50=114.6 мс | bybit_book 222 сд. p50=112.3 мс | bybit_spot 182 сд. p50=114.8 мс | bybit_spot_book 120 сд. p50=112.3 мс | okx 192 сд. p50=163.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5139 сд. p50=145.2 мс
07:29:07 [pm] T- 52.5s Up 0.05/0.06 Down 0.94/0.95 ptb=78340.4 | CLOB 5666 сообщ., задержка p50/p90=43.6/45.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793345347454 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.2 мс | lag loop p99/max=1.9/2.1 мс
```

Представлено версией кода: b8783c2; python 3.12.3
