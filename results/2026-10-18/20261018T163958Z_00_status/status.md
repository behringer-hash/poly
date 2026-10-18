# Состояние сервера записи

Время (UTC): 2026-10-18 16:39:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 9 hours, 16 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         545        1196           2         350        1360
Swap:           2047         244        1803
```
- нагрузка CPU (1/5/15 мин): 0.09 / 0.12 / 0.14

## Данные
- файлов: 6046, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 245 | 32 МБ | 1 |
| bn_book | 245 | 3 МБ | 13 |
| bnf_agg | 245 | 49 МБ | 1 |
| bnf_book | 118 | 557 МБ | 456692 |
| bnf_depth5 | 118 | 41 МБ | 456768 |
| bnf_liq | 211 | 138 КБ | 258 |
| bs_trade | 118 | 1 МБ | 456688 |
| by_book1 | 245 | 102 МБ | 1 |
| by_liq | 217 | 113 КБ | 3524 |
| by_trade | 245 | 32 МБ | 1 |
| bys_book1 | 129 | 44 МБ | 1 |
| bys_trade | 129 | 18 МБ | 1 |
| cb_ticker | 245 | 30 МБ | 1 |
| clock | 245 | 189 КБ | 43 |
| clock_pm | 245 | 190 КБ | 7 |
| events | 234 | 75 КБ | 1079 |
| events_pm | 245 | 89 КБ | 362 |
| health_cex | 245 | 3 МБ | 5 |
| health_feeds | 245 | 8 МБ | 5 |
| health_pm | 245 | 3 МБ | 5 |
| kr_trade | 118 | 3 МБ | 456688 |
| ok_trade | 244 | 43 МБ | 1 |
| pm_depth | 245 | 49 МБ | 1 |
| pm_rtt | 245 | 2 МБ | 3 |
| pm_top | 245 | 100 МБ | 1 |
| pm_trades | 245 | 71 МБ | 1 |
| rtds | 245 | 16 МБ | 1 |
| windows | 245 | 506 КБ | 83 |

Дни с данными: 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 36, всего 292
- Polymarket CLOB: TCP 7, TLS 40, всего 80
- Polymarket gamma: TCP 5, TLS 37, всего 56

## Последние строки журнала записи
```
16:39:11 [cex] binance_futures 114 сд. p50=144.4 мс | bybit 128 сд. p50=113.7 мс | bybit_book 121 сд. p50=111.2 мс | bybit_spot 102 сд. p50=114.3 мс | bybit_spot_book 87 сд. p50=110.8 мс | okx 219 сд. p50=153.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:39:12 [pm] T- 47.5s Up n/a/0.01 Down 0.99/n/a ptb=81056.5 | CLOB 826 сообщ., задержка p50/p90=62.5/74.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792341552540 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=51.6 мс | lag loop p99/max=2.0/2.2 мс
16:39:21 [cex] Binance 69 сд. задержка p50/p90=142.8/143.6 мс | Coinbase 50 задержка p50=75.6 мс | смещение часов +18.5 мс | lag loop p99/max=2.0/2.1 мс
16:39:21 [cex] binance_futures 152 сд. p50=144.6 мс | bybit 163 сд. p50=113.0 мс | bybit_book 138 сд. p50=110.8 мс | bybit_spot 270 сд. p50=112.9 мс | bybit_spot_book 138 сд. p50=110.4 мс | okx 149 сд. p50=155.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:39:22 [pm] T- 37.5s Up n/a/0.01 Down 0.99/n/a ptb=81056.5 | CLOB 536 сообщ., задержка p50/p90=62.6/66.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792341562541 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=51.5 мс | lag loop p99/max=2.1/2.2 мс
16:39:31 [cex] Binance 47 сд. задержка p50/p90=142.7/143.0 мс | Coinbase 54 задержка p50=86.3 мс | смещение часов +18.5 мс | lag loop p99/max=2.1/2.2 мс
16:39:31 [cex] binance_futures 82 сд. p50=143.8 мс | bybit 173 сд. p50=113.7 мс | bybit_book 166 сд. p50=110.7 мс | bybit_spot 188 сд. p50=112.8 мс | bybit_spot_book 95 сд. p50=110.1 мс | okx 89 сд. p50=152.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:39:32 [pm] T- 27.5s Up n/a/0.01 Down 0.99/n/a ptb=81056.5 | CLOB 459 сообщ., задержка p50/p90=62.1/65.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792341572543 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=51.5 мс | lag loop p99/max=2.1/2.1 мс
16:39:41 [cex] Binance 45 сд. задержка p50/p90=142.5/142.7 мс | Coinbase 33 задержка p50=76.4 мс | смещение часов +18.5 мс | lag loop p99/max=2.2/2.2 мс
16:39:41 [cex] binance_futures 70 сд. p50=163.6 мс | bybit 133 сд. p50=112.8 мс | bybit_book 230 сд. p50=110.7 мс | bybit_spot 116 сд. p50=112.7 мс | bybit_spot_book 94 сд. p50=110.1 мс | okx 98 сд. p50=152.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:39:42 [pm] T- 17.5s Up n/a/0.00 Down 1.00/n/a ptb=81056.5 | CLOB 512 сообщ., задержка p50/p90=62.3/69.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792341582544 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=51.5 мс | lag loop p99/max=2.0/2.1 мс
16:39:45 [pm] окно btc-updown-5m-1792341600 (2026-10-18 16:40:00 UTC): Bitcoin Up or Down - October 18, 12:40PM-12:45PM ET
16:39:51 [cex] Binance 57 сд. задержка p50/p90=142.6/142.9 мс | Coinbase 34 задержка p50=78.0 мс | смещение часов +18.5 мс | lag loop p99/max=2.2/2.2 мс
16:39:51 [cex] binance_futures 100 сд. p50=144.8 мс | bybit 227 сд. p50=113.1 мс | bybit_book 186 сд. p50=110.6 мс | bybit_spot 155 сд. p50=112.6 мс | bybit_spot_book 118 сд. p50=110.2 мс | okx 146 сд. p50=154.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:39:52 [pm] T-  7.5s Up n/a/0.00 Down 1.00/n/a ptb=81056.5 | CLOB 1425 сообщ., задержка p50/p90=43.3/62.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792341592545 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=51.5 мс | lag loop p99/max=2.2/20.8 мс
```

Представлено версией кода: eab44f6; python 3.12.3
