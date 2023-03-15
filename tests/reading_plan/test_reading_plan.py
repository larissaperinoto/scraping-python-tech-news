from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
""" from unittest import mock, TestCase
 """

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
    """ database.find_news = mock.MagicMock(return_value=mock_data) """
    """   find_news_mock = mock.patch.object(ReadingPlanService, "_db_news_proxy")
    mockando = find_news_mock.start()
    mockando.return_value = mock_data """
    try:
        ReadingPlanService.group_news_for_available_time(-1)
    except ValueError as e:
        print(str(e))
        assert str(e) == "Valor 'available_time' deve ser maior que zero"

    """ find_news_mock.stop() """
