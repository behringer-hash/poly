# Состояние сервера записи

Время (UTC): 2026-10-11 15:18:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 4 days, 7 hours, 54 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         692         921           1         500        1213
Swap:           2047          62        1985
```
- нагрузка CPU (1/5/15 мин): 0.07 / 0.14 / 0.13

## Данные
- файлов: 1944, всего 470 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 76 | 8 МБ | 0 |
| bn_book | 76 | 688 КБ | 2 |
| bnf_agg | 76 | 12 МБ | 0 |
| bnf_book | 76 | 293 МБ | 0 |
| bnf_depth5 | 76 | 27 МБ | 0 |
| bnf_liq | 64 | 35 КБ | 798 |
| bs_trade | 76 | 917 КБ | 8 |
| by_book1 | 76 | 26 МБ | 0 |
| by_liq | 59 | 33 КБ | 11061 |
| by_trade | 76 | 8 МБ | 0 |
| cb_ticker | 76 | 7 МБ | 0 |
| clock | 76 | 58 КБ | 51 |
| clock_pm | 76 | 58 КБ | 5 |
| events | 73 | 25 КБ | 187 |
| events_pm | 76 | 29 КБ | 485 |
| health_cex | 76 | 792 КБ | 6 |
| health_feeds | 76 | 3 МБ | 6 |
| health_pm | 76 | 816 КБ | 5 |
| kr_trade | 76 | 2 МБ | 0 |
| ok_trade | 76 | 11 МБ | 0 |
| pm_depth | 76 | 15 МБ | 1 |
| pm_rtt | 76 | 509 КБ | 1 |
| pm_top | 76 | 29 МБ | 1 |
| pm_trades | 76 | 21 МБ | 1 |
| rtds | 76 | 5 МБ | 1 |
| windows | 76 | 156 КБ | 54 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 39, всего 288
- Polymarket CLOB: TCP 5, TLS 47, всего 91
- Polymarket gamma: TCP 5, TLS 38, всего 52

## Последние строки журнала записи
```
15:17:40 [cex] Binance 43 сд. задержка p50/p90=145.5/147.7 мс | Coinbase 10 задержка p50=81.6 мс | смещение часов +18.6 мс | lag loop p99/max=2.0/2.1 мс
15:17:40 [cex] binance_futures 42 сд. p50=144.7 мс | bybit 3 сд. p50=114.6 мс | okx 16 сд. p50=154.1 мс | binance_futures_book 603 сд. p50=144.8 мс | binance_futures_depth 76 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 32 сд. p50=112.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=45.5 мс | bitstamp 1 сд. p50=47.4 мс
15:17:40 [pm] T-139.1s Up 0.05/0.06 Down 0.94/0.95 ptb=83049.6 | CLOB 2678 сообщ., задержка p50/p90=36.1/44.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791731860905 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.1/2.1 мс
15:17:50 [cex] Binance 19 сд. задержка p50/p90=143.8/144.9 мс | Coinbase 53 задержка p50=80.5 мс | смещение часов +18.6 мс | lag loop p99/max=2.1/2.1 мс
15:17:50 [cex] binance_futures 75 сд. p50=154.2 мс | bybit 48 сд. p50=113.0 мс | okx 16 сд. p50=153.2 мс | binance_futures_book 2186 сд. p50=143.2 мс | binance_futures_depth 96 сд. p50=142.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 73 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=42.2 мс | bitstamp 1 сд. p50=47.2 мс
15:17:50 [pm] T-129.1s Up 0.15/0.16 Down 0.84/0.85 ptb=83049.6 | CLOB 4485 сообщ., задержка p50/p90=37.0/351.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791731870906 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.1/2.1 мс
15:18:00 [cex] Binance 23 сд. задержка p50/p90=143.8/144.8 мс | Coinbase 11 задержка p50=80.3 мс | смещение часов +18.6 мс | lag loop p99/max=2.1/2.1 мс
15:18:00 [cex] binance_futures 10 сд. p50=292.1 мс | bybit 8 сд. p50=112.9 мс | okx 9 сд. p50=152.2 мс | binance_futures_book 551 сд. p50=143.0 мс | binance_futures_depth 88 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 53 сд. p50=110.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=42.6 мс | bitstamp 2 сд. p50=50.2 мс
15:18:00 [pm] T-119.1s Up 0.09/0.10 Down 0.90/0.91 ptb=83049.6 | CLOB 2662 сообщ., задержка p50/p90=35.9/39.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791731880908 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=1.8/2.0 мс
15:18:10 [cex] Binance 21 сд. задержка p50/p90=143.8/145.0 мс | Coinbase 29 задержка p50=79.8 мс | смещение часов +18.6 мс | lag loop p99/max=2.1/2.1 мс
15:18:10 [cex] binance_futures 10 сд. p50=292.2 мс | bybit 2 сд. p50=112.4 мс | okx 13 сд. p50=152.3 мс | binance_futures_book 822 сд. p50=143.0 мс | binance_futures_depth 92 сд. p50=143.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 34 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 8 сд. p50=40.4 мс | bitstamp 0 сд. p50=n/a мс
15:18:10 [pm] T-109.1s Up 0.09/0.10 Down 0.90/0.91 ptb=83049.6 | CLOB 4631 сообщ., задержка p50/p90=35.8/39.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791731890909 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=2.1/2.2 мс
15:18:20 [cex] Binance 33 сд. задержка p50/p90=143.9/144.8 мс | Coinbase 6 задержка p50=81.6 мс | смещение часов +18.6 мс | lag loop p99/max=2.0/2.2 мс
15:18:20 [cex] binance_futures 12 сд. p50=292.3 мс | bybit 61 сд. p50=115.2 мс | okx 4 сд. p50=152.5 мс | binance_futures_book 726 сд. p50=143.0 мс | binance_futures_depth 94 сд. p50=142.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 108 сд. p50=110.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=41.1 мс | bitstamp 6 сд. p50=54.4 мс
15:18:20 [pm] T- 99.1s Up 0.07/0.08 Down 0.92/0.93 ptb=83049.6 | CLOB 4179 сообщ., задержка p50/p90=35.9/46.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791731900910 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=2.0/2.0 мс
```

Представлено версией кода: 69087ca; python 3.12.3
