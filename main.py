import asyncio
import os

from aiogram import Bot, Dispatcher
from bot.handlers import router
from dotenv import load_dotenv

load_dotenv()


async def main() -> None:
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
