import pytest


@pytest.fixture(scope="module", autouse=True)
def class_setup_teardown():
    # Выполняется один раз перед всеми тестами в классе
    print("\n----module-level setup----")
    yield
    # Выполняется один раз после всех тестов в классе
    print("\n----module-level teardown----")
