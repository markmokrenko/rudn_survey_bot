from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.main_keyboard import main_menu
from keyboards.admin_keyboards import im_admin_keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import db


async def im_admin(message: types.Message):
    if message.from_user.username in db.show_admins_usernames():
        await message.answer(f'Добро пожаловать, администратор {message.from_user.first_name}',
                             reply_markup=im_admin_keyboard)
    else:
        await message.answer('У вас нет прав доступа, обратитесь к администратору')
        await message.delete()


async def download_cases_table(callback: types.CallbackQuery):
    if callback.from_user.username in db.show_admins_usernames():
        db.download_database()
        with open(r'temp/result.xlsx', 'rb') as result:
            await callback.message.answer_document(result)
    else:
        await callback.message.answer('У вас нет прав доступа, обратитесь к администратору')


'''Запуск машины состояний для загрузки нового пользователя в БД'''


class FSMAddUser(StatesGroup):
    username = State()
    department = State()


async def add_new_user_start(callback: types.CallbackQuery):
    if callback.from_user.username in db.show_admins_usernames():
        await FSMAddUser.username.set()
        await callback.message.answer('Введите имя пользователя:')
        await callback.answer()


async def add_new_user_username(message: types.Message,
                                state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await FSMAddUser.next()
    await message.answer('Введите место работы пользователя:')


async def add_new_user_depatrment(message: types.Message,
                                  state: FSMContext):
    async with state.proxy() as data:
        data['department'] = message.text
    try:
        await db.add_user(state)
        await message.answer('Выбор сохранен')
    except Exception:
        await message.answer('Произошла ошибка, новый пользователь не сохранен')
    await state.finish()


'''Запуск машины состояний для загрузки нового администратора'''


class FSMAddAdmin(StatesGroup):
    username = State()


async def add_new_admin_start(callback: types.CallbackQuery):
    if callback.from_user.username in db.show_admins_usernames():
        await FSMAddAdmin.username.set()
        await callback.message.answer('Введите имя администратора:')
        await callback.answer()


async def add_new_admin_username(message: types.Message,
                                 state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    try:
        await db.add_admin(state)
        await message.answer('Выбор сохранен')
    except Exception:
        await message.answer('Произошла ошибка, новый администратор не сохранен')
    await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(im_admin, text='Я администратор')
    dp.register_callback_query_handler(download_cases_table, text='DownloadDB')
    dp.register_callback_query_handler(add_new_user_start, text='Add_user', state=None)
    dp.register_message_handler(add_new_user_username, state=FSMAddUser.username)
    dp.register_message_handler(add_new_user_depatrment, state=FSMAddUser.department)
    dp.register_callback_query_handler(add_new_admin_start, text='Add_admin', state=None)
    dp.register_message_handler(add_new_admin_username, state=FSMAddAdmin.username)
