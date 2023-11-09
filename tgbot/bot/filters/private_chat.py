from aiogram.enums import ChatType
from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatPrivateFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == ChatType.PRIVATE
