from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

start_router = Router()

@start_router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "👋 Salom!\n\n"
        "📄 Menga PDF / DOCX / TXT file yuboring.\n"
        "🧠 Men shu fayl asosida 10 ta quiz yarataman."
    )
