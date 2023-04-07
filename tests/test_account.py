from selenium.webdriver.common.by import By
from selenium import webdriver
from ..locators import main_logo_account_link, \
    main_constructor_account_link, \
    login_login_field, \
    login_password_field, \
    login_submit_button, \
    exit_account, \
    account_enter_button, \
    login_header

def test_open_constructor_from_login_page_by_logo_link():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(By.XPATH, main_logo_account_link).click()
    # произошел переход в конструктор
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_open_constructor_from_login_page_by_constructor_link():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(By.XPATH, main_constructor_account_link).click()
    # произошел переход в конструктор
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
    driver.quit()

def test_open_login_page_after_logout():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    # предварительно регистрируемся с этими данными
    reg_test_data = {
        "login": "arpine_vardanyan_8_123@gmail.com",
        "password": "123456"
    }

    driver.find_element(By.XPATH, login_login_field).send_keys(reg_test_data['login'])
    driver.find_element(By.XPATH, login_password_field).send_keys(reg_test_data['password'])

    driver.find_element(By.XPATH, login_submit_button).click()

    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, account_enter_button).click()

    driver.find_element(By.XPATH, exit_account).click()

    # Проверка, после выхода из личного кабинета происходит редирект на страницу входа
    assert driver.find_element(By.XPATH, login_header).text == 'Вход'
    driver.quit()
