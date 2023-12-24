from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import locators as loc
from constants import constants as const


class TestsLoginChecks:

    # Проверка входа по кнопке «Войти в аккаунт» на главной
    def test_login_in_account_button(self, driver):
        driver.find_element(By.XPATH, loc.LOGIN_TO_ACCOUNT).click()  # Нажимаем «Войти в аккаунт»
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(const.TEST_EMAIL)  # Вводим email
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(const.PASSWORD)  # Вводим пароль
        driver.find_element(By.XPATH, loc.ENTER_TO_ACCOUNT).click()  # Нажимаем кнопку «Войти»
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(const.BASE_URL))  # Ждем переход
        assert driver.current_url == const.BASE_URL  # Проверяем переход на базовый URL

    # Проверка входа через кнопку «Личный кабинет»
    def test_login_account_personal_area_button(self, driver):
        driver.find_element(By.XPATH, loc.PERSONAL_AREA_BUTTON).click()  # Нажимаем кнопку «Личный Кабинет»
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(const.TEST_EMAIL)  # Вводим email
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(const.PASSWORD)  # Вводим пароль
        driver.find_element(By.XPATH, loc.ENTER_TO_ACCOUNT).click()  # Нажимаем кнопку «Войти»
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(const.BASE_URL))  # Ждем переход
        assert driver.current_url == const.BASE_URL  # Проверяем переход на базовый URL

    # Проверка входа через кнопку в форме регистрации
    def test_login_account_registration_page(self, driver):
        driver.find_element(By.XPATH, loc.PERSONAL_AREA_BUTTON).click()  # Нажимаем кнопку «Личный Кабинет»
        driver.find_element(By.XPATH, loc.REGISTER_BUTTON).click()  # Нажимаем кнопку «Зарегистрироваться»
        driver.find_element(By.XPATH, loc.ENTER_TO_ACCOUNT_LINK).click()  # Нажимаем кнопку «Войти»
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(const.TEST_EMAIL)  # Вводим email
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(const.PASSWORD)  # Вводим пароль
        driver.find_element(By.XPATH, loc.ENTER_TO_ACCOUNT).click()  # Нажимаем кнопку «Войти»
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(const.BASE_URL))  # Ждем переход
        assert driver.current_url == const.BASE_URL  # Проверяем переход на базовый URL

    # Проверка входа через кнопку в форме восстановления пароля
    def test_login_account_recover_password(self, driver):
        driver.find_element(By.XPATH, loc.PERSONAL_AREA_BUTTON).click()  # Нажимаем кнопку «Личный Кабинет»
        driver.find_element(By.XPATH, loc.RECOVER_PASSWORD).click()  # Нажимаем кнопку «Восстановить пароль»
        driver.find_element(By.XPATH, loc.BUTTON_REMEMBERED_THE_PASSWORD).click()  # Нажимаем «Вспомнили пароль? Войти»
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(const.TEST_EMAIL)  # Вводим email
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(const.PASSWORD)  # Вводим пароль
        driver.find_element(By.XPATH, loc.ENTER_TO_ACCOUNT).click()  # Нажимаем кнопку «Войти»
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(const.BASE_URL))  # Ждем переход
        assert driver.current_url == const.BASE_URL  # Проверяем переход базовый URL
