#!/usr/bin/env bash
# Локальная проверка runner.sh без сервера: «удалённый» репозиторий создаётся во временной папке.
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
git init -q --bare -b main "$T/remote.git"
git init -q -b main "$T/work"
cp -r "$SRC/ops" "$SRC/jobs" "$SRC/btc5m_lab" "$T/work/"
find "$T/work" -name __pycache__ -prune -exec rm -rf {} +
git -C "$T/work" -c user.name=t -c user.email=t@t add -A
git -C "$T/work" -c user.name=t -c user.email=t@t commit -q -m init
git -C "$T/work" remote add origin "$T/remote.git"; git -C "$T/work" push -q origin main
cat >"$T/lab.env" <<ENV
REPO_URL=$T/remote.git
BRANCH=main
RESULTS_BRANCH=server-results
REPO_DIR=$T/poly
RESULTS_DIR=$T/poly-results
DATA_DIR=$T/data
STATE_DIR=$T/state
PYTHON=${PYTHON:-python3}
JOB_TIMEOUT=120
KEEP_DAYS=14
ENV
export LAB_ENV="$T/lab.env" SKIP_RESTART=1 HOME="$T"
mkdir -p "$T/data/2026-01-01"; echo "recv_ms,x" >"$T/data/2026-01-01/pm_top_10.csv"
count() { git --git-dir="$T/remote.git" ls-tree -r --name-only server-results | grep -c "$1" || true; }
check() { [ "$1" = "$2" ] || { echo "FAIL: $3 (ожидалось $2, получено $1)"; exit 1; }; echo "ok: $3"; }

bash "$T/work/ops/runner.sh" >"$T/run1.log" 2>&1 || { cat "$T/run1.log"; exit 1; }
check "$(count 00_smoke_test/job.log)" 1 "разовое задание выполнено и отправлено"
check "$(count 00_status/status.md)" 1 "периодическое задание выполнено и отправлено"

bash "$T/work/ops/runner.sh" >"$T/run2.log" 2>&1
check "$(count 00_smoke_test/job.log)" 1 "разовое задание не повторяется"
check "$(count 00_status/status.md)" 1 "периодическое не запускается раньше интервала"

echo 0 >"$T/state/last/00_status"
bash "$T/work/ops/runner.sh" >"$T/run3.log" 2>&1
check "$(count 00_status/status.md)" 2 "периодическое запускается по истечении интервала"

printf '#!/usr/bin/env bash\necho hello > "$OUT_DIR/hi.txt"\n' >"$T/work/jobs/once/50_new.sh"
git -C "$T/work" -c user.name=t -c user.email=t@t add -A
git -C "$T/work" -c user.name=t -c user.email=t@t commit -q -m newjob; git -C "$T/work" push -q origin main
bash "$T/work/ops/runner.sh" >"$T/run4.log" 2>&1
check "$(count 50_new/hi.txt)" 1 "новое задание подхвачено из git"

printf '#!/usr/bin/env bash\nhead -c 3000000 /dev/zero > "$OUT_DIR/big.bin"\nsleep 300\n' >"$T/work/jobs/once/60_big.sh"
git -C "$T/work" -c user.name=t -c user.email=t@t add -A
git -C "$T/work" -c user.name=t -c user.email=t@t commit -q -m big; git -C "$T/work" push -q origin main
sed -i 's/JOB_TIMEOUT=120/JOB_TIMEOUT=3/' "$T/lab.env"
bash "$T/work/ops/runner.sh" >"$T/run5.log" 2>&1
check "$(count 60_big/big.bin)" 0 "файлы больше 2 МБ не попадают в отчёты"
check "$(count 60_big/exit_code)" 1 "зависшее задание остановлено по таймауту"
check "$(cat "$T"/poly-results/results/*/*60_big/exit_code)" 124 "код таймаута 124"
echo "ВСЁ В ПОРЯДКЕ"
