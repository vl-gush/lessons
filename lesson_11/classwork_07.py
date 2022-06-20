"""
Создать программу позволяющую осуществлять поиск по имени или возрасту, оба параметра вводятся с клавиатуры.
"""

import sqlite3


def select_user(name: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE firstname = ? OR age = ?;
            """,
            (name, age)
        )
        session.commit()
        return cursor.fetchall()


if __name__ == "__main__":
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    print(select_user(name, age))
