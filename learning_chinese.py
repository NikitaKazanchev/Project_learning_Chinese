from random import sample, choice
from dictionary_of_hieroglyphs import CHINESE_RUSSIAN_DICTIONARY
import json


def write(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def read(filename):
    with open(filename, "r", encoding="utf-8") as file:
       return json.load(file)
       

def chinese_russian_dict():
    chinese_russian_dict = CHINESE_RUSSIAN_DICTIONARY.copy()  # копируем словарь для работы с ним и сохранением оригинала
    return chinese_russian_dict


def getting_the_list_under_study(number_of_words_to_study):
    chinese_russian_dictionary = read("remaining_words.json")
    if len(chinese_russian_dictionary) == 0:
        chinese_russian_dictionary = chinese_russian_dict()
    while chinese_russian_dictionary:
        list_of_words = list(chinese_russian_dictionary.items())
        list_of_hieroglyphs_with_translation = sample(list_of_words, number_of_words_to_study)
        studied_hieroglyphs_with_translation = {}
        for hieroglyph,translation in dict(list_of_hieroglyphs_with_translation).items():
            studied_hieroglyphs_with_translation[hieroglyph] = translation
            if hieroglyph in chinese_russian_dictionary:
                del chinese_russian_dictionary[hieroglyph]  # полученный для изучения словарь удаляем по ключу из общего словаря. что бы не получать повторно изученного материала
                write(chinese_russian_dictionary, "remaining_words.json")
        return studied_hieroglyphs_with_translation


def word_knowledge_test():
    learned_hieroglyphs = {}
    if len(learned_hieroglyphs) == 0:
        learned_hieroglyphs = read("studied_words.json")
    studied_words =  getting_the_list_under_study(5)
    while studied_words:
        print(f"Изучаемые слова {studied_words}")
        studied_hieroglyph, studied_translation = choice(list(studied_words.items()))
        transfer_request = input(f"Введите перевод {studied_hieroglyph} ")
        if transfer_request in studied_translation:
            print("Верно")
            learned_hieroglyphs[studied_hieroglyph] = studied_translation        
            write(learned_hieroglyphs, "studied_words.json")
            del studied_words[studied_hieroglyph]
            if len(studied_words) == 0:
                studied_words = getting_the_list_under_study(5)
        else:
            print(f'Не верно! правильный ответ : "{studied_translation}"')


if __name__ == "__main__":
    word_knowledge_test()
