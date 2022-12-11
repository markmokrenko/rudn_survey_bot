from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.main_keyboard import main_menu
from database import db


async def command_start_reply(message: types.Message):
    if message.from_user.username in db.show_users_usernames():
        await message.answer('Этот бот создан для записи клинических случаев', reply_markup=main_menu)
        await message.delete()
    else:
        await message.answer('У вас нет доступа, обратитесь к администратору.')
        await message.delete()

async def help(message: types.Message):
    if message.from_user.username in db.show_users_usernames():
        await message.answer('Пункт меню находится в разработке, за помощью обратитесь к администратору')




def register_handlers_user(dp : Dispatcher):
    dp.register_message_handler(command_start_reply, commands=['start'])
    dp.register_message_handler(help, text='Помощь')
    # dp.register_message_handler(show_me_requests, text='Мои квартиры')
    # dp.register_callback_query_handler(delete_my_request, text='Удалить', )
