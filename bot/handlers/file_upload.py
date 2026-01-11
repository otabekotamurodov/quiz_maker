import os
from aiogram import Router
from aiogram.types import Message, Document

from services.file_parser import parse_file
from services.text_cleaner import clean_text
from services.quiz_generator import generate_quiz

file_router = Router()

ALLOWED_EXTENSIONS = (".pdf", ".docx", ".txt")
UPLOAD_DIR = "uploads"


@file_router.message(lambda m: m.document is not None)
async def handle_file(message: Message):
    document: Document = message.document
    file_name = document.file_name.lower()

    # 1️⃣ Format tekshirish
    if not file_name.endswith(ALLOWED_EXTENSIONS):
        await message.answer(
            "❌ Noto‘g‘ri format.\n"
            "Faqat PDF, DOCX yoki TXT file yuboring."
        )
        return

    # 2️⃣ File saqlash
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, document.file_name)

    bot = message.bot
    tg_file = await bot.get_file(document.file_id)
    await bot.download_file(tg_file.file_path, file_path)

    await message.answer("📥 File qabul qilindi. O‘qilmoqda...")

    # 3️⃣ File → TEXT
    try:
        raw_text = parse_file(file_path)
        clean_text_data = clean_text(raw_text)
    except Exception as e:
        await message.answer("❌ File o‘qishda xatolik yuz berdi.")
        return

    if len(clean_text_data) < 300:
        await message.answer(
            "❌ File ichidagi matn juda kam.\n"
            "Iltimos, mazmunliroq file yuboring."
        )
        return

    await message.answer(
        "✅ File muvaffaqiyatli o‘qildi!\n"
        f"📄 Belgilar soni: {len(clean_text_data)}\n\n"
        "🧠 Quiz generatsiya qilinmoqda..."
    )

    # 4️⃣ TEXT → QUIZ (OpenAI)
    try:
        quiz_json = generate_quiz(clean_text_data)
    except Exception as e:
        await message.answer("❌ Quiz generatsiyada xatolik yuz berdi.")
        return

    # 5️⃣ Natijani yuborish (hozircha raw JSON)
    await message.answer(
        "🎉 Quiz tayyor!\n\n"
        "📌 Quyida 10 ta savol (JSON format):\n\n"
        f"{quiz_json[:3500]}"
    )
