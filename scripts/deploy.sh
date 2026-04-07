#!/usr/bin/env bash
set -euo pipefail

APP_DIR="${APP_DIR:-/opt/quiz_maker}"
SERVICE_NAME="${SERVICE_NAME:-quiz-bot.service}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

cd "$APP_DIR"

if [ ! -f .env ]; then
  echo ".env file not found in $APP_DIR"
  exit 1
fi

mkdir -p uploads

if [ ! -d .venv ]; then
  "$PYTHON_BIN" -m venv .venv
fi

.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m py_compile \
  main.py \
  config.py \
  bot/handlers/start.py \
  bot/handlers/file_upload.py \
  services/file_parser.py \
  services/text_cleaner.py \
  services/quiz_generator.py \
  services/quiz_formatter.py

sudo systemctl daemon-reload
sudo systemctl restart "$SERVICE_NAME"
sudo systemctl status "$SERVICE_NAME" --no-pager
