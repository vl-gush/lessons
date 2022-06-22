"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий. Реализовать следующие
функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""
import sqlite3


def create_product(name: str, price: int, quantity: int, comment: str = None):
    with sqlite3.connect("products_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO product (name, price, quantity, comment)
            VALUES (?, ?, ?, ?)
            """,
            (name, price, quantity, comment),
        )
        session.commit()


def read_product(name: str):
    with sqlite3.connect("products_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM product
            WHERE name = ?;
            """,
            (name,)
        )
        session.commit()
        return cursor.fetchone()


def update_product(id: int, new_name: str, new_quantity: int, new_price: int, new_comment: str = None):
    with sqlite3.connect("products_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            UPDATE product
            SET name = ?, quantity = ?, price = ?, comment = ?
            WHERE id = ?;
            """,
            (new_name, new_quantity, new_price, new_comment, id)
        )
        session.commit()


def delete_product(id: int):
    with sqlite3.connect("products_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM product
            WHERE id = ?;
            """,
            (id,)
        )
        session.commit()


if __name__ == "__main__":
    create_product("IPhone", 2000, 5)
    create_product("Samsung GALAXY", 1500, 10)
    create_product("Sony XPERIA", 1000, 15)
