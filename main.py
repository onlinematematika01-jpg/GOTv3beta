import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database.db import connect_db
from scheduler.scheduler import start_scheduler

from handlers import start, profile

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # DB
    await connect_db()

    # Routers
    dp.include_router(start.router)
    dp.include_router(profile.router)

    # Scheduler
    start_scheduler()

    print("Bot ishga tushdi...")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
