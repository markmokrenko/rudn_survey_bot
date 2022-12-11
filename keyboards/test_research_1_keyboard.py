from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

'''Клавиатура пол пациента'''
choose_patient_sex_buttons = [InlineKeyboardButton(text='Мужской', callback_data='мужской'),
                              InlineKeyboardButton(text='Женский', callback_data='женский')]
choose_patient_sex_keyboard = InlineKeyboardMarkup(row_width=1)
choose_patient_sex_keyboard.add(*choose_patient_sex_buttons)

'''Клавиатура доступность пациента для контроля'''
choose_patient_accessibility_buttons = [InlineKeyboardButton(text='Да', callback_data='да'),
                                        InlineKeyboardButton(text='Нет', callback_data='нет')]
choose_patient_accessibility_keyboard = InlineKeyboardMarkup(row_width=1)
choose_patient_accessibility_keyboard.add(*choose_patient_accessibility_buttons)

'''Клавиатура вредные условия труда'''
choose_patient_occupation_buttons = [InlineKeyboardButton(text='Без особенностей', callback_data='без особенностей'),
                                     InlineKeyboardButton(text='Химически вредные вещества',
                                                          callback_data='химически вредные вещества'),
                                     InlineKeyboardButton(text='Лучевая нагрузка',
                                                          callback_data='лучевая нагрузка'),
                                     InlineKeyboardButton(text='Физическая нагрузка',
                                                          callback_data='физическая нагрузка')]
choose_patient_occupation_keyboard = InlineKeyboardMarkup(row_width=1)
choose_patient_occupation_keyboard.add(*choose_patient_occupation_buttons)

'''Клавиатура тип ИБС'''
choose_ischemic_heart_disease_buttons = [InlineKeyboardButton(text='Не наблюдается', callback_data='не наблюдается'),
                                         InlineKeyboardButton(text='Нестаб. стенокард.',
                                                              callback_data='нестаб стенокард'),
                                         InlineKeyboardButton(text='Был инфаркт миокарда',
                                                              callback_data='инфаркт в прош'),
                                         InlineKeyboardButton(text='Сердечная недост.',
                                                              callback_data='сердечная недост'),
                                         InlineKeyboardButton(text='Стаб. стенокард.',
                                                              callback_data='стаб стенокард')
                                         ]
choose_ischemic_heart_disease_keyboard = InlineKeyboardMarkup(row_width=1)
choose_ischemic_heart_disease_keyboard.add(*choose_ischemic_heart_disease_buttons)

'''Клавиатура степень АГ'''
choose_arterial_hypertension_stage_buttons = [InlineKeyboardButton(text='Норма', callback_data='норма'),
                                              InlineKeyboardButton(text='Норм. повыш.',
                                                                   callback_data='норм повыш'),
                                              InlineKeyboardButton(text='1 ст.',
                                                                   callback_data='1 ст'),
                                              InlineKeyboardButton(text='2 ст.',
                                                                   callback_data='2 ст'),
                                              InlineKeyboardButton(text='Ниже нормы',
                                                                   callback_data='ниже нормы')
                                              ]
choose_arterial_hypertension_stage_keyboard = InlineKeyboardMarkup(row_width=1)
choose_arterial_hypertension_stage_keyboard.add(*choose_arterial_hypertension_stage_buttons)
