from src.settings import API_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.redis import RedisStorage

from redis.asyncio.client import Redis


bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=RedisStorage(Redis()))
