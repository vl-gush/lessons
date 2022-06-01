"""
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык. Написать две функции,
одна переводит слово с английского на русский, где слово - это входной параметр, вторая функция - с русского на
английский.
"""

my_words = {
   "word": "слово",
   "street": "улица",
   "city": "город",
   "red": "красный",
   "sister": "сестра"
}


def eng_to_rus(word):
   return my_words[word]


def rus_to_eng(word):
   for key, value in my_words.items():
      if my_words[key] == word:
         return key


print(eng_to_rus("street"))
print(rus_to_eng("слово"))