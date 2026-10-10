# Состояние сервера записи

Время (UTC): 2026-10-10 00:47:36

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 17 hours, 23 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         665         883           2         551        1240
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.15 / 0.19 / 0.17

## Данные
- файлов: 953, всего 382 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 37 | 6 МБ | 0 |
| bn_book | 37 | 603 КБ | 178 |
| bnf_agg | 37 | 10 МБ | 2 |
| bnf_book | 37 | 260 МБ | 0 |
| bnf_depth5 | 37 | 19 МБ | 0 |
| bnf_liq | 35 | 27 КБ | 1176 |
| bs_trade | 37 | 700 КБ | 6 |
| by_book1 | 37 | 20 МБ | 0 |
| by_liq | 33 | 28 КБ | 5309 |
| by_trade | 37 | 7 МБ | 2 |
| cb_ticker | 37 | 6 МБ | 0 |
| clock | 37 | 29 КБ | 37 |
| clock_pm | 37 | 29 КБ | 52 |
| events | 34 | 12 КБ | 563 |
| events_pm | 37 | 17 КБ | 423 |
| health_cex | 37 | 407 КБ | 2 |
| health_feeds | 37 | 2 МБ | 2 |
| health_pm | 37 | 417 КБ | 4 |
| kr_trade | 37 | 1 МБ | 2 |
| ok_trade | 37 | 9 МБ | 0 |
| pm_depth | 37 | 9 МБ | 2 |
| pm_rtt | 37 | 270 КБ | 6 |
| pm_top | 37 | 17 МБ | 2 |
| pm_trades | 37 | 12 МБ | 2 |
| rtds | 37 | 3 МБ | 2 |
| windows | 37 | 78 КБ | 2 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 39, всего 288
- Polymarket CLOB: TCP 6, TLS 41, всего 83
- Polymarket gamma: TCP 5, TLS 46, всего 56

## Последние строки журнала записи
```
00:46:51 [pm] T-188.8s Up 0.45/0.46 Down 0.54/0.55 ptb=82482.0 | CLOB 4307 сообщ., задержка p50/p90=37.4/39.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791593211183 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.0 мс | lag loop p99/max=1.7/2.1 мс
00:46:53 [cex] Binance 16 сд. задержка p50/p90=158.9/160.0 мс | Coinbase 41 задержка p50=81.4 мс | смещение часов +22.4 мс | lag loop p99/max=2.1/2.2 мс
00:46:53 [cex] binance_futures 32 сд. p50=290.2 мс | bybit 76 сд. p50=116.6 мс | okx 69 сд. p50=154.9 мс | binance_futures_book 539 сд. p50=146.5 мс | binance_futures_depth 95 сд. p50=142.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 129 сд. p50=114.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=46.5 мс | bitstamp 3 сд. p50=48.4 мс
00:47:01 [pm] T-178.8s Up 0.33/0.34 Down 0.66/0.67 ptb=82482.0 | CLOB 3951 сообщ., задержка p50/p90=37.5/39.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791593221185 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.0 мс | lag loop p99/max=2.2/35.0 мс
00:47:03 [cex] Binance 15 сд. задержка p50/p90=158.9/159.0 мс | Coinbase 13 задержка p50=80.4 мс | смещение часов +18.7 мс | lag loop p99/max=2.2/2.2 мс
00:47:03 [cex] binance_futures 24 сд. p50=287.5 мс | bybit 3 сд. p50=115.9 мс | okx 31 сд. p50=151.1 мс | binance_futures_book 510 сд. p50=143.5 мс | binance_futures_depth 95 сд. p50=141.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 92 сд. p50=114.1 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=42.4 мс | bitstamp 1 сд. p50=46.3 мс
00:47:11 [pm] T-168.8s Up 0.32/0.33 Down 0.67/0.68 ptb=82482.0 | CLOB 4152 сообщ., задержка p50/p90=37.4/39.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791593231186 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.0 мс | lag loop p99/max=1.9/2.1 мс
00:47:13 [cex] Binance 15 сд. задержка p50/p90=155.2/156.2 мс | Coinbase 9 задержка p50=78.0 мс | смещение часов +18.7 мс | lag loop p99/max=2.2/2.2 мс
00:47:13 [cex] binance_futures 11 сд. p50=286.8 мс | bybit 10 сд. p50=112.4 мс | okx 17 сд. p50=151.0 мс | binance_futures_book 671 сд. p50=142.8 мс | binance_futures_depth 96 сд. p50=138.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 59 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 4 сд. p50=36.2 мс | bitstamp 0 сд. p50=n/a мс
00:47:21 [pm] T-158.8s Up 0.33/0.34 Down 0.66/0.67 ptb=82482.0 | CLOB 3430 сообщ., задержка p50/p90=37.5/40.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791593241188 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.0 мс | lag loop p99/max=1.8/2.1 мс
00:47:23 [cex] Binance 13 сд. задержка p50/p90=155.3/156.3 мс | Coinbase 5 задержка p50=77.0 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/2.2 мс
00:47:23 [cex] binance_futures 22 сд. p50=286.5 мс | bybit 15 сд. p50=112.4 мс | okx 13 сд. p50=150.9 мс | binance_futures_book 731 сд. p50=142.8 мс | binance_futures_depth 96 сд. p50=138.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 56 сд. p50=110.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 1 сд. p50=36.4 мс | bitstamp 0 сд. p50=n/a мс
00:47:31 [pm] T-148.8s Up 0.28/0.29 Down 0.71/0.72 ptb=82482.0 | CLOB 4171 сообщ., задержка p50/p90=38.2/93.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791593251190 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.0 мс | lag loop p99/max=1.4/1.5 мс
00:47:33 [cex] Binance 13 сд. задержка p50/p90=155.2/155.5 мс | Coinbase 9 задержка p50=77.3 мс | смещение часов +18.7 мс | lag loop p99/max=2.3/2.4 мс
00:47:33 [cex] binance_futures 17 сд. p50=286.5 мс | bybit 25 сд. p50=112.9 мс | okx 21 сд. p50=150.9 мс | binance_futures_book 642 сд. p50=142.8 мс | binance_futures_depth 95 сд. p50=138.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 66 сд. p50=110.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 11 сд. p50=37.8 мс | bitstamp 1 сд. p50=49.6 мс
```

Представлено версией кода: 7642f87; python 3.12.3
