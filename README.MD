# Quiz Maker Bot

Telegram bot foydalanuvchidan `PDF`, `DOCX` yoki `TXT` fayl qabul qiladi, matnni ajratadi va OpenAI orqali 10 ta quiz savol generatsiya qiladi.

## Stack

- Python 3.12
- `aiogram` polling bot
- `pdfplumber` va `python-docx`
- OpenAI Responses API

## Local ishga tushirish

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py
```

`.env` ichida quyidagilar bo'lishi kerak:

```env
BOT_TOKEN=...
OPENAI_API_KEY=...
```

## Ubuntu 24.04 deploy

Serverda quyidagilarni bajaring:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
sudo useradd -r -s /usr/sbin/nologin -m -d /opt/quiz_maker quizbot
sudo mkdir -p /opt/quiz_maker
sudo chown quizbot:quizbot /opt/quiz_maker
```

Kodini `/opt/quiz_maker` ichiga joylang, keyin:

```bash
cd /opt/quiz_maker
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
mkdir -p uploads
```

`.env` faylga haqiqiy `BOT_TOKEN` va `OPENAI_API_KEY` yozing.

Systemd service o'rnatish:

```bash
sudo cp deploy/quiz-bot.service /etc/systemd/system/quiz-bot.service
sudo systemctl daemon-reload
sudo systemctl enable --now quiz-bot.service
sudo systemctl status quiz-bot.service
```

Loglarni ko'rish:

```bash
journalctl -u quiz-bot.service -f
```

## GitHub Actions CI/CD

Repo ichiga quyidagilar qo'shildi:

- `.github/workflows/ci.yml`: `main` ga push va `pull_request` da dependency install + syntax check
- `.github/workflows/deploy.yml`: `CI` muvaffaqiyatli tugasa `main` branch uchun serverga deploy
- `scripts/deploy.sh`: serverdagi yangilash skripti

GitHub repository secrets:

- `DEPLOY_HOST`: server IP yoki domen
- `DEPLOY_USER`: SSH user
- `DEPLOY_SSH_KEY`: private key
- `DEPLOY_PATH`: serverdagi loyiha yo'li, masalan `/opt/quiz_maker`
- `DEPLOY_PORT`: ixtiyoriy, default `22`

Server tayyorlash bo'yicha minimal talablar:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
sudo usermod -aG sudo quizbot
```

`quizbot` user uchun quyidagi `sudoers` ruxsatini berish tavsiya qilinadi:

```bash
sudo visudo -f /etc/sudoers.d/quizbot-deploy
```

Ichiga yozing:

```sudoers
quizbot ALL=(ALL) NOPASSWD: /bin/systemctl daemon-reload, /bin/systemctl restart quiz-bot.service, /bin/systemctl status quiz-bot.service
```

CD ishlashi uchun serverda kamida bir marta `.env` yaratib qo'yish kerak.

## Eslatma

- Bot webhook emas, `polling` rejimida ishlaydi.
- `uploads/` katalogi yozish huquqiga ega bo'lishi kerak.
- `requirements.txt` avval bo'sh edi, deploy uchun dependency ro'yxati to'ldirildi.
- `services/quiz_generator.py` promptga fayl matnini qo'shmayotgan edi, bu deploydan oldin tuzatildi.
