#!/usr/bin/env bash
# Проверка после установки: версии, модульные тесты кода. Выполняется один раз (и снова при изменении файла).
set -u
echo "python: $($PYTHON --version)"; echo "git: $(git rev-parse --short HEAD)"; echo
"$PYTHON" -m pytest -q btc5m_lab/tests 2>&1 | tail -15
echo; echo "--- свободное место и память ---"; df -h / | tail -1; free -m | head -2
