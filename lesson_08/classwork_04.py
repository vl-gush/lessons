"""
Создать общий класс Animal, содержащий все общие методы классов Dog и Cat. Унаследовать Dog и Cat от класса Animal и
Удалить в дочерних классах те методы, которые имеются у родительского класса. Создать объект каждого класса и вызвать
все его методы.
"""

class Animal:
    def __init__(self, weight: int, height: int, name: str, age: int):
        self.weight = weight
        self.height = height
        self.name = name
        self.age = age

    def jump(self):
        print(f"{self.name} is jumping.")

    def run(self):
        print(f"{self.name} is running")

    def talk(self):
        raise NotImplementedError
