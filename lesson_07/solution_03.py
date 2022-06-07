"""
Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина. Каждая строка входного файла
представляет собой запись вида Покупатель, Товар, Количество, Стоимость где Покупатель - имя покупателя (строка без
пробелов), товар - название товара (строка без пробелов), количество - количество приобретенных единиц товара.
- Создайте список и выведите на экран всех покупателей, а для каждого покупателя подсчитайте общее количество
  приобретенных им товаров и их стоимость.
- Создайте список и выведите на экран все товары, а для каждого товара подсчитайте общее количество приобретенных и их
  стоимость.
"""
import csv


def buyers(purchases):
    d = {}
    for buyer, _, quantity, cost in purchases:
        if buyer not in d:
            d[buyer] = [0, 0]
        d[buyer][0] += int(quantity)
        d[buyer][1] += int(cost) * int(quantity)
    return d


def products(purchases):
    d = {}
    for _, product, quantity, cost in purchases:
        if product not in d:
            d[product] = [0, 0]
        d[product][0] += int(quantity)
        d[product][1] += int(cost) * int(quantity)
    return d


def main():
    with open("dictionary.csv") as f:
        purchases = csv.reader(f)
        result_buyers = buyers(purchases)
        for key, value in result_buyers.items():
            print(f"{key} купил {value[0]} товаров на сумму {value[1]}")

    print()

    with open("dictionary.csv") as f:
        purchases = csv.reader(f)
        result_products = products(purchases)
        for key, value in result_products.items():
            print(f"{key.capitalize()} купили {value[0]} раз на сумму {value[1]}")


if __name__ == "__main__":
    main()
