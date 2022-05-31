"""
Вывести в порядке возрастания все простые числа, расположенные между n и m
(включая сами числа n и m), а также количество x этих чисел.
"""

n = int(input("Введите число: "))
m = int(input("Введите число: "))

numbers = []

for i in range(n, m + 1):
    dividers = []
    for j in range(2, i + 1):
        if i % j == 0:
            dividers.append(j)
    if len(dividers) == 1:
        numbers.append(i)

print(*numbers, sep=", ")
print(len(numbers))
