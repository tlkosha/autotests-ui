import pytest

@pytest.mark.xfail (reason="Найден баг в приложении, из-за которого тест падает с ошибкой") #в данном тесте мы ожидаем баг и он попадет в xpassed,а не упадет с error. тест запускается
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail (reason="Баг уже исправлен, но на тест все еще висит маркировка xfail")
def test_without_bug():
    ...

