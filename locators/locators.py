# Sprint_5
# Список локаторов для страницы https://stellarburgers.nomoreparties.site/

# Кнопки
PERSONAL_AREA_BUTTON = ".//*[@href='/account']"  # Кнопка личного кабинета
REGISTRATION_PAGE_BUTTON = ".//*[@href='/register']"  # Кнопка перехода к регистрации нового пользователя
REGISTER_BUTTON = ".//*[text()='Зарегистрироваться']"  # Кнопка зарегистрироваться
LOGIN_TO_ACCOUNT = ".//*[text()='Войти в аккаунт']"  # Кнопка перехода к странице входа в аккаунт
ENTER_TO_ACCOUNT = ".//button[text()='Войти']"  # Кнопка войти в аккаунт
ENTER_TO_ACCOUNT_LINK = ".//*[@href='/login']" # Кнопка войти в форме для регистрации
PLACE_AN_ORDER = ".//*[text()='Оформить заказ']"  # Кнопка оформить заказ
RECOVER_PASSWORD = ".//*[text()='Восстановить пароль']"  # Кнопка восстановить пароль
BUTTON_REMEMBERED_THE_PASSWORD = ".//a[text()='Войти']"  # Кнопка входа вспомнил пароль
EXIT_BUTTON = ".//*[text()='Выход']"  # Кнопка выхода из личного кабинета
BUTTON_CONSTRUCTOR = ".//*[text()='Конструктор']"  # Кнопка входа в конструктор
LOGO = ".//*[@class='AppHeader_header__logo__2D0X2']"
BUTTON_SWITCHING_TO_SAUCE = ".//section[1]/div[1]/div[2]"  # Кнопка перехода в раздел соусов
BUTTON_SWITCHING_TO_FILLING = ".//section[1]/div[1]/div[3]"  # Кнопка перехода в раздел начинок
BUTTON_SWITCHING_TO_BUNS = ".//section[1]/div[1]/div[1]"  # Кнопка перехода в раздел булок

# Поля для ввода
NAME_INPUT_FIELD = ".//fieldset[1]/*/*/*[@name='name']"  # Поле ввода Имени при регистрации
EMAIL_INPUT_FIELD = ".//fieldset[2]/*/*/*[@name='name']"  # Поле ввода Email при регистрации
PASSWORD_INPUT_FIELD = ".//*[@type='password']"  # Поле ввода пароля при регистрации
LOGIN_EMAIL_INPUT_FIELD = ".//*[@name='name']"  # Поле ввода Email для входа в аккаунт
LOGIN_PASSWORD_INPUT_FIELD = ".//*[@name='Пароль']"  # Поле ввода пароля для входа в аккаунт

# Поля для вывода
ERROR_INVALID_PASSWORD_FIELD = ".//*[text()='Некорректный пароль']"  # Поле ошибки при неверном формате пароля
