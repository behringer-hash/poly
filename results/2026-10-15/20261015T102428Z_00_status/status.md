# Состояние сервера записи

Время (UTC): 2026-10-15 10:24:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 3 hours, 0 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         685         411           2        1058        1220
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.02 / 0.07 / 0.12

## Данные
- файлов: 4200, всего 1003 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 167 | 22 МБ | 2 |
| bn_book | 167 | 2 МБ | 8 |
| bnf_agg | 167 | 34 МБ | 2 |
| bnf_book | 118 | 557 МБ | 174962 |
| bnf_depth5 | 118 | 41 МБ | 175038 |
| bnf_liq | 149 | 100 КБ | 22 |
| bs_trade | 118 | 1 МБ | 174958 |
| by_book1 | 167 | 71 МБ | 2 |
| by_liq | 147 | 83 КБ | 24 |
| by_trade | 167 | 22 МБ | 2 |
| bys_book1 | 51 | 19 МБ | 2 |
| bys_trade | 51 | 9 МБ | 2 |
| cb_ticker | 167 | 20 МБ | 2 |
| clock | 167 | 129 КБ | 58 |
| clock_pm | 167 | 129 КБ | 55 |
| events | 158 | 51 КБ | 225 |
| events_pm | 167 | 59 КБ | 211 |
| health_cex | 167 | 2 МБ | 2 |
| health_feeds | 167 | 6 МБ | 2 |
| health_pm | 167 | 2 МБ | 7 |
| kr_trade | 118 | 3 МБ | 174958 |
| ok_trade | 166 | 30 МБ | 2 |
| pm_depth | 167 | 33 МБ | 3 |
| pm_rtt | 167 | 1 МБ | 3 |
| pm_top | 167 | 68 МБ | 3 |
| pm_trades | 167 | 49 МБ | 3 |
| rtds | 167 | 11 МБ | 0 |
| windows | 167 | 344 КБ | 384 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 35, всего 297
- Polymarket CLOB: TCP 12, TLS 45, всего 87
- Polymarket gamma: TCP 5, TLS 36, всего 49

## Последние строки журнала записи
```
10:23:39 [pm] T- 80.1s Up n/a/0.00 Down 1.00/n/a ptb=81090.6 | CLOB 1033 сообщ., задержка p50/p90=38.3/42.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792059819931 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.2/2.2 мс
10:23:46 [cex] Binance 57 сд. задержка p50/p90=144.9/145.0 мс | Coinbase 42 задержка p50=78.1 мс | смещение часов +18.8 мс | lag loop p99/max=2.1/2.2 мс
10:23:46 [cex] binance_futures 208 сд. p50=144.4 мс | bybit 258 сд. p50=113.7 мс | bybit_book 242 сд. p50=110.5 мс | bybit_spot 90 сд. p50=112.7 мс | bybit_spot_book 141 сд. p50=110.2 мс | okx 153 сд. p50=152.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:23:49 [pm] T- 70.1s Up n/a/0.00 Down 1.00/n/a ptb=81090.6 | CLOB 510 сообщ., задержка p50/p90=38.2/40.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792059829932 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.1/2.2 мс
10:23:56 [cex] Binance 45 сд. задержка p50/p90=144.1/146.3 мс | Coinbase 39 задержка p50=78.2 мс | смещение часов +18.8 мс | lag loop p99/max=2.1/2.2 мс
10:23:56 [cex] binance_futures 93 сд. p50=221.2 мс | bybit 337 сд. p50=113.0 мс | bybit_book 225 сд. p50=110.5 мс | bybit_spot 137 сд. p50=113.0 мс | bybit_spot_book 149 сд. p50=110.3 мс | okx 150 сд. p50=152.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:23:59 [pm] T- 60.1s Up n/a/0.00 Down 1.00/n/a ptb=81090.6 | CLOB 772 сообщ., задержка p50/p90=38.3/42.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792059839933 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=2.1/2.2 мс
10:24:06 [cex] Binance 251 сд. задержка p50/p90=143.8/144.6 мс | Coinbase 45 задержка p50=78.6 мс | смещение часов +18.8 мс | lag loop p99/max=7.9/11.8 мс
10:24:06 [cex] binance_futures 247 сд. p50=148.1 мс | bybit 344 сд. p50=113.9 мс | bybit_book 239 сд. p50=110.5 мс | bybit_spot 300 сд. p50=114.0 мс | bybit_spot_book 159 сд. p50=110.3 мс | okx 332 сд. p50=153.6 мс | binance_liq 1 сд. p50=1163.2 мс | bybit_liq 1 сд. p50=443.4 мс
10:24:09 [pm] T- 50.1s Up n/a/0.00 Down 1.00/n/a ptb=81090.6 | CLOB 615 сообщ., задержка p50/p90=38.5/57.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792059849933 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.4 мс | lag loop p99/max=5.2/5.8 мс
10:24:16 [cex] Binance 65 сд. задержка p50/p90=143.6/144.4 мс | Coinbase 40 задержка p50=78.8 мс | смещение часов +18.8 мс | lag loop p99/max=2.2/2.3 мс
10:24:16 [cex] binance_futures 280 сд. p50=144.9 мс | bybit 246 сд. p50=112.9 мс | bybit_book 217 сд. p50=110.5 мс | bybit_spot 113 сд. p50=112.8 мс | bybit_spot_book 136 сд. p50=110.3 мс | okx 190 сд. p50=152.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:24:19 [pm] T- 40.1s Up n/a/0.00 Down 1.00/n/a ptb=81090.6 | CLOB 562 сообщ., задержка p50/p90=38.1/40.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792059859934 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.0/2.0 мс
10:24:26 [cex] Binance 111 сд. задержка p50/p90=144.0/145.2 мс | Coinbase 38 задержка p50=78.9 мс | смещение часов +18.8 мс | lag loop p99/max=2.2/2.3 мс
10:24:26 [cex] binance_futures 202 сд. p50=146.0 мс | bybit 491 сд. p50=113.7 мс | bybit_book 227 сд. p50=110.5 мс | bybit_spot 221 сд. p50=113.0 мс | bybit_spot_book 153 сд. p50=110.2 мс | okx 182 сд. p50=152.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: ec1316a; python 3.12.3
