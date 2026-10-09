# Состояние сервера записи

Время (UTC): 2026-10-09 13:26:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 6 hours, 2 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         668         802           2         630        1237
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.19 / 0.20 / 0.28

## Данные
- файлов: 670, всего 308 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 26 | 5 МБ | 0 |
| bn_book | 26 | 485 КБ | 0 |
| bnf_agg | 26 | 8 МБ | 0 |
| bnf_book | 26 | 218 МБ | 0 |
| bnf_depth5 | 26 | 13 МБ | 0 |
| bnf_liq | 26 | 23 КБ | 1164 |
| bs_trade | 26 | 535 КБ | 2 |
| by_book1 | 26 | 15 МБ | 0 |
| by_liq | 23 | 25 КБ | 1887 |
| by_trade | 26 | 6 МБ | 0 |
| cb_ticker | 26 | 4 МБ | 0 |
| clock | 26 | 20 КБ | 8 |
| clock_pm | 26 | 20 КБ | 17 |
| events | 23 | 7 КБ | 552 |
| events_pm | 26 | 15 КБ | 81 |
| health_cex | 26 | 279 КБ | 0 |
| health_feeds | 26 | 1 МБ | 0 |
| health_pm | 26 | 285 КБ | 3 |
| kr_trade | 26 | 1 МБ | 2 |
| ok_trade | 26 | 8 МБ | 0 |
| pm_depth | 26 | 6 МБ | 1 |
| pm_rtt | 26 | 182 КБ | 5 |
| pm_top | 26 | 12 МБ | 1 |
| pm_trades | 26 | 8 МБ | 1 |
| rtds | 26 | 2 МБ | 1 |
| windows | 26 | 53 КБ | 184 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 38, всего 287
- Polymarket CLOB: TCP 6, TLS 41, всего 82
- Polymarket gamma: TCP 5, TLS 42, всего 54

## Последние строки журнала записи
```
13:25:55 [pm] T-244.6s Up 0.36/0.37 Down 0.63/0.64 ptb=82971.2 | CLOB 6901 сообщ., задержка p50/p90=386.2/557.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791552355415 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=1.3/1.9 мс
13:25:57 [cex] Binance 41 сд. задержка p50/p90=144.9/146.0 мс | Coinbase 73 задержка p50=83.6 мс | смещение часов +20.8 мс | lag loop p99/max=2.3/6.7 мс
13:25:57 [cex] binance_futures 73 сд. p50=153.2 мс | bybit 74 сд. p50=115.1 мс | okx 59 сд. p50=146.9 мс | binance_futures_book 1809 сд. p50=157.9 мс | binance_futures_depth 89 сд. p50=145.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 157 сд. p50=112.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 11 сд. p50=42.6 мс | bitstamp 4 сд. p50=52.3 мс
13:26:05 [pm] T-234.6s Up 0.28/0.29 Down 0.71/0.72 ptb=82971.2 | CLOB 7230 сообщ., задержка p50/p90=46.4/598.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791552365417 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=2.1/2.2 мс
13:26:07 [cex] Binance 175 сд. задержка p50/p90=145.4/147.3 мс | Coinbase 44 задержка p50=84.0 мс | смещение часов +20.8 мс | lag loop p99/max=5.9/8.7 мс
13:26:07 [cex] binance_futures 176 сд. p50=148.8 мс | bybit 242 сд. p50=115.3 мс | okx 273 сд. p50=147.6 мс | binance_futures_book 3789 сд. p50=158.4 мс | binance_futures_depth 95 сд. p50=145.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 282 сд. p50=112.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 47 сд. p50=45.5 мс | bitstamp 8 сд. p50=48.1 мс
13:26:15 [pm] T-224.6s Up 0.15/0.16 Down 0.84/0.85 ptb=82971.2 | CLOB 8441 сообщ., задержка p50/p90=45.7/89.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791552375418 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=1.9/2.1 мс
13:26:17 [cex] Binance 198 сд. задержка p50/p90=145.4/147.0 мс | Coinbase 69 задержка p50=83.2 мс | смещение часов +20.8 мс | lag loop p99/max=2.7/2.8 мс
13:26:17 [cex] binance_futures 290 сд. p50=152.9 мс | bybit 393 сд. p50=115.6 мс | okx 326 сд. p50=148.2 мс | binance_futures_book 5069 сд. p50=157.7 мс | binance_futures_depth 97 сд. p50=145.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 252 сд. p50=112.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 53 сд. p50=49.6 мс | bitstamp 10 сд. p50=52.0 мс
13:26:25 [pm] T-214.6s Up 0.13/0.14 Down 0.86/0.87 ptb=82971.2 | CLOB 8289 сообщ., задержка p50/p90=43.9/88.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791552385419 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=1.6/1.8 мс
13:26:27 [cex] Binance 69 сд. задержка p50/p90=144.9/146.2 мс | Coinbase 45 задержка p50=82.6 мс | смещение часов +20.8 мс | lag loop p99/max=2.1/2.1 мс
13:26:27 [cex] binance_futures 142 сд. p50=154.4 мс | bybit 215 сд. p50=115.5 мс | okx 259 сд. p50=148.4 мс | binance_futures_book 4200 сд. p50=159.7 мс | binance_futures_depth 96 сд. p50=145.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 221 сд. p50=112.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 17 сд. p50=47.7 мс | bitstamp 11 сд. p50=48.0 мс
13:26:35 [pm] T-204.6s Up 0.12/0.13 Down 0.87/0.88 ptb=82971.2 | CLOB 4054 сообщ., задержка p50/p90=42.3/72.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791552395421 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.1/4.6 мс
13:26:37 [cex] Binance 75 сд. задержка p50/p90=145.6/146.7 мс | Coinbase 64 задержка p50=83.2 мс | смещение часов +21.2 мс | lag loop p99/max=2.1/2.1 мс
13:26:37 [cex] binance_futures 152 сд. p50=146.8 мс | bybit 145 сд. p50=115.4 мс | okx 89 сд. p50=146.9 мс | binance_futures_book 1719 сд. p50=157.7 мс | binance_futures_depth 96 сд. p50=145.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 180 сд. p50=113.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 14 сд. p50=46.1 мс | bitstamp 4 сд. p50=53.5 мс
```

Представлено версией кода: 7642f87; python 3.12.3
