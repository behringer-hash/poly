# Состояние сервера записи

Время (UTC): 2026-10-19 01:02:03

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 4 days, 17 hours, 38 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         542         854           1         681        1363
Swap:           2047         254        1793
```
- нагрузка CPU (1/5/15 мин): 0.41 / 0.28 / 0.21

## Данные
- файлов: 6258, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 254 | 32 МБ | 1 |
| bn_book | 254 | 3 МБ | 1 |
| bnf_agg | 254 | 49 МБ | 1 |
| bnf_book | 118 | 557 МБ | 486817 |
| bnf_depth5 | 118 | 41 МБ | 486894 |
| bnf_liq | 219 | 145 КБ | 322 |
| bs_trade | 118 | 1 МБ | 486813 |
| by_book1 | 254 | 103 МБ | 1 |
| by_liq | 226 | 120 КБ | 569 |
| by_trade | 254 | 32 МБ | 1 |
| bys_book1 | 138 | 45 МБ | 1 |
| bys_trade | 138 | 18 МБ | 1 |
| cb_ticker | 254 | 30 МБ | 1 |
| clock | 254 | 195 КБ | 39 |
| clock_pm | 254 | 195 КБ | 60 |
| events | 242 | 78 КБ | 1701 |
| events_pm | 253 | 91 КБ | 905 |
| health_cex | 254 | 3 МБ | 7 |
| health_feeds | 254 | 8 МБ | 7 |
| health_pm | 254 | 3 МБ | 6 |
| kr_trade | 118 | 3 МБ | 486813 |
| ok_trade | 253 | 43 МБ | 1 |
| pm_depth | 254 | 50 МБ | 0 |
| pm_rtt | 254 | 2 МБ | 0 |
| pm_top | 254 | 102 МБ | 0 |
| pm_trades | 254 | 73 МБ | 0 |
| rtds | 254 | 16 МБ | 0 |
| windows | 253 | 525 КБ | 180 |

Дни с данными: 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 49, всего 297
- Polymarket CLOB: TCP 6, TLS 54, всего 98
- Polymarket gamma: TCP 5, TLS 49, всего 65

## Последние строки журнала записи
```
01:01:15 [cex] Binance 206 сд. задержка p50/p90=145.5/146.6 мс | Coinbase 49 задержка p50=79.4 мс | смещение часов +21.5 мс | lag loop p99/max=2.1/2.2 мс
01:01:15 [cex] binance_futures 150 сд. p50=150.1 мс | bybit 225 сд. p50=115.3 мс | bybit_book 173 сд. p50=113.4 мс | bybit_spot 199 сд. p50=115.2 мс | bybit_spot_book 118 сд. p50=113.0 мс | okx 129 сд. p50=155.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:01:17 [pm] T-222.6s Up 0.50/0.51 Down 0.49/0.50 ptb=82208.6 | CLOB 10112 сообщ., задержка p50/p90=44.4/46.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792371677409 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=1.3/1.5 мс
01:01:25 [cex] Binance 182 сд. задержка p50/p90=145.7/146.7 мс | Coinbase 42 задержка p50=80.3 мс | смещение часов +21.3 мс | lag loop p99/max=2.1/2.2 мс
01:01:25 [cex] binance_futures 192 сд. p50=146.7 мс | bybit 433 сд. p50=115.8 мс | bybit_book 158 сд. p50=113.4 мс | bybit_spot 261 сд. p50=115.8 мс | bybit_spot_book 206 сд. p50=113.0 мс | okx 224 сд. p50=155.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:01:27 [pm] T-212.6s Up 0.48/0.49 Down 0.51/0.52 ptb=82208.6 | CLOB 9596 сообщ., задержка p50/p90=44.0/45.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792371687410 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=1.8/1.9 мс
01:01:35 [cex] Binance 7 сд. задержка p50/p90=145.1/146.0 мс | Coinbase 37 задержка p50=80.5 мс | смещение часов +21.3 мс | lag loop p99/max=2.1/2.2 мс
01:01:35 [cex] binance_futures 38 сд. p50=294.7 мс | bybit 49 сд. p50=114.6 мс | bybit_book 118 сд. p50=113.3 мс | bybit_spot 5 сд. p50=115.3 мс | bybit_spot_book 81 сд. p50=112.8 мс | okx 34 сд. p50=154.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:01:37 [pm] T-202.6s Up 0.50/0.51 Down 0.49/0.50 ptb=82208.6 | CLOB 9983 сообщ., задержка p50/p90=44.5/46.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792371697412 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=1.5/2.8 мс
01:01:45 [cex] Binance 109 сд. задержка p50/p90=146.2/149.9 мс | Coinbase 59 задержка p50=81.4 мс | смещение часов +21.3 мс | lag loop p99/max=2.1/2.3 мс
01:01:45 [cex] binance_futures 128 сд. p50=148.3 мс | bybit 112 сд. p50=116.8 мс | bybit_book 127 сд. p50=113.3 мс | bybit_spot 123 сд. p50=119.2 мс | bybit_spot_book 57 сд. p50=112.8 мс | okx 150 сд. p50=156.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:01:47 [pm] T-192.6s Up 0.37/0.38 Down 0.62/0.63 ptb=82208.6 | CLOB 8664 сообщ., задержка p50/p90=44.5/64.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792371707413 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=3.0/3.4 мс
01:01:55 [cex] Binance 590 сд. задержка p50/p90=145.3/146.2 мс | Coinbase 53 задержка p50=81.5 мс | смещение часов +21.3 мс | lag loop p99/max=2.1/2.2 мс
01:01:55 [cex] binance_futures 183 сд. p50=147.6 мс | bybit 297 сд. p50=115.0 мс | bybit_book 193 сд. p50=113.3 мс | bybit_spot 354 сд. p50=115.5 мс | bybit_spot_book 151 сд. p50=112.7 мс | okx 193 сд. p50=155.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
01:01:57 [pm] T-182.6s Up 0.36/0.37 Down 0.63/0.64 ptb=82208.6 | CLOB 12384 сообщ., задержка p50/p90=45.2/59.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792371717414 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=42.4 мс | lag loop p99/max=2.1/2.2 мс
```

Представлено версией кода: 88f2465; python 3.12.3
