# Состояние сервера записи

Время (UTC): 2026-10-14 00:27:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 6 days, 17 hours, 3 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         557         635           2         895        1348
Swap:           2047          78        1969
```
- нагрузка CPU (1/5/15 мин): 0.27 / 0.19 / 0.13

## Данные
- файлов: 3388, всего 892 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 133 | 16 МБ | 0 |
| bn_book | 133 | 1 МБ | 75 |
| bnf_agg | 133 | 25 МБ | 0 |
| bnf_book | 118 | 557 МБ | 52742 |
| bnf_depth5 | 118 | 41 МБ | 52818 |
| bnf_liq | 117 | 71 КБ | 3544 |
| bs_trade | 118 | 1 МБ | 52738 |
| by_book1 | 133 | 52 МБ | 0 |
| by_liq | 114 | 61 КБ | 516 |
| by_trade | 133 | 16 МБ | 0 |
| bys_book1 | 17 | 5 МБ | 0 |
| bys_trade | 17 | 2 МБ | 3 |
| cb_ticker | 133 | 15 МБ | 0 |
| clock | 133 | 103 КБ | 9 |
| clock_pm | 133 | 103 КБ | 8 |
| events | 125 | 42 КБ | 479 |
| events_pm | 133 | 50 КБ | 70 |
| health_cex | 133 | 1 МБ | 7 |
| health_feeds | 133 | 5 МБ | 7 |
| health_pm | 133 | 1 МБ | 6 |
| kr_trade | 118 | 3 МБ | 52738 |
| ok_trade | 132 | 21 МБ | 0 |
| pm_depth | 133 | 26 МБ | 1 |
| pm_rtt | 133 | 894 КБ | 3 |
| pm_top | 133 | 53 МБ | 1 |
| pm_trades | 133 | 39 МБ | 3 |
| rtds | 133 | 8 МБ | 1 |
| windows | 133 | 274 КБ | 174 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 46, всего 295
- Polymarket CLOB: TCP 6, TLS 44, всего 85
- Polymarket gamma: TCP 5, TLS 47, всего 58

## Последние строки журнала записи
```
00:26:41 [cex] Binance 8 сд. задержка p50/p90=145.8/146.8 мс | Coinbase 6 задержка p50=81.1 мс | смещение часов +20.8 мс | lag loop p99/max=2.0/2.1 мс
00:26:41 [cex] binance_futures 23 сд. p50=294.1 мс | bybit 15 сд. p50=113.9 мс | bybit_book 102 сд. p50=112.6 мс | bybit_spot 29 сд. p50=114.9 мс | bybit_spot_book 45 сд. p50=112.2 мс | okx 32 сд. p50=147.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:26:42 [pm] T-197.3s Up 0.60/0.61 Down 0.39/0.40 ptb=83331.6 | CLOB 5704 сообщ., задержка p50/p90=36.6/44.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791937602650 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=2.1/2.5 мс
00:26:51 [cex] Binance 7 сд. задержка p50/p90=146.0/146.8 мс | Coinbase 24 задержка p50=81.0 мс | смещение часов +20.8 мс | lag loop p99/max=2.0/2.1 мс
00:26:51 [cex] binance_futures 13 сд. p50=294.1 мс | bybit 33 сд. p50=114.4 мс | bybit_book 85 сд. p50=112.5 мс | bybit_spot 4 сд. p50=114.9 мс | bybit_spot_book 25 сд. p50=112.3 мс | okx 21 сд. p50=148.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:26:52 [pm] T-187.3s Up 0.65/0.66 Down 0.34/0.35 ptb=83331.6 | CLOB 5685 сообщ., задержка p50/p90=36.6/57.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791937612652 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=1.8/2.2 мс
00:27:01 [cex] Binance 9 сд. задержка p50/p90=145.8/145.9 мс | Coinbase 13 задержка p50=80.9 мс | смещение часов +20.8 мс | lag loop p99/max=1.9/2.3 мс
00:27:01 [cex] binance_futures 12 сд. p50=294.2 мс | bybit 6 сд. p50=114.0 мс | bybit_book 92 сд. p50=112.6 мс | bybit_spot 16 сд. p50=115.1 мс | bybit_spot_book 29 сд. p50=112.4 мс | okx 8 сд. p50=148.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:27:02 [pm] T-177.3s Up 0.61/0.62 Down 0.38/0.39 ptb=83331.6 | CLOB 4626 сообщ., задержка p50/p90=36.9/51.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791937622654 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.4 мс | lag loop p99/max=1.9/1.9 мс
00:27:11 [cex] Binance 11 сд. задержка p50/p90=145.8/146.0 мс | Coinbase 38 задержка p50=80.9 мс | смещение часов +20.8 мс | lag loop p99/max=2.2/2.2 мс
00:27:11 [cex] binance_futures 12 сд. p50=294.0 мс | bybit 8 сд. p50=114.5 мс | bybit_book 73 сд. p50=112.5 мс | bybit_spot 4 сд. p50=115.2 мс | bybit_spot_book 15 сд. p50=112.4 мс | okx 5 сд. p50=147.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:27:12 [pm] T-167.3s Up 0.61/0.62 Down 0.38/0.39 ptb=83331.6 | CLOB 5597 сообщ., задержка p50/p90=37.1/77.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791937632655 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.3 мс | lag loop p99/max=1.5/2.2 мс
00:27:21 [cex] Binance 15 сд. задержка p50/p90=145.8/146.8 мс | Coinbase 22 задержка p50=81.0 мс | смещение часов +19.9 мс | lag loop p99/max=2.1/2.2 мс
00:27:21 [cex] binance_futures 12 сд. p50=294.1 мс | bybit 2 сд. p50=114.2 мс | bybit_book 56 сд. p50=112.5 мс | bybit_spot 4 сд. p50=115.1 мс | bybit_spot_book 12 сд. p50=112.1 мс | okx 37 сд. p50=147.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
00:27:22 [pm] T-157.3s Up 0.63/0.64 Down 0.36/0.37 ptb=83331.6 | CLOB 4361 сообщ., задержка p50/p90=36.8/40.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791937642656 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.3 мс | lag loop p99/max=1.9/2.0 мс
```

Представлено версией кода: ec1316a; python 3.12.3
