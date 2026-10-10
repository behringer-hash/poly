# Состояние сервера записи

Время (UTC): 2026-10-10 12:15:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 3 days, 4 hours, 51 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         680        1011           2         422        1225
Swap:           2047          44        2003
```
- нагрузка CPU (1/5/15 мин): 0.03 / 0.10 / 0.12

## Данные
- файлов: 1259, всего 383 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 49 | 6 МБ | 1 |
| bn_book | 49 | 622 КБ | 28 |
| bnf_agg | 49 | 10 МБ | 1 |
| bnf_book | 49 | 253 МБ | 1 |
| bnf_depth5 | 49 | 19 МБ | 1 |
| bnf_liq | 43 | 30 КБ | 5404 |
| bs_trade | 49 | 745 КБ | 7 |
| by_book1 | 49 | 20 МБ | 1 |
| by_liq | 43 | 29 КБ | 4984 |
| by_trade | 49 | 7 МБ | 1 |
| cb_ticker | 49 | 6 МБ | 3 |
| clock | 49 | 37 КБ | 42 |
| clock_pm | 49 | 37 КБ | 59 |
| events | 46 | 16 КБ | 515 |
| events_pm | 49 | 21 КБ | 840 |
| health_cex | 49 | 515 КБ | 9 |
| health_feeds | 49 | 2 МБ | 9 |
| health_pm | 49 | 528 КБ | 10 |
| kr_trade | 49 | 2 МБ | 9 |
| ok_trade | 49 | 9 МБ | 1 |
| pm_depth | 49 | 10 МБ | 2 |
| pm_rtt | 49 | 327 КБ | 4 |
| pm_top | 49 | 20 МБ | 2 |
| pm_trades | 49 | 14 МБ | 2 |
| rtds | 49 | 3 МБ | 2 |
| windows | 49 | 99 КБ | 252 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 37, всего 286
- Polymarket CLOB: TCP 6, TLS 43, всего 92
- Polymarket gamma: TCP 5, TLS 38, всего 50

## Последние строки журнала записи
```
12:14:38 [cex] Binance 128 сд. задержка p50/p90=144.7/145.0 мс | Coinbase 14 задержка p50=79.6 мс | смещение часов +18.6 мс | lag loop p99/max=2.1/2.2 мс
12:14:38 [cex] binance_futures 47 сд. p50=293.4 мс | bybit 4 сд. p50=114.8 мс | okx 20 сд. p50=143.8 мс | binance_futures_book 485 сд. p50=145.3 мс | binance_futures_depth 84 сд. p50=146.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 126 сд. p50=112.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=38.8 мс | bitstamp 0 сд. p50=n/a мс
12:14:45 [pm] окно btc-updown-5m-1791634500 (2026-10-10 12:15:00 UTC): Bitcoin Up or Down - October 10, 8:15AM-8:20AM ET
12:14:47 [pm] T- 12.9s Up 0.99/n/a Down n/a/0.01 ptb=82796.2 | CLOB 1026 сообщ., задержка p50/p90=40.3/73.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791634487093 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=2.2/27.7 мс
12:14:48 [cex] Binance 217 сд. задержка p50/p90=143.1/148.1 мс | Coinbase 32 задержка p50=77.9 мс | смещение часов +18.6 мс | lag loop p99/max=2.1/5.6 мс
12:14:48 [cex] binance_futures 126 сд. p50=145.2 мс | bybit 65 сд. p50=115.6 мс | okx 87 сд. p50=143.1 мс | binance_futures_book 2265 сд. p50=144.3 мс | binance_futures_depth 85 сд. p50=144.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 102 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 11 сд. p50=37.8 мс | bitstamp 2 сд. p50=64.3 мс
12:14:57 [pm] T-  2.9s Up 0.99/n/a Down n/a/0.01 ptb=82796.2 | CLOB 1207 сообщ., задержка p50/p90=39.4/42.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791634497094 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=2.0/2.2 мс
12:14:58 [cex] Binance 63 сд. задержка p50/p90=159.4/159.8 мс | Coinbase 17 задержка p50=78.0 мс | смещение часов +18.6 мс | lag loop p99/max=2.1/2.2 мс
12:14:58 [cex] binance_futures 15 сд. p50=291.5 мс | bybit 2 сд. p50=113.1 мс | okx 21 сд. p50=142.1 мс | binance_futures_book 444 сд. p50=143.8 мс | binance_futures_depth 74 сд. p50=144.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 84 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 12 сд. p50=46.9 мс | bitstamp 2 сд. p50=46.0 мс
12:15:07 [pm] T-292.9s Up 0.27/0.28 Down 0.72/0.73 ptb=82809.5 | CLOB 2322 сообщ., задержка p50/p90=39.0/41.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791634507095 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.7 мс | lag loop p99/max=2.8/7.8 мс
12:15:08 [cex] Binance 30 сд. задержка p50/p90=143.6/150.5 мс | Coinbase 8 задержка p50=78.6 мс | смещение часов +18.6 мс | lag loop p99/max=5.6/26.9 мс
12:15:08 [cex] binance_futures 14 сд. p50=291.4 мс | bybit 4 сд. p50=112.9 мс | okx 28 сд. p50=142.1 мс | binance_futures_book 668 сд. p50=143.8 мс | binance_futures_depth 87 сд. p50=144.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 121 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=40.6 мс | bitstamp 1 сд. p50=47.4 мс
12:15:17 [pm] T-282.9s Up 0.34/0.35 Down 0.65/0.66 ptb=82809.5 | CLOB 3617 сообщ., задержка p50/p90=38.8/39.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791634517097 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.8 мс | lag loop p99/max=1.3/1.4 мс
12:15:18 [cex] Binance 14 сд. задержка p50/p90=142.8/143.1 мс | Coinbase 5 задержка p50=77.2 мс | смещение часов +18.6 мс | lag loop p99/max=2.1/2.2 мс
12:15:18 [cex] binance_futures 11 сд. p50=292.3 мс | bybit 6 сд. p50=112.7 мс | okx 219 сд. p50=142.2 мс | binance_futures_book 313 сд. p50=143.7 мс | binance_futures_depth 75 сд. p50=144.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 98 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=39.7 мс | bitstamp 1 сд. p50=51.0 мс
```

Представлено версией кода: 69087ca; python 3.12.3
