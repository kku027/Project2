from selenium import webdriver
from time import sleep
import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

file = open("log.txt", "w")  # Открываем файл для записи логов
#  driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)  # Запуск без закрытия сайта
#  option.add_argument("--headless")  # Запуск без открытия сайта
driver = webdriver.Chrome(options=option)


#  End of setup

# --- Запуск сценария--- Sc functions
def set_up():
    driver.get('http://www.saucedemo.com/')  # Переход на сайт
    driver.maximize_window()  # Максимизация окна


def login():
    #  Поиск поля для ввода имени пользователя
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)  # ВВод имени пользователя
    file.write("Success write login\n")  # Запись в лог

    #  Поиск поля для ввода пароля
    user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce"
    user_pass.send_keys(password)  # ВВод пароля
    file.write("Success write password\n")  # Запись в лог

#    sleep(3)  # Небольшая задержка для устройства

    #  Поиск кнопки входа и клик по ней
    login_butt = driver.find_element(By.XPATH, '//input [@id="login-button"]')
    login_butt.click()
    file.write("Success click login\n")  # Запись в лог

def login_with_enter():
    #  Поиск поля для ввода имени пользователя
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)  # ВВод имени пользователя
    file.write("Success write login\n")  # Запись в лог

    #  Поиск поля для ввода пароля
    user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce"
    user_pass.send_keys(password)  # ВВод пароля
    file.write("Success write password\n")  # Запись в лог

    user_pass.send_keys(Keys.ENTER)
    file.write("Success Enter login\n")  # Запись в лог

def fake_login():
    #  Поиск поля для ввода имени пользователя
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)  # ВВод имени пользователя
    file.write("Success write login\n")  # Запись в лог

    #  Поиск поля для ввода пароля
    user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce1"
    user_pass.send_keys(password)  # ВВод пароля
    file.write("Success write fake password\n")  # Запись в лог

#    sleep(3)  # Небольшая задержка для устройства

    #  Поиск кнопки входа и клик по ней
    login_butt = driver.find_element(By.XPATH, '//input [@id="login-button"]')
    login_butt.click()
    file.write("Success click login\n")  # Запись в лог

#  def refresh_page():      # Сценарий ерезагрузки страницы
#    driver.refresh()


# --- Завершение сценария--- End of Sc functions
#  ---------Tests----------
def test_login_redirect():
    correct_url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url

    assert correct_url == get_url, "test_login_redirect is Failed"
    file.write("test_login_redirect is OK \n")  # Запись в лог


def test_context_after_login_is_correct():  # Тест на корректный ввод
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    driver.save_screenshot(f"sc-real-login\\screenshot_test_context_after_login_is_correct_"
                           f"{datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")}.png")

    assert correct_text == current_text.text, "test_context_after_login_is_correct is Failed"
    file.write("test_context_after_login_is_correct is OK \n")  # Запись в лог


def test_fake_login_label():  # Тест на неверный ввод
    correct_text = "Epic sadface: Username and password do not match any user in this service"
    current_text = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    assert correct_text == current_text.text, "test_fake_login_label is Failed"
    file.write('test_fake_login_label is OK \n')  # Запись в лог


# End of tests

sleep(5)  # Небольшая задержка чтобы увидеть результат


#  Закрытие файла и завершение работы с драйвером
# --- Завершение сценария Sc_functions
def sc_real_login():  # Запуск сценария--sc_real_login()
    set_up()
    login()

    test_login_redirect()
    test_context_after_login_is_correct()

def sc_real_login_with_enter():  # Запуск сценария--sc_real_login_with_enter()
    set_up()
    login()

    test_login_redirect()
    test_context_after_login_is_correct()



def sc_fake_login():  # Запуск сценария--sc_fake_login()
    set_up()
    fake_login()
#    sleep(2)
#    refresh_page()     # Запуск перезагрузки страницы

    test_fake_login_label()

#  set_up()
#  user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
#  login = "standard_user"
#  user_name.send_keys(login)
#  sleep(2)
#  user_name.send_keys(Keys.CONTROL + 'a')


sc_real_login_with_enter()
#  sc_fake_login()
#  sc_real_login()
file.close()