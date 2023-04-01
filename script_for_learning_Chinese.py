from random import sample, choice
from dictionary_of_hieroglyphs import CHINESE_RUSSIAN_DICTIONARY

def chinese_russian_dict():
    chinese_russian_dict = CHINESE_RUSSIAN_DICTIONARY.copy() # копируем словарь для работы с ним и сохранением оригинала
    return chinese_russian_dict

def checking_the_knowledge_of_hieroglyphs(k):
    worker_chinese_russian_dict = chinese_russian_dict()
    learned_hieroglyphs = {}
    while worker_chinese_russian_dict:
        list_of_words = list(worker_chinese_russian_dict.items())
        list_of_hieroglyphs_with_translation = sample(list_of_words, k)
        studied_hieroglyphs_with_translation = {}
        for hieroglyph,translation in dict(list_of_hieroglyphs_with_translation).items():
            studied_hieroglyphs_with_translation[hieroglyph] = translation
            if hieroglyph in worker_chinese_russian_dict:
                del worker_chinese_russian_dict[hieroglyph] # полученный для изучения словарь удаляем по ключу из общего словаря. что бы не получать повторно изученные слова
        print(f"Изучаемые слова: {studied_hieroglyphs_with_translation}")
        while studied_hieroglyphs_with_translation:
            studied_hieroglyph, studied_translation = choice(list(studied_hieroglyphs_with_translation.items()))
            transfer_request = input(f"Введите перевод {studied_hieroglyph} ")
            if transfer_request in studied_translation:
                print("Верно")
                learned_hieroglyphs[studied_hieroglyph] = studied_translation
                del studied_hieroglyphs_with_translation[studied_hieroglyph]
                print(learned_hieroglyphs)
            else:
                print(f'Не верно! правильный ответ : "{translation}"')
        

if __name__ == "__main__":
    checking_the_knowledge_of_hieroglyphs(3)
   