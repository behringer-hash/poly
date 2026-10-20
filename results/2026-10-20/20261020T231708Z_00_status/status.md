# Состояние сервера записи

Время (UTC): 2026-10-20 23:17:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 15 hours, 53 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         780         533           1         784        1125
Swap:           2047         476        1571
```
- нагрузка CPU (1/5/15 мин): 0.30 / 0.35 / 0.35

## Данные
- файлов: 7362, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 300 | 39 МБ | 0 |
| bn_book | 300 | 4 МБ | 8 |
| bnf_agg | 300 | 59 МБ | 0 |
| bnf_book | 118 | 557 МБ | 653322 |
| bnf_depth5 | 118 | 41 МБ | 653399 |
| bnf_liq | 263 | 169 КБ | 362 |
| bs_trade | 118 | 1 МБ | 653318 |
| by_book1 | 300 | 124 МБ | 0 |
| by_liq | 271 | 135 КБ | 3572 |
| by_trade | 300 | 39 МБ | 0 |
| bys_book1 | 184 | 62 МБ | 0 |
| bys_trade | 184 | 25 МБ | 0 |
| cb_ticker | 300 | 37 МБ | 0 |
| clock | 300 | 231 КБ | 2 |
| clock_pm | 300 | 232 КБ | 36 |
| events | 289 | 91 КБ | 643 |
| events_pm | 300 | 108 КБ | 7 |
| health_cex | 300 | 3 МБ | 2 |
| health_feeds | 300 | 10 МБ | 2 |
| health_pm | 300 | 3 МБ | 5 |
| kr_trade | 118 | 3 МБ | 653318 |
| ok_trade | 299 | 52 МБ | 0 |
| pm_depth | 300 | 59 МБ | 1 |
| pm_rtt | 300 | 2 МБ | 3 |
| pm_top | 300 | 122 МБ | 1 |
| pm_trades | 300 | 86 МБ | 1 |
| rtds | 300 | 19 МБ | 1 |
| windows | 300 | 618 КБ | 184 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 289
- Polymarket CLOB: TCP 5, TLS 48, всего 90
- Polymarket gamma: TCP 6, TLS 56, всего 67

## Последние строки журнала записи
```
23:16:25 [cex] Binance 10 сд. задержка p50/p90=143.1/144.2 мс | Coinbase 28 задержка p50=76.1 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.1 мс
23:16:25 [cex] binance_futures 22 сд. p50=292.9 мс | bybit 64 сд. p50=113.7 мс | bybit_book 90 сд. p50=111.1 мс | bybit_spot 1 сд. p50=112.4 мс | bybit_spot_book 43 сд. p50=111.1 мс | okx 22 сд. p50=145.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:16:32 [pm] T-207.4s Up 0.21/0.22 Down 0.78/0.79 ptb=82897.4 | CLOB 5765 сообщ., задержка p50/p90=50.6/260.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792538192623 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=2.2/6.4 мс
23:16:35 [cex] Binance 91 сд. задержка p50/p90=143.4/144.9 мс | Coinbase 42 задержка p50=76.8 мс | смещение часов +19.1 мс | lag loop p99/max=2.2/2.7 мс
23:16:35 [cex] binance_futures 141 сд. p50=145.5 мс | bybit 121 сд. p50=113.5 мс | bybit_book 132 сд. p50=111.0 мс | bybit_spot 95 сд. p50=112.8 мс | bybit_spot_book 134 сд. p50=111.0 мс | okx 139 сд. p50=146.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:16:42 [pm] T-197.4s Up 0.12/0.13 Down 0.87/0.88 ptb=82897.4 | CLOB 5176 сообщ., задержка p50/p90=40.8/182.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792538202625 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.8 мс | lag loop p99/max=1.8/8.6 мс
23:16:45 [cex] Binance 25 сд. задержка p50/p90=143.2/144.5 мс | Coinbase 45 задержка p50=76.5 мс | смещение часов +19.1 мс | lag loop p99/max=2.2/2.2 мс
23:16:45 [cex] binance_futures 34 сд. p50=292.8 мс | bybit 113 сд. p50=113.4 мс | bybit_book 137 сд. p50=111.0 мс | bybit_spot 17 сд. p50=113.6 мс | bybit_spot_book 144 сд. p50=111.0 мс | okx 47 сд. p50=145.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:16:52 [pm] T-187.4s Up 0.14/0.15 Down 0.85/0.86 ptb=82897.4 | CLOB 4477 сообщ., задержка p50/p90=40.9/46.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792538212627 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.6 мс | lag loop p99/max=1.6/1.8 мс
23:16:55 [cex] Binance 29 сд. задержка p50/p90=143.2/144.1 мс | Coinbase 58 задержка p50=76.6 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.2 мс
23:16:55 [cex] binance_futures 64 сд. p50=265.6 мс | bybit 68 сд. p50=112.9 мс | bybit_book 166 сд. p50=111.0 мс | bybit_spot 131 сд. p50=113.6 мс | bybit_spot_book 128 сд. p50=111.0 мс | okx 38 сд. p50=145.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
23:17:00 [pm] btc-updown-5m-1792538100: CLOB#0 разорван (ConnectionClosedError(Close(code=1013, reason='slow consumer: send buffer full'), Close(code=1013, reason='slow consumer: send buffer full'), True)), переподключение
23:17:02 [pm] T-177.4s Up 0.08/0.09 Down 0.91/0.92 ptb=82897.4 | CLOB 6994 сообщ., задержка p50/p90=40.7/44.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792538222628 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.6 мс | lag loop p99/max=4.2/5.3 мс
23:17:05 [cex] Binance 232 сд. задержка p50/p90=143.2/146.7 мс | Coinbase 40 задержка p50=76.6 мс | смещение часов +18.2 мс | lag loop p99/max=3.4/4.9 мс
23:17:05 [cex] binance_futures 164 сд. p50=146.4 мс | bybit 270 сд. p50=114.1 мс | bybit_book 182 сд. p50=111.0 мс | bybit_spot 85 сд. p50=114.3 мс | bybit_spot_book 188 сд. p50=111.2 мс | okx 119 сд. p50=146.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 96010db; python 3.12.3
