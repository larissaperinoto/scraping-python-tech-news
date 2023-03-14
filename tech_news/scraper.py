from parsel import Selector
import requests
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url: str):
    headers = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
        time.sleep(1)

    except (requests.ReadTimeout, requests.HTTPError):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(".entry-title a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    if type(html_content) is not str:
        return None
    BASE_URL = "https://blog.betrybe.com"
    selector = Selector(text=html_content)
    next_page_url = selector.css(".current::text").get()
    if next_page_url is None:
        return None
    return f"{BASE_URL}/page/{str(int(next_page_url) + 1)}/"


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    reading_time = selector.css(".meta-reading-time *::text").get()
    css_query = "div.entry-content:first-of-type > p:nth-of-type(1) *::text"
    summary = "".join(selector.css(css_query).getall())
    category = selector.css(".category-style .label::text").get()
    return {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time.split()[0]),
        "summary": summary.strip(),
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    next_page = 'https://blog.betrybe.com/'
    news = []

    while next_page:
        page_content = fetch(next_page)
        urls = scrape_updates(page_content)
        for url in urls:
            news_content = fetch(url)
            news_dict = scrape_news(news_content)
            news.append(news_dict)
            create_news(news_dict)

            if len(news) == amount:
                next_page = None
                return news
            else:
                next_page = scrape_next_page_link(page_content)
