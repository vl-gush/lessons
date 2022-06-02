"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное, в
идеале не использовать библиотечные функции.
"""


def most_common_and_longer(text):
    word_list = text_to_list(text)
    return (
        get_most_common_word(word_list),
        get_longer_word(word_list)
    )


def text_to_list(text):
    word_list = []
    word = ""
    index = 0

    while index < len(text):
        if text[index].isalpha():
            word += text[index].lower()
            if index == len(text) - 1:
                word_list.append(word)
        else:
            if len(word) != 0:
                word_list.append(word)
                word = ""
        index += 1
    return word_list


def get_longer_word(words):
    result = words[0]
    for word in words[1:]:
        if len(word) > len(result):
            result = word
    return result


def get_most_common_word(words):
    d = {}
    for word in words:
        d[word] = d.get(word, 0) + 1
    counter = 0
    for key, value in d.items():
        if counter < value:
            counter = value
            result = key
    return result


print(most_common_and_longer(input("Text: ")))
