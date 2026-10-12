# Состояние сервера записи

Время (UTC): 2026-10-12 13:07:25

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 5 hours, 43 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         777         809           2         527        1128
Swap:           2047         105        1942
```
- нагрузка CPU (1/5/15 мин): 0.14 / 0.50 / 0.53

## Данные
- файлов: 2512, всего 644 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 98 | 11 МБ | 1 |
| bn_book | 98 | 905 КБ | 1 |
| bnf_agg | 98 | 16 МБ | 1 |
| bnf_book | 98 | 416 МБ | 0 |
| bnf_depth5 | 98 | 33 МБ | 1 |
| bnf_liq | 85 | 48 КБ | 212 |
| bs_trade | 98 | 1 МБ | 1 |
| by_book1 | 98 | 33 МБ | 1 |
| by_liq | 81 | 42 КБ | 214 |
| by_trade | 98 | 10 МБ | 1 |
| cb_ticker | 98 | 10 МБ | 1 |
| clock | 98 | 74 КБ | 55 |
| clock_pm | 98 | 74 КБ | 7 |
| events | 92 | 31 КБ | 5632 |
| events_pm | 98 | 37 КБ | 262 |
| health_cex | 98 | 1023 КБ | 1 |
| health_feeds | 98 | 4 МБ | 1 |
| health_pm | 98 | 1 МБ | 1 |
| kr_trade | 98 | 2 МБ | 1 |
| ok_trade | 98 | 14 МБ | 1 |
| pm_depth | 98 | 19 МБ | 1 |
| pm_rtt | 98 | 648 КБ | 3 |
| pm_top | 98 | 37 МБ | 1 |
| pm_trades | 98 | 27 МБ | 1 |
| rtds | 98 | 6 МБ | 1 |
| windows | 98 | 199 КБ | 170 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 55, всего 305
- Polymarket CLOB: TCP 7, TLS 61, всего 100
- Polymarket gamma: TCP 5, TLS 64, всего 76

## Последние строки журнала записи
```
13:06:42 [pm] T-197.5s Up 0.82/0.83 Down 0.17/0.18 ptb=82621.6 | CLOB 7669 сообщ., задержка p50/p90=86.4/217.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791810402452 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=1.9/2.2 мс
13:06:42 [cex] Binance 97 сд. задержка p50/p90=147.5/153.0 мс | Coinbase 40 задержка p50=84.8 мс | смещение часов +22.2 мс | lag loop p99/max=2.9/3.7 мс
13:06:42 [cex] binance_futures 168 сд. p50=151.2 мс | bybit 219 сд. p50=117.0 мс | okx 178 сд. p50=157.3 мс | binance_futures_book 4530 сд. p50=150.4 мс | binance_futures_depth 95 сд. p50=146.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 222 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 14 сд. p50=66.7 мс | bitstamp 2 сд. p50=57.1 мс
13:06:52 [pm] T-187.5s Up 0.85/0.86 Down 0.14/0.15 ptb=82621.6 | CLOB 6422 сообщ., задержка p50/p90=61.1/187.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791810412453 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=1.4/1.9 мс
13:06:52 [cex] Binance 46 сд. задержка p50/p90=147.4/151.1 мс | Coinbase 39 задержка p50=83.8 мс | смещение часов +22.2 мс | lag loop p99/max=2.0/2.2 мс
13:06:52 [cex] binance_futures 110 сд. p50=183.9 мс | bybit 183 сд. p50=116.1 мс | okx 147 сд. p50=157.1 мс | binance_futures_book 4932 сд. p50=149.6 мс | binance_futures_depth 96 сд. p50=146.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 188 сд. p50=114.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 31 сд. p50=46.2 мс | bitstamp 3 сд. p50=48.7 мс
13:07:02 [pm] T-177.5s Up 0.85/0.86 Down 0.14/0.15 ptb=82621.6 | CLOB 5221 сообщ., задержка p50/p90=40.4/99.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791810422454 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=1.7/2.1 мс
13:07:02 [cex] Binance 43 сд. задержка p50/p90=146.4/147.4 мс | Coinbase 21 задержка p50=84.8 мс | смещение часов +22.2 мс | lag loop p99/max=2.1/13.2 мс
13:07:02 [cex] binance_futures 92 сд. p50=213.4 мс | bybit 132 сд. p50=115.6 мс | okx 68 сд. p50=156.1 мс | binance_futures_book 2680 сд. p50=147.9 мс | binance_futures_depth 94 сд. p50=146.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 203 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 18 сд. p50=49.8 мс | bitstamp 1 сд. p50=50.2 мс
13:07:12 [pm] T-167.5s Up 0.90/0.91 Down 0.09/0.10 ptb=82621.6 | CLOB 4618 сообщ., задержка p50/p90=39.0/46.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791810432455 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=1.2/1.2 мс
13:07:12 [cex] Binance 70 сд. задержка p50/p90=146.8/148.2 мс | Coinbase 45 задержка p50=84.3 мс | смещение часов +22.2 мс | lag loop p99/max=2.1/2.8 мс
13:07:12 [cex] binance_futures 99 сд. p50=158.2 мс | bybit 108 сд. p50=115.8 мс | okx 98 сд. p50=156.6 мс | binance_futures_book 1684 сд. p50=147.9 мс | binance_futures_depth 93 сд. p50=146.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 158 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 25 сд. p50=51.9 мс | bitstamp 0 сд. p50=n/a мс
13:07:22 [pm] T-157.5s Up 0.87/0.88 Down 0.12/0.13 ptb=82621.6 | CLOB 5641 сообщ., задержка p50/p90=43.8/241.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791810442458 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=1.6/1.8 мс
13:07:22 [cex] Binance 65 сд. задержка p50/p90=154.4/156.4 мс | Coinbase 38 задержка p50=83.9 мс | смещение часов +22.2 мс | lag loop p99/max=4.5/8.2 мс
13:07:22 [cex] binance_futures 126 сд. p50=162.3 мс | bybit 246 сд. p50=126.8 мс | okx 185 сд. p50=156.2 мс | binance_futures_book 3532 сд. p50=148.3 мс | binance_futures_depth 97 сд. p50=146.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 148 сд. p50=113.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 15 сд. p50=47.5 мс | bitstamp 3 сд. p50=53.8 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
