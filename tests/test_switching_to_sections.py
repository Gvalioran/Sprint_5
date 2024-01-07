from selenium.webdriver.common.by import By

from locators import locators as loc


class TestSwitchingToSections:

    # Проверка перехода к соусам по клику по разделу
    def test_switching_to_sauce(self, driver):
        driver.find_element(By.XPATH, loc.BUTTON_SWITCHING_TO_SAUCE).click()  # Переходим на вкладку соусы
        assert "current" in driver.find_element(By.XPATH, loc.BUTTON_SWITCHING_TO_SAUCE).get_attribute("class")
        # Проверяем что переход сработал

    # Проверка перехода к начинкам по клику по разделу
    def test_switching_to_filling(self, driver):
        driver.find_element(By.XPATH, loc.BUTTON_SWITCHING_TO_FILLING).click()  # Переходим на вкладку начинка
        assert "current" in driver.find_element(By.XPATH, loc.BUTTON_SWITCHING_TO_FILLING).get_attribute("class")
        # Проверяем что переход сработал

    # Проверка перехода к булкам по клику по разделу
    def test_switching_to_buns(self, driver):
        driver.find_element(By.XPATH, loc.BUTTON_SWITCHING_TO_FILLING).click()  # Переходим на вкладку начинка
        driver.find_element(By.XPATH, loc.BUTTON_SWITCHING_TO_BUNS).click()  # Переходим обратно на вкладку булки
        assert "current" in driver.find_element(By.XPATH, loc.BUTTON_SWITCHING_TO_BUNS).get_attribute("class")
        # Проверяем что переход сработал
