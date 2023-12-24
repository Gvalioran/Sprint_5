from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import locators as loc
from constants import constants as const


class TestsRegisterPage:

    # Проверка ограничения регистрации без имени
    def test_register_account_not_name(self, driver, generating_test_data):
        driver.find_element(By.XPATH, loc.PERSONAL_AREA_BUTTON).click()  # Нажимаем кнопку «Личный Кабинет»
        driver.find_element(By.XPATH, loc.REGISTRATION_PAGE_BUTTON).click()  # Нажимаем кнопку «Зарегистрироваться»
        driver.find_element(By.XPATH, loc.EMAIL_INPUT_FIELD).send_keys(generating_test_data[1])  # Вводим email
        driver.find_element(By.XPATH, loc.PASSWORD_INPUT_FIELD).send_keys(generating_test_data[2])  # Вводим пароль
        driver.find_element(By.XPATH, loc.REGISTER_BUTTON).click()  # Нажимаем кнопку «Зарегистрироваться»
        assert driver.current_url == const.REGISTRATION_URL  # Проверяем что страница осталась той же

    # Проверка ограничения регистрации с некорректным форматом почты
    def test_register_account_invalid_mail_format(self, driver, generating_test_data):
        driver.find_element(By.XPATH, loc.PERSONAL_AREA_BUTTON).click()  # Нажимаем на кнопку «Личный Кабинет»
        driver.find_element(By.XPATH, loc.REGISTRATION_PAGE_BUTTON).click()  # Нажимаем кнопку «Зарегистрироваться»
        driver.find_element(By.XPATH, loc.NAME_INPUT_FIELD).send_keys(generating_test_data[0])  # Вводим имя
        driver.find_element(By.XPATH, loc.EMAIL_INPUT_FIELD).send_keys(generating_test_data[0])  # Вводим неверный email
        driver.find_element(By.XPATH, loc.PASSWORD_INPUT_FIELD).send_keys(generating_test_data[2])  # Вводим пароль
        driver.find_element(By.XPATH, loc.REGISTER_BUTTON).click()  # Нажимаем кнопку «Зарегистрироваться»
        assert driver.current_url == const.REGISTRATION_URL  # Проверяем что страница осталась той же

    # Проверка ограничения регистрации с некорректным форматом пароля
    def test_register_account_invalid_password_format(self, driver, generating_test_data):
        driver.find_element(By.XPATH, loc.PERSONAL_AREA_BUTTON).click()  # Нажимаем на кнопку «Личный Кабинет»
        driver.find_element(By.XPATH, loc.REGISTRATION_PAGE_BUTTON).click()  # Нажимаем кнопку «Зарегистрироваться»
        driver.find_element(By.XPATH, loc.NAME_INPUT_FIELD).send_keys(generating_test_data[0])  # Вводим имя
        driver.find_element(By.XPATH, loc.EMAIL_INPUT_FIELD).send_keys(generating_test_data[1])  # Вводим email
        driver.find_element(By.XPATH, loc.PASSWORD_INPUT_FIELD).send_keys("12345")  # Вводим некорректный пароль
        driver.find_element(By.XPATH, loc.REGISTER_BUTTON).click()  # Нажимаем кнопку «Зарегистрироваться»
        assert (driver.find_element(By.XPATH, loc.ERROR_INVALID_PASSWORD_FIELD).text == "Некорректный пароль")
        # Проверяем наличие ошибки

    # Проверка регистрации с корректными данными
    def test_register_valid_account(self, driver, generating_test_data):
        driver.find_element(By.XPATH, loc.PERSONAL_AREA_BUTTON).click()  # Нажимаем на кнопку «Личный Кабинет»
        driver.find_element(By.XPATH, loc.REGISTRATION_PAGE_BUTTON).click()  # Нажимаем на кнопку «Зарегистрироваться»
        driver.find_element(By.XPATH, loc.NAME_INPUT_FIELD).send_keys(generating_test_data[0])  # Вводим имя
        driver.find_element(By.XPATH, loc.EMAIL_INPUT_FIELD).send_keys(generating_test_data[1])  # Вводим email
        driver.find_element(By.XPATH, loc.PASSWORD_INPUT_FIELD).send_keys(generating_test_data[2])  # Вводим пароль
        driver.find_element(By.XPATH, loc.REGISTER_BUTTON).click()  # Нажимаем кнопку «Зарегистрироваться»
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(const.LOGIN_IN_URL))  # Ждем переход
        assert driver.current_url == const.LOGIN_IN_URL  # Проверяем переход на страницу входа
