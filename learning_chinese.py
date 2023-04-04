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


def checking_the_knowledge_of_hieroglyphs(number_of_words_to_study):
    worker_chinese_russian_dict = chinese_russian_dict()
    learned_hieroglyphs = {}
    if len(learned_hieroglyphs) == 0:
        learned_hieroglyphs = read("studied_words.json")
        for deleted_hieroglyphs, deleted_translation in dict(learned_hieroglyphs).items():
            del worker_chinese_russian_dict[deleted_hieroglyphs]
    print(len(worker_chinese_russian_dict))
    print(learned_hieroglyphs)        
    while worker_chinese_russian_dict:
        list_of_words = list(worker_chinese_russian_dict.items())
        list_of_hieroglyphs_with_translation = sample(list_of_words, number_of_words_to_study)  
        studied_hieroglyphs_with_translation = {}
        for hieroglyph,translation in dict(list_of_hieroglyphs_with_translation).items():  
            studied_hieroglyphs_with_translation[hieroglyph] = translation
            if hieroglyph in worker_chinese_russian_dict:
                del worker_chinese_russian_dict[hieroglyph]  # полученный для изучения словарь удаляем по ключу из общего словаря. что бы не получать повторно изученные слова
                write(worker_chinese_russian_dict, "remaining_words.json")
        print(f"Изучаемые слова: {studied_hieroglyphs_with_translation}")
        while studied_hieroglyphs_with_translation:
            studied_hieroglyph, studied_translation = choice(list(studied_hieroglyphs_with_translation.items()))
            transfer_request = input(f"Введите перевод {studied_hieroglyph} ")
            if transfer_request in studied_translation:
                print("Верно")
                learned_hieroglyphs[studied_hieroglyph] = studied_translation
                write(learned_hieroglyphs, "studied_words.json")
                del studied_hieroglyphs_with_translation[studied_hieroglyph]
                print(learned_hieroglyphs)
            else:
                print(f'Не верно! правильный ответ : "{translation}"')
            
         
if __name__ == "__main__":
    checking_the_knowledge_of_hieroglyphs(3)    
    


