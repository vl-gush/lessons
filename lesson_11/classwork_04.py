"""
Создать функцию, которая позволяет добавлять данные в таблицу user. Добавить 5 различных записей.
"""

import sqlite3


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age)
            VALUES (?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age),
        )
        session.commit()


if __name__ == "__main__":
    create_user("Vladislav", "Gushtyn", "test.email", "test", 25)
    create_user("Vysotskiy", "Denis", "test.email", "test", 26)
    create_user("Robert", "Urban", "test.email", "test", 26)
    create_user("Anton", "Shamko", "test.email", "test", 24)
    create_user("Sergey", "Gushtyn", "test.email", "test", 28)
