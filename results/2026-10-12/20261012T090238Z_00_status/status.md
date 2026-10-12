# Состояние сервера записи

Время (UTC): 2026-10-12 09:02:38

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 5 days, 1 hour, 38 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         730         773           2         609        1175
Swap:           2047         105        1942
```
- нагрузка CPU (1/5/15 мин): 0.62 / 0.62 / 0.44

## Данные
- файлов: 2406, всего 592 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 94 | 10 МБ | 1 |
| bn_book | 94 | 854 КБ | 3 |
| bnf_agg | 94 | 15 МБ | 1 |
| bnf_book | 94 | 377 МБ | 0 |
| bnf_depth5 | 94 | 31 МБ | 1 |
| bnf_liq | 80 | 45 КБ | 382 |
| bs_trade | 94 | 1 МБ | 7 |
| by_book1 | 94 | 31 МБ | 1 |
| by_liq | 76 | 41 КБ | 177 |
| by_trade | 94 | 9 МБ | 1 |
| cb_ticker | 94 | 9 МБ | 3 |
| clock | 94 | 71 КБ | 1 |
| clock_pm | 94 | 71 КБ | 20 |
| events | 89 | 31 КБ | 1442 |
| events_pm | 93 | 37 КБ | 631 |
| health_cex | 94 | 977 КБ | 7 |
| health_feeds | 94 | 3 МБ | 7 |
| health_pm | 94 | 1002 КБ | 6 |
| kr_trade | 94 | 2 МБ | 3 |
| ok_trade | 94 | 13 МБ | 1 |
| pm_depth | 94 | 18 МБ | 0 |
| pm_rtt | 94 | 618 КБ | 4 |
| pm_top | 94 | 36 МБ | 0 |
| pm_trades | 94 | 25 МБ | 0 |
| rtds | 94 | 6 МБ | 0 |
| windows | 94 | 191 КБ | 151 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 3, TLS 43, всего 293
- Polymarket CLOB: TCP 10, TLS 45, всего 85
- Polymarket gamma: TCP 5, TLS 40, всего 56

## Последние строки журнала записи
```
09:01:50 [cex] Binance 32 сд. задержка p50/p90=166.5/167.3 мс | Coinbase 7 задержка p50=105.2 мс | смещение часов +42.5 мс | lag loop p99/max=2.1/2.3 мс
09:01:50 [cex] binance_futures 47 сд. p50=315.7 мс | bybit 84 сд. p50=135.7 мс | okx 58 сд. p50=176.5 мс | binance_futures_book 2387 сд. p50=166.8 мс | binance_futures_depth 94 сд. p50=166.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 109 сд. p50=134.2 мс | bybit_liq 0 сд. p50=n/a мс | kraken 3 сд. p50=63.0 мс | bitstamp 1 сд. p50=71.7 мс
09:01:50 [pm] T-189.8s Up 0.85/0.86 Down 0.14/0.15 ptb=83427.0 | CLOB 5281 сообщ., задержка p50/p90=59.5/61.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791795710188 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.9/1.9 мс
09:02:00 [cex] Binance 25 сд. задержка p50/p90=166.4/167.3 мс | Coinbase 10 задержка p50=104.7 мс | смещение часов +42.5 мс | lag loop p99/max=2.2/3.6 мс
09:02:00 [cex] binance_futures 55 сд. p50=300.0 мс | bybit 52 сд. p50=136.5 мс | okx 47 сд. p50=176.2 мс | binance_futures_book 997 сд. p50=166.8 мс | binance_futures_depth 93 сд. p50=167.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 122 сд. p50=134.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 6 сд. p50=65.3 мс | bitstamp 4 сд. p50=69.6 мс
09:02:00 [pm] T-179.8s Up 0.86/0.87 Down 0.13/0.14 ptb=83427.0 | CLOB 3635 сообщ., задержка p50/p90=59.4/60.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791795720189 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.1/1.6 мс
09:02:10 [cex] Binance 19 сд. задержка p50/p90=166.4/166.6 мс | Coinbase 1 задержка p50=102.5 мс | смещение часов +42.5 мс | lag loop p99/max=2.1/2.1 мс
09:02:10 [cex] binance_futures 44 сд. p50=315.6 мс | bybit 25 сд. p50=135.6 мс | okx 45 сд. p50=176.2 мс | binance_futures_book 1049 сд. p50=166.7 мс | binance_futures_depth 96 сд. p50=167.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 86 сд. p50=134.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 2 сд. p50=66.4 мс | bitstamp 11 сд. p50=90.3 мс
09:02:10 [pm] T-169.8s Up 0.87/0.88 Down 0.12/0.13 ptb=83427.0 | CLOB 3110 сообщ., задержка p50/p90=59.4/60.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791795730191 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.1/2.1 мс
09:02:20 [cex] Binance 153 сд. задержка p50/p90=175.5/179.9 мс | Coinbase 45 задержка p50=103.6 мс | смещение часов +42.5 мс | lag loop p99/max=16.2/18.0 мс
09:02:20 [cex] binance_futures 183 сд. p50=175.2 мс | bybit 182 сд. p50=139.5 мс | okx 179 сд. p50=177.4 мс | binance_futures_book 7396 сд. p50=170.0 мс | binance_futures_depth 97 сд. p50=166.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 185 сд. p50=134.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 23 сд. p50=84.8 мс | bitstamp 4 сд. p50=86.6 мс
09:02:20 [pm] T-159.8s Up 0.91/0.92 Down 0.08/0.09 ptb=83427.0 | CLOB 6702 сообщ., задержка p50/p90=42.6/61.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791795740192 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=2.0/3.6 мс
09:02:30 [cex] Binance 246 сд. задержка p50/p90=175.2/180.2 мс | Coinbase 41 задержка p50=104.8 мс | смещение часов +42.5 мс | lag loop p99/max=8.0/11.4 мс
09:02:30 [cex] binance_futures 415 сд. p50=179.9 мс | bybit 361 сд. p50=138.2 мс | okx 205 сд. p50=184.0 мс | binance_futures_book 11816 сд. p50=171.4 мс | binance_futures_depth 97 сд. p50=167.0 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 206 сд. p50=134.3 мс | bybit_liq 0 сд. p50=n/a мс | kraken 49 сд. p50=77.9 мс | bitstamp 8 сд. p50=82.3 мс
09:02:30 [pm] T-149.8s Up 0.97/0.98 Down 0.02/0.03 ptb=83427.0 | CLOB 4762 сообщ., задержка p50/p90=40.4/112.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791795750194 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.5 мс | lag loop p99/max=1.9/2.8 мс
```

Представлено версией кода: 5864ea5; python 3.12.3
