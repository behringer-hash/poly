# Состояние сервера записи

Время (UTC): 2026-10-11 19:29:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 4 days, 12 hours, 5 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         692         955           1         466        1213
Swap:           2047          72        1975
```
- нагрузка CPU (1/5/15 мин): 0.16 / 0.21 / 0.19

## Данные
- файлов: 2047, всего 516 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 80 | 9 МБ | 2 |
| bn_book | 80 | 735 КБ | 10 |
| bnf_agg | 80 | 13 МБ | 2 |
| bnf_book | 80 | 326 МБ | 2 |
| bnf_depth5 | 80 | 29 МБ | 2 |
| bnf_liq | 67 | 37 КБ | 5262 |
| bs_trade | 80 | 978 КБ | 10 |
| by_book1 | 80 | 28 МБ | 2 |
| by_liq | 63 | 36 КБ | 2487 |
| by_trade | 80 | 8 МБ | 4 |
| cb_ticker | 80 | 8 МБ | 2 |
| clock | 80 | 61 КБ | 22 |
| clock_pm | 80 | 61 КБ | 36 |
| events | 77 | 27 КБ | 368 |
| events_pm | 80 | 32 КБ | 234 |
| health_cex | 80 | 840 КБ | 4 |
| health_feeds | 80 | 3 МБ | 4 |
| health_pm | 80 | 865 КБ | 4 |
| kr_trade | 80 | 2 МБ | 2 |
| ok_trade | 80 | 12 МБ | 2 |
| pm_depth | 80 | 16 МБ | 0 |
| pm_rtt | 80 | 543 КБ | 2 |
| pm_top | 80 | 31 МБ | 0 |
| pm_trades | 80 | 22 МБ | 8 |
| rtds | 80 | 5 МБ | 0 |
| windows | 80 | 165 КБ | 64 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 37, всего 287
- Polymarket CLOB: TCP 5, TLS 38, всего 82
- Polymarket gamma: TCP 5, TLS 36, всего 48

## Последние строки журнала записи
```
19:28:22 [cex] Binance 21 сд. задержка p50/p90=144.4/144.6 мс | Coinbase 32 задержка p50=82.4 мс | смещение часов +19.4 мс | lag loop p99/max=2.0/2.5 мс
19:28:22 [cex] binance_futures 28 сд. p50=292.2 мс | bybit 31 сд. p50=113.8 мс | okx 30 сд. p50=153.7 мс | binance_futures_book 744 сд. p50=143.9 мс | binance_futures_depth 84 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 92 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=41.7 мс | bitstamp 2 сд. p50=66.6 мс
19:28:23 [pm] T- 96.9s Up 0.01/0.02 Down 0.98/0.99 ptb=83635.7 | CLOB 1187 сообщ., задержка p50/p90=35.7/38.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791746903129 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.3 мс | lag loop p99/max=2.0/2.2 мс
19:28:32 [cex] Binance 34 сд. задержка p50/p90=145.0/145.2 мс | Coinbase 29 задержка p50=80.6 мс | смещение часов +19.4 мс | lag loop p99/max=2.0/2.2 мс
19:28:32 [cex] binance_futures 23 сд. p50=292.4 мс | bybit 24 сд. p50=113.8 мс | okx 23 сд. p50=152.9 мс | binance_futures_book 316 сд. p50=143.6 мс | binance_futures_depth 80 сд. p50=143.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 62 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 8 сд. p50=44.5 мс | bitstamp 0 сд. p50=n/a мс
19:28:33 [pm] T- 86.9s Up n/a/0.01 Down 0.99/n/a ptb=83635.7 | CLOB 808 сообщ., задержка p50/p90=35.6/39.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791746913130 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.1/2.3 мс
19:28:42 [cex] Binance 12 сд. задержка p50/p90=144.5/144.6 мс | Coinbase 30 задержка p50=81.4 мс | смещение часов +19.4 мс | lag loop p99/max=2.0/2.3 мс
19:28:42 [cex] binance_futures 21 сд. p50=292.4 мс | bybit 38 сд. p50=113.5 мс | okx 23 сд. p50=153.1 мс | binance_futures_book 408 сд. p50=143.7 мс | binance_futures_depth 76 сд. p50=143.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 58 сд. p50=111.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=41.7 мс | bitstamp 0 сд. p50=n/a мс
19:28:43 [pm] T- 76.9s Up n/a/0.01 Down 0.99/n/a ptb=83635.7 | CLOB 468 сообщ., задержка p50/p90=33.6/35.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791746923131 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.1/2.2 мс
19:28:52 [cex] Binance 11 сд. задержка p50/p90=143.8/144.8 мс | Coinbase 28 задержка p50=80.4 мс | смещение часов +18.7 мс | lag loop p99/max=1.9/2.0 мс
19:28:52 [cex] binance_futures 27 сд. p50=291.7 мс | bybit 75 сд. p50=113.2 мс | okx 30 сд. p50=152.3 мс | binance_futures_book 491 сд. p50=143.2 мс | binance_futures_depth 84 сд. p50=143.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 71 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=43.1 мс | bitstamp 1 сд. p50=63.6 мс
19:28:53 [pm] T- 66.9s Up n/a/0.01 Down 0.99/n/a ptb=83635.7 | CLOB 434 сообщ., задержка p50/p90=33.8/36.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791746933132 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.0/2.1 мс
19:29:02 [cex] Binance 87 сд. задержка p50/p90=144.6/147.8 мс | Coinbase 43 задержка p50=81.0 мс | смещение часов +18.7 мс | lag loop p99/max=2.2/4.6 мс
19:29:02 [cex] binance_futures 102 сд. p50=144.4 мс | bybit 63 сд. p50=114.4 мс | okx 99 сд. p50=154.4 мс | binance_futures_book 3170 сд. p50=143.6 мс | binance_futures_depth 86 сд. p50=143.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 67 сд. p50=110.9 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=39.8 мс | bitstamp 3 сд. p50=44.3 мс
19:29:03 [pm] T- 56.9s Up n/a/0.01 Down 0.99/n/a ptb=83635.7 | CLOB 1919 сообщ., задержка p50/p90=37.0/62.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791746943134 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.1/2.2 мс
```

Представлено версией кода: 69087ca; python 3.12.3
