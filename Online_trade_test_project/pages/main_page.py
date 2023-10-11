from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    url = 'https://www.onlinetrade.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    unblock_button = "//input[@id='otv3_submit']"
    catalog_menu = "//div[@id='main_area']/div[2]/div/div/div[2]/a[1]"
    catalog_menu_smartphone = "//ul[@id='ssCM_2325_ID']/li[1]/a"

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

    # Actions
    # def input_password(self, password):
    #     self.get_password().send_keys(password)
    #     print("Input password")

    def click_unblock_button(self):
        self.get_unblock_button().click()
        print("Click Login Button")

    def click_cat_menu(self):
        self.get_cat_menu().click()
        print("Click Catalog menu Button")

    def click_smartphone(self):
        self.get_smartphone().click()
        print("Click Catalog menu Smartphone Button")

    def get_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        try:
            self.get_unblock_button()
            self.click_unblock_button()
        except Exception:
            self.click_cat_menu()
            self.click_smartphone()





