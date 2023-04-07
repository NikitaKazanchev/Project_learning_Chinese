from random import sample
from rich.console import Console
from rich.theme import Theme
from rich.table import Table


chines_russian_dictionary = {
    "爱":"любить; любовь; любимый",
    "八": "восемь, восьмой",
    "爸爸": "папа, тятя",
    "杯子": "стакан, кружка, бокал, рюмка",
    "北京": "Пекин",
    "本": "счетное слово для растений, цветов",
    "不客, 气": "не церемоньтесь, не стесняйтесь",
    "不": "отрицательная частица не",
    "菜": "овощи, блюдо, пища, стол",
    "茶": "чай",
    "吃": "есть, кушать",
    "出租车": "такси",
    "打电话": "звонить по телефону",
    "大": "большой, крупный, великий,огромный",
    "的": "суффикс прилагательного, суффикс притяжательности",
    "点": "капля, немножко, чуточку, точка, запятая",    
    "电脑": "компьютер",
    "电视": "телевидение, телевизионный",
    "电影": "кино",
    "东西": "вещь, предмет",
    "都": "все, всё",
    "读": "читать, зачитывать",
    "对不起": "виноват, простите, извините",
    "多": "много, многочисленный, свыше",
    "多少": "сколько",
    "儿子": "сын",
    "二": "два, второй",
    "饭馆": "ресторан, столовая",
    "飞机": "самолёт",
    "分钟": "минута",
    "高兴": "радоваться, радостный",
    "个": "отдельный, индивидуальный",
    "工作": "работать, работа",
    "狗": "собака, собачий",
    "汉语": "китайский язык",
    "好": "хороший, хорошо, приятный, удобный",
    "喝": "пить",
    "和": "мирный, союз и, предлог с",
    "很": "очень, весьма",
    "后面": "задняя сторона, зад, позади, сзади, задний",
    "回": "возвращаться",
    "会": "уметь, мочь, владеть, собрание, заседание",
}

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
    chinese_russian_dict = chines_russian_dictionary.copy()  #копируем словарь для работы с ним и сохранением оригинала
    return chinese_russian_dict


def getting_the_list_under_study():
    chinese_russian_dictionary = chinese_russian_dict()
    learned_hieroglyphs = {}
    if learned_hieroglyphs:
        for studied_hieroglyph, studied_translation in dict(learned_hieroglyphs).items():
            del chinese_russian_dictionary[studied_hieroglyph]    
    while chinese_russian_dictionary:
        list_of_words = list(chinese_russian_dictionary.items())
        list_of_hieroglyphs_with_translation = sample(list_of_words, 3)
        for hieroglyph, translation in dict(list_of_hieroglyphs_with_translation).items():
            if hieroglyph in chinese_russian_dictionary:
                #полученный для изучения словарь удаляем по ключу из общего словаря.
                #что бы не получать повторно изученного материала.
                del chinese_russian_dictionary[hieroglyph]  
        return list_of_hieroglyphs_with_translation


def word_knowledge_test():
    learned_hieroglyphs = {}
    words_to_repeat = {}
    studied_words =  dict(getting_the_list_under_study())
    studied_words.update(words_to_repeat)
    style_text = adding_a_style()
    style_text.print(table(studied_words))
    for studied_hieroglyph, studied_translation in studied_words.items():
        translate_request = style_text.input(f"[text]Введите перевод[/text] [dict]{studied_hieroglyph}[/dict] ")
        if translate_request == studied_translation:
            style_text.print("Верно :thumbs_up:", style="good")
            learned_hieroglyphs[studied_hieroglyph] = studied_translation        
        else:
            style_text.print(f'[bad]Не верно![/bad] [text]правильный ответ :[/text] [dict]"{studied_translation}"[/dict]')
            words_to_repeat[studied_hieroglyph] = studied_translation
            

if __name__ == "__main__":
    word_knowledge_test()
