"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark.
Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы объекта и вывести на экран все
его атрибуты.
"""

from classwork_04 import Animal


class Dog(Animal):

    def talk(self):
        print(f"{self.name} is barking")


if __name__ == "__main__":
    dog1 = Dog(10, 5, "First", 3)
    dog1.jump()

    dog2 = Dog(10, 7, "Second", 5)
    dog2.talk()
