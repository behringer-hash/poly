# Состояние сервера записи

Время (UTC): 2026-10-15 06:17:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 22 hours, 53 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         676         445           2        1033        1229
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.39 / 0.35 / 0.35

## Данные
- файлов: 4103, всего 994 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 163 | 22 МБ | 1 |
| bn_book | 163 | 2 МБ | 1 |
| bnf_agg | 163 | 33 МБ | 1 |
| bnf_book | 118 | 557 МБ | 160142 |
| bnf_depth5 | 118 | 41 МБ | 160218 |
| bnf_liq | 146 | 98 КБ | 90 |
| bs_trade | 118 | 1 МБ | 160138 |
| by_book1 | 163 | 69 МБ | 1 |
| by_liq | 143 | 82 КБ | 92 |
| by_trade | 163 | 22 МБ | 1 |
| bys_book1 | 47 | 18 МБ | 1 |
| bys_trade | 47 | 8 МБ | 1 |
| cb_ticker | 163 | 19 МБ | 1 |
| clock | 163 | 125 КБ | 60 |
| clock_pm | 163 | 125 КБ | 60 |
| events | 153 | 50 КБ | 2075 |
| events_pm | 162 | 58 КБ | 2048 |
| health_cex | 163 | 2 МБ | 3 |
| health_feeds | 163 | 6 МБ | 3 |
| health_pm | 163 | 2 МБ | 9 |
| kr_trade | 118 | 3 МБ | 160138 |
| ok_trade | 162 | 29 МБ | 1 |
| pm_depth | 163 | 32 МБ | 1 |
| pm_rtt | 163 | 1 МБ | 3 |
| pm_top | 163 | 66 МБ | 1 |
| pm_trades | 163 | 48 МБ | 1 |
| rtds | 163 | 10 МБ | 1 |
| windows | 163 | 335 КБ | 54 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 35, всего 283
- Polymarket CLOB: TCP 5, TLS 36, всего 77
- Polymarket gamma: TCP 5, TLS 37, всего 49

## Последние строки журнала записи
```
06:16:44 [cex] Binance 121 сд. задержка p50/p90=147.6/149.5 мс | Coinbase 49 задержка p50=85.5 мс | смещение часов +23.0 мс | lag loop p99/max=2.2/2.2 мс
06:16:44 [cex] binance_futures 181 сд. p50=150.7 мс | bybit 238 сд. p50=117.1 мс | bybit_book 293 сд. p50=114.5 мс | bybit_spot 163 сд. p50=116.8 мс | bybit_spot_book 168 сд. p50=114.4 мс | okx 215 сд. p50=156.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:16:47 [pm] T-192.1s Up 0.77/0.78 Down 0.22/0.23 ptb=80637.5 | CLOB 10316 сообщ., задержка p50/p90=38.4/39.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792045007866 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.2/1.3 мс
06:16:54 [cex] Binance 151 сд. задержка p50/p90=147.7/148.6 мс | Coinbase 49 задержка p50=85.8 мс | смещение часов +23.0 мс | lag loop p99/max=2.1/2.3 мс
06:16:54 [cex] binance_futures 211 сд. p50=148.5 мс | bybit 179 сд. p50=116.8 мс | bybit_book 266 сд. p50=114.5 мс | bybit_spot 191 сд. p50=116.6 мс | bybit_spot_book 171 сд. p50=114.2 мс | okx 228 сд. p50=157.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:16:57 [pm] T-182.1s Up 0.91/0.92 Down 0.08/0.09 ptb=80637.5 | CLOB 5738 сообщ., задержка p50/p90=38.4/39.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792045017868 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=1.8/1.9 мс
06:17:04 [cex] Binance 123 сд. задержка p50/p90=148.0/149.3 мс | Coinbase 50 задержка p50=86.5 мс | смещение часов +23.0 мс | lag loop p99/max=2.2/5.7 мс
06:17:04 [cex] binance_futures 241 сд. p50=148.6 мс | bybit 267 сд. p50=117.0 мс | bybit_book 315 сд. p50=114.6 мс | bybit_spot 193 сд. p50=117.0 мс | bybit_spot_book 192 сд. p50=114.3 мс | okx 243 сд. p50=157.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:17:07 [pm] T-172.1s Up 0.93/0.94 Down 0.06/0.07 ptb=80637.5 | CLOB 7177 сообщ., задержка p50/p90=38.6/41.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792045027869 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=7.8/8.6 мс
06:17:14 [cex] Binance 87 сд. задержка p50/p90=147.6/148.8 мс | Coinbase 54 задержка p50=86.5 мс | смещение часов +23.0 мс | lag loop p99/max=2.2/2.2 мс
06:17:14 [cex] binance_futures 157 сд. p50=152.9 мс | bybit 211 сд. p50=117.0 мс | bybit_book 283 сд. p50=114.5 мс | bybit_spot 135 сд. p50=116.7 мс | bybit_spot_book 178 сд. p50=114.3 мс | okx 209 сд. p50=157.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:17:17 [pm] T-162.1s Up 0.94/0.95 Down 0.05/0.06 ptb=80637.5 | CLOB 3773 сообщ., задержка p50/p90=38.5/40.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792045037871 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.7 мс | lag loop p99/max=2.0/2.1 мс
06:17:24 [cex] Binance 164 сд. задержка p50/p90=148.0/151.6 мс | Coinbase 44 задержка p50=86.5 мс | смещение часов +23.0 мс | lag loop p99/max=2.1/2.3 мс
06:17:24 [cex] binance_futures 182 сд. p50=150.7 мс | bybit 280 сд. p50=117.1 мс | bybit_book 293 сд. p50=114.6 мс | bybit_spot 248 сд. p50=117.0 мс | bybit_spot_book 184 сд. p50=114.3 мс | okx 209 сд. p50=157.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
06:17:27 [pm] T-152.1s Up 0.98/0.99 Down 0.01/0.02 ptb=80637.5 | CLOB 4529 сообщ., задержка p50/p90=38.5/39.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792045047872 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=2.1/2.9 мс
```

Представлено версией кода: ec1316a; python 3.12.3
