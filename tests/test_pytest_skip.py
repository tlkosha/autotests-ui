import pytest

@pytest.mark.skip(reason="Фича в разработке") #Причина пропуска
def test_feature_in_development():
    ...
@pytest.mark.skip(reason="Фича в разработке") #тест с маркировкой skip не будет запущен и сразу попадает в 1 skipped
class TestSuiteSkip:
    def test_feature_in_development_1(self):
        ...

    def test_feature_in_development_2(self):
        ...