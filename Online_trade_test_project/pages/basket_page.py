from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Basket_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    without_reg_button = "//*[@id='main_area']/div[4]/div/div/div[2]/div/div/a[2]"
    item_name = "//*[@id='tabs_cart']/form/table/tbody[2]/tr/td[3]/div[2]/a"
    item_price = "//*[@id='tabs_cart']/form/table/tbody[2]/tr/td[5]/div/b"
    final_button = "//*[@id='main_area']/div[4]/div/form/div[2]/input"
    address_area = "//*[@id='address']"
    contact_name = "//*[@id='contact__ID']"
    contact_phone = "//*[@id='cellphone__ID']"
    contact_email = "//*[@id='email__ID']"

    # Getters
    def get_without_reg_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.without_reg_button)))

    def get_item_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.item_name)))

    def get_item_price(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.item_price)))

    def get_final_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.final_button)))

    def get_address_area(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.address_area)))

    def get_contact_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.contact_name)))

    def get_contact_phone(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.contact_phone)))

    def get_contact_email(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.contact_email)))

    # Actions
    def click_without_reg_button(self):
        self.get_without_reg_button().click()
        print("Click without registration Button")

    def click_final_button(self):
        self.get_final_button().click()
        print("Click final Button")

    def input_address_area(self, key):
        self.get_address_area().send_keys(key)
        print("Input address")

    def input_contact_name(self, key):
        self.get_contact_name().send_keys(key)
        print("Input name")

    def input_contact_phone(self, key):
        self.get_contact_phone().send_keys(key)
        print("Input phone")

    def input_contact_email(self, key):
        self.get_contact_email().send_keys(key)
        print("Input email")

    def checkout(self):
        self.get_current_url()
        self.click_without_reg_button()
        self.assert_word(self.get_item_name(), "Смартфон Xiaomi Redmi 12 4/128GB Черный")
        self.assert_word(self.get_item_price(), "13 990 ₽")
        self.click_final_button()
        self.input_address_area("Ленинградский проспект, дом. 81, кв. 77")
        self.input_contact_name("Александр")
        self.input_contact_phone("+79999999999")
        self.input_contact_email("example@email.ru")
        self.screenshot()



