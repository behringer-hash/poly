# Состояние сервера записи

Время (UTC): 2026-10-18 08:26:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 1 hour, 2 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         860         494           2         839        1045
Swap:           2047         236        1811
```
- нагрузка CPU (1/5/15 мин): 0.13 / 0.18 / 0.18

## Данные
- файлов: 5856, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 237 | 31 МБ | 1 |
| bn_book | 237 | 3 МБ | 35 |
| bnf_agg | 237 | 46 МБ | 1 |
| bnf_book | 118 | 557 МБ | 427092 |
| bnf_depth5 | 118 | 41 МБ | 427168 |
| bnf_liq | 204 | 135 КБ | 3591 |
| bs_trade | 118 | 1 МБ | 427088 |
| by_book1 | 237 | 97 МБ | 1 |
| by_liq | 210 | 110 КБ | 1587 |
| by_trade | 237 | 30 МБ | 3 |
| bys_book1 | 121 | 41 МБ | 1 |
| bys_trade | 121 | 16 МБ | 3 |
| cb_ticker | 237 | 29 МБ | 10 |
| clock | 237 | 183 КБ | 8 |
| clock_pm | 237 | 183 КБ | 35 |
| events | 226 | 73 КБ | 532 |
| events_pm | 237 | 85 КБ | 1355 |
| health_cex | 237 | 2 МБ | 10 |
| health_feeds | 237 | 8 МБ | 10 |
| health_pm | 237 | 2 МБ | 9 |
| kr_trade | 118 | 3 МБ | 427088 |
| ok_trade | 236 | 40 МБ | 1 |
| pm_depth | 237 | 47 МБ | 1 |
| pm_rtt | 237 | 2 МБ | 1 |
| pm_top | 237 | 96 МБ | 1 |
| pm_trades | 237 | 69 МБ | 1 |
| rtds | 237 | 15 МБ | 1 |
| windows | 237 | 489 КБ | 245 |

Дни с данными: 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 34, всего 282
- Polymarket CLOB: TCP 5, TLS 38, всего 78
- Polymarket gamma: TCP 5, TLS 39, всего 51

## Последние строки журнала записи
```
08:25:58 [pm] T-241.8s Up 0.18/0.19 Down 0.81/0.82 ptb=81605.1 | CLOB 5782 сообщ., задержка p50/p90=38.8/58.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792311958155 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=2.1/3.8 мс
08:25:58 [cex] Binance 24 сд. задержка p50/p90=145.4/146.3 мс | Coinbase 19 задержка p50=78.9 мс | смещение часов +21.5 мс | lag loop p99/max=2.1/2.2 мс
08:25:58 [cex] binance_futures 25 сд. p50=294.7 мс | bybit 34 сд. p50=144.1 мс | bybit_book 91 сд. p50=113.0 мс | bybit_spot 5 сд. p50=115.3 мс | bybit_spot_book 29 сд. p50=113.1 мс | okx 5 сд. p50=154.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:26:08 [pm] T-231.8s Up 0.16/0.17 Down 0.83/0.84 ptb=81605.1 | CLOB 5185 сообщ., задержка p50/p90=38.7/40.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792311968157 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=2.9/4.7 мс
08:26:08 [cex] Binance 54 сд. задержка p50/p90=145.9/146.2 мс | Coinbase 4 задержка p50=78.8 мс | смещение часов +21.5 мс | lag loop p99/max=3.2/3.8 мс
08:26:08 [cex] binance_futures 43 сд. p50=148.1 мс | bybit 9 сд. p50=120.5 мс | bybit_book 61 сд. p50=113.0 мс | bybit_spot 48 сд. p50=116.4 мс | bybit_spot_book 80 сд. p50=113.1 мс | okx 8 сд. p50=154.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:26:18 [pm] T-221.8s Up 0.18/0.19 Down 0.81/0.82 ptb=81605.1 | CLOB 4746 сообщ., задержка p50/p90=38.7/40.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792311978158 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=2.0/2.1 мс
08:26:18 [cex] Binance 19 сд. задержка p50/p90=145.4/146.4 мс | Coinbase 9 задержка p50=79.7 мс | смещение часов +21.5 мс | lag loop p99/max=2.0/2.5 мс
08:26:18 [cex] binance_futures 7 сд. p50=294.9 мс | bybit 6 сд. p50=115.4 мс | bybit_book 33 сд. p50=113.0 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 21 сд. p50=113.4 мс | okx 5 сд. p50=155.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:26:28 [pm] T-211.8s Up 0.18/0.19 Down 0.81/0.82 ptb=81605.1 | CLOB 3960 сообщ., задержка p50/p90=38.6/40.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792311988160 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=1.7/1.9 мс
08:26:28 [cex] Binance 6 сд. задержка p50/p90=145.4/145.6 мс | Coinbase 11 задержка p50=77.0 мс | смещение часов +21.5 мс | lag loop p99/max=2.0/2.1 мс
08:26:28 [cex] binance_futures 17 сд. p50=294.8 мс | bybit 4 сд. p50=115.1 мс | bybit_book 65 сд. p50=113.0 мс | bybit_spot 0 сд. p50=n/a мс | bybit_spot_book 19 сд. p50=113.2 мс | okx 7 сд. p50=155.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:26:38 [pm] T-201.8s Up 0.18/0.19 Down 0.81/0.82 ptb=81605.1 | CLOB 4498 сообщ., задержка p50/p90=38.6/40.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792311998162 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.9 мс | lag loop p99/max=2.0/2.2 мс
08:26:38 [cex] Binance 11 сд. задержка p50/p90=144.9/146.6 мс | Coinbase 0 задержка p50=n/a мс | смещение часов +20.0 мс | lag loop p99/max=2.1/2.1 мс
08:26:38 [cex] binance_futures 17 сд. p50=293.3 мс | bybit 1 сд. p50=113.9 мс | bybit_book 79 сд. p50=111.6 мс | bybit_spot 1 сд. p50=114.1 мс | bybit_spot_book 47 сд. p50=111.8 мс | okx 5 сд. p50=153.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: b24b4e3; python 3.12.3
