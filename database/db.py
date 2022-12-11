import sqlite3
from create_bot import bot
import pandas as pd

def sql_start():
    global base, cur
    base = sqlite3.connect(r'database/database.db')
    cur = base.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS '
                 'cases(username TEXT, patient_number TEXT, sex TEXT, date_of_birth TEXT, ages INT,'
                 'accessibility TEXT, occupation TEXT, ischemic_heart_disease TEXT,'
                 ' arterial_hypertension_stage TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS '
                 'users(username TEXT, department TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS '
                 'admins(username TEXT)')
    base.commit()
    print(show_users_usernames())

def show_users_usernames():
    names = []
    for i in cur.execute('SELECT username FROM users').fetchall():
        names.append(i[0])
    return names

def show_admins_usernames():
    names = []
    for i in cur.execute('SELECT username FROM admins').fetchall():
        names.append(i[0])
    return names

async def add_user(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES(?, ?)', tuple(data.values()))
        base.commit()

async def add_admin(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO admins VALUES(?)', tuple(data.values()))
        base.commit()

async def add_research(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO cases VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

def download_database():
    df = pd.read_sql('SELECT * FROM cases', base)
    df.to_excel(r'temp/result.xlsx', index=False)

#
#
# async def sql_add_users_flat(state):
#     async with state.proxy() as data:
#         cur.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
#         base.commit()