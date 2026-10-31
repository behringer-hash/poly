#!/usr/bin/env bash
# interval_min: 240
# timeout_min: 90
# Проверка вперёд стратегии 4 (claude/strategy_4_signal_maker.md, раздел 3): mm_map, варианты F*, на каждом новом
# полном дне начиная с 30.10 (один раз на день; отметки в ~/fwd_sig). Если нового дня нет — ничего не делает.
set -u
ulimit -v 3000000 2>/dev/null || true
cd btc5m_lab || exit 1
ST="$HOME/fwd_sig"; mkdir -p "$ST"
today=$(date -u +%F)
V=F0_v1,F1_v2,F2_v2_nofresh,F3_v1_nofresh,F4_v2_th3,R6_ie_v2   # R6 добавлен 31.10
n=0
for d in $(ls "$DATA_DIR" 2>/dev/null | grep -E '^20[0-9]{2}-[0-9]{2}-[0-9]{2}$' | sort); do
  [[ "$d" < "2026-10-30" ]] && continue
  [[ "$d" < "$today" ]] || continue            # только завершённые сутки (UTC)
  [ -e "$ST/$d.done" ] && continue
  echo "== $d"
  nice -n 19 "$PYTHON" -u -W ignore mm_map.py "$DATA_DIR/$d" --out "$OUT_DIR" --variants $V 2>&1 | tail -10
  touch "$ST/$d.done"; n=$((n+1))
  [ $n -ge 2 ] && break                        # не больше двух дней за запуск
done
[ $n -eq 0 ] && echo "новых полных дней нет"
exit 0
