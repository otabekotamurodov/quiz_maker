#!/bin/bash
set -e

APP_DIR="/home/quizbot/projects/quiz_maker"
cd "$APP_DIR"

echo "📥 Pulling latest code..."
git pull origin main

echo "🐍 Activating venv..."
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate

echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📁 Ensuring uploads dir..."
mkdir -p uploads

echo "🔄 Restarting service..."
sudo systemctl restart quiz_maker

echo "✅ Deploy finished"