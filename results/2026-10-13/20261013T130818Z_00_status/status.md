# Состояние сервера записи

Время (UTC): 2026-10-13 13:08:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 6 days, 5 hours, 44 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         519        1036           2         529        1386
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.51 / 0.32 / 0.26

## Данные
- файлов: 3124, всего 858 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 122 | 14 МБ | 2 |
| bn_book | 122 | 1 МБ | 2 |
| bnf_agg | 122 | 22 МБ | 2 |
| bnf_book | 118 | 557 МБ | 11992 |
| bnf_depth5 | 118 | 41 МБ | 12068 |
| bnf_liq | 108 | 66 КБ | 226 |
| bs_trade | 118 | 1 МБ | 11988 |
| by_book1 | 122 | 46 МБ | 2 |
| by_liq | 102 | 58 КБ | 1282 |
| by_trade | 122 | 14 МБ | 2 |
| bys_book1 | 6 | 2 МБ | 2 |
| bys_trade | 6 | 1015 КБ | 2 |
| cb_ticker | 122 | 13 МБ | 2 |
| clock | 122 | 94 КБ | 16 |
| clock_pm | 122 | 94 КБ | 15 |
| events | 114 | 39 КБ | 698 |
| events_pm | 121 | 46 КБ | 1384 |
| health_cex | 122 | 1 МБ | 2 |
| health_feeds | 122 | 5 МБ | 2 |
| health_pm | 122 | 1 МБ | 1 |
| kr_trade | 118 | 3 МБ | 11988 |
| ok_trade | 121 | 19 МБ | 2 |
| pm_depth | 122 | 24 МБ | 1 |
| pm_rtt | 122 | 807 КБ | 3 |
| pm_top | 122 | 48 МБ | 1 |
| pm_trades | 122 | 35 МБ | 1 |
| rtds | 122 | 8 МБ | 1 |
| windows | 122 | 249 КБ | 253 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 42, всего 292
- Polymarket CLOB: TCP 5, TLS 48, всего 95
- Polymarket gamma: TCP 5, TLS 38, всего 58

## Последние строки журнала записи
```
13:07:36 [cex] Binance 91 сд. задержка p50/p90=146.2/147.0 мс | Coinbase 27 задержка p50=81.7 мс | смещение часов +21.3 мс | lag loop p99/max=2.1/2.1 мс
13:07:36 [cex] binance_futures 132 сд. p50=146.4 мс | bybit 129 сд. p50=116.0 мс | bybit_book 234 сд. p50=113.2 мс | bybit_spot 242 сд. p50=116.3 мс | bybit_spot_book 113 сд. p50=123.1 мс | okx 189 сд. p50=156.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:07:36 [pm] T-143.2s Up 0.49/0.50 Down 0.50/0.51 ptb=83111.2 | CLOB 12359 сообщ., задержка p50/p90=54.1/102.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791896856838 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.2 мс | lag loop p99/max=4.1/4.5 мс
13:07:46 [cex] Binance 47 сд. задержка p50/p90=145.8/146.8 мс | Coinbase 35 задержка p50=80.3 мс | смещение часов +21.3 мс | lag loop p99/max=2.0/2.2 мс
13:07:46 [cex] binance_futures 101 сд. p50=148.3 мс | bybit 83 сд. p50=115.9 мс | bybit_book 267 сд. p50=113.2 мс | bybit_spot 180 сд. p50=115.7 мс | bybit_spot_book 87 сд. p50=123.0 мс | okx 73 сд. p50=156.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:07:46 [pm] T-133.2s Up 0.45/0.46 Down 0.54/0.55 ptb=83111.2 | CLOB 10908 сообщ., задержка p50/p90=38.6/43.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791896866839 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.3 мс | lag loop p99/max=1.3/2.4 мс
13:07:56 [cex] Binance 30 сд. задержка p50/p90=145.8/146.8 мс | Coinbase 49 задержка p50=80.0 мс | смещение часов +21.3 мс | lag loop p99/max=2.2/2.3 мс
13:07:56 [cex] binance_futures 125 сд. p50=146.9 мс | bybit 142 сд. p50=115.5 мс | bybit_book 227 сд. p50=113.3 мс | bybit_spot 298 сд. p50=115.7 мс | bybit_spot_book 101 сд. p50=123.1 мс | okx 157 сд. p50=156.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:07:56 [pm] T-123.2s Up 0.47/0.48 Down 0.52/0.53 ptb=83111.2 | CLOB 13320 сообщ., задержка p50/p90=38.3/40.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791896876841 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=1.7/1.9 мс
13:08:06 [cex] Binance 33 сд. задержка p50/p90=145.6/146.7 мс | Coinbase 42 задержка p50=79.2 мс | смещение часов +20.9 мс | lag loop p99/max=2.1/2.1 мс
13:08:06 [cex] binance_futures 54 сд. p50=272.7 мс | bybit 87 сд. p50=114.9 мс | bybit_book 277 сд. p50=113.1 мс | bybit_spot 31 сд. p50=117.3 мс | bybit_spot_book 62 сд. p50=123.1 мс | okx 33 сд. p50=179.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:08:06 [pm] T-113.2s Up 0.53/0.54 Down 0.46/0.47 ptb=83111.2 | CLOB 12305 сообщ., задержка p50/p90=38.2/44.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791896886843 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=1.7/3.7 мс
13:08:16 [cex] Binance 115 сд. задержка p50/p90=145.7/146.5 мс | Coinbase 35 задержка p50=79.1 мс | смещение часов +20.9 мс | lag loop p99/max=2.0/2.0 мс
13:08:16 [cex] binance_futures 107 сд. p50=145.7 мс | bybit 143 сд. p50=115.1 мс | bybit_book 355 сд. p50=112.8 мс | bybit_spot 198 сд. p50=114.9 мс | bybit_spot_book 98 сд. p50=122.7 мс | okx 114 сд. p50=156.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:08:16 [pm] T-103.2s Up 0.76/0.77 Down 0.23/0.24 ptb=83111.2 | CLOB 9798 сообщ., задержка p50/p90=37.7/41.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791896896844 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=1.7/1.9 мс
```

Представлено версией кода: ec1316a; python 3.12.3
