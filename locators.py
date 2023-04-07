# Локаторы

# Регистрация

reg_name_field = './/form/fieldset[1]//input' # Поле ввода логина
reg_email_field = './/form/fieldset[2]//input' # Поле ввода e-mail
reg_password_field = './/form/fieldset[3]//input' # Поле ввода пароля
reg_password_field_error = ".//form/fieldset[3]//p[contains(@class,'input__error')]" # Вывод ошибки для поля с паролем
reg_submit_button = './/form//button' # Кнопка Зарегистрироваться
reg_error_message = ".//form/following-sibling::p[contains(@class,'input__error')]" # Вывод общей ошибки

# Вход

login_header = ".//h2[text()='Вход']" # Заголовок страницы входа
login_login_field = './/form/fieldset[1]//input' # Поле ввода логина
login_password_field = './/form/fieldset[2]//input' # Поле ввода пароля
login_submit_button = './/form//button' # Кнопка Зарегистрироваться

# Главная

main_account_enter_button = './/button[text() = "Войти в аккаунт"]' # Кнопка Войти в аккаунт
main_logo_account_link = ".//div[contains(@class,'logo')]/a[@href='/']" # Ссылка на логотипе
main_constructor_account_link = ".//ul[contains(@class,'header__list')]/li[1]/a[@href='/']" # Ссылка на кнопке Конструктор
account_enter_button = './/a[@href="/account"]'  # вход через кнопку «Личный кабинет»,

# Личный кабинет
exit_account = ".//button[text()='Выход']" # Выход из ЛК

# Форма регистрации

registration_account_enter = './/a[@href="/login"]' # вход через кнопку в форме регистрации,

# Восстановление пароля

restore_account_enter = './/a[@href="/login"]' # вход через кнопку в форме восстановления пароля.

# Конструктор

constructor_bun = ".//div[contains(@class,'tab_tab')][1]" # Кнопка булки
constructor_sauce = ".//div[contains(@class,'tab_tab')][2]" # Кнопка соусы
constructor_filling = ".//div[contains(@class,'tab_tab')][3]" # Кнопка начинки