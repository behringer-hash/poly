# Состояние сервера записи

Время (UTC): 2026-10-26 19:31:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 5 days, 12 hours, 7 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         644        1037           1         396        1261
Swap:           2047         293        1754
```
- нагрузка CPU (1/5/15 мин): 0.47 / 0.43 / 0.45

## Данные
- файлов: 5845, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 1 |
| bn_book | 242 | 3 МБ | 15 |
| bnf_agg | 242 | 52 МБ | 1 |
| bnf_book | 46 | 363 МБ | 1 |
| bnf_depth5 | 39 | 15 МБ | 1158249 |
| bnf_liq | 217 | 146 КБ | 775 |
| bs_trade | 39 | 548 КБ | 1158168 |
| by_book1 | 242 | 109 МБ | 1 |
| by_liq | 229 | 108 КБ | 1814 |
| by_trade | 242 | 35 МБ | 1 |
| bys_book1 | 205 | 70 МБ | 1 |
| bys_trade | 205 | 28 МБ | 3 |
| cb_ticker | 242 | 33 МБ | 1 |
| clock | 242 | 188 КБ | 62 |
| clock_pm | 242 | 188 КБ | 12 |
| events | 230 | 72 КБ | 161 |
| events_pm | 241 | 85 КБ | 40 |
| health_cex | 242 | 2 МБ | 7 |
| health_feeds | 242 | 8 МБ | 7 |
| health_pm | 242 | 3 МБ | 6 |
| kr_trade | 39 | 1 МБ | 1158168 |
| ok_trade | 241 | 45 МБ | 1 |
| pm_depth | 242 | 49 МБ | 2 |
| pm_rtt | 242 | 2 МБ | 4 |
| pm_top | 242 | 102 МБ | 2 |
| pm_trades | 242 | 72 МБ | 2 |
| rtds | 242 | 16 МБ | 2 |
| windows | 242 | 500 КБ | 44 |

Дни с данными: 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 41, всего 290
- Polymarket CLOB: TCP 5, TLS 40, всего 88
- Polymarket gamma: TCP 4, TLS 39, всего 46

## Последние строки журнала записи
```
19:30:30 [cex] binance_futures 57 сд. p50=295.1 мс | bybit 125 сд. p50=114.8 мс | bybit_book 164 сд. p50=112.5 мс | bybit_spot 51 сд. p50=115.8 мс | bybit_spot_book 50 сд. p50=113.1 мс | okx 37 сд. p50=156.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1765 сд. p50=146.2 мс
19:30:31 [pm] T-268.7s Up 0.24/0.25 Down 0.75/0.76 ptb=79868.3 | CLOB 8571 сообщ., задержка p50/p90=44.6/46.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793043031307 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.4/1.7 мс
19:30:38 [pm] btc-updown-5m-1793043000: CLOB#1 разорван (ConnectionClosedError(Close(code=1013, reason='slow consumer: send buffer full'), Close(code=1013, reason='slow consumer: send buffer full'), True)), переподключение
19:30:40 [cex] Binance 88 сд. задержка p50/p90=145.5/146.7 мс | Coinbase 75 задержка p50=86.0 мс | смещение часов +22.7 мс | lag loop p99/max=2.2/3.5 мс
19:30:40 [cex] binance_futures 100 сд. p50=157.3 мс | bybit 164 сд. p50=116.5 мс | bybit_book 182 сд. p50=112.5 мс | bybit_spot 189 сд. p50=116.8 мс | bybit_spot_book 79 сд. p50=113.2 мс | okx 87 сд. p50=156.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3134 сд. p50=148.0 мс
19:30:41 [pm] T-258.7s Up 0.19/0.20 Down 0.80/0.81 ptb=79868.3 | CLOB 8619 сообщ., задержка p50/p90=44.1/45.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793043041308 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=2.6/2.6 мс
19:30:50 [cex] Binance 32 сд. задержка p50/p90=145.4/146.3 мс | Coinbase 41 задержка p50=84.6 мс | смещение часов +22.7 мс | lag loop p99/max=2.0/2.1 мс
19:30:50 [cex] binance_futures 25 сд. p50=295.1 мс | bybit 9 сд. p50=113.9 мс | bybit_book 92 сд. p50=112.5 мс | bybit_spot 19 сд. p50=114.7 мс | bybit_spot_book 22 сд. p50=113.4 мс | okx 28 сд. p50=155.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 339 сд. p50=146.2 мс
19:30:51 [pm] T-248.7s Up 0.19/0.20 Down 0.80/0.81 ptb=79868.3 | CLOB 3594 сообщ., задержка p50/p90=44.1/45.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793043051310 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.7/1.8 мс
19:31:00 [cex] Binance 110 сд. задержка p50/p90=145.8/148.3 мс | Coinbase 77 задержка p50=85.9 мс | смещение часов +22.7 мс | lag loop p99/max=7.1/7.3 мс
19:31:00 [cex] binance_futures 114 сд. p50=156.2 мс | bybit 274 сд. p50=114.9 мс | bybit_book 234 сд. p50=112.4 мс | bybit_spot 57 сд. p50=115.9 мс | bybit_spot_book 96 сд. p50=113.3 мс | okx 188 сд. p50=158.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5995 сд. p50=146.1 мс
19:31:01 [pm] T-238.7s Up 0.14/0.15 Down 0.85/0.86 ptb=79868.3 | CLOB 7881 сообщ., задержка p50/p90=44.3/45.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793043061311 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=1.6/5.8 мс
19:31:10 [cex] Binance 77 сд. задержка p50/p90=145.5/147.6 мс | Coinbase 77 задержка p50=85.8 мс | смещение часов +22.7 мс | lag loop p99/max=3.6/9.1 мс
19:31:10 [cex] binance_futures 110 сд. p50=154.0 мс | bybit 177 сд. p50=116.9 мс | bybit_book 242 сд. p50=112.5 мс | bybit_spot 250 сд. p50=120.3 мс | bybit_spot_book 98 сд. p50=113.4 мс | okx 158 сд. p50=157.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4383 сд. p50=146.6 мс
19:31:11 [pm] T-228.7s Up 0.12/0.13 Down 0.87/0.88 ptb=79868.3 | CLOB 7763 сообщ., задержка p50/p90=44.7/46.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793043071312 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=1.8/2.0 мс
```

Представлено версией кода: 80591e6; python 3.12.3
