# Состояние сервера записи

Время (UTC): 2026-10-15 16:34:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 9 hours, 10 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         679         362           2        1112        1226
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.11 / 0.21 / 0.19

## Данные
- файлов: 4341, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 173 | 25 МБ | 0 |
| bn_book | 173 | 2 МБ | 0 |
| bnf_agg | 173 | 39 МБ | 0 |
| bnf_book | 118 | 557 МБ | 197162 |
| bnf_depth5 | 118 | 41 МБ | 197238 |
| bnf_liq | 155 | 111 КБ | 115 |
| bs_trade | 118 | 1 МБ | 197158 |
| by_book1 | 173 | 79 МБ | 0 |
| by_liq | 153 | 92 КБ | 125 |
| by_trade | 173 | 26 МБ | 0 |
| bys_book1 | 57 | 25 МБ | 0 |
| bys_trade | 57 | 11 МБ | 2 |
| cb_ticker | 173 | 22 МБ | 0 |
| clock | 173 | 134 КБ | 55 |
| clock_pm | 173 | 134 КБ | 55 |
| events | 161 | 52 КБ | 2542 |
| events_pm | 173 | 61 КБ | 1050 |
| health_cex | 173 | 2 МБ | 8 |
| health_feeds | 173 | 6 МБ | 8 |
| health_pm | 173 | 2 МБ | 5 |
| kr_trade | 118 | 3 МБ | 197158 |
| ok_trade | 172 | 34 МБ | 0 |
| pm_depth | 173 | 35 МБ | 1 |
| pm_rtt | 173 | 1 МБ | 3 |
| pm_top | 173 | 71 МБ | 1 |
| pm_trades | 173 | 52 МБ | 3 |
| rtds | 173 | 11 МБ | 1 |
| windows | 173 | 358 КБ | 23 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 39, всего 285
- Polymarket CLOB: TCP 5, TLS 38, всего 86
- Polymarket gamma: TCP 5, TLS 37, всего 52

## Последние строки журнала записи
```
16:33:39 [cex] Binance 100 сд. задержка p50/p90=142.0/144.2 мс | Coinbase 70 задержка p50=82.3 мс | смещение часов +18.7 мс | lag loop p99/max=2.2/2.2 мс
16:33:39 [cex] binance_futures 212 сд. p50=144.5 мс | bybit 359 сд. p50=111.5 мс | bybit_book 303 сд. p50=109.3 мс | bybit_spot 290 сд. p50=112.2 мс | bybit_spot_book 196 сд. p50=109.2 мс | okx 245 сд. p50=157.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:33:43 [pm] T- 76.8s Up 0.02/0.03 Down 0.97/0.98 ptb=81995.3 | CLOB 5103 сообщ., задержка p50/p90=40.5/52.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792082023224 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=1.3/1.6 мс
16:33:49 [cex] Binance 132 сд. задержка p50/p90=142.0/143.3 мс | Coinbase 48 задержка p50=82.0 мс | смещение часов +18.7 мс | lag loop p99/max=2.2/2.3 мс
16:33:49 [cex] binance_futures 311 сд. p50=143.3 мс | bybit 288 сд. p50=111.7 мс | bybit_book 275 сд. p50=109.3 мс | bybit_spot 205 сд. p50=111.7 мс | bybit_spot_book 189 сд. p50=109.1 мс | okx 300 сд. p50=157.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:33:53 [pm] T- 66.8s Up n/a/0.01 Down 0.99/n/a ptb=81995.3 | CLOB 3009 сообщ., задержка p50/p90=39.9/77.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792082033226 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=2.1/9.2 мс
16:33:59 [cex] Binance 175 сд. задержка p50/p90=141.9/142.8 мс | Coinbase 57 задержка p50=82.1 мс | смещение часов +18.7 мс | lag loop p99/max=2.0/2.1 мс
16:33:59 [cex] binance_futures 278 сд. p50=143.9 мс | bybit 280 сд. p50=111.4 мс | bybit_book 387 сд. p50=109.3 мс | bybit_spot 184 сд. p50=111.9 мс | bybit_spot_book 202 сд. p50=109.1 мс | okx 262 сд. p50=157.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:34:03 [pm] T- 56.8s Up n/a/0.01 Down 0.99/n/a ptb=81995.3 | CLOB 2407 сообщ., задержка p50/p90=39.7/52.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792082043227 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.6 мс | lag loop p99/max=3.1/3.3 мс
16:34:09 [cex] Binance 148 сд. задержка p50/p90=142.2/144.8 мс | Coinbase 79 задержка p50=85.2 мс | смещение часов +18.7 мс | lag loop p99/max=3.5/4.4 мс
16:34:09 [cex] binance_futures 278 сд. p50=145.7 мс | bybit 226 сд. p50=111.7 мс | bybit_book 350 сд. p50=109.4 мс | bybit_spot 143 сд. p50=112.8 мс | bybit_spot_book 213 сд. p50=109.2 мс | okx 261 сд. p50=157.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:34:13 [pm] T- 46.8s Up n/a/0.01 Down 0.99/n/a ptb=81995.3 | CLOB 1262 сообщ., задержка p50/p90=39.5/40.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792082053228 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.7 мс | lag loop p99/max=1.9/2.1 мс
16:34:19 [cex] Binance 240 сд. задержка p50/p90=142.5/145.2 мс | Coinbase 55 задержка p50=81.8 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/2.2 мс
16:34:19 [cex] binance_futures 204 сд. p50=144.3 мс | bybit 171 сд. p50=111.4 мс | bybit_book 279 сд. p50=109.3 мс | bybit_spot 185 сд. p50=111.5 мс | bybit_spot_book 174 сд. p50=109.1 мс | okx 155 сд. p50=157.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
16:34:23 [pm] T- 36.8s Up n/a/0.01 Down 0.99/n/a ptb=81995.3 | CLOB 1054 сообщ., задержка p50/p90=39.5/41.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792082063230 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.7 мс | lag loop p99/max=2.0/2.0 мс
```

Представлено версией кода: ec1316a; python 3.12.3
