import sqlite3 as sq


def create_table():
    with sq.connect('users_data.db') as con:
        cur = con.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS reg_data(
                user_id INTEGER PRIMARY KEY NOT NULL,
                username TEXT NOT NULL,
                name TEXT NOT NULL DEFAULT "A",
                email TEXT NOT NULL "A",
                age INTEGER NOT NULL 0
            )
        ''')


def delete_table():
    with sq.connect('users_data.db') as con:
        cur = con.cursor()
        cur.execute('DROP TABLE IF EXISTS reg_data')


def add_user(id: int, username: str, name: str, email: str, age: int):
    with sq.connect('users_data.db') as con:
        cur = con.cursor()
        cur.execute('INSERT INTO reg_data VALUES(?, ?, ?, ?, ?)', [id, username, name, email, age])
        con.commit()


def get_all_users():
    with sq.connect('users_data.db') as con:
        cur = con.cursor()
        cur.execute('''
            SELECT * FROM reg_data
        ''')
        result = cur.fetchall()
        data = []
        keys = ['id', 'username', 'name', 'email', 'age']
        for user in result:
            data.append(dict(zip(keys, user)))
        return data
