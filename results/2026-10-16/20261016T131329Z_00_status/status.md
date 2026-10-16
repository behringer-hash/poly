# Состояние сервера записи

Время (UTC): 2026-10-16 13:13:30

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 days, 5 hours, 49 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         466        1412           2         226        1439
Swap:           2047         263        1784
```
- нагрузка CPU (1/5/15 мин): 1.26 / 1.08 / 0.68

## Данные
- файлов: 4842, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 194 | 27 МБ | 1 |
| bn_book | 194 | 3 МБ | 7 |
| bnf_agg | 194 | 40 МБ | 1 |
| bnf_book | 118 | 557 МБ | 271504 |
| bnf_depth5 | 118 | 41 МБ | 271580 |
| bnf_liq | 174 | 117 КБ | 258 |
| bs_trade | 118 | 1 МБ | 271500 |
| by_book1 | 194 | 84 МБ | 1 |
| by_liq | 173 | 97 КБ | 258 |
| by_trade | 194 | 26 МБ | 1 |
| bys_book1 | 78 | 30 МБ | 1 |
| bys_trade | 78 | 12 МБ | 1 |
| cb_ticker | 194 | 24 МБ | 1 |
| clock | 194 | 149 КБ | 42 |
| clock_pm | 194 | 149 КБ | 58 |
| events | 182 | 59 КБ | 1252 |
| events_pm | 194 | 71 КБ | 46 |
| health_cex | 194 | 2 МБ | 9 |
| health_feeds | 194 | 7 МБ | 9 |
| health_pm | 194 | 2 МБ | 4 |
| kr_trade | 118 | 3 МБ | 271500 |
| ok_trade | 193 | 36 МБ | 1 |
| pm_depth | 194 | 39 МБ | 0 |
| pm_rtt | 194 | 1 МБ | 2 |
| pm_top | 194 | 79 МБ | 0 |
| pm_trades | 194 | 57 МБ | 0 |
| rtds | 194 | 12 МБ | 0 |
| windows | 194 | 399 КБ | 85 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 41, всего 292
- Polymarket CLOB: TCP 6, TLS 41, всего 154
- Polymarket gamma: TCP 5, TLS 38, всего 50

## Последние строки журнала записи
```
13:12:45 [pm] T-135.0s Up 0.90/0.91 Down 0.09/0.10 ptb=81854.0 | CLOB 3815 сообщ., задержка p50/p90=55.8/547.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792156365035 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=33.4/50.9 мс
13:12:49 [cex] Binance 473 сд. задержка p50/p90=159.7/184.4 мс | Coinbase 60 задержка p50=91.0 мс | смещение часов +33.4 мс | lag loop p99/max=95.7/168.2 мс
13:12:49 [cex] binance_futures 336 сд. p50=190.9 мс | bybit 326 сд. p50=129.0 мс | bybit_book 302 сд. p50=125.5 мс | bybit_spot 377 сд. p50=129.3 мс | bybit_spot_book 162 сд. p50=125.6 мс | okx 341 сд. p50=161.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:12:55 [pm] T-125.0s Up 0.92/0.93 Down 0.07/0.08 ptb=81854.0 | CLOB 6946 сообщ., задержка p50/p90=55.8/78.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792156375037 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=4.1/4.6 мс
13:12:59 [cex] Binance 176 сд. задержка p50/p90=157.3/158.6 мс | Coinbase 96 задержка p50=94.0 мс | смещение часов +33.4 мс | lag loop p99/max=2.3/6.9 мс
13:12:59 [cex] binance_futures 135 сд. p50=178.8 мс | bybit 110 сд. p50=127.3 мс | bybit_book 181 сд. p50=125.3 мс | bybit_spot 60 сд. p50=135.3 мс | bybit_spot_book 103 сд. p50=125.5 мс | okx 68 сд. p50=162.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:13:05 [pm] T-115.0s Up 0.93/0.94 Down 0.06/0.07 ptb=81854.0 | CLOB 4182 сообщ., задержка p50/p90=55.0/57.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792156385039 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=2.6/5.5 мс
13:13:09 [cex] Binance 186 сд. задержка p50/p90=157.4/158.2 мс | Coinbase 50 задержка p50=91.2 мс | смещение часов +33.4 мс | lag loop p99/max=3.3/7.5 мс
13:13:09 [cex] binance_futures 69 сд. p50=298.0 мс | bybit 42 сд. p50=127.4 мс | bybit_book 152 сд. p50=125.4 мс | bybit_spot 52 сд. p50=128.4 мс | bybit_spot_book 85 сд. p50=125.5 мс | okx 95 сд. p50=161.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:13:15 [pm] T-105.0s Up 0.95/0.96 Down 0.04/0.05 ptb=81854.0 | CLOB 4834 сообщ., задержка p50/p90=55.2/59.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792156395040 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=1.5/2.2 мс
13:13:19 [cex] Binance 141 сд. задержка p50/p90=157.4/158.2 мс | Coinbase 83 задержка p50=90.3 мс | смещение часов +33.4 мс | lag loop p99/max=2.1/3.6 мс
13:13:19 [cex] binance_futures 65 сд. p50=298.9 мс | bybit 61 сд. p50=132.6 мс | bybit_book 121 сд. p50=125.4 мс | bybit_spot 31 сд. p50=128.4 мс | bybit_spot_book 86 сд. p50=125.6 мс | okx 33 сд. p50=160.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
13:13:25 [pm] T- 95.0s Up 0.97/0.98 Down 0.02/0.03 ptb=81854.0 | CLOB 3262 сообщ., задержка p50/p90=56.0/81.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792156405042 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=3.3/10.5 мс
13:13:29 [cex] Binance 184 сд. задержка p50/p90=157.3/158.5 мс | Coinbase 21 задержка p50=89.9 мс | смещение часов +33.4 мс | lag loop p99/max=2.0/2.0 мс
13:13:29 [cex] binance_futures 176 сд. p50=161.7 мс | bybit 85 сд. p50=127.3 мс | bybit_book 189 сд. p50=125.4 мс | bybit_spot 128 сд. p50=128.3 мс | bybit_spot_book 155 сд. p50=125.5 мс | okx 30 сд. p50=160.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 8728f34; python 3.12.3
