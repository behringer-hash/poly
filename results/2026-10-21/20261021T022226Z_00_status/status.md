# Состояние сервера записи

Время (UTC): 2026-10-21 02:22:26

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 6 days, 18 hours, 58 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         776         494           1         828        1129
Swap:           2047         475        1572
```
- нагрузка CPU (1/5/15 мин): 0.23 / 0.26 / 0.27

## Данные
- файлов: 7433, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 303 | 39 МБ | 1 |
| bn_book | 303 | 4 МБ | 1 |
| bnf_agg | 303 | 60 МБ | 1 |
| bnf_book | 118 | 557 МБ | 664440 |
| bnf_depth5 | 118 | 41 МБ | 664517 |
| bnf_liq | 266 | 171 КБ | 395 |
| bs_trade | 118 | 1 МБ | 664436 |
| by_book1 | 303 | 127 МБ | 1 |
| by_liq | 274 | 135 КБ | 425 |
| by_trade | 303 | 40 МБ | 1 |
| bys_book1 | 187 | 63 МБ | 1 |
| bys_trade | 187 | 25 МБ | 1 |
| cb_ticker | 303 | 37 МБ | 1 |
| clock | 303 | 234 КБ | 52 |
| clock_pm | 303 | 234 КБ | 27 |
| events | 292 | 93 КБ | 421 |
| events_pm | 302 | 109 КБ | 2363 |
| health_cex | 303 | 3 МБ | 9 |
| health_feeds | 303 | 10 МБ | 9 |
| health_pm | 303 | 3 МБ | 2 |
| kr_trade | 118 | 3 МБ | 664436 |
| ok_trade | 302 | 52 МБ | 1 |
| pm_depth | 303 | 60 МБ | 0 |
| pm_rtt | 303 | 2 МБ | 0 |
| pm_top | 303 | 124 МБ | 0 |
| pm_trades | 303 | 87 МБ | 0 |
| rtds | 303 | 19 МБ | 0 |
| windows | 303 | 625 КБ | 262 |

Дни с данными: 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 8, TLS 47, всего 297
- Polymarket CLOB: TCP 5, TLS 46, всего 91
- Polymarket gamma: TCP 5, TLS 39, всего 51

## Последние строки журнала записи
```
02:21:44 [pm] T-195.7s Up 0.09/0.10 Down 0.90/0.91 ptb=82777.8 | CLOB 3504 сообщ., задержка p50/p90=41.0/42.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792549304254 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.6/1.7 мс
02:21:47 [cex] Binance 92 сд. задержка p50/p90=147.0/148.6 мс | Coinbase 41 задержка p50=80.9 мс | смещение часов +21.8 мс | lag loop p99/max=2.0/2.1 мс
02:21:47 [cex] binance_futures 125 сд. p50=147.4 мс | bybit 163 сд. p50=115.9 мс | bybit_book 133 сд. p50=113.7 мс | bybit_spot 125 сд. p50=116.1 мс | bybit_spot_book 142 сд. p50=114.1 мс | okx 180 сд. p50=150.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
02:21:54 [pm] T-185.7s Up 0.02/0.03 Down 0.97/0.98 ptb=82777.8 | CLOB 5765 сообщ., задержка p50/p90=41.2/45.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792549314255 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.9/2.0 мс
02:21:57 [cex] Binance 83 сд. задержка p50/p90=146.3/147.0 мс | Coinbase 47 задержка p50=80.9 мс | смещение часов +21.8 мс | lag loop p99/max=2.1/2.1 мс
02:21:57 [cex] binance_futures 122 сд. p50=146.9 мс | bybit 178 сд. p50=115.5 мс | bybit_book 155 сд. p50=113.7 мс | bybit_spot 127 сд. p50=117.1 мс | bybit_spot_book 116 сд. p50=114.0 мс | okx 109 сд. p50=150.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
02:22:04 [pm] T-175.7s Up 0.03/0.04 Down 0.96/0.97 ptb=82777.8 | CLOB 3562 сообщ., задержка p50/p90=44.3/55.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792549324257 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=2.0/4.1 мс
02:22:07 [cex] Binance 96 сд. задержка p50/p90=146.2/148.3 мс | Coinbase 45 задержка p50=80.7 мс | смещение часов +21.8 мс | lag loop p99/max=2.2/3.5 мс
02:22:07 [cex] binance_futures 162 сд. p50=150.2 мс | bybit 167 сд. p50=116.0 мс | bybit_book 199 сд. p50=113.8 мс | bybit_spot 229 сд. p50=120.2 мс | bybit_spot_book 131 сд. p50=114.1 мс | okx 66 сд. p50=150.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
02:22:14 [pm] T-165.7s Up 0.03/0.04 Down 0.96/0.97 ptb=82777.8 | CLOB 3563 сообщ., задержка p50/p90=44.1/46.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792549334258 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.5 мс | lag loop p99/max=1.8/2.0 мс
02:22:17 [cex] Binance 110 сд. задержка p50/p90=146.5/147.9 мс | Coinbase 63 задержка p50=81.1 мс | смещение часов +21.8 мс | lag loop p99/max=2.0/2.2 мс
02:22:17 [cex] binance_futures 116 сд. p50=148.9 мс | bybit 163 сд. p50=116.4 мс | bybit_book 263 сд. p50=113.7 мс | bybit_spot 194 сд. p50=127.6 мс | bybit_spot_book 168 сд. p50=114.0 мс | okx 138 сд. p50=150.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
02:22:24 [pm] T-155.7s Up 0.01/0.02 Down 0.98/0.99 ptb=82777.8 | CLOB 3472 сообщ., задержка p50/p90=44.2/47.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792549344259 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.9/2.1 мс
02:22:27 [cex] Binance 99 сд. задержка p50/p90=145.9/147.2 мс | Coinbase 62 задержка p50=80.7 мс | смещение часов +21.8 мс | lag loop p99/max=2.2/2.2 мс
02:22:27 [cex] binance_futures 121 сд. p50=147.6 мс | bybit 153 сд. p50=116.6 мс | bybit_book 182 сд. p50=113.7 мс | bybit_spot 188 сд. p50=131.6 мс | bybit_spot_book 116 сд. p50=114.0 мс | okx 106 сд. p50=150.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: 96010db; python 3.12.3
