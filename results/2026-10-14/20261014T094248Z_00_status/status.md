# Состояние сервера записи

Время (UTC): 2026-10-14 09:42:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 2 hours, 18 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         565         492           2        1040        1340
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.32 / 0.24 / 0.19

## Данные
- файлов: 3603, всего 922 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 142 | 18 МБ | 1 |
| bn_book | 142 | 2 МБ | 20 |
| bnf_agg | 142 | 27 МБ | 1 |
| bnf_book | 118 | 557 МБ | 86062 |
| bnf_depth5 | 118 | 41 МБ | 86138 |
| bnf_liq | 125 | 75 КБ | 455 |
| bs_trade | 118 | 1 МБ | 86058 |
| by_book1 | 142 | 57 МБ | 1 |
| by_liq | 123 | 64 КБ | 659 |
| by_trade | 142 | 17 МБ | 1 |
| bys_book1 | 26 | 9 МБ | 1 |
| bys_trade | 26 | 4 МБ | 1 |
| cb_ticker | 142 | 16 МБ | 1 |
| clock | 142 | 110 КБ | 5 |
| clock_pm | 142 | 110 КБ | 6 |
| events | 134 | 45 КБ | 1227 |
| events_pm | 142 | 53 КБ | 429 |
| health_cex | 142 | 1 МБ | 1 |
| health_feeds | 142 | 5 МБ | 1 |
| health_pm | 142 | 2 МБ | 10 |
| kr_trade | 118 | 3 МБ | 86058 |
| ok_trade | 141 | 23 МБ | 1 |
| pm_depth | 142 | 29 МБ | 2 |
| pm_rtt | 142 | 964 КБ | 2 |
| pm_top | 142 | 58 МБ | 2 |
| pm_trades | 142 | 42 МБ | 2 |
| rtds | 142 | 9 МБ | 2 |
| windows | 142 | 294 КБ | 103 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 38, всего 288
- Polymarket CLOB: TCP 6, TLS 45, всего 95
- Polymarket gamma: TCP 5, TLS 39, всего 51

## Последние строки журнала записи
```
09:42:05 [cex] Binance 23 сд. задержка p50/p90=153.2/154.1 мс | Coinbase 18 задержка p50=78.6 мс | смещение часов +19.3 мс | lag loop p99/max=2.1/2.2 мс
09:42:05 [cex] binance_futures 87 сд. p50=158.9 мс | bybit 133 сд. p50=114.0 мс | bybit_book 136 сд. p50=111.1 мс | bybit_spot 83 сд. p50=113.6 мс | bybit_spot_book 62 сд. p50=111.2 мс | okx 30 сд. p50=151.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:42:07 [pm] T-172.7s Up 0.21/0.22 Down 0.78/0.79 ptb=83237.9 | CLOB 7113 сообщ., задержка p50/p90=40.2/46.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791970927299 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.1 мс | lag loop p99/max=7.0/8.4 мс
09:42:15 [cex] Binance 44 сд. задержка p50/p90=153.5/154.5 мс | Coinbase 44 задержка p50=76.9 мс | смещение часов +19.3 мс | lag loop p99/max=2.1/2.2 мс
09:42:15 [cex] binance_futures 91 сд. p50=146.1 мс | bybit 67 сд. p50=112.5 мс | bybit_book 105 сд. p50=111.0 мс | bybit_spot 63 сд. p50=112.8 мс | bybit_spot_book 62 сд. p50=111.1 мс | okx 79 сд. p50=151.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:42:17 [pm] T-162.7s Up 0.22/0.23 Down 0.77/0.78 ptb=83237.9 | CLOB 4976 сообщ., задержка p50/p90=39.8/41.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791970937300 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.1 мс | lag loop p99/max=1.2/1.3 мс
09:42:25 [cex] Binance 56 сд. задержка p50/p90=154.1/154.9 мс | Coinbase 30 задержка p50=76.4 мс | смещение часов +19.3 мс | lag loop p99/max=2.1/2.2 мс
09:42:25 [cex] binance_futures 78 сд. p50=170.1 мс | bybit 100 сд. p50=117.1 мс | bybit_book 92 сд. p50=111.1 мс | bybit_spot 96 сд. p50=113.9 мс | bybit_spot_book 48 сд. p50=111.0 мс | okx 76 сд. p50=151.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:42:27 [pm] T-152.7s Up 0.11/0.12 Down 0.88/0.89 ptb=83237.9 | CLOB 5677 сообщ., задержка p50/p90=40.2/51.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791970947301 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=1.8/2.0 мс
09:42:35 [cex] Binance 44 сд. задержка p50/p90=153.7/153.9 мс | Coinbase 31 задержка p50=77.1 мс | смещение часов +19.3 мс | lag loop p99/max=2.0/2.0 мс
09:42:35 [cex] binance_futures 66 сд. p50=177.1 мс | bybit 171 сд. p50=118.1 мс | bybit_book 151 сд. p50=111.1 мс | bybit_spot 68 сд. p50=112.9 мс | bybit_spot_book 79 сд. p50=111.1 мс | okx 44 сд. p50=151.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:42:37 [pm] T-142.7s Up 0.08/0.09 Down 0.91/0.92 ptb=83237.9 | CLOB 4660 сообщ., задержка p50/p90=39.8/41.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791970957302 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=2.0/2.1 мс
09:42:45 [cex] Binance 12 сд. задержка p50/p90=153.5/154.5 мс | Coinbase 34 задержка p50=76.1 мс | смещение часов +20.3 мс | lag loop p99/max=2.2/2.2 мс
09:42:45 [cex] binance_futures 45 сд. p50=292.7 мс | bybit 37 сд. p50=113.2 мс | bybit_book 167 сд. p50=111.9 мс | bybit_spot 2 сд. p50=114.1 мс | bybit_spot_book 59 сд. p50=111.5 мс | okx 19 сд. p50=151.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
09:42:47 [pm] T-132.7s Up 0.07/0.08 Down 0.92/0.93 ptb=83237.9 | CLOB 4431 сообщ., задержка p50/p90=42.2/44.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791970967304 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.9 мс | lag loop p99/max=1.4/1.5 мс
```

Представлено версией кода: ec1316a; python 3.12.3
