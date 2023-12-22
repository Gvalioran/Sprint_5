from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import locators as loc


class TestsLoginChecks:

    # Проверка перехода по клику на «Личный кабинет»
    def test_login_account_button(self, driver):
        driver.find_element(By.XPATH, loc.Login_to_account).click()
        driver.find_element(By.XPATH, loc.Login_Email_input_field).send_keys(loc.Test_email)
        driver.find_element(By.XPATH, loc.Login_Password_input_field).send_keys(loc.Password)
        driver.find_element(By.XPATH, loc.Enter_to_account).click()
        driver.find_element(By.XPATH, loc.Personal_Area_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, loc.Exit_button)))
        assert driver.find_element(By.XPATH, loc.Exit_button).text == "Выход"

    # Проверка перехода по клику на «Конструктор»
    def test_switching_to_constructor(self, driver):
        driver.find_element(By.XPATH, loc.Login_to_account).click()
        driver.find_element(By.XPATH, loc.Login_Email_input_field).send_keys(loc.Test_email)
        driver.find_element(By.XPATH, loc.Login_Password_input_field).send_keys(loc.Password)
        driver.find_element(By.XPATH, loc.Enter_to_account).click()
        driver.find_element(By.XPATH, loc.Personal_Area_button).click()
        driver.find_element(By.XPATH, loc.Button_constructor).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, loc.Place_an_order)))
        assert (driver.find_element(By.XPATH, loc.Place_an_order).text == "Оформить заказ")

    # Проверка перехода по клику на логотип Stellar Burgers
    def test_switching_to_constructor_through_logo(self, driver):
        driver.find_element(By.XPATH, loc.Login_to_account).click()
        driver.find_element(By.XPATH, loc.Login_Email_input_field).send_keys(loc.Test_email)
        driver.find_element(By.XPATH, loc.Login_Password_input_field).send_keys(loc.Password)
        driver.find_element(By.XPATH, loc.Enter_to_account).click()
        driver.find_element(By.XPATH, loc.Personal_Area_button).click()
        driver.find_element(By.XPATH, loc.Logo).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, loc.Place_an_order)))
        assert (driver.find_element(By.XPATH, loc.Place_an_order).text == "Оформить заказ")

    # Проверка выхода по кнопке «Выйти» в личном кабинете
    def test_exit_account_button(self, driver):
        driver.find_element(By.XPATH, loc.Login_to_account).click()
        driver.find_element(By.XPATH, loc.Login_Email_input_field).send_keys(loc.Test_email)
        driver.find_element(By.XPATH, loc.Login_Password_input_field).send_keys(loc.Password)
        driver.find_element(By.XPATH, loc.Enter_to_account).click()
        driver.find_element(By.XPATH, loc.Personal_Area_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, loc.Exit_button)))
        driver.find_element(By.XPATH, loc.Exit_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, loc.Enter_to_account)))
        assert driver.find_element(By.XPATH, loc.Enter_to_account).text == "Войти"
