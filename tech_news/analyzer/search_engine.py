from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": f"{title}", "$options": "i"}}
    result = []

    for news in search_news(query=query):
        result.append((news['title'], news['url']))

    return result


# Requisito 8
def search_by_date(date):
    try:
        isoFormat = datetime.fromisoformat(date).strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    query = {"timestamp": {"$regex": f"{isoFormat}"}}
    result = []

    for news in search_news(query=query):
        result.append((news['title'], news['url']))

    return result


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": f"{category}", "$options": "i"}}
    result = []

    for news in search_news(query=query):
        result.append((news['title'], news['url']))

    return result
