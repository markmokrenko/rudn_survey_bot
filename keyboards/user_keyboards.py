from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

'''Клавиатура выбора исследования'''

choose_research_keyboard_buttons = [InlineKeyboardButton(text='Тестовое исследование 1', callback_data='TestResearch1')]
choose_research_keyboard = InlineKeyboardMarkup(row_width=1)
choose_research_keyboard.add(*choose_research_keyboard_buttons)
