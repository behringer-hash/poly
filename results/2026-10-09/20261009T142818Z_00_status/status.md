# Состояние сервера записи

Время (UTC): 2026-10-09 14:28:18

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 1 week, 2 days, 7 hours, 4 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 7 ГБ из 57 ГБ, свободно 50 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         663         734           2         702        1242
Swap:           2047           6        2041
```
- нагрузка CPU (1/5/15 мин): 0.50 / 0.40 / 0.37

## Данные
- файлов: 697, всего 376 МБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 27 | 6 МБ | 1 |
| bn_book | 27 | 567 КБ | 7 |
| bnf_agg | 27 | 10 МБ | 1 |
| bnf_book | 27 | 273 МБ | 0 |
| bnf_depth5 | 27 | 14 МБ | 1 |
| bnf_liq | 27 | 26 КБ | 280 |
| bs_trade | 27 | 600 КБ | 11 |
| by_book1 | 27 | 18 МБ | 1 |
| by_liq | 25 | 27 КБ | 282 |
| by_trade | 27 | 8 МБ | 1 |
| cb_ticker | 27 | 5 МБ | 1 |
| clock | 27 | 21 КБ | 17 |
| clock_pm | 27 | 21 КБ | 26 |
| events | 24 | 8 КБ | 31 |
| events_pm | 27 | 15 КБ | 291 |
| health_cex | 27 | 291 КБ | 9 |
| health_feeds | 27 | 1 МБ | 9 |
| health_pm | 27 | 298 КБ | 2 |
| kr_trade | 27 | 1 МБ | 1 |
| ok_trade | 27 | 9 МБ | 1 |
| pm_depth | 27 | 6 МБ | 2 |
| pm_rtt | 27 | 190 КБ | 4 |
| pm_top | 27 | 13 МБ | 2 |
| pm_trades | 27 | 9 МБ | 2 |
| rtds | 27 | 2 МБ | 2 |
| windows | 27 | 56 КБ | 14 |

Дни с данными: 2026-10-08, 2026-10-09

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 42, всего 301
- Polymarket CLOB: TCP 5, TLS 42, всего 85
- Polymarket gamma: TCP 5, TLS 41, всего 53

## Последние строки журнала записи
```
14:27:38 [cex] binance_futures 224 сд. p50=149.0 мс | bybit 213 сд. p50=113.2 мс | okx 172 сд. p50=156.8 мс | binance_futures_book 3136 сд. p50=144.3 мс | binance_futures_depth 95 сд. p50=144.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 246 сд. p50=110.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 21 сд. p50=44.4 мс | bitstamp 7 сд. p50=51.7 мс
14:27:42 [cex] okx: ConnectionClosedError(None, None, None) (wss://ws.okx.com:8443/ws/v5/public)
14:27:45 [pm] T-134.1s Up 0.15/0.16 Down 0.84/0.85 ptb=83101.6 | CLOB 6368 сообщ., задержка p50/p90=40.7/115.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791556065942 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.6 мс | lag loop p99/max=2.0/2.1 мс
14:27:46 [cex] okx подключён: wss://ws.okx.com:8443/ws/v5/public
14:27:48 [cex] Binance 123 сд. задержка p50/p90=144.9/147.5 мс | Coinbase 70 задержка p50=81.5 мс | смещение часов +18.6 мс | lag loop p99/max=2.3/2.7 мс
14:27:48 [cex] binance_futures 332 сд. p50=149.1 мс | bybit 239 сд. p50=114.2 мс | okx 264 сд. p50=157.0 мс | binance_futures_book 6557 сд. p50=146.3 мс | binance_futures_depth 97 сд. p50=144.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 302 сд. p50=110.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 19 сд. p50=61.3 мс | bitstamp 22 сд. p50=56.0 мс
14:27:55 [pm] T-124.1s Up 0.26/0.27 Down 0.73/0.74 ptb=83101.6 | CLOB 9098 сообщ., задержка p50/p90=54.0/193.3 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791556075943 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.5 мс | lag loop p99/max=1.7/2.0 мс
14:27:58 [cex] Binance 142 сд. задержка p50/p90=144.1/144.8 мс | Coinbase 59 задержка p50=81.2 мс | смещение часов +18.6 мс | lag loop p99/max=3.0/5.4 мс
14:27:58 [cex] binance_futures 264 сд. p50=150.9 мс | bybit 398 сд. p50=116.2 мс | okx 194 сд. p50=156.7 мс | binance_futures_book 5222 сд. p50=145.4 мс | binance_futures_depth 97 сд. p50=143.6 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 238 сд. p50=110.6 мс | bybit_liq 0 сд. p50=n/a мс | kraken 48 сд. p50=42.4 мс | bitstamp 19 сд. p50=51.7 мс
14:28:05 [pm] T-114.1s Up 0.27/0.28 Down 0.72/0.73 ptb=83101.6 | CLOB 11417 сообщ., задержка p50/p90=134.2/201.7 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791556085944 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.4 мс | lag loop p99/max=3.0/18.2 мс
14:28:08 [cex] Binance 70 сд. задержка p50/p90=147.5/152.3 мс | Coinbase 51 задержка p50=84.7 мс | смещение часов +22.6 мс | lag loop p99/max=8.7/11.6 мс
14:28:08 [cex] binance_futures 185 сд. p50=156.2 мс | bybit 180 сд. p50=116.7 мс | okx 161 сд. p50=159.5 мс | binance_futures_book 5286 сд. p50=148.6 мс | binance_futures_depth 97 сд. p50=147.1 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 236 сд. p50=114.4 мс | bybit_liq 0 сд. p50=n/a мс | kraken 23 сд. p50=38.7 мс | bitstamp 8 сд. p50=54.3 мс
14:28:15 [pm] T-104.1s Up 0.25/0.26 Down 0.74/0.75 ptb=83101.6 | CLOB 9331 сообщ., задержка p50/p90=43.8/166.6 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1791556095945 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=47.4 мс | lag loop p99/max=1.7/2.1 мс
14:28:18 [cex] Binance 59 сд. задержка p50/p90=148.2/153.1 мс | Coinbase 44 задержка p50=85.8 мс | смещение часов +22.6 мс | lag loop p99/max=2.2/51.6 мс
14:28:18 [cex] binance_futures 116 сд. p50=201.8 мс | bybit 132 сд. p50=117.7 мс | okx 105 сд. p50=160.0 мс | binance_futures_book 2882 сд. p50=150.4 мс | binance_futures_depth 97 сд. p50=147.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_book 205 сд. p50=114.5 мс | bybit_liq 0 сд. p50=n/a мс | kraken 14 сд. p50=45.6 мс | bitstamp 3 сд. p50=104.1 мс
```

Представлено версией кода: 7642f87; python 3.12.3
