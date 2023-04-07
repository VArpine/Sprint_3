from selenium.webdriver.common.by import By
from selenium import webdriver
from ..locators import main_account_enter_button, \
    account_enter_button, \
    registration_account_enter, \
    restore_account_enter

def test_open_login_page_by_personal_account_button_click():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, main_account_enter_button).click()

    driver.implicitly_wait(3)
    # произошел переход в лк
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()

def test_open_login_page_by_personal_account_link_click():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, account_enter_button).click()

    driver.implicitly_wait(3)
    # произошел переход в лк
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()

def test_open_login_page_from_registration_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, registration_account_enter).click()

    driver.implicitly_wait(3)
    # произошел переход в лк
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()

def test_open_login_page_from_forgot_password_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    driver.find_element(By.XPATH, restore_account_enter).click()

    driver.implicitly_wait(3)
    # произошел переход в лк
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
    driver.quit()