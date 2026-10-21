import json
import sys

import bot


def parse_with(tmp_path, monkeypatch, live, extra):
    p = tmp_path / "lc.json"
    p.write_text(json.dumps(live), encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["bot.py", "--live", str(p), "--mode", "dry", "--no-chart"] + extra)
    return bot.parse()


LIVE = {"variant": "c2", "size": 5, "slippage_mode": "fixed", "slippage_cents": 20, "slippage_choices": [],
        "funder": "0x1", "private_key_env": "X", "stop_file": "STOP2"}


def test_paper_follows_live_params(tmp_path, monkeypatch):
    cfg, a = parse_with(tmp_path, monkeypatch, LIVE, ["--clip", "50", "--variants", "c2:0.035:bybit:1,other:0.03:bybit:1",
                                                       "--latencies", "200,300", "--show", "c1@200", "--slip-ticks", "3"])
    assert [v.name for v in cfg.variants] == ["c2"]
    assert cfg.variants[0].clip == 5.0
    assert cfg.slippage_ticks == 20
    assert a.show == "c2@200" and a.live_only_main


def test_keeps_valid_latency_choice(tmp_path, monkeypatch):
    cfg, a = parse_with(tmp_path, monkeypatch, LIVE, ["--variants", "c2:0.035:bybit:1", "--latencies", "200,300", "--show", "c2@300"])
    assert a.show == "c2@300"


def test_random_mode_leaves_paper_slip(tmp_path, monkeypatch):
    live = dict(LIVE, slippage_mode="random", slippage_choices=[3, 10])
    cfg, a = parse_with(tmp_path, monkeypatch, live, ["--variants", "c2:0.035:bybit:1", "--latencies", "200", "--slip-ticks", "4"])
    assert cfg.slippage_ticks == 4
