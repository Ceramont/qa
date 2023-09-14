from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Client_info(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name = "//*[@id='first-name']"
    second_name = "//*[@id='last-name']"
    zip_code = "//*[@id='postal-code']"
    confirm_button = "//*[@id='continue']"

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_second_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.second_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_confirm_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_button)))

    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("input first name")

    def input_second_name(self, second_name):
        self.get_second_name().send_keys(second_name)
        print("input second name")

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("input zip-code")

    def click_confirm_button(self):
        self.get_confirm_button().click()
        print("Click confirm Button")

    def input_info(self):
        self.get_current_url()
        self.input_first_name("Ivan")
        self.input_second_name("Ivanov")
        self.input_zip_code("1000")
        self.click_confirm_button()
