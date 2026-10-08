#!/usr/bin/env bash
# Берёт из git задания (jobs/once, jobs/recurring), выполняет их и отправляет маленькие отчёты в ветку результатов.
# Запускается из systemd-таймера раз в 5 минут от имени пользователя lab. Секретов не читает и не пишет.
set -uo pipefail
ENV_FILE="${LAB_ENV:-$HOME/lab.env}"
# shellcheck disable=SC1090
source "$ENV_FILE" || { echo "нет файла настроек $ENV_FILE" >&2; exit 2; }
: "${JOB_TIMEOUT:=1800}" "${KEEP_DAYS:=14}" "${RESULTS_KEEP_DAYS:=30}"
mkdir -p "$STATE_DIR/done" "$STATE_DIR/last" "$DATA_DIR"

exec 9>"$STATE_DIR/runner.lock"
flock -n 9 || { echo "предыдущий запуск ещё идёт"; exit 0; }

log() { echo "[$(date -u +%FT%TZ)] $*"; }

# ---------- 1. обновить код (на сервере код никогда не правится руками)
if [ ! -d "$REPO_DIR/.git" ]; then
  git clone -q --branch "$BRANCH" "$REPO_URL" "$REPO_DIR" || { log "не удалось клонировать $REPO_URL"; exit 1; }
fi
old_rev=$(git -C "$REPO_DIR" rev-parse HEAD)
git -C "$REPO_DIR" fetch -q origin "$BRANCH" || { log "git fetch не удался (сеть? ключ?)"; exit 1; }
git -C "$REPO_DIR" reset -q --hard "origin/$BRANCH"
new_rev=$(git -C "$REPO_DIR" rev-parse HEAD)
if [ "$old_rev" != "$new_rev" ] && [ "${SKIP_RESTART:-0}" != "1" ]; then
  if git -C "$REPO_DIR" diff --name-only "$old_rev" "$new_rev" -- \
      btc5m_lab/run.py btc5m_lab/config.py btc5m_lab/common.py btc5m_lab/cex.py btc5m_lab/pm.py \
      btc5m_lab/feeds_extra.py | grep -q .; then
    log "код записи изменился — перезапускаю lab-collector"
    sudo -n /bin/systemctl restart lab-collector || log "перезапуск не разрешён (sudoers?)"
  fi
fi

# ---------- 2. репозиторий результатов
if [ ! -d "$RESULTS_DIR/.git" ]; then
  git init -q -b "$RESULTS_BRANCH" "$RESULTS_DIR"
  git -C "$RESULTS_DIR" remote add origin "$REPO_URL"
fi
git -C "$RESULTS_DIR" config user.name "lab-server"
git -C "$RESULTS_DIR" config user.email "lab-server@localhost"
if git -C "$RESULTS_DIR" fetch -q origin "$RESULTS_BRANCH" 2>/dev/null; then
  git -C "$RESULTS_DIR" reset -q --hard FETCH_HEAD
fi

# ---------- 3. выполнение заданий
run_job() {  # run_job <имя> <путь к скрипту>
  local name="$1" path="$2" ts out rc
  ts=$(date -u +%Y%m%dT%H%M%SZ)
  out="$RESULTS_DIR/results/$(date -u +%F)/${ts}_${name}"
  mkdir -p "$out"
  log "запуск задания $name"
  local tmo
  tmo=$(sed -n 's/^# timeout_min:[[:space:]]*\([0-9]\+\).*/\1/p' "$path" | head -1)
  tmo=$(( ${tmo:-0} > 0 ? tmo * 60 : JOB_TIMEOUT ))
  ( cd "$REPO_DIR" && OUT_DIR="$out" DATA_DIR="$DATA_DIR" REPO_DIR="$REPO_DIR" PYTHON="$PYTHON" \
      timeout "$tmo" bash "$path" ) >"$out/job.log" 2>&1
  rc=$?
  echo "$rc" >"$out/exit_code"
  log "задание $name завершено, код $rc"
  # защита репозитория от раздувания: хвост лога и никаких файлов больше 2 МБ
  tail -c 200000 "$out/job.log" >"$out/job.log.tmp" && mv "$out/job.log.tmp" "$out/job.log"
  find "$out" -type f -size +2M -delete
}

shopt -s nullglob
for f in "$REPO_DIR"/jobs/once/*.sh; do
  name=$(basename "$f" .sh)
  id="$name-$(sha256sum "$f" | cut -c1-12)"
  [ -e "$STATE_DIR/done/$id" ] && continue
  touch "$STATE_DIR/done/$id"          # отмечаем до запуска: упавшее задание не зациклится
  run_job "$name" "$f"
done
now=$(date +%s)
for f in "$REPO_DIR"/jobs/recurring/*.sh; do
  name=$(basename "$f" .sh)
  interval=$(sed -n 's/^# interval_min:[[:space:]]*\([0-9]\+\).*/\1/p' "$f" | head -1)
  interval=${interval:-60}
  last=$(cat "$STATE_DIR/last/$name" 2>/dev/null || echo 0)
  [ $((now - last)) -lt $((interval * 60)) ] && continue
  echo "$now" >"$STATE_DIR/last/$name"
  run_job "$name" "$f"
done

# ---------- 4. уборка: старые сырые данные и старые отчёты
find "$DATA_DIR" -type f -mtime +"$KEEP_DAYS" -delete 2>/dev/null
find "$DATA_DIR" -mindepth 1 -type d -empty -delete 2>/dev/null
find "$RESULTS_DIR/results" -mindepth 2 -maxdepth 2 -type d -mtime +"$RESULTS_KEEP_DAYS" -exec rm -rf {} + 2>/dev/null

# ---------- 5. отправка отчётов
cd "$RESULTS_DIR" || exit 1
git add -A
if git diff --cached --quiet; then
  log "новых отчётов нет"
  exit 0
fi
git commit -q -m "results $(date -u +%FT%TZ)"
for i in 1 2 3 4; do
  if git push -q origin "HEAD:$RESULTS_BRANCH"; then log "отчёты отправлены"; exit 0; fi
  log "push не удался, попытка $i"
  sleep $((2 ** i))
  git fetch -q origin "$RESULTS_BRANCH" 2>/dev/null && git rebase -q FETCH_HEAD 2>/dev/null
done
log "не удалось отправить отчёты (ключ без права записи?)"
exit 1
