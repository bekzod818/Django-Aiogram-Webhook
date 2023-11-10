import json
from aiogram.types import Update
from django.http import HttpRequest
from tgbot.bot.loader import dp, bot
from tgbot.bot.handlers import setup_routers


async def proceed_update(req: HttpRequest):
    update = Update(**json.loads(req.body))
    dp.include_router(setup_routers())
    await dp.feed_webhook_update(bot=bot, update=update)
