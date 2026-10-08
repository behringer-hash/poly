"""Настройки и разбор аргументов командной строки."""
from __future__ import annotations

import argparse
from dataclasses import dataclass, field

DEFAULT_WALLET = "0x3048d65321be3497164cdfc2996f94f98a2e7537"


@dataclass
class Variant:
    """Один вариант бумажной стратегии. Каждый вариант × каждая задержка - отдельный бумажный счёт."""
    name: str
    model: str            # "anchor" - сдвиг рыночной цены на ход BTC; "abs" - абсолютная модель TWAP
    edge_thr: float       # минимальный edge после комиссии, $ на шейр
    clip: float = 50.0    # размер ордера, шейров
    cooldown: float = 1.0 # не чаще одного сигнала на сторону за N секунд
    # источник цены BTC для сигнала: "primary" (paper_btc_source), "bybit", "coinbase",
    # или "both" - Bybit и Coinbase одновременно: берётся меньший из двух ходов в пользу стороны
    source: str = "primary"
    # множитель оценки волатильности BTC для этого варианта: >1 - строже (нужен больший ход BTC),
    # <1 - мягче (больше сигналов, но слабее)
    sigma_mult: float = 1.0
    # якорь: "reset" - при любом изменении mid якорь = текущая цена BTC (как раньше);
    # "residual" - якорь сдвигается только на ту часть хода BTC, которую книга реально отыграла
    anchor: str = "reset"
    # модель "momentum": сигнал, если цена источника mom_src за последние mom_window_ms мс сдвинулась
    # больше чем на mom_usd долларов; покупка стороны по направлению хода, лимит = ask + slip_c центов,
    # без проверки справедливой цены. mom_src: "binance_fut", "binance" (спот) или "binance_any" (оба)
    mom_src: str = ""
    mom_window_ms: int = 300
    mom_usd: float = 2.0
    slip_c: float = 0.0
    # порог от волатильности: если mom_k > 0, порог = mom_k * sigma_1s(источника, 5 мин) * sqrt(окно, с)
    mom_k: float = 0.0
    # свой диапазон цен для варианта (0 - общий price_lo/price_hi)
    v_price_lo: float = 0.0
    v_price_hi: float = 0.0
    # модель "imbalance": сигнал, когда дисбаланс верха книги фьючерса Binance (bid_qty-ask_qty)/(сумма)
    # достигает qi_min в сторону покупки; qi_confirm_k > 0 - ещё и ход цены фьючерса за 150 мс >= k*sigma*sqrt(0,15)
    qi_min: float = 0.0
    qi_confirm_k: float = 0.0


