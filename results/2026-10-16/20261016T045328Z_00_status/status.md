# Состояние сервера записи

Время (UTC): 2026-10-16 04:53:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 21 hours, 29 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         728         305           2        1160        1177
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.22 / 0.20 / 0.18

## Данные
- файлов: 4629, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 185 | 26 МБ | 2 |
| bn_book | 185 | 2 МБ | 2 |
| bnf_agg | 185 | 39 МБ | 2 |
| bnf_book | 118 | 557 МБ | 241502 |
| bnf_depth5 | 118 | 41 МБ | 241578 |
| bnf_liq | 167 | 114 КБ | 1530 |
| bs_trade | 118 | 1 МБ | 241498 |
| by_book1 | 185 | 83 МБ | 2 |
| by_liq | 164 | 96 КБ | 3740 |
| by_trade | 185 | 26 МБ | 2 |
| bys_book1 | 69 | 29 МБ | 2 |
| bys_trade | 69 | 12 МБ | 2 |
| cb_ticker | 185 | 24 МБ | 2 |
| clock | 185 | 144 КБ | 18 |
| clock_pm | 185 | 144 КБ | 18 |
| events | 174 | 56 КБ | 304 |
| events_pm | 185 | 66 КБ | 1804 |
| health_cex | 185 | 2 МБ | 2 |
| health_feeds | 185 | 7 МБ | 2 |
| health_pm | 185 | 2 МБ | 8 |
| kr_trade | 118 | 3 МБ | 241498 |
| ok_trade | 184 | 35 МБ | 2 |
| pm_depth | 185 | 38 МБ | 2 |
| pm_rtt | 185 | 1 МБ | 4 |
| pm_top | 185 | 78 МБ | 2 |
| pm_trades | 185 | 56 МБ | 2 |
| rtds | 185 | 12 МБ | 2 |
| windows | 185 | 383 КБ | 144 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-16

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 40, всего 288
- Polymarket CLOB: TCP 7, TLS 43, всего 86
- Polymarket gamma: TCP 5, TLS 42, всего 54

## Последние строки журнала записи
```
04:52:39 [pm] T-140.6s Up 0.74/0.75 Down 0.25/0.26 ptb=81930.3 | CLOB 9332 сообщ., задержка p50/p90=38.3/39.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792126359415 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.1 мс | lag loop p99/max=1.5/2.2 мс
04:52:44 [cex] Binance 36 сд. задержка p50/p90=143.7/144.7 мс | Coinbase 57 задержка p50=77.9 мс | смещение часов +18.7 мс | lag loop p99/max=2.0/2.1 мс
04:52:44 [cex] binance_futures 51 сд. p50=143.2 мс | bybit 26 сд. p50=113.0 мс | bybit_book 95 сд. p50=110.7 мс | bybit_spot 147 сд. p50=112.9 мс | bybit_spot_book 223 сд. p50=110.0 мс | okx 64 сд. p50=144.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:52:49 [pm] T-130.6s Up 0.76/0.77 Down 0.23/0.24 ptb=81930.3 | CLOB 5150 сообщ., задержка p50/p90=38.2/39.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792126369416 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.7/1.8 мс
04:52:54 [cex] Binance 15 сд. задержка p50/p90=143.4/143.6 мс | Coinbase 42 задержка p50=77.9 мс | смещение часов +18.7 мс | lag loop p99/max=2.2/2.2 мс
04:52:54 [cex] binance_futures 11 сд. p50=292.2 мс | bybit 4 сд. p50=112.4 мс | bybit_book 65 сд. p50=110.7 мс | bybit_spot 4 сд. p50=113.0 мс | bybit_spot_book 222 сд. p50=110.0 мс | okx 20 сд. p50=143.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:52:59 [pm] T-120.6s Up 0.80/0.81 Down 0.19/0.20 ptb=81930.3 | CLOB 6547 сообщ., задержка p50/p90=38.3/39.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792126379417 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.3/2.1 мс
04:53:04 [cex] Binance 97 сд. задержка p50/p90=143.7/144.4 мс | Coinbase 61 задержка p50=78.2 мс | смещение часов +18.7 мс | lag loop p99/max=4.1/4.6 мс
04:53:04 [cex] binance_futures 73 сд. p50=144.0 мс | bybit 44 сд. p50=112.6 мс | bybit_book 194 сд. p50=110.7 мс | bybit_spot 188 сд. p50=113.4 мс | bybit_spot_book 422 сд. p50=110.0 мс | okx 78 сд. p50=144.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:53:09 [pm] T-110.6s Up 0.90/0.91 Down 0.09/0.10 ptb=81930.3 | CLOB 8915 сообщ., задержка p50/p90=38.8/55.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792126389418 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=3.4/4.7 мс
04:53:14 [cex] Binance 17 сд. задержка p50/p90=146.0/146.2 мс | Coinbase 45 задержка p50=79.8 мс | смещение часов +21.4 мс | lag loop p99/max=2.1/2.2 мс
04:53:14 [cex] binance_futures 24 сд. p50=293.6 мс | bybit 22 сд. p50=115.2 мс | bybit_book 143 сд. p50=113.2 мс | bybit_spot 110 сд. p50=116.5 мс | bybit_spot_book 159 сд. p50=112.5 мс | okx 44 сд. p50=147.3 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
04:53:19 [pm] T-100.6s Up 0.88/0.89 Down 0.11/0.12 ptb=81930.3 | CLOB 7815 сообщ., задержка p50/p90=40.3/42.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792126399420 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.2 мс | lag loop p99/max=1.5/1.8 мс
04:53:24 [cex] Binance 11 сд. задержка p50/p90=146.1/146.3 мс | Coinbase 34 задержка p50=80.7 мс | смещение часов +21.4 мс | lag loop p99/max=2.2/2.2 мс
04:53:24 [cex] binance_futures 36 сд. p50=146.5 мс | bybit 18 сд. p50=115.5 мс | bybit_book 96 сд. p50=113.4 мс | bybit_spot 35 сд. p50=115.7 мс | bybit_spot_book 37 сд. p50=112.8 мс | okx 18 сд. p50=147.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: ec1316a; python 3.12.3
