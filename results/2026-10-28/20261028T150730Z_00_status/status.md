# Состояние сервера записи

Время (UTC): 2026-10-28 15:07:30

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 4 weeks, 7 hours, 43 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 12 ГБ из 57 ГБ, свободно 45 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         488         919           1         668        1417
Swap:           2047         305        1742
```
- нагрузка CPU (1/5/15 мин): 1.58 / 1.56 / 1.48

## Данные
- файлов: 5824, всего 952 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 243 | 34 МБ | 1 |
| bn_book | 243 | 3 МБ | 3 |
| bnf_agg | 243 | 49 МБ | 1 |
| bnf_book | 51 | 292 МБ | 0 |
| bnf_liq | 211 | 134 КБ | 275 |
| by_book1 | 243 | 106 МБ | 1 |
| by_liq | 226 | 98 КБ | 1949 |
| by_trade | 243 | 32 МБ | 1 |
| bys_book1 | 243 | 81 МБ | 1 |
| bys_trade | 243 | 31 МБ | 3 |
| cb_ticker | 243 | 31 МБ | 1 |
| clock | 243 | 187 КБ | 25 |
| clock_pm | 243 | 188 КБ | 48 |
| events | 234 | 74 КБ | 301 |
| events_pm | 242 | 84 КБ | 409 |
| health_cex | 243 | 2 МБ | 3 |
| health_feeds | 243 | 7 МБ | 3 |
| health_pm | 243 | 3 МБ | 4 |
| ok_trade | 243 | 42 МБ | 1 |
| pm_depth | 243 | 49 МБ | 2 |
| pm_rtt | 243 | 2 МБ | 2 |
| pm_top | 243 | 100 МБ | 2 |
| pm_trades | 243 | 70 МБ | 2 |
| rtds | 243 | 15 МБ | 2 |
| windows | 243 | 499 КБ | 115 |

Дни с данными: 2026-10-15, 2026-10-16, 2026-10-17, 2026-10-18, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26, 2026-10-27, 2026-10-28

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 5, TLS 48, всего 288
- Polymarket CLOB: TCP 7, TLS 44, всего 86
- Polymarket gamma: TCP 4, TLS 45, всего 56

## Последние строки журнала записи
```
15:06:45 [pm] T-194.9s Up 0.78/0.79 Down 0.21/0.22 ptb=80528.9 | CLOB 4649 сообщ., задержка p50/p90=53.2/120.9 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793200005060 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=2.2/2.9 мс
15:06:47 [cex] Binance 113 сд. задержка p50/p90=159.9/170.1 мс | Coinbase 89 задержка p50=109.2 мс | смещение часов +37.5 мс | lag loop p99/max=11.4/18.6 мс
15:06:47 [cex] binance_futures 118 сд. p50=176.9 мс | bybit 83 сд. p50=134.9 мс | bybit_book 187 сд. p50=131.9 мс | bybit_spot 106 сд. p50=146.5 мс | bybit_spot_book 375 сд. p50=132.0 мс | okx 111 сд. p50=180.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 7424 сд. p50=167.7 мс
15:06:55 [pm] T-184.9s Up 0.60/0.61 Down 0.39/0.40 ptb=80528.9 | CLOB 8998 сообщ., задержка p50/p90=53.4/89.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793200015062 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=3.0/9.1 мс
15:06:57 [cex] Binance 130 сд. задержка p50/p90=160.4/168.3 мс | Coinbase 41 задержка p50=110.4 мс | смещение часов +37.5 мс | lag loop p99/max=8.0/9.1 мс
15:06:57 [cex] binance_futures 155 сд. p50=172.4 мс | bybit 114 сд. p50=135.5 мс | bybit_book 234 сд. p50=131.9 мс | bybit_spot 101 сд. p50=137.0 мс | bybit_spot_book 126 сд. p50=132.1 мс | okx 111 сд. p50=179.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5629 сд. p50=157.2 мс
15:07:05 [pm] T-174.9s Up 0.62/0.63 Down 0.37/0.38 ptb=80528.9 | CLOB 9030 сообщ., задержка p50/p90=53.3/79.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793200025064 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=6.5/43.3 мс
15:07:07 [cex] Binance 71 сд. задержка p50/p90=160.0/161.0 мс | Coinbase 30 задержка p50=108.9 мс | смещение часов +37.1 мс | lag loop p99/max=2.2/194.1 мс
15:07:07 [cex] binance_futures 49 сд. p50=305.5 мс | bybit 46 сд. p50=134.1 мс | bybit_book 151 сд. p50=131.8 мс | bybit_spot 7 сд. p50=134.7 мс | bybit_spot_book 41 сд. p50=132.1 мс | okx 34 сд. p50=176.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 1165 сд. p50=156.8 мс
15:07:15 [pm] T-164.9s Up 0.62/0.63 Down 0.37/0.38 ptb=80528.9 | CLOB 6903 сообщ., задержка p50/p90=52.6/54.4 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793200035065 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=1.3/1.8 мс
15:07:17 [cex] Binance 47 сд. задержка p50/p90=159.1/159.9 мс | Coinbase 48 задержка p50=109.8 мс | смещение часов +37.1 мс | lag loop p99/max=2.2/2.2 мс
15:07:17 [cex] binance_futures 37 сд. p50=306.1 мс | bybit 45 сд. p50=134.1 мс | bybit_book 102 сд. p50=131.3 мс | bybit_spot 5 сд. p50=133.3 мс | bybit_spot_book 39 сд. p50=131.6 мс | okx 11 сд. p50=174.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 699 сд. p50=156.3 мс
15:07:25 [pm] T-154.9s Up 0.45/0.46 Down 0.54/0.55 ptb=80528.9 | CLOB 7170 сообщ., задержка p50/p90=54.6/88.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1793200045067 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=46.5 мс | lag loop p99/max=8.5/11.7 мс
15:07:27 [cex] Binance 82 сд. задержка p50/p90=159.4/168.8 мс | Coinbase 26 задержка p50=107.8 мс | смещение часов +37.1 мс | lag loop p99/max=3.2/22.6 мс
15:07:27 [cex] binance_futures 113 сд. p50=159.7 мс | bybit 61 сд. p50=135.3 мс | bybit_book 203 сд. p50=131.4 мс | bybit_spot 96 сд. p50=134.3 мс | bybit_spot_book 80 сд. p50=131.7 мс | okx 83 сд. p50=175.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс | binance_futures_book 5204 сд. p50=156.4 мс
```

Представлено версией кода: 6e8cac9; python 3.12.3
