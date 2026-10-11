# Состояние сервера записи

Время (UTC): 2026-10-11 12:12:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 4 days, 4 hours, 48 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         695         952           1         465        1210
Swap:           2047          62        1985
```
- нагрузка CPU (1/5/15 мин): 0.13 / 0.17 / 0.17

## Данные
- файлов: 1868, всего 459 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 73 | 8 МБ | -0 |
| bn_book | 73 | 682 КБ | 36 |
| bnf_agg | 73 | 12 МБ | -0 |
| bnf_book | 73 | 289 МБ | -0 |
| bnf_depth5 | 73 | 25 МБ | -0 |
| bnf_liq | 61 | 35 КБ | 355 |
| bs_trade | 73 | 893 КБ | 10 |
| by_book1 | 73 | 25 МБ | -0 |
| by_liq | 59 | 32 КБ | 670 |
| by_trade | 73 | 7 МБ | -0 |
| cb_ticker | 73 | 7 МБ | 2 |
| clock | 73 | 55 КБ | -0 |
| clock_pm | 73 | 55 КБ | 17 |
| events | 70 | 24 КБ | 612 |
| events_pm | 72 | 28 КБ | 1573 |
| health_cex | 73 | 758 КБ | 8 |
| health_feeds | 73 | 3 МБ | 8 |
| health_pm | 73 | 781 КБ | 7 |
| kr_trade | 73 | 2 МБ | -0 |
| ok_trade | 73 | 10 МБ | -0 |
| pm_depth | 73 | 14 МБ | 1 |
| pm_rtt | 73 | 484 КБ | 1 |
| pm_top | 73 | 28 МБ | 1 |
| pm_trades | 73 | 20 МБ | 1 |
| rtds | 73 | 5 МБ | 1 |
| windows | 73 | 149 КБ | 273 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 37, всего 285
- Polymarket CLOB: TCP 6, TLS 52, всего 94
- Polymarket gamma: TCP 5, TLS 41, всего 53

## Последние строки журнала записи
```
12:11:19 [cex] Binance 124 сд. задержка p50/p90=149.2/160.1 мс | Coinbase 48 задержка p50=83.4 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.9 мс
12:11:19 [cex] binance_futures 171 сд. p50=148.2 мс | bybit 156 сд. p50=118.9 мс | okx 149 сд. p50=158.7 мс | binance_futures_book 2804 сд. p50=146.8 мс | binance_futures_depth 95 сд. p50=146.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 171 сд. p50=113.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 14 сд. p50=47.8 мс | bitstamp 5 сд. p50=56.6 мс
12:11:19 [pm] T-220.7s Up 0.75/0.76 Down 0.24/0.25 ptb=83103.6 | CLOB 7159 сообщ., задержка p50/p90=42.7/120.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791720679323 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=2.2/3.1 мс
12:11:29 [cex] Binance 27 сд. задержка p50/p90=145.8/146.8 мс | Coinbase 11 задержка p50=82.8 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.1 мс
12:11:29 [cex] binance_futures 23 сд. p50=294.8 мс | bybit 8 сд. p50=115.7 мс | okx 22 сд. p50=155.1 мс | binance_futures_book 570 сд. p50=146.2 мс | binance_futures_depth 93 сд. p50=146.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 98 сд. p50=113.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=44.6 мс | bitstamp 2 сд. p50=52.0 мс
12:11:29 [pm] T-210.7s Up 0.79/0.80 Down 0.20/0.21 ptb=83103.6 | CLOB 3933 сообщ., задержка p50/p90=37.9/45.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791720689325 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=1.9/2.1 мс
12:11:39 [cex] Binance 35 сд. задержка p50/p90=145.9/147.3 мс | Coinbase 32 задержка p50=83.5 мс | смещение часов +21.6 мс | lag loop p99/max=2.2/2.3 мс
12:11:39 [cex] binance_futures 27 сд. p50=294.8 мс | bybit 7 сд. p50=115.4 мс | okx 25 сд. p50=155.4 мс | binance_futures_book 1122 сд. p50=146.5 мс | binance_futures_depth 87 сд. p50=146.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 153 сд. p50=113.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=45.8 мс | bitstamp 2 сд. p50=47.5 мс
12:11:39 [pm] T-200.7s Up 0.81/0.82 Down 0.18/0.19 ptb=83103.6 | CLOB 3506 сообщ., задержка p50/p90=37.8/45.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791720699327 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.0 мс | lag loop p99/max=2.0/2.1 мс
12:11:49 [cex] Binance 18 сд. задержка p50/p90=145.9/146.8 мс | Coinbase 10 задержка p50=84.0 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.2 мс
12:11:49 [cex] binance_futures 27 сд. p50=294.8 мс | bybit 5 сд. p50=115.7 мс | okx 22 сд. p50=155.3 мс | binance_futures_book 383 сд. p50=146.2 мс | binance_futures_depth 87 сд. p50=146.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 102 сд. p50=113.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=46.3 мс | bitstamp 2 сд. p50=48.7 мс
12:11:49 [pm] T-190.7s Up 0.83/0.84 Down 0.16/0.17 ptb=83103.6 | CLOB 2232 сообщ., задержка p50/p90=37.3/40.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791720709329 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.0 мс | lag loop p99/max=2.0/2.0 мс
12:11:59 [cex] Binance 29 сд. задержка p50/p90=145.8/148.1 мс | Coinbase 11 задержка p50=83.8 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.1 мс
12:11:59 [cex] binance_futures 72 сд. p50=147.3 мс | bybit 7 сд. p50=115.7 мс | okx 30 сд. p50=155.5 мс | binance_futures_book 955 сд. p50=146.4 мс | binance_futures_depth 96 сд. p50=146.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 121 сд. p50=113.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=43.1 мс | bitstamp 1 сд. p50=47.2 мс
12:11:59 [pm] T-180.7s Up 0.84/0.85 Down 0.15/0.16 ptb=83103.6 | CLOB 2999 сообщ., задержка p50/p90=39.4/56.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791720719330 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.0 мс | lag loop p99/max=1.8/1.9 мс
```

Представлено версией кода: 69087ca; python 3.12.3
