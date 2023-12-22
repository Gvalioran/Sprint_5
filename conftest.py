import pytest
import random
from selenium import webdriver
from locators import locators as loc


@pytest.fixture  # Фикстура для создания драйвера
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(loc.url)
    yield driver
    driver.quit()


@pytest.fixture()  # Фикстура, которая создает данные для регистрации пользователя
def generate_an_account():
    array = [chr(i) for i in range(65, 91)]
    random.shuffle(array)
    name = ""
    for i in range(random.randint(5, 10)):
        name += array.pop()
    login = f"{name}{random.randint(1000, 9999)}@yandex.ru"
    password = random.randint(100000, 999999)
    return name, login, password
