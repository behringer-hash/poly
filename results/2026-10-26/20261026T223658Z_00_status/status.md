# Состояние сервера записи

Время (UTC): 2026-10-26 22:36:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 3 weeks, 5 days, 15 hours, 13 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 11 ГБ из 57 ГБ, свободно 46 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         664         914           1         499        1241
Swap:           2047         293        1754
```
- нагрузка CPU (1/5/15 мин): 0.72 / 0.42 / 0.36

## Данные
- файлов: 5841, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 242 | 34 МБ | 2 |
| bn_book | 242 | 3 МБ | 10 |
| bnf_agg | 242 | 51 МБ | 2 |
| bnf_book | 46 | 361 МБ | 0 |
| bnf_depth5 | 36 | 14 МБ | 1169389 |
| bnf_liq | 216 | 147 КБ | 2885 |
| bs_trade | 36 | 526 КБ | 1169308 |
| by_book1 | 242 | 109 МБ | 2 |
| by_liq | 229 | 107 КБ | 188 |
| by_trade | 242 | 34 МБ | 2 |
| bys_book1 | 208 | 70 МБ | 2 |
| bys_trade | 208 | 28 МБ | 12 |
| cb_ticker | 242 | 33 МБ | 2 |
| clock | 242 | 188 КБ | 12 |
| clock_pm | 242 | 188 КБ | 22 |
| events | 230 | 72 КБ | 438 |
| events_pm | 241 | 84 КБ | 114 |
| health_cex | 242 | 2 МБ | 6 |
| health_feeds | 242 | 8 МБ | 6 |
| health_pm | 242 | 3 МБ | 4 |
| kr_trade | 36 | 1 МБ | 1169308 |
| ok_trade | 241 | 45 МБ | 2 |
| pm_depth | 242 | 49 МБ | 0 |
| pm_rtt | 242 | 2 МБ | 0 |
| pm_top | 242 | 103 МБ | 0 |
| pm_trades | 242 | 72 МБ | 0 |
| rtds | 242 | 16 МБ | 0 |
| windows | 242 | 500 КБ | 204 |

Дни с данными: 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 49, всего 295
- Polymarket CLOB: TCP 5, TLS 45, всего 87
- Polymarket gamma: TCP 6, TLS 54, всего 62

## Последние строки журнала записи
```
22:36:12 [cex] Binance 268 сд. задержка p50/p90=145.1/157.5 мс | Coinbase 49 задержка p50=79.5 мс | смещение часов +18.9 мс | lag loop p99/max=2.5/2.7 мс
22:36:12 [cex] binance_futures 57 сд. p50=154.6 мс | bybit 84 сд. p50=111.0 мс | bybit_book 139 сд. p50=108.6 мс | bybit_spot 51 сд. p50=110.7 мс | bybit_spot_book 76 сд. p50=109.4 мс | okx 54 сд. p50=161.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 3430 сд. p50=143.0 мс
22:36:13 [pm] T-227.0s Up 0.74/0.75 Down 0.25/0.26 ptb=79810.9 | CLOB 7174 сообщ., задержка p50/p90=40.4/42.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793054173025 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.3 мс | lag loop p99/max=2.0/2.4 мс
22:36:22 [cex] Binance 243 сд. задержка p50/p90=142.7/145.9 мс | Coinbase 52 задержка p50=80.4 мс | смещение часов +18.9 мс | lag loop p99/max=4.4/7.6 мс
22:36:22 [cex] binance_futures 102 сд. p50=144.9 мс | bybit 63 сд. p50=111.5 мс | bybit_book 112 сд. p50=108.6 мс | bybit_spot 102 сд. p50=119.9 мс | bybit_spot_book 106 сд. p50=109.4 мс | okx 52 сд. p50=160.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4099 сд. p50=146.4 мс
22:36:23 [pm] T-217.0s Up 0.73/0.74 Down 0.26/0.27 ptb=79810.9 | CLOB 4989 сообщ., задержка p50/p90=40.2/42.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793054183027 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=2.0/2.4 мс
22:36:32 [cex] Binance 109 сд. задержка p50/p90=142.7/166.9 мс | Coinbase 40 задержка p50=82.4 мс | смещение часов +18.9 мс | lag loop p99/max=2.3/27.3 мс
22:36:32 [cex] binance_futures 153 сд. p50=144.4 мс | bybit 121 сд. p50=111.5 мс | bybit_book 168 сд. p50=108.6 мс | bybit_spot 232 сд. p50=111.8 мс | bybit_spot_book 80 сд. p50=109.5 мс | okx 227 сд. p50=160.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 6538 сд. p50=143.6 мс
22:36:33 [pm] T-207.0s Up 0.60/0.61 Down 0.39/0.40 ptb=79810.9 | CLOB 7839 сообщ., задержка p50/p90=40.1/43.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793054193029 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=1.9/1.9 мс
22:36:42 [cex] Binance 83 сд. задержка p50/p90=144.1/145.0 мс | Coinbase 61 задержка p50=101.6 мс | смещение часов +18.9 мс | lag loop p99/max=1.8/1.9 мс
22:36:42 [cex] binance_futures 103 сд. p50=146.3 мс | bybit 78 сд. p50=111.1 мс | bybit_book 131 сд. p50=108.5 мс | bybit_spot 122 сд. p50=116.3 мс | bybit_spot_book 59 сд. p50=109.6 мс | okx 102 сд. p50=161.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 2219 сд. p50=163.3 мс
22:36:43 [pm] T-197.0s Up 0.51/0.52 Down 0.48/0.49 ptb=79810.9 | CLOB 8376 сообщ., задержка p50/p90=42.5/45.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793054203030 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.2 мс | lag loop p99/max=3.2/3.3 мс
22:36:52 [cex] Binance 64 сд. задержка p50/p90=142.7/146.6 мс | Coinbase 45 задержка p50=80.9 мс | смещение часов +19.0 мс | lag loop p99/max=5.3/18.5 мс
22:36:52 [cex] binance_futures 76 сд. p50=147.4 мс | bybit 360 сд. p50=116.1 мс | bybit_book 247 сд. p50=108.6 мс | bybit_spot 85 сд. p50=111.5 мс | bybit_spot_book 83 сд. p50=109.5 мс | okx 54 сд. p50=166.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 4618 сд. p50=142.7 мс
22:36:53 [pm] T-187.0s Up 0.34/0.35 Down 0.65/0.66 ptb=79810.9 | CLOB 9434 сообщ., задержка p50/p90=42.3/43.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793054213032 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=43.1 мс | lag loop p99/max=1.5/1.7 мс
```

Представлено версией кода: 80591e6; python 3.12.3
