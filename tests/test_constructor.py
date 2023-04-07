from selenium.webdriver.common.by import By
from selenium import webdriver
from ..locators import constructor_bun, \
    constructor_sauce, \
    constructor_filling

def test_open_sauce_section():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, constructor_sauce).click()

    driver.implicitly_wait(3)
    # Проверка, активный раздел должен быть помечен классом current
    assert 'current' in driver.find_element(By.XPATH, constructor_sauce).get_attribute('class')
    driver.quit()

def test_open_filling_section():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, constructor_filling).click()
    # Проверка, активный раздел должен быть помечен классом current
    driver.implicitly_wait(3)
    assert 'current' in driver.find_element(By.XPATH, constructor_filling).get_attribute('class')
    driver.quit()

def test_open_bun_section_after_open_sauce_section():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, constructor_sauce).click()
    driver.find_element(By.XPATH, constructor_bun).click()
    # Проверка, активный раздел должен быть помечен классом current
    assert 'current' in driver.find_element(By.XPATH, constructor_bun).get_attribute('class')
    driver.quit()