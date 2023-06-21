import sqlite3 as sq


def create_table():
    with sq.connect('users_data.db') as con:
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS reg_data(
                user_id INTEGER PRIMARY KEY NOT NULL,
                username TEXT NOT NULL,
                name TEXT NOT NULL,
                email TEXT NULL,
                age INTEGER NOT NULL
            )
        ''')


def delete_table():
    with sq.connect('users_data.db') as con:
        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS reg_data')


create_table()
