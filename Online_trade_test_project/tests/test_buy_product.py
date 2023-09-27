from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import Main_page


def test_select_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    options.page_load_strategy = 'eager'
    g = Service()
    driver = webdriver.Chrome(service=g, options=options)
    print("Start Test 1")

    mp = Main_page(driver)
    mp.get_main_page()


    print("End of test_buy_products")
    # driver.quit()


