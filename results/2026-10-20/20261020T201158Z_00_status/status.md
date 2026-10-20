# Состояние сервера записи

Время (UTC): 2026-10-20 20:11:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 12 hours, 48 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         762         587           1         748        1143
Swap:           2047         476        1571
```
- нагрузка CPU (1/5/15 мин): 0.42 / 0.32 / 0.32

## Данные
- файлов: 7290, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 297 | 38 МБ | 1 |
| bn_book | 297 | 4 МБ | 13 |
| bnf_agg | 297 | 59 МБ | 1 |
| bnf_book | 118 | 557 МБ | 642212 |
| bnf_depth5 | 118 | 41 МБ | 642288 |
| bnf_liq | 260 | 168 КБ | 168 |
| bs_trade | 118 | 1 МБ | 642208 |
| by_book1 | 297 | 123 МБ | 1 |
| by_liq | 268 | 133 КБ | 2903 |
| by_trade | 297 | 39 МБ | 1 |
| bys_book1 | 181 | 61 МБ | 1 |
| bys_trade | 181 | 24 МБ | 7 |
| cb_ticker | 297 | 36 МБ | 1 |
| clock | 297 | 229 КБ | 22 |
| clock_pm | 297 | 229 КБ | 56 |
| events | 286 | 91 КБ | 577 |
| events_pm | 297 | 107 КБ | 269 |
| health_cex | 297 | 3 МБ | 3 |
| health_feeds | 297 | 10 МБ | 3 |
| health_pm | 297 | 3 МБ | 7 |
| kr_trade | 118 | 3 МБ | 642208 |
| ok_trade | 296 | 51 МБ | 1 |
| pm_depth | 297 | 59 МБ | 1 |
| pm_rtt | 297 | 2 МБ | 3 |
| pm_top | 297 | 121 МБ | 1 |
| pm_trades | 297 | 85 МБ | 1 |
| rtds | 297 | 19 МБ | 1 |
| windows | 297 | 611 КБ | 84 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 40, всего 290
- Polymarket CLOB: TCP 5, TLS 47, всего 93
- Polymarket gamma: TCP 5, TLS 47, всего 62

## Последние строки журнала записи
```
20:11:10 [pm] T-229.0s Up 0.53/0.54 Down 0.46/0.47 ptb=82562.5 | CLOB 7556 сообщ., задержка p50/p90=46.5/54.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792527070955 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.7/2.2 мс
20:11:14 [cex] Binance 9 сд. задержка p50/p90=145.7/146.7 мс | Coinbase 22 задержка p50=78.7 мс | смещение часов +21.6 мс | lag loop p99/max=1.9/2.2 мс
20:11:14 [cex] binance_futures 21 сд. p50=294.9 мс | bybit 35 сд. p50=115.6 мс | bybit_book 94 сд. p50=113.8 мс | bybit_spot 2 сд. p50=118.5 мс | bybit_spot_book 40 сд. p50=113.6 мс | okx 17 сд. p50=148.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
20:11:20 [pm] T-219.0s Up 0.57/0.58 Down 0.42/0.43 ptb=82562.5 | CLOB 5311 сообщ., задержка p50/p90=46.5/52.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792527080956 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.4/2.1 мс
20:11:24 [cex] Binance 10 сд. задержка p50/p90=145.6/145.9 мс | Coinbase 31 задержка p50=79.3 мс | смещение часов +21.6 мс | lag loop p99/max=2.1/2.2 мс
20:11:24 [cex] binance_futures 22 сд. p50=295.4 мс | bybit 18 сд. p50=115.3 мс | bybit_book 57 сд. p50=113.8 мс | bybit_spot 1 сд. p50=115.5 мс | bybit_spot_book 24 сд. p50=113.5 мс | okx 11 сд. p50=147.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
20:11:30 [pm] T-209.0s Up 0.55/0.56 Down 0.44/0.45 ptb=82562.5 | CLOB 6398 сообщ., задержка p50/p90=46.3/50.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792527090957 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.2/1.2 мс
20:11:34 [cex] Binance 14 сд. задержка p50/p90=145.7/146.6 мс | Coinbase 26 задержка p50=78.7 мс | смещение часов +21.6 мс | lag loop p99/max=2.3/3.2 мс
20:11:34 [cex] binance_futures 21 сд. p50=295.0 мс | bybit 2 сд. p50=115.6 мс | bybit_book 53 сд. p50=113.8 мс | bybit_spot 3 сд. p50=115.0 мс | bybit_spot_book 19 сд. p50=113.6 мс | okx 14 сд. p50=148.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
20:11:40 [pm] T-199.0s Up 0.46/0.47 Down 0.53/0.54 ptb=82562.5 | CLOB 7352 сообщ., задержка p50/p90=49.5/63.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792527100958 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=3.1/8.1 мс
20:11:44 [cex] Binance 83 сд. задержка p50/p90=146.7/148.1 мс | Coinbase 53 задержка p50=80.0 мс | смещение часов +21.6 мс | lag loop p99/max=2.0/2.2 мс
20:11:44 [cex] binance_futures 154 сд. p50=146.7 мс | bybit 222 сд. p50=115.9 мс | bybit_book 128 сд. p50=113.8 мс | bybit_spot 224 сд. p50=116.1 мс | bybit_spot_book 126 сд. p50=113.6 мс | okx 184 сд. p50=149.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
20:11:50 [pm] T-189.0s Up 0.57/0.58 Down 0.42/0.43 ptb=82562.5 | CLOB 6728 сообщ., задержка p50/p90=46.3/48.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792527110960 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.2/1.3 мс
20:11:54 [cex] Binance 26 сд. задержка p50/p90=145.7/145.8 мс | Coinbase 17 задержка p50=79.0 мс | смещение часов +21.6 мс | lag loop p99/max=2.2/2.3 мс
20:11:54 [cex] binance_futures 17 сд. p50=295.0 мс | bybit 5 сд. p50=115.0 мс | bybit_book 59 сд. p50=113.9 мс | bybit_spot 2 сд. p50=115.6 мс | bybit_spot_book 45 сд. p50=113.6 мс | okx 21 сд. p50=147.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 96010db; python 3.12.3
