# Состояние сервера записи

Время (UTC): 2026-10-27 03:46:08

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 5 days, 20 hours, 22 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         683         792           1         608        1222
Swap:           2047         293        1754
```
- нагрузка CPU (1/5/15 мин): 0.48 / 0.56 / 0.46

## Данные
- файлов: 5836, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 35 МБ | 1 |
| bn_book | 242 | 3 МБ | 1 |
| bnf_agg | 242 | 52 МБ | 1 |
| bnf_book | 46 | 387 МБ | 1 |
| bnf_depth5 | 31 | 12 МБ | 1187938 |
| bnf_liq | 216 | 148 КБ | 47 |
| bs_trade | 31 | 464 КБ | 1187858 |
| by_book1 | 242 | 112 МБ | 1 |
| by_liq | 229 | 109 КБ | 1675 |
| by_trade | 242 | 35 МБ | 1 |
| bys_book1 | 213 | 72 МБ | 1 |
| bys_trade | 213 | 29 МБ | 1 |
| cb_ticker | 242 | 33 МБ | 1 |
| clock | 242 | 188 КБ | 57 |
| clock_pm | 242 | 189 КБ | 7 |
| events | 230 | 73 КБ | 51 |
| events_pm | 241 | 85 КБ | 257 |
| health_cex | 242 | 2 МБ | 1 |
| health_feeds | 242 | 8 МБ | 1 |
| health_pm | 242 | 3 МБ | 1 |
| kr_trade | 31 | 1007 КБ | 1187858 |
| ok_trade | 241 | 45 МБ | 1 |
| pm_depth | 242 | 50 МБ | 1 |
| pm_rtt | 242 | 2 МБ | 5 |
| pm_top | 242 | 103 МБ | 1 |
| pm_trades | 242 | 72 МБ | 1 |
| rtds | 242 | 16 МБ | 1 |
| windows | 242 | 501 КБ | 33 |

Дни с данными: 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 38, всего 284
- Polymarket CLOB: TCP 7, TLS 43, всего 83
- Polymarket gamma: TCP 5, TLS 47, всего 53

## Последние строки журнала записи
```
03:45:25 [cex] Binance 23 сд. задержка p50/p90=146.3/147.2 мс | Coinbase 53 задержка p50=113.6 мс | смещение часов +23.5 мс | lag loop p99/max=2.1/51.0 мс
03:45:25 [cex] binance_futures 25 сд. p50=295.8 мс | bybit 12 сд. p50=114.9 мс | bybit_book 76 сд. p50=113.3 мс | bybit_spot 13 сд. p50=115.2 мс | bybit_spot_book 39 сд. p50=113.5 мс | okx 31 сд. p50=163.1 мс | binance_liq 1 сд. p50=1151.1 мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 515 сд. p50=147.1 мс
03:45:25 [pm] T-274.2s Up 0.42/0.43 Down 0.57/0.58 ptb=79788.6 | CLOB 6038 сообщ., задержка p50/p90=38.9/40.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793072725808 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=1.6/2.1 мс
03:45:35 [cex] Binance 29 сд. задержка p50/p90=146.3/146.7 мс | Coinbase 38 задержка p50=94.3 мс | смещение часов +23.5 мс | lag loop p99/max=2.1/2.2 мс
03:45:35 [cex] binance_futures 19 сд. p50=296.1 мс | bybit 19 сд. p50=114.8 мс | bybit_book 114 сд. p50=113.3 мс | bybit_spot 11 сд. p50=114.9 мс | bybit_spot_book 46 сд. p50=113.3 мс | okx 11 сд. p50=163.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1020 сд. p50=147.2 мс
03:45:35 [pm] T-264.2s Up 0.43/0.44 Down 0.56/0.57 ptb=79788.6 | CLOB 6908 сообщ., задержка p50/p90=38.8/41.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793072735810 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=1.2/1.3 мс
03:45:45 [cex] Binance 18 сд. задержка p50/p90=146.2/147.0 мс | Coinbase 28 задержка p50=93.4 мс | смещение часов +23.5 мс | lag loop p99/max=2.1/2.1 мс
03:45:45 [cex] binance_futures 25 сд. p50=296.0 мс | bybit 39 сд. p50=115.7 мс | bybit_book 148 сд. p50=113.2 мс | bybit_spot 14 сд. p50=115.3 мс | bybit_spot_book 41 сд. p50=113.3 мс | okx 17 сд. p50=163.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 761 сд. p50=147.2 мс
03:45:45 [pm] T-254.2s Up 0.39/0.40 Down 0.60/0.61 ptb=79788.6 | CLOB 4892 сообщ., задержка p50/p90=39.2/46.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793072745812 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.8 мс | lag loop p99/max=2.1/2.1 мс
03:45:55 [cex] Binance 91 сд. задержка p50/p90=146.9/149.0 мс | Coinbase 48 задержка p50=95.4 мс | смещение часов +23.5 мс | lag loop p99/max=2.5/4.4 мс
03:45:55 [cex] binance_futures 142 сд. p50=148.8 мс | bybit 106 сд. p50=115.7 мс | bybit_book 230 сд. p50=113.3 мс | bybit_spot 182 сд. p50=117.3 мс | bybit_spot_book 105 сд. p50=113.4 мс | okx 127 сд. p50=163.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2235 сд. p50=147.9 мс
03:45:55 [pm] T-244.2s Up 0.31/0.33 Down 0.67/0.69 ptb=79788.6 | CLOB 7852 сообщ., задержка p50/p90=39.0/42.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793072755813 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=2.0/2.4 мс
03:46:05 [cex] Binance 76 сд. задержка p50/p90=146.4/147.9 мс | Coinbase 33 задержка p50=93.5 мс | смещение часов +23.5 мс | lag loop p99/max=2.2/7.5 мс
03:46:05 [cex] binance_futures 104 сд. p50=149.8 мс | bybit 93 сд. p50=115.5 мс | bybit_book 313 сд. p50=113.2 мс | bybit_spot 236 сд. p50=116.0 мс | bybit_spot_book 126 сд. p50=113.3 мс | okx 107 сд. p50=163.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3799 сд. p50=147.3 мс
03:46:05 [pm] T-234.2s Up 0.19/0.20 Down 0.80/0.81 ptb=79788.6 | CLOB 7892 сообщ., задержка p50/p90=46.4/47.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793072765814 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.6 мс | lag loop p99/max=1.2/1.2 мс
```

Представлено версией кода: 80591e6; python 3.12.3
