import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import Login


def test_select_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)
    print("Start Test")
    login = Login(driver)
    login.authorization()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a [@class='shopping_cart_link']"))).click()
    print("Enter Cart")