@dataclass
class Config:
    data_dir: str = "data"
    wallet: str = DEFAULT_WALLET

    # --- Binance / Coinbase
    binance_ws: str = "wss://data-stream.binance.vision"  # по bn_diag у вас лучший вариант
    binance_rest: str = "https://api.binance.com"
    # потоки Binance: aggTrade (все сделки, есть время биржи), bookTicker (лучшие цены, очень частый),
    # depth5 (топ-5 уровней раз в 100 мс - лёгкая замена bookTicker при слабом канале)
    binance_streams: str = "aggTrade,depth5"
    coinbase: bool = True
    # доп. биржи только для записи: binance_futures, bybit, okx
    # (OKX по умолчанию выключен: до вас идёт с задержкой в секунды и нагружает тот же канал в Азию)
    extra_feeds: list[str] = field(default_factory=lambda: ["binance_futures", "bybit"])
    coinbase_ws: str = "wss://ws-feed.exchange.coinbase.com"

    # --- Polymarket
    gamma_api: str = "https://gamma-api.polymarket.com"
    data_api: str = "https://data-api.polymarket.com"
    clob_ws: str = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
    rtds_ws: str = "wss://ws-live-data.polymarket.com"
    pre_open_sec: float = 15.0     # подключаться к окну заранее
    post_close_sec: float = 10.0   # держать окно после конца
    top_sizes: str = "up"          # писать изменения объёма на лучших ценах: none | up | both
    top_size_throttle_ms: float = 50.0  # ...но не чаще раза в N мс (цены пишутся всегда сразу)
    maker: bool = False             # бумажный мейкер (maker.py)
    maker_show: str = "mm_1c_cons"  # какой мейкерский счёт показывать подробно
    backup_clob: bool = True        # второе (резервное) соединение с книгой; на слабом сервере можно выключить
    depth_hz: float = 2.0          # частота снэпшотов топ-5 уровней книги
    depth_levels: int = 5

    # --- кошелёк
    wallet_enabled: bool = True
    wallet_poll_sec: float = 1.0

    # --- бумажная торговля
    paper: bool = True
    # основной источник цены BTC (волатильность, базис к Chainlink, вариант source="primary");
    # Bybit и Coinbase подключаются всегда, пока включена бумажная торговля
    paper_btc_source: str = "bybit"  # bybit | coinbase | binance | rtds
    # доп. источник цены для бумажной торговли: Binance spot bookTicker (из Стокгольма ~150 мс, из дома медленно)
    paper_binance: bool = False
    # фьючерс Binance (bookTicker + aggTrade) как источник для моментум-вариантов
    paper_binance_fut: bool = False
    # верх книги фьючерса Binance с объёмами (для вариантов imbalance); адреса перебираются по очереди
    paper_binance_fut_book: bool = False
    paper_binance_fut_book_urls: list[str] = field(default_factory=lambda: [
        "wss://fstream.binance.com/public/stream?streams=btcusdt@bookTicker",
        "wss://fstream.binance.com/stream?streams=btcusdt@bookTicker",
        "wss://fstream.binance.com/ws/btcusdt@bookTicker",
        "wss://fstream.binance.com/market/stream?streams=btcusdt@bookTicker"])
    # только сделки: поток bookTicker фьючерсов Binance на /market не приходит (у Binance он на отдельном адресе),
    # а симуляция моментума и так считалась по ценам сделок
    paper_binance_fut_url: str = "wss://fstream.binance.com/market/stream?streams=btcusdt@aggTrade"
    paper_binance_url: str = "wss://stream.binance.com:9443/stream?streams=btcusdt@bookTicker/btcusdt@aggTrade"
    src_max_age: dict = field(default_factory=lambda: {"bybit": 1.5, "coinbase": 2.5, "binance": 1.0, "binance_fut": 1.0, "binance_fut_book": 1.0, "rtds": 3.0})
    fee_rate: float = 0.07
    latencies_ms: list[int] = field(default_factory=lambda: [50, 150, 300, 600])
    slippage_ticks: int = 0             # на сколько тиков выше увиденного ask ставим лимит
    min_T: float = 5.0                  # не торговать, если до конца окна меньше N секунд
    min_elapsed: float = 3.0            # и первые N секунд окна
    price_lo: float = 0.05
    price_hi: float = 0.95
    min_fill: float = 5.0               # минимальный размер ордера Polymarket
    sigma_fallback: float = 5.0
    markout_sec: float = 5.0
    max_btc_age_sec: float = 1.0        # не торговать, если последняя цена BTC старше N секунд
    max_book_lag_ms: float = 400.0      # не торговать, если книга Polymarket доходит к нам с задержкой больше N мс
    max_book_age_ms: float = 2000.0     # не торговать сторону, если её книга не обновлялась дольше N мс
    variants: list[Variant] = field(default_factory=lambda: [
        # имя = порог + источник: by - Bybit, cb - Coinbase, both - подтверждение обоими
        Variant("anc_1c_by", "anchor", 0.01, source="bybit"),
        Variant("anc_2c_by", "anchor", 0.02, source="bybit"),
        Variant("anc_3c_by", "anchor", 0.03, source="bybit"),
        Variant("anc_3c_by_res", "anchor", 0.03, source="bybit", anchor="residual"),
        Variant("anc_2c_by_res", "anchor", 0.02, source="bybit", anchor="residual"),
        Variant("anc_3c_by_s075", "anchor", 0.03, source="bybit", sigma_mult=0.75),
        # моментум: ход Binance за 300 мс -> лимит по ask + 1 ц (нужны --binance-fut и/или --binance-source)
        Variant("mom2_bnf", "momentum", 0.0, mom_src="binance_fut", mom_window_ms=300, mom_usd=2.0, slip_c=1),
        Variant("mom4_bnf", "momentum", 0.0, mom_src="binance_fut", mom_window_ms=300, mom_usd=4.0, slip_c=1),
        Variant("mom2_bn", "momentum", 0.0, mom_src="binance", mom_window_ms=300, mom_usd=2.0, slip_c=1),
        Variant("mom2_bnany", "momentum", 0.0, mom_src="binance_any", mom_window_ms=300, mom_usd=2.0, slip_c=1),
        # моментум с порогом от волатильности (2,5 и 3,5 сигмы за 300 мс), цены 0,30-0,95
        Variant("mom25s", "momentum", 0.0, mom_src="binance_fut", mom_window_ms=300, mom_k=2.5, slip_c=1,
                v_price_lo=0.30, v_price_hi=0.95),
        Variant("mom35s", "momentum", 0.0, mom_src="binance_fut", mom_window_ms=300, mom_k=3.5, slip_c=1,
                v_price_lo=0.30, v_price_hi=0.95),
        Variant("mom4_bnf30", "momentum", 0.0, mom_src="binance_fut", mom_window_ms=300, mom_usd=4.0, slip_c=1,
                v_price_lo=0.30, v_price_hi=0.95),
        # те же пороги от волатильности, но с большей переплатой (лимит = ask + 3 / 5 ц)
        # дисбаланс верха книги фьючерса Binance (нужен --binance-fut-book); _p1/_p2/_p3 - лимит ask + 1/2/3 ц; цены 0,10-0,90
        Variant("imb90_p1", "imbalance", 0.0, qi_min=0.9, qi_confirm_k=0.0, slip_c=1, v_price_lo=0.10, v_price_hi=0.90, cooldown=3.0),
        Variant("imb90_p2", "imbalance", 0.0, qi_min=0.9, qi_confirm_k=0.0, slip_c=2, v_price_lo=0.10, v_price_hi=0.90, cooldown=3.0),
        Variant("imb90_p3", "imbalance", 0.0, qi_min=0.9, qi_confirm_k=0.0, slip_c=3, v_price_lo=0.10, v_price_hi=0.90, cooldown=3.0),
        Variant("imb95_p1", "imbalance", 0.0, qi_min=0.95, qi_confirm_k=0.0, slip_c=1, v_price_lo=0.10, v_price_hi=0.90, cooldown=3.0),
        Variant("imb95_p2", "imbalance", 0.0, qi_min=0.95, qi_confirm_k=0.0, slip_c=2, v_price_lo=0.10, v_price_hi=0.90, cooldown=3.0),
        Variant("imb95_p3", "imbalance", 0.0, qi_min=0.95, qi_confirm_k=0.0, slip_c=3, v_price_lo=0.10, v_price_hi=0.90, cooldown=3.0),
        Variant("imb90_m1_p1", "imbalance", 0.0, qi_min=0.9, qi_confirm_k=1.0, slip_c=1, v_price_lo=0.10, v_price_hi=0.90, cooldown=3.0),
        Variant("imb90_m1_p2", "imbalance", 0.0, qi_min=0.9, qi_confirm_k=1.0, slip_c=2, v_price_lo=0.10, v_price_hi=0.90, cooldown=3.0),
        Variant("imb90_m1_p3", "imbalance", 0.0, qi_min=0.9, qi_confirm_k=1.0, slip_c=3, v_price_lo=0.10, v_price_hi=0.90, cooldown=3.0),
        Variant("mom25s_p3", "momentum", 0.0, mom_src="binance_fut", mom_window_ms=300, mom_k=2.5, slip_c=3,
                v_price_lo=0.30, v_price_hi=0.95),
        Variant("mom25s_p5", "momentum", 0.0, mom_src="binance_fut", mom_window_ms=300, mom_k=2.5, slip_c=5,
                v_price_lo=0.30, v_price_hi=0.95),
        Variant("mom35s_p3", "momentum", 0.0, mom_src="binance_fut", mom_window_ms=300, mom_k=3.5, slip_c=3,
                v_price_lo=0.30, v_price_hi=0.95),
        Variant("mom35s_p5", "momentum", 0.0, mom_src="binance_fut", mom_window_ms=300, mom_k=3.5, slip_c=5,
                v_price_lo=0.30, v_price_hi=0.95),
        Variant("anc_3c_by_s15", "anchor", 0.03, source="bybit", sigma_mult=1.5),
        # первый пришедший тик с любой биржи (Bybit, Coinbase, Binance при --binance-source)
        Variant("anc_3c_any_s15", "anchor", 0.03, source="any", sigma_mult=1.5),
        Variant("anc_2c_cb", "anchor", 0.02, source="coinbase"),
        Variant("anc_2c_both", "anchor", 0.02, source="both"),
    ])

    status_every_sec: float = 10.0


