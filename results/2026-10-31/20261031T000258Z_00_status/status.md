# Состояние сервера записи

Время (UTC): 2026-10-31 00:02:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 2 days, 16 hours, 39 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 13 ГБ из 57 ГБ, свободно 44 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         673         601           1         819        1232
Swap:           2047         318        1729
```
- нагрузка CPU (1/5/15 мин): 0.65 / 0.41 / 0.32

## Данные
- файлов: 5869, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 243 | 37 МБ | 1 |
| bn_book | 243 | 3 МБ | 7 |
| bnf_agg | 243 | 52 МБ | 1 |
| bnf_book | 108 | 755 МБ | 0 |
| bnf_liq | 212 | 149 КБ | 106 |
| by_book1 | 243 | 114 МБ | 1 |
| by_liq | 226 | 118 КБ | 122 |
| by_trade | 243 | 35 МБ | 1 |
| bys_book1 | 243 | 84 МБ | 1 |
| bys_trade | 243 | 34 МБ | 3 |
| cb_ticker | 243 | 33 МБ | 1 |
| clock | 243 | 188 КБ | 42 |
| clock_pm | 243 | 188 КБ | 17 |
| events | 223 | 71 КБ | 1111 |
| events_pm | 241 | 87 КБ | 392 |
| health_cex | 243 | 3 МБ | 1 |
| health_feeds | 243 | 8 МБ | 1 |
| health_pm | 243 | 3 МБ | 1 |
| ok_trade | 243 | 46 МБ | 1 |
| pm_depth | 243 | 49 МБ | 1 |
| pm_rtt | 243 | 2 МБ | 1 |
| pm_top | 243 | 99 МБ | 1 |
| pm_trades | 242 | 71 МБ | 1 |
| rtds | 243 | 15 МБ | 1 |
| windows | 243 | 499 КБ | 173 |

Дни с данными: 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 6, TLS 106, всего 357
- Polymarket CLOB: TCP 10, TLS 88, всего 133
- Polymarket gamma: TCP 6, TLS 76, всего 84

## Последние строки журнала записи
```
00:02:16 [cex] Binance 35 сд. задержка p50/p90=143.3/144.2 мс | Coinbase 52 задержка p50=89.7 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.2 мс
00:02:16 [cex] binance_futures 42 сд. p50=292.6 мс | bybit 6 сд. p50=112.5 мс | bybit_book 63 сд. p50=110.5 мс | bybit_spot 12 сд. p50=112.8 мс | bybit_spot_book 27 сд. p50=111.0 мс | okx 23 сд. p50=150.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 802 сд. p50=144.1 мс
00:02:16 [pm] T-163.6s Up 0.37/0.38 Down 0.62/0.63 ptb=77212.8 | CLOB 3570 сообщ., задержка p50/p90=200.9/266.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793404936355 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.7/2.0 мс
00:02:26 [cex] Binance 48 сд. задержка p50/p90=142.6/143.5 мс | Coinbase 50 задержка p50=88.8 мс | смещение часов +18.4 мс | lag loop p99/max=2.1/2.2 мс
00:02:26 [cex] binance_futures 34 сд. p50=291.9 мс | bybit 28 сд. p50=111.4 мс | bybit_book 41 сд. p50=109.7 мс | bybit_spot 24 сд. p50=111.8 мс | bybit_spot_book 32 сд. p50=110.2 мс | okx 16 сд. p50=149.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1182 сд. p50=143.5 мс
00:02:26 [pm] T-153.6s Up 0.25/0.26 Down 0.74/0.75 ptb=77212.8 | CLOB 5749 сообщ., задержка p50/p90=39.6/44.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793404946356 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.7 мс | lag loop p99/max=1.9/2.4 мс
00:02:36 [cex] Binance 74 сд. задержка p50/p90=145.9/149.1 мс | Coinbase 48 задержка p50=89.4 мс | смещение часов +18.4 мс | lag loop p99/max=2.0/8.7 мс
00:02:36 [cex] binance_futures 106 сд. p50=147.3 мс | bybit 58 сд. p50=112.3 мс | bybit_book 103 сд. p50=109.7 мс | bybit_spot 50 сд. p50=115.3 мс | bybit_spot_book 32 сд. p50=110.2 мс | okx 67 сд. p50=151.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2754 сд. p50=144.5 мс
00:02:36 [pm] T-143.6s Up 0.60/0.61 Down 0.39/0.40 ptb=77212.8 | CLOB 8193 сообщ., задержка p50/p90=44.6/106.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793404956357 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.3/1.5 мс
00:02:46 [cex] Binance 70 сд. задержка p50/p90=143.0/149.6 мс | Coinbase 38 задержка p50=88.8 мс | смещение часов +18.4 мс | lag loop p99/max=2.1/2.1 мс
00:02:46 [cex] binance_futures 112 сд. p50=149.8 мс | bybit 67 сд. p50=112.9 мс | bybit_book 130 сд. p50=109.8 мс | bybit_spot 146 сд. p50=112.3 мс | bybit_spot_book 68 сд. p50=110.2 мс | okx 87 сд. p50=159.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2565 сд. p50=144.0 мс
00:02:46 [pm] T-133.6s Up 0.63/0.64 Down 0.36/0.37 ptb=77212.8 | CLOB 6980 сообщ., задержка p50/p90=45.2/50.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793404966358 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.5/1.6 мс
00:02:56 [cex] Binance 27 сд. задержка p50/p90=142.6/143.6 мс | Coinbase 34 задержка p50=88.5 мс | смещение часов +18.4 мс | lag loop p99/max=2.1/2.1 мс
00:02:56 [cex] binance_futures 37 сд. p50=292.0 мс | bybit 33 сд. p50=111.3 мс | bybit_book 91 сд. p50=109.7 мс | bybit_spot 26 сд. p50=111.9 мс | bybit_spot_book 37 сд. p50=110.2 мс | okx 25 сд. p50=149.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 676 сд. p50=143.4 мс
00:02:56 [pm] T-123.6s Up 0.60/0.61 Down 0.39/0.40 ptb=77212.8 | CLOB 3984 сообщ., задержка p50/p90=44.3/48.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793404976360 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.0/2.0 мс
```

Представлено версией кода: fcaf736; python 3.12.3
