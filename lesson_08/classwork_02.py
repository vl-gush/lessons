"""
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у объекта. Создать
один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
"""

from classwork_01 import Dog


class NewDog(Dog):

    def change_name(self, new_name: str):
        self.name = new_name


if __name__ == "__main__":
    dog = NewDog(20, 5, "First", 3)
    print(dog.name)
    dog.change_name("Second")
    print(dog.name)
