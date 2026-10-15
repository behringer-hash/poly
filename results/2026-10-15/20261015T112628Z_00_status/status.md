# Состояние сервера записи

Время (UTC): 2026-10-15 11:26:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 4 hours, 2 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         679         410           2        1064        1226
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.23 / 0.23 / 0.18

## Данные
- файлов: 4224, всего 1007 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 168 | 22 МБ | 2 |
| bn_book | 168 | 2 МБ | 2 |
| bnf_agg | 168 | 34 МБ | 2 |
| bnf_book | 118 | 557 МБ | 178682 |
| bnf_depth5 | 118 | 41 МБ | 178758 |
| bnf_liq | 150 | 100 КБ | 466 |
| bs_trade | 118 | 1 МБ | 178678 |
| by_book1 | 168 | 72 МБ | 2 |
| by_liq | 148 | 83 КБ | 1331 |
| by_trade | 168 | 23 МБ | 2 |
| bys_book1 | 52 | 20 МБ | 2 |
| bys_trade | 52 | 9 МБ | 2 |
| cb_ticker | 168 | 20 МБ | 2 |
| clock | 168 | 130 КБ | 26 |
| clock_pm | 168 | 130 КБ | 24 |
| events | 159 | 51 КБ | 256 |
| events_pm | 168 | 60 КБ | 643 |
| health_cex | 168 | 2 МБ | 10 |
| health_feeds | 168 | 6 МБ | 10 |
| health_pm | 168 | 2 МБ | 6 |
| kr_trade | 118 | 3 МБ | 178678 |
| ok_trade | 167 | 30 МБ | 2 |
| pm_depth | 168 | 33 МБ | 0 |
| pm_rtt | 168 | 1 МБ | 2 |
| pm_top | 168 | 68 МБ | 0 |
| pm_trades | 168 | 49 МБ | 0 |
| rtds | 168 | 11 МБ | 0 |
| windows | 168 | 346 КБ | 174 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 35, всего 294
- Polymarket CLOB: TCP 6, TLS 38, всего 88
- Polymarket gamma: TCP 5, TLS 37, всего 56

## Последние строки журнала записи
```
11:25:40 [pm] T-259.5s Up 0.64/0.65 Down 0.35/0.36 ptb=80905.2 | CLOB 6075 сообщ., задержка p50/p90=40.3/49.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792063540465 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.1/2.2 мс
11:25:46 [cex] Binance 51 сд. задержка p50/p90=146.1/146.9 мс | Coinbase 64 задержка p50=83.4 мс | смещение часов +21.3 мс | lag loop p99/max=1.9/2.2 мс
11:25:46 [cex] binance_futures 97 сд. p50=161.7 мс | bybit 148 сд. p50=128.9 мс | bybit_book 154 сд. p50=192.2 мс | bybit_spot 152 сд. p50=124.7 мс | bybit_spot_book 108 сд. p50=124.2 мс | okx 59 сд. p50=160.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
11:25:50 [pm] T-249.5s Up 0.67/0.68 Down 0.32/0.33 ptb=80905.2 | CLOB 6642 сообщ., задержка p50/p90=39.9/43.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792063550467 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/2.1 мс
11:25:56 [cex] Binance 10 сд. задержка p50/p90=146.0/147.0 мс | Coinbase 37 задержка p50=83.5 мс | смещение часов +21.3 мс | lag loop p99/max=2.1/2.1 мс
11:25:56 [cex] binance_futures 54 сд. p50=164.9 мс | bybit 122 сд. p50=129.0 мс | bybit_book 150 сд. p50=187.5 мс | bybit_spot 141 сд. p50=124.7 мс | bybit_spot_book 136 сд. p50=124.1 мс | okx 49 сд. p50=160.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
11:26:00 [pm] T-239.5s Up 0.66/0.67 Down 0.33/0.34 ptb=80905.2 | CLOB 7940 сообщ., задержка p50/p90=39.3/41.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792063560469 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/39.0 мс
11:26:06 [cex] Binance 29 сд. задержка p50/p90=146.0/146.4 мс | Coinbase 26 задержка p50=77.3 мс | смещение часов +14.0 мс | lag loop p99/max=2.3/4.8 мс
11:26:06 [cex] binance_futures 32 сд. p50=166.1 мс | bybit 33 сд. p50=128.5 мс | bybit_book 116 сд. p50=185.5 мс | bybit_spot 86 сд. p50=124.4 мс | bybit_spot_book 91 сд. p50=123.8 мс | okx 18 сд. p50=159.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
11:26:10 [pm] T-229.5s Up 0.56/0.57 Down 0.43/0.44 ptb=80905.2 | CLOB 7248 сообщ., задержка p50/p90=64.7/142.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792063570470 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=6.9/18.8 мс
11:26:16 [cex] Binance 139 сд. задержка p50/p90=138.8/139.7 мс | Coinbase 52 задержка p50=78.3 мс | смещение часов +14.0 мс | lag loop p99/max=2.1/2.2 мс
11:26:16 [cex] binance_futures 172 сд. p50=159.1 мс | bybit 200 сд. p50=121.5 мс | bybit_book 226 сд. p50=170.2 мс | bybit_spot 204 сд. p50=117.2 мс | bybit_spot_book 188 сд. p50=116.8 мс | okx 151 сд. p50=152.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
11:26:20 [pm] T-219.5s Up 0.67/0.69 Down 0.31/0.33 ptb=80905.2 | CLOB 11004 сообщ., задержка p50/p90=40.3/47.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792063580472 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.1/6.6 мс
11:26:26 [cex] Binance 41 сд. задержка p50/p90=138.7/139.3 мс | Coinbase 44 задержка p50=76.7 мс | смещение часов +14.0 мс | lag loop p99/max=1.8/1.8 мс
11:26:26 [cex] binance_futures 67 сд. p50=157.6 мс | bybit 157 сд. p50=121.3 мс | bybit_book 205 сд. p50=177.2 мс | bybit_spot 171 сд. p50=117.2 мс | bybit_spot_book 129 сд. p50=116.8 мс | okx 65 сд. p50=152.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: ec1316a; python 3.12.3
