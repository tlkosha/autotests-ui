import pytest

@pytest.fixture(autouse=True) #(autouse=True) - автоматический запуск
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")

@pytest.fixture(scope="session")  #scope session - запускается 1 раз на всю сессию
def settings():
    print("[SESSION] Инициализируем настройки автотестов")

@pytest.fixture(scope="class") #scope="class" запускается 1 раз на тестовый класс
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope="function") #дефолтно всегда scope = function, можно не указывать как здесь. Запускается 1 раз на функцию
def browser():
    print("[FUNCTION] Открываем браузер на каждый автотест")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...

class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...