from selenium.webdriver.common.by import By
from selenium import webdriver
from random import randint
from ..locators import reg_name_field, \
    reg_email_field,\
    reg_password_field, \
    reg_submit_button, \
    reg_password_field_error, \
    login_header

reg_test_data = {
    "name": "Арпине",
    "email": "arpine_vardanyan_8_" + str(randint(100, 999)) + "@gmail.com",
    "password": str(randint(100000, 999999))
}

def test_try_registration_with_valid_data():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, reg_name_field).send_keys(reg_test_data['name'])
    driver.find_element(By.XPATH, reg_email_field).send_keys(reg_test_data['email'])
    driver.find_element(By.XPATH, reg_password_field).send_keys(reg_test_data['password'])

    driver.find_element(By.XPATH, reg_submit_button).click()

    driver.implicitly_wait(3)
    # Проверка, после успешной регистрации происходит редирект на страницу входа
    assert driver.find_element(By.XPATH, login_header).text == 'Вход'
    driver.quit()

reg_test_incorrect_data = {
    "name": "Арпине",
    "email": "arpine_vardanyan_8_" + str(randint(100, 999)) + "@gmail.com",
    "password": str(randint(1000, 9999))
}

def test_try_registration_with_invalid_password():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(By.XPATH, reg_name_field).send_keys(reg_test_incorrect_data['name'])
    driver.find_element(By.XPATH, reg_email_field).send_keys(reg_test_incorrect_data['email'])
    driver.find_element(By.XPATH, reg_password_field).send_keys(reg_test_incorrect_data['password'])

    driver.find_element(By.XPATH, reg_submit_button).click()

    driver.implicitly_wait(3)
    # Проверка, после ввода пароля с количеством символов меньше 6 выводится ошибка
    assert driver.find_element(By.XPATH, reg_password_field_error).text == 'Некорректный пароль'
    driver.quit()


