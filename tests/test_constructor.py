from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import constructor_bun, \
    constructor_sauce, \
    constructor_filling

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, constructor_sauce).click()

driver.implicitly_wait(3)
# Проверка, активный раздел должен быть помечен классом current
assert 'current' in driver.find_element(By.XPATH, constructor_sauce).get_attribute('class')

driver.find_element(By.XPATH, constructor_filling).click()
# Проверка, активный раздел должен быть помечен классом current
assert 'current' in driver.find_element(By.XPATH, constructor_filling).get_attribute('class')

driver.find_element(By.XPATH, constructor_bun).click()
# Проверка, активный раздел должен быть помечен классом current
assert 'current' in driver.find_element(By.XPATH, constructor_bun).get_attribute('class')
driver.quit()