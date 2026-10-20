# Состояние сервера записи

Время (UTC): 2026-10-20 10:56:48

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 3 hours, 32 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         825         144           1        1121        1080
Swap:           2047         250        1797
```
- нагрузка CPU (1/5/15 мин): 0.23 / 0.25 / 0.26

## Данные
- файлов: 7051, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 287 | 37 МБ | 1 |
| bn_book | 287 | 4 МБ | 38 |
| bnf_agg | 287 | 57 МБ | 1 |
| bnf_book | 118 | 557 МБ | 608902 |
| bnf_depth5 | 118 | 41 МБ | 608979 |
| bnf_liq | 250 | 161 КБ | 704 |
| bs_trade | 118 | 1 МБ | 608898 |
| by_book1 | 287 | 119 МБ | 1 |
| by_liq | 259 | 129 КБ | 1297 |
| by_trade | 287 | 37 МБ | 5 |
| bys_book1 | 171 | 58 МБ | 1 |
| bys_trade | 171 | 24 МБ | 1 |
| cb_ticker | 287 | 35 МБ | 1 |
| clock | 287 | 223 КБ | 59 |
| clock_pm | 287 | 223 КБ | 27 |
| events | 276 | 88 КБ | 92 |
| events_pm | 287 | 104 КБ | 364 |
| health_cex | 287 | 3 МБ | 7 |
| health_feeds | 287 | 9 МБ | 7 |
| health_pm | 287 | 3 МБ | 3 |
| kr_trade | 118 | 3 МБ | 608898 |
| ok_trade | 286 | 49 МБ | 1 |
| pm_depth | 287 | 58 МБ | 1 |
| pm_rtt | 287 | 2 МБ | 1 |
| pm_top | 287 | 119 МБ | 1 |
| pm_trades | 287 | 83 МБ | 1 |
| rtds | 287 | 19 МБ | 1 |
| windows | 287 | 595 КБ | 13 |

Дни с данными: 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 6, TLS 60, всего 310
- Polymarket CLOB: TCP 4, TLS 46, всего 93
- Polymarket gamma: TCP 4, TLS 48, всего 58

## Последние строки журнала записи
```
10:55:59 [cex] Binance 70 сд. задержка p50/p90=146.2/148.8 мс | Coinbase 2 задержка p50=79.2 мс | смещение часов +22.1 мс | lag loop p99/max=2.1/2.2 мс
10:55:59 [cex] binance_futures 59 сд. p50=147.7 мс | bybit 43 сд. p50=116.6 мс | bybit_book 102 сд. p50=113.2 мс | bybit_spot 189 сд. p50=115.8 мс | bybit_spot_book 87 сд. p50=113.6 мс | okx 80 сд. p50=153.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:56:05 [pm] T-234.2s Up 0.53/0.54 Down 0.46/0.47 ptb=81417.1 | CLOB 6438 сообщ., задержка p50/p90=44.3/48.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792493765821 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=6.4/9.2 мс
10:56:09 [cex] Binance 43 сд. задержка p50/p90=146.2/146.5 мс | Coinbase 25 задержка p50=80.5 мс | смещение часов +22.1 мс | lag loop p99/max=3.6/34.7 мс
10:56:09 [cex] binance_futures 115 сд. p50=148.0 мс | bybit 293 сд. p50=132.0 мс | bybit_book 141 сд. p50=113.2 мс | bybit_spot 245 сд. p50=117.2 мс | bybit_spot_book 90 сд. p50=113.5 мс | okx 56 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:56:15 [pm] T-224.2s Up 0.45/0.46 Down 0.54/0.55 ptb=81417.1 | CLOB 7656 сообщ., задержка p50/p90=44.4/52.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792493775823 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=2.1/12.7 мс
10:56:19 [cex] Binance 20 сд. задержка p50/p90=145.8/146.8 мс | Coinbase 19 задержка p50=80.5 мс | смещение часов +22.1 мс | lag loop p99/max=2.1/2.9 мс
10:56:19 [cex] binance_futures 28 сд. p50=292.5 мс | bybit 58 сд. p50=115.9 мс | bybit_book 94 сд. p50=113.2 мс | bybit_spot 2 сд. p50=115.6 мс | bybit_spot_book 50 сд. p50=113.4 мс | okx 4 сд. p50=153.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:56:25 [pm] T-214.2s Up 0.36/0.37 Down 0.63/0.64 ptb=81417.1 | CLOB 5788 сообщ., задержка p50/p90=45.0/72.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792493785823 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=2.1/2.2 мс
10:56:29 [cex] Binance 13 сд. задержка p50/p90=145.7/146.8 мс | Coinbase 8 задержка p50=81.3 мс | смещение часов +22.1 мс | lag loop p99/max=2.5/2.6 мс
10:56:29 [cex] binance_futures 39 сд. p50=148.6 мс | bybit 51 сд. p50=115.7 мс | bybit_book 103 сд. p50=113.2 мс | bybit_spot 54 сд. p50=117.2 мс | bybit_spot_book 48 сд. p50=113.3 мс | okx 26 сд. p50=153.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:56:35 [pm] T-204.2s Up 0.45/0.46 Down 0.54/0.55 ptb=81417.1 | CLOB 8612 сообщ., задержка p50/p90=39.7/44.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792493795825 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=2.1/2.6 мс
10:56:39 [cex] Binance 19 сд. задержка p50/p90=145.8/146.8 мс | Coinbase 17 задержка p50=80.6 мс | смещение часов +22.1 мс | lag loop p99/max=2.1/2.2 мс
10:56:39 [cex] binance_futures 27 сд. p50=149.4 мс | bybit 55 сд. p50=115.8 мс | bybit_book 103 сд. p50=113.2 мс | bybit_spot 48 сд. p50=116.3 мс | bybit_spot_book 82 сд. p50=113.5 мс | okx 36 сд. p50=153.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
10:56:45 [pm] T-194.2s Up 0.54/0.55 Down 0.45/0.46 ptb=81417.1 | CLOB 7203 сообщ., задержка p50/p90=39.9/60.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792493805827 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.2 мс | lag loop p99/max=1.9/2.1 мс
```

Представлено версией кода: 00dc1d8; python 3.12.3
