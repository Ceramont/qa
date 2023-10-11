from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Smartphone_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    availability_now_checkbox = "//*[@id='l1d2185d7198ca866f057607628f90f1e']/span[1]"
    discount_promo_price_checkbox = "//*[@id='lebb67a4271abe715344471b0f16321f6']/span[1]"
    manufacturer_XIAOMI_checkbox = "//*[@id='l46435b29b8bf4dd5d73b4a4fa25f3e50']/span[1]"
    price_menu = "//form[@id='search_form_id']/div/div[5]/div[1]"
    left_border_price_input = "//input[@id='price1']" # 10000
    right_border_price_input = "//input[@id='price2']" # 11000
    rate_menu = "//form[@id='search_form_id']/div/div[6]/div[1]"
    rate_five_checkbox = "//*[@id='lf7c90596d2b3675b0f1cd96316dc4245']/span[1]"
    platform_android_checkbox = "//*[@id='l8f79dda83ca97aa859634f97ba399dc7']/span[1]"
    lte_yes_checkbox = "//*[@id='lcf115de5209c6087965fdc15299c1c8b']/span[1]"
    screen_diagonal_left_border = "//input[@id='diagonal1']" #5
    screen_diagonal_right_border = "//input[@id='diagonal2']" #7
    cpu_cores_menu = "//div[@id='columnBlock__2312filter__ID']/div[1]"
    cpu_cores_8_checkbox = "//*[@id='la0e1864461da8948a9a483528659acdb']/span[1]"
    ram_menu = "//div[@id='columnBlock__2317filter__ID']/div[1]"
    ram_4_checkbox = "//*[@id='l8a349126efc646d67ce37d1639c23c7d']/span[1]"
    rom_menu = "//div[@id='columnBlock__102filter__ID']/div[1]"
    rom_128_checkbox = "//*[@id='l77edb32393ed9592a633d06859632e56']/span[1]"
    camera_menu = "//div[@id='columnBlock__98filter__ID']/div[1]"
    camera_50plus00dot8 = "//input[@id='fe559e04f9e10802dae0a4005cfa3a0cf']"
    nfc_checkbox = "//*[@id='l062993585a465aecb861561818225523']/span[1]"
    color_menu = "//*[@id='columnBlock__4805filter__ID']/div[1]"
    color_black_checkbox = "//*[@id='lf7db97e847b201c1a4f0627f817f3b72']/span[1]"
    result_item = "//*[@id='item_container_2655519__ID']/div[2]/div[2]/a"
    final_button = "//*[@id='search_form_id']/div/div[26]/a[1]"
    buy_button = "//*[@id='item_container_2655519__ID']/div[3]/div[3]/a"
    checkout_button = "//*[@id='js__popup_addedToCart__cartLinkID']"
    # Getters
    def get_availability_now_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.availability_now_checkbox)))

    def get_discount_promo_price_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.discount_promo_price_checkbox)))

    def get_manufacturer_XIAOMI_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.manufacturer_XIAOMI_checkbox)))

    def get_price_menu(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.price_menu)))

    def get_left_border_price_input(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.left_border_price_input)))

    def get_right_border_price_input(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.right_border_price_input)))

    def get_rate_menu(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.rate_menu)))

    def get_rate_five_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.rate_five_checkbox)))

    def get_platform_android_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.platform_android_checkbox)))

    def get_lte_yes_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.lte_yes_checkbox)))

    def get_screen_diagonal_left_border(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.screen_diagonal_left_border)))

    def get_screen_diagonal_right_border(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.screen_diagonal_right_border)))

    def get_cpu_cores_menu(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cpu_cores_menu)))

    def get_cpu_cores_8_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.cpu_cores_8_checkbox)))

    def get_ram_menu(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ram_menu)))

    def get_ram_4_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ram_4_checkbox)))

    def get_rom_menu(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.rom_menu)))

    def get_rom_128_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.rom_128_checkbox)))

    def get_camera_menu(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.camera_menu)))

    def get_camera_50plus00dot8(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.camera_50plus00dot8)))

    def get_nfc_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.nfc_checkbox)))

    def get_color_menu(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.color_menu)))

    def get_color_black_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.color_black_checkbox)))

    def get_final_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.final_button)))

    def get_result_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.result_item)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions

    def click_availability_now_checkbox(self):
        self.get_availability_now_checkbox().click()
        print("Click availability = now checkbox")

    def click_discount_promo_price_checkbox(self):
        self.get_discount_promo_price_checkbox().click()
        print("Click promo price checkbox")

    def click_manufacturer_XIAOMI_checkbox(self):
        self.get_manufacturer_XIAOMI_checkbox().click()
        print("Click XIAOMI checkbox")

    def click_price_menu(self):
        self.get_price_menu().click()
        print("Click price_menu Button")

    def input_left_border_price_input(self, key):
        for i in range(15):
            self.get_left_border_price_input().send_keys(Keys.BACKSPACE)
        self.get_left_border_price_input().send_keys(key)
        print("Input left border price")

    def input_right_border_price_input(self, key):
        for i in range(15):
            self.get_right_border_price_input().send_keys(Keys.BACKSPACE)
        self.get_right_border_price_input().send_keys(key)
        print("Input left border price")

    def click_rate_menu(self):
        self.get_rate_menu().click()
        print("Click rate menu")

    def click_rate_five_checkbox(self):
        self.get_rate_five_checkbox().click()
        print("Click five rate")

    def click_platform_android_checkbox(self):
        self.get_platform_android_checkbox().click()
        print("Click Android")

    def click_lte_yes_checkbox(self):
        self.get_lte_yes_checkbox().click()
        print("Click Lte yes")

    def input_screen_diagonal_left_border(self, key):
        for i in range(15):
            self.get_screen_diagonal_left_border().send_keys(Keys.BACKSPACE)
        self.get_screen_diagonal_left_border().send_keys(key)
        print("Input left border diag")

    def input_screen_diagonal_right_border(self, key):
        for i in range(15):
            self.get_screen_diagonal_right_border().send_keys(Keys.BACKSPACE)
        self.get_screen_diagonal_right_border().send_keys(key)
        print("Input right border diag")

    def click_cpu_cores_menu(self):
        self.get_cpu_cores_menu().click()
        print("Click cpu cores menu")

    def click_cpu_cores_8_checkbox(self):
        self.get_cpu_cores_8_checkbox().click()
        print("Click cores 8")

    def click_ram_menu(self):
        self.get_ram_menu().click()
        print("Click ram menu")

    def click_ram_4_checkbox(self):
        self.get_ram_4_checkbox().click()
        print("Click 4 GB")

    def click_rom_menu(self):
        self.get_rom_menu().click()
        print("Click rom menu")

    def click_rom_128_checkbox(self):
        self.get_rom_128_checkbox().click()
        print("Click 128 GB")

    def click_camera_menu(self):
        self.get_camera_menu().click()
        print("Click Camera menu")

    def click_camera_50plus00dot8(self):
        self.get_camera_50plus00dot8().click()
        print("Click 50+0.08")

    def click_nfc_checkbox(self):
        self.get_nfc_checkbox().click()
        print("Click nfc checkbox")

    def click_color_menu(self):
        self.get_color_menu().click()
        print("Click color menu")

    def click_color_black_checkbox(self):
        self.get_color_black_checkbox().click()
        print("Click color black menu")

    def click_final_button(self):
        self.get_final_button().click()
        print("Click final Button")

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Click buy Button")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout Button")


    def get_filter_result(self):
        self.get_current_url()

        self.click_availability_now_checkbox()
        # self.click_discount_promo_price_checkbox()
        self.click_manufacturer_XIAOMI_checkbox()
        self.click_price_menu()
        self.input_left_border_price_input(10000)
        self.input_right_border_price_input(15000)
        self.click_rate_menu()
        self.click_rate_five_checkbox()
        self.click_platform_android_checkbox()
        self.click_lte_yes_checkbox()
        self.input_screen_diagonal_left_border(5)
        self.input_screen_diagonal_right_border(7)
        self.click_cpu_cores_menu()
        self.click_cpu_cores_8_checkbox()
        self.click_ram_menu()
        self.click_ram_4_checkbox()
        self.click_rom_menu()
        self.click_rom_128_checkbox()
        self.click_camera_menu()
        # self.click_camera_50plus00dot8()
        self.click_nfc_checkbox()
        self.click_color_menu()
        self.click_color_black_checkbox()
        self.click_final_button()
        self.assert_word(self.get_result_item(), "Xiaomi Redmi 12 4/128GB Черный")
        self.click_buy_button()
        self.click_checkout_button()

