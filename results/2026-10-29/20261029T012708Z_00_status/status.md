# Состояние сервера записи

Время (UTC): 2026-10-29 01:27:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 18 hours, 3 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 12 ГБ из 57 ГБ, свободно 45 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         608         679           1         793        1297
Swap:           2047         304        1743
```
- нагрузка CPU (1/5/15 мин): 0.39 / 0.28 / 0.21

## Данные
- файлов: 5807, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 34 МБ | 1 |
| bn_book | 242 | 3 МБ | 3 |
| bnf_agg | 242 | 50 МБ | 1 |
| bnf_book | 61 | 394 МБ | 1 |
| bnf_liq | 210 | 138 КБ | 195 |
| by_book1 | 242 | 109 МБ | 1 |
| by_liq | 224 | 99 КБ | 1009 |
| by_trade | 242 | 34 МБ | 1 |
| bys_book1 | 242 | 83 МБ | 1 |
| bys_trade | 242 | 33 МБ | 3 |
| cb_ticker | 242 | 32 МБ | 1 |
| clock | 242 | 188 КБ | 35 |
| clock_pm | 242 | 188 КБ | 8 |
| events | 231 | 73 КБ | 347 |
| events_pm | 241 | 83 КБ | 508 |
| health_cex | 242 | 2 МБ | 3 |
| health_feeds | 242 | 7 МБ | 3 |
| health_pm | 242 | 3 МБ | 6 |
| ok_trade | 242 | 43 МБ | 1 |
| pm_depth | 242 | 50 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 2 |
| pm_top | 242 | 101 МБ | 0 |
| pm_trades | 242 | 71 МБ | 0 |
| rtds | 242 | 16 МБ | 0 |
| windows | 242 | 499 КБ | 214 |

Дни с данными: 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 37, всего 287
- Polymarket CLOB: TCP 5, TLS 40, всего 83
- Polymarket gamma: TCP 4, TLS 37, всего 67

## Последние строки журнала записи
```
01:26:21 [pm] T-218.9s Up 0.91/0.92 Down 0.08/0.09 ptb=80791.0 | CLOB 2895 сообщ., задержка p50/p90=39.8/47.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793237181107 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=1.8/2.1 мс
01:26:24 [cex] Binance 61 сд. задержка p50/p90=144.6/145.8 мс | Coinbase 40 задержка p50=92.9 мс | смещение часов +20.4 мс | lag loop p99/max=2.1/6.5 мс
01:26:24 [cex] binance_futures 27 сд. p50=294.7 мс | bybit 33 сд. p50=113.4 мс | bybit_book 153 сд. p50=112.0 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 41 сд. p50=111.9 мс | okx 17 сд. p50=157.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2309 сд. p50=145.6 мс
01:26:31 [pm] T-208.9s Up 0.88/0.89 Down 0.11/0.12 ptb=80791.0 | CLOB 3925 сообщ., задержка p50/p90=39.8/146.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793237191108 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=2.1/2.2 мс
01:26:34 [cex] Binance 104 сд. задержка p50/p90=145.2/145.9 мс | Coinbase 44 задержка p50=95.0 мс | смещение часов +18.1 мс | lag loop p99/max=2.1/2.3 мс
01:26:34 [cex] binance_futures 82 сд. p50=147.4 мс | bybit 114 сд. p50=114.0 мс | bybit_book 189 сд. p50=111.9 мс | bybit_spot 91 сд. p50=116.5 мс | bybit_spot_book 77 сд. p50=111.7 мс | okx 79 сд. p50=158.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2653 сд. p50=145.5 мс
01:26:41 [pm] T-198.9s Up 0.89/0.90 Down 0.10/0.11 ptb=80791.0 | CLOB 2601 сообщ., задержка p50/p90=40.3/52.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793237201110 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=2.2/2.3 мс
01:26:44 [cex] Binance 14 сд. задержка p50/p90=142.4/143.1 мс | Coinbase 87 задержка p50=91.9 мс | смещение часов +18.1 мс | lag loop p99/max=1.9/1.9 мс
01:26:44 [cex] binance_futures 71 сд. p50=147.3 мс | bybit 32 сд. p50=113.5 мс | bybit_book 138 сд. p50=109.8 мс | bybit_spot 58 сд. p50=114.8 мс | bybit_spot_book 55 сд. p50=109.6 мс | okx 109 сд. p50=157.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1463 сд. p50=146.5 мс
01:26:51 [pm] T-188.9s Up 0.77/0.78 Down 0.22/0.23 ptb=80791.0 | CLOB 2987 сообщ., задержка p50/p90=40.0/56.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793237211111 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=2.1/2.1 мс
01:26:54 [cex] Binance 168 сд. задержка p50/p90=143.0/145.1 мс | Coinbase 98 задержка p50=93.3 мс | смещение часов +18.1 мс | lag loop p99/max=3.1/4.4 мс
01:26:54 [cex] binance_futures 164 сд. p50=146.8 мс | bybit 194 сд. p50=114.5 мс | bybit_book 276 сд. p50=109.8 мс | bybit_spot 222 сд. p50=113.6 мс | bybit_spot_book 167 сд. p50=109.6 мс | okx 181 сд. p50=156.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 8812 сд. p50=145.7 мс
01:27:01 [pm] T-178.9s Up 0.87/0.88 Down 0.12/0.13 ptb=80791.0 | CLOB 4975 сообщ., задержка p50/p90=41.6/68.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793237221112 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=2.3/7.0 мс
01:27:04 [cex] Binance 56 сд. задержка p50/p90=143.6/145.4 мс | Coinbase 42 задержка p50=91.6 мс | смещение часов +18.1 мс | lag loop p99/max=2.1/3.6 мс
01:27:04 [cex] binance_futures 108 сд. p50=147.5 мс | bybit 73 сд. p50=111.6 мс | bybit_book 247 сд. p50=109.7 мс | bybit_spot 373 сд. p50=113.1 мс | bybit_spot_book 110 сд. p50=109.6 мс | okx 87 сд. p50=156.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 7160 сд. p50=144.7 мс
```

Представлено версией кода: 65c4468; python 3.12.3
