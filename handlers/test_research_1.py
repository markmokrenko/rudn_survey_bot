from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.test_research_1_keyboard import choose_patient_sex_keyboard, choose_patient_accessibility_keyboard, \
    choose_patient_occupation_keyboard, choose_ischemic_heart_disease_keyboard, \
    choose_arterial_hypertension_stage_keyboard, cancelling_keyboard
from database import db
import datetime

'''Запуск машины состояний для тестового исследования 1'''


class FSMTestResearch1(StatesGroup):
    patient_number = State()
    sex = State()
    date_of_birth = State()
    ages = State()
    accessibility = State()
    occupation = State()
    ischemic_heart_disease = State()
    arterial_hypertension_stage = State()


async def test_research_1_start(callback: types.CallbackQuery):
    if callback.from_user.username in db.show_users_usernames():
        await FSMTestResearch1.patient_number.set()
        await callback.message.answer('Данное исследование создано с целью тестирования работы бота')
        await callback.message.answer('Введите код клинического случая.\nКод клинического случая, в формате ККНННН,\n'
                                      'где КК- 2 первых символа организации,\nНННН-порядковый номер пациента, например'
                                      ' для Клиники Долгалева -KD0001, KD0002 и т.д.\nтакже вносится в кодификатор',
                                      reply_markup=cancelling_keyboard)
        await callback.answer()
    else:
        await callback.message.answer('У вас нет прав доступа, обратитесь к администратору')


async def cancelling(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await callback.message.answer('Анкетирование остановлено. Данные не сохранены.')
    await callback.answer()


async def add_patient_number(message: types.Message,
                             state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.from_user.username
        data['patient_number'] = message.text
    await FSMTestResearch1.next()
    await message.answer('Введите пол пациента:', reply_markup=choose_patient_sex_keyboard)


async def add_sex(callback: types.CallbackQuery,
                  state: FSMContext):
    async with state.proxy() as data:
        data['sex'] = callback.data
    await FSMTestResearch1.next()
    await callback.message.answer('Введите дату рождения пациента в формате ДД.ММ.ГГГГ:',
                                  reply_markup=cancelling_keyboard)
    await callback.answer()


async def add_date_of_birth(message: types.Message,
                            state: FSMContext):
    async with state.proxy() as data:
        try:
            data['date_of_birth'] = datetime.datetime.strptime(message.text, "%d.%m.%Y")
        except:
            # выполняется проверка на соответствие шаблону даты, дата конвертируется
            await message.reply('Дата введена неверно.\nВведите дату рождения пациента в формате ДД.ММ.ГГГГ:')
            data['date_of_birth'] = datetime.datetime.strptime(message.text, "%d.%m.%Y")
    await FSMTestResearch1.next()
    await message.answer('Введите возраст пациента на момент операции:', reply_markup=cancelling_keyboard)


async def add_ages(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        try:
            # проверка на число
            data['ages'] = int(message.text)
        except Exception:
            await message.reply('Введите число')
            data['ages'] = int(message.text)
    await FSMTestResearch1.next()
    await message.answer('Доступен ли пациент для постоянного контроля?',
                         reply_markup=choose_patient_accessibility_keyboard)


async def add_accessibility(callback: types.CallbackQuery,
                            state: FSMContext):
    async with state.proxy() as data:
        data['accessibility'] = callback.data
    await FSMTestResearch1.next()
    await callback.message.answer('Укажите особенности профессиональной деятельности:',
                                  reply_markup=choose_patient_occupation_keyboard)
    await callback.answer()


async def add_occupation(callback: types.CallbackQuery,
                         state: FSMContext):
    async with state.proxy() as data:
        data['occupation'] = callback.data
    await FSMTestResearch1.next()
    await callback.message.answer('Укажите тип ИБС, если она присутствует',
                                  reply_markup=choose_ischemic_heart_disease_keyboard)
    await callback.answer()


async def add_ischemic_heart_disease(callback: types.CallbackQuery,
                                     state: FSMContext):
    async with state.proxy() as data:
        data['ischemic_heart_disease'] = callback.data
    await FSMTestResearch1.next()
    await callback.message.answer('Укажите степень артериальной гипертонии',
                                  reply_markup=choose_arterial_hypertension_stage_keyboard)
    await callback.answer()


async def add_arterial_hypertension_stage(callback: types.CallbackQuery,
                                          state: FSMContext):
    async with state.proxy() as data:
        data['arterial_hypertension_stage'] = callback.data
    await callback.answer()
    try:
        await db.add_research_for_test1(state)
        await callback.message.answer('Выбор сохранен')
    except Exception:
        await callback.message.answer('Произошла ошибка, данные не сохранены')
    await state.finish()


def register_handlers_test_research_1(dp: Dispatcher):
    dp.register_callback_query_handler(test_research_1_start, text='TestResearch1', state=None)
    dp.register_message_handler(add_patient_number, state=FSMTestResearch1.patient_number)
    dp.register_callback_query_handler(cancelling, text='cancel', state='*')
    dp.register_callback_query_handler(add_sex, state=FSMTestResearch1.sex)
    dp.register_message_handler(add_date_of_birth, state=FSMTestResearch1.date_of_birth)
    dp.register_message_handler(add_ages, state=FSMTestResearch1.ages)
    dp.register_callback_query_handler(add_accessibility, state=FSMTestResearch1.accessibility)
    dp.register_callback_query_handler(add_occupation, state=FSMTestResearch1.occupation)
    dp.register_callback_query_handler(add_ischemic_heart_disease, state=FSMTestResearch1.ischemic_heart_disease)
    dp.register_callback_query_handler(add_arterial_hypertension_stage,
                                       state=FSMTestResearch1.arterial_hypertension_stage)
