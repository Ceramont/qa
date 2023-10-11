from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Basket_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    without_reg_button = "//*[@id='main_area']/div[4]/div/div/div[2]/div/div/a[2]"
    item_name = "//*[@id='tabs_cart']/form/table/tbody[2]/tr/td[3]/div[2]/a"
    item_price = "//*[@id='tabs_cart']/form/table/tbody[2]/tr/td[5]/div/b"

    # Getters
    def get_without_reg_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.without_reg_button)))


    # Actions
    # def input_password(self, password):
    #     self.get_password().send_keys(password)
    #     print("Input password")

    def click_without_reg_button(self):
        self.get_without_reg_button().click()
        print("Click Login Button")



    def checkout(self):
        self.driver.get(self.url)
        self.get_current_url()






