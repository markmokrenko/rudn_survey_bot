from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN

'''Файл создан, чтобы быть посредником между main и остальными модулями
здесь создается экземпляр бота и диспетчера, импорировать их отсюда'''

# данные будут храниться в оперативной памяти, при выходе бота в оффлайн, данные теряются
storage = MemoryStorage()

# инициализация бота
bot = Bot(TOKEN)
# инициализация диспетчера
dp = Dispatcher(bot, storage=storage)