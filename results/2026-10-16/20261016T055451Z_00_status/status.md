# Состояние сервера записи

Время (UTC): 2026-10-16 05:54:51

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 22 hours, 30 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         729         297           2        1168        1176
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.24 / 0.20 / 0.18

## Данные
- файлов: 4652, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 186 | 26 МБ | 4 |
| bn_book | 186 | 2 МБ | 51 |
| bnf_agg | 186 | 40 МБ | 2 |
| bnf_book | 118 | 557 МБ | 245185 |
| bnf_depth5 | 118 | 41 МБ | 245262 |
| bnf_liq | 167 | 114 КБ | 5213 |
| bs_trade | 118 | 1 МБ | 245181 |
| by_book1 | 186 | 84 МБ | 2 |
| by_liq | 165 | 95 КБ | 2957 |
| by_trade | 186 | 26 МБ | 4 |
| bys_book1 | 70 | 31 МБ | 2 |
| bys_trade | 70 | 12 МБ | 6 |
| cb_ticker | 186 | 24 МБ | 2 |
| clock | 186 | 144 КБ | 14 |
| clock_pm | 186 | 145 КБ | 16 |
| events | 175 | 57 КБ | 317 |
| events_pm | 186 | 66 КБ | 830 |
| health_cex | 186 | 2 МБ | 6 |
| health_feeds | 186 | 7 МБ | 6 |
| health_pm | 186 | 2 МБ | 1 |
| kr_trade | 118 | 3 МБ | 245181 |
| ok_trade | 185 | 35 МБ | 2 |
| pm_depth | 186 | 38 МБ | 1 |
| pm_rtt | 186 | 1 МБ | 3 |
| pm_top | 186 | 78 МБ | 1 |
| pm_trades | 186 | 56 МБ | 1 |
| rtds | 186 | 12 МБ | 1 |
| windows | 186 | 386 КБ | 198 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 36, всего 286
- Polymarket CLOB: TCP 6, TLS 40, всего 80
- Polymarket gamma: TCP 5, TLS 38, всего 55

## Последние строки журнала записи
```
05:54:05 [cex] binance_futures 76 сд. p50=149.1 мс | bybit 95 сд. p50=113.2 мс | bybit_book 154 сд. p50=110.7 мс | bybit_spot 107 сд. p50=114.0 мс | bybit_spot_book 131 сд. p50=110.4 мс | okx 95 сд. p50=146.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
05:54:09 [pm] T- 50.1s Up 0.99/n/a Down n/a/0.01 ptb=82041.7 | CLOB 992 сообщ., задержка p50/p90=59.1/61.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792130049909 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.2/18.9 мс
05:54:15 [cex] Binance 15 сд. задержка p50/p90=143.0/144.0 мс | Coinbase 35 задержка p50=77.9 мс | смещение часов +18.7 мс | lag loop p99/max=2.0/2.1 мс
05:54:15 [cex] binance_futures 19 сд. p50=292.3 мс | bybit 29 сд. p50=113.2 мс | bybit_book 107 сд. p50=110.7 мс | bybit_spot 2 сд. p50=113.1 мс | bybit_spot_book 57 сд. p50=110.3 мс | okx 5 сд. p50=144.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
05:54:19 [pm] T- 40.1s Up 1.00/n/a Down n/a/0.00 ptb=82041.7 | CLOB 959 сообщ., задержка p50/p90=59.2/61.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792130059910 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.9/2.1 мс
05:54:25 [cex] Binance 15 сд. задержка p50/p90=143.0/143.1 мс | Coinbase 65 задержка p50=77.6 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/2.1 мс
05:54:25 [cex] binance_futures 30 сд. p50=291.8 мс | bybit 23 сд. p50=112.5 мс | bybit_book 94 сд. p50=110.7 мс | bybit_spot 75 сд. p50=113.0 мс | bybit_spot_book 114 сд. p50=110.3 мс | okx 7 сд. p50=144.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
05:54:29 [pm] T- 30.1s Up 1.00/n/a Down n/a/0.00 ptb=82041.7 | CLOB 626 сообщ., задержка p50/p90=59.0/60.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792130069911 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.1/2.2 мс
05:54:35 [cex] Binance 16 сд. задержка p50/p90=143.1/144.3 мс | Coinbase 42 задержка p50=77.8 мс | смещение часов +18.7 мс | lag loop p99/max=2.2/2.2 мс
05:54:35 [cex] binance_futures 45 сд. p50=143.1 мс | bybit 8 сд. p50=112.8 мс | bybit_book 101 сд. p50=110.7 мс | bybit_spot 3 сд. p50=113.1 мс | bybit_spot_book 140 сд. p50=110.3 мс | okx 40 сд. p50=145.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
05:54:39 [pm] T- 20.1s Up 1.00/n/a Down n/a/0.00 ptb=82041.7 | CLOB 615 сообщ., задержка p50/p90=59.5/60.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792130079911 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.2/2.3 мс
05:54:45 [cex] Binance 12 сд. задержка p50/p90=142.3/142.5 мс | Coinbase 40 задержка p50=77.2 мс | смещение часов +18.0 мс | lag loop p99/max=2.1/2.2 мс
05:54:45 [cex] binance_futures 20 сд. p50=291.1 мс | bybit 5 сд. p50=111.4 мс | bybit_book 75 сд. p50=110.0 мс | bybit_spot 4 сд. p50=112.7 мс | bybit_spot_book 158 сд. p50=109.6 мс | okx 14 сд. p50=143.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
05:54:45 [pm] окно btc-updown-5m-1792130100 (2026-10-16 05:55:00 UTC): Bitcoin Up or Down - October 16, 1:55AM-2:00AM ET
05:54:49 [pm] T- 10.1s Up 1.00/n/a Down n/a/0.00 ptb=82041.7 | CLOB 877 сообщ., задержка p50/p90=42.0/60.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792130089913 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.1/10.9 мс
```

Представлено версией кода: ec1316a; python 3.12.3