def _all_feeds():
    from feeds_extra import FEEDS
    return list(FEEDS)


def parse_args(argv=None) -> Config:
    p = argparse.ArgumentParser(description="BTC 5m lab: сбор данных + проверка гипотез + бумажная торговля")
    p.add_argument("--data-dir", default="data")
    p.add_argument("--wallet", default=DEFAULT_WALLET)
    p.add_argument("--no-wallet", action="store_true")
    p.add_argument("--no-coinbase", action="store_true")
    p.add_argument("--extra-feeds", default="binance_futures,bybit",
                   help="Доп. биржи для записи через запятую (binance_futures, bybit, okx) или none")
    p.add_argument("--no-paper", action="store_true")
    p.add_argument("--binance-ws", default="wss://data-stream.binance.vision",
                   help="Адрес Binance: wss://data-stream.binance.vision | wss://stream.binance.com:443 | :9443")
    p.add_argument("--binance-streams", default="aggTrade,depth5",
                   help="Какие потоки Binance брать: aggTrade, bookTicker, depth5 (через запятую)")
    p.add_argument("--paper-btc-source", default="bybit", choices=["bybit", "coinbase", "binance", "rtds"])
    p.add_argument("--latencies", default="50,150,300,600", help="Задержки ордера для бумажной торговли, мс")
    p.add_argument("--fee-rate", type=float, default=0.07)
    p.add_argument("--no-quickedit", action="store_true",
                   help="Отключить выделение мышью в консоли Windows на время работы (по умолчанию не трогаем)")
    p.add_argument("--top-sizes", default="up", choices=["none", "up", "both"],
                   help="Изменения объёма на лучших ценах в pm_top: none, up (по умолчанию), both")
    p.add_argument("--only", default="", help="Запустить только часть процессов: cex,pm,wallet (для отладки)")
    a = p.parse_args(argv)
    cfg = Config(
        data_dir=a.data_dir,
        wallet=a.wallet.lower(),
        wallet_enabled=not a.no_wallet,
        coinbase=not a.no_coinbase,
        extra_feeds=([] if a.extra_feeds.strip().lower() == "none" else
                     _all_feeds() if a.extra_feeds.strip().lower() == "all" else
                     [x.strip() for x in a.extra_feeds.split(",") if x.strip()]),
        paper=not a.no_paper,
        binance_ws=a.binance_ws.rstrip("/"),
        binance_streams=a.binance_streams,
        paper_btc_source=a.paper_btc_source,
        latencies_ms=[int(x) for x in a.latencies.split(",") if x.strip()],
        fee_rate=a.fee_rate,
        top_sizes=a.top_sizes,
    )
    cfg.no_quickedit = a.no_quickedit  # type: ignore[attr-defined]
    cfg.only = [x.strip() for x in a.only.split(",") if x.strip()]  # type: ignore[attr-defined]
    return cfg
