import unittest

from parser import parser_app


def test_categories_contains():
    incorrect = ('https://ria.ru/20201202/vypivka-1587384879.html',
    'https://ria.ru/20201202/kosmonavty-1587384178.html')
    correct = 'https://ria.ru/20201202/vaktsinatsiya-1587383472.html'
    for url in incorrect:
        categories = parser_app.check_categories(url)
        assert len(categories) == 0
    categories = parser_app.check_categories(correct)
    assert len(categories) > 0