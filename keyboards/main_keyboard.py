from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


'''Main menu keyboard'''
b1 = KeyboardButton('Добавить случай')
b2 = KeyboardButton('Помощь')
b3 = KeyboardButton('Я администратор')
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(b1).add(b2).add(b3)