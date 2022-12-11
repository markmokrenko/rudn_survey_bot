from aiogram.utils import executor
from create_bot import dp
from handlers import user_handlers, admin_handlers
from database import db


async def on_startup(_):
    print("Бот онлайн")
    # создание базы данных при запуске бота
    db.sql_start()


if __name__ == '__main__':
    # регистрация хендлеров из файлов
    user_handlers.register_handlers_user(dp)
    admin_handlers.register_handlers_admin(dp)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
