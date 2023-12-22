from selenium.webdriver.common.by import By

from locators import locators as loc


class TestSwitchingToSections:

    # Проверка перехода к соусам по клику по разделу
    def test_switching_to_sauce(self, driver):
        driver.find_element(By.XPATH, loc.Button_switching_to_sauce).click()
        assert "current" in (driver.find_element(By.XPATH, loc.Button_switching_to_sauce).get_attribute("class"))

    # Проверка перехода к начинкам по клику по разделу
    def test_switching_to_filling(self, driver):
        driver.find_element(By.XPATH, loc.Button_switching_to_filling).click()
        assert "current" in (driver.find_element(By.XPATH, loc.Button_switching_to_filling).get_attribute("class"))

    # Проверка перехода к булкам по клику по разделу
    def test_switching_to_buns(self, driver):
        driver.find_element(By.XPATH, loc.Button_switching_to_filling).click()
        driver.find_element(By.XPATH, loc.Button_switching_to_buns).click()
        assert "current" in (driver.find_element(By.XPATH, loc.Button_switching_to_buns).get_attribute("class"))
