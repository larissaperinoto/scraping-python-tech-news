from tech_news.database import find_news
from collections import Counter


def top_5_categories():
    categories = []

    for news in find_news():
        categories.append(news["category"])

    counted = Counter(sorted(categories))
    most_common = sorted(counted, key=counted.get, reverse=True)

    return most_common[0:5]

