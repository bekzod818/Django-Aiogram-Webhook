import asyncio
from django.core.management.base import BaseCommand
from aiogram import Bot, Dispatcher
from aiogram.client.session.middlewares.request_logging import logger
from tgbot.bot.loader import dp, bot


class Command(BaseCommand):
    help = 'Run bot in polling'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Bot started!"))
        try:
            main()
        except KeyboardInterrupt:
            self.stdout.write(self.style.NOTICE("Bot stopped!"))


def setup_handlers(dispatcher: Dispatcher) -> None:
    """HANDLERS"""
    from tgbot.bot.handlers import setup_routers

    dispatcher.include_router(setup_routers())


def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    from tgbot.bot.middlewares.throttling import ThrottlingMiddleware

    # Spamdan himoya qilish uchun klassik ichki o'rta dastur. So'rovlar orasidagi asosiy vaqtlar 0,5 soniya
    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))


def setup_filters(dispatcher: Dispatcher) -> None:
    """FILTERS"""
    from tgbot.bot.filters import ChatPrivateFilter

    # Chat turini aniqlash uchun klassik umumiy filtr
    # Filtrni handlers/users/__init__ -dagi har bir routerga alohida o'rnatish mumkin
    dispatcher.message.filter(ChatPrivateFilter())


async def setup_aiogram(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info("Configuring aiogram")
    setup_handlers(dispatcher=dispatcher)
    setup_middlewares(dispatcher=dispatcher, bot=bot)
    setup_filters(dispatcher=dispatcher)
    logger.info("Configured aiogram")


async def aiogram_on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    from tgbot.bot.utils.set_bot_commands import set_default_commands
    from tgbot.bot.utils.notify_admins import on_startup_notify

    logger.info("Starting polling")
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_aiogram(bot=bot, dispatcher=dispatcher)
    await on_startup_notify(bot=bot)
    await set_default_commands(bot=bot)


async def aiogram_on_shutdown_polling(dispatcher: Dispatcher, bot: Bot):
    logger.info("Stopping polling")
    await bot.session.close()
    await dispatcher.storage.close()


def main():
    """CONFIG"""
    dp.startup.register(aiogram_on_startup_polling)
    dp.shutdown.register(aiogram_on_shutdown_polling)
    asyncio.run(dp.start_polling(bot, close_bot_session=True))
    # allowed_updates=['message', 'chat_member']
