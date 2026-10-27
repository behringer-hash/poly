"""Общие утилиты: точные часы, запись данных, окна, математика, мониторинг event loop."""
from __future__ import annotations

import asyncio
import math
import os
import queue
import sys
import threading
import time
from collections import deque
from datetime import datetime, timezone
from statistics import NormalDist

try:
    import orjson

    def loads(s):
        return orjson.loads(s)
except ImportError:  # pragma: no cover
    import json

    def loads(s):
        return json.loads(s)

WINDOW_SEC = 300
_N = NormalDist()


# ----------------------------------------------------------------------------- часы
class Clock:
    """Время в секундах (float, микросекунды).

    На Windows до Python 3.13 time.time() имеет разрешение ~15.6 мс, поэтому
    берём высокоточный perf_counter и привязываем его к системным часам.
    Перепривязка раз в 30 с, чтобы следовать за синхронизацией Windows Time.
    """

    def __init__(self):
        self._precise = sys.platform != "win32" or sys.version_info >= (3, 13)
        self._anchor()

    def _anchor(self):
        self._wall0 = time.time_ns()
        self._perf0 = time.perf_counter_ns()
        self._next = self._perf0 + 30 * 10**9

    def now(self) -> float:
        if self._precise:
            return time.time_ns() / 1e9
        p = time.perf_counter_ns()
        if p > self._next:
            self._anchor()
            p = self._perf0
        return (self._wall0 + (p - self._perf0)) / 1e9


clock = Clock()


