# Состояние сервера записи

Время (UTC): 2026-10-15 12:28:10

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 5 hours, 4 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         683         397           2        1073        1222
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.23 / 0.25 / 0.21

## Данные
- файлов: 4247, всего 1015 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 169 | 23 МБ | 2 |
| bn_book | 169 | 2 МБ | 2 |
| bnf_agg | 169 | 35 МБ | 2 |
| bnf_book | 118 | 557 МБ | 182384 |
| bnf_depth5 | 118 | 41 МБ | 182461 |
| bnf_liq | 151 | 101 КБ | 181 |
| bs_trade | 118 | 1 МБ | 182380 |
| by_book1 | 169 | 73 МБ | 2 |
| by_liq | 148 | 83 КБ | 1999 |
| by_trade | 169 | 23 МБ | 2 |
| bys_book1 | 53 | 21 МБ | 2 |
| bys_trade | 53 | 9 МБ | 2 |
| cb_ticker | 169 | 21 МБ | 2 |
| clock | 169 | 130 КБ | 40 |
| clock_pm | 169 | 131 КБ | 39 |
| events | 160 | 51 КБ | 1676 |
| events_pm | 169 | 62 КБ | 81 |
| health_cex | 169 | 2 МБ | 2 |
| health_feeds | 169 | 6 МБ | 2 |
| health_pm | 169 | 2 МБ | 9 |
| kr_trade | 118 | 3 МБ | 182380 |
| ok_trade | 168 | 31 МБ | 2 |
| pm_depth | 169 | 34 МБ | 1 |
| pm_rtt | 169 | 1 МБ | 3 |
| pm_top | 169 | 69 МБ | 1 |
| pm_trades | 169 | 50 МБ | 1 |
| rtds | 169 | 11 МБ | 1 |
| windows | 169 | 348 КБ | 186 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 45, всего 294
- Polymarket CLOB: TCP 6, TLS 42, всего 159
- Polymarket gamma: TCP 5, TLS 45, всего 58

## Последние строки журнала записи
```
12:27:27 [cex] Binance 118 сд. задержка p50/p90=155.6/156.9 мс | Coinbase 61 задержка p50=82.6 мс | смещение часов +19.1 мс | lag loop p99/max=2.1/2.1 мс
12:27:27 [cex] binance_futures 265 сд. p50=144.5 мс | bybit 238 сд. p50=113.6 мс | bybit_book 251 сд. p50=110.9 мс | bybit_spot 151 сд. p50=112.8 мс | bybit_spot_book 178 сд. p50=110.7 мс | okx 285 сд. p50=157.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
12:27:30 [pm] T-149.0s Up 0.31/0.32 Down 0.68/0.69 ptb=80939.8 | CLOB 8577 сообщ., задержка p50/p90=39.3/46.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792067250974 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=1.5/1.8 мс
12:27:37 [cex] Binance 50 сд. задержка p50/p90=155.2/156.3 мс | Coinbase 56 задержка p50=82.0 мс | смещение часов +18.3 мс | lag loop p99/max=1.9/2.0 мс
12:27:37 [cex] binance_futures 142 сд. p50=143.8 мс | bybit 137 сд. p50=112.7 мс | bybit_book 212 сд. p50=110.2 мс | bybit_spot 122 сд. p50=112.2 мс | bybit_spot_book 175 сд. p50=110.2 мс | okx 41 сд. p50=156.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
12:27:40 [pm] T-139.0s Up 0.33/0.34 Down 0.66/0.67 ptb=80939.8 | CLOB 10280 сообщ., задержка p50/p90=38.0/40.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792067260975 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.1 мс | lag loop p99/max=1.8/2.1 мс
12:27:47 [cex] Binance 40 сд. задержка p50/p90=154.5/155.6 мс | Coinbase 44 задержка p50=80.3 мс | смещение часов +18.3 мс | lag loop p99/max=2.1/2.3 мс
12:27:47 [cex] binance_futures 112 сд. p50=144.9 мс | bybit 90 сд. p50=112.6 мс | bybit_book 173 сд. p50=110.2 мс | bybit_spot 39 сд. p50=112.9 мс | bybit_spot_book 105 сд. p50=110.0 мс | okx 38 сд. p50=156.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
12:27:50 [pm] T-129.0s Up 0.34/0.37 Down 0.63/0.66 ptb=80939.8 | CLOB 8537 сообщ., задержка p50/p90=38.1/39.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792067270977 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=2.4/4.9 мс
12:27:57 [cex] Binance 130 сд. задержка p50/p90=154.8/156.2 мс | Coinbase 62 задержка p50=85.0 мс | смещение часов +18.3 мс | lag loop p99/max=2.0/2.1 мс
12:27:57 [cex] binance_futures 230 сд. p50=143.9 мс | bybit 301 сд. p50=113.0 мс | bybit_book 273 сд. p50=110.2 мс | bybit_spot 216 сд. p50=112.3 мс | bybit_spot_book 174 сд. p50=110.0 мс | okx 167 сд. p50=156.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
12:28:00 [pm] T-119.0s Up 0.55/0.56 Down 0.44/0.45 ptb=80939.8 | CLOB 12655 сообщ., задержка p50/p90=38.3/42.0 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792067280978 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=1.2/1.5 мс
12:28:07 [cex] Binance 162 сд. задержка p50/p90=156.2/158.0 мс | Coinbase 184 задержка p50=177.2 мс | смещение часов +18.3 мс | lag loop p99/max=4.0/6.2 мс
12:28:07 [cex] binance_futures 175 сд. p50=143.7 мс | bybit 171 сд. p50=113.1 мс | bybit_book 259 сд. p50=110.2 мс | bybit_spot 146 сд. p50=112.0 мс | bybit_spot_book 148 сд. p50=109.9 мс | okx 161 сд. p50=157.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
12:28:10 [pm] T-109.0s Up 0.72/0.73 Down 0.27/0.28 ptb=80939.8 | CLOB 9633 сообщ., задержка p50/p90=37.6/38.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792067290979 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.0 мс | lag loop p99/max=7.2/7.5 мс
```

Представлено версией кода: ec1316a; python 3.12.3
