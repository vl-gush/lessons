# Ввести с клавиатуры целое число n. Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while.

n = int(input("Введите число: "))
result = 0

while n > 0:
    result += n ** 3
    n -= 1

print(result)
