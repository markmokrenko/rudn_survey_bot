from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

'''Клавиатура появляется по нажатию кнопки я администратор'''
im_admin_keyboard_buttons = [InlineKeyboardButton(text='Выгрузить БД', callback_data='DownloadDB'),
                             InlineKeyboardButton(text='Добавить пользователя', callback_data='Add_user'),
                             InlineKeyboardButton(text='Добавить администратора', callback_data='Add_admin')]
im_admin_keyboard = InlineKeyboardMarkup(row_width=1)
im_admin_keyboard.add(*im_admin_keyboard_buttons)

'''Клавиатура выбора базы данных для скачивания'''
choose_db_for_download_buttons = [InlineKeyboardButton(text='test_research_1', callback_data='1_download')]
choose_db_for_download_keyboard = InlineKeyboardMarkup(row_width=1)
choose_db_for_download_keyboard.add(*choose_db_for_download_buttons)
