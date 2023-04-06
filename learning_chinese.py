from random import sample, choice
from dictionary_of_hieroglyphs import CHINESE_RUSSIAN_DICTIONARY
import json
from config import EXERCISE_LENGHT_WORDS, STUDIED_WORDS


def write(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def read(filename):
    with open(filename, "r", encoding="utf-8") as file:
       return json.load(file)
       

def chinese_russian_dict():
    chinese_russian_dict = CHINESE_RUSSIAN_DICTIONARY.copy()  #копируем словарь для работы с ним и сохранением оригинала
    return chinese_russian_dict


def getting_the_list_under_study():
    chinese_russian_dictionary = chinese_russian_dict()
    learned_hieroglyphs = read(STUDIED_WORDS)
    if learned_hieroglyphs:
        for studied_hieroglyph, studied_translation in dict(learned_hieroglyphs).items():
            del chinese_russian_dictionary[studied_hieroglyph]    
    while chinese_russian_dictionary:
        list_of_words = list(chinese_russian_dictionary.items())
        list_of_hieroglyphs_with_translation = sample(list_of_words, EXERCISE_LENGHT_WORDS)
        studied_hieroglyphs_with_translation = {}
        for hieroglyph, translation in dict(list_of_hieroglyphs_with_translation).items():
            studied_hieroglyphs_with_translation[hieroglyph] = translation
            if hieroglyph in chinese_russian_dictionary:
<<<<<<< HEAD
                del chinese_russian_dictionary[hieroglyph]  # полученный для изучения словарь удаляем по ключу из общего словаря. что бы не получать повторно изученного материала
        print(len(chinese_russian_dictionary))
        return studied_hieroglyphs_with_translation
=======
                del chinese_russian_dictionary[hieroglyph]  #полученный для изучения словарь удаляем по ключу из общего словаря. что бы не получать повторно изученного материала
        return list_of_hieroglyphs_with_translation
>>>>>>> 03cb8dd0bf724519944ae4ebd79bdfe7c5b22e71


def word_knowledge_test():
    learned_hieroglyphs = {}
    learned_hieroglyphs = read(STUDIED_WORDS)
    studied_words =  getting_the_list_under_study()
    while studied_words:
        print(f"Изучаемые слова {studied_words}")
        studied_hieroglyph, studied_translation = choice(list(studied_words.items()))
        translate_request = input(f"Введите перевод {studied_hieroglyph} ")
        if translate_request == studied_translation:
            print("Верно")
            learned_hieroglyphs[studied_hieroglyph] = studied_translation        
            write(learned_hieroglyphs, STUDIED_WORDS)
            del studied_words[studied_hieroglyph]
        else:
            print(f'Не верно! правильный ответ : "{studied_translation}"')


if __name__ == "__main__":
    word_knowledge_test()
