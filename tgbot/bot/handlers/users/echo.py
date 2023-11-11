from aiogram import Router, types
from tgbot.bot.loader import dp

router = Router()


@router.message()
async def start_user(message: types.Message):
    await message.answer(message.text)
