# Состояние сервера записи

Время (UTC): 2026-10-11 01:46:36

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 18 hours, 22 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         707         928           2         486        1198
Swap:           2047          56        1991
```
- нагрузка CPU (1/5/15 мин): 0.10 / 0.07 / 0.08

## Данные
- файлов: 1587, всего 443 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 62 | 7 МБ | 2 |
| bn_book | 62 | 658 КБ | 126 |
| bnf_agg | 62 | 11 МБ | 4 |
| bnf_book | 62 | 283 МБ | 2 |
| bnf_depth5 | 62 | 25 МБ | 2 |
| bnf_liq | 50 | 31 КБ | 15250 |
| bs_trade | 62 | 851 КБ | 16 |
| by_book1 | 62 | 24 МБ | 2 |
| by_liq | 52 | 31 КБ | 171 |
| by_trade | 62 | 7 МБ | 2 |
| cb_ticker | 62 | 7 МБ | 2 |
| clock | 62 | 48 КБ | 32 |
| clock_pm | 62 | 48 КБ | 47 |
| events | 59 | 21 КБ | 579 |
| events_pm | 62 | 25 КБ | 2047 |
| health_cex | 62 | 663 КБ | 2 |
| health_feeds | 62 | 2 МБ | 2 |
| health_pm | 62 | 682 КБ | 2 |
| kr_trade | 62 | 2 МБ | 8 |
| ok_trade | 62 | 10 МБ | 2 |
| pm_depth | 62 | 13 МБ | 0 |
| pm_rtt | 62 | 435 КБ | 0 |
| pm_top | 62 | 26 МБ | 0 |
| pm_trades | 62 | 18 МБ | 0 |
| rtds | 62 | 4 МБ | 0 |
| windows | 62 | 129 КБ | 151 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 36, всего 286
- Polymarket CLOB: TCP 6, TLS 39, всего 80
- Polymarket gamma: TCP 5, TLS 38, всего 49

## Последние строки журнала записи
```
01:45:54 [pm] T-246.0s Up 0.47/0.48 Down 0.52/0.53 ptb=82933.9 | CLOB 4188 сообщ., задержка p50/p90=43.1/72.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791683154037 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.0/2.1 мс
01:45:54 [cex] Binance 19 сд. задержка p50/p90=143.3/144.2 мс | Coinbase 32 задержка p50=86.3 мс | смещение часов +19.4 мс | lag loop p99/max=2.2/2.2 мс
01:45:54 [cex] binance_futures 26 сд. p50=174.5 мс | bybit 63 сд. p50=114.8 мс | okx 5 сд. p50=153.4 мс | binance_futures_book 1357 сд. p50=145.0 мс | binance_futures_depth 83 сд. p50=144.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 83 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 0 сд. p50=n/a мс | bitstamp 1 сд. p50=45.8 мс
01:46:04 [pm] T-236.0s Up 0.48/0.49 Down 0.51/0.52 ptb=82933.9 | CLOB 3527 сообщ., задержка p50/p90=40.0/45.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791683164038 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.9/4.9 мс
01:46:04 [cex] Binance 16 сд. задержка p50/p90=143.3/143.7 мс | Coinbase 10 задержка p50=81.2 мс | смещение часов +19.5 мс | lag loop p99/max=2.6/4.7 мс
01:46:04 [cex] binance_futures 9 сд. p50=293.0 мс | bybit 5 сд. p50=113.3 мс | okx 5 сд. p50=153.2 мс | binance_futures_book 421 сд. p50=144.2 мс | binance_futures_depth 81 сд. p50=145.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 35 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=45.9 мс | bitstamp 1 сд. p50=49.2 мс
01:46:14 [pm] T-226.0s Up 0.43/0.44 Down 0.56/0.57 ptb=82933.9 | CLOB 2742 сообщ., задержка p50/p90=39.7/43.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791683174039 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.6/1.9 мс
01:46:14 [cex] Binance 25 сд. задержка p50/p90=143.3/143.9 мс | Coinbase 12 задержка p50=81.0 мс | смещение часов +19.5 мс | lag loop p99/max=2.2/2.2 мс
01:46:14 [cex] binance_futures 12 сд. p50=293.7 мс | bybit 2 сд. p50=113.7 мс | okx 5 сд. p50=152.9 мс | binance_futures_book 343 сд. p50=144.3 мс | binance_futures_depth 78 сд. p50=144.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 26 сд. p50=111.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=42.0 мс | bitstamp 1 сд. p50=47.1 мс
01:46:24 [pm] T-216.0s Up 0.44/0.45 Down 0.55/0.56 ptb=82933.9 | CLOB 3452 сообщ., задержка p50/p90=42.1/57.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791683184041 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.9/2.1 мс
01:46:24 [cex] Binance 20 сд. задержка p50/p90=143.3/144.4 мс | Coinbase 23 задержка p50=81.6 мс | смещение часов +19.5 мс | lag loop p99/max=2.2/2.2 мс
01:46:24 [cex] binance_futures 13 сд. p50=293.2 мс | bybit 1 сд. p50=112.9 мс | okx 4 сд. p50=153.0 мс | binance_futures_book 428 сд. p50=144.3 мс | binance_futures_depth 83 сд. p50=144.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 47 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=40.8 мс | bitstamp 2 сд. p50=53.7 мс
01:46:34 [pm] T-206.0s Up 0.52/0.53 Down 0.47/0.48 ptb=82933.9 | CLOB 4584 сообщ., задержка p50/p90=39.6/42.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791683194042 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.8/2.0 мс
01:46:34 [cex] Binance 8 сд. задержка p50/p90=143.5/144.6 мс | Coinbase 31 задержка p50=80.1 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.2 мс
01:46:34 [cex] binance_futures 7 сд. p50=293.2 мс | bybit 7 сд. p50=113.3 мс | okx 2 сд. p50=153.4 мс | binance_futures_book 274 сд. p50=144.3 мс | binance_futures_depth 78 сд. p50=144.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 44 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=40.1 мс | bitstamp 0 сд. p50=n/a мс
```

Представлено версией кода: 69087ca; python 3.12.3
