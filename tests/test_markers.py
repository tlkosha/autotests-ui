import pytest

@pytest.mark.smoke
def test_some_case():
    ...
@pytest.mark.regression  #можно весить несколько маркировок на один тест. чтобы исключить и запустить только с 1 маркировкой тесты - 'smoke and not regression'
@pytest.mark.smoke
def regression_case():
    ...

@pytest.mark.regression #Маркировка на класс
@pytest.mark.smoke
class TestSuite:
    def test_case(self):
        ...

    def test_case2(self):
        ...

###########################################################
@pytest.mark.regression #Действует на все функции в классе. Если хотим исключить slow - python -m pytest -s -v -m 'regression and not slow'
class TestUserAuthentification:
    @pytest.mark.smoke
    def test_login(self):
        ...
    @pytest.mark.slow
    def password_reset(self):
        ...

    def test_logout(self):
        ...

    # Если хотим запустить тесты и regression и slow, т.е. только 1 из этих то python -m pytest -s -v -m "regression and slow"

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    ...

@pytest.mark.ui
class TestUserInterface:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass