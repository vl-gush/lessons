"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
"""

from classwork_04 import Animal


class Cat(Animal):

    def talk(self):
        print(f"{self.name} is meowing")


if __name__ == "__main__":
    cat = Cat(5, 3, "Cat", 1)
    cat.talk()
