# Состояние сервера записи

Время (UTC): 2026-10-09 10:16:58

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 2 hours, 53 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         665         893           2         538        1240
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.21 / 0.14 / 0.14

## Данные
- файлов: 592, всего 243 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 23 | 4 МБ | 1 |
| bn_book | 23 | 410 КБ | 13 |
| bnf_agg | 23 | 7 МБ | 1 |
| bnf_book | 23 | 168 МБ | 1 |
| bnf_depth5 | 23 | 11 МБ | 1 |
| bnf_liq | 22 | 21 КБ | 4241 |
| bs_trade | 23 | 451 КБ | 3 |
| by_book1 | 23 | 12 МБ | 1 |
| by_liq | 21 | 22 КБ | 124 |
| by_trade | 23 | 5 МБ | 1 |
| cb_ticker | 23 | 3 МБ | 5 |
| clock | 23 | 17 КБ | 15 |
| clock_pm | 23 | 17 КБ | 20 |
| events | 20 | 7 КБ | 229 |
| events_pm | 23 | 11 КБ | 602 |
| health_cex | 23 | 242 КБ | 1 |
| health_feeds | 23 | 913 КБ | 1 |
| health_pm | 23 | 247 КБ | 4 |
| kr_trade | 23 | 935 КБ | 1 |
| ok_trade | 23 | 6 МБ | 1 |
| pm_depth | 23 | 5 МБ | 2 |
| pm_rtt | 23 | 155 КБ | 6 |
| pm_top | 23 | 10 МБ | 2 |
| pm_trades | 23 | 7 МБ | 2 |
| rtds | 23 | 2 МБ | 2 |
| windows | 23 | 46 КБ | 173 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 37, всего 286
- Polymarket CLOB: TCP 6, TLS 41, всего 79
- Polymarket gamma: TCP 5, TLS 38, всего 49

## Последние строки журнала записи
```
10:16:13 [pm] T-226.2s Up 0.34/0.35 Down 0.65/0.66 ptb=82632.1 | CLOB 4666 сообщ., задержка p50/p90=42.4/53.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791540973813 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.2/1.3 мс
10:16:15 [cex] Binance 21 сд. задержка p50/p90=141.6/142.5 мс | Coinbase 20 задержка p50=227.7 мс | смещение часов +17.5 мс | lag loop p99/max=2.0/2.1 мс
10:16:15 [cex] binance_futures 32 сд. p50=302.8 мс | bybit 30 сд. p50=110.9 мс | okx 19 сд. p50=141.7 мс | binance_futures_book 594 сд. p50=141.8 мс | binance_futures_depth 94 сд. p50=143.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 124 сд. p50=109.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 5 сд. p50=37.0 мс | bitstamp 7 сд. p50=46.4 мс
10:16:23 [pm] T-216.2s Up 0.31/0.32 Down 0.68/0.69 ptb=82632.1 | CLOB 4371 сообщ., задержка p50/p90=46.0/215.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791540983814 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.7/1.8 мс
10:16:25 [cex] Binance 45 сд. задержка p50/p90=141.7/142.9 мс | Coinbase 10 задержка p50=80.0 мс | смещение часов +17.5 мс | lag loop p99/max=2.2/2.2 мс
10:16:25 [cex] binance_futures 53 сд. p50=302.8 мс | bybit 46 сд. p50=111.1 мс | okx 135 сд. p50=144.0 мс | binance_futures_book 652 сд. p50=141.9 мс | binance_futures_depth 97 сд. p50=143.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 136 сд. p50=109.8 мс | bybit_liq 0 сд. p50=n/a мс | kraken 12 сд. p50=39.4 мс | bitstamp 8 сд. p50=46.8 мс
10:16:33 [pm] T-206.2s Up 0.25/0.26 Down 0.74/0.75 ptb=82632.1 | CLOB 4290 сообщ., задержка p50/p90=62.1/114.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791540993815 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.8/1.9 мс
10:16:35 [cex] Binance 30 сд. задержка p50/p90=141.7/145.0 мс | Coinbase 21 задержка p50=81.8 мс | смещение часов +17.5 мс | lag loop p99/max=2.1/2.3 мс
10:16:35 [cex] binance_futures 46 сд. p50=281.7 мс | bybit 34 сд. p50=111.0 мс | okx 20 сд. p50=141.8 мс | binance_futures_book 1016 сд. p50=141.9 мс | binance_futures_depth 95 сд. p50=143.4 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 112 сд. p50=109.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 7 сд. p50=39.4 мс | bitstamp 2 сд. p50=63.8 мс
10:16:43 [pm] T-196.2s Up 0.24/0.25 Down 0.75/0.76 ptb=82632.1 | CLOB 6149 сообщ., задержка p50/p90=225.3/407.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791541003816 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=4.4/6.2 мс
10:16:45 [cex] Binance 39 сд. задержка p50/p90=143.6/147.1 мс | Coinbase 25 задержка p50=79.8 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.2 мс
10:16:45 [cex] binance_futures 52 сд. p50=265.4 мс | bybit 131 сд. p50=112.5 мс | okx 14 сд. p50=141.9 мс | binance_futures_book 901 сд. p50=143.5 мс | binance_futures_depth 95 сд. p50=143.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 163 сд. p50=110.0 мс | bybit_liq 0 сд. p50=n/a мс | kraken 9 сд. p50=55.9 мс | bitstamp 7 сд. p50=51.7 мс
10:16:53 [pm] T-186.2s Up 0.26/0.27 Down 0.73/0.74 ptb=82632.1 | CLOB 5608 сообщ., задержка p50/p90=48.3/83.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791541013817 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=44.8 мс | lag loop p99/max=1.2/1.9 мс
10:16:55 [cex] Binance 23 сд. задержка p50/p90=143.6/144.6 мс | Coinbase 8 задержка p50=84.5 мс | смещение часов +19.5 мс | lag loop p99/max=2.1/2.1 мс
10:16:55 [cex] binance_futures 33 сд. p50=304.8 мс | bybit 66 сд. p50=112.9 мс | okx 15 сд. p50=144.1 мс | binance_futures_book 747 сд. p50=143.9 мс | binance_futures_depth 91 сд. p50=145.5 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 138 сд. p50=111.7 мс | bybit_liq 0 сд. p50=n/a мс | kraken 10 сд. p50=42.3 мс | bitstamp 2 сд. p50=60.0 мс
```

Представлено версией кода: 3f62835; python 3.12.3
