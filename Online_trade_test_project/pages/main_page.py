from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    url = 'https://www.onlinetrade.ru/'

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    unblock_button = "//input[@id='otv3_submit']"
    catalog_menu = "//a[@title='Каталог товаров']"
    catalog_menu_smartphone = "//a[@href='/catalogue/smartfony-c13/']"
    cookie_submit = "//a[@class = 'button button__blue js__cookiePanel__button']"

    # Getters
    def get_unblock_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.unblock_button)))

    def get_cat_menu(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_menu)))

    def get_smartphone(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_menu_smartphone)))

    def get_cookie_submit(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cookie_submit)))

    # Actions

    def click_unblock_button(self):
        self.get_unblock_button().click()
        print("Click Login Button")

    def click_cat_menu(self):
        self.get_cat_menu().click()
        print("Click Catalog menu Button")

    def click_smartphone(self):
        self.get_smartphone().click()
        print("Click Catalog menu Smartphone Button")

    def click_cookie_submit(self):
        self.get_cookie_submit().click()
        print("Click Ccookie submit Button")

    def get_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        try:
            self.get_unblock_button()
            self.click_unblock_button()
        except Exception:
            self.click_cookie_submit()
            self.click_cat_menu()
            self.click_smartphone()





