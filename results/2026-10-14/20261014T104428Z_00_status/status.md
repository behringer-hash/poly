# Состояние сервера записи

Время (UTC): 2026-10-14 10:44:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 3 hours, 20 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         589         461           2        1045        1316
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.12 / 0.15 / 0.13

## Данные
- файлов: 3626, всего 925 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 143 | 18 МБ | 4 |
| bn_book | 143 | 2 МБ | 85 |
| bnf_agg | 143 | 27 МБ | 2 |
| bnf_book | 118 | 557 МБ | 89762 |
| bnf_depth5 | 118 | 41 МБ | 89838 |
| bnf_liq | 126 | 77 КБ | 590 |
| bs_trade | 118 | 1 МБ | 89758 |
| by_book1 | 143 | 58 МБ | 2 |
| by_liq | 124 | 65 КБ | 1500 |
| by_trade | 143 | 18 МБ | 2 |
| bys_book1 | 27 | 9 МБ | 2 |
| bys_trade | 27 | 4 МБ | 8 |
| cb_ticker | 143 | 16 МБ | 2 |
| clock | 143 | 111 КБ | 16 |
| clock_pm | 143 | 111 КБ | 15 |
| events | 134 | 45 КБ | 2798 |
| events_pm | 143 | 52 КБ | 1630 |
| health_cex | 143 | 1 МБ | 2 |
| health_feeds | 143 | 5 МБ | 2 |
| health_pm | 143 | 2 МБ | 9 |
| kr_trade | 118 | 3 МБ | 89758 |
| ok_trade | 142 | 24 МБ | 2 |
| pm_depth | 143 | 29 МБ | 1 |
| pm_rtt | 143 | 972 КБ | 3 |
| pm_top | 143 | 58 МБ | 1 |
| pm_trades | 143 | 42 МБ | 1 |
| rtds | 143 | 9 МБ | 1 |
| windows | 143 | 296 КБ | 263 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 36, всего 301
- Polymarket CLOB: TCP 6, TLS 47, всего 89
- Polymarket gamma: TCP 5, TLS 39, всего 62

## Последние строки журнала записи
```
10:43:45 [cex] Binance 20 сд. задержка p50/p90=147.2/148.1 мс | Coinbase 24 задержка p50=81.3 мс | смещение часов +23.0 мс | lag loop p99/max=2.0/2.2 мс
10:43:45 [cex] binance_futures 26 сд. p50=308.1 мс | bybit 19 сд. p50=116.7 мс | bybit_book 129 сд. p50=114.7 мс | bybit_spot 2 сд. p50=117.0 мс | bybit_spot_book 26 сд. p50=114.9 мс | okx 12 сд. p50=154.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:43:47 [pm] T- 72.2s Up 0.75/0.76 Down 0.24/0.25 ptb=83308.6 | CLOB 8866 сообщ., задержка p50/p90=37.3/40.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791974627823 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.4 мс | lag loop p99/max=1.1/1.1 мс
10:43:55 [cex] Binance 16 сд. задержка p50/p90=147.3/148.3 мс | Coinbase 32 задержка p50=81.7 мс | смещение часов +23.0 мс | lag loop p99/max=2.1/2.2 мс
10:43:55 [cex] binance_futures 56 сд. p50=160.1 мс | bybit 94 сд. p50=123.4 мс | bybit_book 76 сд. p50=114.7 мс | bybit_spot 85 сд. p50=119.1 мс | bybit_spot_book 47 сд. p50=114.6 мс | okx 81 сд. p50=155.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:43:57 [pm] T- 62.2s Up 0.28/0.29 Down 0.71/0.72 ptb=83308.6 | CLOB 11108 сообщ., задержка p50/p90=37.5/39.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791974637824 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=1.4/1.7 мс
10:44:05 [cex] Binance 13 сд. задержка p50/p90=147.2/147.3 мс | Coinbase 24 задержка p50=79.8 мс | смещение часов +23.0 мс | lag loop p99/max=2.1/2.1 мс
10:44:05 [cex] binance_futures 20 сд. p50=308.6 мс | bybit 5 сд. p50=115.7 мс | bybit_book 58 сд. p50=114.7 мс | bybit_spot 1 сд. p50=116.2 мс | bybit_spot_book 19 сд. p50=114.8 мс | okx 17 сд. p50=154.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:44:07 [pm] T- 52.2s Up 0.22/0.23 Down 0.77/0.78 ptb=83308.6 | CLOB 5276 сообщ., задержка p50/p90=37.3/38.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791974647826 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=2.8/5.9 мс
10:44:15 [cex] Binance 14 сд. задержка p50/p90=147.1/148.3 мс | Coinbase 16 задержка p50=78.9 мс | смещение часов +20.4 мс | lag loop p99/max=1.9/2.1 мс
10:44:15 [cex] binance_futures 28 сд. p50=305.7 мс | bybit 4 сд. p50=115.9 мс | bybit_book 58 сд. p50=114.5 мс | bybit_spot 1 сд. p50=116.5 мс | bybit_spot_book 19 сд. p50=114.6 мс | okx 6 сд. p50=152.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:44:17 [pm] T- 42.2s Up 0.15/0.16 Down 0.84/0.85 ptb=83308.6 | CLOB 8045 сообщ., задержка p50/p90=43.0/46.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791974657828 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=1.9/2.0 мс
10:44:25 [cex] Binance 22 сд. задержка p50/p90=144.8/145.7 мс | Coinbase 29 задержка p50=77.1 мс | смещение часов +20.4 мс | lag loop p99/max=2.1/2.2 мс
10:44:25 [cex] binance_futures 24 сд. p50=305.6 мс | bybit 6 сд. p50=113.9 мс | bybit_book 55 сд. p50=112.2 мс | bybit_spot 1 сд. p50=114.2 мс | bybit_spot_book 19 сд. p50=112.3 мс | okx 8 сд. p50=152.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:44:27 [pm] T- 32.2s Up 0.08/0.09 Down 0.91/0.92 ptb=83308.6 | CLOB 4868 сообщ., задержка p50/p90=43.0/47.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791974667829 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.5 мс | lag loop p99/max=2.0/2.2 мс
```

Представлено версией кода: ec1316a; python 3.12.3
