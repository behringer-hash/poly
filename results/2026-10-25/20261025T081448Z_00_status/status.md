# Состояние сервера записи

Время (UTC): 2026-10-25 08:14:48

## Службы
- lab-collector: inactive
- lab-runner.timer: active
- uptime: up 3 weeks, 4 days, 50 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 10 ГБ из 57 ГБ, свободно 47 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         543         203           2        1352        1362
Swap:           2047          94        1953
```
- нагрузка CPU (1/5/15 мин): 0.05 / 0.03 / 0.00

## Данные
- файлов: 6562, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 270 | 34 МБ | 325863 |
| bn_book | 270 | 3 МБ | 325866 |
| bnf_agg | 270 | 56 МБ | 325871 |
| bnf_book | 74 | 315 МБ | 1031182 |
| bnf_depth5 | 74 | 25 МБ | 1031258 |
| bnf_liq | 235 | 151 КБ | 326084 |
| bs_trade | 74 | 792 КБ | 1031178 |
| by_book1 | 270 | 110 МБ | 325866 |
| by_liq | 245 | 115 КБ | 326086 |
| by_trade | 270 | 38 МБ | 325871 |
| bys_book1 | 198 | 66 МБ | 325861 |
| bys_trade | 198 | 28 МБ | 325871 |
| cb_ticker | 270 | 33 МБ | 325865 |
| clock | 270 | 210 КБ | 325911 |
| clock_pm | 270 | 209 КБ | 325866 |
| events | 261 | 82 КБ | 325871 |
| events_pm | 270 | 94 КБ | 325865 |
| health_cex | 270 | 3 МБ | 325879 |
| health_feeds | 270 | 9 МБ | 325879 |
| health_pm | 270 | 3 МБ | 325865 |
| kr_trade | 74 | 2 МБ | 1031178 |
| ok_trade | 269 | 45 МБ | 325859 |
| pm_depth | 270 | 53 МБ | 325866 |
| pm_rtt | 270 | 2 МБ | 325865 |
| pm_top | 270 | 110 МБ | 325867 |
| pm_trades | 270 | 78 МБ | 325865 |
| rtds | 270 | 17 МБ | 325870 |
| windows | 270 | 557 КБ | 325865 |

Дни с данными: 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 35, всего 285
- Polymarket CLOB: TCP 6, TLS 37, всего 81
- Polymarket gamma: TCP 4, TLS 35, всего 42

## Последние строки журнала записи
```
13:42:48 [cex] binance_futures 136 сд. p50=159.1 мс | bybit 231 сд. p50=117.7 мс | bybit_book 351 сд. p50=115.3 мс | bybit_spot 120 сд. p50=129.8 мс | bybit_spot_book 122 сд. p50=115.5 мс | okx 214 сд. p50=149.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:42:49 [pm] T-130.8s Up 0.04/0.05 Down 0.95/0.96 ptb=83489.2 | CLOB 5948 сообщ., задержка p50/p90=43.4/46.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590169239 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.7/1.8 мс
13:42:58 [cex] Binance 194 сд. задержка p50/p90=170.9/172.1 мс | Coinbase 84 задержка p50=81.0 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/7.6 мс
13:42:58 [cex] binance_futures 320 сд. p50=160.6 мс | bybit 599 сд. p50=141.2 мс | bybit_book 301 сд. p50=115.3 мс | bybit_spot 220 сд. p50=124.5 мс | bybit_spot_book 197 сд. p50=115.4 мс | okx 369 сд. p50=163.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:42:59 [pm] T-120.8s Up 0.01/0.02 Down 0.98/0.99 ptb=83489.2 | CLOB 5791 сообщ., задержка p50/p90=41.4/43.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590179241 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.0/2.1 мс
13:43:08 [cex] Binance 552 сд. задержка p50/p90=149.4/163.6 мс | Coinbase 78 задержка p50=80.3 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/4.0 мс
13:43:08 [cex] binance_futures 503 сд. p50=158.7 мс | bybit 665 сд. p50=117.0 мс | bybit_book 494 сд. p50=114.1 мс | bybit_spot 384 сд. p50=124.9 мс | bybit_spot_book 260 сд. p50=114.3 мс | okx 619 сд. p50=149.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:43:09 [pm] T-110.8s Up 0.16/0.17 Down 0.83/0.84 ptb=83489.2 | CLOB 13057 сообщ., задержка p50/p90=41.5/43.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590189243 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.3/4.0 мс
13:43:18 [cex] Binance 305 сд. задержка p50/p90=156.5/158.7 мс | Coinbase 97 задержка p50=83.0 мс | смещение часов +22.1 мс | lag loop p99/max=2.1/2.1 мс
13:43:18 [cex] binance_futures 366 сд. p50=160.4 мс | bybit 483 сд. p50=117.0 мс | bybit_book 465 сд. p50=114.1 мс | bybit_spot 275 сд. p50=123.8 мс | bybit_spot_book 218 сд. p50=114.3 мс | okx 371 сд. p50=148.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:43:19 [pm] T-100.8s Up 0.19/0.20 Down 0.80/0.81 ptb=83489.2 | CLOB 13971 сообщ., задержка p50/p90=41.4/42.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590199244 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.8/3.3 мс
13:43:28 [cex] Binance 262 сд. задержка p50/p90=148.2/154.1 мс | Coinbase 58 задержка p50=79.7 мс | смещение часов +22.1 мс | lag loop p99/max=2.2/2.9 мс
13:43:28 [cex] binance_futures 254 сд. p50=149.6 мс | bybit 216 сд. p50=116.4 мс | bybit_book 433 сд. p50=114.1 мс | bybit_spot 108 сд. p50=118.7 мс | bybit_spot_book 156 сд. p50=114.3 мс | okx 323 сд. p50=148.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:43:29 [pm] T- 90.8s Up 0.35/0.36 Down 0.64/0.65 ptb=83489.2 | CLOB 14782 сообщ., задержка p50/p90=41.5/44.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792590209247 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.6/2.2 мс
[run] остановка...
```

Представлено версией кода: b98a05a; python 3.12.3
