from aiogram import Router

from tgbot.bot.filters import ChatPrivateFilter


def setup_routers() -> Router:
    from .users import start, help, echo
    from .errors import error_handler

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    start.router.message.filter(ChatPrivateFilter())

    router.include_routers(start.router, help.router, echo.router, error_handler.router)

    return router
