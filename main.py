import os
from dotenv import load_dotenv

load_dotenv()

import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN, validate_config

from bot.handlers.start import start_router
from bot.handlers.file_upload import file_router
import logging

# ✅ LOGGING CONFIG (shuni qo‘shish shart)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)


async def main():
    validate_config()
    logger.info("Bot started")
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(file_router)  # 👈 NEW

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
