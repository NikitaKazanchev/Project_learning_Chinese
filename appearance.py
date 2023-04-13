from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.progress import track
from time import sleep


def process_data(studied, the_number_of_all_words):
    sleep(0.02)

    for _ in track(studied, description='[green]Прогресс', total=the_number_of_all_words):
        continue


def text_output_style():
    custom_theme = Theme({
        "good" : "green",
        "bad": "bold red",
        "text": "blue",
        "dict": "dark_orange3",
    })
    console = Console(theme=custom_theme)
    return console


def framing_the_table(the_dictionary_being_studied):
    hieroglyphs_with_translation = dict(the_dictionary_being_studied)
    table = Table(title="[dark_orange3]Изучаемые слова[/dark_orange3]")
    table.add_column("[blue]Иероглиф[/blue]", style="cyan")
    table.add_column("[blue]Перевод[/blue]", justify="right", style="cyan")
    for studied_hieroglyph, studied_translation in hieroglyphs_with_translation.items():
        table.add_row(studied_hieroglyph, studied_translation, style="dark_orange3")
    return table