def utc_str(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


# ----------------------------------------------------------------------------- окна
def window_start(ts: float) -> int:
    return int(ts - ts % WINDOW_SEC)


def slug_for(start: int) -> str:
    return f"btc-updown-5m-{start}"


# ----------------------------------------------------------------------------- математика
def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_inv(p: float) -> float:
    p = min(max(p, 1e-4), 1 - 1e-4)
    return _N.inv_cdf(p)


def taker_fee(price: float, rate: float) -> float:
    """Комиссия тейкера на 1 шейр: rate * p * (1-p) (по данным кошелька rate=0.07)."""
    return rate * price * (1.0 - price)


class RollingSigma:
    """Волатильность $/sqrt(с) по ценам, сэмплированным раз в секунду, окно N секунд."""

    def __init__(self, window_sec: int = 900, fallback: float = 5.0):
        self.fallback = fallback
        self.cur_sec: int | None = None      # текущая (незакрытая) секунда
        self.cur_px: float | None = None     # последняя цена в ней
        self.done: tuple[int, float] | None = None  # последняя закрытая секунда и её цена закрытия
        self.diffs: deque[float] = deque(maxlen=window_sec)
        self.s = 0.0
        self.s2 = 0.0

    def update(self, ts: float, px: float):
        sec = int(ts)
        if self.cur_sec is None or sec == self.cur_sec:
            self.cur_sec, self.cur_px = sec, px
            return
        if sec < self.cur_sec:
            return
        # закрываем секунду cur_sec
        if self.done is not None:
            gap = self.cur_sec - self.done[0]
            if 0 < gap <= 5:
                x = (self.cur_px - self.done[1]) / math.sqrt(gap)
                if len(self.diffs) == self.diffs.maxlen:
                    old = self.diffs[0]
                    self.s -= old
                    self.s2 -= old * old
                self.diffs.append(x)
                self.s += x
                self.s2 += x * x
        self.done = (self.cur_sec, self.cur_px)
        self.cur_sec, self.cur_px = sec, px

    @property
    def warm(self) -> bool:
        return len(self.diffs) >= 60

    def sigma(self) -> float:
        n = len(self.diffs)
        if n < 60:
            return self.fallback
        m = self.s / n
        v = max(0.0, (self.s2 - n * m * m) / (n - 1))
        s = math.sqrt(v)
        return s if s > 0.3 else self.fallback


class Quantiles:
    """Небольшой буфер для p50/p90 в консольной статистике."""

    def __init__(self, n: int = 2000):
        self.buf: deque[float] = deque(maxlen=n)

    def add(self, x: float):
        self.buf.append(x)

    def q(self, p: float):
        if not self.buf:
            return None
        s = sorted(self.buf)
        return s[min(len(s) - 1, int(p * len(s)))]

    def clear(self):
        self.buf.clear()


# ----------------------------------------------------------------------------- запись данных
def _fmt(v) -> str:
    if v is None:
        return ""
    if isinstance(v, float):
        if v != v:  # NaN
            return ""
        s = repr(round(v, 6))
        return s[:-2] if s.endswith(".0") else s
    s = str(v)
    if "," in s or '"' in s or "\n" in s:
        s = '"' + s.replace('"', '""') + '"'
    return s


class DataWriter:
    """Пишет потоки в data/<YYYY-MM-DD>/<поток>_<HH>.csv (UTC) в отдельном потоке ОС.

    В течение часа файл - обычный CSV (сбрасывается на диск каждые 2 с, при сбое
    ничего не теряется). При смене часа и при остановке программы файл сжимается
    в <поток>_<HH>.csv.xz (xz в ~2 раза компактнее gzip) и удаляется. Если такой
    .xz уже есть (перезапуск в тот же час), сжатые данные дописываются в него
    отдельным xz-блоком - формат это допускает. Оставшиеся после сбоя .csv
    сжимаются при следующем запуске.
    Горячий путь (event loop) только кладёт кортеж в очередь.
    """

    def __init__(self, root: str, schemas: dict[str, list[str]], tag: str):
        self.root = root
        self.schemas = schemas
        self.tag = tag
        self.q: queue.SimpleQueue = queue.SimpleQueue()
        self.files: dict[str, tuple[str, object]] = {}
        self.counts: dict[str, int] = {k: 0 for k in schemas}
        self.packer_q: queue.SimpleQueue = queue.SimpleQueue()
        self.packer = threading.Thread(target=self._pack_loop, name=f"packer-{tag}", daemon=True)
        self.packer.start()
        self._pack_leftovers()
        self.t = threading.Thread(target=self._run, name=f"writer-{tag}", daemon=True)
        self.t.start()

    def write(self, stream: str, row: tuple):
        self.q.put((stream, row))

    # ---- сжатие
    @staticmethod
    def pack_file(path: str):
        import lzma
        if not os.path.exists(path):
            return
        with open(path, "rb") as f:
            data = f.read()
        if data:
            comp = lzma.compress(data, preset=6)
            with open(path + ".xz", "ab") as f:
                f.write(comp)
        os.remove(path)

    def _pack_loop(self):
        while True:
            p = self.packer_q.get()
            if p == "__STOP__":
                return
            try:
                self.pack_file(p)
            except Exception as e:
                log("writer", f"сжатие {p}: {e}")

    def _pack_leftovers(self):
        import glob
        for s in self.schemas:
            for p in glob.glob(os.path.join(self.root, "*", f"{s}_??.csv")):
                try:  # синхронно: писатель ещё не запущен, гонки за файл нет
                    self.pack_file(p)
                except Exception as e:
                    log("writer", f"сжатие {p}: {e}")

    # ---- запись
    def _path(self, stream: str, ts: float) -> str:
        d = datetime.fromtimestamp(ts, tz=timezone.utc)
        folder = os.path.join(self.root, d.strftime("%Y-%m-%d"))
        os.makedirs(folder, exist_ok=True)
        return os.path.join(folder, f"{stream}_{d.strftime('%H')}.csv")

    def _fh(self, stream: str, ts: float):
        path = self._path(stream, ts)
        cur = self.files.get(stream)
        if cur and cur[0] == path:
            return cur[1]
        if cur:
            cur[1].close()
            self.packer_q.put(cur[0])
        new = not os.path.exists(path)
        fh = open(path, "a", encoding="utf-8", newline="")
        if new:
            fh.write(",".join(self.schemas[stream]) + "\n")
        self.files[stream] = (path, fh)
        return fh

    def _run(self):
        last_flush = time.time()
        while True:
            try:
                item = self.q.get(timeout=0.5)
            except queue.Empty:
                item = None
            now = time.time()
            batch = [] if item is None else [item]
            while len(batch) < 20000:
                try:
                    batch.append(self.q.get_nowait())
                except queue.Empty:
                    break
            stop = False
            for it in batch:
                if it == "__STOP__":
                    stop = True
                    continue
                stream, row = it
                try:
                    self._fh(stream, now).write(",".join(_fmt(v) for v in row) + "\n")
                    self.counts[stream] = self.counts.get(stream, 0) + 1
                except Exception as e:  # не роняем процесс из-за одной строки
                    log("writer", f"{self.tag}/{stream}: {e}")
            if now - last_flush > 2.0 or stop:
                for _, fh in self.files.values():
                    try:
                        fh.flush()
                    except Exception:
                        pass
                last_flush = now
            if stop:
                for path, fh in self.files.values():
                    try:
                        fh.close()
                        self.pack_file(path)
                    except Exception:
                        pass
                self.files.clear()
                return

    def close(self):
        self.q.put("__STOP__")
        self.t.join(timeout=60)
        self.packer_q.put("__STOP__")
        self.packer.join(timeout=60)


# ----------------------------------------------------------------------------- мониторинг
class LoopLag:
    """Меряет, насколько event loop опаздывает будить корутины (признак перегрузки)."""

    def __init__(self):
        self.q = Quantiles(1000)
        self.max_ms = 0.0

    async def run(self, period: float = 0.05):
        while True:
            t0 = time.perf_counter()
            await asyncio.sleep(period)
            lag = (time.perf_counter() - t0 - period) * 1000
            self.q.add(lag)
            self.max_ms = max(self.max_ms, lag)

    def snapshot_reset(self):
        r = (self.q.q(0.5), self.q.q(0.99), self.max_ms)
        self.q.clear()
        self.max_ms = 0.0
        return r


def probe_clock(binance_rest: str):
    """Смещение локальных часов: (серверное время - локальное) в мс и RTT.
    Берём лучший из 5 замеров (минимальный RTT). Binance точнее всего; запасной - Coinbase."""
    import requests
    sources = [
        ("binance", f"{binance_rest}/api/v3/time", lambda j: float(j["serverTime"])),
        ("coinbase", "https://api.exchange.coinbase.com/time", lambda j: float(j["epoch"]) * 1000),
    ]
    last_err = None
    for name, url, parse in sources:
        best = None
        try:
            for _ in range(5):
                t0 = clock.now()
                r = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
                t1 = clock.now()
                srv = parse(r.json())
                rtt = (t1 - t0) * 1000
                off = srv - (t0 + t1) / 2 * 1000
                if best is None or rtt < best[1]:
                    best = (off, rtt)
                time.sleep(0.2)
            return name, best[0], best[1]
        except Exception as e:
            last_err = e
    raise RuntimeError(f"все источники времени недоступны: {last_err!r}")


def big_rcvbuf_socket(url: str, rcvbuf: int = 8 * 1024 * 1024):
    """TCP-сокет с увеличенным приёмным буфером (как в исходном логгере) - меньше риск
    обрыва "slow consumer" от Polymarket при всплесках трафика."""
    import socket
    import urllib.parse
    u = urllib.parse.urlparse(url)
    s = socket.create_connection((u.hostname, u.port or 443), timeout=10)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, rcvbuf)
    except OSError:
        pass
    return s, u.hostname


