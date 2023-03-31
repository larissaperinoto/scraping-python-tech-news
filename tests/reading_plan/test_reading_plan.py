from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import MagicMock
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
    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock_data)

    m = "Valor 'available_time' deve ser maior que zero"
    with pytest.raises(ValueError, match=m):
        ReadingPlanService.group_news_for_available_time(-1)

    result = ReadingPlanService.group_news_for_available_time(10)

    assert len(result["readable"]) == 1
    assert len(result["unreadable"]) == 1

    if len(result["readable"]) > 0:
        assert result['readable'][0]['unfilled_time'] == 4
