import pytest
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


@pytest.mark.order(3)
def test_select_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test 1")

    login = Login(driver)
    login.authorization()

    main_page = Main_page(driver)
    main_page.select_products_1()

    print("Enter Cart")
    cp = Cart_page(driver)
    cp.product_confirm()

    cip = Client_info(driver)
    cip.input_info()

    pp = Payment(driver)
    pp.click_finish_button()

    fp = Finish(driver)
    fp.finish()
    print("End of test_buy_products")
    driver.quit()


@pytest.mark.order(2)
def test_select_product_2():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test 2")

    login = Login(driver)
    login.authorization()

    main_page = Main_page(driver)
    main_page.select_products_2()

    print("Enter Cart")
    cp = Cart_page(driver)
    cp.product_confirm()

    cip = Client_info(driver)
    cip.input_info()

    pp = Payment(driver)
    pp.click_finish_button()

    fp = Finish(driver)
    fp.finish()
    print("End of test_buy_products")
    driver.quit()


@pytest.mark.order(1)
def test_select_product_3():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test 3")

    login = Login(driver)
    login.authorization()

    main_page = Main_page(driver)
    main_page.select_products_3()

    print("Enter Cart")
    cp = Cart_page(driver)
    cp.product_confirm()

    cip = Client_info(driver)
    cip.input_info()

    pp = Payment(driver)
    pp.click_finish_button()

    fp = Finish(driver)
    fp.finish()
    print("End of test_buy_products")
    driver.quit()


