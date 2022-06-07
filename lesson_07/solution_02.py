"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы, которая считывает
название города и выводит на печать страну.
"""

d = {
    "Belarus": ["Minsk", "Vitebsk", "Mogilev", "Brest"],
    "Russia": ["Moscow", "Saint-Petersburg", "Krasnodar", "Ekaterinburg"],
    "USA": ["New York", "Washington", "Chicago", "Boston", "Los Angeles"]
}


def get_country_by_city(city):
    for country, cities in d.items():
        if city in cities:
            return country
    return "The city is not in the database"


def main():
    city = input("Enter the name of the city: ")
    print(get_country_by_city(city))


if __name__ == "__main__":
    main()
