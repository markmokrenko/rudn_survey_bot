from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.main_keyboard import main_menu
from keyboards.user_keyboards import choose_research_keyboard
from database import db


async def command_start_reply(message: types.Message):
    if message.from_user.username in db.show_users_usernames():
        await message.answer(
            f'Здравствуйте, {message.from_user.first_name}.\nЭтот бот создан для записи клинических случаев',
            reply_markup=main_menu)
        await message.delete()
    else:
        await message.answer('У вас нет прав доступа, обратитесь к администратору')
        await message.delete()


async def help(message: types.Message):
    if message.from_user.username in db.show_users_usernames():
        await message.answer('Пункт меню находится в разработке, за помощью обратитесь к администратору')
    else:
        await message.answer('У вас нет прав доступа, обратитесь к администратору')
        await message.delete()


async def choose_research(message: types.Message):
    if message.from_user.username in db.show_users_usernames():
        await message.answer('Выберите исследование для записи случая:', reply_markup=choose_research_keyboard)
    else:
        await message.answer('У вас нет прав доступа, обратитесь к администратору')
        await message.delete()


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(command_start_reply, commands=['start'])
    dp.register_message_handler(help, text='Помощь')
    dp.register_message_handler(choose_research, text='Добавить случай')
