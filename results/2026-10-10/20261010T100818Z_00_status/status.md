# Состояние сервера записи

Время (UTC): 2026-10-10 10:08:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 2 hours, 44 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         704         981           2         428        1201
Swap:           2047          38        2009
```
- нагрузка CPU (1/5/15 мин): 0.19 / 0.18 / 0.14

## Данные
- файлов: 1210, всего 373 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 47 | 6 МБ | 0 |
| bn_book | 47 | 619 КБ | 45 |
| bnf_agg | 47 | 10 МБ | 0 |
| bnf_book | 47 | 248 МБ | 0 |
| bnf_depth5 | 47 | 18 МБ | 0 |
| bnf_liq | 43 | 30 КБ | 386 |
| bs_trade | 47 | 733 КБ | 0 |
| by_book1 | 47 | 20 МБ | 0 |
| by_liq | 42 | 30 КБ | 2206 |
| by_trade | 47 | 7 МБ | 0 |
| cb_ticker | 47 | 6 МБ | 0 |
| clock | 47 | 35 КБ | 51 |
| clock_pm | 47 | 35 КБ | 1 |
| events | 44 | 15 КБ | 299 |
| events_pm | 47 | 21 КБ | 389 |
| health_cex | 47 | 491 КБ | 0 |
| health_feeds | 47 | 2 МБ | 0 |
| health_pm | 47 | 504 КБ | 1 |
| kr_trade | 47 | 1 МБ | 0 |
| ok_trade | 47 | 9 МБ | 0 |
| pm_depth | 47 | 9 МБ | 1 |
| pm_rtt | 47 | 308 КБ | 3 |
| pm_top | 47 | 19 МБ | 1 |
| pm_trades | 47 | 13 МБ | 1 |
| rtds | 47 | 3 МБ | 1 |
| windows | 47 | 95 КБ | 104 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 35, всего 287
- Polymarket CLOB: TCP 5, TLS 39, всего 87
- Polymarket gamma: TCP 5, TLS 38, всего 50

## Последние строки журнала записи
```
10:07:35 [pm] T-144.0s Up 0.01/0.02 Down 0.98/0.99 ptb=82785.8 | CLOB 2547 сообщ., задержка p50/p90=62.6/284.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791626855997 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/2.2 мс
10:07:37 [cex] Binance 148 сд. задержка p50/p90=147.1/149.9 мс | Coinbase 20 задержка p50=79.1 мс | смещение часов +18.9 мс | lag loop p99/max=2.1/4.7 мс
10:07:37 [cex] binance_futures 117 сд. p50=148.3 мс | bybit 44 сд. p50=117.1 мс | okx 102 сд. p50=145.5 мс | binance_futures_book 1644 сд. p50=143.8 мс | binance_futures_depth 91 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 59 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 18 сд. p50=42.9 мс | bitstamp 5 сд. p50=46.9 мс
10:07:45 [pm] T-134.0s Up 0.02/0.03 Down 0.97/0.98 ptb=82785.8 | CLOB 1844 сообщ., задержка p50/p90=61.1/69.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791626865999 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.8/2.1 мс
10:07:47 [cex] Binance 51 сд. задержка p50/p90=143.0/143.9 мс | Coinbase 19 задержка p50=78.6 мс | смещение часов +18.9 мс | lag loop p99/max=2.0/2.1 мс
10:07:47 [cex] binance_futures 34 сд. p50=292.5 мс | bybit 23 сд. p50=112.6 мс | okx 16 сд. p50=142.5 мс | binance_futures_book 524 сд. p50=143.2 мс | binance_futures_depth 86 сд. p50=143.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 55 сд. p50=110.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=39.8 мс | bitstamp 4 сд. p50=48.5 мс
10:07:55 [pm] T-124.0s Up 0.02/0.03 Down 0.97/0.98 ptb=82785.8 | CLOB 1326 сообщ., задержка p50/p90=60.7/65.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791626876000 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/2.1 мс
10:07:57 [cex] Binance 44 сд. задержка p50/p90=143.0/143.9 мс | Coinbase 3 задержка p50=78.7 мс | смещение часов +18.9 мс | lag loop p99/max=2.2/2.2 мс
10:07:57 [cex] binance_futures 29 сд. p50=292.4 мс | bybit 21 сд. p50=113.1 мс | okx 23 сд. p50=142.5 мс | binance_futures_book 451 сд. p50=143.2 мс | binance_futures_depth 91 сд. p50=143.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 41 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=42.7 мс | bitstamp 3 сд. p50=46.7 мс
10:08:06 [pm] T-114.0s Up n/a/0.01 Down 0.99/n/a ptb=82785.8 | CLOB 1205 сообщ., задержка p50/p90=60.9/66.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791626886001 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.2/2.2 мс
10:08:07 [cex] Binance 35 сд. задержка p50/p90=142.9/143.8 мс | Coinbase 8 задержка p50=78.3 мс | смещение часов +18.9 мс | lag loop p99/max=2.2/3.3 мс
10:08:07 [cex] binance_futures 30 сд. p50=292.5 мс | bybit 10 сд. p50=113.0 мс | okx 15 сд. p50=142.7 мс | binance_futures_book 402 сд. p50=143.2 мс | binance_futures_depth 90 сд. p50=143.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 49 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=43.9 мс | bitstamp 3 сд. p50=46.0 мс
10:08:16 [pm] T-104.0s Up n/a/0.01 Down 0.99/n/a ptb=82785.8 | CLOB 558 сообщ., задержка p50/p90=60.7/65.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791626896003 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/2.1 мс
10:08:17 [cex] Binance 29 сд. задержка p50/p90=143.0/143.8 мс | Coinbase 20 задержка p50=77.9 мс | смещение часов +18.9 мс | lag loop p99/max=2.1/2.1 мс
10:08:17 [cex] binance_futures 31 сд. p50=292.5 мс | bybit 12 сд. p50=112.6 мс | okx 15 сд. p50=142.3 мс | binance_futures_book 353 сд. p50=143.2 мс | binance_futures_depth 89 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 56 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=39.9 мс | bitstamp 3 сд. p50=47.6 мс
```

Представлено версией кода: 3ffd786; python 3.12.3
