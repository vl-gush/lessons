# Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.

import random


n = random.randint(1, 10)

while n != 7:
    print(n)
    n = random.randint(1, 10)
