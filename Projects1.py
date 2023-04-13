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
from config import PATH_TO_DATA, PATH_TO_LEARNED, PATH_TO_NOT_LEARNED

def open_json(path_to_file):
    try:
        with open(path_to_file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
            data = []
    return data

def get_hieroglyphs_dict(hieroglyphs_dict_in_list):
    return random.choice(hieroglyphs_dict_in_list)

def decompose(item):
    hieroglyph = item['иероглиф']
    translation = item['перевод']
    return hieroglyph, translation

def save(lists_of_hieroglyphs, path_to_file, item=''):
    if item:
        lists_of_hieroglyphs.append(item)
    with open(path_to_file, 'w', encoding='utf-8') as json_file:
        json.dump(lists_of_hieroglyphs, json_file, ensure_ascii=False)
    
if __name__ == '__main__':

    hieroglyphs_dict_in_list = open_json(PATH_TO_DATA)
    learned = open_json(PATH_TO_LEARNED)
    not_learned = open_json(PATH_TO_NOT_LEARNED)
    for card_number in range(4):
        item = get_hieroglyphs_dict(hieroglyphs_dict_in_list)
        hieroglyph, translation = decompose(item)
        print(hieroglyph) 
        is_show_translate = input('Нажми Enter, чтобы увидеть перевод иероглифа: ')
        if is_show_translate == '':
            print(translation)
        is_user_learned = input('Выучил?: ')
        if is_user_learned == 'Да':
            save(learned, PATH_TO_LEARNED, item)
        else:
            save(not_learned, PATH_TO_NOT_LEARNED, item)
        hieroglyphs_dict_in_list.pop(hieroglyphs_dict_in_list.index(item))
        save(hieroglyphs_dict_in_list, PATH_TO_DATA)

    print('Мы закончили ежедневное изучение, теперь повторим не выученные иероглифы')

    still_not_learned = []
    for not_learnead_card in not_learned:
        hieroglyph, translation = decompose(not_learnead_card)
        print(hieroglyph)
        is_show_translate = input('Нажми Enter, чтобы увидеть перевод иероглифа: ')
        if is_show_translate == '':
            print(translation)
            is_user_learned = input('Выучил?: ')
            if is_user_learned == 'Да':
                save(learned, PATH_TO_LEARNED, not_learnead_card)
            else:
                still_not_learned.append(not_learnead_card)
    
    save(still_not_learned, PATH_TO_NOT_LEARNED)