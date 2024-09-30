import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users (
        username,
        password,
        favourite_color  -- Use the correct column name here
        )VALUES(
            'Gordon',
            'Ramsy',
            'Red'
    );"""
)

cursor.execute(
    """INSERT INTO users (
        username,
        password,
        favourite_color  -- Use the correct column name here
        )VALUES(
            'Ironman',
            'Tony',
            'Gold'
    );"""
)

connection.commit()
connection.close()
