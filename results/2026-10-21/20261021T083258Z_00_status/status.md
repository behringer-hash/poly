# Состояние сервера записи

Время (UTC): 2026-10-21 08:32:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 1 hour, 9 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 9 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         752         347           2         994        1153
Swap:           2047         245        1802
```
- нагрузка CPU (1/5/15 мин): 0.43 / 0.39 / 0.38

## Данные
- файлов: 7575, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 309 | 40 МБ | 2 |
| bn_book | 309 | 4 МБ | 25 |
| bnf_agg | 309 | 61 МБ | 2 |
| bnf_book | 118 | 557 МБ | 686672 |
| bnf_depth5 | 118 | 41 МБ | 686748 |
| bnf_liq | 270 | 175 КБ | 2390 |
| bs_trade | 118 | 1 МБ | 686668 |
| by_book1 | 309 | 130 МБ | 2 |
| by_liq | 279 | 136 КБ | 278 |
| by_trade | 309 | 41 МБ | 2 |
| bys_book1 | 193 | 69 МБ | 2 |
| bys_trade | 193 | 26 МБ | 2 |
| cb_ticker | 309 | 38 МБ | 2 |
| clock | 309 | 239 КБ | 41 |
| clock_pm | 309 | 239 КБ | 41 |
| events | 298 | 95 КБ | 559 |
| events_pm | 309 | 112 КБ | 49 |
| health_cex | 309 | 3 МБ | 2 |
| health_feeds | 309 | 10 МБ | 2 |
| health_pm | 309 | 3 МБ | 1 |
| kr_trade | 118 | 3 МБ | 686668 |
| ok_trade | 308 | 53 МБ | -0 |
| pm_depth | 309 | 62 МБ | 1 |
| pm_rtt | 309 | 2 МБ | 1 |
| pm_top | 309 | 127 МБ | 1 |
| pm_trades | 309 | 89 МБ | 1 |
| rtds | 309 | 20 МБ | 1 |
| windows | 309 | 638 КБ | 113 |

Дни с данными: 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 292
- Polymarket CLOB: TCP 5, TLS 55, всего 94
- Polymarket gamma: TCP 4, TLS 44, всего 51

## Последние строки журнала записи
```
08:32:16 [cex] Binance 67 сд. задержка p50/p90=147.0/148.8 мс | Coinbase 59 задержка p50=77.9 мс | смещение часов +21.7 мс | lag loop p99/max=2.1/2.3 мс
08:32:16 [cex] binance_futures 160 сд. p50=148.8 мс | bybit 136 сд. p50=115.1 мс | bybit_book 195 сд. p50=112.0 мс | bybit_spot 191 сд. p50=142.0 мс | bybit_spot_book 130 сд. p50=112.3 мс | okx 234 сд. p50=147.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:32:16 [pm] T-163.5s Up 0.15/0.16 Down 0.84/0.85 ptb=83176.5 | CLOB 4844 сообщ., задержка p50/p90=42.3/45.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792571536530 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=3.0/4.0 мс
08:32:26 [cex] Binance 19 сд. задержка p50/p90=146.2/147.2 мс | Coinbase 25 задержка p50=79.1 мс | смещение часов +21.7 мс | lag loop p99/max=2.1/2.3 мс
08:32:26 [cex] binance_futures 50 сд. p50=295.8 мс | bybit 35 сд. p50=115.4 мс | bybit_book 145 сд. p50=113.3 мс | bybit_spot 2 сд. p50=115.5 мс | bybit_spot_book 73 сд. p50=113.5 мс | okx 32 сд. p50=147.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:32:26 [pm] T-153.5s Up 0.13/0.14 Down 0.86/0.87 ptb=83176.5 | CLOB 5022 сообщ., задержка p50/p90=42.2/43.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792571546531 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=1.4/1.7 мс
08:32:36 [cex] Binance 205 сд. задержка p50/p90=146.4/147.2 мс | Coinbase 43 задержка p50=79.0 мс | смещение часов +21.7 мс | lag loop p99/max=2.0/2.0 мс
08:32:36 [cex] binance_futures 89 сд. p50=148.9 мс | bybit 107 сд. p50=116.0 мс | bybit_book 159 сд. p50=113.2 мс | bybit_spot 116 сд. p50=123.5 мс | bybit_spot_book 65 сд. p50=113.6 мс | okx 56 сд. p50=148.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:32:36 [pm] T-143.5s Up 0.08/0.09 Down 0.91/0.92 ptb=83176.5 | CLOB 5382 сообщ., задержка p50/p90=42.2/43.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792571556532 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.4/1.4 мс
08:32:46 [cex] Binance 22 сд. задержка p50/p90=146.1/146.4 мс | Coinbase 24 задержка p50=78.5 мс | смещение часов +21.7 мс | lag loop p99/max=2.2/2.2 мс
08:32:46 [cex] binance_futures 32 сд. p50=295.8 мс | bybit 47 сд. p50=115.5 мс | bybit_book 140 сд. p50=113.3 мс | bybit_spot 28 сд. p50=116.8 мс | bybit_spot_book 56 сд. p50=113.6 мс | okx 27 сд. p50=147.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:32:46 [pm] T-133.5s Up 0.06/0.07 Down 0.93/0.94 ptb=83176.5 | CLOB 3653 сообщ., задержка p50/p90=42.2/43.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792571566534 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=1.3/2.0 мс
08:32:56 [cex] Binance 23 сд. задержка p50/p90=146.2/147.2 мс | Coinbase 37 задержка p50=79.0 мс | смещение часов +21.7 мс | lag loop p99/max=2.0/2.1 мс
08:32:56 [cex] binance_futures 55 сд. p50=280.5 мс | bybit 115 сд. p50=115.8 мс | bybit_book 167 сд. p50=113.3 мс | bybit_spot 129 сд. p50=117.0 мс | bybit_spot_book 101 сд. p50=113.6 мс | okx 99 сд. p50=148.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
08:32:56 [pm] T-123.5s Up 0.08/0.09 Down 0.91/0.92 ptb=83176.5 | CLOB 4523 сообщ., задержка p50/p90=42.6/196.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792571576535 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=2.0/2.7 мс
```

Представлено версией кода: 96010db; python 3.12.3
