from random import sample, choice
from dictionary_of_hieroglyphs import chinese_russian_dictionary

def chinese_russian_dict():
    chinese_russian_dict = chinese_russian_dictionary.copy() # копируем словарь для работы с ним и сохранением орегинала
    return chinese_russian_dict

def checking_the_knowledge_of_hieroglyphs():
    while chinese_russian_dict():
        list_of_words = list(chinese_russian_dict().items())
        list_of_hieroglyphs_with_translation = sample(list_of_words, 5)
        studied_hieroglyphs_with_translation = {}
        for hieroglyph,translation in dict(list_of_hieroglyphs_with_translation).items():
            studied_hieroglyphs_with_translation[hieroglyph] = translation
            if hieroglyph in chinese_russian_dict():
                del chinese_russian_dict()[hieroglyph]
        learned_hieroglyphs = {}
        while studied_hieroglyphs_with_translation:
            random_hieroglyph_with_translation = choice(list(studied_hieroglyphs_with_translation.items()))
            transfer_request = input(f"Введите перевод {random_hieroglyph_with_translation[0]} ")
            if transfer_request in random_hieroglyph_with_translation[1]:
                print("Верно")
                learned_hieroglyphs[random_hieroglyph_with_translation[0]] = random_hieroglyph_with_translation[1]
                del studied_hieroglyphs_with_translation[random_hieroglyph_with_translation[0]]
            else:
                print(f'Не верно! правильный ответ : "{random_hieroglyph_with_translation[1]}"')

if __name__ == "__main__":
    checking_the_knowledge_of_hieroglyphs()