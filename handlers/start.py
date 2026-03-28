from aiogram import Router
from aiogram.types import Message
from services.user_service import get_or_create_user
from keyboards.main_menu import main_menu

router = Router()

@router.message(lambda msg: msg.text == "/start")
async def start_handler(message: Message):
    user = await get_or_create_user(
        message.from_user.id,
        message.from_user.username
    )

    await message.answer(
        f"Xush kelibsiz, {user['username']}!\n"
        f"Siz tizimga qo‘shildingiz.",
        reply_markup=main_menu()
    )
