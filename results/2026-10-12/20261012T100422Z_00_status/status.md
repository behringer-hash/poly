# Состояние сервера записи

Время (UTC): 2026-10-12 10:04:22

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 2 hours, 40 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         763         724           2         626        1142
Swap:           2047         105        1942
```
- нагрузка CPU (1/5/15 мин): 0.27 / 0.42 / 0.36

## Данные
- файлов: 2435, всего 599 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 95 | 10 МБ | 0 |
| bn_book | 95 | 864 КБ | 12 |
| bnf_agg | 95 | 15 МБ | 0 |
| bnf_book | 95 | 382 МБ | 0 |
| bnf_depth5 | 95 | 32 МБ | 0 |
| bnf_liq | 82 | 45 КБ | 151 |
| bs_trade | 95 | 1 МБ | 0 |
| by_book1 | 95 | 32 МБ | 0 |
| by_liq | 78 | 40 КБ | 137 |
| by_trade | 95 | 9 МБ | 0 |
| cb_ticker | 95 | 9 МБ | 0 |
| clock | 95 | 72 КБ | 18 |
| clock_pm | 95 | 72 КБ | 34 |
| events | 90 | 30 КБ | 2914 |
| events_pm | 95 | 36 КБ | 188 |
| health_cex | 95 | 988 КБ | 0 |
| health_feeds | 95 | 4 МБ | 0 |
| health_pm | 95 | 1014 КБ | 1 |
| kr_trade | 95 | 2 МБ | 2 |
| ok_trade | 95 | 13 МБ | 0 |
| pm_depth | 95 | 18 МБ | 1 |
| pm_rtt | 95 | 626 КБ | 1 |
| pm_top | 95 | 36 МБ | 1 |
| pm_trades | 95 | 26 МБ | 1 |
| rtds | 95 | 6 МБ | 1 |
| windows | 95 | 193 КБ | 196 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 38, всего 289
- Polymarket CLOB: TCP 6, TLS 42, всего 91
- Polymarket gamma: TCP 5, TLS 40, всего 51

## Последние строки журнала записи
```
10:03:40 [pm] T- 79.3s Up 0.05/0.06 Down 0.94/0.95 ptb=83459.4 | CLOB 3760 сообщ., задержка p50/p90=41.0/74.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791799420719 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=1.8/1.9 мс
10:03:40 [cex] Binance 33 сд. задержка p50/p90=144.7/145.8 мс | Coinbase 19 задержка p50=82.5 мс | смещение часов +20.6 мс | lag loop p99/max=2.1/2.1 мс
10:03:40 [cex] binance_futures 32 сд. p50=294.2 мс | bybit 4 сд. p50=113.5 мс | okx 37 сд. p50=154.5 мс | binance_futures_book 1072 сд. p50=145.0 мс | binance_futures_depth 93 сд. p50=145.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 66 сд. p50=112.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 15 сд. p50=39.3 мс | bitstamp 0 сд. p50=n/a мс
10:03:50 [pm] T- 69.3s Up 0.01/0.02 Down 0.98/0.99 ptb=83459.4 | CLOB 3143 сообщ., задержка p50/p90=41.1/43.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791799430721 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.9/1.9 мс
10:03:50 [cex] Binance 21 сд. задержка p50/p90=144.7/145.2 мс | Coinbase 9 задержка p50=82.8 мс | смещение часов +20.6 мс | lag loop p99/max=2.0/2.2 мс
10:03:50 [cex] binance_futures 34 сд. p50=294.1 мс | bybit 10 сд. p50=113.8 мс | okx 27 сд. p50=154.4 мс | binance_futures_book 2210 сд. p50=145.0 мс | binance_futures_depth 95 сд. p50=145.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 76 сд. p50=112.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=42.8 мс | bitstamp 1 сд. p50=44.8 мс
10:04:00 [pm] T- 59.3s Up n/a/0.01 Down 0.99/n/a ptb=83459.4 | CLOB 3076 сообщ., задержка p50/p90=41.5/55.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791799440722 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=2.0/2.1 мс
10:04:00 [cex] Binance 16 сд. задержка p50/p90=144.6/145.1 мс | Coinbase 7 задержка p50=82.8 мс | смещение часов +20.6 мс | lag loop p99/max=2.2/2.2 мс
10:04:00 [cex] binance_futures 25 сд. p50=294.1 мс | bybit 10 сд. p50=113.4 мс | okx 81 сд. p50=154.4 мс | binance_futures_book 1785 сд. p50=145.0 мс | binance_futures_depth 96 сд. p50=145.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 109 сд. p50=112.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=41.7 мс | bitstamp 4 сд. p50=49.9 мс
10:04:10 [pm] T- 49.3s Up n/a/0.01 Down 0.99/n/a ptb=83459.4 | CLOB 1644 сообщ., задержка p50/p90=41.4/45.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791799450723 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=4.0/7.2 мс
10:04:10 [cex] Binance 32 сд. задержка p50/p90=142.7/144.9 мс | Coinbase 44 задержка p50=80.4 мс | смещение часов +18.3 мс | lag loop p99/max=4.1/5.7 мс
10:04:10 [cex] binance_futures 49 сд. p50=206.7 мс | bybit 93 сд. p50=114.0 мс | okx 26 сд. p50=154.1 мс | binance_futures_book 3762 сд. p50=142.9 мс | binance_futures_depth 91 сд. p50=143.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 138 сд. p50=110.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 10 сд. p50=42.1 мс | bitstamp 1 сд. p50=47.4 мс
10:04:20 [pm] T- 39.3s Up n/a/0.01 Down 0.99/n/a ptb=83459.4 | CLOB 997 сообщ., задержка p50/p90=41.3/43.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791799460724 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.0/3.3 мс
10:04:20 [cex] Binance 31 сд. задержка p50/p90=142.4/143.4 мс | Coinbase 7 задержка p50=80.1 мс | смещение часов +18.3 мс | lag loop p99/max=2.1/2.1 мс
10:04:20 [cex] binance_futures 65 сд. p50=256.3 мс | bybit 9 сд. p50=111.5 мс | okx 15 сд. p50=152.6 мс | binance_futures_book 1569 сд. p50=142.8 мс | binance_futures_depth 88 сд. p50=142.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 88 сд. p50=110.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=47.0 мс | bitstamp 5 сд. p50=50.4 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
