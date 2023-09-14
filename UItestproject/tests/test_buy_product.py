import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info
from pages.login_page import Login
from pages.main_page import Main_page


def test_select_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test")

    login = Login(driver)
    login.authorization()

    main_page = Main_page(driver)
    main_page.select_product()

    print("Enter Cart")
    cp = Cart_page(driver)
    cp.product_confirm()

    cip = Client_info(driver)
    cip.input_info()



