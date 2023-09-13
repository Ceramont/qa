from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
user_names = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']

passwd = 'secret_sauce'


class Login():
    def __init__(self, webdr, users, passwords):
        self.driver = webdr
        self.users = users
        self.passwords = passwords

    """Метод для поиска элемента со следующими модами:
        0: Простой поиск
        1: Поиск + click()
        2: Поиск + подстановка значений из переменной load
        3: Поиск + извлечение текста внутри элемента """
    def find_el(self, xpath, mode=0, load=''):
        if mode == 0:
            return self.driver.find_element(By.XPATH, xpath)
        elif mode == 1:
            return WebDriverWait(driver, 10).until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH, xpath))).click()
        elif mode == 2:
            return self.driver.find_element(By.XPATH, xpath).send_keys(load)
        elif mode == 3:
            return self.driver.find_element(By.XPATH, xpath).text

    """Метод Авторизации"""
    def auth(self):
        for user in self.users:
            print(f"Авторизирую {user}")
            self.find_el("//input[@placeholder='Username']", 2, user)
            self.find_el("//input[@placeholder='Password']", 2, self.passwords)
            self.find_el("//input[@name='login-button']", 1)
            try:
                error_text = self.find_el("//*[@id='login_button_container']/div/form/div[3]/h3", 3)
                assert error_text == 'Epic sadface: Sorry, this user has been locked out.'
                print(f"Неожиданно,но у {user} : some problems")
                self.find_el("//*[@id='login_button_container']/div/form/div[3]/h3/button", 1)
                for i in range(len(user) + 1):
                    self.find_el("//input[@placeholder='Username']", 2, Keys.BACKSPACE)
                    self.find_el("//input[@placeholder='Password']", 2, Keys.BACKSPACE)
            except:
                self.deauth(user)

    """Метод выхода их уч. записи"""
    def deauth(self, username):
        assert self.find_el("//*[@id='header_container']/div[2]/span", 3) == 'Products'
        print(f"{username} успешно авторизован")
        print(f"Выхожу из {username}")
        self.find_el("//*[@id='react-burger-menu-btn']", 1)
        self.find_el("//*[@id='logout_sidebar_link']", 1)
        assert self.find_el("//*[@id='login_credentials']/h4", 3) == 'Accepted usernames are:'
        print(f"{username} успешно вышел")


log = Login(driver, user_names, passwd)
log.auth()
print("Тест успешно выполнен")
driver.close()