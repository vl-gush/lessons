"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек, т.е. реализовать цикл в котором на каждом
ходу у игрока спрашивается, достать ли следующую карту, в случае положительного ответа  - вытягивать случайную карту.
Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.
"""
from classwork_03 import get_card

my_dict = {
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 3,
    "Q": 4,
    "K": 5,
    "A": 1
}


def nominal_to_value(num):
    return my_dict[num]


n, _ = get_card()
value = nominal_to_value(n)

score = value

while True:
    print("Your score:", score)
    answer = input("Достать карту? [Y/n]\n")
    if answer == "n":
        break
    n, _ = get_card()
    value = nominal_to_value(n)
    score += value

    if score > 21:
        print("Game over.")
        break

    elif score == 21:
        print("You winner!")


