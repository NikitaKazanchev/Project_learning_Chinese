# Написать код, который показывает карточку с иероглифом + на карточке можно проиграть его произношение (аудиофайл)
# Создать словарь с переводом и иероглифом - ок
# При запуске программы появляется рандомный иероглиф - ок
# Написать функцию, которая по вызову будет выводить на экран иероглиф по ключу из словаря - ок
# По кнопке "открыть" появляется перевод - ок    
# Написать цикл While True, в котором Input будет просить написать ввести команду "Открыть", чтобы показать перевод. - ок
# Далее if написал "Открыть" - показывается перевод - ок
# После перевода появляется кнопка "Изучаю" и "Выучил" - ок
# в этом же цикле новый Input чтобы ввести команды "Изучаю" и "Выучил - ок
# Если выбрал "Изучаю" иероглиф также рандомно может появится в списке - ок
# Далее if "Изучаю" - тут подумать. - ок
# Если выбрал "Выучил" иероглиф откладывается и больше не появляется - ок
# elif "Выучил" - подумать - ок
# После выбора появляется новый иероглиф - ок

# 11/04:

# Написать функцию, которая будет выдавать первые 5 карточек иероглифов из словаря для изучения
# Далее будет запоминать какие иероглифы выучил, а какие нет
# На следующий день будет выдавать следующие 5 карточек из списка + те, которые не выучил в предыдущие дни
# Создать файл json, где будут хранится выученные слова, которые не будут повторяться и весь словарь с иероглифами

# С учетом прошлой записи это надо будет разбить на мелкие функции
# + выкладывать в общий репозиторий

import random
import json

path_to_data = r'C:\projects\projects_china_site\data.json'
path_to_learned = r'C:\projects\projects_china_site\learned.json'
path_to_not_learned = r'C:\projects\projects_china_site\notlearned.json'

def open_json(path_to_file):
    try:
        with open(path_to_file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
            data = []
    return data

def get_data(hieroglyphs_dict_in_list):
    item = random.choice(hieroglyphs_dict_in_list)
    return item

def decompose(item):
    hieroglyph = item.get('иероглиф',{})
    translation = item.get('перевод',{})
    return hieroglyph, translation

def save(item, lists_of_hieroglyphs, path_to_file):
    lists_of_hieroglyphs.append(item)
    with open(path_to_file, 'w', encoding='utf-8') as json_file:
        json.dump(lists_of_hieroglyphs, json_file)
    

hieroglyphs_dict_in_list = open_json(path_to_data)
learned = open_json(path_to_learned)
not_learned = open_json(path_to_not_learned)
counter = 5
while counter:
    item = get_data(hieroglyphs_dict_in_list)
    hieroglyph, translation = decompose(item)
    if hieroglyph in learned:
        continue
    counter -= 1
    print(hieroglyph) 
    is_show_translate = input('Нажми Enter, чтобы увидеть перевод иероглифа: ')
    if is_show_translate == '':
        print(translation)
        is_user_learned = input('Выучил?: ')
        if is_user_learned == 'Да':
            save(item, learned, path_to_learned)
        else:
            save(item, not_learned, path_to_not_learned)





