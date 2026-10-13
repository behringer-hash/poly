# Состояние сервера записи

Время (UTC): 2026-10-13 10:00:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 6 days, 2 hours, 36 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         639        1176           2         269        1266
Swap:           2047         167        1880
```
- нагрузка CPU (1/5/15 мин): 1.72 / 1.56 / 1.07

## Данные
- файлов: 3054, всего 845 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 119 | 14 МБ | 2 |
| bn_book | 119 | 1 МБ | 2 |
| bnf_agg | 119 | 21 МБ | 2 |
| bnf_book | 118 | 557 МБ | 722 |
| bnf_depth5 | 118 | 41 МБ | 798 |
| bnf_liq | 105 | 65 КБ | 722 |
| bs_trade | 118 | 1 МБ | 718 |
| by_book1 | 119 | 44 МБ | 2 |
| by_liq | 100 | 57 КБ | 720 |
| by_trade | 119 | 13 МБ | 2 |
| bys_book1 | 3 | 380 КБ | 2 |
| bys_trade | 3 | 177 КБ | 2 |
| cb_ticker | 119 | 12 МБ | 2 |
| clock | 119 | 91 КБ | 24 |
| clock_pm | 119 | 91 КБ | 29 |
| events | 112 | 38 КБ | 675 |
| events_pm | 118 | 44 КБ | 796 |
| health_cex | 119 | 1 МБ | 6 |
| health_feeds | 119 | 4 МБ | 6 |
| health_pm | 119 | 1 МБ | 3 |
| kr_trade | 118 | 3 МБ | 718 |
| ok_trade | 118 | 19 МБ | 779 |
| pm_depth | 119 | 23 МБ | 1 |
| pm_rtt | 119 | 781 КБ | 1 |
| pm_top | 119 | 46 МБ | 1 |
| pm_trades | 119 | 34 МБ | 1 |
| rtds | 119 | 7 МБ | 1 |
| windows | 119 | 242 КБ | 202 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 53, всего 303
- Polymarket CLOB: TCP 7, TLS 92, всего 143
- Polymarket gamma: TCP 6, TLS 60, всего 72

## Последние строки журнала записи
```
09:59:40 [cex] binance_futures 59 сд. p50=265.7 мс | bybit 9 сд. p50=133.1 мс | bybit_book 205 сд. p50=130.7 мс | bybit_spot 33 сд. p50=134.4 мс | bybit_spot_book 222 сд. p50=130.7 мс
09:59:44 [pm] T- 15.5s Up 0.99/n/a Down n/a/0.01 ptb=83505.9 | CLOB 4524 сообщ., задержка p50/p90=51.4/53.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791885584465 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.3 мс | lag loop p99/max=1.6/2.0 мс
09:59:45 [pm] окно btc-updown-5m-1791885600 (2026-10-13 10:00:00 UTC): Bitcoin Up or Down - October 13, 6:00AM-6:05AM ET
09:59:50 [cex] Binance 54 сд. задержка p50/p90=160.7/161.7 мс | Coinbase 27 задержка p50=103.5 мс | смещение часов +39.3 мс | lag loop p99/max=2.9/3.1 мс
09:59:50 [cex] binance_futures 54 сд. p50=313.7 мс | bybit 33 сд. p50=133.6 мс | bybit_book 103 сд. p50=130.7 мс | bybit_spot 28 сд. p50=136.5 мс | bybit_spot_book 82 сд. p50=130.7 мс
09:59:54 [pm] T-  5.5s Up 0.99/n/a Down n/a/0.01 ptb=83505.9 | CLOB 2205 сообщ., задержка p50/p90=58.6/60.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791885594466 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.3 мс | lag loop p99/max=36.1/39.8 мс
10:00:00 [cex] Binance 95 сд. задержка p50/p90=160.8/161.5 мс | Coinbase 36 задержка p50=102.8 мс | смещение часов +39.3 мс | lag loop p99/max=5.3/11.4 мс
10:00:00 [cex] binance_futures 57 сд. p50=313.6 мс | bybit 40 сд. p50=135.0 мс | bybit_book 112 сд. p50=130.7 мс | bybit_spot 54 сд. p50=134.6 мс | bybit_spot_book 216 сд. p50=130.6 мс
10:00:04 [pm] T-295.5s Up 0.59/0.60 Down 0.40/0.41 ptb=83508.4 | CLOB 3494 сообщ., задержка p50/p90=51.5/289.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791885604468 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.3 мс | lag loop p99/max=21.0/34.9 мс
10:00:10 [cex] Binance 107 сд. задержка p50/p90=155.8/161.5 мс | Coinbase 49 задержка p50=99.1 мс | смещение часов +33.8 мс | lag loop p99/max=5.2/8.3 мс
10:00:10 [cex] binance_futures 149 сд. p50=163.6 мс | bybit 192 сд. p50=129.5 мс | bybit_book 184 сд. p50=125.7 мс | bybit_spot 138 сд. p50=130.2 мс | bybit_spot_book 166 сд. p50=126.0 мс
10:00:14 [pm] T-285.5s Up 0.55/0.56 Down 0.44/0.45 ptb=83508.4 | CLOB 8539 сообщ., задержка p50/p90=51.4/92.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791885614471 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.3 мс | lag loop p99/max=3.1/3.8 мс
10:00:20 [cex] Binance 87 сд. задержка p50/p90=155.5/157.0 мс | Coinbase 36 задержка p50=98.7 мс | смещение часов +33.8 мс | lag loop p99/max=3.0/3.1 мс
10:00:20 [cex] binance_futures 167 сд. p50=160.8 мс | bybit 179 сд. p50=128.7 мс | bybit_book 191 сд. p50=125.2 мс | bybit_spot 179 сд. p50=129.0 мс | bybit_spot_book 137 сд. p50=125.3 мс
10:00:24 [pm] T-275.5s Up 0.68/0.69 Down 0.31/0.32 ptb=83508.4 | CLOB 8373 сообщ., задержка p50/p90=49.7/60.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791885624472 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=2.4/3.0 мс
```

Представлено версией кода: cc28eb3; python 3.12.3
