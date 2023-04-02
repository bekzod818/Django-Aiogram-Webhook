from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from tgbot.models import User
from tgbot.bot.loader import dp, bot
from django.conf import settings


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user, created = User.objects.get_or_create(
        tg_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username
    )
    for admin in settings.ADMINS:
        if created:
            await bot.send_message(chat_id=admin, text=f"{user} bazaga qo'shildi")
        else:
            await bot.send_message(chat_id=admin, text=f"{user} bazaga oldin qo'shilgan")
    await message.answer(f"Salom, {message.from_user.full_name}!")
    