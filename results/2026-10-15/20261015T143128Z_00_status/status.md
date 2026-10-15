# Состояние сервера записи

Время (UTC): 2026-10-15 14:31:28

## Службы
- lab-collector: active
- lab-runner.timer: active
- uptime: up 2 weeks, 1 day, 7 hours, 7 minutes
- синхронизация часов: yes

## Ресурсы
- диск: занято 8 ГБ из 57 ГБ, свободно 49 ГБ
- память:
```
total        used        free      shared  buff/cache   available
Mem:            1906         682         359           2        1113        1223
Swap:           2047          54        1993
```
- нагрузка CPU (1/5/15 мин): 0.24 / 0.23 / 0.26

## Данные
- файлов: 4294, всего 1 ГБ

| поток | файлов | размер | последнее обновление, с назад |
|---|---|---|---|
| bn_agg | 171 | 25 МБ | 1 |
| bn_book | 171 | 2 МБ | 1 |
| bnf_agg | 171 | 40 МБ | 1 |
| bnf_book | 118 | 557 МБ | 189782 |
| bnf_depth5 | 118 | 41 МБ | 189858 |
| bnf_liq | 153 | 110 КБ | 19 |
| bs_trade | 118 | 1 МБ | 189778 |
| by_book1 | 171 | 79 МБ | 1 |
| by_liq | 151 | 93 КБ | 21 |
| by_trade | 171 | 29 МБ | 1 |
| bys_book1 | 55 | 25 МБ | 1 |
| bys_trade | 55 | 12 МБ | 1 |
| cb_ticker | 171 | 22 МБ | 1 |
| clock | 171 | 132 КБ | 55 |
| clock_pm | 171 | 132 КБ | 56 |
| events | 160 | 51 КБ | 9074 |
| events_pm | 171 | 61 КБ | 303 |
| health_cex | 171 | 2 МБ | 9 |
| health_feeds | 171 | 6 МБ | 9 |
| health_pm | 171 | 2 МБ | 6 |
| kr_trade | 118 | 3 МБ | 189778 |
| ok_trade | 170 | 36 МБ | 1 |
| pm_depth | 171 | 34 МБ | 2 |
| pm_rtt | 171 | 1 МБ | 6 |
| pm_top | 171 | 70 МБ | 2 |
| pm_trades | 171 | 51 МБ | 2 |
| rtds | 171 | 11 МБ | 2 |
| windows | 171 | 353 КБ | 84 |

Дни с данными: 2026-10-08, 2026-10-09, 2026-10-10, 2026-10-11, 2026-10-12, 2026-10-13, 2026-10-14, 2026-10-15

## Сеть до бирж (время ответа HTTPS, мс)
- Binance REST: TCP 4, TLS 49, всего 311
- Polymarket CLOB: TCP 6, TLS 43, всего 86
- Polymarket gamma: TCP 5, TLS 43, всего 97

