import json
from aiogram.types import Update
from django.http import HttpRequest
from tgbot.bot.loader import bot, dp


async def proceed_update(req: HttpRequest):
    upd = Update.model_validate(json.loads(req.body), context={"bot": bot})
    await dp.feed_webhook_update(bot, upd)
