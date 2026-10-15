# Состояние сервера записи

Время (UTC): 2026-10-15 21:41:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 14 hours, 18 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         690         333           2        1131        1215
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.32 / 0.18 / 0.15

## Данные
- файлов: 4461, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 178 | 25 МБ | 1 |
| bn_book | 178 | 2 МБ | 5 |
| bnf_agg | 178 | 38 МБ | 1 |
| bnf_book | 118 | 557 МБ | 215612 |
| bnf_depth5 | 118 | 41 МБ | 215688 |
| bnf_liq | 159 | 111 КБ | 5135 |
| bs_trade | 118 | 1 МБ | 215608 |
| by_book1 | 178 | 79 МБ | 1 |
| by_liq | 158 | 93 КБ | 729 |
| by_trade | 178 | 25 МБ | 3 |
| bys_book1 | 62 | 25 МБ | 1 |
| bys_trade | 62 | 11 МБ | 3 |
| cb_ticker | 178 | 22 МБ | 1 |
| clock | 178 | 138 КБ | 3 |
| clock_pm | 178 | 138 КБ | 5 |
| events | 167 | 54 КБ | 251 |
| events_pm | 178 | 64 КБ | 1104 |
| health_cex | 178 | 2 МБ | 5 |
| health_feeds | 178 | 6 МБ | 5 |
| health_pm | 178 | 2 МБ | 1 |
| kr_trade | 118 | 3 МБ | 215608 |
| ok_trade | 177 | 34 МБ | 1 |
| pm_depth | 178 | 36 МБ | 1 |
| pm_rtt | 178 | 1 МБ | 3 |
| pm_top | 178 | 74 МБ | 1 |
| pm_trades | 178 | 53 МБ | 1 |
| rtds | 178 | 12 МБ | 1 |
| windows | 178 | 368 КБ | 234 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 35, всего 282
- Polymarket CLOB: TCP 8, TLS 44, всего 88
- Polymarket gamma: TCP 5, TLS 37, всего 55

## Последние строки журнала записи
```
21:41:11 [cex] Binance 20 сд. задержка p50/p90=142.0/143.0 мс | Coinbase 20 задержка p50=77.8 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/2.2 мс
21:41:11 [cex] binance_futures 22 сд. p50=291.0 мс | bybit 3 сд. p50=110.9 мс | bybit_book 66 сд. p50=108.7 мс | bybit_spot 3 сд. p50=111.9 мс | bybit_spot_book 30 сд. p50=109.1 мс | okx 12 сд. p50=156.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:41:15 [pm] T-224.2s Up 0.45/0.46 Down 0.54/0.55 ptb=82234.6 | CLOB 4811 сообщ., задержка p50/p90=38.1/39.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792100475783 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.1 мс | lag loop p99/max=1.8/2.1 мс
21:41:21 [cex] Binance 18 сд. задержка p50/p90=142.0/142.2 мс | Coinbase 16 задержка p50=77.7 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/2.2 мс
21:41:21 [cex] binance_futures 31 сд. p50=290.9 мс | bybit 12 сд. p50=111.3 мс | bybit_book 113 сд. p50=108.7 мс | bybit_spot 32 сд. p50=112.0 мс | bybit_spot_book 41 сд. p50=109.0 мс | okx 11 сд. p50=156.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:41:25 [pm] T-214.2s Up 0.44/0.45 Down 0.55/0.56 ptb=82234.6 | CLOB 4305 сообщ., задержка p50/p90=38.3/39.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792100485784 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.1 мс | lag loop p99/max=2.0/2.2 мс
21:41:31 [cex] Binance 53 сд. задержка p50/p90=142.2/143.0 мс | Coinbase 95 задержка p50=78.7 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/2.2 мс
21:41:31 [cex] binance_futures 68 сд. p50=147.3 мс | bybit 53 сд. p50=111.8 мс | bybit_book 143 сд. p50=108.7 мс | bybit_spot 141 сд. p50=112.5 мс | bybit_spot_book 42 сд. p50=109.0 мс | okx 83 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:41:35 [pm] T-204.2s Up 0.63/0.64 Down 0.36/0.37 ptb=82234.6 | CLOB 7789 сообщ., задержка p50/p90=38.2/39.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792100495786 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.1 мс | lag loop p99/max=1.9/2.2 мс
21:41:41 [cex] Binance 53 сд. задержка p50/p90=142.4/144.0 мс | Coinbase 44 задержка p50=78.3 мс | смещение часов +18.7 мс | lag loop p99/max=2.1/2.2 мс
21:41:41 [cex] binance_futures 64 сд. p50=222.5 мс | bybit 28 сд. p50=111.6 мс | bybit_book 108 сд. p50=108.7 мс | bybit_spot 49 сд. p50=111.6 мс | bybit_spot_book 53 сд. p50=109.0 мс | okx 53 сд. p50=156.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:41:45 [pm] T-194.2s Up 0.66/0.67 Down 0.33/0.34 ptb=82234.6 | CLOB 6588 сообщ., задержка p50/p90=38.2/39.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792100505787 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.1 мс | lag loop p99/max=1.6/2.0 мс
21:41:51 [cex] Binance 24 сд. задержка p50/p90=142.0/143.0 мс | Coinbase 39 задержка p50=78.3 мс | смещение часов +18.7 мс | lag loop p99/max=2.0/2.2 мс
21:41:51 [cex] binance_futures 31 сд. p50=290.9 мс | bybit 1 сд. p50=110.5 мс | bybit_book 59 сд. p50=108.7 мс | bybit_spot 3 сд. p50=111.6 мс | bybit_spot_book 21 сд. p50=108.9 мс | okx 50 сд. p50=156.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
21:41:55 [pm] T-184.2s Up 0.50/0.51 Down 0.49/0.50 ptb=82234.6 | CLOB 6791 сообщ., задержка p50/p90=40.2/41.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792100515789 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=45.1 мс | lag loop p99/max=1.7/2.2 мс
```

Представлено версией кода: ec1316a; python 3.12.3