## Последние строки журнала записи
```
14:30:42 [pm] T-257.8s Up 0.17/0.18 Down 0.82/0.83 ptb=81117.0 | CLOB 8904 сообщ., задержка p50/p90=41.4/43.5 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792074642178 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.0 мс | lag loop p99/max=1.8/2.0 мс
14:30:48 [cex] Binance 172 сд. задержка p50/p90=143.5/145.4 мс | Coinbase 90 задержка p50=83.3 мс | смещение часов +20.2 мс | lag loop p99/max=2.0/2.1 мс
14:30:48 [cex] binance_futures 248 сд. p50=158.9 мс | bybit 301 сд. p50=112.9 мс | bybit_book 393 сд. p50=110.5 мс | bybit_spot 305 сд. p50=112.8 мс | bybit_spot_book 260 сд. p50=110.3 мс | okx 341 сд. p50=158.9 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:30:52 [pm] T-247.8s Up 0.17/0.18 Down 0.82/0.83 ptb=81117.0 | CLOB 9571 сообщ., задержка p50/p90=41.3/43.8 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792074652179 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.2 мс | lag loop p99/max=1.7/2.9 мс
14:30:58 [cex] Binance 242 сд. задержка p50/p90=143.9/145.0 мс | Coinbase 126 задержка p50=91.2 мс | смещение часов +20.2 мс | lag loop p99/max=1.9/2.0 мс
14:30:58 [cex] binance_futures 326 сд. p50=158.0 мс | bybit 266 сд. p50=113.3 мс | bybit_book 347 сд. p50=110.5 мс | bybit_spot 205 сд. p50=112.9 мс | bybit_spot_book 255 сд. p50=110.3 мс | okx 424 сд. p50=158.8 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:31:02 [pm] T-237.8s Up 0.11/0.12 Down 0.88/0.89 ptb=81117.0 | CLOB 8449 сообщ., задержка p50/p90=41.5/44.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792074662180 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.0 мс | lag loop p99/max=2.1/2.2 мс
14:31:08 [cex] Binance 583 сд. задержка p50/p90=143.7/146.1 мс | Coinbase 70 задержка p50=83.2 мс | смещение часов +20.2 мс | lag loop p99/max=2.0/2.1 мс
14:31:08 [cex] binance_futures 724 сд. p50=158.7 мс | bybit 952 сд. p50=113.2 мс | bybit_book 465 сд. p50=110.5 мс | bybit_spot 340 сд. p50=112.9 мс | bybit_spot_book 344 сд. p50=110.3 мс | okx 999 сд. p50=159.2 мс | binance_liq 3 сд. p50=1077.2 мс | bybit_liq 1 сд. p50=188.9 мс
14:31:12 [pm] T-227.8s Up 0.09/0.10 Down 0.90/0.91 ptb=81117.0 | CLOB 7747 сообщ., задержка p50/p90=41.3/44.2 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792074672182 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.0 мс | lag loop p99/max=1.1/1.3 мс
14:31:18 [cex] Binance 157 сд. задержка p50/p90=143.4/144.5 мс | Coinbase 65 задержка p50=83.0 мс | смещение часов +20.2 мс | lag loop p99/max=2.1/2.2 мс
14:31:18 [cex] binance_futures 280 сд. p50=158.5 мс | bybit 463 сд. p50=112.9 мс | bybit_book 472 сд. p50=110.5 мс | bybit_spot 303 сд. p50=112.6 мс | bybit_spot_book 297 сд. p50=110.3 мс | okx 445 сд. p50=158.7 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
14:31:22 [pm] T-217.8s Up 0.14/0.15 Down 0.85/0.86 ptb=81117.0 | CLOB 7870 сообщ., задержка p50/p90=43.3/141.1 мс | BTC[bybit]=n/a (0 обн., задержка p50 n/a мс, тишина 1792074682183 мс; Bybit сообщ.: книга 0, сделки 0) coinbase=n/a p50=n/aмс binance_fut_book=n/a p50=n/aмс binance_fut=n/a p50=n/aмс σ=5.00 (разогрев) базис=n/a | HTTPS до CLOB p50=48.0 мс | lag loop p99/max=1.4/1.8 мс
14:31:28 [cex] Binance 175 сд. задержка p50/p90=143.5/144.3 мс | Coinbase 64 задержка p50=83.5 мс | смещение часов +20.2 мс | lag loop p99/max=2.1/2.1 мс
14:31:28 [cex] binance_futures 305 сд. p50=158.6 мс | bybit 256 сд. p50=112.9 мс | bybit_book 413 сд. p50=110.5 мс | bybit_spot 168 сд. p50=112.7 мс | bybit_spot_book 262 сд. p50=110.3 мс | okx 335 сд. p50=159.2 мс | binance_liq 0 сд. p50=n/a мс | bybit_liq 0 сд. p50=n/a мс
```

Представлено версией кода: ec1316a; python 3.12.3
