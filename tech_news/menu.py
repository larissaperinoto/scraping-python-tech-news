from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date, search_by_category
)
import sys

menu = """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
 """

actions = {
    0: "Digite quantas notícias serão buscadas:",
    1: "Digite o título:",
    2: "Digite a data no formato aaaa-mm-dd:",
    3: "Digite a categoria:",
}


def analyzer_menu():
    option = int(input(menu))
    return switch(option)


def switch(option):
    match option:
        case 0:
            response = input(actions[option])
            return get_tech_news(int(response))
        case 1:
            title = input(actions[option])
            return search_by_title(title)
        case 2:
            date = input(actions[option])
            return search_by_date(date)
        case 3:
            category = input(actions[option])
            return search_by_category(date)
        case 4:
            return top_5_categories()
        case 5:
            return print("Até a próxima!")
        case _:
            sys.stderr.write("Opção inválida")
