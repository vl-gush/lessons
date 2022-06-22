"""
Создать программу с пользовательским интерфейсом позволяющим выбирать определенную функцию и вводить необходимые данные.
"""

from solution_01 import create_product, read_product, update_product, delete_product


def user_interface(command: str):
    if command.lower() == "добавить":
        name = input("Введите название товара: ")
        price = int(input("Введите цену товара: "))
        quantity = int(input("Введите количество товара: "))
        comment = input("Введите комментарий к товару [null]: ")
        comment = comment or None
        create_product(name, price, quantity, comment)
    elif command.lower() == "прочитать":
        name = input("Введите название товара: ")
        print(read_product(name))
    elif command.lower() == "изменить":
        id = int(input("Введите id товара, который хотите изменить: "))
        new_name = input("Введите новое имя товара: ")
        new_quantity = int(input("введите новое количество товара: "))
        new_price = int(input("Введите новую цену товара: "))
        update_product(id, new_name, new_quantity, new_price)
    elif command.lower() == "удалить":
        id = int(input("Введите id продукта, который хотите удалить: "))
        delete_product(id)


if __name__ == "__main__":
    commands = ["добавить", "прочитать", "изменить", "удалить"]
    command = input(f"Введите команду {commands}: ")
    if command in commands:
        user_interface(command)
    else:
        print("Неподдерживаемая команда")
