# Состояние сервера записи

Время (UTC): 2026-10-28 02:43:46

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 6 days, 19 hours, 19 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         596         697           2         792        1309
Swap:           2047         282        1765
```
- нагрузка CPU (1/5/15 мин): 0.10 / 0.21 / 0.25

## Данные
- файлов: 5810, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 1 |
| bn_book | 242 | 3 МБ | 72 |
| bnf_agg | 242 | 51 МБ | 1 |
| bnf_book | 46 | 347 МБ | 1 |
| bnf_depth5 | 8 | 3 МБ | 1270596 |
| bnf_liq | 213 | 137 КБ | 3462 |
| bs_trade | 8 | 139 КБ | 1270516 |
| by_book1 | 242 | 111 МБ | 1 |
| by_liq | 226 | 99 КБ | 1521 |
| by_trade | 242 | 34 МБ | 1 |
| bys_book1 | 236 | 82 МБ | 1 |
| bys_trade | 236 | 32 МБ | 3 |
| cb_ticker | 242 | 32 МБ | 1 |
| clock | 242 | 188 КБ | 48 |
| clock_pm | 242 | 189 КБ | 6 |
| events | 233 | 75 КБ | 397 |
| events_pm | 241 | 85 КБ | 161 |
| health_cex | 242 | 2 МБ | 5 |
| health_feeds | 242 | 7 МБ | 5 |
| health_pm | 242 | 3 МБ | 6 |
| kr_trade | 8 | 215 КБ | 1270516 |
| ok_trade | 241 | 44 МБ | 3 |
| pm_depth | 242 | 50 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 2 |
| pm_top | 242 | 102 МБ | 0 |
| pm_trades | 242 | 71 МБ | 0 |
| rtds | 242 | 16 МБ | 0 |
| windows | 242 | 501 КБ | 131 |

Дни с данными: 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 36, всего 282
- Polymarket CLOB: TCP 6, TLS 38, всего 81
- Polymarket gamma: TCP 3, TLS 35, всего 43

## Последние строки журнала записи
```
02:42:58 [pm] T-121.7s Up 0.02/0.03 Down 0.97/0.98 ptb=80811.6 | CLOB 1876 сообщ., задержка p50/p90=39.1/40.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793155378309 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=1.9/1.9 мс
02:42:59 [cex] Binance 24 сд. задержка p50/p90=142.9/143.8 мс | Coinbase 11 задержка p50=94.8 мс | смещение часов +19.3 мс | lag loop p99/max=2.1/2.2 мс
02:42:59 [cex] binance_futures 46 сд. p50=292.6 мс | bybit 5 сд. p50=111.7 мс | bybit_book 88 сд. p50=109.9 мс | bybit_spot 8 сд. p50=112.1 мс | bybit_spot_book 49 сд. p50=109.9 мс | okx 27 сд. p50=143.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 704 сд. p50=143.5 мс
02:43:08 [pm] T-111.7s Up 0.01/0.02 Down 0.98/0.99 ptb=80811.6 | CLOB 3745 сообщ., задержка p50/p90=39.2/40.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793155388311 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=2.0/2.3 мс
02:43:09 [cex] Binance 28 сд. задержка p50/p90=142.0/143.0 мс | Coinbase 41 задержка p50=92.6 мс | смещение часов +19.3 мс | lag loop p99/max=2.1/2.7 мс
02:43:09 [cex] binance_futures 67 сд. p50=162.1 мс | bybit 48 сд. p50=113.0 мс | bybit_book 126 сд. p50=109.0 мс | bybit_spot 104 сд. p50=113.1 мс | bybit_spot_book 67 сд. p50=109.0 мс | okx 28 сд. p50=143.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2004 сд. p50=143.3 мс
02:43:18 [pm] T-101.7s Up 0.02/0.03 Down 0.97/0.98 ptb=80811.6 | CLOB 1846 сообщ., задержка p50/p90=39.2/40.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793155398312 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.0/2.0 мс
02:43:19 [cex] Binance 24 сд. задержка p50/p90=142.0/142.9 мс | Coinbase 16 задержка p50=92.4 мс | смещение часов +19.3 мс | lag loop p99/max=2.2/2.2 мс
02:43:19 [cex] binance_futures 31 сд. p50=292.1 мс | bybit 12 сд. p50=111.3 мс | bybit_book 202 сд. p50=108.9 мс | bybit_spot 6 сд. p50=110.8 мс | bybit_spot_book 49 сд. p50=109.1 мс | okx 14 сд. p50=143.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 619 сд. p50=142.8 мс
02:43:28 [pm] T- 91.7s Up 0.03/0.04 Down 0.96/0.97 ptb=80811.6 | CLOB 4571 сообщ., задержка p50/p90=39.5/104.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793155408314 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=2.1/2.2 мс
02:43:29 [cex] Binance 25 сд. задержка p50/p90=142.0/143.1 мс | Coinbase 27 задержка p50=92.3 мс | смещение часов +19.3 мс | lag loop p99/max=6.5/6.9 мс
02:43:29 [cex] binance_futures 137 сд. p50=147.2 мс | bybit 36 сд. p50=111.5 мс | bybit_book 154 сд. p50=108.9 мс | bybit_spot 139 сд. p50=113.7 мс | bybit_spot_book 84 сд. p50=109.1 мс | okx 83 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4542 сд. p50=142.9 мс
02:43:38 [pm] T- 81.7s Up 0.03/0.04 Down 0.96/0.97 ptb=80811.6 | CLOB 2628 сообщ., задержка p50/p90=39.3/42.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793155418316 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=2.2/3.1 мс
02:43:39 [cex] Binance 42 сд. задержка p50/p90=141.9/142.8 мс | Coinbase 15 задержка p50=91.5 мс | смещение часов +19.3 мс | lag loop p99/max=2.2/2.2 мс
02:43:39 [cex] binance_futures 44 сд. p50=291.6 мс | bybit 31 сд. p50=113.9 мс | bybit_book 152 сд. p50=109.0 мс | bybit_spot 134 сд. p50=111.3 мс | bybit_spot_book 83 сд. p50=109.1 мс | okx 40 сд. p50=143.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2041 сд. p50=143.0 мс
```

Представлено версией кода: adb4c8b; python 3.12.3
