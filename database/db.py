import sqlite3
from create_bot import bot
import pandas as pd


def sql_start():
    ''' Функция создает базу данных и 3 (пока) таблицы: результаты test_research_1, админы, пользователи.'''
    global base, cur
    base = sqlite3.connect(r'database/database.db')
    cur = base.cursor()
    # создается таблица для записей результатов test_research_1
    cur.execute('CREATE TABLE IF NOT EXISTS '
                'test_research_1(username TEXT, patient_number TEXT, sex TEXT, date_of_birth TEXT, ages INT,'
                'accessibility TEXT, occupation TEXT, ischemic_heart_disease TEXT,'
                ' arterial_hypertension_stage TEXT)')
    # создаются таблицы для записи админов и пользователей
    cur.execute('CREATE TABLE IF NOT EXISTS '
                'users(username TEXT, department TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS '
                'admins(username TEXT)')
    base.commit()


def show_users_usernames():
    '''Функция выводит отформатированный список юзернеймов пользователей'''
    names = []
    for i in cur.execute('SELECT username FROM users').fetchall():
        names.append(i[0])
    return names


def show_admins_usernames():
    '''Функция выводит отформатированный список юзернеймов админов'''
    names = []
    for i in cur.execute('SELECT username FROM admins').fetchall():
        names.append(i[0])
    return names


async def add_user(state):
    '''Функция добавляет пользователя в users по запросу админа'''
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES(?, ?)', tuple(data.values()))
        base.commit()


async def add_admin(state):
    '''Функция добавляет админа в admins по запросу админа'''
    async with state.proxy() as data:
        cur.execute('INSERT INTO admins VALUES(?)', tuple(data.values()))
        base.commit()


async def add_research(state):
    '''Функция добавляет результаты опроса test_research_1 по запросу пользователя'''
    async with state.proxy() as data:
        cur.execute('INSERT INTO test_research_1 VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


def download_database():
    '''Функция выгружает БД в виде файла .xlsx'''
    df = pd.read_sql('SELECT * FROM test_research_1', base)
    df.to_excel(r'temp/result.xlsx', index=False)
