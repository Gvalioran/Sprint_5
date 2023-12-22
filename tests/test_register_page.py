from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import locators as loc


class TestsRegisterPage:

    # Проверка ограничения регистрации без имени
    def test_register_account_not_name(self, driver, generate_an_account):
        driver.find_element(By.XPATH, loc.Personal_Area_button).click()
        driver.find_element(By.XPATH, loc.Go_to_registration_page_button).click()
        driver.find_element(By.XPATH, loc.Email_input_field).send_keys(generate_an_account[1])
        driver.find_element(By.XPATH, loc.Password_input_field).send_keys(generate_an_account[2])
        driver.find_element(By.XPATH, loc.Register_button).click()
        assert driver.current_url == loc.registration_url

    # Проверка ограничения регистрации с некорректным форматом почты
    def test_register_account_invalid_mail_format(self, driver, generate_an_account):
        driver.find_element(By.XPATH, loc.Personal_Area_button).click()
        driver.find_element(By.XPATH, loc.Go_to_registration_page_button).click()
        driver.find_element(By.XPATH, loc.Name_input_field).send_keys(generate_an_account[0])
        driver.find_element(By.XPATH, loc.Email_input_field).send_keys(generate_an_account[0])
        driver.find_element(By.XPATH, loc.Password_input_field).send_keys(generate_an_account[2])
        driver.find_element(By.XPATH, loc.Register_button).click()
        assert driver.current_url == loc.registration_url

    # Проверка ограничения регистрации с некорректным форматом пароля
    def test_register_account_invalid_password_format(self, driver, generate_an_account):
        driver.find_element(By.XPATH, loc.Personal_Area_button).click()
        driver.find_element(By.XPATH, loc.Go_to_registration_page_button).click()
        driver.find_element(By.XPATH, loc.Name_input_field).send_keys(generate_an_account[0])
        driver.find_element(By.XPATH, loc.Email_input_field).send_keys(generate_an_account[1])
        driver.find_element(By.XPATH, loc.Password_input_field).send_keys("12345")
        driver.find_element(By.XPATH, loc.Register_button).click()
        assert (driver.find_element(By.XPATH, loc.Error_invalid_password_field).text == "Некорректный пароль")

    # Проверка регистрации с корректными данными
    def test_register_valid_account(self, driver, generate_an_account):
        driver.find_element(By.XPATH, loc.Personal_Area_button).click()
        driver.find_element(By.XPATH, loc.Go_to_registration_page_button).click()
        driver.find_element(By.XPATH, loc.Name_input_field).send_keys(generate_an_account[0])
        driver.find_element(By.XPATH, loc.Email_input_field).send_keys(generate_an_account[1])
        driver.find_element(By.XPATH, loc.Password_input_field).send_keys(generate_an_account[2])
        driver.find_element(By.XPATH, loc.Register_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, loc.Recover_password)))
        assert (driver.find_element(By.XPATH, loc.Recover_password).text == "Восстановить пароль")
