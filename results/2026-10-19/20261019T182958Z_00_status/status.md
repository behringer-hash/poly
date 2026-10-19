# Состояние сервера записи

Время (UTC): 2026-10-19 18:29:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 5 days, 11 hours, 6 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         756         333           1         997        1149
Swap:           2047         250        1797
```
- нагрузка CPU (1/5/15 мин): 0.32 / 0.27 / 0.27

## Данные
- файлов: 6671, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 271 | 35 МБ | 1 |
| bn_book | 271 | 3 МБ | 5 |
| bnf_agg | 271 | 54 МБ | 1 |
| bnf_book | 118 | 557 МБ | 549692 |
| bnf_depth5 | 118 | 41 МБ | 549768 |
| bnf_liq | 237 | 156 КБ | 146 |
| bs_trade | 118 | 1 МБ | 549688 |
| by_book1 | 271 | 113 МБ | 1 |
| by_liq | 244 | 124 КБ | 258 |
| by_trade | 271 | 35 МБ | 1 |
| bys_book1 | 155 | 53 МБ | 1 |
| bys_trade | 155 | 21 МБ | 3 |
| cb_ticker | 271 | 33 МБ | 1 |
| clock | 271 | 209 КБ | 15 |
| clock_pm | 271 | 209 КБ | 36 |
| events | 260 | 82 КБ | 739 |
| events_pm | 271 | 97 КБ | 531 |
| health_cex | 271 | 3 МБ | 5 |
| health_feeds | 271 | 9 МБ | 5 |
| health_pm | 271 | 3 МБ | 0 |
| kr_trade | 118 | 3 МБ | 549688 |
| ok_trade | 270 | 47 МБ | 1 |
| pm_depth | 271 | 54 МБ | 0 |
| pm_rtt | 271 | 2 МБ | 2 |
| pm_top | 271 | 110 МБ | 0 |
| pm_trades | 271 | 78 МБ | 0 |
| rtds | 271 | 17 МБ | 0 |
| windows | 271 | 559 КБ | 145 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 38, всего 290
- Polymarket CLOB: TCP 5, TLS 38, всего 81
- Polymarket gamma: TCP 5, TLS 40, всего 53

## Последние строки журнала записи
```
18:29:12 [cex] binance_futures 68 сд. p50=267.1 мс | bybit 139 сд. p50=113.5 мс | bybit_book 237 сд. p50=111.8 мс | bybit_spot 45 сд. p50=114.1 мс | bybit_spot_book 84 сд. p50=111.4 мс | okx 51 сд. p50=151.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:29:16 [pm] T- 43.4s Up n/a/0.01 Down 0.99/n/a ptb=81810.2 | CLOB 454 сообщ., задержка p50/p90=39.8/40.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792434556640 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.1/2.2 мс
18:29:22 [cex] Binance 10 сд. задержка p50/p90=143.7/144.7 мс | Coinbase 45 задержка p50=78.0 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.2 мс
18:29:22 [cex] binance_futures 52 сд. p50=268.6 мс | bybit 111 сд. p50=113.4 мс | bybit_book 200 сд. p50=111.9 мс | bybit_spot 10 сд. p50=114.0 мс | bybit_spot_book 66 сд. p50=111.3 мс | okx 14 сд. p50=151.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:29:26 [pm] T- 33.4s Up n/a/0.00 Down 1.00/n/a ptb=81810.2 | CLOB 556 сообщ., задержка p50/p90=39.1/41.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792434566641 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.1/2.1 мс
18:29:32 [cex] Binance 21 сд. задержка p50/p90=143.7/143.8 мс | Coinbase 73 задержка p50=104.4 мс | смещение часов +19.5 мс | lag loop p99/max=2.0/2.2 мс
18:29:32 [cex] binance_futures 80 сд. p50=146.5 мс | bybit 88 сд. p50=113.3 мс | bybit_book 139 сд. p50=111.8 мс | bybit_spot 72 сд. p50=113.7 мс | bybit_spot_book 53 сд. p50=111.4 мс | okx 15 сд. p50=151.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:29:36 [pm] T- 23.4s Up n/a/0.00 Down 1.00/n/a ptb=81810.2 | CLOB 560 сообщ., задержка p50/p90=38.6/40.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792434576642 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.0/2.0 мс
18:29:42 [cex] Binance 9 сд. задержка p50/p90=143.7/144.7 мс | Coinbase 33 задержка p50=78.1 мс | смещение часов +18.0 мс | lag loop p99/max=2.1/2.2 мс
18:29:42 [cex] binance_futures 39 сд. p50=293.6 мс | bybit 21 сд. p50=113.0 мс | bybit_book 91 сд. p50=111.9 мс | bybit_spot 3 сд. p50=113.7 мс | bybit_spot_book 42 сд. p50=111.5 мс | okx 31 сд. p50=151.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:29:45 [pm] окно btc-updown-5m-1792434600 (2026-10-19 18:30:00 UTC): Bitcoin Up or Down - October 19, 2:30PM-2:35PM ET
18:29:46 [pm] T- 13.4s Up n/a/0.00 Down 1.00/n/a ptb=81810.2 | CLOB 641 сообщ., задержка p50/p90=37.8/40.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792434586643 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.1/2.1 мс
18:29:52 [cex] Binance 196 сд. задержка p50/p90=142.6/144.6 мс | Coinbase 118 задержка p50=80.2 мс | смещение часов +18.0 мс | lag loop p99/max=2.2/2.2 мс
18:29:52 [cex] binance_futures 214 сд. p50=144.5 мс | bybit 225 сд. p50=112.1 мс | bybit_book 234 сд. p50=110.4 мс | bybit_spot 305 сд. p50=112.8 мс | bybit_spot_book 151 сд. p50=109.8 мс | okx 235 сд. p50=150.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
18:29:56 [pm] T-  3.4s Up n/a/0.00 Down 1.00/n/a ptb=81810.2 | CLOB 2397 сообщ., задержка p50/p90=39.4/40.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792434596646 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.8/2.0 мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
