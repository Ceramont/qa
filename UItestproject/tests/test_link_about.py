import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info
from pages.finish_page import Finish
from pages.login_page import Login
from pages.main_page import Main_page
from pages.payment_page import Payment


def test_link_about():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test")

    login = Login(driver)
    login.authorization()

    main_page = Main_page(driver)
    main_page.select_menu_about()

    print("End of test_link_about")
    driver.quit()



