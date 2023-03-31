from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
import pytest

mock_data = [
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia bacana",
        "timestamp": "14/04/2021",
        "writer": "Fernando",
        "reading_time": 11,
        "summary": "Uma tecnologia muito bacana",
        "category": "Tecnologia",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia Mais bacana",
        "timestamp": "23/04/2021",
        "writer": "Maria",
        "reading_time": 6,
        "summary": "Uma tecnologia ainda mais bacana",
        "category": "Ferramentas",
    },
]


def test_reading_plan_group_news():
    m = "Valor 'available_time' deve ser maior que zero"
    with pytest.raises(ValueError, match=m):
        ReadingPlanService.group_news_for_available_time(-1)
