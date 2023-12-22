from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import locators as loc


class TestsLoginChecks:

    # Проверка входа по кнопке «Войти в аккаунт» на главной
    def test_login_account_button(self, driver):
        driver.find_element(By.XPATH, loc.Login_to_account).click()
        driver.find_element(By.XPATH, loc.Login_Email_input_field).send_keys(loc.Test_email)
        driver.find_element(By.XPATH, loc.Login_Password_input_field).send_keys(loc.Password)
        driver.find_element(By.XPATH, loc.Enter_to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, loc.Place_an_order)))
        assert (driver.find_element(By.XPATH, loc.Place_an_order).text == "Оформить заказ")

    # Проверка входа через кнопку «Личный кабинет»
    def test_login_account_personal_area_button(self, driver):
        driver.find_element(By.XPATH, loc.Personal_Area_button).click()
        driver.find_element(By.XPATH, loc.Login_Email_input_field).send_keys(loc.Test_email)
        driver.find_element(By.XPATH, loc.Login_Password_input_field).send_keys(loc.Password)
        driver.find_element(By.XPATH, loc.Enter_to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, loc.Place_an_order)))
        assert (driver.find_element(By.XPATH, loc.Place_an_order).text == "Оформить заказ")

    # Проверка входа через кнопку в форме регистрации
    def test_login_account_registration_page(self, driver):
        driver.find_element(By.XPATH, loc.Personal_Area_button).click()
        driver.find_element(By.XPATH, loc.Register_button).click()
        driver.find_element(By.XPATH, loc.Login_Email_input_field).send_keys(loc.Test_email)
        driver.find_element(By.XPATH, loc.Login_Password_input_field).send_keys(loc.Password)
        driver.find_element(By.XPATH, loc.Enter_to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, loc.Place_an_order)))
        assert (driver.find_element(By.XPATH, loc.Place_an_order).text == "Оформить заказ")

    # Проверка входа через кнопку в форме восстановления пароля
    def test_login_account_recover_password(self, driver):
        driver.find_element(By.XPATH, loc.Personal_Area_button).click()
        driver.find_element(By.XPATH, loc.Recover_password).click()
        driver.find_element(By.XPATH, loc.Button_remembered_the_password).click()
        driver.find_element(By.XPATH, loc.Login_Email_input_field).send_keys(loc.Test_email)
        driver.find_element(By.XPATH, loc.Login_Password_input_field).send_keys(loc.Password)
        driver.find_element(By.XPATH, loc.Enter_to_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, loc.Place_an_order)))
        assert (driver.find_element(By.XPATH, loc.Place_an_order).text == "Оформить заказ")