BN_STREAMS = {"aggTrade": "btcusdt@aggTrade", "bookTicker": "btcusdt@bookTicker", "depth5": "btcusdt@depth5@100ms"}


def binance_url(cfg) -> tuple[str, list[str]]:
    names = [s.strip() for s in cfg.binance_streams.split(",") if s.strip() in BN_STREAMS]
    if "aggTrade" not in names:
        names.insert(0, "aggTrade")  # нужен всегда: по нему меряем задержку
    return f"{cfg.binance_ws}/stream?streams=" + "/".join(BN_STREAMS[n] for n in names), names


def binance_bbo(x: dict):
    """Лучшие bid/ask из bookTicker или depth5; None для остальных сообщений."""
    if "b" in x and "a" in x and "u" in x:
        return x.get("u"), x["b"], x.get("B"), x["a"], x.get("A")
    if "bids" in x and "asks" in x and x["bids"] and x["asks"]:
        return x.get("lastUpdateId"), x["bids"][0][0], x["bids"][0][1], x["asks"][0][0], x["asks"][0][1]
    return None


async def iter_ws(ws, stall_sec: float):
    """Как `async for raw in ws`, но если за stall_sec не пришло ни одного сообщения,
    соединение считается зависшим и закрывается (исключение TimeoutError наружу).
    Для BTCUSDT и активной книги Polymarket тишина дольше нескольких секунд = обрыв."""
    while True:
        raw = await asyncio.wait_for(ws.recv(), timeout=stall_sec)
        yield raw


def fnum(x, fmt=".1f", na="n/a"):
    return na if x is None else format(x, fmt)


# ----------------------------------------------------------------------------- консоль
# Вывод в консоль идёт через отдельный поток. Причина: в консоли Windows, если
# выделить мышью текст (режим QuickEdit), print() блокируется до снятия выделения.
# Если печатать прямо из event loop, замирает весь процесс: пинги Binance/Coinbase
# остаются без ответа и соединения рвутся по "keepalive ping timeout".
_out_q: queue.SimpleQueue = queue.SimpleQueue()
_out_started = False
_out_lock = threading.Lock()


def _printer():
    while True:
        s = _out_q.get()
        try:
            print(s, flush=True)
        except Exception:
            pass


def emit(text: str):
    global _out_started
    if not _out_started:
        with _out_lock:
            if not _out_started:
                threading.Thread(target=_printer, name="console", daemon=True).start()
                _out_started = True
    if _out_q.qsize() < 5000:  # если консоль долго заблокирована - лишнее выбрасываем
        _out_q.put(text)


def log(tag: str, msg: str):
    emit(f"{datetime.now().strftime('%H:%M:%S')} [{tag}] {msg}")


def flush_console(timeout: float = 2.0):
    t_end = time.time() + timeout
    while not _out_q.empty() and time.time() < t_end:
        time.sleep(0.05)


def disable_quick_edit():
    """Отключает QuickEdit консоли Windows и возвращает функцию, которая вернёт прежний режим.
    Включается только ключом --no-quickedit: вывод и так идёт через отдельный поток,
    поэтому выделение текста мышью больше не останавливает сбор данных."""
    if sys.platform != "win32":
        return lambda: None
    try:
        import ctypes
        k32 = ctypes.windll.kernel32
        h = k32.GetStdHandle(-10)  # STD_INPUT_HANDLE
        mode = ctypes.c_uint32()
        if not k32.GetConsoleMode(h, ctypes.byref(mode)):
            return lambda: None
        old = mode.value
        k32.SetConsoleMode(h, (old & ~0x0040) | 0x0080)
        return lambda: k32.SetConsoleMode(h, old)
    except Exception:
        return lambda: None


def ms(ts: float) -> int:
    """Секунды (float) -> целые миллисекунды: компактнее в файлах."""
    return int(round(ts * 1000))
