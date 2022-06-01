"""
Написать функцию, которая используя модуль requests скачивает файл сохраняет
его на файловой системе, функция имеет два параметра: ссылка на файл и имя на
файловой системе. В качестве примера ссылки на файл можно использовать лицензию
из ГитХаба из вашего репозитория:
https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE
"""
import requests


def download_file(file_url, file_path):
    response = requests.get(file_url).text
    with open(file_path, "w") as file:
        file.write(response)


download_file(
    "https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE",
    "example"
)
