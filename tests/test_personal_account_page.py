from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import locators as loc
from constants import constants as const


class TestsLoginChecks:

    # Проверка перехода по клику на «Личный кабинет»
    def test_transfer_to_personal_account(self, driver):
        driver.find_element(By.XPATH, loc.LOGIN_TO_ACCOUNT).click()  # Нажимаем кнопку «Войти в аккаунт»
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(const.TEST_EMAIL)  # Вводим email
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(const.PASSWORD)  # Вводим пароль
        driver.find_element(By.XPATH, loc.ENTER_TO_ACCOUNT).click()  # Нажимаем кнопку «Войти»
        driver.find_element(By.XPATH, loc.PERSONAL_AREA_BUTTON).click()  # Нажимаем кнопку «Личный Кабинет»
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(const.USER_PROFILE_URL))  # Ждем переход
        assert driver.current_url == const.USER_PROFILE_URL  # Проверяем переход на URL личного кабинета

    # Проверка перехода по клику на «Конструктор»
    def test_switching_to_constructor(self, driver):
        driver.find_element(By.XPATH, loc.LOGIN_TO_ACCOUNT).click()  # Нажимаем кнопку «Войти в аккаунт»
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(const.TEST_EMAIL)  # Вводим email
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(const.PASSWORD)  # Вводим пароль
        driver.find_element(By.XPATH, loc.ENTER_TO_ACCOUNT).click()  # Нажимаем кнопку «Войти»
        driver.find_element(By.XPATH, loc.PERSONAL_AREA_BUTTON).click()  # Нажимаем кнопку «Личный Кабинет»
        driver.find_element(By.XPATH, loc.BUTTON_CONSTRUCTOR).click()  # Нажимаем кнопку «Конструктор»
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(const.BASE_URL))  # Ждем переход
        assert driver.current_url == const.BASE_URL  # Проверяем переход базовый URL

    # Проверка перехода по клику на логотип Stellar Burgers
    def test_switching_to_constructor_through_logo(self, driver):
        driver.find_element(By.XPATH, loc.LOGIN_TO_ACCOUNT).click()  # Нажимаем кнопку «Войти в аккаунт»
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(const.TEST_EMAIL)  # Вводим email
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(const.PASSWORD)  # Вводим пароль
        driver.find_element(By.XPATH, loc.ENTER_TO_ACCOUNT).click()  # Нажимаем кнопку «Войти»
        driver.find_element(By.XPATH, loc.PERSONAL_AREA_BUTTON).click()  # Нажимаем кнопку «Личный Кабинет»
        driver.find_element(By.XPATH, loc.LOGO).click()  # Нажимаем кнопку Логотипа
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(const.BASE_URL))  # Ждем переход
        assert driver.current_url == const.BASE_URL  # Проверяем переход базовый URL

    # Проверка выхода по кнопке «Выйти» в личном кабинете
    def test_exit_account_button(self, driver):
        driver.find_element(By.XPATH, loc.LOGIN_TO_ACCOUNT).click()  # Нажимаем кнопку «Войти в аккаунт»
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(const.TEST_EMAIL)  # Вводим email
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(const.PASSWORD)  # Вводим пароль
        driver.find_element(By.XPATH, loc.ENTER_TO_ACCOUNT).click()  # Нажимаем кнопку войти
        driver.find_element(By.XPATH, loc.PERSONAL_AREA_BUTTON).click()  # Нажимаем кнопку «Личный Кабинет»
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, loc.EXIT_BUTTON)))
        driver.find_element(By.XPATH, loc.EXIT_BUTTON).click()  # Ждем и нажимаем кнопку «Выйти»
        WebDriverWait(driver, 3).until(expected_conditions.url_to_be(const.LOGIN_IN_URL))  # Ждем переход
        assert driver.current_url == const.LOGIN_IN_URL  # Проверяем переход URL входа
