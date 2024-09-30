import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
       pk INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT NOT NULL,
       password TEXT NOT NULL,
       favourite_color TEXT
    );"""
)

connection.commit()
connection.close()
