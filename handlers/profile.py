from aiogram import Router
from aiogram.types import Message
from database.db import get_pool

router = Router()

@router.message(lambda msg: msg.text == "📊 Profil")
async def profile_handler(message: Message):
    pool = await get_pool()

    async with pool.acquire() as conn:
        user = await conn.fetchrow(
            "SELECT * FROM users WHERE id=$1",
            message.from_user.id
        )

    if not user:
        return await message.answer("Avval /start bosing")

    text = f"""
👤 Profil

ID: {user['id']}
Gold: {user['gold']}
Army: {user['army']}
Dragons: {user['dragons']}
"""

    await message.answer(text)
