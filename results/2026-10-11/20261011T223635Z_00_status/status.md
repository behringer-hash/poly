# Состояние сервера записи

Время (UTC): 2026-10-11 22:36:36

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 4 days, 15 hours, 12 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         696         834           1         583        1209
Swap:           2047          72        1975
```
- нагрузка CPU (1/5/15 мин): 0.39 / 0.29 / 0.23

## Данные
- файлов: 2125, всего 567 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 83 | 9 МБ | 1 |
| bn_book | 83 | 777 КБ | 28 |
| bnf_agg | 83 | 14 МБ | 1 |
| bnf_book | 83 | 366 МБ | 1 |
| bnf_depth5 | 83 | 31 МБ | 1 |
| bnf_liq | 70 | 38 КБ | 164 |
| bs_trade | 83 | 1 МБ | 1 |
| by_book1 | 83 | 29 МБ | 1 |
| by_liq | 66 | 36 КБ | 510 |
| by_trade | 83 | 9 МБ | 1 |
| cb_ticker | 83 | 8 МБ | 1 |
| clock | 83 | 64 КБ | 21 |
| clock_pm | 83 | 64 КБ | 36 |
| events | 80 | 28 КБ | 550 |
| events_pm | 83 | 32 КБ | 1002 |
| health_cex | 83 | 875 КБ | 1 |
| health_feeds | 83 | 3 МБ | 1 |
| health_pm | 83 | 901 КБ | 0 |
| kr_trade | 83 | 2 МБ | 5 |
| ok_trade | 83 | 12 МБ | 1 |
| pm_depth | 83 | 17 МБ | 0 |
| pm_rtt | 83 | 568 КБ | 4 |
| pm_top | 83 | 33 МБ | 0 |
| pm_trades | 83 | 23 МБ | 0 |
| rtds | 83 | 5 МБ | 0 |
| windows | 83 | 171 КБ | 242 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 38, всего 287
- Polymarket CLOB: TCP 5, TLS 37, всего 82
- Polymarket gamma: TCP 5, TLS 43, всего 53

## Последние строки журнала записи
```
22:35:54 [cex] Binance 101 сд. задержка p50/p90=146.6/153.2 мс | Coinbase 22 задержка p50=83.6 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/2.2 мс
22:35:54 [cex] binance_futures 108 сд. p50=143.9 мс | bybit 99 сд. p50=117.0 мс | okx 80 сд. p50=155.1 мс | binance_futures_book 4276 сд. p50=144.3 мс | binance_futures_depth 87 сд. p50=144.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 164 сд. p50=110.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 9 сд. p50=39.7 мс | bitstamp 15 сд. p50=45.4 мс
22:35:54 [pm] T-245.2s Up 0.33/0.34 Down 0.66/0.67 ptb=83571.2 | CLOB 9964 сообщ., задержка p50/p90=72.8/118.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791758154770 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.6 мс | lag loop p99/max=1.9/2.2 мс
22:36:04 [cex] Binance 24 сд. задержка p50/p90=144.1/148.7 мс | Coinbase 40 задержка p50=81.0 мс | смещение часов +19.0 мс | lag loop p99/max=2.1/4.8 мс
22:36:04 [cex] binance_futures 33 сд. p50=258.4 мс | bybit 15 сд. p50=113.8 мс | okx 14 сд. p50=153.2 мс | binance_futures_book 2064 сд. p50=143.6 мс | binance_futures_depth 89 сд. p50=144.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 103 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=46.4 мс | bitstamp 12 сд. p50=46.9 мс
22:36:04 [pm] T-235.2s Up 0.44/0.45 Down 0.55/0.56 ptb=83571.2 | CLOB 5563 сообщ., задержка p50/p90=35.4/45.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791758164772 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.6 мс | lag loop p99/max=1.9/2.2 мс
22:36:14 [cex] Binance 50 сд. задержка p50/p90=144.1/144.4 мс | Coinbase 20 задержка p50=80.0 мс | смещение часов +19.7 мс | lag loop p99/max=2.1/3.2 мс
22:36:14 [cex] binance_futures 82 сд. p50=144.4 мс | bybit 100 сд. p50=114.3 мс | okx 57 сд. p50=153.6 мс | binance_futures_book 4810 сд. p50=143.5 мс | binance_futures_depth 87 сд. p50=144.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 103 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=43.4 мс | bitstamp 11 сд. p50=45.2 мс
22:36:14 [pm] T-225.2s Up 0.53/0.54 Down 0.46/0.47 ptb=83571.2 | CLOB 7128 сообщ., задержка p50/p90=34.8/37.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791758174774 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.5 мс | lag loop p99/max=2.0/3.1 мс
22:36:24 [cex] Binance 41 сд. задержка p50/p90=144.3/144.6 мс | Coinbase 18 задержка p50=80.9 мс | смещение часов +19.7 мс | lag loop p99/max=2.2/2.2 мс
22:36:24 [cex] binance_futures 12 сд. p50=292.9 мс | bybit 5 сд. p50=113.1 мс | okx 40 сд. p50=153.7 мс | binance_futures_book 750 сд. p50=144.1 мс | binance_futures_depth 82 сд. p50=144.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 51 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=63.9 мс | bitstamp 13 сд. p50=46.8 мс
22:36:24 [pm] T-215.2s Up 0.60/0.61 Down 0.39/0.40 ptb=83571.2 | CLOB 4228 сообщ., задержка p50/p90=35.0/39.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791758184775 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.5 мс | lag loop p99/max=1.9/1.9 мс
22:36:34 [cex] Binance 19 сд. задержка p50/p90=144.2/145.5 мс | Coinbase 14 задержка p50=81.4 мс | смещение часов +19.7 мс | lag loop p99/max=2.1/2.2 мс
22:36:34 [cex] binance_futures 17 сд. p50=293.1 мс | bybit 8 сд. p50=113.9 мс | okx 19 сд. p50=153.5 мс | binance_futures_book 747 сд. p50=144.1 мс | binance_futures_depth 90 сд. p50=144.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 59 сд. p50=111.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=43.0 мс | bitstamp 11 сд. p50=46.2 мс
22:36:34 [pm] T-205.2s Up 0.56/0.57 Down 0.43/0.44 ptb=83571.2 | CLOB 4848 сообщ., задержка p50/p90=35.4/46.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791758194776 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.6 мс | lag loop p99/max=1.2/2.1 мс
```

Представлено версией кода: 69087ca; python 3.12.3
