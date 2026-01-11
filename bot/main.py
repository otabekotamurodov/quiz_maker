import os
from dotenv import load_dotenv

load_dotenv()

import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from bot.handlers.start import start_router
from bot.handlers.file_upload import file_router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(file_router)  # 👈 NEW

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
BOT_TOKEN = os.getenv("BOT_TOKEN")
