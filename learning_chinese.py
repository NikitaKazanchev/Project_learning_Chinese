from random import sample
from dictionary_of_hieroglyphs import CHINESE_RUSSIAN_DICTIONARY
import json
from config import NUMBER_OF_WORDS_TO_STUDY, STUDIED_WORDS, REPET_THE_WORDS
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

def write(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def read(filename):
    with open(filename, "r", encoding="utf-8") as file:
       return json.load(file)
       

def adding_a_style():
    custom_theme = Theme({
    "good" : "green",
    "bad": "bold red",
    "text": "blue",
    "dict": "dark_orange3",
    })
    console = Console(theme=custom_theme)
    return console

def table(the_dictionary_being_studied):
    hieroglyphs_with_translation = dict(the_dictionary_being_studied)
    table = Table(title="[dark_orange3]Изучаемые слова[/dark_orange3]")
    table.add_column("[blue]Иероглиф[/blue]", style="cyan")
    table.add_column("[blue]Перевод[/blue]", justify="right", style="cyan")
    for studied_hieroglyph, studied_translation in hieroglyphs_with_translation.items():
        table.add_row(studied_hieroglyph, studied_translation, style="dark_orange3")
    return table


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
        list_of_hieroglyphs_with_translation = sample(list_of_words, NUMBER_OF_WORDS_TO_STUDY)
        for hieroglyph, translation in dict(list_of_hieroglyphs_with_translation).items():
            if hieroglyph in chinese_russian_dictionary:
                #полученный для изучения словарь удаляем по ключу из общего словаря.
                #что бы не получать повторно изученного материала.
                del chinese_russian_dictionary[hieroglyph]  
        return list_of_hieroglyphs_with_translation


def word_knowledge_test():
    learned_hieroglyphs = {}
    learned_hieroglyphs = read(STUDIED_WORDS)
    words_to_repeat = {}
    studied_words =  dict(getting_the_list_under_study())
    words_to_repeat = read(REPET_THE_WORDS)
    studied_words.update(words_to_repeat)
    style_text = adding_a_style()
    style_text.print(table(studied_words))
    for studied_hieroglyph, studied_translation in studied_words.items():
        translate_request = style_text.input(f"[text]Введите перевод[/text] [dict]{studied_hieroglyph}[/dict] ")
        if translate_request == studied_translation:
            style_text.print("Верно :thumbs_up:", style="good")
            learned_hieroglyphs[studied_hieroglyph] = studied_translation        
            write(learned_hieroglyphs, STUDIED_WORDS)
        else:
            style_text.print(f'[bad]Не верно![/bad] [text]правильный ответ :[/text] [dict]"{studied_translation}"[/dict]')
            words_to_repeat[studied_hieroglyph] = studied_translation
            write(words_to_repeat, REPET_THE_WORDS)

if __name__ == "__main__":
    word_knowledge_test()
