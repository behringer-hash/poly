# Состояние сервера записи

Время (UTC): 2026-10-16 01:48:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 18 hours, 24 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         691         307           2        1156        1214
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.24 / 0.17 / 0.17

## Данные
- файлов: 4558, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 182 | 25 МБ | 0 |
| bn_book | 182 | 2 МБ | 0 |
| bnf_agg | 182 | 39 МБ | 0 |
| bnf_book | 118 | 557 МБ | 230412 |
| bnf_depth5 | 118 | 41 МБ | 230488 |
| bnf_liq | 164 | 112 КБ | 130 |
| bs_trade | 118 | 1 МБ | 230408 |
| by_book1 | 182 | 82 МБ | 0 |
| by_liq | 162 | 93 КБ | 628 |
| by_trade | 182 | 26 МБ | 0 |
| bys_book1 | 66 | 28 МБ | 0 |
| bys_trade | 66 | 12 МБ | 0 |
| cb_ticker | 182 | 23 МБ | 0 |
| clock | 182 | 141 КБ | 55 |
| clock_pm | 182 | 141 КБ | 52 |
| events | 171 | 56 КБ | 261 |
| events_pm | 182 | 65 КБ | 1998 |
| health_cex | 182 | 2 МБ | 4 |
| health_feeds | 182 | 6 МБ | 4 |
| health_pm | 182 | 2 МБ | 10 |
| kr_trade | 118 | 3 МБ | 230408 |
| ok_trade | 181 | 35 МБ | 0 |
| pm_depth | 182 | 37 МБ | 2 |
| pm_rtt | 182 | 1 МБ | 2 |
| pm_top | 182 | 76 МБ | 2 |
| pm_trades | 182 | 55 МБ | 2 |
| rtds | 182 | 12 МБ | 2 |
| windows | 182 | 377 КБ | 34 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 41, всего 291
- Polymarket CLOB: TCP 5, TLS 42, всего 87
- Polymarket gamma: TCP 5, TLS 47, всего 57

## Последние строки журнала записи
```
01:47:53 [cex] Binance 34 сд. задержка p50/p90=146.6/147.0 мс | Coinbase 35 задержка p50=82.0 мс | смещение часов +22.2 мс | lag loop p99/max=2.1/2.2 мс
01:47:53 [cex] binance_futures 55 сд. p50=173.0 мс | bybit 66 сд. p50=116.1 мс | bybit_book 168 сд. p50=113.9 мс | bybit_spot 38 сд. p50=116.5 мс | bybit_spot_book 161 сд. p50=113.7 мс | okx 38 сд. p50=160.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:47:57 [pm] T-122.1s Up 0.42/0.43 Down 0.57/0.58 ptb=82069.7 | CLOB 7920 сообщ., задержка p50/p90=43.8/46.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792115277854 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.1 мс | lag loop p99/max=1.8/2.1 мс
01:48:03 [cex] Binance 30 сд. задержка p50/p90=146.5/147.7 мс | Coinbase 15 задержка p50=82.4 мс | смещение часов +22.2 мс | lag loop p99/max=2.2/2.3 мс
01:48:03 [cex] binance_futures 60 сд. p50=148.7 мс | bybit 36 сд. p50=117.0 мс | bybit_book 113 сд. p50=114.0 мс | bybit_spot 77 сд. p50=116.7 мс | bybit_spot_book 50 сд. p50=113.9 мс | okx 38 сд. p50=160.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:48:07 [pm] T-112.1s Up 0.36/0.37 Down 0.63/0.64 ptb=82069.7 | CLOB 8515 сообщ., задержка p50/p90=44.0/46.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792115287855 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.0 мс | lag loop p99/max=4.2/8.0 мс
01:48:13 [cex] Binance 19 сд. задержка p50/p90=146.0/146.9 мс | Coinbase 32 задержка p50=82.1 мс | смещение часов +22.2 мс | lag loop p99/max=2.0/2.1 мс
01:48:13 [cex] binance_futures 19 сд. p50=295.7 мс | bybit 26 сд. p50=116.0 мс | bybit_book 142 сд. p50=113.9 мс | bybit_spot 1 сд. p50=115.6 мс | bybit_spot_book 34 сд. p50=113.9 мс | okx 40 сд. p50=160.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:48:17 [pm] T-102.1s Up 0.35/0.36 Down 0.64/0.65 ptb=82069.7 | CLOB 9651 сообщ., задержка p50/p90=43.5/44.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792115297857 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.0 мс | lag loop p99/max=1.2/1.2 мс
01:48:23 [cex] Binance 18 сд. задержка p50/p90=146.1/147.2 мс | Coinbase 17 задержка p50=85.9 мс | смещение часов +22.2 мс | lag loop p99/max=2.1/2.2 мс
01:48:23 [cex] binance_futures 21 сд. p50=295.7 мс | bybit 37 сд. p50=115.9 мс | bybit_book 92 сд. p50=114.0 мс | bybit_spot 9 сд. p50=115.5 мс | bybit_spot_book 54 сд. p50=113.9 мс | okx 30 сд. p50=160.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:48:27 [pm] T- 92.1s Up 0.36/0.37 Down 0.63/0.64 ptb=82069.7 | CLOB 7864 сообщ., задержка p50/p90=43.7/45.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792115307858 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.9 мс | lag loop p99/max=1.9/2.1 мс
01:48:33 [cex] Binance 60 сд. задержка p50/p90=146.1/147.4 мс | Coinbase 46 задержка p50=82.5 мс | смещение часов +22.2 мс | lag loop p99/max=2.0/2.0 мс
01:48:33 [cex] binance_futures 87 сд. p50=147.9 мс | bybit 121 сд. p50=116.1 мс | bybit_book 141 сд. p50=113.9 мс | bybit_spot 80 сд. p50=116.5 мс | bybit_spot_book 75 сд. p50=113.7 мс | okx 58 сд. p50=160.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:48:37 [pm] T- 82.1s Up 0.12/0.13 Down 0.87/0.88 ptb=82069.7 | CLOB 8564 сообщ., задержка p50/p90=44.0/60.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792115317859 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.8/1.9 мс
```

Представлено версией кода: ec1316a; python 3.12.3
